"""
Project Analyzer module.
Performs automatic scanning and analysis of project codebases:
- Primary language & framework detection (Python, JS/TS, Vue, Quasar, PHP/Laravel, Go, Rust, Java, etc.)
- Package manager detection (pip, npm, yarn, pnpm, bun, composer, cargo, etc.)
- Configuration files and entry points detection
- File and line counts, extensions breakdown
- Dependency detection (manifests + DependencyDetector source scan)
- Important files, large files (with warnings), and recently modified files
- Project structure tree representation
- Recommended file selection for context generation
- Excluded directories detection
"""
import os
import re
import json
from collections import Counter
from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Set, Any, Optional, Tuple

from app.core.dependency_detector import DependencyDetector
from app.core.project_structure import build_folder_tree_str
from app.models.project import DEFAULT_ALLOWED_EXTENSIONS
from app.utils.file_utils import (
    is_binary_file, get_file_size, safe_read_file, format_bytes, KNOWN_BINARY_EXTENSIONS
)

# Common directories that should be excluded
DEFAULT_ANALYZER_EXCLUSIONS = {
    ".git", "node_modules", "__pycache__", "venv", ".venv",
    "dist", "build", ".idea", ".vscode", "vendor", ".quasar", ".github", "public"
}

# Known entry point filenames
KNOWN_ENTRY_POINTS = {
    "main.py", "app.py", "manage.py", "wsgi.py", "asgi.py", "run.py", "server.py", "index.py", "__main__.py",
    "main.js", "main.ts", "index.js", "index.ts", "app.js", "app.ts", "server.js",
    "artisan", "server.php", "index.php", "main.go", "lib.rs", "main.rs"
}

# Known configuration filenames
KNOWN_CONFIG_FILES = {
    "package.json", "package-lock.json", "composer.json", "composer.lock",
    "tsconfig.json", "jsconfig.json", "quasar.config.js", "quasar.config.ts",
    "quasar.conf.js", "vite.config.js", "vite.config.ts", "webpack.config.js",
    "babel.config.js", "tailwind.config.js", "postcss.config.js", "eslint.config.js",
    "requirements.txt", "pyproject.toml", "setup.py", "setup.cfg", "Pipfile", "Pipfile.lock",
    "Dockerfile", "docker-compose.yml", "docker-compose.yaml",
    ".env.example", ".env", "Makefile", "Cargo.toml", "Cargo.lock", "go.mod", "go.sum",
    "pom.xml", "build.gradle", "build.gradle.kts"
}

# Extension to language mapping
EXTENSION_LANGUAGE_MAP = {
    ".py": "Python",
    ".js": "JavaScript",
    ".mjs": "JavaScript",
    ".cjs": "JavaScript",
    ".jsx": "JavaScript (React)",
    ".ts": "TypeScript",
    ".tsx": "TypeScript (React)",
    ".vue": "Vue.js",
    ".php": "PHP",
    ".html": "HTML",
    ".htm": "HTML",
    ".css": "CSS",
    ".scss": "SCSS",
    ".sass": "Sass",
    ".less": "Less",
    ".java": "Java",
    ".c": "C",
    ".cpp": "C++",
    ".cc": "C++",
    ".h": "C/C++ Header",
    ".hpp": "C++ Header",
    ".cs": "C#",
    ".go": "Go",
    ".rs": "Rust",
    ".rb": "Ruby",
    ".sql": "SQL",
    ".sh": "Shell Script",
    ".bat": "Batch",
    ".cmd": "Batch",
    ".ps1": "PowerShell",
    ".json": "JSON",
    ".yaml": "YAML",
    ".yml": "YAML",
    ".xml": "XML",
}


@dataclass
class FileMetric:
    rel_path: str
    abs_path: str
    size_bytes: int
    lines: int
    mtime: float
    mtime_formatted: str
    is_entry_point: bool = False
    is_config: bool = False
    is_important: bool = False
    score: int = 0


