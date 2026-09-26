#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
apply_phase1_sqlite.py

Aplica la Fase 1 — Persistencia SQLite para nodos — sobre el proyecto
"agente" (DeepSeek Code Packager).

Uso:
    python3 apply_phase1_sqlite.py /ruta/al/proyecto
    python3 apply_phase1_sqlite.py                 # usa el directorio actual

Características:
  * Detecta automáticamente la raíz del proyecto (o la recibe como argumento).
  * Verifica que los archivos objetivo existan ANTES de modificar nada.
  * Crea backups en .backup/ preservando la ruta relativa original.
  * Es idempotente: ejecutarlo dos veces no duplica bloques.
  * Solo modifica los archivos estrictamente necesarios.
  * Al finalizar valida la sintaxis con py_compile.
  * Solo utiliza la biblioteca estándar de Python.
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

BACKUP_DIRNAME = ".backup"

STATS = {
    "modified": 0,
    "created": 0,
    "skipped": 0,
    "backups": 0,
    "errors": 0,
}


# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

def _log(prefix, msg):
    print(f"{prefix} {msg}")


def info(msg):  _log("[INFO]", msg)
def ok(msg):    _log("[OK]", msg)
def skip(msg):  _log("[SKIP]", msg)
def error(msg): _log("[ERROR]", msg); STATS["errors"] += 1


# ---------------------------------------------------------------------------
# Helpers de I/O y validación
# ---------------------------------------------------------------------------

def ensure_target_exists(root: Path, rel_path: str) -> Path:
    p = root / rel_path
    if not p.is_file():
        raise RuntimeError(f"Archivo objetivo no encontrado: {p}")
    info(f"Archivo encontrado: {rel_path}")
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


def write_new_file(root: Path, rel_path: str, content: str) -> None:
    target = root / rel_path
    if target.exists():
        existing = target.read_text(encoding="utf-8", errors="ignore")
        if content.strip() and content.strip() in existing:
            skip(f"Archivo ya presente y correcto: {rel_path}")
            STATS["skipped"] += 1
            return
        skip(f"Archivo ya existe (no se sobreescribe): {rel_path}")
        STATS["skipped"] += 1
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")
    STATS["created"] += 1
    ok(f"Archivo creado: {rel_path}")


def _apply_change(root: Path, rel_path: str, new_content: str) -> None:
    backup_file(root, rel_path)
    (root / rel_path).write_text(new_content, encoding="utf-8")
    STATS["modified"] += 1
    ok(f"Cambio aplicado: {rel_path}")


def insert_after(root: Path, rel_path: str, anchor: str,
                 block: str, marker: str) -> None:
    content = (root / rel_path).read_text(encoding="utf-8")
    if marker in content:
        skip(f"Cambio ya aplicado: {rel_path} (marcador presente)")
        STATS["skipped"] += 1
        return
    idx = content.find(anchor)
    if idx == -1:
        raise RuntimeError(
            f"Ancla no encontrada en {rel_path}:\n  {anchor!r}"
        )
    end = idx + len(anchor)
    new_content = content[:end] + "\n" + block + content[end:]
    _apply_change(root, rel_path, new_content)


def insert_before(root: Path, rel_path: str, anchor: str,
                  block: str, marker: str) -> None:
    content = (root / rel_path).read_text(encoding="utf-8")
    if marker in content:
        skip(f"Cambio ya aplicado: {rel_path} (marcador presente)")
        STATS["skipped"] += 1
        return
    idx = content.find(anchor)
    if idx == -1:
        raise RuntimeError(
            f"Ancla no encontrada en {rel_path}:\n  {anchor!r}"
        )
    new_content = content[:idx] + block + "\n" + content[idx:]
    _apply_change(root, rel_path, new_content)


