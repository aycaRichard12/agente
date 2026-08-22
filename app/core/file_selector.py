"""State manager for 1 folder + N individual files selections."""
from typing import List, Set, Optional
from app.models.project import ProjectSelection


class FileSelectorManager:
    def __init__(self):
        self.selection = ProjectSelection()

    def set_folder(self, folder_path: str) -> None:
        self.selection.set_folder(folder_path)

    def remove_folder(self) -> None:
        self.selection.remove_folder()

    def set_checked_folder_files(self, rel_paths: List[str]) -> None:
        self.selection.checked_folder_files = set(rel_paths)

    def add_individual_files(self, paths: List[str]) -> int:
        return self.selection.add_individual_files(paths)

    def remove_individual_file(self, path: str) -> None:
        self.selection.remove_individual_file(path)

    def clear_individual_files(self) -> None:
        self.selection.clear_individual_files()

    def set_exclusions_from_string(self, exclusions_str: str) -> None:
        parsed = {d.strip() for d in exclusions_str.split(',') if d.strip()}
        self.selection.excluded_dirs = parsed

    def get_selection(self) -> ProjectSelection:
        return self.selection