@dataclass
class ProjectAnalysisResult:
    folder_path: str
    project_name: str
    primary_language: str
    language_summary: Dict[str, Dict[str, int]]  # lang -> {files: N, lines: N}
    framework: str
    framework_details: str
    package_manager: str
    config_files: List[str]
    entry_points: List[str]
    total_files: int
    total_lines: int
    total_size_bytes: int
    extension_counts: Dict[str, int]
    extension_lines: Dict[str, int]
    manifest_dependencies: Dict[str, List[str]]
    code_dependencies: Dict[str, List[str]]
    important_files: List[str]
    large_files: List[Dict[str, Any]]
    recently_modified_files: List[Dict[str, Any]]
    project_structure_tree: str
    recommended_files: List[str]
    excluded_dirs_found: List[str]
    configured_exclusions: List[str]

    def to_formatted_report(self) -> str:
        """Produces a human-readable structured text report."""
        lines = [
            "==============================================================",
            f"REPORTE DE ANÁLISIS AUTOMÁTICO: {self.project_name}",
            "==============================================================",
            f"• Carpeta: {self.folder_path}",
            f"• Lenguaje principal: {self.primary_language}",
            f"• Framework: {self.framework}" + (f" ({self.framework_details})" if self.framework_details else ""),
            f"• Gestor de paquetes: {self.package_manager}",
            f"• Total archivos analizados: {self.total_files}",
            f"• Total líneas de código: {self.total_lines:,}",
            f"• Tamaño total: {format_bytes(self.total_size_bytes)}",
            "",
            "--------------------------------------------------------------",
            "RESUMEN POR EXTENSIÓN",
            "--------------------------------------------------------------",
        ]
        for ext, count in sorted(self.extension_counts.items(), key=lambda x: x[1], reverse=True):
            ext_lines = self.extension_lines.get(ext, 0)
            lines.append(f"  {ext}: {count} archivo(s) · {ext_lines:,} líneas")

        lines.extend([
            "",
            "--------------------------------------------------------------",
            "ENTRY POINTS Y ARCHIVOS DE CONFIGURACIÓN",
            "--------------------------------------------------------------",
        ])
        if self.entry_points:
            lines.append("Entry points:")
            for ep in self.entry_points:
                lines.append(f"  ⚡ {ep}")
        else:
            lines.append("Entry points: (No detectados en raíz)")

        if self.config_files:
            lines.append("Configuración:")
            for cf in self.config_files:
                lines.append(f"  ⚙️ {cf}")

        if self.manifest_dependencies:
            lines.extend([
                "",
                "--------------------------------------------------------------",
                "DEPENDENCIAS DETECTADAS (MANIFIESTOS)",
                "--------------------------------------------------------------",
            ])
            for manifest, deps in self.manifest_dependencies.items():
                lines.append(f"• {manifest}:")
                for d in deps[:20]:
                    lines.append(f"  - {d}")
                if len(deps) > 20:
                    lines.append(f"  ... (+{len(deps) - 20} dependencias más)")

        if self.large_files:
            lines.extend([
                "",
                "--------------------------------------------------------------",
                "ARCHIVOS MÁS GRANDES",
                "--------------------------------------------------------------",
            ])
            for f in self.large_files[:5]:
                warn = " ⚠️ [GRANDE]" if f.get("is_warning") else ""
                lines.append(f"  • {f['path']} ({format_bytes(f['size_bytes'])}, {f['lines']:,} líneas){warn}")

        if self.recently_modified_files:
            lines.extend([
                "",
                "--------------------------------------------------------------",
                "ARCHIVOS MODIFICADOS RECIENTEMENTE",
                "--------------------------------------------------------------",
            ])
            for f in self.recently_modified_files[:5]:
                lines.append(f"  • {f['path']} ({f['mtime_formatted']})")

        lines.extend([
            "",
            "--------------------------------------------------------------",
            "ARCHIVOS RECOMENDADOS PARA ANALIZAR",
            "--------------------------------------------------------------",
        ])
        for rf in self.recommended_files:
            lines.append(f"  ✓ {rf}")

        lines.extend([
            "",
            "--------------------------------------------------------------",
            "DIRECTORIOS EXCLUIDOS",
            "--------------------------------------------------------------",
        ])
        for ex in self.configured_exclusions:
            present = " (presente en proyecto)" if ex in self.excluded_dirs_found else ""
            lines.append(f"  ⚠️ {ex}/{present}")

        return "\n".join(lines)