def replace_exact(root: Path, rel_path: str, old: str, new: str) -> None:
    content = (root / rel_path).read_text(encoding="utf-8")
    if old not in content:
        if new in content:
            skip(f"Reemplazo ya aplicado: {rel_path}")
        else:
            skip(f"Patrón no encontrado en {rel_path} (posible versión distinta)")
        STATS["skipped"] += 1
        return
    new_content = content.replace(old, new, 1)
    _apply_change(root, rel_path, new_content)


# ---------------------------------------------------------------------------
# Contenido de archivos nuevos
# ---------------------------------------------------------------------------

STORAGE_INIT_PY = '''"""Phase 1 SQLite persistence package."""
from app.core.storage.database import Database, get_database, default_db_path

__all__ = ["Database", "get_database", "default_db_path"]
'''


DATABASE_PY = '''"""
SQLite persistence layer for project nodes, metrics and dependencies (Phase 1).

This module is intentionally restricted to:
  - Opening / creating the SQLite database.
  - Initializing the schema.
  - Executing queries and updates.
  - Managing transactions.
  - Providing the CRUD operations required for projects and nodes.

No Delta Scan or incremental change detection logic is implemented here.
"""
import os
import sqlite3
from typing import Dict, List, Optional, Set, Tuple


# ---------------------------------------------------------------------------
# Path resolution
# ---------------------------------------------------------------------------

def _find_project_root() -> Optional[str]:
    """Walk up from this file to find the project root (contains main.py)."""
    here = os.path.dirname(os.path.abspath(__file__))
    candidate = os.path.abspath(os.path.join(here, "..", "..", ".."))
    if os.path.isfile(os.path.join(candidate, "main.py")):
        return candidate
    return None


def default_db_path() -> str:
    """Resolve project_cache.db path.

    Prefer <project_root>/.cache/project_cache.db, fallback to
    ~/.analyzer_app/project_cache.db when the project root cannot be resolved.
    """
    root = _find_project_root()
    if root:
        return os.path.join(root, ".cache", "project_cache.db")
    home = os.path.expanduser("~")
    return os.path.join(home, ".analyzer_app", "project_cache.db")


# ---------------------------------------------------------------------------
# Schema
# ---------------------------------------------------------------------------

SCHEMA_STATEMENTS = [
    """CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        path TEXT UNIQUE NOT NULL,
        project_type TEXT,
        framework TEXT,
        last_scanned TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""",
    """CREATE TABLE IF NOT EXISTS nodes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_id INTEGER NOT NULL,
        rel_path TEXT NOT NULL,
        parent_path TEXT,
        is_dir BOOLEAN NOT NULL,
        mtime REAL NOT NULL,
        lines_count INTEGER DEFAULT 0,
        file_size INTEGER DEFAULT 0,
        is_important BOOLEAN DEFAULT 0,
        is_checked BOOLEAN DEFAULT 1,
        FOREIGN KEY(project_id) REFERENCES projects(id) ON DELETE CASCADE,
        UNIQUE(project_id, rel_path)
    )""",
    """CREATE TABLE IF NOT EXISTS node_dependencies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source_node_id INTEGER NOT NULL,
        target_path TEXT NOT NULL,
        FOREIGN KEY(source_node_id) REFERENCES nodes(id) ON DELETE CASCADE
    )""",
    "CREATE INDEX IF NOT EXISTS idx_nodes_rel_path ON nodes(project_id, rel_path)",
    "CREATE INDEX IF NOT EXISTS idx_nodes_parent ON nodes(project_id, parent_path)",
]


# ---------------------------------------------------------------------------
# Database
# ---------------------------------------------------------------------------

class Database:
    """Thin SQLite wrapper for the project cache (Phase 1)."""

    def __init__(self, db_path: Optional[str] = None):
        self.db_path = db_path or default_db_path()
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self._conn = sqlite3.connect(self.db_path)
        self._conn.row_factory = sqlite3.Row
        self._conn.execute("PRAGMA foreign_keys = ON")
        self._init_schema()

    def _init_schema(self) -> None:
        with self._conn:
            for stmt in SCHEMA_STATEMENTS:
                self._conn.execute(stmt)

    # ---------- projects ----------

    def get_or_create_project(self, path: str,
                              project_type: Optional[str] = None,
                              framework: Optional[str] = None) -> int:
        cur = self._conn.cursor()
        cur.execute("SELECT id FROM projects WHERE path = ?", (path,))
        row = cur.fetchone()
        if row:
            return int(row["id"])
        cur.execute(
            "INSERT INTO projects (path, project_type, framework) VALUES (?, ?, ?)",
            (path, project_type, framework),
        )
        self._conn.commit()
        return int(cur.lastrowid)

    def get_project_by_path(self, path: str) -> Optional[Dict]:
        cur = self._conn.cursor()
        cur.execute("SELECT * FROM projects WHERE path = ?", (path,))
        row = cur.fetchone()
        return dict(row) if row else None

    def update_last_scanned(self, project_id: int) -> None:
        with self._conn:
            self._conn.execute(
                "UPDATE projects SET last_scanned = CURRENT_TIMESTAMP WHERE id = ?",
                (project_id,),
            )

    def delete_project(self, path: str) -> None:
        with self._conn:
            self._conn.execute("DELETE FROM projects WHERE path = ?", (path,))

    # ---------- nodes ----------

    def replace_nodes(self, project_id: int, nodes: List[Dict]) -> None:
        """Delete existing nodes for project and insert the new batch atomically."""
        rows = [
            (
                project_id,
                n["rel_path"],
                n.get("parent_path"),
                int(bool(n.get("is_dir", 0))),
                float(n.get("mtime", 0.0) or 0.0),
                int(n.get("lines_count", 0) or 0),
                int(n.get("file_size", 0) or 0),
                int(bool(n.get("is_important", 0))),
                int(bool(n.get("is_checked", 1))),
            )
            for n in nodes
        ]
        with self._conn:
            self._conn.execute("DELETE FROM nodes WHERE project_id = ?", (project_id,))
            if rows:
                self._conn.executemany(
                    """INSERT INTO nodes
                       (project_id, rel_path, parent_path, is_dir, mtime,
                        lines_count, file_size, is_important, is_checked)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    rows,
                )

    def get_nodes(self, project_id: int) -> List[Dict]:
        cur = self._conn.cursor()
        cur.execute("SELECT * FROM nodes WHERE project_id = ?", (project_id,))
        return [dict(r) for r in cur.fetchall()]

    def update_is_checked(self, project_id: int,
                          rel_path: str, is_checked: bool) -> None:
        with self._conn:
            self._conn.execute(
                "UPDATE nodes SET is_checked = ? "
                "WHERE project_id = ? AND rel_path = ?",
                (int(bool(is_checked)), project_id, rel_path),
            )

    def update_is_checked_batch(self, project_id: int,
                                updates: List[Tuple[str, bool]]) -> None:
        rows = [(int(bool(c)), project_id, rp) for rp, c in updates]
        if not rows:
            return
        with self._conn:
            self._conn.executemany(
                "UPDATE nodes SET is_checked = ? "
                "WHERE project_id = ? AND rel_path = ?",
                rows,
            )

    def load_checked_state(self, project_path: str) -> Optional[Set[str]]:
        """Return the set of checked rel_paths (files only).

        Returns None when there is no persisted data for this project,
        so the caller can distinguish "never saved" from "all unchecked".
        """
        cur = self._conn.cursor()
        cur.execute("SELECT id FROM projects WHERE path = ?", (project_path,))
        row = cur.fetchone()
        if not row:
            return None
        project_id = int(row["id"])
        cur.execute(
            "SELECT rel_path, is_checked FROM nodes "
            "WHERE project_id = ? AND is_dir = 0",
            (project_id,),
        )
        rows = cur.fetchall()
        if not rows:
            return None
        return {r["rel_path"] for r in rows if r["is_checked"]}

    def delete_nodes(self, project_id: int) -> None:
        with self._conn:
            self._conn.execute("DELETE FROM nodes WHERE project_id = ?", (project_id,))

    # ---------- dependencies ----------

    def save_dependencies_batch(self, project_id: int,
                                deps: List[Tuple[str, str]]) -> None:
        """deps: list of (source_rel_path, target_path)."""
        if not deps:
            return
        cur = self._conn.cursor()
        cur.execute("SELECT id, rel_path FROM nodes WHERE project_id = ?", (project_id,))
        id_map = {r["rel_path"]: int(r["id"]) for r in cur.fetchall()}

        rows = []
        for src_rel, target in deps:
            node_id = id_map.get(src_rel)
            if node_id is None:
                continue
            rows.append((node_id, target))

        with self._conn:
            self._conn.execute(
                """DELETE FROM node_dependencies
                   WHERE source_node_id IN
                         (SELECT id FROM nodes WHERE project_id = ?)""",
                (project_id,),
            )
            if rows:
                self._conn.executemany(
                    "INSERT INTO node_dependencies (source_node_id, target_path) "
                    "VALUES (?, ?)",
                    rows,
                )

    def get_dependencies(self, project_id: int) -> List[Dict]:
        cur = self._conn.cursor()
        cur.execute(
            """SELECT n.rel_path AS source_path, d.target_path AS target_path
               FROM node_dependencies d
               JOIN nodes n ON n.id = d.source_node_id
               WHERE n.project_id = ?""",
            (project_id,),
        )
        return [dict(r) for r in cur.fetchall()]

    def close(self) -> None:
        try:
            self._conn.close()
        except Exception:
            pass


# ---------------------------------------------------------------------------
# Singleton accessor
# ---------------------------------------------------------------------------

_db_singleton: Optional[Database] = None


def get_database(db_path: Optional[str] = None) -> Database:
    """Return the process-wide Database singleton."""
    global _db_singleton
    if _db_singleton is None or (db_path and db_path != _db_singleton.db_path):
        _db_singleton = Database(db_path)
    return _db_singleton


def reset_database_singleton() -> None:
    """For tests: close and drop the current singleton."""
    global _db_singleton
    if _db_singleton is not None:
        _db_singleton.close()
    _db_singleton = None
'''


