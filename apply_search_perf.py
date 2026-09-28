#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
apply_search_perf.py

Aplica las optimizaciones de rendimiento del buscador de archivos sobre el
proyecto "agente" (DeepSeek Code Packager).

Cambios aplicados
-----------------
  1. app/core/project_scanner.py
     - Firma de invalidación recursiva (raíz + subdirectorios de primer nivel)
       para evitar devolver caché obsoleta cuando cambian archivos en subcarpetas.

  2. app/core/storage/database.py
     - Nuevo método `load_file_paths()` para lectura ligera desde SQLite.

  3. app/gui/file_search_dialog.py
     - BATCH_SIZE reducido de 100 → 25.
     - Nuevo RENDER_BATCH_DELAY_MS = 15 (antes 1 ms).
     - `_refresh_results` agenda la primera tanda con `after(0, ...)` en vez de
       renderizar sincrónicamente.
     - `_render_batch` usa RENDER_BATCH_DELAY_MS entre tandas.
     - `_load_files` y `_async_scan_worker` ahora consultan SQLite primero
       (DB-first) y caen a `os.walk` sólo si la DB no tiene datos.
     - `_check_scan_queue` maneja la tupla de 3 elementos (sid, files, source).
     - Nuevo botón "↻ Refrescar" para forzar reescaneo desde disco.

Uso:
    python3 apply_search_perf.py /ruta/al/proyecto
    python3 apply_search_perf.py                 # directorio actual
    python3 apply_search_perf.py --dry-run       # sólo muestra

