#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
apply_changes.py
Script para aplicar automáticamente todos los cambios del buscador de archivos
y árbol de dependencias al proyecto "agente".

Uso:
    python apply_changes.py                     # Aplica sobre el directorio actual
    python apply_changes.py --root /ruta/proyecto
    python apply_changes.py --dry-run           # Solo muestra qué haría
    python apply_changes.py --no-backup         # No crea respaldos

El script es idempotente: puede ejecutarse varias veces sin dañar el proyecto.
"""

import argparse
import os
import shutil
import sys
from datetime import datetime
from pathlib import Path


# ---------------------------------------------------------------------------
# Utilidades
# ---------------------------------------------------------------------------

BACKUP_DIRNAME = ".backup_apply_changes"
MARKER_NEW_FILES = "# === AUTO-GENERATED: file_search_dependency_feature ==="


def log(msg, level="INFO"):
    prefix = {
        "INFO": "[INFO]",
        "OK":   "[  OK ]",
        "WARN": "[WARN]",
        "ERR":  "[FAIL]",
        "SKIP": "[SKIP]",
    }.get(level, "[INFO]")
    print(f"{prefix} {msg}")


def ensure_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)


def backup_file(path: Path, backup_root: Path, dry_run: bool = False):
    if not path.is_file():
        return
    rel = path.name
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    dst = backup_root / f"{rel}.{ts}.bak"
    if dry_run:
        log(f"(dry-run) respaldaría {path} -> {dst}", "SKIP")
        return
    ensure_dir(backup_root)
    shutil.copy2(path, dst)
    log(f"Respaldo creado: {dst}", "OK")


def write_file(path: Path, content: str, dry_run: bool = False, force: bool = False):
    """Escribe un archivo. Si existe y no es force, avisa y omite."""
    if path.exists() and not force:
        log(f"Ya existe (no se sobreescribe): {path}", "SKIP")
        return False
    if dry_run:
        log(f"(dry-run) escribiría {path} ({len(content)} bytes)", "SKIP")
        return True
    ensure_dir(path.parent)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    log(f"Archivo escrito: {path}", "OK")
    return True


def append_block_if_missing(path: Path, marker: str, block: str,
                            dry_run: bool = False, position: str = "end",
                            anchor: str = None):
    """
    Agrega un bloque al archivo solo si el marcador no está presente.
    position = 'end' | 'after_anchor'
    """
    if not path.is_file():
        log(f"No existe, se omite: {path}", "ERR")
        return False

    text = path.read_text(encoding="utf-8")

    if marker in text:
        log(f"Bloque ya presente en {path} (marcador encontrado)", "SKIP")
        return False

    if dry_run:
        log(f"(dry-run) agregaría bloque a {path}", "SKIP")
        return True

    if position == "after_anchor" and anchor and anchor in text:
        idx = text.index(anchor) + len(anchor)
        new_text = text[:idx] + "\n" + block + "\n" + text[idx:]
    else:
        if not text.endswith("\n"):
            text += "\n"
        new_text = text + "\n" + block + "\n"

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    log(f"Bloque agregado a {path}", "OK")
    return True


def replace_block(path: Path, old: str, new: str,
                  dry_run: bool = False) -> bool:
    """Reemplaza una subcadena exacta por otra. Solo si old está presente."""
    if not path.is_file():
        log(f"No existe: {path}", "ERR")
        return False

    text = path.read_text(encoding="utf-8")
    if old not in text:
        log(f"Patrón no encontrado en {path}", "SKIP")
        return False

    if dry_run:
        log(f"(dry-run) reemplazaría bloque en {path}", "SKIP")
        return True

    new_text = text.replace(old, new, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    log(f"Bloque reemplazado en {path}", "OK")
    return True


# ---------------------------------------------------------------------------
# Contenido de archivos nuevos
# ---------------------------------------------------------------------------

DEPENDENCY_GRAPH_PY = '''"""
Dependency graph/resolver for project files.
Resolves imports/includes/requires to real project files and builds a dependency tree.
"""
import os
import re
from dataclasses import dataclass, field
from typing import List, Dict, Set, Optional

from app.core.dependency_detector import DependencyDetector
from app.utils.file_utils import safe_read_file


@dataclass
class DependencyNode:
    rel_path: str
    depth: int
    children: List["DependencyNode"] = field(default_factory=list)
    is_cycle: bool = False
    is_repeated: bool = False
    external: Optional[str] = None


class DependencyResolver:
    def __init__(
        self,
        folder_path: str,
        excluded_dirs: Optional[Set[str]] = None,
        detector: Optional[DependencyDetector] = None,
        max_read_bytes: int = 200_000,
    ):
        self.folder_path = os.path.abspath(folder_path)
        self.excluded_dirs = set(excluded_dirs or [])
        self.detector = detector or DependencyDetector()
        self.max_read_bytes = max_read_bytes

        self._file_index: Dict[str, str] = {}
        self._module_index: Dict[str, str] = {}
        self._content_cache: Dict[str, str] = {}
        self._deps_cache: Dict[str, List[str]] = {}
        self._expanded: Set[str] = set()

        self._build_index()

    # ------------------------------------------------------------------
    # Index
    # ------------------------------------------------------------------
    def _build_index(self) -> None:
        if not self.folder_path or not os.path.isdir(self.folder_path):
            return

        for dirpath, dirnames, filenames in os.walk(self.folder_path):
            dirnames[:] = [d for d in dirnames if d not in self.excluded_dirs]

            for f in filenames:
                abs_p = os.path.join(dirpath, f)
                rel = os.path.relpath(abs_p, self.folder_path).replace("\\\\", "/")
                self._file_index[rel] = abs_p

                if f.endswith(".py"):
                    mod = rel[:-3].replace("/", ".")
                    if mod.endswith(".__init__"):
                        mod = mod[: -len(".__init__")]
                    self._module_index[mod] = rel

    def _normalize(self, rel_path: str) -> str:
        return rel_path.replace("\\\\", "/").lstrip("./")

    def _read(self, rel_path: str) -> str:
        rel_path = self._normalize(rel_path)
        if rel_path in self._content_cache:
            return self._content_cache[rel_path]

        abs_p = self._file_index.get(rel_path)
        if not abs_p or not os.path.isfile(abs_p):
            self._content_cache[rel_path] = ""
            return ""

        content = safe_read_file(abs_p, max_bytes=self.max_read_bytes)
        self._content_cache[rel_path] = content
        return content

    # ------------------------------------------------------------------
    # Dependency detection
    # ------------------------------------------------------------------
    def get_dependencies(self, rel_path: str) -> List[str]:
        rel_path = self._normalize(rel_path)
        if rel_path in self._deps_cache:
            return self._deps_cache[rel_path]

        content = self._read(rel_path)
        if not content:
            self._deps_cache[rel_path] = []
            return []

        deps = self.detector.detect_file_dependencies(rel_path, content)
        self._deps_cache[rel_path] = deps
        return deps

    # ------------------------------------------------------------------
    # Resolution
    # ------------------------------------------------------------------
    def resolve_dependency(self, source_rel_path: str, dep_string: str) -> List[str]:
        source_rel_path = self._normalize(source_rel_path)
        ext = os.path.splitext(source_rel_path)[1].lower()

        if ext == ".py":
            candidates = self._resolve_python_dep(source_rel_path, dep_string)
        elif ext in (".js", ".jsx", ".ts", ".tsx", ".vue", ".mjs", ".cjs"):
            candidates = self._resolve_js_dep(source_rel_path, dep_string)
        elif ext == ".php":
            candidates = self._resolve_php_dep(source_rel_path, dep_string)
        else:
            candidates = self._resolve_by_basename(dep_string)

        result: List[str] = []
        for c in candidates:
            norm = self._normalize(c)
            if norm in self._file_index and norm not in result:
                result.append(norm)
        return result

    def _resolve_python_dep(self, source_rel: str, dep: str) -> List[str]:
        dep = dep.strip()

        if dep.startswith("import "):
            rest = dep[len("import "):].strip()
            parts = [p.strip() for p in rest.split(",")]
            result: List[str] = []
            for p in parts:
                p = p.split(" as ")[0].strip()
                result.extend(self._module_to_rel(p))
            return result

        if dep.startswith("from "):
            rest = dep[len("from "):].strip()
            if " import " not in rest:
                return []

            module, _names = rest.split(" import ", 1)
            module = module.strip()

            if module.startswith("."):
                base_dir = os.path.dirname(source_rel)
                dots = len(module) - len(module.lstrip("."))
                module_name = module.lstrip(".")

                up = max(0, dots - 1)
                parts = base_dir.split("/") if base_dir else []
                if up > 0:
                    parts = parts[:-up] if up <= len(parts) else []

                rel_dir = "/".join(parts)
                if module_name:
                    mod_path = (rel_dir + "/" + module_name.replace(".", "/")) if rel_dir else module_name.replace(".", "/")
                else:
                    mod_path = rel_dir

                return self._path_to_rel_candidates(mod_path)

            return self._module_to_rel(module)

        return []

    def _module_to_rel(self, module: str) -> List[str]:
        module = module.strip()
        if not module:
            return []

        if module in self._module_index:
            return [self._module_index[module]]

        pkg_init = module + ".__init__"
        if pkg_init in self._module_index:
            return [self._module_index[pkg_init]]

        path_py = module.replace(".", "/") + ".py"
        if path_py in self._file_index:
            return [path_py]

        path_init = module.replace(".", "/") + "/__init__.py"
        if path_init in self._file_index:
            return [path_init]

        return []

    def _path_to_rel_candidates(self, base_path: str) -> List[str]:
        base_path = self._normalize(base_path)
        candidates = []
        for cand in (
            base_path + ".py",
            base_path + "/__init__.py",
            base_path,
        ):
            if cand in self._file_index:
                candidates.append(cand)
        return candidates

    def _resolve_js_dep(self, source_rel: str, dep: str) -> List[str]:
        m = re.search(r'[\\'"]([^\\'"]+)[\\'"]', dep)
        if not m:
            return []

        raw = m.group(1)
        if not raw.startswith("."):
            return []

        base_dir = os.path.dirname(source_rel)
        target = os.path.normpath(os.path.join(base_dir, raw)).replace("\\\\", "/")

        candidates: List[str] = []
        for ext in ("", ".js", ".jsx", ".ts", ".tsx", ".vue", ".json", ".mjs", ".cjs"):
            cand = target + ext
            if cand in self._file_index:
                candidates.append(cand)

        for ext in (".js", ".jsx", ".ts", ".tsx", ".vue"):
            cand = target + "/index" + ext
            if cand in self._file_index:
                candidates.append(cand)

        return candidates

    def _resolve_php_dep(self, source_rel: str, dep: str) -> List[str]:
        m = re.search(r'[\\'"]([^\\'"]+)[\\'"]', dep)
        if not m:
            return []

        raw = m.group(1)

        if raw.startswith("."):
            base_dir = os.path.dirname(source_rel)
            target = os.path.normpath(os.path.join(base_dir, raw)).replace("\\\\", "/")
            for cand in (target, target + ".php"):
                if cand in self._file_index:
                    return [cand]
            return []

        for cand in (raw, raw + ".php"):
            if cand in self._file_index:
                return [cand]

        return []

    def _resolve_by_basename(self, dep: str) -> List[str]:
        base = os.path.basename(dep)
        return [rel for rel in self._file_index if os.path.basename(rel) == base]

    # ------------------------------------------------------------------
    # Tree building
    # ------------------------------------------------------------------
    def build_tree(self, root_rel_path: str, max_depth: int = 50) -> DependencyNode:
        root_rel_path = self._normalize(root_rel_path)
        self._expanded.clear()
        return self._build_node(root_rel_path, depth=0, ancestors=set(), max_depth=max_depth)

    def _build_node(
        self,
        rel_path: str,
        depth: int,
        ancestors: Set[str],
        max_depth: int,
    ) -> DependencyNode:
        node = DependencyNode(rel_path=rel_path, depth=depth)

        if depth >= max_depth:
            return node

        if rel_path in ancestors:
            node.is_cycle = True
            return node

        if rel_path in self._expanded:
            node.is_repeated = True
            return node

        self._expanded.add(rel_path)

        new_ancestors = set(ancestors)
        new_ancestors.add(rel_path)

        for dep in self.get_dependencies(rel_path):
            for child_rel in self.resolve_dependency(rel_path, dep):
                child = self._build_node(
                    child_rel,
                    depth=depth + 1,
                    ancestors=new_ancestors,
                    max_depth=max_depth,
                )
                node.children.append(child)

        return node
'''


DEPENDENCY_TREE_DIALOG_PY = '''"""Dependency tree dialog. Reuses CheckboxTreeview and integrates with existing file selection."""
import tkinter as tk
from tkinter import ttk
from typing import Callable, List, Optional, Set

from app.core.dependency_graph import DependencyResolver, DependencyNode
from app.gui.file_tree import CheckboxTreeview

C_BG = "#1e2330"
C_PANEL = "#252b3b"
C_BORDER = "#323a50"
C_ACCENT = "#4f8ef7"
C_TEXT = "#e8eaf0"
C_TEXT2 = "#8b92a8"
C_ENTRY = "#2a3148"


class DependencyTreeDialog(tk.Toplevel):
    def __init__(
        self,
        parent: tk.Tk,
        folder_path: str,
        root_rel_path: str,
        excluded_dirs: Optional[Set[str]] = None,
        on_apply_selection: Optional[Callable[[List[str]], None]] = None,
    ):
        super().__init__(parent)
        self.folder_path = folder_path
        self.root_rel_path = root_rel_path
        self.on_apply_selection = on_apply_selection

        self.title(f"🌳 Dependencias: {root_rel_path}")
        self.geometry("900x650")
        self.minsize(700, 480)
        self.configure(bg=C_BG)

        self.transient(parent)
        self.grab_set()

        try:
            self.resolver = DependencyResolver(folder_path, excluded_dirs=excluded_dirs)
            self.root_node = self.resolver.build_tree(root_rel_path)
        except Exception as exc:
            tk.Label(
                self,
                text=f"Error al construir árbol: {exc}",
                bg=C_BG, fg=C_TEXT, font=("Segoe UI", 10),
            ).pack(padx=20, pady=20)
            self.root_node = None

        self._build_header()
        self._build_tree()
        self._build_buttons()

        if self.root_node is not None:
            self._insert_node("", self.root_node, is_root=True)

    def _build_header(self):
        hdr = tk.Frame(self, bg=C_PANEL, padx=14, pady=10)
        hdr.pack(fill=tk.X)

        tk.Label(
            hdr,
            text=f"🌳 Árbol de dependencias: {self.root_rel_path}",
            font=("Segoe UI", 12, "bold"),
            bg=C_PANEL,
            fg=C_TEXT,
        ).pack(anchor="w")

        tk.Label(
            hdr,
            text="Selecciona archivos o ramas y aplícalos al contexto principal.",
            font=("Segoe UI", 8),
            bg=C_PANEL,
            fg=C_TEXT2,
        ).pack(anchor="w")

    def _build_tree(self):
        container = tk.Frame(self, bg=C_BG, padx=10, pady=6)
        container.pack(fill=tk.BOTH, expand=True)

        self.tree = CheckboxTreeview(container)
        sy = ttk.Scrollbar(container, orient=tk.VERTICAL, command=self.tree.yview)
        sx = ttk.Scrollbar(container, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscrollcommand=sy.set, xscrollcommand=sx.set)

        sy.pack(side=tk.RIGHT, fill=tk.Y)
        sx.pack(side=tk.BOTTOM, fill=tk.X)
        self.tree.pack(fill=tk.BOTH, expand=True)

    def _build_buttons(self):
        bar = tk.Frame(self, bg=C_PANEL, padx=10, pady=8)
        bar.pack(fill=tk.X, side=tk.BOTTOM)

        ttk.Button(bar, text="Seleccionar raíz", command=self._select_root).pack(side=tk.LEFT, padx=2)
        ttk.Button(bar, text="Seleccionar rama", command=self._select_branch).pack(side=tk.LEFT, padx=2)
        ttk.Button(bar, text="Seleccionar todos", command=self._select_all).pack(side=tk.LEFT, padx=2)
        ttk.Button(bar, text="Deseleccionar rama", command=self._deselect_branch).pack(side=tk.LEFT, padx=2)

        ttk.Button(bar, text="✅ Aplicar selección", command=self._apply).pack(side=tk.RIGHT, padx=2)
        ttk.Button(bar, text="Cerrar", command=self.destroy).pack(side=tk.RIGHT, padx=2)

    def _insert_node(self, parent_item: str, node: DependencyNode, is_root: bool = False):
        notes = []
        if node.is_cycle:
            notes.append("⟲ ciclo")
        if node.is_repeated:
            notes.append("♻ ya analizado")

        icon = "📄"
        if node.is_cycle:
            icon = "🔁"
        elif node.is_repeated:
            icon = "🔂"
        elif node.children:
            icon = "📂"

        item = self.tree.insert(
            parent_item,
            "end",
            text=icon,
            values=("☐", node.rel_path),
            tags=("unchecked",),
        )

        for child in node.children:
            self._insert_node(item, child)

        return item

    def _current_item(self):
        sel = self.tree.selection()
        return sel[0] if sel else None

    def _select_root(self):
        if self.tree.get_children():
            root = self.tree.get_children()[0]
            self.tree.check_item(root)

    def _select_branch(self):
        item = self._current_item()
        if item:
            self.tree.check_item(item)

    def _select_all(self):
        self.tree.select_all()

    def _deselect_branch(self):
        item = self._current_item()
        if item:
            self.tree.uncheck_item(item)

    def _apply(self):
        selected = self.tree.get_checked_files()
        if self.on_apply_selection:
            self.on_apply_selection(selected)
        self.destroy()
'''


FILE_SEARCH_DIALOG_PY = '''"""File search dialog with per-file dependency analysis action."""
import os
import tkinter as tk
from tkinter import ttk
from typing import Callable, List, Optional, Set

from app.core.project_scanner import scan_directory

C_BG = "#1e2330"
C_PANEL = "#252b3b"
C_BORDER = "#323a50"
C_ACCENT = "#4f8ef7"
C_TEXT = "#e8eaf0"
C_TEXT2 = "#8b92a8"
C_ENTRY = "#2a3148"


class FileSearchDialog(tk.Toplevel):
    def __init__(
        self,
        parent: tk.Tk,
        folder_path: str,
        excluded_dirs: Optional[Set[str]] = None,
        on_analyze_dependencies: Optional[Callable[[str], None]] = None,
    ):
        super().__init__(parent)
        self.folder_path = folder_path
        self.excluded_dirs = excluded_dirs or set()
        self.on_analyze_dependencies = on_analyze_dependencies

        self.title("🔎 Buscador de archivos")
        self.geometry("820x560")
        self.minsize(640, 420)
        self.configure(bg=C_BG)

        self.transient(parent)
        self.grab_set()

        self.search_var = tk.StringVar()
        self.all_files: List[str] = []

        self._build_header()
        self._build_results()
        self._load_files()

    def _build_header(self):
        hdr = tk.Frame(self, bg=C_PANEL, padx=12, pady=10)
        hdr.pack(fill=tk.X)

        tk.Label(
            hdr,
            text="🔎 Buscar archivos del proyecto",
            font=("Segoe UI", 12, "bold"),
            bg=C_PANEL,
            fg=C_TEXT,
        ).pack(anchor="w")

        row = tk.Frame(hdr, bg=C_PANEL)
        row.pack(fill=tk.X, pady=(6, 0))

        self.entry = ttk.Entry(row, textvariable=self.search_var, font=("Consolas", 9))
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 6))
        self.entry.bind("<KeyRelease>", lambda _e: self._refresh_results())

        ttk.Button(row, text="Buscar", command=self._refresh_results).pack(side=tk.LEFT)
        ttk.Button(row, text="Limpiar", command=self._clear_search).pack(side=tk.LEFT, padx=(6, 0))

    def _build_results(self):
        container = tk.Frame(self, bg=C_ENTRY, bd=1, relief="flat",
                             highlightbackground=C_BORDER, highlightthickness=1)
        container.pack(fill=tk.BOTH, expand=True, padx=12, pady=8)

        self.canvas = tk.Canvas(container, bg=C_ENTRY, bd=0, highlightthickness=0)
        scrollbar = ttk.Scrollbar(container, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scroll_frame = tk.Frame(self.canvas, bg=C_ENTRY)

        self.scroll_frame.bind(
            "<Configure>",
            lambda _e: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
        )
        self.canvas_window = self.canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")

        def _on_resize(event):
            self.canvas.itemconfig(self.canvas_window, width=event.width)

        self.canvas.bind("<Configure>", _on_resize)

        def _on_mousewheel(event):
            if event.delta:
                self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
            elif event.num == 4:
                self.canvas.yview_scroll(-1, "units")
            elif event.num == 5:
                self.canvas.yview_scroll(1, "units")

        self.canvas.bind_all("<MouseWheel>", _on_mousewheel)
        self.canvas.bind_all("<Button-4>", _on_mousewheel)
        self.canvas.bind_all("<Button-5>", _on_mousewheel)

        self.canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def _load_files(self):
        try:
            self.all_files = scan_directory(
                self.folder_path,
                self.excluded_dirs,
                allowed_extensions=None,
            )
        except Exception:
            self.all_files = []
        self._refresh_results()

    def _clear_search(self):
        self.search_var.set("")
        self._refresh_results()

    def _refresh_results(self):
        query = self.search_var.get().strip().lower()

        for child in self.scroll_frame.winfo_children():
            child.destroy()

        matches = [
            rel for rel in self.all_files
            if not query or query in rel.lower()
        ]

        if not matches:
            tk.Label(
                self.scroll_frame,
                text="(Sin resultados)",
                font=("Segoe UI", 9, "italic"),
                bg=C_ENTRY,
                fg=C_TEXT2,
            ).pack(anchor="w", padx=10, pady=10)
            return

        for rel in matches:
            row = tk.Frame(self.scroll_frame, bg=C_ENTRY, padx=8, pady=3)
            row.pack(fill=tk.X)

            tk.Label(
                row,
                text=rel,
                font=("Consolas", 9),
                bg=C_ENTRY,
                fg=C_TEXT,
                anchor="w",
            ).pack(side=tk.LEFT, fill=tk.X, expand=True)

            ttk.Button(
                row,
                text="🔗 Dependencias",
                command=lambda r=rel: self._analyze(r),
            ).pack(side=tk.RIGHT)

    def _analyze(self, rel_path: str):
        if self.on_analyze_dependencies:
            self.on_analyze_dependencies(rel_path)
'''


TEST_DEPENDENCY_GRAPH_PY = '''import os
import shutil
import tempfile
import unittest

from app.core.dependency_graph import DependencyResolver


class TestDependencyResolver(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="test_dep_graph_")

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _write(self, rel_path, content):
        path = os.path.join(self.tmp, rel_path)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

    def test_file_without_dependencies(self):
        self._write("a.py", "x = 1\\n")
        resolver = DependencyResolver(self.tmp)
        node = resolver.build_tree("a.py")
        self.assertEqual(node.rel_path, "a.py")
        self.assertEqual(node.children, [])

    def test_single_dependency(self):
        self._write("a.py", "import b\\n")
        self._write("b.py", "x = 1\\n")
        resolver = DependencyResolver(self.tmp)
        node = resolver.build_tree("a.py")
        self.assertEqual(len(node.children), 1)
        self.assertEqual(node.children[0].rel_path, "b.py")

    def test_chain_dependencies(self):
        self._write("a.py", "import b\\n")
        self._write("b.py", "import c\\n")
        self._write("c.py", "x = 1\\n")
        resolver = DependencyResolver(self.tmp)
        node = resolver.build_tree("a.py")
        self.assertEqual(node.children[0].rel_path, "b.py")
        self.assertEqual(node.children[0].children[0].rel_path, "c.py")

    def test_circular_dependency(self):
        self._write("a.py", "import b\\n")
        self._write("b.py", "import c\\n")
        self._write("c.py", "import a\\n")
        resolver = DependencyResolver(self.tmp)
        node = resolver.build_tree("a.py")
        c = node.children[0].children[0]
        self.assertEqual(c.rel_path, "c.py")
        self.assertTrue(c.children[0].is_cycle)

    def test_repeated_dependency(self):
        self._write("a.py", "import b\\nimport c\\n")
        self._write("b.py", "import d\\n")
        self._write("c.py", "import d\\n")
        self._write("d.py", "x = 1\\n")
        resolver = DependencyResolver(self.tmp)
        node = resolver.build_tree("a.py")
        b = next(ch for ch in node.children if ch.rel_path == "b.py")
        c = next(ch for ch in node.children if ch.rel_path == "c.py")
        self.assertEqual(b.children[0].rel_path, "d.py")
        self.assertEqual(c.children[0].rel_path, "d.py")
        self.assertTrue(c.children[0].is_repeated)

    def test_external_dependency_ignored(self):
        self._write("a.py", "import os\\n")
        resolver = DependencyResolver(self.tmp)
        node = resolver.build_tree("a.py")
        self.assertEqual(node.children, [])

    def test_missing_dependency_ignored(self):
        self._write("a.py", "import missing_module\\n")
        resolver = DependencyResolver(self.tmp)
        node = resolver.build_tree("a.py")
        self.assertEqual(node.children, [])


if __name__ == "__main__":
    unittest.main()
'''


# ---------------------------------------------------------------------------
# Bloques de código a insertar en main_window.py
# ---------------------------------------------------------------------------

MAIN_WINDOW_IMPORTS_BLOCK = """# === AUTO-GENERATED: file_search_dependency_feature ===
from app.gui.file_search_dialog import FileSearchDialog
from app.gui.dependency_tree_dialog import DependencyTreeDialog
# === END AUTO-GENERATED ===
"""

MAIN_WINDOW_METHODS_BLOCK = """    # === AUTO-GENERATED: file_search_dependency_feature ===
    def on_open_file_search(self):
        folder = self.var_folder.get()
        if not folder or not os.path.isdir(folder):
            dialogs.show_warning("Atención", "Selecciona una carpeta del proyecto primero.")
            return

        excluded = self.selector.get_selection().excluded_dirs
        FileSearchDialog(
            self.root,
            folder,
            excluded_dirs=excluded,
            on_analyze_dependencies=self.open_dependency_tree,
        )

    def open_dependency_tree(self, rel_path: str):
        folder = self.var_folder.get()
        if not folder or not os.path.isdir(folder):
            dialogs.show_warning("Atención", "Selecciona una carpeta del proyecto primero.")
            return

        excluded = self.selector.get_selection().excluded_dirs
        DependencyTreeDialog(
            self.root,
            folder,
            rel_path,
            excluded_dirs=excluded,
            on_apply_selection=self.apply_dependency_selection,
        )

    def apply_dependency_selection(self, selected_files: List[str]):
        if not selected_files:
            return

        existing = set(self.tree.get_checked_files())
        combined = existing | set(selected_files)

        self.tree.set_checked_files(combined)
        self.selector.set_checked_folder_files(self.tree.get_checked_files())
        self._refresh_selection_stats()

        self.sv_status.set(
            f"✓ {len(selected_files)} dependencia(s) agregadas/actualizadas en la selección."
        )
    # === END AUTO-GENERATED ===