# ---------------------------------------------------------------------------
# Bloques a insertar en archivos existentes
# ---------------------------------------------------------------------------

# --- ProjectAnalyzer.persist_result -----------------------------------------

PERSIST_RESULT_BLOCK = '''    # === PERSISTENCE: PHASE1 (persist_result) ===
    def persist_result(self, result) -> None:
        """Persist a ProjectAnalysisResult to the SQLite cache (Phase 1).

        This method is additive and does not modify the existing analyze()
        pipeline, its return type, or FileMetric structure.
        """
        try:
            from app.core.storage.database import get_database
        except Exception:
            return

        folder = getattr(result, "folder_path", None)
        if not folder or not os.path.isdir(folder):
            return

        try:
            db = get_database()
        except Exception:
            return

        project_id = db.get_or_create_project(
            path=folder,
            project_type=getattr(result, "primary_language", None),
            framework=getattr(result, "framework", None),
        )

        # Preserve previously persisted is_checked state
        existing_checked = db.load_checked_state(folder)

        important = set(getattr(result, "important_files", []) or [])
        nodes = []

        for dirpath, dirnames, filenames in os.walk(folder):
            dirnames[:] = [d for d in dirnames if d not in self.excluded_dirs]
            rel_dir = os.path.relpath(dirpath, folder)

            if rel_dir != ".":
                rel_norm = rel_dir.replace("\\\\", "/")
                parent = os.path.dirname(rel_norm).replace("\\\\", "/") or None
                try:
                    mtime = float(os.stat(dirpath).st_mtime)
                except Exception:
                    mtime = 0.0
                nodes.append({
                    "rel_path": rel_norm,
                    "parent_path": parent,
                    "is_dir": 1,
                    "mtime": mtime,
                    "lines_count": 0,
                    "file_size": 0,
                    "is_important": 0,
                    "is_checked": 0,
                })

            for f in filenames:
                full = os.path.join(dirpath, f)
                if is_binary_file(full):
                    continue
                rel_file = f if rel_dir == "." else os.path.join(rel_dir, f)
                rel_file = rel_file.replace("\\\\", "/")
                try:
                    st = os.stat(full)
                    mtime = float(st.st_mtime)
                    size = int(st.st_size)
                except Exception:
                    mtime = 0.0
                    size = 0
                parent = os.path.dirname(rel_file).replace("\\\\", "/") or None

                if existing_checked is None:
                    is_checked = 1
                else:
                    is_checked = 1 if rel_file in existing_checked else 0

                nodes.append({
                    "rel_path": rel_file,
                    "parent_path": parent,
                    "is_dir": 0,
                    "mtime": mtime,
                    "lines_count": 0,
                    "file_size": size,
                    "is_important": 1 if rel_file in important else 0,
                    "is_checked": is_checked,
                })

        try:
            db.replace_nodes(project_id, nodes)

            dep_pairs = []
            code_deps = getattr(result, "code_dependencies", {}) or {}
            for rel_path, deps in code_deps.items():
                for d in deps:
                    dep_pairs.append((rel_path, d))
            db.save_dependencies_batch(project_id, dep_pairs)

            db.update_last_scanned(project_id)
        except Exception:
            pass
    # === END PERSISTENCE: PHASE1 (persist_result) ===
'''


