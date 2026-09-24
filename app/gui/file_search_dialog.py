"""File search dialog with per-file dependency analysis action."""
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
