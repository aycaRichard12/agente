"""Project scanner module for scanning directory structures."""
import os
from typing import Set, Dict, Any, List
from app.utils.file_utils import KNOWN_BINARY_EXTENSIONS


def is_file_allowed(filename: str, allowed_extensions: Set[str], filter_by_ext: bool = True) -> bool:
    """Checks if file is allowed (not binary media and matching allowed extensions)."""
    ext = os.path.splitext(filename)[1].lower()
    if ext in KNOWN_BINARY_EXTENSIONS:
        return False
    if filter_by_ext and allowed_extensions:
        return ext in allowed_extensions
    return True


def scan_directory(folder_path: str, excluded_dirs: Set[str], allowed_extensions: Set[str] = None) -> List[str]:
    """
    Recursively scans folder_path ignoring excluded_dirs and non-allowed file extensions.
    Returns sorted list of relative file paths.
    """
    if not folder_path or not os.path.isdir(folder_path):
        return []

    valid_files = []
    for dirpath, dirnames, filenames in os.walk(folder_path):
        dirnames[:] = [d for d in dirnames if d not in excluded_dirs]
        rel_dir = os.path.relpath(dirpath, folder_path)
        
        for f in filenames:
            if is_file_allowed(f, allowed_extensions):
                rel_file = f if rel_dir == '.' else os.path.join(rel_dir, f)
                valid_files.append(rel_file)

    return sorted(valid_files)
