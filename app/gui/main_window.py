"""Main Tkinter window – redesigned layout with left tree, right problem pane, and full bottom stats bar."""
import os
import sys
import subprocess
import tkinter as tk
from tkinter import ttk, scrolledtext
from typing import List, Set

from app.models.project import ExportConfig, DEFAULT_ALLOWED_EXTENSIONS
from app.models.analysis_types import (
    ANALYSIS_PROFILES, get_analysis_profile, get_all_analysis_types
)
from app.core.file_selector import FileSelectorManager
from app.generators.prompt_generator import PromptGenerator
from app.generators.markdown_generator import generate_markdown_bundle
from app.generators.text_generator import generate_text_bundle
from app.generators.standalone_prompt_generator import generate_standalone_prompt
from app.gui.file_tree import CheckboxTreeview
from app.gui.analysis_dialog import ProjectAnalysisDialog
from app.core.project_analyzer import ProjectAnalyzer
from app.gui import dialogs
from app.utils.file_utils import (
    copy_to_clipboard, write_text_file, KNOWN_BINARY_EXTENSIONS,
    is_binary_file, get_file_size,
)

# ─── Colour palette ─────────────────────────────────────────────────────────
C_BG        = "#1e2330"   # main background
C_PANEL     = "#252b3b"   # panel background
C_BORDER    = "#323a50"   # separator / border
C_ACCENT    = "#4f8ef7"   # primary accent (blue)
C_ACCENT_DK = "#3a6fcc"   # accent hover
C_SUCCESS   = "#3ecf8e"   # green
C_WARN      = "#f5a623"   # amber
C_TEXT      = "#e8eaf0"   # primary text
C_TEXT2     = "#8b92a8"   # secondary / muted
C_ENTRY     = "#2a3148"   # entry bg
C_TREE_SEL  = "#2f3d5c"   # tree selection highlight
C_STAT_BG   = "#161b28"   # bottom bar bg
# ────────────────────────────────────────────────────────────────────────────


