"""
Intelligent Context Dialog GUI Component.
Presents prioritized files (🔴 Critical, 🟠 Important, 🟡 Related, ⚪ Secondary),
allows user review, filtering, and manual modification before context generation.
"""
import os
import tkinter as tk
from tkinter import ttk
from typing import List, Callable, Optional, Dict

from app.core.intelligent_context import (
    PrioritizedFile,
    PRIORITY_CRITICAL,
    PRIORITY_IMPORTANT,
    PRIORITY_RELATED,
    PRIORITY_SECONDARY
)
from app.utils.file_utils import format_bytes

# Colour palette (aligned with main_window.py & analysis_dialog.py)
C_BG        = "#1e2330"
C_PANEL     = "#252b3b"
C_BORDER    = "#323a50"
C_ACCENT    = "#4f8ef7"
C_ACCENT_DK = "#3a6fcc"
C_SUCCESS   = "#3ecf8e"
C_WARN      = "#f5a623"
C_TEXT      = "#e8eaf0"
C_TEXT2     = "#8b92a8"
C_ENTRY     = "#2a3148"
C_TREE_SEL  = "#2f3d5c"


class IntelligentContextDialog(tk.Toplevel):
    """Modal dialog allowing user to review and adjust intelligent context file selection."""

    def __init__(
        self,
        parent: tk.Tk,
        problem_desc: str,
        prioritized_files: List[PrioritizedFile],
        on_confirm: Callable[[List[str]], None]
    ):
        super().__init__(parent)
        self.problem_desc = problem_desc
        self.prioritized_files = prioritized_files
        self.on_confirm = on_confirm
        self.file_vars: Dict[str, tk.BooleanVar] = {}

        self.title("🧠 Selección Inteligente de Contexto")
        self.geometry("960x700")
        self.minsize(800, 520)
        self.configure(bg=C_BG)

        # Make dialog modal and centered
        self.transient(parent)
        self.grab_set()
        self._center_window(parent)

        self._build_header()
        self._build_summary_bar()
        self._build_file_list()
        self._build_bottom_bar()

    def _center_window(self, parent: tk.Tk):
        self.update_idletasks()
        try:
            pw = parent.winfo_width()
            ph = parent.winfo_height()
            px = parent.winfo_rootx()
            py = parent.winfo_rooty()
            w = self.winfo_width()
            h = self.winfo_height()
            x = px + max(0, (pw - w) // 2)
            y = py + max(0, (ph - h) // 2)
            self.geometry(f"{w}x{h}+{x}+{y}")
        except Exception:
            pass

    def _build_header(self):
        hdr = tk.Frame(self, bg=C_PANEL, padx=16, pady=12, highlightthickness=1, highlightbackground=C_BORDER)
        hdr.pack(fill=tk.X)

        tk.Label(
            hdr,
            text="🧠  Selección Inteligente de Archivos de Contexto",
            font=("Segoe UI", 12, "bold"),
            bg=C_PANEL, fg=C_TEXT
        ).pack(anchor="w")

        short_desc = (self.problem_desc[:120] + "...") if len(self.problem_desc) > 120 else (self.problem_desc or "Sin descripción especificada")
        tk.Label(
            hdr,
            text=f"Problema reportado: \"{short_desc}\"",
            font=("Segoe UI", 9, "italic"),
            bg=C_PANEL, fg=C_ACCENT
        ).pack(anchor="w", pady=(2, 0))

    def _build_summary_bar(self):
        bar = tk.Frame(self, bg=C_BG, padx=16, pady=8)
        bar.pack(fill=tk.X)

        counts = {
            PRIORITY_CRITICAL: 0,
            PRIORITY_IMPORTANT: 0,
            PRIORITY_RELATED: 0,
            PRIORITY_SECONDARY: 0
        }
        for pf in self.prioritized_files:
            counts[pf.priority_level] = counts.get(pf.priority_level, 0) + 1

        badges_frame = tk.Frame(bar, bg=C_BG)
        badges_frame.pack(side=tk.LEFT)

        def _add_badge(parent, text, bg_color):
            f = tk.Frame(parent, bg=bg_color, padx=8, pady=3)
            f.pack(side=tk.LEFT, padx=3)
            tk.Label(f, text=text, font=("Segoe UI", 8, "bold"), bg=bg_color, fg="#ffffff").pack()

        _add_badge(badges_frame, f"🔴 Críticos ({counts[PRIORITY_CRITICAL]})", "#e74c3c")
        _add_badge(badges_frame, f"🟠 Importantes ({counts[PRIORITY_IMPORTANT]})", "#e67e22")
        _add_badge(badges_frame, f"🟡 Relacionados ({counts[PRIORITY_RELATED]})", "#f1c40f")
        _add_badge(badges_frame, f"⚪ Secundarios ({counts[PRIORITY_SECONDARY]})", "#7f8c8d")

        self.lbl_stats = tk.Label(
            bar,
            text="",
            font=("Segoe UI", 9, "bold"),
            bg=C_BG, fg=C_TEXT
        )
        self.lbl_stats.pack(side=tk.RIGHT)

    def _build_file_list(self):
        main_frame = tk.Frame(self, bg=C_PANEL, padx=12, pady=10, highlightthickness=1, highlightbackground=C_BORDER)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=16, pady=4)

        # Toolbar presets
        tb = tk.Frame(main_frame, bg=C_PANEL)
        tb.pack(fill=tk.X, pady=(0, 6))

        ttk.Button(tb, text="☑ Marcar todos", style="Neutral.TButton", command=self._select_all).pack(side=tk.LEFT, padx=(0, 4))
        ttk.Button(tb, text="☐ Desmarcar todos", style="Neutral.TButton", command=self._deselect_all).pack(side=tk.LEFT, padx=(0, 4))
        ttk.Button(tb, text="🔴 Solo Críticos e Importantes", style="Neutral.TButton", command=self._select_critical_important).pack(side=tk.LEFT)

        # Scrollable area
        list_container = tk.Frame(main_frame, bg=C_ENTRY, bd=1, relief="flat", highlightbackground=C_BORDER, highlightthickness=1)
        list_container.pack(fill=tk.BOTH, expand=True)

        canvas = tk.Canvas(list_container, bg=C_ENTRY, bd=0, highlightthickness=0)
        scrollbar = ttk.Scrollbar(list_container, orient=tk.VERTICAL, command=canvas.yview)
        scroll_frame = tk.Frame(canvas, bg=C_ENTRY)

        scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas_window = canvas.create_window((0, 0), window=scroll_frame, anchor="nw")

        def _on_resize(event):
            canvas.itemconfig(canvas_window, width=event.width)
        canvas.bind("<Configure>", _on_resize)

        # Mousewheel
        def _on_mw(event):
            if event.delta:
                canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
            elif event.num == 4:
                canvas.yview_scroll(-1, "units")
            elif event.num == 5:
                canvas.yview_scroll(1, "units")

        canvas.bind_all("<MouseWheel>", _on_mw)
        canvas.bind_all("<Button-4>", _on_mw)
        canvas.bind_all("<Button-5>", _on_mw)

        canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Populate rows
        for pf in self.prioritized_files:
            var = tk.BooleanVar(value=pf.is_selected)
            self.file_vars[pf.rel_path] = var

            row = tk.Frame(scroll_frame, bg=C_ENTRY, padx=8, pady=4, bd=0)
            row.pack(fill=tk.X, pady=1)

            # Icon / badge label
            lbl_badge = tk.Label(
                row,
                text=f"{pf.priority_icon} {pf.priority_label}",
                font=("Segoe UI", 8, "bold"),
                bg=C_ENTRY, fg=C_TEXT, width=14, anchor="w"
            )
            lbl_badge.pack(side=tk.LEFT)

            # Checkbox + rel_path
            cb = tk.Checkbutton(
                row,
                text=pf.rel_path,
                variable=var,
                font=("Consolas", 9, "bold" if pf.priority_level <= 2 else "normal"),
                bg=C_ENTRY,
                fg=C_TEXT if pf.priority_level <= 2 else C_TEXT2,
                activebackground=C_ENTRY,
                activeforeground=C_ACCENT,
                selectcolor=C_PANEL,
                anchor="w",
                command=self._update_stats
            )
            cb.pack(side=tk.LEFT, fill=tk.X, expand=True)

            # Size badge
            tk.Label(
                row,
                text=format_bytes(pf.size_bytes),
                font=("Consolas", 8),
                bg=C_ENTRY, fg=C_TEXT2, width=10, anchor="e"
            ).pack(side=tk.LEFT, padx=(4, 8))

            # Rationale tooltip/hint
            tk.Label(
                row,
                text=pf.reason,
                font=("Segoe UI", 8, "italic"),
                bg=C_ENTRY, fg=C_TEXT2, anchor="w"
            ).pack(side=tk.LEFT, padx=4)

        self._update_stats()

    def _build_bottom_bar(self):
        btn_bar = tk.Frame(self, bg=C_PANEL, padx=16, pady=12, highlightthickness=1, highlightbackground=C_BORDER)
        btn_bar.pack(fill=tk.X, side=tk.BOTTOM)

        ttk.Button(
            btn_bar,
            text="Cancelar",
            style="Neutral.TButton",
            command=self.destroy
        ).pack(side=tk.RIGHT, padx=(8, 0))

        ttk.Button(
            btn_bar,
            text="⚡ Aplicar Selección e Incluir en Contexto",
            style="Accent.TButton",
            command=self._on_confirm
        ).pack(side=tk.RIGHT)

    def _select_all(self):
        for var in self.file_vars.values():
            var.set(True)
        self._update_stats()

    def _deselect_all(self):
        for var in self.file_vars.values():
            var.set(False)
        self._update_stats()

    def _select_critical_important(self):
        for pf in self.prioritized_files:
            var = self.file_vars.get(pf.rel_path)
            if var:
                var.set(pf.priority_level <= PRIORITY_IMPORTANT)
        self._update_stats()

    def _update_stats(self):
        selected_files = [pf for pf in self.prioritized_files if self.file_vars[pf.rel_path].get()]
        total_sz = sum(pf.size_bytes for pf in selected_files)
        cnt = len(selected_files)
        tot = len(self.prioritized_files)
        self.lbl_stats.config(text=f"Seleccionados: {cnt} de {tot} archivos ({format_bytes(total_sz)})")

    def _on_confirm(self):
        selected_rel_paths = [pf.rel_path for pf in self.prioritized_files if self.file_vars[pf.rel_path].get()]
        self.on_confirm(selected_rel_paths)
        self.destroy()
