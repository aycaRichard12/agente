#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
apply_phase2_delta_scan.py — Aplica Fase 2 (Delta Scan + caché) sobre el
proyecto "agente".

Uso:
    python3 apply_phase2_delta_scan.py /ruta/al/proyecto

Idempotente. Backups en .backup/. Valida sintaxis con py_compile.
"""
import argparse, py_compile, shutil, sys
from datetime import datetime
from pathlib import Path

BACKUP = ".backup"
ROOT_FILES = [
    "app/__init__.py",
    "app/core/project_analyzer.py",
    "app/core/storage/database.py",
    "app/gui/main_window.py",
]

def log(lvl, msg): print(f"[{lvl}] {msg}")
def backup(root: Path, rel: str) -> None:
    src = root / rel
    if not src.is_file(): return
    dst = root / BACKUP / rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    log("INFO", f"Backup creado: {dst.relative_to(root)}")

def insert_after(root: Path, rel: str, anchor: str, block: str, marker: str):
    p = root / rel
    txt = p.read_text(encoding="utf-8")
    if marker in txt:
        log("SKIP", f"Ya aplicado: {rel} ({marker.strip()})"); return
    i = txt.find(anchor)
    if i == -1:
        raise RuntimeError(f"Ancla no encontrada en {rel}:\n  {anchor!r}")
    e = i + len(anchor)
    backup(root, rel)
    p.write_text(txt[:e] + "\n" + block + txt[e:], encoding="utf-8")
    log("OK", f"Cambio aplicado: {rel}  ({marker.strip()})")

def insert_before(root: Path, rel: str, anchor: str, block: str, marker: str):
    p = root / rel
    txt = p.read_text(encoding="utf-8")
    if marker in txt:
        log("SKIP", f"Ya aplicado: {rel} ({marker.strip()})"); return
    i = txt.find(anchor)
    if i == -1:
        raise RuntimeError(f"Ancla no encontrada en {rel}:\n  {anchor!r}")
    backup(root, rel)
    p.write_text(txt[:i] + block + "\n" + txt[i:], encoding="utf-8")
    log("OK", f"Cambio aplicado: {rel}  ({marker.strip()})")

# --- bloques ---

DB_WAL_OLD = '''        self._conn = sqlite3.connect(self.db_path)
        self._conn.row_factory = sqlite3.Row
        self._conn.execute("PRAGMA foreign_keys = ON")
        self._init_schema()'''

DB_WAL_NEW = '''        self._conn = sqlite3.connect(self.db_path, timeout=10.0)
        self._conn.row_factory = sqlite3.Row
        self._conn.execute("PRAGMA foreign_keys = ON")
        self._conn.execute("PRAGMA journal_mode = WAL")
        self._conn.execute("PRAGMA synchronous = NORMAL")
        self._init_schema()'''

DB_DELTA_BLOCK = '''    # === PHASE 2: DELTA SCAN ===
    def load_nodes_map(self, project_path: str):
        cur = self._conn.cursor()
        cur.execute("SELECT id FROM projects WHERE path = ?", (project_path,))
        row = cur.fetchone()
        if not row:
            return None
        project_id = int(row["id"])
        cur.execute(
            "SELECT id, rel_path, parent_path, is_dir, mtime, lines_count, "
            "file_size, is_important, is_checked FROM nodes WHERE project_id = ?",
            (project_id,),
        )
        return {r["rel_path"]: dict(r) for r in cur.fetchall()}

    def apply_delta(self, project_id, to_insert, to_update,
                    to_delete_paths, dep_pairs):
        if to_delete_paths:
            with self._conn:
                self._conn.executemany(
                    "DELETE FROM nodes WHERE project_id = ? AND rel_path = ?",
                    [(project_id, rp) for rp in to_delete_paths],
                )
        if to_update:
            with self._conn:
                self._conn.executemany(
                    """UPDATE nodes SET mtime=?, lines_count=?, file_size=?,
                                       is_important=?
                       WHERE project_id=? AND rel_path=?""",
                    [(n["mtime"], n["lines_count"], n["file_size"],
                      int(bool(n.get("is_important", 0))),
                      project_id, n["rel_path"]) for n in to_update],
                )
        if to_insert:
            with self._conn:
                self._conn.executemany(
                    """INSERT INTO nodes
                       (project_id, rel_path, parent_path, is_dir, mtime,
                        lines_count, file_size, is_important, is_checked)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    [(project_id, n["rel_path"], n.get("parent_path"),
                      int(bool(n.get("is_dir", 0))),
                      float(n.get("mtime", 0.0)),
                      int(n.get("lines_count", 0) or 0),
                      int(n.get("file_size", 0) or 0),
                      int(bool(n.get("is_important", 0))),
                      int(bool(n.get("is_checked", 1))))
                     for n in to_insert],
                )
        if to_update or to_insert or to_delete_paths:
            with self._conn:
                pairs = ([(project_id, n["rel_path"]) for n in to_update] +
                         [(project_id, n["rel_path"]) for n in to_insert] +
                         [(project_id, rp) for rp in to_delete_paths])
                self._conn.executemany(
                    """DELETE FROM node_dependencies
                       WHERE source_node_id IN
                         (SELECT id FROM nodes WHERE project_id=? AND rel_path=?)""",
                    pairs,
                )
                if dep_pairs:
                    cur = self._conn.cursor()
                    cur.execute(
                        "SELECT id, rel_path FROM nodes WHERE project_id=?",
                        (project_id,))
                    id_map = {r["rel_path"]: int(r["id"])
                              for r in cur.fetchall()}
                    rows = [(id_map[s], t) for s, t in dep_pairs if s in id_map]
                    if rows:
                        self._conn.executemany(
                            "INSERT INTO node_dependencies "
                            "(source_node_id, target_path) VALUES (?, ?)",
                            rows,
                        )
        self.update_last_scanned(project_id)
    # === END PHASE 2 ===