# --- CheckboxTreeview -------------------------------------------------------

FILE_TREE_ATTRS_BLOCK = '''        # === PERSISTENCE: PHASE1 (attrs) ===
        self._on_check_change = None
        # === END PERSISTENCE: PHASE1 (attrs) ===
'''

FILE_TREE_METHODS_BLOCK = '''    # === PERSISTENCE: PHASE1 (methods) ===
    def set_check_change_callback(self, callback) -> None:
        """Register callback(rel_path: str, is_checked: bool) for persistence."""
        self._on_check_change = callback

    def _notify_check_change(self, rel_path: str, is_checked: bool) -> None:
        if not self._on_check_change or not rel_path:
            return
        try:
            self._on_check_change(rel_path, is_checked)
        except Exception:
            pass
    # === END PERSISTENCE: PHASE1 (methods) ===
'''


FILE_TREE_CHECK_OLD = '''    def check_item(self, item):
        rel_path = self.set(item, "name")
        if rel_path:
            self.set(item, "check", "☑")
            self.item(item, tags=("checked",))
            if not self.get_children(item):
                self.checked_items.add(rel_path)
        for child in self.get_children(item):
            self.check_item(child)
'''

FILE_TREE_CHECK_NEW = '''    def check_item(self, item):
        rel_path = self.set(item, "name")
        if rel_path:
            was_checked = rel_path in self.checked_items
            self.set(item, "check", "☑")
            self.item(item, tags=("checked",))
            if not self.get_children(item):
                self.checked_items.add(rel_path)
                if not was_checked:
                    self._notify_check_change(rel_path, True)
        for child in self.get_children(item):
            self.check_item(child)
'''


