#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
resume_phase1_sqlite.py

Completa los 3 cambios pendientes de la Fase 1 (SQLite) que quedaron sin
aplicar tras el error de anclaje en main_window.py:

  4. Método _on_tree_check_change (persistencia de checkbox)
  5. Restaurar is_checked en reload_tree()
  6. Persistir tras el análisis en on_analyze_project()

Uso:
    python3 resume_phase1_sqlite.py /ruta/al/proyecto
    python3 resume_phase1_sqlite.py                 # directorio actual

Características:
  * Idempotente: si un cambio ya está aplicado, se omite con [SKIP].
  * Crea backup en .backup/ conservando la ruta relativa.
  * Valida la sintaxis final con py_compile.
  * Solo biblioteca estándar.
"""
import argparse
import shutil
import sys
import py_compile
from datetime import datetime
from pathlib import Path


BACKUP_DIRNAME = ".backup"
MAIN_WINDOW_REL = "app/gui/main_window.py"


# ---------------------------------------------------------------------------
# Bloques a insertar (idénticos a los del script original)
# ---------------------------------------------------------------------------

MW_METHOD_BLOCK = '''    # === PERSISTENCE: PHASE1 (method) ===
    def _on_tree_check_change(self, rel_path: str, is_checked: bool):
        """Persist checkbox changes to SQLite (Phase 1)."""
        if self._persist_db is None:
            return
        folder = self.var_folder.get()
        if not folder:
            return
        try:
            project_id = self._persist_db.get_or_create_project(folder)
            self._persist_db.update_is_checked(project_id, rel_path, is_checked)
        except Exception:
            pass
    # === END PERSISTENCE: PHASE1 (method) ===
'''

MW_RELOAD_BLOCK = '''        # === PERSISTENCE: PHASE1 (reload) ===
        if self._persist_db is not None:
            try:
                saved = self._persist_db.load_checked_state(folder)
                if saved is not None:
                    self.tree.set_checked_files(saved)
                    self.selector.set_checked_folder_files(
                        self.tree.get_checked_files()
                    )
            except Exception:
                pass
        # === END PERSISTENCE: PHASE1 (reload) ===
'''

MW_ANALYZE_BLOCK = '''        # === PERSISTENCE: PHASE1 (analyze) ===
        try:
            analyzer.persist_result(result)
        except Exception:
            pass
        # === END PERSISTENCE: PHASE1 (analyze) ===
'''


# ---------------------------------------------------------------------------
# Anclas 100 % ASCII (sin box-drawing characters)
# ---------------------------------------------------------------------------

ANCHOR_METHOD  = "    def on_select_folder(self):"
ANCHOR_RELOAD  = (
    '                rel_file = os.path.join(rel_dir, f) if rel_dir != "." else f\n'
    '                self.tree.insert_file(parent_item, rel_file)'
)
ANCHOR_ANALYZE = "        result = analyzer.analyze(folder, max_file_size_mb=max_file_mb)"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def log(level, msg):
    print(f"[{level}] {msg}")


def backup(root: Path, rel: str) -> None:
    src = root / rel
    if not src.is_file():
        return
    dst = root / BACKUP_DIRNAME / rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    log("INFO", f"Backup creado: {dst.relative_to(root)}")


def insert_before(root: Path, rel: str, anchor: str, block: str, marker: str) -> None:
    p = root / rel
    content = p.read_text(encoding="utf-8")
    if marker in content:
        log("SKIP", f"Cambio ya aplicado: {rel} ({marker.strip()})")
        return
    idx = content.find(anchor)
    if idx == -1:
        raise RuntimeError(f"Ancla no encontrada en {rel}:\n  {anchor!r}")
    new = content[:idx] + block + "\n" + content[idx:]
    backup(root, rel)
    p.write_text(new, encoding="utf-8")
    log("OK", f"Cambio aplicado: {rel}  ({marker.strip()})")


def insert_after(root: Path, rel: str, anchor: str, block: str, marker: str) -> None:
    p = root / rel
    content = p.read_text(encoding="utf-8")
    if marker in content:
        log("SKIP", f"Cambio ya aplicado: {rel} ({marker.strip()})")
        return
    idx = content.find(anchor)
    if idx == -1:
        raise RuntimeError(f"Ancla no encontrada en {rel}:\n  {anchor!r}")
    end = idx + len(anchor)
    new = content[:end] + "\n" + block + content[end:]
    backup(root, rel)
    p.write_text(new, encoding="utf-8")
    log("OK", f"Cambio aplicado: {rel}  ({marker.strip()})")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Reanuda los cambios pendientes de la Fase 1 (SQLite)."
    )
    parser.add_argument("root", nargs="?", default=".",
                        help="Ruta raíz del proyecto (por defecto: directorio actual).")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    mw = root / MAIN_WINDOW_REL
    if not mw.is_file():
        log("ERROR", f"No existe {mw}")
        return 1

    log("INFO", f"Proyecto detectado: {root}")
    log("INFO", f"Inicio: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    try:
        # 4. Método _on_tree_check_change (antes de los UI event handlers)
        insert_before(
            root, MAIN_WINDOW_REL,
            anchor=ANCHOR_METHOD,
            block=MW_METHOD_BLOCK,
            marker="# === PERSISTENCE: PHASE1 (method) ===",
        )

        # 5. Restaurar estado tras cargar el árbol
        insert_after(
            root, MAIN_WINDOW_REL,
            anchor=ANCHOR_RELOAD,
            block=MW_RELOAD_BLOCK,
            marker="# === PERSISTENCE: PHASE1 (reload) ===",
        )

        # 6. Persistir tras el análisis
        insert_after(
            root, MAIN_WINDOW_REL,
            anchor=ANCHOR_ANALYZE,
            block=MW_ANALYZE_BLOCK,
            marker="# === PERSISTENCE: PHASE1 (analyze) ===",
        )
    except Exception as exc:
        log("ERROR", str(exc))
        print()
        log("INFO", "Proceso detenido. No se continúan aplicando cambios.")
        return 1

    print()
    log("INFO", "--- Validando sintaxis (py_compile) ---")
    try:
        py_compile.compile(str(mw), doraise=True)
        log("OK", f"Sintaxis OK: {MAIN_WINDOW_REL}")
    except py_compile.PyCompileError as exc:
        log("ERROR", f"Sintaxis inválida en {MAIN_WINDOW_REL}: {exc}")
        return 1

    print()
    log("INFO", "Fase 1 completada. Reinicia la aplicación para probar.")
    return 0


if __name__ == "__main__":
    sys.exit(main())