"""File reading and code line numbering formatting core module."""
import os
from app.utils.file_utils import safe_read_file


def format_line_numbers(content: str, add_line_numbers: bool = True) -> str:
    """Adds formatted LINE X | line numbers to code string."""
    if not add_line_numbers:
        return content
    lines = content.splitlines()
    width = max(len(str(len(lines))), 1)
    numbered = [f"LINE {i+1:{width}d} | {line}" for i, line in enumerate(lines)]
    return '\n'.join(numbered)


def read_and_format_file(abs_path: str, add_line_numbers: bool = True, max_file_size_mb: float = 1.0) -> str:
    """Reads file content safely with size limit protection and formats line numbers."""
    if not os.path.isfile(abs_path):
        return f"[Archivo no encontrado: {abs_path}]"
    
    max_bytes = int(max_file_size_mb * 1024 * 1024)
    raw_content = safe_read_file(abs_path, max_bytes=max_bytes)
    return format_line_numbers(raw_content, add_line_numbers)