"""


CORE_INIT_NEW = '''"""Core package initialization."""
from app.core.project_scanner import scan_directory
from app.core.file_selector import FileSelectorManager
from app.core.file_reader import read_and_format_file
from app.core.project_structure import build_folder_tree_str
from app.core.dependency_detector import DependencyDetector, detect_project_dependencies
from app.core.dependency_graph import DependencyResolver, DependencyNode

__all__ = [
    "scan_directory",
    "FileSelectorManager",
    "read_and_format_file",
    "build_folder_tree_str",
    "DependencyDetector",
    "detect_project_dependencies",
    "DependencyResolver",
    "DependencyNode",
]
'''


# ---------------------------------------------------------------------------
# Aplicación de cambios
# ---------------------------------------------------------------------------

def apply_changes(root: Path, dry_run: bool = False, backup: bool = True):
    backup_root = root / BACKUP_DIRNAME
    if backup and not dry_run:
        ensure_dir(backup_root)

    log(f"Raíz del proyecto: {root}")
    log(f"Modo dry-run: {dry_run}")
    log(f"Respaldos: {'activado' if backup else 'desactivado'}")
    print()

    # -----------------------------------------------------------------
    # 1. Verificación básica de estructura
    # -----------------------------------------------------------------
    required = [
        root / "app" / "core" / "dependency_detector.py",
        root / "app" / "core" / "file_selector.py",
        root / "app" / "core" / "project_scanner.py",
        root / "app" / "gui" / "file_tree.py",
        root / "app" / "gui" / "main_window.py",
        root / "app" / "models" / "project.py",
    ]
    missing = [str(p) for p in required if not p.is_file()]
    if missing:
        log("Estructura del proyecto no reconocida. Archivos faltantes:", "ERR")
        for m in missing:
            log(f"  - {m}", "ERR")
        sys.exit(1)

    # -----------------------------------------------------------------
    # 2. Respaldos
    # -----------------------------------------------------------------
    if backup:
        log("--- Creando respaldos ---")
        for f in [
            root / "app" / "core" / "__init__.py",
            root / "app" / "gui" / "main_window.py",
        ]:
            backup_file(f, backup_root, dry_run=dry_run)
        print()

    # -----------------------------------------------------------------
    # 3. Nuevos archivos
    # -----------------------------------------------------------------
    log("--- Creando archivos nuevos ---")
    write_file(
        root / "app" / "core" / "dependency_graph.py",
        DEPENDENCY_GRAPH_PY,
        dry_run=dry_run,
    )
    write_file(
        root / "app" / "gui" / "dependency_tree_dialog.py",
        DEPENDENCY_TREE_DIALOG_PY,
        dry_run=dry_run,
    )
    write_file(
        root / "app" / "gui" / "file_search_dialog.py",
        FILE_SEARCH_DIALOG_PY,
        dry_run=dry_run,
    )
    write_file(
        root / "tests" / "test_dependency_graph.py",
        TEST_DEPENDENCY_GRAPH_PY,
        dry_run=dry_run,
    )
    print()

    # -----------------------------------------------------------------
    # 4. Modificar app/core/__init__.py
    # -----------------------------------------------------------------
    log("--- Actualizando app/core/__init__.py ---")
    core_init = root / "app" / "core" / "__init__.py"
    if core_init.is_file():
        current = core_init.read_text(encoding="utf-8")
        if "DependencyResolver" in current and "dependency_graph" in current:
            log("app/core/__init__.py ya actualizado", "SKIP")
        else:
            if dry_run:
                log("(dry-run) reemplazaría app/core/__init__.py", "SKIP")
            else:
                with open(core_init, "w", encoding="utf-8") as f:
                    f.write(CORE_INIT_NEW)
                log(f"Actualizado: {core_init}", "OK")
    print()

    # -----------------------------------------------------------------
    # 5. Modificar app/gui/main_window.py
    # -----------------------------------------------------------------
    log("--- Modificando app/gui/main_window.py ---")
    mw = root / "app" / "gui" / "main_window.py"
    mw_text = mw.read_text(encoding="utf-8")

    # 5.1 Importar diálogos
    if "file_search_dialog" not in mw_text and "FileSearchDialog" not in mw_text:
        anchor_import = "from app.gui import dialogs"
        if anchor_import in mw_text:
            append_block_if_missing(
                mw,
                marker=MARKER_NEW_FILES,
                block=MAIN_WINDOW_IMPORTS_BLOCK,
                dry_run=dry_run,
                position="after_anchor",
                anchor=anchor_import,
            )
        else:
            log("No se encontró 'from app.gui import dialogs' para anclar imports", "WARN")
    else:
        log("Imports de diálogos ya presentes", "SKIP")

    # 5.2 Insertar botón "Buscador" en toolbar del árbol
    mw_text = mw.read_text(encoding="utf-8")
    if 'text="🔎 Buscador"' not in mw_text:
        old_btn = (
            'ttk.Button(tb, text="🧠 Selección Inteligente", style="Accent.TButton",\n'
            '                   command=self.on_intelligent_context_select).pack(side=tk.LEFT, padx=(0, 4))\n'
        )
        new_btn = old_btn + (
            '        ttk.Button(tb, text="🔎 Buscador", style="Accent.TButton",\n'
            '                   command=self.on_open_file_search).pack(side=tk.LEFT, padx=(0, 4))\n'
        )
        replace_block(mw, old_btn, new_btn, dry_run=dry_run)
    else:
        log("Botón Buscador ya presente", "SKIP")

    # 5.3 Insertar métodos nuevos (antes de on_copy_clipboard)
    mw_text = mw.read_text(encoding="utf-8")
    if "def on_open_file_search" not in mw_text:
        anchor = "    def on_copy_clipboard(self):"
        if anchor in mw_text:
            append_block_if_missing(
                mw,
                marker=MARKER_NEW_FILES + "_methods",
                block=MAIN_WINDOW_METHODS_BLOCK,
                dry_run=dry_run,
                position="after_anchor",
                anchor=anchor,
            )
        else:
            log("No se encontró 'on_copy_clipboard' para anclar métodos nuevos", "WARN")
    else:
        log("Métodos on_open_file_search ya presentes", "SKIP")

    print()
    log("=== Proceso finalizado ===", "OK")
    if dry_run:
        log("Ejecuta sin --dry-run para aplicar realmente los cambios.", "INFO")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Aplica los cambios del buscador de archivos y árbol de dependencias."
    )
    parser.add_argument("--root", default=".", help="Directorio raíz del proyecto agente.")
    parser.add_argument("--dry-run", action="store_true", help="No modifica nada, solo muestra.")
    parser.add_argument("--no-backup", action="store_true", help="No crea respaldos.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not root.is_dir():
        log(f"El directorio no existe: {root}", "ERR")
        sys.exit(1)

    apply_changes(
        root=root,
        dry_run=args.dry_run,
        backup=not args.no_backup,
    )


if __name__ == "__main__":
    main()