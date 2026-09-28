"""File search dialog with per-file dependency analysis action and optimized performance."""
import os
import queue
import threading
import tkinter as tk
from tkinter import ttk
from typing import Callable, List, Optional, Set, Tuple

from app.core.project_scanner import scan_directory

C_BG = "#1e2330"
C_PANEL = "#252b3b"
C_BORDER = "#323a50"
C_ACCENT = "#4f8ef7"
C_TEXT = "#e8eaf0"
C_TEXT2 = "#8b92a8"
C_ENTRY = "#2a3148"

MAX_RENDER_LIMIT = 500
BATCH_SIZE = 25              # 100 -> 25 : tandas más pequeñas, sin bloquear el mainloop
DEBOUNCE_MS = 150
LOADING_DELAY_MS = 200
QUEUE_CHECK_MS = 20
RENDER_BATCH_DELAY_MS = 15   # 1 -> 15 : cede el hilo entre tandas


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
        self._files_indexed: List[Tuple[str, str]] = []  # [(rel_path, rel_path_lower)]

        self._scan_id: int = 0
        self._scan_queue: queue.Queue = queue.Queue()

        self._debounce_timer: Optional[str] = None
        self._loading_timer: Optional[str] = None
        self._render_timer: Optional[str] = None
        self._poll_timer: Optional[str] = None
        self._last_query: Optional[str] = None

        self.lbl_loading: Optional[tk.Label] = None

        self._build_header()
        self._build_results()

        # Bind trace on search_var for debounced searching
        self._trace_id = self.search_var.trace_add("write", self._on_query_trace)

        # Cleanup on destroy
        self.bind("<Destroy>", self._on_destroy)

        self._load_files()

    def _build_header(self):
        hdr = tk.Frame(self, bg=C_PANEL, padx=12, pady=10)
        hdr.pack(fill=tk.X)

        header_top = tk.Frame(hdr, bg=C_PANEL)
        header_top.pack(fill=tk.X)

        tk.Label(
            header_top,
            text="🔎 Buscar archivos del proyecto",
            font=("Segoe UI", 12, "bold"),
            bg=C_PANEL,
            fg=C_TEXT,
        ).pack(side=tk.LEFT, anchor="w")

        self.lbl_loading = tk.Label(
            header_top,
            text="⏳ Escaneando...",
            font=("Segoe UI", 9, "italic"),
            bg=C_PANEL,
            fg=C_ACCENT,
        )

        row = tk.Frame(hdr, bg=C_PANEL)
        row.pack(fill=tk.X, pady=(6, 0))

        self.entry = ttk.Entry(row, textvariable=self.search_var, font=("Consolas", 9))
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 6))

        ttk.Button(row, text="Buscar", command=self._force_refresh_results).pack(side=tk.LEFT)
        ttk.Button(row, text="Limpiar", command=self._clear_search).pack(side=tk.LEFT, padx=(6, 0))

    def _build_results(self):
        container = tk.Frame(
            self,
            bg=C_ENTRY,
            bd=1,
            relief="flat",
            highlightbackground=C_BORDER,
            highlightthickness=1,
        )
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
            if self.winfo_exists():
                self.canvas.itemconfig(self.canvas_window, width=event.width)

        self.canvas.bind("<Configure>", _on_resize)

        # Scoped mousewheel binding directly to canvas and scroll_frame
        def _on_mousewheel(event):
            if not self.winfo_exists():
                return
            if event.delta:
                self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
            elif event.num == 4:
                self.canvas.yview_scroll(-1, "units")
            elif event.num == 5:
                self.canvas.yview_scroll(1, "units")

        self.canvas.bind("<MouseWheel>", _on_mousewheel)
        self.canvas.bind("<Button-4>", _on_mousewheel)
        self.canvas.bind("<Button-5>", _on_mousewheel)
        self.scroll_frame.bind("<MouseWheel>", _on_mousewheel)
        self.scroll_frame.bind("<Button-4>", _on_mousewheel)
        self.scroll_frame.bind("<Button-5>", _on_mousewheel)

        self.canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def _load_files(self, force_refresh: bool = False):
        self._scan_id += 1
        current_scan_id = self._scan_id

        # Schedule delayed loading indicator after 200ms
        self._cancel_timer("_loading_timer")
        self._loading_timer = self.after(
            LOADING_DELAY_MS, lambda: self._show_loading(current_scan_id)
        )

        # FIX: launch background worker: DB-first, os.walk fallback
        threading.Thread(
            target=self._async_scan_worker,
            args=(
                current_scan_id,
                self.folder_path,
                self.excluded_dirs,
                self._scan_queue,
                force_refresh,
            ),
            daemon=True,
        ).start()

        # Start queue polling loop on main GUI thread
        self._schedule_queue_check()

    def _schedule_queue_check(self):
        self._cancel_timer("_poll_timer")
        if self.winfo_exists():
            self._poll_timer = self.after(QUEUE_CHECK_MS, self._check_scan_queue)

    def _check_scan_queue(self):
        if not self.winfo_exists():
            return

        received = False
        latest_files = None
        source = None

        while True:
            try:
                sid, files, src = self._scan_queue.get_nowait()
                if sid == self._scan_id:
                    latest_files = files
                    source = src
                    received = True
            except queue.Empty:
                break

        if received and latest_files is not None:
            self._hide_loading()
            self.all_files = latest_files
            self._files_indexed = [(f, f.lower()) for f in latest_files]
            if self.lbl_loading is not None and self.winfo_exists():
                tag = "caché DB" if source == "db" else "escaneo"
                self.lbl_loading.config(
                    text=f"✓ {len(latest_files)} archivos ({tag})"
                )
            self._refresh_results(force=True)
        else:
            # Reschedule queue check
            self._schedule_queue_check()

    @staticmethod
    def _async_scan_worker(
        scan_id: int,
        folder_path: str,
        excluded_dirs: Set[str],
        res_queue: queue.Queue,
        force_refresh: bool = False,
    ):
        """Worker thread entry point: DB-first con fallback a os.walk.

        Estrategia:
          1) Si !force_refresh, consultar SQLite (project_cache.db). ~1 ms.
          2) Si la DB no tiene filas o el usuario forzó refresco, os.walk.
        """
        files: List[str] = []
        source = "scan"
        try:
            from app.core.storage.database import get_database

            if not force_refresh:
                db = get_database()
                db_files, _last_scanned, exists = db.load_file_paths(folder_path)
                if exists and db_files:
                    files = db_files
                    source = "db"

            if not files:
                files = scan_directory(
                    folder_path, excluded_dirs, allowed_extensions=None
                )
                source = "scan"
        except Exception:
            # Ante cualquier fallo, caer a escaneo directo
            try:
                files = scan_directory(
                    folder_path, excluded_dirs, allowed_extensions=None
                )
            except Exception:
                files = []
            source = "scan"

        res_queue.put((scan_id, files, source))

    def _show_loading(self, scan_id: int):
        if not self.winfo_exists():
            return
        if scan_id == self._scan_id and self.lbl_loading:
            self.lbl_loading.pack(side=tk.RIGHT)

    def _hide_loading(self):
        self._cancel_timer("_loading_timer")
        if self.winfo_exists() and self.lbl_loading:
            self.lbl_loading.pack_forget()

    def _on_query_trace(self, *args):
        self._cancel_timer("_debounce_timer")
        self._debounce_timer = self.after(DEBOUNCE_MS, self._refresh_results)

    def _force_refresh_results(self):
        self._cancel_timer("_debounce_timer")
        self._refresh_results(force=True)

    def _clear_search(self):
        self.search_var.set("")
        self._force_refresh_results()

    def _cancel_timer(self, attr_name: str):
        timer_id = getattr(self, attr_name, None)
        if timer_id:
            try:
                self.after_cancel(timer_id)
            except Exception:
                pass
            setattr(self, attr_name, None)

    def _cancel_render_task(self):
        self._cancel_timer("_render_timer")

    def _refresh_results(self, force: bool = False):
        if not self.winfo_exists():
            return

        query = self.search_var.get().strip().lower()
        if not force and self._last_query == query:
            return
        self._last_query = query

        self._cancel_render_task()

        # Clear existing scroll_frame children
        for child in self.scroll_frame.winfo_children():
            child.destroy()

        matches = [
            rel for rel, rel_lower in self._files_indexed
            if not query or query in rel_lower
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

        total_matches = len(matches)
        matches_to_render = matches[:MAX_RENDER_LIMIT]

        # FIX: incluso la primera tanda se agenda con after(0, ...) para no
        # bloquear el hilo de la GUI dentro de _refresh_results.
        self._render_timer = self.after(
            0,
            lambda: self._render_batch(matches_to_render, 0, total_matches),
        )

    def _render_batch(self, matches_subset: List[str], start_idx: int, total_matches: int):
        if not self.winfo_exists():
            return

        end_idx = min(start_idx + BATCH_SIZE, len(matches_subset))

        for idx in range(start_idx, end_idx):
            rel = matches_subset[idx]
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

        if end_idx < len(matches_subset):
            # FIX: 15 ms en lugar de 1 ms para que el mainloop procese eventos
            # (redibujado, teclado, ratón) entre tandas.
            self._render_timer = self.after(
                RENDER_BATCH_DELAY_MS,
                lambda: self._render_batch(matches_subset, end_idx, total_matches),
            )
        else:
            # Batch complete, display total matches summary if hard limit hit
            if total_matches > MAX_RENDER_LIMIT:
                footer = tk.Frame(self.scroll_frame, bg=C_ENTRY, padx=8, pady=6)
                footer.pack(fill=tk.X)
                tk.Label(
                    footer,
                    text=f"Mostrando {MAX_RENDER_LIMIT} de {total_matches:,} resultados. Afina la búsqueda para ver más.",
                    font=("Segoe UI", 8, "italic"),
                    bg=C_ENTRY,
                    fg=C_TEXT2,
                ).pack(anchor="w")

    def _analyze(self, rel_path: str):
        if self.on_analyze_dependencies:
            self.on_analyze_dependencies(rel_path)

    def _on_destroy(self, event):
        if event.widget == self:
            self._cancel_timer("_debounce_timer")
            self._cancel_timer("_loading_timer")
            self._cancel_timer("_render_timer")
            self._cancel_timer("_poll_timer")
            self._scan_id += 1  # invalidate any pending scan callbacks
            try:
                self.search_var.trace_remove("write", self._trace_id)
            except Exception:
                pass