FILE_TREE_UNCHECK_OLD = '''    def uncheck_item(self, item):
        rel_path = self.set(item, "name")
        if rel_path:
            self.set(item, "check", "☐")
            self.item(item, tags=("unchecked",))
            if rel_path in self.checked_items:
                self.checked_items.remove(rel_path)
        for child in self.get_children(item):
            self.uncheck_item(child)
'''

FILE_TREE_UNCHECK_NEW = '''    def uncheck_item(self, item):
        rel_path = self.set(item, "name")
        if rel_path:
            was_checked = rel_path in self.checked_items
            self.set(item, "check", "☐")
            self.item(item, tags=("unchecked",))
            if rel_path in self.checked_items:
                self.checked_items.remove(rel_path)
            if was_checked:
                self._notify_check_change(rel_path, False)
        for child in self.get_children(item):
            self.uncheck_item(child)
'''


# --- MainWindow -------------------------------------------------------------

MW_IMPORT_BLOCK = '''# === PERSISTENCE: PHASE1 (imports) ===
from app.core.storage.database import get_database
# === END PERSISTENCE: PHASE1 (imports) ===
'''

MW_INIT_BLOCK = '''        # === PERSISTENCE: PHASE1 (init) ===
        self._persist_db = None
        try:
            self._persist_db = get_database()
        except Exception:
            self._persist_db = None
        # === END PERSISTENCE: PHASE1 (init) ===
'''

