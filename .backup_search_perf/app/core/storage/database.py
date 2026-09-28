"""
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
        self._conn = sqlite3.connect(self.db_path, timeout=10.0)
        self._conn.row_factory = sqlite3.Row
        self._conn.execute("PRAGMA foreign_keys = ON")
        self._conn.execute("PRAGMA journal_mode = WAL")
        self._conn.execute("PRAGMA synchronous = NORMAL")
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

    # === PHASE 2: DELTA SCAN ===
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
