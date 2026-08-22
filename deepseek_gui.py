import os
import sys
import json
import re
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
from pathlib import Path

# ------------------------------------------------------------
# Treeview con Checkboxes para explorar archivos de carpetas
# ------------------------------------------------------------
class CheckboxTreeview(ttk.Treeview):
    def __init__(self, master, **kwargs):
        super().__init__(master, columns=("check", "name"), show="tree headings", **kwargs)
        self.heading("#0", text="", anchor="w")
        self.heading("check", text="☑", anchor="center", command=self.toggle_all_header)
        self.heading("name", text="Archivo / Carpeta", anchor="w")
        self.column("#0", width=35, stretch=False)
        self.column("check", width=40, stretch=False, anchor="center")
        self.column("name", width=260, stretch=True)
        
        self.tag_configure("checked", foreground="#1b5e20")
        self.tag_configure("unchecked", foreground="#757575")
        self.bind("<Button-1>", self.on_click)
        self.checked_items = set()  # Contiene rutas relativas de archivos marcados

    def insert_file(self, parent, rel_path, is_checked=True):
        item = self.insert(parent, "end", text="📄", values=("☑" if is_checked else "☐", rel_path), tags=("checked" if is_checked else "unchecked",))
        if is_checked:
            self.checked_items.add(rel_path)
        return item

    def insert_folder(self, parent, rel_path):
        return self.insert(parent, "end", text="📁", values=("", rel_path), open=True)

    def check_item(self, item):
        rel_path = self.set(item, "name")
        if rel_path:
            self.set(item, "check", "☑")
            self.item(item, tags=("checked",))
            # Si no es un directorio (es un archivo)
            if not self.get_children(item):
                self.checked_items.add(rel_path)
        # Check Recursivo para hijos
        for child in self.get_children(item):
            self.check_item(child)

    def uncheck_item(self, item):
        rel_path = self.set(item, "name")
        if rel_path:
            self.set(item, "check", "☐")
            self.item(item, tags=("unchecked",))
            if rel_path in self.checked_items:
                self.checked_items.remove(rel_path)
        # Uncheck Recursivo para hijos
        for child in self.get_children(item):
            self.uncheck_item(child)

    def toggle_item(self, item):
        check_val = self.set(item, "check")
        if check_val == "☑":
            self.uncheck_item(item)
        else:
            self.check_item(item)

    def toggle_all_header(self):
        all_children = self.get_children()
        if not all_children:
            return
        # Si alguno no está marcado, marcamos todos; si todos están marcados, desmarcamos todos.
        all_checked = all(self.set(child, "check") == "☑" for child in all_children if self.set(child, "check") != "")
        for child in all_children:
            if all_checked:
                self.uncheck_item(child)
            else:
                self.check_item(child)

    def on_click(self, event):
        region = self.identify_region(event.x, event.y)
        item = self.identify_row(event.y)
        if not item:
            return
        column = self.identify_column(event.x)
        # Clic en la columna del checkbox (#2) o doble clic/clic directo
        if region == "cell" and column == "#2":
            self.toggle_item(item)
        elif region == "tree":
            # Clic en el icono
            self.toggle_item(item)

    def select_all(self):
        for item in self.get_children():
            self.check_item(item)

    def deselect_all(self):
        for item in self.get_children():
            self.uncheck_item(item)

    def get_checked_files(self):
        return list(self.checked_items)


# ------------------------------------------------------------
# Utilidades de lectura y formateo de archivos
# ------------------------------------------------------------
def safe_read_file(path):
    """Lee el contenido de un archivo probando encodings comunes."""
    encodings = ['utf-8', 'utf-8-sig', 'latin-1', 'cp1252']
    for enc in encodings:
        try:
            with open(path, 'r', encoding=enc) as f:
                return f.read()
        except UnicodeDecodeError:
            continue
        except Exception as e:
            return f"[Error al leer archivo: {e}]"
    # Fallback con ignorar errores
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()
    except Exception as e:
        return f"[Error critico al leer archivo: {e}]"

