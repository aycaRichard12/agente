"""
Modular dependency and reference detector.
Scans source code for imports, includes, and requires across multiple languages.
Designed so full AST parsers can be easily plugged in per language later.
"""
import os
import re
from typing import List, Dict


class DependencyDetector:
    def __init__(self):
        # Regex patterns for fast, robust import detection
        self._py_pattern = re.compile(r'^\s*(?:import\s+[\w\.]+|from\s+[\w\.]+\s+import\s+[\w\*\,]+)', re.MULTILINE)
        self._js_pattern = re.compile(
            r'^\s*(?:import\s+.*?from\s+[\'"].*?[\'"]|import\s*[\'"].*?[\'"]|const\s+.*?=\s*require\([\'"].*?[\'"]\)|require\([\'"].*?[\'"]\))', 
            re.MULTILINE
        )
        self._php_pattern = re.compile(
            r'^\s*(?:require(?:_once)?\s*\(?[\'"].*?[\'"]\)?|include(?:_once)?\s*\(?[\'"].*?[\'"]\)?|use\s+[\w\\]+;)', 
            re.MULTILINE | re.IGNORECASE
        )
        self._cpp_pattern = re.compile(r'^\s*#include\s+[<"].*?[>"]', re.MULTILINE)
        self._java_pattern = re.compile(r'^\s*(?:import\s+[\w\.\*]+;|using\s+[\w\.]+;)', re.MULTILINE)

    def detect_file_dependencies(self, rel_path: str, raw_content: str) -> List[str]:
        """
        Extracts import and dependency statements from source code content.
        Returns a clean list of detected dependency strings.
        """
        if not raw_content or raw_content.startswith("[OMITIDO"):
            return []

        ext = os.path.splitext(rel_path)[1].lower()
        found = []

        if ext == ".py":
            found = self._scan_pattern(self._py_pattern, raw_content)
        elif ext in (".js", ".jsx", ".ts", ".tsx", ".vue"):
            found = self._scan_pattern(self._js_pattern, raw_content)
        elif ext == ".php":
            found = self._scan_pattern(self._php_pattern, raw_content)
        elif ext in (".c", ".cpp", ".h", ".hpp"):
            found = self._scan_pattern(self._cpp_pattern, raw_content)
        elif ext in (".java", ".cs"):
            found = self._scan_pattern(self._java_pattern, raw_content)

        return found[:15]  # Limit to top 15 dependencies per file to keep context clean

    def _scan_pattern(self, pattern: re.Pattern, content: str) -> List[str]:
        matches = pattern.findall(content)
        results = []
        for m in matches:
            cleaned = ' '.join(m.strip().split())
            if cleaned and cleaned not in results:
                results.append(cleaned)
        return results


def detect_project_dependencies(files_dict: Dict[str, str]) -> Dict[str, List[str]]:
    """
    Scans a dictionary mapping file rel_paths -> file contents.
    Returns dict of rel_path -> list of detected dependency strings.
    """
    detector = DependencyDetector()
    project_deps = {}
    for rel_path, content in files_dict.items():
        deps = detector.detect_file_dependencies(rel_path, content)
        if deps:
            project_deps[rel_path] = deps
    return project_deps