Idempotente: ejecutarlo varias veces no duplica cambios.
Sólo usa la biblioteca estándar de Python.
"""

import argparse
import os
import shutil
import sys
import py_compile
from datetime import datetime
from pathlib import Path


# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------

BACKUP_DIRNAME = ".backup_search_perf"

STATS = {
    "modified": 0,
    "skipped":  0,
    "backups":  0,
    "errors":   0,
}

REQUIRED_FILES = [
    "app/__init__.py",
    "app/core/__init__.py",
    "app/core/project_scanner.py",
    "app/core/storage/__init__.py",
    "app/core/storage/database.py",
    "app/gui/file_search_dialog.py",
    "app/gui/main_window.py",
]


# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

def info(msg):  print(f"[INFO] {msg}")
def ok(msg):    print(f"[ OK ] {msg}");  STATS["modified"] += 1
def skip(msg):  print(f"[SKIP] {msg}");  STATS["skipped"] += 1
def warn(msg):  print(f"[WARN] {msg}")
def error(msg): print(f"[FAIL] {msg}");  STATS["errors"] += 1


# ---------------------------------------------------------------------------
# Helpers de I/O
# ---------------------------------------------------------------------------

def ensure_target_exists(root: Path, rel_path: str) -> Path:
    p = root / rel_path
    if not p.is_file():
        raise RuntimeError(f"Archivo objetivo no encontrado: {p}")
    return p


def backup_file(root: Path, rel_path: str) -> None:
    src = root / rel_path
    if not src.is_file():
        return
    dst = root / BACKUP_DIRNAME / rel_path
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    STATS["backups"] += 1
    info(f"Backup creado: {dst.relative_to(root)}")


def _apply_change(root: Path, rel_path: str, new_content: str) -> None:
    backup_file(root, rel_path)
    (root / rel_path).write_text(new_content, encoding="utf-8")
    ok(f"Cambio aplicado: {rel_path}")


def replace_exact(root: Path, rel_path: str, old: str, new: str,
                  marker_check: str = None) -> None:
    """Reemplaza `old` por `new` si `old` está presente.

    `marker_check`: subcadena que, si ya está presente en el archivo,
    indica que el cambio ya fue aplicado (idempotencia).
    """
    path = root / rel_path
    content = path.read_text(encoding="utf-8")

    if marker_check and marker_check in content:
        skip(f"{rel_path}: cambio ya aplicado (marcador presente)")
        return

    if old not in content:
        warn(f"{rel_path}: patrón no encontrado (posible versión distinta)")
        STATS["skipped"] += 1
        return

    new_content = content.replace(old, new, 1)
    _apply_change(root, rel_path, new_content)


def insert_before(root: Path, rel_path: str, anchor: str,
                  block: str, marker_check: str) -> None:
    """Inserta `block` antes de `anchor` en el archivo."""
    path = root / rel_path
    content = path.read_text(encoding="utf-8")

    if marker_check and marker_check in content:
        skip(f"{rel_path}: cambio ya aplicado (marcador presente)")
        return

    idx = content.find(anchor)
    if idx == -1:
        raise RuntimeError(f"Ancla no encontrada en {rel_path}:\n  {anchor!r}")

    new_content = content[:idx] + block + content[idx:]
    _apply_change(root, rel_path, new_content)


def append_if_missing(root: Path, rel_path: str, block: str,
                      marker_check: str) -> None:
    """Añade `block` al final del archivo si `marker_check` no está presente."""
    path = root / rel_path
    content = path.read_text(encoding="utf-8")

    if marker_check and marker_check in content:
        skip(f"{rel_path}: cambio ya aplicado (marcador presente)")
        return

    if not content.endswith("\n"):
        content += "\n"
    new_content = content + block
    _apply_change(root, rel_path, new_content)


# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Contenido: PATCH 1 — app/core/project_scanner.py
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

SCANNER_OLD_SIGNATURE = '''    folder_mtime = 0.0
    try:
        folder_mtime = os.path.getmtime(abs_folder)
    except OSError:
        pass

    if use_cache and not force_refresh:
        with _cache_lock:
            if cache_key in _SCAN_CACHE:
                cached_mtime, cached_files = _SCAN_CACHE[cache_key]
                if cached_mtime == folder_mtime:
                    return list(cached_files)
'''

SCANNER_NEW_SIGNATURE = '''    # FIX: firma de invalidación recursiva ligera (raíz + subdirectorios
    # inmediatos). No es perfecta, pero evita devolver caché obsoleta cuando
    # cambian archivos dentro de subcarpetas de primer nivel, sin coste de
    # os.walk completo.
    signature = 0.0
    try:
        signature = os.path.getmtime(abs_folder)
        with os.scandir(abs_folder) as it:
            for entry in it:
                if entry.is_dir(follow_symlinks=False):
                    try:
                        signature = max(
                            signature,
                            entry.stat(follow_symlinks=False).st_mtime,
                        )
                    except OSError:
                        continue
    except OSError:
        pass

    if use_cache and not force_refresh:
        with _cache_lock:
            if cache_key in _SCAN_CACHE:
                cached_mtime, cached_files = _SCAN_CACHE[cache_key]
                if cached_mtime == signature:
                    return list(cached_files)
'''

SCANNER_OLD_STORE = "            _SCAN_CACHE[cache_key] = (folder_mtime, valid_files)"
SCANNER_NEW_STORE = "            _SCAN_CACHE[cache_key] = (signature, valid_files)"


# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Contenido: PATCH 2 — app/core/storage/database.py
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

DATABASE_ANCHOR = "    # === PHASE 2: DELTA SCAN ==="

DATABASE_NEW_METHOD = '''    def load_file_paths(self, project_path: str):
        """Devuelve lista plana de rutas de archivo (is_dir=0) ordenadas.

        Pensado para alimentar el buscador sin pagar el coste de os.walk.
        Devuelve:
            (files: List[str], last_scanned: Optional[str], exists: bool)
        donde `files` es [] si el proyecto existe pero no tiene nodos.
        """
        cur = self._conn.cursor()
        cur.execute(
            "SELECT id, last_scanned FROM projects WHERE path = ?",
            (project_path,),
        )
        row = cur.fetchone()
        if not row:
            return [], None, False
        project_id = int(row["id"])
        last_scanned = row["last_scanned"]
        cur.execute(
            "SELECT rel_path FROM nodes "
            "WHERE project_id = ? AND is_dir = 0 "
            "ORDER BY rel_path",
            (project_id,),
        )
        files = [r["rel_path"] for r in cur.fetchall()]
        return files, last_scanned, True

'''


# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Contenido: PATCH 3 — app/gui/file_search_dialog.py
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

FSD_OLD_CONSTANTS = '''MAX_RENDER_LIMIT = 500
BATCH_SIZE = 100
DEBOUNCE_MS = 150
LOADING_DELAY_MS = 200
QUEUE_CHECK_MS = 20
'''

FSD_NEW_CONSTANTS = '''MAX_RENDER_LIMIT = 500
BATCH_SIZE = 25              # 100 -> 25 : tandas más pequeñas, sin bloquear el mainloop
DEBOUNCE_MS = 150
LOADING_DELAY_MS = 200
QUEUE_CHECK_MS = 20
RENDER_BATCH_DELAY_MS = 15   # 1 -> 15 : cede el hilo entre tandas
'''


FSD_OLD_REFRESH_TAIL = '''        # Render first batch synchronously
        self._render_batch(matches_to_render, start_idx=0, total_matches=total_matches)
'''

FSD_NEW_REFRESH_TAIL = '''        # FIX: incluso la primera tanda se agenda con after(0, ...) para no
        # bloquear el hilo de la GUI dentro de _refresh_results.
        self._render_timer = self.after(
            0,
            lambda: self._render_batch(matches_to_render, 0, total_matches),
        )
'''


FSD_OLD_RENDER_TAIL = '''        if end_idx < len(matches_subset):
            # Schedule next batch
            self._render_timer = self.after(
                1, lambda: self._render_batch(matches_subset, end_idx, total_matches)
            )
'''

FSD_NEW_RENDER_TAIL = '''        if end_idx < len(matches_subset):
            # FIX: 15 ms en lugar de 1 ms para que el mainloop procese eventos
            # (redibujado, teclado, ratón) entre tandas.
            self._render_timer = self.after(
                RENDER_BATCH_DELAY_MS,
                lambda: self._render_batch(matches_subset, end_idx, total_matches),
            )
'''


FSD_OLD_LOAD_FILES = '''    def _load_files(self):
        self._scan_id += 1
        current_scan_id = self._scan_id

        # Schedule delayed loading indicator after 200ms
        self._cancel_timer("_loading_timer")
        self._loading_timer = self.after(
            LOADING_DELAY_MS, lambda: self._show_loading(current_scan_id)
        )

        # Launch background scan daemon thread
        threading.Thread(
            target=self._async_scan_worker,
            args=(current_scan_id, self.folder_path, self.excluded_dirs, self._scan_queue),
            daemon=True,
        ).start()

        # Start queue polling loop on main GUI thread
        self._schedule_queue_check()
'''

FSD_NEW_LOAD_FILES = '''    def _load_files(self, force_refresh: bool = False):
        self._scan_id += 1
        current_scan_id = self._scan_id

        # Schedule delayed loading indicator after 200ms
        self._cancel_timer("_loading_timer")
        self._loading_timer = self.after(
            LOADING_DELAY_MS, lambda: self._show_loading(current_scan_id)
        )

        # FIX: launch background worker: DB-first, os.walk fallback
        threading.Thread(
            target=self._async_scan_worker,
            args=(
                current_scan_id,
                self.folder_path,
                self.excluded_dirs,
                self._scan_queue,
                force_refresh,
            ),
            daemon=True,
        ).start()

        # Start queue polling loop on main GUI thread
        self._schedule_queue_check()
'''


FSD_OLD_CHECK_QUEUE_HEAD = '''        received = False
        latest_files = None

        while True:
            try:
                sid, files = self._scan_queue.get_nowait()
                if sid == self._scan_id:
                    latest_files = files
                    received = True
            except queue.Empty:
                break

        if received and latest_files is not None:
            self._hide_loading()
            self.all_files = latest_files
            self._files_indexed = [(f, f.lower()) for f in latest_files]
            self._refresh_results(force=True)
'''

FSD_NEW_CHECK_QUEUE_HEAD = '''        received = False
        latest_files = None
        source = None

        while True:
            try:
                sid, files, src = self._scan_queue.get_nowait()
                if sid == self._scan_id:
                    latest_files = files
                    source = src
                    received = True
            except queue.Empty:
                break

        if received and latest_files is not None:
            self._hide_loading()
            self.all_files = latest_files
            self._files_indexed = [(f, f.lower()) for f in latest_files]
            if self.lbl_loading is not None and self.winfo_exists():
                tag = "caché DB" if source == "db" else "escaneo"
                self.lbl_loading.config(
                    text=f"✓ {len(latest_files)} archivos ({tag})"
                )
            self._refresh_results(force=True)
'''


FSD_OLD_SCAN_WORKER = '''    @staticmethod
    def _async_scan_worker(scan_id: int, folder_path: str, excluded_dirs: Set[str], res_queue: queue.Queue):
        """Worker thread entry point: purely python I/O, no Tkinter calls."""
        try:
            files = scan_directory(folder_path, excluded_dirs, allowed_extensions=None)
        except Exception:
            files = []
        res_queue.put((scan_id, files))
'''

FSD_NEW_SCAN_WORKER = '''    @staticmethod
    def _async_scan_worker(
        scan_id: int,
        folder_path: str,
        excluded_dirs: Set[str],
        res_queue: queue.Queue,
        force_refresh: bool = False,
    ):
        """Worker thread entry point: DB-first con fallback a os.walk.

        Estrategia:
          1) Si !force_refresh, consultar SQLite (project_cache.db). ~1 ms.
          2) Si la DB no tiene filas o el usuario forzó refresco, os.walk.
        """
        files: List[str] = []
        source = "scan"
        try:
            from app.core.storage.database import get_database

            if not force_refresh:
                db = get_database()
                db_files, _last_scanned, exists = db.load_file_paths(folder_path)
                if exists and db_files:
                    files = db_files
                    source = "db"

            if not files:
                files = scan_directory(
                    folder_path, excluded_dirs, allowed_extensions=None
                )
                source = "scan"
        except Exception:
            # Ante cualquier fallo, caer a escaneo directo
            try:
                files = scan_directory(
                    folder_path, excluded_dirs, allowed_extensions=None
                )
            except Exception:
                files = []
            source = "scan"

        res_queue.put((scan_id, files, source))
'''


FSD_OLD_HEADER_BUTTONS = '''        ttk.Button(row, text="Buscar", command=self._force_refresh_results).pack(side=tk.LEFT)
        ttk.Button(row, text="Limpiar", command=self._clear_search).pack(side=tk.LEFT, padx=(6, 0))
'''

FSD_NEW_HEADER_BUTTONS = '''        ttk.Button(row, text="Buscar", command=self._force_refresh_results).pack(side=tk.LEFT)
        ttk.Button(row, text="Limpiar", command=self._clear_search).pack(side=tk.LEFT, padx=(6, 0))
        ttk.Button(
            row,
            text="↻ Refrescar",
            command=lambda: self._load_files(force_refresh=True),
        ).pack(side=tk.LEFT, padx=(6, 0))
'''


# ---------------------------------------------------------------------------
# Estructura del proyecto
# ---------------------------------------------------------------------------

def verify_structure(root: Path) -> None:
    info(f"Proyecto detectado: {root}")
    missing = [rel for rel in REQUIRED_FILES if not (root / rel).is_file()]
    if missing:
        for m in missing:
            error(f"Falta archivo requerido: {m}")
        raise RuntimeError(
            "La estructura del proyecto no coincide con la esperada. "
            "Abortando sin modificar archivos."
        )


# ---------------------------------------------------------------------------
# Aplicación de cambios
# ---------------------------------------------------------------------------

def apply_all(root: Path, dry_run: bool) -> None:
    info("--- Verificando estructura del proyecto ---")
    verify_structure(root)

    # ---------------------------------------------------------------------
    # PATCH 1 — app/core/project_scanner.py
    # ---------------------------------------------------------------------
    info("--- [1/4] Optimizando caché de project_scanner.py ---")
    ensure_target_exists(root, "app/core/project_scanner.py")

    replace_exact(
        root, "app/core/project_scanner.py",
        old=SCANNER_OLD_SIGNATURE,
        new=SCANNER_NEW_SIGNATURE,
        marker_check="signature = max(",
    )
    replace_exact(
        root, "app/core/project_scanner.py",
        old=SCANNER_OLD_STORE,
        new=SCANNER_NEW_STORE,
        marker_check="(signature, valid_files)",
    )

    # ---------------------------------------------------------------------
    # PATCH 2 — app/core/storage/database.py
    # ---------------------------------------------------------------------
    info("--- [2/4] Añadiendo load_file_paths() a database.py ---")
    ensure_target_exists(root, "app/core/storage/database.py")

    insert_before(
        root, "app/core/storage/database.py",
        anchor=DATABASE_ANCHOR,
        block=DATABASE_NEW_METHOD,
        marker_check="def load_file_paths(self, project_path",
    )

    # ---------------------------------------------------------------------
    # PATCH 3 — app/gui/file_search_dialog.py (render)
    # ---------------------------------------------------------------------
    info("--- [3/4] Optimizando render de file_search_dialog.py ---")
    ensure_target_exists(root, "app/gui/file_search_dialog.py")

    replace_exact(
        root, "app/gui/file_search_dialog.py",
        old=FSD_OLD_CONSTANTS,
        new=FSD_NEW_CONSTANTS,
        marker_check="RENDER_BATCH_DELAY_MS",
    )
    replace_exact(
        root, "app/gui/file_search_dialog.py",
        old=FSD_OLD_REFRESH_TAIL,
        new=FSD_NEW_REFRESH_TAIL,
        marker_check="# FIX: incluso la primera tanda se agenda con after(0, ...)",
    )
    replace_exact(
        root, "app/gui/file_search_dialog.py",
        old=FSD_OLD_RENDER_TAIL,
        new=FSD_NEW_RENDER_TAIL,
        marker_check="# FIX: 15 ms en lugar de 1 ms",
    )

    # ---------------------------------------------------------------------
    # PATCH 4 — app/gui/file_search_dialog.py (DB-first scan)
    # ---------------------------------------------------------------------
    info("--- [4/4] DB-first scan + botón Refrescar en file_search_dialog.py ---")

    replace_exact(
        root, "app/gui/file_search_dialog.py",
        old=FSD_OLD_LOAD_FILES,
        new=FSD_NEW_LOAD_FILES,
        marker_check="def _load_files(self, force_refresh: bool = False):",
    )
    replace_exact(
        root, "app/gui/file_search_dialog.py",
        old=FSD_OLD_CHECK_QUEUE_HEAD,
        new=FSD_NEW_CHECK_QUEUE_HEAD,
        marker_check="sid, files, src = self._scan_queue.get_nowait()",
    )
    replace_exact(
        root, "app/gui/file_search_dialog.py",
        old=FSD_OLD_SCAN_WORKER,
        new=FSD_NEW_SCAN_WORKER,
        marker_check='db.load_file_paths(folder_path)',
    )
    replace_exact(
        root, "app/gui/file_search_dialog.py",
        old=FSD_OLD_HEADER_BUTTONS,
        new=FSD_NEW_HEADER_BUTTONS,
        marker_check='text="↻ Refrescar"',
    )


# ---------------------------------------------------------------------------
# Validación final
# ---------------------------------------------------------------------------

def validate_syntax(root: Path) -> None:
    info("--- Validando sintaxis (py_compile) ---")
    for rel in [
        "app/core/project_scanner.py",
        "app/core/storage/database.py",
        "app/gui/file_search_dialog.py",
    ]:
        full = root / rel
        if not full.is_file():
            continue
        try:
            py_compile.compile(str(full), doraise=True)
            info(f"Sintaxis OK: {rel}")
        except py_compile.PyCompileError as exc:
            error(f"Sintaxis inválida en {rel}: {exc}")


def print_summary() -> None:
    print()
    print(f"Archivos modificados: {STATS['modified']}")
    print(f"Archivos omitidos:    {STATS['skipped']}")
    print(f"Backups creados:      {STATS['backups']}")
    print(f"Errores:              {STATS['errors']}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Aplica las optimizaciones de rendimiento del buscador."
    )
    p.add_argument(
        "project_root", nargs="?", default=".",
        help="Ruta raíz del proyecto (por defecto: directorio actual).",
    )
    p.add_argument("--dry-run", action="store_true",
                   help="Sólo muestra, no modifica archivos.")
    return p


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        root = Path(args.project_root).resolve()
    except Exception as exc:
        error(f"Ruta inválida: {exc}")
        return 1

    if not root.is_dir():
        error(f"El directorio no existe: {root}")
        return 1

    print(f"[INFO] Proyecto detectado: {root}")
    print(f"[INFO] Inicio: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"[INFO] Dry-run: {args.dry_run}")
    print()

    if args.dry_run:
        info("Modo dry-run: se aplicarán los cambios en memoria y se reportará "
             "qué haría cada uno sin escribir nada.")
        print()

    try:
        apply_all(root, dry_run=args.dry_run)
    except Exception as exc:
        error(str(exc))
        print()
        info("Proceso detenido. No se continúan aplicando cambios.")
        print_summary()
        return 1

    print()
    info("--- Resumen final ---")
    print_summary()

    if not args.dry_run:
        validate_syntax(root)

    print()
    if STATS["errors"] == 0:
        info("Optimizaciones aplicadas. Reinicia la aplicación para probar.")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())