def format_code_with_lines(content, add_line_numbers=True):
    """Agrega números de línea al contenido."""
    if not add_line_numbers:
        return content
    lines = content.splitlines()
    width = len(str(len(lines)))
    width = max(width, 3)
    numbered = [f"{i+1:{width}d} | {line}" for i, line in enumerate(lines)]
    return '\n'.join(numbered)

def build_folder_tree_str(folder_path, checked_rel_paths, excluded_dirs):
    """Genera representación en texto del árbol de directorio."""
    tree_lines = [f"{os.path.basename(folder_path)}/"]
    checked_set = set(checked_rel_paths)

    for dirpath, dirnames, filenames in os.walk(folder_path):
        dirnames[:] = [d for d in dirnames if d not in excluded_dirs]
        rel_dir = os.path.relpath(dirpath, folder_path)
        
        # Filtrar archivos que fueron seleccionados
        valid_files = []
        for f in filenames:
            rel_file = f if rel_dir == '.' else os.path.join(rel_dir, f)
            if rel_file in checked_set:
                valid_files.append(f)

        if rel_dir != '.':
            depth = rel_dir.count(os.sep) + 1
            indent = '  ' * depth
            tree_lines.append(f"{indent}{os.path.basename(dirpath)}/")
        else:
            depth = 1
            indent = '  ' * depth

        subindent = '  ' * (depth + 1)
        for f in valid_files:
            tree_lines.append(f"{subindent}{f}")

    return '\n'.join(tree_lines)