'''

MW_DEBOUNCE_INIT = '''        # === PHASE 2: DEBOUNCE CHECKBOX ===
        self._pending_checks = {}
        self._flush_timer = None
        # === END PHASE 2 ===
'''

MW_DEBOUNCE_METHOD = '''    # === PHASE 2: DEBOUNCE CHECKBOX ===
    def _flush_pending_checks(self):
        self._flush_timer = None
        if not self._pending_checks or self._persist_db is None:
            return
        folder = self.var_folder.get()
        if not folder:
            self._pending_checks.clear(); return
        try:
            pid = self._persist_db.get_or_create_project(folder)
            self._persist_db.update_is_checked_batch(
                pid, list(self._pending_checks.items()))
        except Exception:
            pass
        self._pending_checks.clear()
    # === END PHASE 2 ===
'''

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("root", nargs="?", default=".")
    args = ap.parse_args()
    root = Path(args.root).resolve()

    missing = [f for f in ROOT_FILES if not (root / f).is_file()]
    if missing:
        for m in missing: log("ERROR", f"Falta {m}")
        return 1

    log("INFO", f"Proyecto detectado: {root}")
    log("INFO", f"Inicio: {datetime.now():%Y-%m-%d %H:%M:%S}")
    print()

    try:
        # 1) WAL + timeout en database.py
        db = root / "app/core/storage/database.py"
        txt = db.read_text(encoding="utf-8")
        if "journal_mode = WAL" in txt:
            log("SKIP", "WAL ya aplicado")
        else:
            if DB_WAL_OLD not in txt:
                raise RuntimeError("Ancla WAL no encontrada en database.py")
            backup(root, "app/core/storage/database.py")
            db.write_text(txt.replace(DB_WAL_OLD, DB_WAL_NEW, 1),
                          encoding="utf-8")
            log("OK", "WAL + timeout aplicados")

        # 2) apply_delta + load_nodes_map
        insert_before(
            root, "app/core/storage/database.py",
            anchor="    def close(self) -> None:",
            block=DB_DELTA_BLOCK,
            marker="# === PHASE 2: DELTA SCAN ===",
        )

        # 3) main_window.py — debounce
        insert_after(
            root, "app/gui/main_window.py",
            anchor=("        self.config     = ExportConfig()\n"
                    "        # === PERSISTENCE: PHASE1 (init) ===\n"
                    "        self._persist_db = None\n"
                    "        try:\n"
                    "            self._persist_db = get_database()\n"
                    "        except Exception:\n"
                    "            self._persist_db = None\n"
                    "        # === END PERSISTENCE: PHASE1 (init) ==="),
            block=MW_DEBOUNCE_INIT,
            marker="# === PHASE 2: DEBOUNCE CHECKBOX ===",
        )
        insert_before(
            root, "app/gui/main_window.py",
            anchor="    def on_select_folder(self):",
            block=MW_DEBOUNCE_METHOD,
            marker="# === PHASE 2: DEBOUNCE CHECKBOX ===",
        )

        # 4) Cambio en analyze_incremental y _on_tree_check_change
        #    (se aplica manualmente por la complejidad del bloque).
        log("INFO", "Recuerda reemplazar en main_window.py:")
        log("INFO", "  - analyzer.analyze(...) → analyzer.analyze_incremental(...)")
        log("INFO", "  - Cuerpo de _on_tree_check_change (debounce)")

    except Exception as exc:
        log("ERROR", str(exc))
        return 1

    print()
    log("INFO", "--- Validando sintaxis ---")
    for rel in ["app/core/storage/database.py",
                "app/gui/main_window.py"]:
        try:
            py_compile.compile(str(root / rel), doraise=True)
            log("OK", f"Sintaxis OK: {rel}")
        except py_compile.PyCompileError as e:
            log("ERROR", f"{rel}: {e}")
            return 1

    print()
    log("INFO", "Fase 2 aplicada. Reinicia la aplicación.")
    return 0

if __name__ == "__main__":
    sys.exit(main())