"""
Dependency graph/resolver for project files.
Resolves imports/includes/requires to real project files and builds a dependency tree.
"""
import os
import re
from dataclasses import dataclass, field
from typing import List, Dict, Set, Optional

from app.core.dependency_detector import DependencyDetector
from app.utils.file_utils import safe_read_file


@dataclass
class DependencyNode:
    rel_path: str
    depth: int
    children: List["DependencyNode"] = field(default_factory=list)
    is_cycle: bool = False
    is_repeated: bool = False
    external: Optional[str] = None


class DependencyResolver:
    def __init__(
        self,
        folder_path: str,
        excluded_dirs: Optional[Set[str]] = None,
        detector: Optional[DependencyDetector] = None,
        max_read_bytes: int = 200_000,
    ):
        self.folder_path = os.path.abspath(folder_path)
        self.excluded_dirs = set(excluded_dirs or [])
        self.detector = detector or DependencyDetector()
        self.max_read_bytes = max_read_bytes

        self._file_index: Dict[str, str] = {}
        self._module_index: Dict[str, str] = {}
        self._content_cache: Dict[str, str] = {}
        self._deps_cache: Dict[str, List[str]] = {}
        self._expanded: Set[str] = set()

        self._build_index()

    # ------------------------------------------------------------------
    # Index
    # ------------------------------------------------------------------
    def _build_index(self) -> None:
        if not self.folder_path or not os.path.isdir(self.folder_path):
            return

        for dirpath, dirnames, filenames in os.walk(self.folder_path):
            dirnames[:] = [d for d in dirnames if d not in self.excluded_dirs]

            for f in filenames:
                abs_p = os.path.join(dirpath, f)
                rel = os.path.relpath(abs_p, self.folder_path).replace("\\", "/")
                self._file_index[rel] = abs_p

                if f.endswith(".py"):
                    mod = rel[:-3].replace("/", ".")
                    if mod.endswith(".__init__"):
                        mod = mod[: -len(".__init__")]
                    self._module_index[mod] = rel

    def _normalize(self, rel_path: str) -> str:
        return rel_path.replace("\\", "/").lstrip("./")

    def _read(self, rel_path: str) -> str:
        rel_path = self._normalize(rel_path)
        if rel_path in self._content_cache:
            return self._content_cache[rel_path]

        abs_p = self._file_index.get(rel_path)
        if not abs_p or not os.path.isfile(abs_p):
            self._content_cache[rel_path] = ""
            return ""

        content = safe_read_file(abs_p, max_bytes=self.max_read_bytes)
        self._content_cache[rel_path] = content
        return content

    # ------------------------------------------------------------------
    # Dependency detection
    # ------------------------------------------------------------------
    def get_dependencies(self, rel_path: str) -> List[str]:
        rel_path = self._normalize(rel_path)
        if rel_path in self._deps_cache:
            return self._deps_cache[rel_path]

        content = self._read(rel_path)
        if not content:
            self._deps_cache[rel_path] = []
            return []

        deps = self.detector.detect_file_dependencies(rel_path, content)
        self._deps_cache[rel_path] = deps
        return deps

    # ------------------------------------------------------------------
    # Resolution
    # ------------------------------------------------------------------
    def resolve_dependency(self, source_rel_path: str, dep_string: str) -> List[str]:
        source_rel_path = self._normalize(source_rel_path)
        ext = os.path.splitext(source_rel_path)[1].lower()

        if ext == ".py":
            candidates = self._resolve_python_dep(source_rel_path, dep_string)
        elif ext in (".js", ".jsx", ".ts", ".tsx", ".vue", ".mjs", ".cjs"):
            candidates = self._resolve_js_dep(source_rel_path, dep_string)
        elif ext == ".php":
            candidates = self._resolve_php_dep(source_rel_path, dep_string)
        else:
            candidates = self._resolve_by_basename(dep_string)

        result: List[str] = []
        for c in candidates:
            norm = self._normalize(c)
            if norm in self._file_index and norm not in result:
                result.append(norm)
        return result

    def _resolve_python_dep(self, source_rel: str, dep: str) -> List[str]:
        dep = dep.strip()

        if dep.startswith("import "):
            rest = dep[len("import "):].strip()
            parts = [p.strip() for p in rest.split(",")]
            result: List[str] = []
            for p in parts:
                p = p.split(" as ")[0].strip()
                result.extend(self._module_to_rel(p))
            return result

        if dep.startswith("from "):
            rest = dep[len("from "):].strip()
            if " import " not in rest:
                return []

            module, _names = rest.split(" import ", 1)
            module = module.strip()

            if module.startswith("."):
                base_dir = os.path.dirname(source_rel)
                dots = len(module) - len(module.lstrip("."))
                module_name = module.lstrip(".")

                up = max(0, dots - 1)
                parts = base_dir.split("/") if base_dir else []
                if up > 0:
                    parts = parts[:-up] if up <= len(parts) else []

                rel_dir = "/".join(parts)
                if module_name:
                    mod_path = (rel_dir + "/" + module_name.replace(".", "/")) if rel_dir else module_name.replace(".", "/")
                else:
                    mod_path = rel_dir

                return self._path_to_rel_candidates(mod_path)

            return self._module_to_rel(module)

        return []

    def _module_to_rel(self, module: str) -> List[str]:
        module = module.strip()
        if not module:
            return []

        if module in self._module_index:
            return [self._module_index[module]]

        pkg_init = module + ".__init__"
        if pkg_init in self._module_index:
            return [self._module_index[pkg_init]]

        path_py = module.replace(".", "/") + ".py"
        if path_py in self._file_index:
            return [path_py]

        path_init = module.replace(".", "/") + "/__init__.py"
        if path_init in self._file_index:
            return [path_init]

        return []

    def _path_to_rel_candidates(self, base_path: str) -> List[str]:
        base_path = self._normalize(base_path)
        candidates = []
        for cand in (
            base_path + ".py",
            base_path + "/__init__.py",
            base_path,
        ):
            if cand in self._file_index:
                candidates.append(cand)
        return candidates

    def _resolve_js_dep(self, source_rel: str, dep: str) -> List[str]:
        m = re.search(r'[\'"]([^\'"]+)[\'"]', dep)
        if not m:
            return []

        raw = m.group(1).strip()

        # 1. Import relativo: "./x" o "../x"
        if raw.startswith("."):
            base_dir = os.path.dirname(source_rel)
            target = os.path.normpath(os.path.join(base_dir, raw)).replace("\\", "/")
            return self._js_candidates(target)

        # 2. Import con alias Quasar / Vue CLI / Vite
        alias_targets = self._resolve_js_alias(raw)
        for target in alias_targets:
            hits = self._js_candidates(target)
            if hits:
                return hits

        # 3. Fallback: probar como ruta relativa al folder_path
        if "/" in raw:
            hits = self._js_candidates(raw)
            if hits:
                return hits

        # 4. Import externo (vue, quasar, axios, @quasar/app, ...)
        return []

    def _resolve_js_alias(self, raw: str) -> List[str]:
        """
        Devuelve rutas base candidatas (relativas al folder_path) para un import
        con alias. Se prueban varias variantes porque no sabemos si el usuario
        seleccionó la raíz del proyecto (con src/) o el propio src/.
        """
        aliases = {
            "src/":         ["src/", ""],
            "@/":           ["src/", ""],
            "app/":         ["src/", ""],
            "components/":  ["src/components/", "components/"],
            "layouts/":     ["src/layouts/",    "layouts/"],
            "pages/":       ["src/pages/",      "pages/"],
            "assets/":      ["src/assets/",     "assets/"],
            "boot/":        ["src/boot/",       "boot/"],
            "stores/":      ["src/stores/",     "stores/"],
            "router/":      ["src/router/",     "router/"],
            "composables/": ["src/composables/","composables/"],
            "mixins/":      ["src/mixins/",     "mixins/"],
            "directives/":  ["src/directives/", "directives/"],
            "plugins/":     ["src/plugins/",    "plugins/"],
            "services/":    ["src/services/",   "services/"],
            "helpers/":     ["src/helpers/",    "helpers/"],
        }
        for alias, prefixes in aliases.items():
            if raw.startswith(alias):
                rest = raw[len(alias):]
                return [p + rest for p in prefixes]
        return []

    def _js_candidates(self, target: str) -> List[str]:
        """Prueba target + extensiones y target/index.<ext> contra el índice."""
        target = self._normalize(target)
        out = []
        for ext in ("", ".js", ".jsx", ".ts", ".tsx", ".vue", ".json", ".mjs", ".cjs"):
            cand = target + ext
            if cand in self._file_index:
                out.append(cand)
        for ext in (".js", ".jsx", ".ts", ".tsx", ".vue"):
            cand = target + "/index" + ext
            if cand in self._file_index:
                out.append(cand)
        seen = set()
        result = []
        for c in out:
            if c not in seen:
                seen.add(c)
                result.append(c)
        return result

    def _resolve_php_dep(self, source_rel: str, dep: str) -> List[str]:
        m = re.search(r'[\'"]([^\'"]+)[\'"]', dep)
        if not m:
            return []

        raw = m.group(1)

        if raw.startswith("."):
            base_dir = os.path.dirname(source_rel)
            target = os.path.normpath(os.path.join(base_dir, raw)).replace("\\", "/")
            for cand in (target, target + ".php"):
                if cand in self._file_index:
                    return [cand]
            return []

        for cand in (raw, raw + ".php"):
            if cand in self._file_index:
                return [cand]

        return []

    def _resolve_by_basename(self, dep: str) -> List[str]:
        base = os.path.basename(dep)
        return [rel for rel in self._file_index if os.path.basename(rel) == base]

    # ------------------------------------------------------------------
    # Tree building
    # ------------------------------------------------------------------
    def build_tree(self, root_rel_path: str, max_depth: int = 50) -> DependencyNode:
        root_rel_path = self._normalize(root_rel_path)
        self._expanded.clear()
        return self._build_node(root_rel_path, depth=0, ancestors=set(), max_depth=max_depth)

    def _build_node(
        self,
        rel_path: str,
        depth: int,
        ancestors: Set[str],
        max_depth: int,
    ) -> DependencyNode:
        node = DependencyNode(rel_path=rel_path, depth=depth)

        if depth >= max_depth:
            return node

        if rel_path in ancestors:
            node.is_cycle = True
            return node

        if rel_path in self._expanded:
            node.is_repeated = True
            return node

        self._expanded.add(rel_path)

        new_ancestors = set(ancestors)
        new_ancestors.add(rel_path)

        for dep in self.get_dependencies(rel_path):
            for child_rel in self.resolve_dependency(rel_path, dep):
                child = self._build_node(
                    child_rel,
                    depth=depth + 1,
                    ancestors=new_ancestors,
                    max_depth=max_depth,
                )
                node.children.append(child)

        return node