# ------------------------------------------------------------
# Aplicación Principal (GUI)
# ------------------------------------------------------------
class DeepSeekPromptGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DeepSeek Code Packager - Preparador de Proyectos")
        self.root.geometry("1280x780")
        self.root.minsize(1024, 650)

        # Variables del sistema
        self.selected_folder = tk.StringVar(value="")
        self.individual_files = []  # Lista de rutas absolutas de archivos sueltos
        self.status_var = tk.StringVar(value="Listo para seleccionar archivos.")
        
        # Opciones de exclusión
        default_exclusions = ".git, node_modules, __pycache__, venv, .venv, dist, build, .idea, .vscode"
        self.exclusions_var = tk.StringVar(value=default_exclusions)
        
        # Opciones de salida
        self.opt_line_numbers = tk.BooleanVar(value=True)
        self.opt_include_tree = tk.BooleanVar(value=True)
        self.opt_split_files = tk.BooleanVar(value=False)
        self.opt_max_chars = tk.IntVar(value=60000)

        # Configurar Estilos ttk
        self.setup_styles()
        # Construir Interfaz
        self.build_ui()

    def setup_styles(self):
        style = ttk.Style()
        if "clam" in style.theme_names():
            style.theme_use("clam")
        
        # Colores
        bg_main = "#f4f6f9"
        accent = "#1565c0"
        
        self.root.configure(bg=bg_main)
        style.configure(".", font=("Segoe UI", 9))
        style.configure("Header.TLabel", font=("Segoe UI", 14, "bold"), foreground="#0d47a1")
        style.configure("SubHeader.TLabel", font=("Segoe UI", 9, "italic"), foreground="#555555")
        style.configure("Section.TLabelframe.Label", font=("Segoe UI", 10, "bold"), foreground="#1565c0")
        style.configure("Accent.TButton", font=("Segoe UI", 9, "bold"), background=accent, foreground="white")
        style.map("Accent.TButton", background=[("active", "#0d47a1")])

    def build_ui(self):
        # 1. Encabezado superior
        header_frame = ttk.Frame(self.root, padding=(12, 8))
        header_frame.pack(fill=tk.X)
        
        ttk.Label(header_frame, text="📦 DeepSeek Project & Code Packager", style="Header.TLabel").pack(anchor="w")
        ttk.Label(
            header_frame, 
            text="Prepara y empaqueta código en formatos .md / .txt para subir manualmente al web chat de DeepSeek (sin API ni envío automático)", 
            style="SubHeader.TLabel"
        ).pack(anchor="w")
        
        ttk.Separator(self.root, orient=tk.HORIZONTAL).pack(fill=tk.X, padx=10, pady=2)

        # 2. Panel Principal (PanedWindow Horizontal)
        main_paned = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        main_paned.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # ==========================================
        # PANEL IZQUIERDO: Selección de Archivos/Carpeta
        # ==========================================
        left_frame = ttk.Frame(main_paned, padding=5)
        main_paned.add(left_frame, weight=1)

        # -- Bloque 1: Selección de Carpeta (Máximo 1) --
        folder_group = ttk.LabelFrame(left_frame, text=" 📂 Carpeta del Proyecto (Máximo 1) ", style="Section.TLabelframe", padding=8)
        folder_group.pack(fill=tk.X, pady=(0, 5))

        f_entry_frame = ttk.Frame(folder_group)
        f_entry_frame.pack(fill=tk.X)

        self.folder_entry = ttk.Entry(f_entry_frame, textvariable=self.selected_folder, state="readonly")
        self.folder_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

        ttk.Button(f_entry_frame, text="Seleccionar Carpeta", command=self.select_folder).pack(side=tk.LEFT, padx=2)
        ttk.Button(f_entry_frame, text="❌ Quitar", command=self.remove_folder).pack(side=tk.LEFT, padx=2)

        # -- Bloque 2: Árbol de archivos de la carpeta --
        tree_group = ttk.LabelFrame(left_frame, text=" 🌲 Archivos de la Carpeta ", style="Section.TLabelframe", padding=8)
        tree_group.pack(fill=tk.BOTH, expand=True, pady=5)

        # Toolbar del árbol
        tree_tb = ttk.Frame(tree_group)
        tree_tb.pack(fill=tk.X, pady=(0, 4))
        
        ttk.Button(tree_tb, text="☑ Marcar Todos", command=self.select_all_tree).pack(side=tk.LEFT, padx=2)
        ttk.Button(tree_tb, text="☐ Desmarcar Todos", command=self.deselect_all_tree).pack(side=tk.LEFT, padx=2)
        ttk.Button(tree_tb, text="🔄 Recargar Árbol", command=self.reload_tree).pack(side=tk.RIGHT, padx=2)

        # Treeview con Scrollbar
        tree_container = ttk.Frame(tree_group)
        tree_container.pack(fill=tk.BOTH, expand=True)

        self.tree = CheckboxTreeview(tree_container)
        tree_scroll_y = ttk.Scrollbar(tree_container, orient=tk.VERTICAL, command=self.tree.yview)
        tree_scroll_x = ttk.Scrollbar(tree_container, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscrollcommand=tree_scroll_y.set, xscrollcommand=tree_scroll_x.set)

        tree_scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        tree_scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        self.tree.pack(fill=tk.BOTH, expand=True)

        # -- Bloque 3: Selección de Archivos Individuales (N archivos) --
        ind_group = ttk.LabelFrame(left_frame, text=" 📄 Archivos Individuales Adicionales (N archivos) ", style="Section.TLabelframe", padding=8)
        ind_group.pack(fill=tk.X, pady=(5, 0))

        ind_tb = ttk.Frame(ind_group)
        ind_tb.pack(fill=tk.X, pady=(0, 4))

        ttk.Button(ind_tb, text="➕ Agregar Archivos...", command=self.add_individual_files).pack(side=tk.LEFT, padx=2)
        ttk.Button(ind_tb, text="🗑️ Eliminar Seleccionado", command=self.remove_selected_individual_file).pack(side=tk.LEFT, padx=2)
        ttk.Button(ind_tb, text="🧹 Limpiar Lista", command=self.clear_individual_files).pack(side=tk.RIGHT, padx=2)

        # Listbox para archivos individuales
        list_container = ttk.Frame(ind_group)
        list_container.pack(fill=tk.X)

        self.file_listbox = tk.Listbox(list_container, height=4, selectmode=tk.SINGLE, font=("Consolas", 8))
        list_scroll = ttk.Scrollbar(list_container, orient=tk.VERTICAL, command=self.file_listbox.yview)
        self.file_listbox.configure(yscrollcommand=list_scroll.set)

        list_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.file_listbox.pack(fill=tk.X, expand=True)


        # ==========================================
        # PANEL DERECHO: Prompt, Opciones & Previsualización
        # ==========================================
        right_frame = ttk.Frame(main_paned, padding=5)
        main_paned.add(right_frame, weight=2)

        # -- Bloque 1: Configuración de Exclusiones y Formato --
        opts_group = ttk.LabelFrame(right_frame, text=" ⚙️ Opciones de Formato & Exclusiones ", style="Section.TLabelframe", padding=8)
        opts_group.pack(fill=tk.X, pady=(0, 5))

        # Exclusiones
        ex_frame = ttk.Frame(opts_group)
        ex_frame.pack(fill=tk.X, pady=2)
        ttk.Label(ex_frame, text="Carpetas Excluidas (separadas por coma):").pack(side=tk.LEFT, padx=(0, 5))
        ex_entry = ttk.Entry(ex_frame, textvariable=self.exclusions_var)
        ex_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        ex_entry.bind("<FocusOut>", lambda e: self.reload_tree())

        # Checkboxes de opciones
        chk_frame = ttk.Frame(opts_group)
        chk_frame.pack(fill=tk.X, pady=(4, 0))
        
        ttk.Checkbutton(chk_frame, text="Incluir números de línea", variable=self.opt_line_numbers).pack(side=tk.LEFT, padx=(0, 15))
        ttk.Checkbutton(chk_frame, text="Incluir árbol de estructura", variable=self.opt_include_tree).pack(side=tk.LEFT, padx=(0, 15))

        # -- Bloque 2: Descripción del Problema / Instrucciones --
        desc_group = ttk.LabelFrame(right_frame, text=" 📝 Descripción del Problema / Instrucciones para DeepSeek ", style="Section.TLabelframe", padding=8)
        desc_group.pack(fill=tk.X, pady=5)

        self.problem_text = scrolledtext.ScrolledText(desc_group, height=4, font=("Segoe UI", 9))
        self.problem_text.pack(fill=tk.X, expand=True)
        self.problem_text.insert(
            "1.0", 
            "Por favor analiza el siguiente código del proyecto. Identifica posibles errores, refactorizaciones recomendadas y soluciones al problema."
        )

        # -- Bloque 3: Botones de Acción y Previsualización --
        preview_group = ttk.LabelFrame(right_frame, text=" 🚀 Generación y Previsualización ", style="Section.TLabelframe", padding=8)
        preview_group.pack(fill=tk.BOTH, expand=True, pady=(5, 0))

        # Barra de botones de acción
        action_bar = ttk.Frame(preview_group)
        action_bar.pack(fill=tk.X, pady=(0, 5))

        ttk.Button(action_bar, text="⚡ Generar Prompt / Documento", style="Accent.TButton", command=self.generate_prompt).pack(side=tk.LEFT, padx=4)
        ttk.Button(action_bar, text="📋 Copiar al Portapapeles", command=self.copy_to_clipboard).pack(side=tk.LEFT, padx=4)
        ttk.Button(action_bar, text="💾 Exportar a Archivo (.md / .txt)", command=self.export_to_file).pack(side=tk.LEFT, padx=4)

        # Label de estadísticas
        self.stats_label = ttk.Label(action_bar, text="📊 Archivos: 0 | Líneas: 0 | Caracteres: 0", font=("Segoe UI", 9, "bold"))
        self.stats_label.pack(side=tk.RIGHT, padx=5)

        # Área de previsualización
        self.preview_text = scrolledtext.ScrolledText(preview_group, wrap=tk.NONE, font=("Consolas", 9))
        self.preview_text.pack(fill=tk.BOTH, expand=True)

        # 3. Barra de estado inferior
        status_bar = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN, anchor="w", padding=(5, 2))
        status_bar.pack(fill=tk.X, side=tk.BOTTOM)

    # ------------------------------------------------------------
    # Lógica de Selección de Carpeta y Archivos
    # ------------------------------------------------------------
    def select_folder(self):
        """Selecciona 1 carpeta (reemplaza cualquier carpeta previa)."""
        folder = filedialog.askdirectory(title="Seleccionar Carpeta del Proyecto")
        if folder:
            self.selected_folder.set(folder)
            self.reload_tree()
            self.status_var.set(f"Carpeta seleccionada: {folder}")

    def remove_folder(self):
        """Quita la carpeta seleccionada."""
        self.selected_folder.set("")
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.tree.checked_items.clear()
        self.status_var.set("Carpeta removida.")

    def get_excluded_dirs_set(self):
        """Obtiene el conjunto de directorios excluidos desde el campo de texto."""
        raw = self.exclusions_var.get()
        return {d.strip() for d in raw.split(',') if d.strip()}

    def reload_tree(self):
        """Reconstruye el árbol de archivos respetando las exclusiones configuradas."""
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.tree.checked_items.clear()

        folder_path = self.selected_folder.get()
        if not folder_path or not os.path.isdir(folder_path):
            return

        excluded_dirs = self.get_excluded_dirs_set()
        root_item = self.tree.insert("", "end", text="📁", values=("", folder_path), open=True)

        for dirpath, dirnames, filenames in os.walk(folder_path):
            dirnames[:] = [d for d in dirnames if d not in excluded_dirs]
            rel_dir = os.path.relpath(dirpath, folder_path)
            
            if rel_dir == '.':
                parent_item = root_item
            else:
                parent_item = self._find_folder_item(rel_dir)
                if not parent_item:
                    continue

            for d in sorted(dirnames):
                rel_sub = os.path.join(rel_dir, d) if rel_dir != '.' else d
                self.tree.insert_folder(parent_item, rel_sub)

            for f in sorted(filenames):
                rel_file = os.path.join(rel_dir, f) if rel_dir != '.' else f
                self.tree.insert_file(parent_item, rel_file)

    def _find_folder_item(self, rel_path):
        def search(item):
            if self.tree.set(item, "name") == rel_path:
                return item
            for child in self.tree.get_children(item):
                found = search(child)
                if found:
                    return found
            return None

        for item in self.tree.get_children():
            found = search(item)
            if found:
                return found
        return None

    def select_all_tree(self):
        self.tree.select_all()

    def deselect_all_tree(self):
        self.tree.deselect_all()

    def add_individual_files(self):
        """Agrega N archivos individuales a la lista."""
        files = filedialog.askopenfilenames(title="Seleccionar Archivos Individuales")
        if files:
            added_count = 0
            for f in files:
                abs_f = os.path.abspath(f)
                if abs_f not in self.individual_files:
                    self.individual_files.append(abs_f)
                    self.file_listbox.insert(tk.END, abs_f)
                    added_count += 1
            self.status_var.set(f"Se agregaron {added_count} archivos individuales.")

    def remove_selected_individual_file(self):
        selected_indices = self.file_listbox.curselection()
        if selected_indices:
            idx = selected_indices[0]
            removed = self.individual_files.pop(idx)
            self.file_listbox.delete(idx)
            self.status_var.set(f"Archivo removido: {os.path.basename(removed)}")

    def clear_individual_files(self):
        self.individual_files.clear()
        self.file_listbox.delete(0, tk.END)
        self.status_var.set("Lista de archivos individuales limpiada.")

    # ------------------------------------------------------------
    # Generación y Formateo del Prompt
    # ------------------------------------------------------------
    def collect_all_file_contents(self):
        """Recolecta y formatea el contenido de los archivos seleccionados."""
        folder_path = self.selected_folder.get()
        checked_rel_files = self.tree.get_checked_files()
        add_lines = self.opt_line_numbers.get()

        file_blocks = []
        total_files = 0

        # 1. Archivos de la carpeta seleccionada
        if folder_path and os.path.isdir(folder_path):
            for rel_f in sorted(checked_rel_files):
                full_path = os.path.join(folder_path, rel_f)
                if os.path.isfile(full_path):
                    raw_content = safe_read_file(full_path)
                    formatted_content = format_code_with_lines(raw_content, add_lines)
                    ext = os.path.splitext(rel_f)[1].lstrip('.')
                    file_blocks.append(f"### 📄 Archivo: {rel_f}\n```{ext}\n{formatted_content}\n```")
                    total_files += 1

        # 2. Archivos individuales adicionales
        for abs_f in self.individual_files:
            if os.path.isfile(abs_f):
                # Si está dentro de la carpeta seleccionada, mostrar ruta relativa; si no, mostrar nombre o ruta
                if folder_path and abs_f.startswith(folder_path):
                    display_name = os.path.relpath(abs_f, folder_path)
                else:
                    display_name = os.path.basename(abs_f) + f" ({abs_f})"
                
                raw_content = safe_read_file(abs_f)
                formatted_content = format_code_with_lines(raw_content, add_lines)
                ext = os.path.splitext(abs_f)[1].lstrip('.')
                file_blocks.append(f"### 📄 Archivo Individual: {display_name}\n```{ext}\n{formatted_content}\n```")
                total_files += 1

        return file_blocks, total_files

    def generate_prompt(self):
        folder_path = self.selected_folder.get()
        checked_rel_files = self.tree.get_checked_files()
        problem_desc = self.problem_text.get("1.0", tk.END).strip()
        excluded_dirs = self.get_excluded_dirs_set()

        if not folder_path and not self.individual_files:
            messagebox.showwarning("Atención", "Por favor selecciona una carpeta o al menos un archivo individual.")
            return

        file_blocks, total_files = self.collect_all_file_contents()
        if total_files == 0:
            messagebox.showwarning("Atención", "No hay archivos seleccionados para empaquetar.")
            return

        doc_parts = []
        doc_parts.append("# Contexto de Código y Proyecto para Análisis en DeepSeek\n")
        
        if problem_desc:
            doc_parts.append(f"## 📋 Descripción del Problema / Instrucciones\n{problem_desc}\n")

        if self.opt_include_tree.get() and folder_path and os.path.isdir(folder_path):
            tree_str = build_folder_tree_str(folder_path, checked_rel_files, excluded_dirs)
            doc_parts.append(f"## 🌲 Estructura del Proyecto\n```\n{tree_str}\n```\n")

        doc_parts.append("## 📦 Contenido de los Archivos Seleccionados\n")
        doc_parts.append("\n\n".join(file_blocks))

        full_doc = "\n".join(doc_parts)

        # Actualizar Vista Previa
        self.preview_text.delete("1.0", tk.END)
        self.preview_text.insert(tk.END, full_doc)

        # Estadísticas
        char_count = len(full_doc)
        line_count = full_doc.count("\n") + 1
        self.stats_label.config(text=f"📊 Archivos: {total_files} | Líneas: {line_count} | Caracteres: {char_count:,}")
        self.status_var.set(f"Prompt generado exitosamente ({total_files} archivos, {char_count:,} caracteres).")

    def copy_to_clipboard(self):
        content = self.preview_text.get("1.0", tk.END).strip()
        if not content:
            messagebox.showwarning("Atención", "No hay contenido generado para copiar. Haz clic en 'Generar Prompt' primero.")
            return
        
        self.root.clipboard_clear()
        self.root.clipboard_append(content)
        self.root.update()
        messagebox.showinfo("Éxito", "¡Contenido copiado al portapapeles! Ya puedes pegarlo directamente en DeepSeek Web Chat.")
        self.status_var.set("Contenido copiado al portapapeles.")

    def export_to_file(self):
        content = self.preview_text.get("1.0", tk.END).strip()
        if not content:
            messagebox.showwarning("Atención", "No hay contenido generado para exportar. Haz clic en 'Generar Prompt' primero.")
            return

        file_path = filedialog.asksaveasfilename(
            title="Guardar Documento de Proyecto",
            defaultextension=".md",
            filetypes=[("Markdown Document", "*.md"), ("Text Document", "*.txt"), ("Todos los Archivos", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                messagebox.showinfo("Guardado", f"Archivo guardado exitosamente en:\n{file_path}")
                self.status_var.set(f"Archivo guardado: {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("Error", f"Error al guardar el archivo: {e}")


# ------------------------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = DeepSeekPromptGeneratorApp(root)
    root.mainloop()