"""
Project Analysis Dialog GUI component.
Displays comprehensive project diagnostics, architecture, detected dependencies,
recommended file selection with interactive checkboxes, and excluded directories.
"""
import tkinter as tk
from tkinter import ttk, scrolledtext
from typing import List, Callable, Optional, Dict

from app.core.project_analyzer import ProjectAnalysisResult
from app.utils.file_utils import copy_to_clipboard, format_bytes

# Colour palette (aligned with main_window.py)
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
C_STAT_BG   = "#161b28"


class ProjectAnalysisDialog(tk.Toplevel):
    """Modal dialog displaying project analysis report and recommended selection."""

    def __init__(
        self,
        parent: tk.Tk,
        analysis: ProjectAnalysisResult,
        on_apply_selection: Optional[Callable[[List[str]], None]] = None
    ):
        super().__init__(parent)
        self.analysis = analysis
        self.on_apply_selection = on_apply_selection
        self.file_vars: Dict[str, tk.BooleanVar] = {}

        self.title(f"🔬 Análisis del Proyecto: {analysis.project_name}")
        self.geometry("980x740")
        self.minsize(800, 550)
        self.configure(bg=C_BG)

        # Make dialog modal and centered
        self.transient(parent)
        self.grab_set()
        self._center_window(parent)

        self._build_header()
        self._build_tabs()
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

        left = tk.Frame(hdr, bg=C_PANEL)
        left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        tk.Label(
            left,
            text=f"🔬  Análisis Automático: {self.analysis.project_name}",
            font=("Segoe UI", 13, "bold"),
            bg=C_PANEL, fg=C_TEXT
        ).pack(anchor="w")

        tk.Label(
            left,
            text=self.analysis.folder_path,
            font=("Consolas", 8),
            bg=C_PANEL, fg=C_TEXT2
        ).pack(anchor="w", pady=(2, 0))

        # Badges on right
        badges = tk.Frame(hdr, bg=C_PANEL)
        badges.pack(side=tk.RIGHT, padx=4)

        def _make_badge(parent, text, bg_color, fg_color="#ffffff"):
            f = tk.Frame(parent, bg=bg_color, padx=8, pady=4)
            f.pack(side=tk.LEFT, padx=3)
            tk.Label(f, text=text, font=("Segoe UI", 8, "bold"), bg=bg_color, fg=fg_color).pack()

        # Language badge
        _make_badge(badges, f"💻 {self.analysis.primary_language}", C_ACCENT)
        # Framework badge
        if self.analysis.framework and self.analysis.framework != "No detectado":
            _make_badge(badges, f"⚡ {self.analysis.framework}", "#8e44ad")
        # Package manager badge
        if self.analysis.package_manager and self.analysis.package_manager != "Ninguno detectado":
            _make_badge(badges, f"📦 {self.analysis.package_manager}", "#27ae60")

    def _build_tabs(self):
        style = ttk.Style(self)
        style.configure("Analysis.TNotebook", background=C_BG, borderwidth=0)
        style.configure("Analysis.TNotebook.Tab", background=C_PANEL, foreground=C_TEXT, padding=(12, 6), font=("Segoe UI", 9, "bold"))
        style.map("Analysis.TNotebook.Tab",
                  background=[("selected", C_ACCENT), ("active", C_BORDER)],
                  foreground=[("selected", "#ffffff"), ("active", C_TEXT)])

        notebook = ttk.Notebook(self, style="Analysis.TNotebook")
        notebook.pack(fill=tk.BOTH, expand=True, padx=12, pady=8)

        # Tab 1: Recommended Selection
        tab_recommend = tk.Frame(notebook, bg=C_BG)
        notebook.add(tab_recommend, text="🎯 Selección Recomendada")
        self._build_recommendation_tab(tab_recommend)

        # Tab 2: Full Architecture & Diagnostics
        tab_report = tk.Frame(notebook, bg=C_BG)
        notebook.add(tab_report, text="📊 Diagnóstico del Proyecto")
        self._build_report_tab(tab_report)

    # ── Tab 1: Recommended Selection ──────────────────────────────────────
    def _build_recommendation_tab(self, parent: tk.Frame):
        paned = ttk.PanedWindow(parent, orient=tk.HORIZONTAL)
        paned.pack(fill=tk.BOTH, expand=True, padx=4, pady=4)

        # Left Column: Recommended files with checkboxes
        left_frame = tk.Frame(paned, bg=C_PANEL, padx=10, pady=8)
        paned.add(left_frame, weight=3)

        top_bar = tk.Frame(left_frame, bg=C_PANEL)
        top_bar.pack(fill=tk.X, pady=(0, 6))

        tk.Label(
            top_bar,
            text="Archivos recomendados para analizar",
            font=("Segoe UI", 10, "bold"),
            bg=C_PANEL, fg=C_ACCENT
        ).pack(side=tk.LEFT)

        self.lbl_selected_count = tk.Label(
            top_bar,
            text="",
            font=("Segoe UI", 8, "italic"),
            bg=C_PANEL, fg=C_TEXT2
        )
        self.lbl_selected_count.pack(side=tk.RIGHT)

        btn_row = tk.Frame(left_frame, bg=C_PANEL)
        btn_row.pack(fill=tk.X, pady=(0, 6))

        ttk.Button(btn_row, text="☑ Marcar todos", style="Neutral.TButton",
                   command=self._select_all_recommended).pack(side=tk.LEFT, padx=(0, 4))
        ttk.Button(btn_row, text="☐ Desmarcar todos", style="Neutral.TButton",
                   command=self._deselect_all_recommended).pack(side=tk.LEFT)

        # Scrollable checkboxes list
        list_container = tk.Frame(left_frame, bg=C_ENTRY, bd=1, relief="flat", highlightbackground=C_BORDER, highlightthickness=1)
        list_container.pack(fill=tk.BOTH, expand=True)

        canvas = tk.Canvas(list_container, bg=C_ENTRY, bd=0, highlightthickness=0)
        scrollbar = ttk.Scrollbar(list_container, orient=tk.VERTICAL, command=canvas.yview)
        scroll_frame = tk.Frame(canvas, bg=C_ENTRY)

        scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas_window = canvas.create_window((0, 0), window=scroll_frame, anchor="nw")

        def _on_canvas_resize(event):
            canvas.itemconfig(canvas_window, width=event.width)
        canvas.bind("<Configure>", _on_canvas_resize)

        # Mousewheel scroll binding
        def _on_mousewheel(event):
            if event.delta:
                canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
            elif event.num == 4:
                canvas.yview_scroll(-1, "units")
            elif event.num == 5:
                canvas.yview_scroll(1, "units")

        canvas.bind_all("<MouseWheel>", _on_mousewheel)
        canvas.bind_all("<Button-4>", _on_mousewheel)
        canvas.bind_all("<Button-5>", _on_mousewheel)

        canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Populate recommended files checkboxes
        if not self.analysis.recommended_files:
            tk.Label(
                scroll_frame,
                text="(No se encontraron archivos recomendados)",
                bg=C_ENTRY, fg=C_TEXT2, font=("Segoe UI", 9, "italic")
            ).pack(anchor="w", padx=10, pady=10)
        else:
            for rel_file in self.analysis.recommended_files:
                var = tk.BooleanVar(value=True)  # Pre-checked by default!
                self.file_vars[rel_file] = var

                row = tk.Frame(scroll_frame, bg=C_ENTRY, padx=6, pady=2)
                row.pack(fill=tk.X)

                cb = tk.Checkbutton(
                    row,
                    text=f"✓  {rel_file}",
                    variable=var,
                    font=("Consolas", 9),
                    bg=C_ENTRY,
                    fg=C_TEXT,
                    activebackground=C_ENTRY,
                    activeforeground=C_ACCENT,
                    selectcolor=C_PANEL,
                    anchor="w",
                    command=self._update_selected_count
                )
                cb.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self._update_selected_count()

        # Right Column: Excluded directories & summary hints
        right_frame = tk.Frame(paned, bg=C_PANEL, padx=10, pady=8)
        paned.add(right_frame, weight=2)

        tk.Label(
            right_frame,
            text="Directorios Excluidos",
            font=("Segoe UI", 10, "bold"),
            bg=C_PANEL, fg=C_WARN
        ).pack(anchor="w", pady=(0, 6))

        tk.Label(
            right_frame,
            text="Estos directorios se omiten automáticamente para evitar archivos irrelevantes o pesados:",
            font=("Segoe UI", 8),
            bg=C_PANEL, fg=C_TEXT2, wraplength=260, justify=tk.LEFT
        ).pack(anchor="w", pady=(0, 8))

        excl_box = tk.Frame(right_frame, bg=C_ENTRY, padx=8, pady=8, highlightbackground=C_BORDER, highlightthickness=1)
        excl_box.pack(fill=tk.BOTH, expand=True)

        # List excluded directories
        excl_list = sorted(list(self.analysis.configured_exclusions))
        for d in excl_list:
            is_present = d in self.analysis.excluded_dirs_found
            fg = C_WARN if is_present else C_TEXT2
            mark = "⚠️" if is_present else "•"
            extra = " (detectado)" if is_present else ""
            lbl = tk.Label(
                excl_box,
                text=f"{mark} {d}/{extra}",
                font=("Consolas", 8, "bold" if is_present else "normal"),
                bg=C_ENTRY, fg=fg, anchor="w"
            )
            lbl.pack(anchor="w", pady=1)

        # Quick Tip Box
        tip_box = tk.Frame(right_frame, bg="#1a2538", padx=8, pady=8, highlightbackground=C_ACCENT, highlightthickness=1)
        tip_box.pack(fill=tk.X, pady=(10, 0))

        tk.Label(
            tip_box,
            text="💡 Consejo:",
            font=("Segoe UI", 8, "bold"),
            bg="#1a2538", fg=C_ACCENT
        ).pack(anchor="w")

        tk.Label(
            tip_box,
            text="Presiona 'Aplicar selección' para transferir estos archivos seleccionados directamente a la ventana principal. El prompt se generará solo con ellos.",
            font=("Segoe UI", 8),
            bg="#1a2538", fg=C_TEXT, wraplength=250, justify=tk.LEFT
        ).pack(anchor="w", pady=(2, 0))

    def _select_all_recommended(self):
        for var in self.file_vars.values():
            var.set(True)
        self._update_selected_count()

    def _deselect_all_recommended(self):
        for var in self.file_vars.values():
            var.set(False)
        self._update_selected_count()

    def _update_selected_count(self):
        checked = sum(1 for v in self.file_vars.values() if v.get())
        total = len(self.file_vars)
        self.lbl_selected_count.config(text=f"{checked} de {total} seleccionados")

    def get_selected_recommended_files(self) -> List[str]:
        return [f for f, var in self.file_vars.items() if var.get()]

    # ── Tab 2: Full Architecture & Diagnostics ────────────────────────────
    def _build_report_tab(self, parent: tk.Frame):
        report_text = scrolledtext.ScrolledText(
            parent,
            wrap=tk.WORD,
            font=("Consolas", 9),
            bg=C_ENTRY,
            fg=C_TEXT,
            insertbackground=C_TEXT,
            selectbackground=C_TREE_SEL,
            selectforeground=C_TEXT,
            relief="flat",
            bd=0,
            padx=12,
            pady=10
        )
        report_text.pack(fill=tk.BOTH, expand=True, padx=4, pady=4)
        report_text.insert(tk.END, self.analysis.to_formatted_report())
        report_text.config(state="disabled")

    # ── Bottom Bar ────────────────────────────────────────────────────────
    def _build_bottom_bar(self):
        bottom = tk.Frame(self, bg=C_STAT_BG, padx=14, pady=10, highlightthickness=1, highlightbackground=C_BORDER)
        bottom.pack(fill=tk.X, side=tk.BOTTOM)

        # Left side buttons
        if self.on_apply_selection:
            ttk.Button(
                bottom,
                text="✅ Aplicar selección",
                style="Success.TButton",
                command=self._on_apply_clicked
            ).pack(side=tk.LEFT, padx=(0, 6))

        ttk.Button(
            bottom,
            text="📋 Copiar reporte",
            style="Neutral.TButton",
            command=self._on_copy_report
        ).pack(side=tk.LEFT, padx=(0, 6))

        # Right side button
        ttk.Button(
            bottom,
            text="Cerrar",
            style="Neutral.TButton",
            command=self.destroy
        ).pack(side=tk.RIGHT)

    def _on_apply_clicked(self):
        selected = self.get_selected_recommended_files()
        if self.on_apply_selection:
            self.on_apply_selection(selected)
        self.destroy()

    def _on_copy_report(self):
        report = self.analysis.to_formatted_report()
        copy_to_clipboard(self, report)
