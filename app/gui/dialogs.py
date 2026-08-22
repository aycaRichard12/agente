"""Dialog helpers and alert wrappers."""
from tkinter import messagebox, filedialog
from typing import Optional, List


def show_info(title: str, message: str) -> None:
    messagebox.showinfo(title, message)


def show_warning(title: str, message: str) -> None:
    messagebox.showwarning(title, message)


def show_error(title: str, message: str) -> None:
    messagebox.showerror(title, message)


def ask_folder(title: str = "Seleccionar Carpeta") -> Optional[str]:
    return filedialog.askdirectory(title=title)


def ask_files(title: str = "Seleccionar Archivos") -> List[str]:
    files = filedialog.askopenfilenames(title=title)
    return list(files) if files else []


def ask_save_file(title: str = "Guardar Archivo", default_ext: str = ".md") -> Optional[str]:
    return filedialog.asksaveasfilename(
        title=title,
        defaultextension=default_ext,
        filetypes=[("Markdown Document", "*.md"), ("Text Document", "*.txt"), ("Todos los Archivos", "*.*")]
    )