MW_CALLBACK_BLOCK = '''        # === PERSISTENCE: PHASE1 (callback) ===
        if self._persist_db is not None:
            self.tree.set_check_change_callback(self._on_tree_check_change)
        # === END PERSISTENCE: PHASE1 (callback) ===
'''

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
# Aplicación de cambios
# ---------------------------------------------------------------------------

REQUIRED_FILES = [
    "app/__init__.py",
    "app/core/__init__.py",
    "app/core/project_analyzer.py",
    "app/gui/file_tree.py",
    "app/gui/main_window.py",
    "app/models/project.py",
    "main.py",
]


def verify_structure(root: Path) -> None:
    info(f"Proyecto detectado: {root}")
    missing = []
    for rel in REQUIRED_FILES:
        p = root / rel
        if not p.is_file():
            missing.append(rel)
    if missing:
        for m in missing:
            error(f"Falta archivo requerido: {m}")
        raise RuntimeError(
            "La estructura del proyecto no coincide con la esperada. "
            "Abortando sin modificar archivos."
        )


def apply_all(root: Path) -> None:
    info("--- Verificando estructura del proyecto ---")
    verify_structure(root)

    info("--- Creando archivos nuevos ---")
    write_new_file(root, "app/core/storage/__init__.py", STORAGE_INIT_PY)
    write_new_file(root, "app/core/storage/database.py", DATABASE_PY)

    info("--- Modificando app/core/project_analyzer.py ---")
    ensure_target_exists(root, "app/core/project_analyzer.py")
    insert_before(
        root, "app/core/project_analyzer.py",
        anchor="    def _is_entry_point(self, rel_path: str) -> bool:",
        block=PERSIST_RESULT_BLOCK,
        marker="# === PERSISTENCE: PHASE1 (persist_result) ===",
    )

    info("--- Modificando app/gui/file_tree.py ---")
    ensure_target_exists(root, "app/gui/file_tree.py")
    insert_after(
        root, "app/gui/file_tree.py",
        anchor="        self.checked_items: Set[str] = set()",
        block=FILE_TREE_ATTRS_BLOCK,
        marker="# === PERSISTENCE: PHASE1 (attrs) ===",
    )
    insert_before(
        root, "app/gui/file_tree.py",
        anchor="    def insert_file(self, parent, rel_path: str, is_checked: bool = True):",
        block=FILE_TREE_METHODS_BLOCK,
        marker="# === PERSISTENCE: PHASE1 (methods) ===",
    )
    replace_exact(root, "app/gui/file_tree.py",
                  FILE_TREE_CHECK_OLD, FILE_TREE_CHECK_NEW)
    replace_exact(root, "app/gui/file_tree.py",
                  FILE_TREE_UNCHECK_OLD, FILE_TREE_UNCHECK_NEW)

    info("--- Modificando app/gui/main_window.py ---")
    ensure_target_exists(root, "app/gui/main_window.py")

    # 1. Import
    insert_after(
        root, "app/gui/main_window.py",
        anchor=("from app.gui.dependency_tree_dialog import DependencyTreeDialog\n"
                "# === END AUTO-GENERATED ==="),
        block=MW_IMPORT_BLOCK,
        marker="# === PERSISTENCE: PHASE1 (imports) ===",
    )

    # 2. Init del estado de persistencia
    insert_after(
        root, "app/gui/main_window.py",
        anchor="        self.config     = ExportConfig()",
        block=MW_INIT_BLOCK,
        marker="# === PERSISTENCE: PHASE1 (init) ===",
    )

    # 3. Registrar callback en el árbol
    insert_after(
        root, "app/gui/main_window.py",
        anchor=('        self.tree.bind("<ButtonRelease-1>",  '
                'lambda _: self.root.after(50, self._refresh_selection_stats))'),
        block=MW_CALLBACK_BLOCK,
        marker="# === PERSISTENCE: PHASE1 (callback) ===",
    )

    # 4. Insertar método _on_tree_check_change antes del bloque de handlers
    insert_before(
        root, "app/gui/main_window.py",
        anchor=("    # ── UI event handlers "
                "────────────────────────────────────────────────"
                "─────────────────"),
        block=MW_METHOD_BLOCK,
        marker="# === PERSISTENCE: PHASE1 (method) ===",
    )

    # 5. Restaurar estado al recargar el árbol
    insert_after(
        root, "app/gui/main_window.py",
        anchor=('                rel_file = os.path.join(rel_dir, f) '
                'if rel_dir != "." else f\n'
                '                self.tree.insert_file(parent_item, rel_file)'),
        block=MW_RELOAD_BLOCK,
        marker="# === PERSISTENCE: PHASE1 (reload) ===",
    )

    # 6. Persistir tras el análisis
    insert_after(
        root, "app/gui/main_window.py",
        anchor=("        result = analyzer.analyze(folder, "
                "max_file_size_mb=max_file_mb)"),
        block=MW_ANALYZE_BLOCK,
        marker="# === PERSISTENCE: PHASE1 (analyze) ===",
    )


