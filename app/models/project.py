"""Data models for project selection, files, and export configuration."""
from dataclasses import dataclass, field
from typing import Set, List, Optional
import os

DEFAULT_ALLOWED_EXTENSIONS = {
    ".py", ".js", ".jsx", ".ts", ".tsx", ".vue", ".php", ".html", ".htm",
    ".css", ".scss", ".sass", ".less", ".json", ".sql", ".md", ".txt",
    ".java", ".cpp", ".c", ".h", ".hpp", ".cs", ".go", ".rs", ".rb",
    ".sh", ".bat", ".cmd", ".ps1", ".yaml", ".yml", ".xml", ".ini", ".env", ".config"
}


@dataclass
class FileItem:
    """Represents an individual file item in the selection."""
    path: str
    rel_path: str = ""
    is_checked: bool = True
    is_individual: bool = False
    size: int = 0

    def __post_init__(self):
        if not self.rel_path:
            self.rel_path = os.path.basename(self.path)


@dataclass
class ProjectSelection:
    """Stores current selection state: 1 folder + N individual files."""
    folder_path: Optional[str] = None
    checked_folder_files: Set[str] = field(default_factory=set)
    individual_files: List[str] = field(default_factory=list)
    excluded_dirs: Set[str] = field(
        default_factory=lambda: {
            ".git", "node_modules", "__pycache__", "venv", ".venv", 
            "dist", "build", ".idea", ".vscode"
        }
    )
    allowed_extensions: Set[str] = field(default_factory=lambda: set(DEFAULT_ALLOWED_EXTENSIONS))
    filter_by_extension: bool = True

    def set_folder(self, folder_path: str) -> None:
        """Sets single project folder (replaces any previous folder)."""
        self.folder_path = folder_path
        self.checked_folder_files.clear()

    def remove_folder(self) -> None:
        """Clears single project folder."""
        self.folder_path = None
        self.checked_folder_files.clear()

    def add_individual_files(self, paths: List[str]) -> int:
        """Adds unique individual file paths."""
        added = 0
        for p in paths:
            abs_p = os.path.abspath(p)
            if abs_p not in self.individual_files:
                self.individual_files.append(abs_p)
                added += 1
        return added

    def remove_individual_file(self, path: str) -> None:
        """Removes a file from individual files list."""
        if path in self.individual_files:
            self.individual_files.remove(path)

    def clear_individual_files(self) -> None:
        """Clears all individual files."""
        self.individual_files.clear()

    def is_file_extension_allowed(self, filename: str) -> bool:
        """Checks if file extension is allowed."""
        if not self.filter_by_extension or not self.allowed_extensions:
            return True
        ext = os.path.splitext(filename)[1].lower()
        return ext in self.allowed_extensions


@dataclass
class ExportConfig:
    """Export and formatting configurations with size & file limits."""
    add_line_numbers: bool = True
    include_tree: bool = True
    include_system_instructions: bool = True
    max_file_size_mb: float = 2.0
    max_total_size_mb: float = 50.0
    max_files: int = 100
    output_format: str = "markdown"  # "markdown" or "text"
    max_chars_per_file: int = 60000