class ProjectAnalyzer:
    """Analyzes a project directory to detect architecture, tech stack, dependencies and key files."""

    def __init__(self, excluded_dirs: Optional[Set[str]] = None, allowed_extensions: Optional[Set[str]] = None):
        self.excluded_dirs = set(excluded_dirs) if excluded_dirs is not None else set(DEFAULT_ANALYZER_EXCLUSIONS)
        self.allowed_extensions = set(allowed_extensions) if allowed_extensions is not None else set(DEFAULT_ALLOWED_EXTENSIONS)
        self.dep_detector = DependencyDetector()

    def analyze(self, folder_path: str, max_file_size_mb: float = 2.0) -> ProjectAnalysisResult:
        """Executes full scan and analysis on the given folder."""
        folder_path = os.path.abspath(folder_path)
        project_name = os.path.basename(folder_path) or folder_path

        files_metrics: List[FileMetric] = []
        extension_counts: Counter = Counter()
        extension_lines: Counter = Counter()
        languages_stats: Dict[str, Dict[str, int]] = {}
        excluded_dirs_found: Set[str] = set()

        total_files = 0
        total_lines = 0
        total_size = 0
        max_file_bytes = int(max_file_size_mb * 1024 * 1024)

        # 1. Recursive scan with exclusions
        for dirpath, dirnames, filenames in os.walk(folder_path):
            # Check for excluded directories present in the project
            for d in list(dirnames):
                if d in self.excluded_dirs:
                    excluded_dirs_found.add(d)
            # Exclude directories
            dirnames[:] = [d for d in sorted(dirnames) if d not in self.excluded_dirs]
            rel_dir = os.path.relpath(dirpath, folder_path)

            for f in sorted(filenames):
                rel_file = f if rel_dir == "." else os.path.join(rel_dir, f)
                full_path = os.path.join(dirpath, f)
                ext = os.path.splitext(f)[1].lower()

                if is_binary_file(full_path):
                    continue

                if self.allowed_extensions and ext not in self.allowed_extensions and f not in KNOWN_CONFIG_FILES and f not in KNOWN_ENTRY_POINTS:
                    continue

                try:
                    stat = os.stat(full_path)
                    size_bytes = stat.st_size
                    mtime = stat.st_mtime
                    mtime_fmt = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M:%S")
                except Exception:
                    size_bytes = 0
                    mtime = 0
                    mtime_fmt = "Desconocido"

                # Count lines safely
                lines_in_file = 0
                try:
                    with open(full_path, "r", encoding="utf-8", errors="ignore") as fp:
                        lines_in_file = sum(1 for _ in fp)
                except Exception:
                    lines_in_file = 0

                norm_rel = rel_file.replace("\\", "/")
                is_ep = self._is_entry_point(norm_rel)
                is_cfg = self._is_config_file(norm_rel)
                is_imp = self._is_important_file(norm_rel, is_ep, is_cfg)

                metric = FileMetric(
                    rel_path=norm_rel,
                    abs_path=full_path,
                    size_bytes=size_bytes,
                    lines=lines_in_file,
                    mtime=mtime,
                    mtime_formatted=mtime_fmt,
                    is_entry_point=is_ep,
                    is_config=is_cfg,
                    is_important=is_imp,
                )
                files_metrics.append(metric)

                total_files += 1
                total_lines += lines_in_file
                total_size += size_bytes
                extension_counts[ext or "[sin extensión]"] += 1
                extension_lines[ext or "[sin extensión]"] += lines_in_file

                lang = EXTENSION_LANGUAGE_MAP.get(ext, "Otro")
                if lang not in languages_stats:
                    languages_stats[lang] = {"files": 0, "lines": 0}
                languages_stats[lang]["files"] += 1
                languages_stats[lang]["lines"] += lines_in_file

        # 2. Determine Primary Language
        primary_lang = "Desconocido"
        if languages_stats:
            code_langs = {k: v for k, v in languages_stats.items() if k not in ("JSON", "YAML", "XML", "Otro")}
            if code_langs:
                primary_lang = max(code_langs.items(), key=lambda item: (item[1]["lines"], item[1]["files"]))[0]
            else:
                primary_lang = max(languages_stats.items(), key=lambda item: (item[1]["lines"], item[1]["files"]))[0]

        # 3. Detect Package Manager & Manifest Dependencies
        pkg_manager, manifest_deps = self._detect_package_manager_and_manifests(folder_path)

        # 4. Detect Framework
        framework, framework_details = self._detect_framework(folder_path, primary_lang, manifest_deps, files_metrics)

        # 5. Detect Code Dependencies using DependencyDetector
        code_dependencies = self._scan_code_dependencies(files_metrics)

        # 6. Categorize Files: Entry points, Configs, Important, Large, Recent
        entry_points = [m.rel_path for m in files_metrics if m.is_entry_point]
        config_files = [m.rel_path for m in files_metrics if m.is_config]
        important_files = [m.rel_path for m in files_metrics if m.is_important]

        # Large files (top 10 by size)
        large_files = []
        for m in sorted(files_metrics, key=lambda x: x.size_bytes, reverse=True)[:10]:
            large_files.append({
                "path": m.rel_path,
                "size_bytes": m.size_bytes,
                "lines": m.lines,
                "is_warning": m.size_bytes > max_file_bytes or m.size_bytes > 1_048_576
            })

        # Recently modified files (top 10 by mtime)
        recent_files = []
        for m in sorted(files_metrics, key=lambda x: x.mtime, reverse=True)[:10]:
            recent_files.append({
                "path": m.rel_path,
                "mtime": m.mtime,
                "mtime_formatted": m.mtime_formatted,
                "size_bytes": m.size_bytes,
                "lines": m.lines
            })

        # 7. Generate Recommended File Selection
        recommended_files = self._select_recommended_files(files_metrics, entry_points, config_files, recent_files)

        # 8. Project Structure Tree
        structure_tree = build_folder_tree_str(
            folder_path,
            [m.rel_path for m in files_metrics if not m.rel_path.count("/") > 2],
            self.excluded_dirs
        )

        return ProjectAnalysisResult(
            folder_path=folder_path,
            project_name=project_name,
            primary_language=primary_lang,
            language_summary=languages_stats,
            framework=framework,
            framework_details=framework_details,
            package_manager=pkg_manager,
            config_files=sorted(config_files),
            entry_points=sorted(entry_points),
            total_files=total_files,
            total_lines=total_lines,
            total_size_bytes=total_size,
            extension_counts=dict(extension_counts),
            extension_lines=dict(extension_lines),
            manifest_dependencies=manifest_deps,
            code_dependencies=code_dependencies,
            important_files=sorted(important_files),
            large_files=large_files,
            recently_modified_files=recent_files,
            project_structure_tree=structure_tree,
            recommended_files=recommended_files,
            excluded_dirs_found=sorted(list(excluded_dirs_found)),
            configured_exclusions=sorted(list(self.excluded_dirs)),
        )

    def _is_entry_point(self, rel_path: str) -> bool:
        """Determines if relative path is an entry point."""
        base = os.path.basename(rel_path).lower()
        if base in KNOWN_ENTRY_POINTS:
            parts = rel_path.split("/")
            if len(parts) <= 3:
                return True
        if rel_path in ("src/main.js", "src/main.ts", "src/index.js", "src/index.ts", "src/App.vue", "src/App.tsx"):
            return True
        if rel_path.endswith("artisan") or rel_path.endswith("public/index.php"):
            return True
        return False

    def _is_config_file(self, rel_path: str) -> bool:
        """Determines if file is a configuration file."""
        base = os.path.basename(rel_path).lower()
        if base in KNOWN_CONFIG_FILES:
            return True
        if base.startswith(".env") or base.endswith(".config.js") or base.endswith(".config.ts"):
            return True
        return False

    def _is_important_file(self, rel_path: str, is_ep: bool, is_cfg: bool) -> bool:
        """Identifies important architectural files (services, controllers, models, routes)."""
        if is_ep or is_cfg:
            return True
        p_lower = rel_path.lower()
        keywords = ("service", "controller", "model", "route", "router", "handler", "api", "repository")
        for kw in keywords:
            if kw in p_lower:
                return True
        return False

    def _detect_package_manager_and_manifests(self, folder: str) -> Tuple[str, Dict[str, List[str]]]:
        """Detects package manager and extracts declared dependencies from manifests."""
        manifest_deps: Dict[str, List[str]] = {}
        detected_managers = []

        # 1. Composer (PHP)
        composer_json = os.path.join(folder, "composer.json")
        if os.path.isfile(composer_json):
            mgr = "Composer"
            detected_managers.append(mgr)
            try:
                with open(composer_json, "r", encoding="utf-8") as fp:
                    data = json.load(fp)
                reqs = []
                for pkg, ver in data.get("require", {}).items():
                    reqs.append(f"{pkg}: {ver}")
                for pkg, ver in data.get("require-dev", {}).items():
                    reqs.append(f"{pkg} (dev): {ver}")
                if reqs:
                    manifest_deps["composer.json"] = reqs
            except Exception:
                pass

        # 2. Node / JS (npm, yarn, pnpm, bun)
        pkg_json = os.path.join(folder, "package.json")
        if os.path.isfile(pkg_json):
            js_mgr = "npm"
            if os.path.isfile(os.path.join(folder, "pnpm-lock.yaml")):
                js_mgr = "pnpm"
            elif os.path.isfile(os.path.join(folder, "yarn.lock")):
                js_mgr = "Yarn"
            elif os.path.isfile(os.path.join(folder, "bun.lockb")) or os.path.isfile(os.path.join(folder, "bun.lock")):
                js_mgr = "Bun"
            detected_managers.append(js_mgr)
            try:
                with open(pkg_json, "r", encoding="utf-8") as fp:
                    data = json.load(fp)
                deps = []
                for pkg, ver in data.get("dependencies", {}).items():
                    deps.append(f"{pkg}: {ver}")
                for pkg, ver in data.get("devDependencies", {}).items():
                    deps.append(f"{pkg} (dev): {ver}")
                if deps:
                    manifest_deps["package.json"] = deps
            except Exception:
                pass

        # 3. Python (pip, poetry, pipenv, conda)
        req_txt = os.path.join(folder, "requirements.txt")
        if os.path.isfile(req_txt):
            detected_managers.append("pip")
            try:
                with open(req_txt, "r", encoding="utf-8") as fp:
                    lines = [l.strip() for l in fp if l.strip() and not l.strip().startswith("#")]
                if lines:
                    manifest_deps["requirements.txt"] = lines
            except Exception:
                pass

        pyproject = os.path.join(folder, "pyproject.toml")
        if os.path.isfile(pyproject):
            if os.path.isfile(os.path.join(folder, "poetry.lock")):
                detected_managers.append("Poetry")
            else:
                detected_managers.append("pip/pyproject.toml")

        pipfile = os.path.join(folder, "Pipfile")
        if os.path.isfile(pipfile):
            detected_managers.append("Pipenv")

        # 4. Rust (Cargo)
        if os.path.isfile(os.path.join(folder, "Cargo.toml")):
            detected_managers.append("Cargo")

        # 5. Go (Go Modules)
        if os.path.isfile(os.path.join(folder, "go.mod")):
            detected_managers.append("Go Modules")

        # 6. Java (Maven / Gradle)
        if os.path.isfile(os.path.join(folder, "pom.xml")):
            detected_managers.append("Maven")
        elif os.path.isfile(os.path.join(folder, "build.gradle")) or os.path.isfile(os.path.join(folder, "build.gradle.kts")):
            detected_managers.append("Gradle")

        primary_mgr = ", ".join(detected_managers) if detected_managers else "Ninguno detectado"
        return primary_mgr, manifest_deps

    def _detect_framework(
        self, folder: str, primary_lang: str, manifest_deps: Dict[str, List[str]], files: List[FileMetric]
    ) -> Tuple[str, str]:
        """Detects framework (Laravel, Quasar, Vue, React, FastAPI, Django, Tkinter, etc.)."""
        # --- PHP / Laravel detection ---
        if os.path.isfile(os.path.join(folder, "artisan")) or any("laravel/framework" in d for d in manifest_deps.get("composer.json", [])):
            ver = "Laravel"
            for d in manifest_deps.get("composer.json", []):
                if "laravel/framework" in d:
                    ver = f"Laravel ({d.split(':')[-1].strip()})"
                    break
            return "Laravel", ver

        if any("symfony" in d.lower() for d in manifest_deps.get("composer.json", [])):
            return "Symfony", "Framework PHP Symfony"

        # --- Quasar Framework detection ---
        quasar_configs = [
            os.path.isfile(os.path.join(folder, "quasar.config.js")),
            os.path.isfile(os.path.join(folder, "quasar.config.ts")),
            os.path.isfile(os.path.join(folder, "quasar.conf.js")),
        ]
        pkg_deps = " ".join(manifest_deps.get("package.json", [])).lower()
        if any(quasar_configs) or "quasar" in pkg_deps or "@quasar/app" in pkg_deps:
            return "Quasar Framework", "Vue.js + Quasar CLI"

        # --- Vue / React / Next / Nuxt / Angular / Nest / Express ---
        if "next" in pkg_deps and "react" in pkg_deps:
            return "Next.js", "React Framework"
        if "nuxt" in pkg_deps:
            return "Nuxt.js", "Vue.js Framework"
        if "@nestjs/core" in pkg_deps:
            return "NestJS", "Node.js Framework"
        if "vue" in pkg_deps:
            return "Vue.js", "Frontend Framework"
        if "react" in pkg_deps:
            return "React", "Frontend Library"
        if "@angular/core" in pkg_deps:
            return "Angular", "Frontend Framework"
        if "express" in pkg_deps:
            return "Express.js", "Node.js Backend"

        # --- Python frameworks ---
        py_reqs = " ".join(manifest_deps.get("requirements.txt", [])).lower()
        if "django" in py_reqs:
            return "Django", "Web Framework"
        if "fastapi" in py_reqs:
            return "FastAPI", "Modern ASGI Web Framework"
        if "flask" in py_reqs:
            return "Flask", "Micro Web Framework"
        if "streamlit" in py_reqs:
            return "Streamlit", "Data App Framework"

        # Check Python imports across scanned files
        has_tkinter = False
        has_fastapi = False
        has_flask = False
        has_django = False
        has_pyside = False

        for f in files:
            if f.rel_path.endswith(".py"):
                try:
                    with open(f.abs_path, "r", encoding="utf-8", errors="ignore") as fp:
                        content = fp.read(4096)
                        if "tkinter" in content:
                            has_tkinter = True
                        if "fastapi" in content:
                            has_fastapi = True
                        if "flask" in content:
                            has_flask = True
                        if "django" in content:
                            has_django = True
                        if "PyQt" in content or "PySide" in content:
                            has_pyside = True
                except Exception:
                    pass

        if has_fastapi:
            return "FastAPI", "Python ASGI Framework"
        if has_django:
            return "Django", "Python Web Framework"
        if has_flask:
            return "Flask", "Python Web Framework"
        if has_pyside:
            return "PyQt / PySide", "Desktop GUI Framework"
        if has_tkinter:
            return "Tkinter", "Python Desktop GUI Standard"

        # Fallback based on primary language
        if primary_lang in ("Python", "JavaScript", "TypeScript", "PHP"):
            return "Estándar / Vanilla", f"Proyecto {primary_lang} modular"

        return "No detectado", ""

    def _scan_code_dependencies(self, files: List[FileMetric]) -> Dict[str, List[str]]:
        """Scans code files using DependencyDetector for imports and dependencies."""
        code_deps: Dict[str, List[str]] = {}
        key_files = [f for f in files if f.is_entry_point or f.is_important][:50]
        if not key_files:
            key_files = files[:30]

        for f in key_files:
            try:
                raw_text = safe_read_file(f.abs_path, max_bytes=100_000)
                deps = self.dep_detector.detect_file_dependencies(f.rel_path, raw_text)
                if deps:
                    code_deps[f.rel_path] = deps
            except Exception:
                pass

        return code_deps

    def _select_recommended_files(
        self, files: List[FileMetric], entry_points: List[str], config_files: List[str], recent_files: List[Dict[str, Any]]
    ) -> List[str]:
        """
        Smart heuristic algorithm that scores and pre-selects the most relevant files for context.
        Prioritizes:
        1. Entry points (main.py, artisan, src/main.js)
        2. Key configuration and dependency manifests (requirements.txt, package.json, composer.json)
        3. Core services, controllers, models, routes
        4. Recently modified files
        Excludes minified, lockfiles, heavy test files, binaries, or excluded directories.
        """
        recent_paths = {rf["path"] for rf in recent_files[:5]}

        for m in files:
            score = 0
            rel = m.rel_path.lower()

            if m.is_entry_point:
                score += 120

            if m.is_config:
                base = os.path.basename(rel)
                if base in ("requirements.txt", "package.json", "composer.json", "pyproject.toml", "quasar.config.js", "quasar.config.ts"):
                    score += 100
                elif base.endswith("lock") or base.endswith("lock.json"):
                    score -= 50
                else:
                    score += 50

            if m.is_important:
                score += 80

            if rel.startswith("app/") or rel.startswith("src/") or rel.startswith("core/"):
                score += 40

            if m.rel_path in recent_paths:
                score += 35

            if m.size_bytes > 300 * 1024:
                score -= 40
            if ".min." in rel or rel.endswith(".map"):
                score -= 100
            if "test" in rel or "spec" in rel:
                score -= 20

            m.score = score

        sorted_files = sorted(files, key=lambda x: x.score, reverse=True)

        recommended = []
        target_limit = min(max(len(sorted_files), 1), 25)

        for m in sorted_files:
            if m.score > 0 or len(recommended) < 5:
                base = os.path.basename(m.rel_path).lower()
                if base.endswith(".lock") or base in ("package-lock.json", "yarn.lock", "composer.lock"):
                    continue
                if ".min." in base:
                    continue
                recommended.append(m.rel_path)
            if len(recommended) >= target_limit:
                break

        # Always ensure entry points and primary manifests are in recommended
        for ep in entry_points:
            if ep not in recommended:
                recommended.insert(0, ep)
        for cfg in config_files:
            base = os.path.basename(cfg).lower()
            if base in ("requirements.txt", "package.json", "composer.json") and cfg not in recommended:
                recommended.append(cfg)

        return sorted(list(dict.fromkeys(recommended)))
