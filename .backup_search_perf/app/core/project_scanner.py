"""Project scanner module for scanning directory structures with caching."""
import os
import threading
from typing import Set, Dict, Any, List, Optional, Tuple
from app.utils.file_utils import KNOWN_BINARY_EXTENSIONS

_cache_lock = threading.Lock()
# Cache mapping: key -> (folder_mtime, valid_files)
_SCAN_CACHE: Dict[Tuple, Tuple[float, List[str]]] = {}
_MAX_CACHE_ENTRIES = 50


def clear_scan_cache() -> None:
    """Clears the scan directory cache."""
    with _cache_lock:
        _SCAN_CACHE.clear()


def is_file_allowed(filename: str, allowed_extensions: Optional[Set[str]], filter_by_ext: bool = True) -> bool:
    """Checks if file is allowed (not binary media and matching allowed extensions)."""
    ext = os.path.splitext(filename)[1].lower()
    if ext in KNOWN_BINARY_EXTENSIONS:
        return False
    if filter_by_ext and allowed_extensions:
        return ext in allowed_extensions
    return True


def scan_directory(
    folder_path: str,
    excluded_dirs: Optional[Set[str]] = None,
    allowed_extensions: Optional[Set[str]] = None,
    use_cache: bool = True,
    force_refresh: bool = False,
) -> List[str]:
    """
    Recursively scans folder_path ignoring excluded_dirs and non-allowed file extensions.
    Returns sorted list of relative file paths. Uses thread-safe caching with mtime checking.
    """
    if not folder_path or not os.path.isdir(folder_path):
        return []

    abs_folder = os.path.abspath(folder_path)
    excluded_set = set(excluded_dirs) if excluded_dirs else set()
    allowed_tuple = tuple(sorted(allowed_extensions)) if allowed_extensions else None
    cache_key = (abs_folder, tuple(sorted(excluded_set)), allowed_tuple)

    # FIX: firma de invalidación recursiva ligera (raíz + subdirectorios
    # inmediatos). No es perfecta, pero evita devolver caché obsoleta cuando
    # cambian archivos dentro de subcarpetas de primer nivel, sin coste de
    # os.walk completo.
    signature = 0.0
    try:
        signature = os.path.getmtime(abs_folder)
        with os.scandir(abs_folder) as it:
            for entry in it:
                if entry.is_dir(follow_symlinks=False):
                    try:
                        signature = max(
                            signature,
                            entry.stat(follow_symlinks=False).st_mtime,
                        )
                    except OSError:
                        continue
    except OSError:
        pass

    if use_cache and not force_refresh:
        with _cache_lock:
            if cache_key in _SCAN_CACHE:
                cached_mtime, cached_files = _SCAN_CACHE[cache_key]
                if cached_mtime == signature:
                    return list(cached_files)

    valid_files = []

    def _walk_error(err: OSError):
        pass  # Ignore permission/access errors gracefully

    try:
        for dirpath, dirnames, filenames in os.walk(abs_folder, onerror=_walk_error):
            dirnames[:] = [d for d in dirnames if d not in excluded_set]
            rel_dir = os.path.relpath(dirpath, abs_folder)

            for f in filenames:
                try:
                    if is_file_allowed(f, allowed_extensions):
                        rel_file = f if rel_dir == '.' else os.path.join(rel_dir, f)
                        valid_files.append(rel_file.replace("\\", "/"))
                except Exception:
                    continue
    except Exception:
        pass

    valid_files = sorted(valid_files)

    if use_cache:
        with _cache_lock:
            if len(_SCAN_CACHE) >= _MAX_CACHE_ENTRIES:
                try:
                    first_key = next(iter(_SCAN_CACHE))
                    del _SCAN_CACHE[first_key]
                except (StopIteration, KeyError):
                    pass
            _SCAN_CACHE[cache_key] = (folder_mtime, valid_files)

    return valid_files
