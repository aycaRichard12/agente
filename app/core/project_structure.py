"""Generates textual tree representation of a folder structure using box-drawing characters."""
import os
from typing import Set, List, Dict, Any


def build_folder_tree_str(folder_path: str, checked_rel_paths: List[str], excluded_dirs: Set[str]) -> str:
    """Generates ASCII/Unicode tree text representation (├──, └──, │) of checked files."""
    if not folder_path or not os.path.isdir(folder_path):
        return ""

    root_name = os.path.basename(folder_path) or folder_path
    
    # Build nested dict hierarchy of checked files
    hierarchy: Dict[str, Any] = {}
    for rel_path in sorted(checked_rel_paths):
        parts = rel_path.split(os.sep)
        curr = hierarchy
        for part in parts[:-1]:
            curr = curr.setdefault(part, {})
        curr[parts[-1]] = None  # File leaf

    def render_node(node_dict: Dict[str, Any], prefix: str = "") -> List[str]:
        lines = []
        keys = list(node_dict.keys())
        for idx, key in enumerate(keys):
            is_last = (idx == len(keys) - 1)
            connector = "└── " if is_last else "├── "
            val = node_dict[key]
            if val is None:
                # File
                lines.append(f"{prefix}{connector}{key}")
            else:
                # Directory
                lines.append(f"{prefix}{connector}{key}/")
                new_prefix = prefix + ("    " if is_last else "│   ")
                lines.extend(render_node(val, new_prefix))
        return lines

    tree_lines = [f"{root_name}/"]
    tree_lines.extend(render_node(hierarchy))
    return "\n".join(tree_lines)
