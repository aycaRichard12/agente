"""Path resolution and string formatting utilities."""
import os


def normalize_path(path: str) -> str:
    """Normalizes path for cross-platform consistency."""
    if not path:
        return ""
    return os.path.abspath(os.path.normpath(path))


def get_relative_path(path: str, start_dir: str) -> str:
    """Returns path relative to start_dir if possible, otherwise absolute path."""
    try:
        norm_path = normalize_path(path)
        norm_start = normalize_path(start_dir)
        if norm_path.startswith(norm_start):
            return os.path.relpath(norm_path, norm_start)
    except Exception:
        pass
    return os.path.basename(path)