class MainWindow:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("DeepSeek Code Packager")
        self.root.geometry("1340x860")
        self.root.minsize(1100, 700)
        self.root.configure(bg=C_BG)

        # ── State ──────────────────────────────────────────────────────────
        self.selector   = FileSelectorManager()
        self.config     = ExportConfig()

        default_excl    = ".git, node_modules, __pycache__, venv, .venv, dist, build, .idea, .vscode, vendor, .quasar, .github, public"
        default_exts    = ", ".join(sorted(DEFAULT_ALLOWED_EXTENSIONS))

        self.var_folder   = tk.StringVar()
        self.var_excl     = tk.StringVar(value=default_excl)
        self.var_exts     = tk.StringVar(value=default_exts)
        self.var_filter   = tk.BooleanVar(value=True)
        self.var_lineno   = tk.BooleanVar(value=True)
        self.var_tree     = tk.BooleanVar(value=True)
        self.var_instruct = tk.BooleanVar(value=True)
        self.var_max_file = tk.DoubleVar(value=2.0)
        self.var_max_tot  = tk.DoubleVar(value=50.0)
        self.var_max_n    = tk.IntVar(value=100)
        self.var_fmt      = tk.StringVar(value="markdown")
        self.var_analysis_type = tk.StringVar(value="Detect errors")

        # Bottom stats vars
        self.sv_folder    = tk.StringVar(value="0")
        self.sv_sel_files = tk.StringVar(value="0")
        self.sv_included  = tk.StringVar(value="0")
        self.sv_excluded  = tk.StringVar(value="0")
        self.sv_size      = tk.StringVar(value="0.00 MB")
        self.sv_lines     = tk.StringVar(value="0")
        self.sv_status    = tk.StringVar(value="Listo.")

        self._setup_styles()
        self._build_header()
        self._build_main()
        self._build_bottom()

    # ── Style helpers ─────────────────────────────────────────────────────
    def _setup_styles(self):
        s = ttk.Style()
        s.theme_use("clam")

        common = {"background": C_BG, "foreground": C_TEXT, "fieldbackground": C_ENTRY,
                  "bordercolor": C_BORDER, "lightcolor": C_BORDER, "darkcolor": C_BORDER,
                  "troughcolor": C_PANEL, "selectbackground": C_TREE_SEL,
                  "selectforeground": C_TEXT}

        s.configure(".",                font=("Segoe UI", 9), **common)
        s.configure("TFrame",           background=C_BG)
        s.configure("TLabel",           background=C_BG, foreground=C_TEXT)
        s.configure("TEntry",           fieldbackground=C_ENTRY, foreground=C_TEXT,
                    insertcolor=C_TEXT, bordercolor=C_BORDER)
        s.configure("TCheckbutton",     background=C_BG, foreground=C_TEXT2)
        s.configure("TRadiobutton",     background=C_BG, foreground=C_TEXT2)
        s.configure("Vertical.TScrollbar",   background=C_BORDER, troughcolor=C_PANEL)
        s.configure("Horizontal.TScrollbar", background=C_BORDER, troughcolor=C_PANEL)
        s.configure("TSeparator",       background=C_BORDER)
        s.configure("TPanedwindow",     background=C_BORDER)
        s.configure("TSpinbox",         fieldbackground=C_ENTRY, foreground=C_TEXT,
                    insertcolor=C_TEXT, bordercolor=C_BORDER, arrowcolor=C_TEXT2)

        # Panel labels
        s.configure("Panel.TFrame",     background=C_PANEL)
        s.configure("Panel.TLabel",     background=C_PANEL, foreground=C_TEXT)
        s.configure("Muted.TLabel",     background=C_PANEL, foreground=C_TEXT2,
                    font=("Segoe UI", 8))
        s.configure("Title.TLabel",     background=C_BG, foreground=C_TEXT,
                    font=("Segoe UI", 15, "bold"))
        s.configure("Sub.TLabel",       background=C_BG, foreground=C_TEXT2,
                    font=("Segoe UI", 9))
        s.configure("Sec.TLabel",       background=C_PANEL, foreground=C_ACCENT,
                    font=("Segoe UI", 9, "bold"))
        s.configure("StatKey.TLabel",   background=C_STAT_BG, foreground=C_TEXT2,
                    font=("Segoe UI", 8))
        s.configure("StatVal.TLabel",   background=C_STAT_BG, foreground=C_TEXT,
                    font=("Segoe UI", 10, "bold"))
        s.configure("Status.TLabel",    background=C_STAT_BG, foreground=C_TEXT2,
                    font=("Segoe UI", 8, "italic"))

        # Treeview
        s.configure("Treeview",         background=C_PANEL, foreground=C_TEXT,
                    fieldbackground=C_PANEL, bordercolor=C_BORDER, rowheight=22)
        s.configure("Treeview.Heading", background=C_BORDER, foreground=C_TEXT2,
                    relief="flat", font=("Segoe UI", 8, "bold"))
        s.map("Treeview",               background=[("selected", C_TREE_SEL)],
                                        foreground=[("selected", C_TEXT)])
        s.map("Treeview.Heading",       background=[("active", C_BORDER)])

        # Buttons
        for name, bg, hover in [
            ("Accent.TButton",  C_ACCENT,   C_ACCENT_DK),
            ("Success.TButton", C_SUCCESS,  "#2faa75"),
            ("Neutral.TButton", C_BORDER,   "#404860"),
            ("Warn.TButton",    C_WARN,     "#cc8b1a"),
        ]:
            s.configure(name, background=bg, foreground=C_BG if name != "Neutral.TButton" else C_TEXT,
                        relief="flat", font=("Segoe UI", 9, "bold"), padding=(10, 5))
            s.map(name, background=[("active", hover)])

    # ── Header ────────────────────────────────────────────────────────────
    def _build_header(self):
        bar = ttk.Frame(self.root, padding=(16, 10, 16, 8))
        bar.pack(fill=tk.X)

        ttk.Label(bar, text="📦  DeepSeek Code Packager", style="Title.TLabel").pack(side=tk.LEFT)

        right = ttk.Frame(bar)
        right.pack(side=tk.RIGHT)
        ttk.Label(right,
                  text="Sin API · Sin conexión · Proyectos grandes seguros",
                  style="Sub.TLabel").pack(anchor="e")

        ttk.Separator(self.root).pack(fill=tk.X)

    # ── Main 3-pane layout ────────────────────────────────────────────────
    def _build_main(self):
        paned = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        paned.pack(fill=tk.BOTH, expand=True, padx=8, pady=6)

        self._build_left(paned)
        self._build_right(paned)

    # ──────────────────────────────────────────────────────────────────────
    # LEFT pane  –  project tree
    # ──────────────────────────────────────────────────────────────────────
    def _build_left(self, paned):
        left = ttk.Frame(paned, style="Panel.TFrame", padding=0)
        paned.add(left, weight=2)

        # ── Folder row
        folder_bar = ttk.Frame(left, style="Panel.TFrame", padding=(8, 6))
        folder_bar.pack(fill=tk.X)

        ttk.Label(folder_bar, text="📂  Carpeta del proyecto", style="Sec.TLabel").pack(anchor="w")

        fe = ttk.Frame(folder_bar, style="Panel.TFrame")
        fe.pack(fill=tk.X, pady=(4, 0))

        self.folder_entry = ttk.Entry(fe, textvariable=self.var_folder, state="readonly")
        self.folder_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 4))

        ttk.Button(fe, text="📂 Seleccionar carpeta",
                   style="Accent.TButton",
                   command=self.on_select_folder).pack(side=tk.LEFT, padx=(0, 3))
        ttk.Button(fe, text="🔬 Analizar",
                   style="Accent.TButton",
                   command=self.on_analyze_project).pack(side=tk.LEFT, padx=(0, 3))
        ttk.Button(fe, text="✖",
                   style="Neutral.TButton",
                   command=self.on_remove_folder, width=3).pack(side=tk.LEFT)

        ttk.Separator(left).pack(fill=tk.X, pady=4)

        # ── Filters row (collapsed / compact)
        flt = ttk.Frame(left, style="Panel.TFrame", padding=(8, 0))
        flt.pack(fill=tk.X)

        fl1 = ttk.Frame(flt, style="Panel.TFrame")
        fl1.pack(fill=tk.X, pady=2)
        ttk.Label(fl1, text="Excluir carpetas:", style="Muted.TLabel").pack(side=tk.LEFT, padx=(0, 4))
        ex = ttk.Entry(fl1, textvariable=self.var_excl, font=("Consolas", 8))
        ex.pack(side=tk.LEFT, fill=tk.X, expand=True)
        ex.bind("<FocusOut>", lambda _: self.reload_tree())

        fl2 = ttk.Frame(flt, style="Panel.TFrame")
        fl2.pack(fill=tk.X, pady=2)
        ttk.Checkbutton(fl2, text="Filtrar extensiones:", variable=self.var_filter,
                        command=self.reload_tree, style="TCheckbutton").pack(side=tk.LEFT, padx=(0, 4))
        ext_e = ttk.Entry(fl2, textvariable=self.var_exts, font=("Consolas", 8))
        ext_e.pack(side=tk.LEFT, fill=tk.X, expand=True)
        ext_e.bind("<FocusOut>", lambda _: self.reload_tree())

        ttk.Separator(left).pack(fill=tk.X, pady=4)

        # ── Tree toolbar
        tb = ttk.Frame(left, style="Panel.TFrame", padding=(8, 0, 8, 4))
        tb.pack(fill=tk.X)
        ttk.Button(tb, text="☑ Todos", style="Neutral.TButton",
                   command=self.on_select_all_tree).pack(side=tk.LEFT, padx=(0, 4))
        ttk.Button(tb, text="☐ Ninguno", style="Neutral.TButton",
                   command=self.on_deselect_all_tree).pack(side=tk.LEFT, padx=(0, 4))
        ttk.Button(tb, text="🔬 Analizar proyecto", style="Accent.TButton",
                   command=self.on_analyze_project).pack(side=tk.LEFT, padx=(0, 4))
        ttk.Button(tb, text="🔄 Recargar", style="Neutral.TButton",
                   command=self.reload_tree).pack(side=tk.RIGHT)

        # ── Tree widget
        tc = ttk.Frame(left, style="Panel.TFrame", padding=(4, 0, 4, 4))
        tc.pack(fill=tk.BOTH, expand=True)

        self.tree = CheckboxTreeview(tc)
        sy = ttk.Scrollbar(tc, orient=tk.VERTICAL,   command=self.tree.yview)
        sx = ttk.Scrollbar(tc, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscrollcommand=sy.set, xscrollcommand=sx.set)
        sy.pack(side=tk.RIGHT, fill=tk.Y)
        sx.pack(side=tk.BOTTOM, fill=tk.X)
        self.tree.pack(fill=tk.BOTH, expand=True)
        self.tree.bind("<<TreeviewSelect>>", lambda _: self._refresh_selection_stats())
        self.tree.bind("<ButtonRelease-1>",  lambda _: self.root.after(50, self._refresh_selection_stats))

        ttk.Separator(left).pack(fill=tk.X, pady=4)

        # ── Individual files list
        il = ttk.Frame(left, style="Panel.TFrame", padding=(8, 0))
        il.pack(fill=tk.X)

        ttk.Label(il, text="📄  Archivos individuales adicionales", style="Sec.TLabel").pack(anchor="w")

        il_tb = ttk.Frame(il, style="Panel.TFrame")
        il_tb.pack(fill=tk.X, pady=(4, 3))
        ttk.Button(il_tb, text="➕ Agregar archivos",
                   style="Neutral.TButton",
                   command=self.on_add_individual_files).pack(side=tk.LEFT, padx=(0, 4))
        ttk.Button(il_tb, text="🗑 Quitar",
                   style="Neutral.TButton",
                   command=self.on_remove_individual_file).pack(side=tk.LEFT, padx=(0, 4))
        ttk.Button(il_tb, text="🧹 Limpiar",
                   style="Neutral.TButton",
                   command=self.on_clear_individual_files).pack(side=tk.RIGHT)

        lc = ttk.Frame(il, style="Panel.TFrame", padding=(0, 0, 0, 6))
        lc.pack(fill=tk.X)
        self.file_listbox = tk.Listbox(
            lc, height=4, selectmode=tk.SINGLE,
            font=("Consolas", 8),
            bg=C_ENTRY, fg=C_TEXT,
            selectbackground=C_TREE_SEL, selectforeground=C_TEXT,
            relief="flat", bd=0, highlightthickness=0,
        )
        ls = ttk.Scrollbar(lc, orient=tk.VERTICAL, command=self.file_listbox.yview)
        self.file_listbox.configure(yscrollcommand=ls.set)
        ls.pack(side=tk.RIGHT, fill=tk.Y)
        self.file_listbox.pack(fill=tk.X, expand=True)

    # ──────────────────────────────────────────────────────────────────────
    # RIGHT pane  –  problem description + settings + preview
    # ──────────────────────────────────────────────────────────────────────
    def _build_right(self, paned):
        right = ttk.Frame(paned, style="Panel.TFrame", padding=0)
        paned.add(right, weight=3)

        # ── Analysis Type selector (top of right pane)
        type_hdr = ttk.Frame(right, style="Panel.TFrame", padding=(10, 8, 10, 2))
        type_hdr.pack(fill=tk.X)

        t_row = ttk.Frame(type_hdr, style="Panel.TFrame")
        t_row.pack(fill=tk.X)

        ttk.Label(t_row, text="🎯  Tipo de análisis:", style="Sec.TLabel").pack(side=tk.LEFT, padx=(0, 6))

        self.cb_analysis_type = ttk.Combobox(
            t_row,
            textvariable=self.var_analysis_type,
            values=get_all_analysis_types(),
            state="readonly",
            font=("Segoe UI", 9, "bold"),
            width=26
        )
        self.cb_analysis_type.pack(side=tk.LEFT, padx=(0, 10))
        self.cb_analysis_type.bind("<<ComboboxSelected>>", self._on_analysis_type_changed)

        self.lbl_profile_hint = ttk.Label(
            type_hdr,
            text="",
            style="Muted.TLabel",
            wraplength=600,
            justify=tk.LEFT
        )
        self.lbl_profile_hint.pack(anchor="w", pady=(3, 0))

        ttk.Separator(right).pack(fill=tk.X, pady=(4, 2))

        # ── Problem description (always visible, prominent)
        desc_hdr = ttk.Frame(right, style="Panel.TFrame", padding=(10, 6, 10, 4))
        desc_hdr.pack(fill=tk.X)
        ttk.Label(desc_hdr, text="📝  Describe el problema / objetivo", style="Sec.TLabel").pack(anchor="w")
        ttk.Label(desc_hdr,
                  text="Este texto se incluirá en deepseek_prompt.md como REPORTED PROBLEM OR GOAL",
                  style="Muted.TLabel").pack(anchor="w")

        desc_body = ttk.Frame(right, style="Panel.TFrame", padding=(10, 0))
        desc_body.pack(fill=tk.X)
        self.problem_text = scrolledtext.ScrolledText(
            desc_body, height=5,
            font=("Segoe UI", 10),
            bg=C_ENTRY, fg=C_TEXT,
            insertbackground=C_TEXT,
            selectbackground=C_TREE_SEL, selectforeground=C_TEXT,
            relief="flat", bd=1, padx=8, pady=6,
            wrap=tk.WORD,
        )
        self.problem_text.pack(fill=tk.X, expand=True)

        self._on_analysis_type_changed(init=True)

        ttk.Separator(right).pack(fill=tk.X, pady=6)

        # ── Generation settings (collapsible look)
        cfg = ttk.Frame(right, style="Panel.TFrame", padding=(10, 0))
        cfg.pack(fill=tk.X)

        ttk.Label(cfg, text="⚙️  Configuración de generación", style="Sec.TLabel").pack(anchor="w", pady=(0, 4))

        r1 = ttk.Frame(cfg, style="Panel.TFrame")
        r1.pack(fill=tk.X, pady=2)
        ttk.Label(r1, text="Máx. archivo:", style="Muted.TLabel").pack(side=tk.LEFT, padx=(0, 3))
        ttk.Spinbox(r1, from_=0.1, to=50.0, increment=0.5,
                    textvariable=self.var_max_file, width=5).pack(side=tk.LEFT, padx=(0, 12))
        ttk.Label(r1, text="MB  ·  Máx. total:", style="Muted.TLabel").pack(side=tk.LEFT, padx=(0, 3))
        ttk.Spinbox(r1, from_=1.0, to=500.0, increment=5.0,
                    textvariable=self.var_max_tot, width=6).pack(side=tk.LEFT, padx=(0, 12))
        ttk.Label(r1, text="MB  ·  Máx. archivos:", style="Muted.TLabel").pack(side=tk.LEFT, padx=(0, 3))
        ttk.Spinbox(r1, from_=1, to=5000, increment=10,
                    textvariable=self.var_max_n, width=5).pack(side=tk.LEFT)

        r2 = ttk.Frame(cfg, style="Panel.TFrame")
        r2.pack(fill=tk.X, pady=2)
        for txt, var in [
            ("Nº de línea", self.var_lineno),
            ("Árbol de carpetas", self.var_tree),
            ("Instrucciones DeepSeek", self.var_instruct),
            ("Filtrar por extensión", self.var_filter),
        ]:
            ttk.Checkbutton(r2, text=txt, variable=var).pack(side=tk.LEFT, padx=(0, 14))
        ttk.Label(r2, text="Formato:", style="Muted.TLabel").pack(side=tk.LEFT, padx=(8, 3))
        ttk.Radiobutton(r2, text="Markdown", value="markdown", variable=self.var_fmt).pack(side=tk.LEFT, padx=(0, 6))
        ttk.Radiobutton(r2, text="Texto",    value="text",     variable=self.var_fmt).pack(side=tk.LEFT)

        ttk.Separator(right).pack(fill=tk.X, pady=6)

        # ── Preview label
        prev_hdr = ttk.Frame(right, style="Panel.TFrame", padding=(10, 0))
        prev_hdr.pack(fill=tk.X)
        ttk.Label(prev_hdr, text="🔍  Vista previa del documento generado", style="Sec.TLabel").pack(anchor="w")

        # ── Preview area
        prev_body = ttk.Frame(right, style="Panel.TFrame", padding=(10, 4, 10, 4))
        prev_body.pack(fill=tk.BOTH, expand=True)
        self.preview_text = scrolledtext.ScrolledText(
            prev_body, wrap=tk.NONE,
            font=("Consolas", 9),
            bg=C_ENTRY, fg=C_TEXT,
            insertbackground=C_TEXT,
            selectbackground=C_TREE_SEL, selectforeground=C_TEXT,
            relief="flat", bd=0, padx=8, pady=6,
        )
        self.preview_text.pack(fill=tk.BOTH, expand=True)

    # ──────────────────────────────────────────────────────────────────────
    # BOTTOM  –  stats bar + action buttons
    # ──────────────────────────────────────────────────────────────────────
    def _build_bottom(self):
        ttk.Separator(self.root).pack(fill=tk.X)

        bottom = tk.Frame(self.root, bg=C_STAT_BG)
        bottom.pack(fill=tk.X, side=tk.BOTTOM)

        # ── Action buttons (left side of bottom bar)
        btn_strip = tk.Frame(bottom, bg=C_STAT_BG, padx=8, pady=6)
        btn_strip.pack(side=tk.LEFT)

        ttk.Button(btn_strip, text="🔬 Analizar proyecto",
                   style="Neutral.TButton",
                   command=self.on_analyze_project).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(btn_strip, text="⚡ Generar contexto",
                   style="Accent.TButton",
                   command=self.on_generate_prompt).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(btn_strip, text="📁 Abrir carpeta resultados",
                   style="Success.TButton",
                   command=self.on_open_results_folder).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(btn_strip, text="📋 Copiar prompt",
                   style="Neutral.TButton",
                   command=self.on_copy_clipboard).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(btn_strip, text="💾 Guardar como…",
                   style="Neutral.TButton",
                   command=self.on_export_file).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(btn_strip, text="🗑 Limpiar selección",
                   style="Neutral.TButton",
                   command=self.on_clear_all).pack(side=tk.LEFT)

        # ── Stat tiles (right side of bottom bar)
        stats = tk.Frame(bottom, bg=C_STAT_BG, padx=12, pady=4)
        stats.pack(side=tk.RIGHT)

        def _stat(parent, key):
            cell = tk.Frame(parent, bg=C_STAT_BG, padx=10, pady=2)
            cell.pack(side=tk.LEFT)
            var = tk.StringVar(value="—")
            tk.Label(cell, text=key, bg=C_STAT_BG, fg=C_TEXT2,
                     font=("Segoe UI", 8)).pack()
            tk.Label(cell, textvariable=var, bg=C_STAT_BG, fg=C_TEXT,
                     font=("Segoe UI", 11, "bold")).pack()
            return var

        self.sv_folder    = _stat(stats, "Carpeta")
        self.sv_sel_files = _stat(stats, "Archivos sel.")
        self.sv_included  = _stat(stats, "Incluidos")
        self.sv_excluded  = _stat(stats, "Excluidos")
        self.sv_size      = _stat(stats, "Tamaño total")
        self.sv_lines     = _stat(stats, "Líneas")

        # ── Status text (very bottom strip)
        status_bar = tk.Frame(self.root, bg="#0f1320", pady=2)
        status_bar.pack(fill=tk.X, side=tk.BOTTOM)
        tk.Label(status_bar, textvariable=self.sv_status,
                 bg="#0f1320", fg=C_TEXT2,
                 font=("Segoe UI", 8, "italic"),
                 anchor="w", padx=10).pack(fill=tk.X)

        self.sv_status.set("Listo. Selecciona una carpeta para comenzar.")

    # ── Stat refresh ─────────────────────────────────────────────────────
    def _refresh_selection_stats(self):
        folder  = self.var_folder.get()
        has_fld = 1 if folder else 0
        sel_files = len(self.tree.get_checked_files()) + len(self.selector.get_selection().individual_files)

        # Count binary vs. included among selected files
        included = 0
        excluded = 0
        total_bytes = 0

        checked = self.tree.get_checked_files()
        ind     = self.selector.get_selection().individual_files

        all_paths = []
        if folder:
            for rel in checked:
                all_paths.append(os.path.join(folder, rel))
        for abs_p in ind:
            all_paths.append(abs_p)

        for fp in all_paths:
            if not os.path.isfile(fp):
                continue
            if is_binary_file(fp):
                excluded += 1
            else:
                included += 1
                total_bytes += get_file_size(fp)

        size_mb = total_bytes / (1024 * 1024)

        self.sv_folder.set(str(has_fld))
        self.sv_sel_files.set(str(sel_files))
        self.sv_included.set(str(included))
        self.sv_excluded.set(str(excluded))
        self.sv_size.set(f"{size_mb:.2f} MB")
        # Lines shown only after generation
        # self.sv_lines is updated in on_generate_prompt

    # ── UI event handlers ────────────────────────────────────────────────
    def on_select_folder(self):
        folder = dialogs.ask_folder("Seleccionar Carpeta del Proyecto")
        if folder:
            self.selector.set_folder(folder)
            self.var_folder.set(folder)
            self.reload_tree()
            self._refresh_selection_stats()
            self.sv_status.set(f"Carpeta seleccionada: {folder}")

    def on_analyze_project(self):
        folder = self.var_folder.get()
        if not folder or not os.path.isdir(folder):
            folder = dialogs.ask_folder("Seleccionar Carpeta para Analizar")
            if not folder:
                return
            self.selector.set_folder(folder)
            self.var_folder.set(folder)
            self.reload_tree()

        self.sv_status.set("Analizando estructura, tecnologías y dependencias del proyecto...")
        self.root.update_idletasks()

        self.selector.set_exclusions_from_string(self.var_excl.get())
        excluded = self.selector.get_selection().excluded_dirs

        try:
            max_file_mb = float(self.var_max_file.get())
        except ValueError:
            max_file_mb = 2.0

        analyzer = ProjectAnalyzer(excluded_dirs=excluded)
        result = analyzer.analyze(folder, max_file_size_mb=max_file_mb)

        self.sv_status.set(
            f"Análisis completado: {result.total_files} archivos, {result.total_lines:,} líneas. "
            f"Lenguaje: {result.primary_language} · Framework: {result.framework}"
        )

        ProjectAnalysisDialog(
            self.root,
            analysis=result,
            on_apply_selection=self.apply_recommended_selection
        )

    def _on_analysis_type_changed(self, event=None, init: bool = False):
        selected = self.var_analysis_type.get()
        profile = get_analysis_profile(selected)
        if hasattr(self, "lbl_profile_hint"):
            self.lbl_profile_hint.config(
                text=f"{profile.icon} {profile.objective}\nEnfoque: {profile.focus}"
            )
        if hasattr(self, "problem_text"):
            current_text = self.problem_text.get("1.0", tk.END).strip()
            all_hints = {p.default_prompt_hint for p in ANALYSIS_PROFILES.values()}
            all_hints.add("Por favor analiza el siguiente código del proyecto. Identifica posibles errores, refactorizaciones recomendadas y soluciones al problema.")

            if not current_text or current_text in all_hints or init:
                self.problem_text.delete("1.0", tk.END)
                self.problem_text.insert("1.0", profile.default_prompt_hint)

    def apply_recommended_selection(self, selected_files: List[str], notify: bool = True):
        if not selected_files:
            if notify:
                dialogs.show_warning("Atención", "No se seleccionó ningún archivo recomendado.")
            return

        self.tree.set_checked_files(set(selected_files))
        self.selector.set_checked_folder_files(self.tree.get_checked_files())
        self._refresh_selection_stats()
        count = len(selected_files)
        self.sv_status.set(f"✓ Selección recomendada aplicada: {count} archivo(s) preparados para contexto.")
        if notify:
            dialogs.show_info(
                "Selección Aplicada",
                f"Se han aplicado {count} archivo(s) recomendados para el contexto.\n\n"
                "Puedes pulsar '⚡ Generar contexto' directamente cuando estés listo."
            )

    def on_remove_folder(self):
        self.selector.remove_folder()
        self.var_folder.set("")
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.tree.checked_items.clear()
        self._refresh_selection_stats()
        self.sv_status.set("Carpeta removida.")

    def on_clear_all(self):
        self.on_remove_folder()
        self.on_clear_individual_files()
        self.preview_text.delete("1.0", tk.END)
        self.sv_lines.set("0")
        self.sv_status.set("Selección limpiada.")

    def reload_tree(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.tree.checked_items.clear()

        folder = self.var_folder.get()
        if not folder or not os.path.isdir(folder):
            return

        self.selector.set_exclusions_from_string(self.var_excl.get())
        excluded_dirs = self.selector.get_selection().excluded_dirs
        allowed_exts  = self._get_exts()
        filter_ext    = self.var_filter.get()

        root_item = self.tree.insert("", "end", text="📁",
                                     values=("", os.path.basename(folder)), open=True)

        for dirpath, dirnames, filenames in os.walk(folder):
            dirnames[:] = [d for d in sorted(dirnames) if d not in excluded_dirs]
            rel_dir = os.path.relpath(dirpath, folder)

            parent_item = root_item if rel_dir == "." else self._find_folder_item(rel_dir)
            if not parent_item:
                continue

            for d in dirnames:
                rel_sub = os.path.join(rel_dir, d) if rel_dir != "." else d
                self.tree.insert_folder(parent_item, rel_sub)

            for f in sorted(filenames):
                ext = os.path.splitext(f)[1].lower()
                if ext in KNOWN_BINARY_EXTENSIONS:
                    continue
                if filter_ext and allowed_exts and ext not in allowed_exts:
                    continue
                rel_file = os.path.join(rel_dir, f) if rel_dir != "." else f
                self.tree.insert_file(parent_item, rel_file)

        self._refresh_selection_stats()

    def _find_folder_item(self, rel_path: str):
        def search(item):
            if self.tree.set(item, "name") == rel_path:
                return item
            for ch in self.tree.get_children(item):
                found = search(ch)
                if found:
                    return found
            return None
        for item in self.tree.get_children():
            found = search(item)
            if found:
                return found
        return None

    def _get_exts(self) -> set:
        exts = set()
        for e in self.var_exts.get().split(","):
            c = e.strip().lower()
            if c:
                exts.add(c if c.startswith(".") else "." + c)
        return exts

    def on_select_all_tree(self):
        self.tree.select_all()
        self._refresh_selection_stats()

    def on_deselect_all_tree(self):
        self.tree.deselect_all()
        self._refresh_selection_stats()

    def on_add_individual_files(self):
        files = dialogs.ask_files("Seleccionar Archivos Individuales")
        if files:
            added = self.selector.add_individual_files(files)
            self.file_listbox.delete(0, tk.END)
            for f in self.selector.get_selection().individual_files:
                self.file_listbox.insert(tk.END, f)
            self._refresh_selection_stats()
            self.sv_status.set(f"Se agregaron {added} archivo(s) individual(es).")

    def on_remove_individual_file(self):
        sel = self.file_listbox.curselection()
        if sel:
            val = self.file_listbox.get(sel[0])
            self.selector.remove_individual_file(val)
            self.file_listbox.delete(sel[0])
            self._refresh_selection_stats()
            self.sv_status.set(f"Archivo removido: {os.path.basename(val)}")

    def on_clear_individual_files(self):
        self.selector.clear_individual_files()
        self.file_listbox.delete(0, tk.END)
        self._refresh_selection_stats()
        self.sv_status.set("Lista de archivos individuales limpiada.")

    def get_output_dir(self) -> str:
        out_dir = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "output"
        )
        os.makedirs(out_dir, exist_ok=True)
        return out_dir

    def on_open_results_folder(self):
        out_dir = self.get_output_dir()
        try:
            if os.name == "nt":
                os.startfile(out_dir)
            else:
                subprocess.run(["open" if sys.platform == "darwin" else "xdg-open", out_dir])
            self.sv_status.set(f"Carpeta de resultados abierta: {out_dir}")
        except Exception as exc:
            dialogs.show_error("Error", f"No se pudo abrir la carpeta: {exc}")

    def on_generate_prompt(self):
        folder = self.var_folder.get()
        ind    = self.selector.get_selection().individual_files

        if not folder and not ind:
            dialogs.show_warning("Atención",
                                 "Selecciona una carpeta o al menos un archivo individual.")
            return

        self.selector.set_checked_folder_files(self.tree.get_checked_files())
        self.selector.set_exclusions_from_string(self.var_excl.get())

        try: self.config.max_file_size_mb  = float(self.var_max_file.get())
        except ValueError: self.config.max_file_size_mb = 2.0

        try: self.config.max_total_size_mb = float(self.var_max_tot.get())
        except ValueError: self.config.max_total_size_mb = 50.0

        try: self.config.max_files = int(self.var_max_n.get())
        except ValueError: self.config.max_files = 100

        self.config.add_line_numbers        = self.var_lineno.get()
        self.config.include_tree            = self.var_tree.get()
        self.config.include_system_instructions = self.var_instruct.get()
        self.config.output_format           = self.var_fmt.get()
        self.config.analysis_type           = self.var_analysis_type.get()

        problem_desc = self.problem_text.get("1.0", tk.END).strip()
        gen = PromptGenerator(self.config)

        doc_text, included, excluded, omitted, total_lines = gen.generate(
            self.selector.get_selection(), problem_desc
        )

        if included == 0 and omitted == 0:
            dialogs.show_warning("Atención",
                                 "No hay archivos de código válidos seleccionados.")
            return

        # Preview
        self.preview_text.delete("1.0", tk.END)
        self.preview_text.insert(tk.END, doc_text)

        # Update bottom stats
        self._refresh_selection_stats()
        self.sv_included.set(str(included))
        self.sv_excluded.set(str(excluded))
        self.sv_lines.set(f"{total_lines:,}")

        # Save output files
        out_dir     = self.get_output_dir()
        md_text, _, _, _, _  = generate_markdown_bundle(
            self.selector.get_selection(), problem_desc, self.config)
        txt_text, _, _, _, _ = generate_text_bundle(
            self.selector.get_selection(), problem_desc, self.config)
        prompt_text = generate_standalone_prompt(problem_desc, analysis_type=self.config.analysis_type)

        write_text_file(os.path.join(out_dir, "deepseek_project_context.md"),  md_text)
        write_text_file(os.path.join(out_dir, "deepseek_project_context.txt"), txt_text)
        write_text_file(os.path.join(out_dir, "deepseek_prompt.md"),           prompt_text)

        dialogs.show_info(
            "✅ Archivos Preparados",
            f"Archivos generados en:\n{out_dir}\n\n"
            f"• Incluidos:  {included}\n"
            f"• Excluidos:  {excluded}\n"
            f"• Omitidos:   {omitted}\n"
            f"• Líneas:     {total_lines:,}\n\n"
            "Abre DeepSeek en tu navegador y adjunta:\n"
            "  1. deepseek_prompt.md\n"
            "  2. deepseek_project_context.md\n"
            "  3. deepseek_project_context.txt"
        )
        self.sv_status.set(
            f"Listo · Incluidos: {included} · Excluidos: {excluded} · Omitidos: {omitted} · Líneas: {total_lines:,}"
        )

    def on_copy_clipboard(self):
        content = self.preview_text.get("1.0", tk.END).strip()
        if not content:
            dialogs.show_warning("Atención",
                                 "Genera el contexto primero (⚡ Generar contexto).")
            return
        if copy_to_clipboard(self.root, content):
            self.sv_status.set("Contenido copiado al portapapeles.")

    def on_export_file(self):
        content = self.preview_text.get("1.0", tk.END).strip()
        if not content:
            dialogs.show_warning("Atención",
                                 "Genera el contexto primero (⚡ Generar contexto).")
            return
        ext = ".md" if self.var_fmt.get() == "markdown" else ".txt"
        fp  = dialogs.ask_save_file("Guardar Documento", default_ext=ext)
        if fp:
            ok, msg = write_text_file(fp, content)
            if ok:
                self.sv_status.set(f"Guardado: {os.path.basename(fp)}")
                dialogs.show_info("Guardado", f"Archivo guardado en:\n{fp}")
            else:
                dialogs.show_error("Error", f"No se pudo guardar: {msg}")
