"""File system I/O operations, binary detection, and memory-safe reading."""
import os
import tkinter as tk
from typing import Tuple

# Common non-code / binary / media extensions
KNOWN_BINARY_EXTENSIONS = {
    # Images
    ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".ico", ".svg", ".webp", ".tiff", ".psd",
    # Videos & Audio
    ".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm", ".mp3", ".wav", ".ogg", ".flac",
    # Executables & Compiled Binaries
    ".exe", ".dll", ".so", ".dylib", ".bin", ".dat", ".o", ".a", ".pyc", ".pyo", ".class", ".sys",
    # Archives & Compressed
    ".zip", ".tar", ".gz", ".7z", ".rar", ".bz2", ".xz", ".iso", ".jar",
    # Documents / Databases
    ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".db", ".sqlite", ".sqlite3"
}


def is_binary_file(path: str) -> bool:
    """
    Checks if a file is binary by extension and by inspecting the first 1024 bytes
    for null characters or non-text control bytes.
    """
    ext = os.path.splitext(path)[1].lower()
    if ext in KNOWN_BINARY_EXTENSIONS:
        return True

    try:
        with open(path, 'rb') as f:
            chunk = f.read(1024)
            if b'\x00' in chunk:
                return True
            # High proportion of non-printable bytes indicates binary
            if chunk:
                non_text = sum(1 for byte in chunk if byte < 9 or (13 < byte < 32) or byte == 127)
                if non_text / len(chunk) > 0.3:
                    return True
    except Exception:
        pass
    return False


def get_file_size(path: str) -> int:
    """Returns size of file in bytes."""
    try:
        return os.path.getsize(path)
    except Exception:
        return 0


def safe_read_file(path: str, max_bytes: int = 1_048_576) -> str:
    """
    Reads file content safely using common encodings.
    Truncates content if size exceeds max_bytes to protect memory usage.
    """
    if is_binary_file(path):
        return f"[OMITIDO: Archivo binario no textual - {os.path.basename(path)}]"

    file_size = get_file_size(path)
    is_truncated = False
    
    if file_size > max_bytes:
        is_truncated = True

    encodings = ['utf-8', 'utf-8-sig', 'latin-1', 'cp1252']
    content = None

    for enc in encodings:
        try:
            with open(path, 'r', encoding=enc) as f:
                if is_truncated:
                    content = f.read(max_bytes)
                else:
                    content = f.read()
                break
        except (UnicodeDecodeError, Exception):
            continue

    if content is None:
        try:
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read(max_bytes) if is_truncated else f.read()
        except Exception as e:
            return f"[Error critico al leer archivo: {e}]"

    if is_truncated:
        size_mb = file_size / (1024 * 1024)
        limit_mb = max_bytes / (1024 * 1024)
        content += f"\n\n... [CONTENIDO TRUNCADO: El archivo supera el límite de {limit_mb:.1f} MB (Tamaño real: {size_mb:.2f} MB)] ..."

    return content


def write_text_file(path: str, content: str) -> Tuple[bool, str]:
    """Writes text content to file safely with UTF-8 encoding."""
    try:
        os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, "Guardado exitosamente."
    except Exception as e:
        return False, str(e)


def copy_to_clipboard(root: tk.Tk, text: str) -> bool:
    """Copies text string to system clipboard using Tkinter."""
    try:
        root.clipboard_clear()
        root.clipboard_append(text)
        root.update()
        return True
    except Exception:
        return False


def format_bytes(size_bytes: int) -> str:
    """Formats raw bytes into human readable string (KB, MB)."""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    else:
        return f"{size_bytes / (1024 * 1024):.2f} MB"
