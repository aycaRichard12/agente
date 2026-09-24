"""Core package initialization."""
from app.core.project_scanner import scan_directory
from app.core.file_selector import FileSelectorManager
from app.core.file_reader import read_and_format_file
from app.core.project_structure import build_folder_tree_str
from app.core.dependency_detector import DependencyDetector, detect_project_dependencies
from app.core.dependency_graph import DependencyResolver, DependencyNode

__all__ = [
    "scan_directory",
    "FileSelectorManager",
    "read_and_format_file",
    "build_folder_tree_str",
    "DependencyDetector",
    "detect_project_dependencies",
    "DependencyResolver",
    "DependencyNode",
]