# ---------------------------------------------------------------------------
# Validación final
# ---------------------------------------------------------------------------

def validate_syntax(root: Path, rel_paths) -> None:
    info("--- Validando sintaxis (py_compile) ---")
    for rel in rel_paths:
        full = root / rel
        if not full.is_file():
            continue
        try:
            py_compile.compile(str(full), doraise=True)
            info(f"Sintaxis OK: {rel}")
        except py_compile.PyCompileError as exc:
            error(f"Sintaxis inválida en {rel}: {exc}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Aplica la Fase 1 (persistencia SQLite) al proyecto agente."
    )
    p.add_argument(
        "project_root", nargs="?", default=".",
        help="Ruta raíz del proyecto (por defecto: directorio actual).",
    )
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
    print()

    try:
        apply_all(root)
    except Exception as exc:
        error(str(exc))
        print()
        info("Proceso detenido. No se continúan aplicando cambios.")
        _print_summary()
        return 1

    print()
    info("--- Resumen final ---")
    _print_summary()

    # Validación sintáctica
    validate_syntax(root, [
        "app/core/storage/__init__.py",
        "app/core/storage/database.py",
        "app/core/project_analyzer.py",
        "app/gui/file_tree.py",
        "app/gui/main_window.py",
    ])

    print()
    info("Fase 1 aplicada. Reinicia la aplicación para probar.")
    return 0 if STATS["errors"] == 0 else 1


def _print_summary() -> None:
    print(f"Archivos modificados: {STATS['modified']}")
    print(f"Archivos creados: {STATS['created']}")
    print(f"Archivos omitidos: {STATS['skipped']}")
    print(f"Backups creados: {STATS['backups']}")
    print(f"Errores: {STATS['errors']}")


if __name__ == "__main__":
    sys.exit(main())