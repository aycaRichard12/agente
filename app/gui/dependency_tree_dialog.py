"""Dependency tree dialog. Reuses CheckboxTreeview and integrates with existing file selection."""
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
