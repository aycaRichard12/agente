==============================================================
REPORTED PROBLEM OR GOAL / PROBLEMA REPORTADO U OBJETIVO
==============================================================
generar el codigo en python para hacer el cambio el codigo se creara en la raiz del archivo 
el problema es este ejemplo seleccione un proyecto en quasar 
entre al modulodo de buscador seleccione un archivo raiz y vi todas sus dependencia pero al aplicar seleccion no me selecciona todas las dependencias


==============================================================
SELECTED ANALYSIS PROFILE / PERFIL DE ANÁLISIS: 🐞 Detect errors
==============================================================
• Objetivo: Identificar errores de sintaxis, bugs lógicos, excepciones no controladas, condiciones de carrera y fallos de tipo en el código.
• Enfoque: Detección exhaustiva de bugs, casos límite (edge cases), seguridad de nulos/undefined, control de flujo y manejo robusto de excepciones.
• Prioridades: 1. Crashes y errores que detienen la ejecución. 2. Fallos silenciosos y corrupción de estado. 3. Manejo deficiente de excepciones. 4. Regresiones potenciales.
• Resultado esperado: Localización exacta de cada error (archivo y línea), causa raíz técnica, código corregido listo para copiar/pegar y caso de prueba de verificación.

⚠️ REGLA DE CONCRECIÓN TÉCNICA: El análisis debe ser CONCRETO, TÉCNICO y ORIENTADO A LA ACCIÓN. Concéntrate exclusivamente en fallos reproducibles y errores verificables. Omite comentarios estilísticos o divagaciones teóricas que no resuelvan un error.

==============================================================
PROJECT CONTEXT / CONTEXTO DEL PROYECTO
==============================================================
• Nombre del Proyecto: agente
• Ruta Base: /media/richard/Nuevo vol/quasar/dess/deploy/agente
• Fecha de Generación: 2026-09-28 15:24:45

--------------------------------------------------------------
PROJECT SUMMARY
--------------------------------------------------------------
Selected files: 66
File extensions:
  .py: 56
  .md: 3
  .bat: 3
  .txt: 2
  .sh: 1
  .sql: 1

Total lines:
18,631

--------------------------------------------------------------
DEPENDENCIES AND REFERENCES
--------------------------------------------------------------
• .backup/app/core/project_analyzer.py:
  - import os
  - import re
  - import json
  - from collections import Counter
  - from dataclasses import dataclass,
  - from datetime import datetime
  - from typing import Dict,
  - from app.core.dependency_detector import DependencyDetector
  - from app.core.project_structure import build_folder_tree_str
  - from app.models.project import DEFAULT_ALLOWED_EXTENSIONS
• .backup/app/core/storage/database.py:
  - import os
  - import sqlite3
  - from typing import Dict,
• .backup/app/gui/file_tree.py:
  - import tkinter
  - from tkinter import ttk
  - from typing import Set,
• .backup/app/gui/main_window.py:
  - import os
  - import sys
  - import subprocess
  - import tkinter
  - from tkinter import ttk,
  - from typing import List,
  - from app.models.project import ExportConfig,
  - from app.core.file_selector import FileSelectorManager
  - from app.generators.prompt_generator import PromptGenerator
  - from app.generators.markdown_generator import generate_markdown_bundle
  - from app.generators.text_generator import generate_text_bundle
  - from app.generators.standalone_prompt_generator import generate_standalone_prompt
  - from app.gui.file_tree import CheckboxTreeview
  - from app.gui.analysis_dialog import ProjectAnalysisDialog
  - from app.core.project_analyzer import ProjectAnalyzer
• .backup_search_perf/app/core/project_scanner.py:
  - import os
  - import threading
  - from typing import Set,
  - from app.utils.file_utils import KNOWN_BINARY_EXTENSIONS
• .backup_search_perf/app/core/storage/database.py:
  - import os
  - import sqlite3
  - from typing import Dict,
• .backup_search_perf/app/gui/file_search_dialog.py:
  - import os
  - import queue
  - import threading
  - import tkinter
  - from tkinter import ttk
  - from typing import Callable,
  - from app.core.project_scanner import scan_directory
  - from app.core.storage.database import get_database
• app/core/__init__.py:
  - from app.core.project_scanner import scan_directory
  - from app.core.file_selector import FileSelectorManager
  - from app.core.file_reader import read_and_format_file
  - from app.core.project_structure import build_folder_tree_str
  - from app.core.dependency_detector import DependencyDetector,
  - from app.core.dependency_graph import DependencyResolver,
• app/core/dependency_detector.py:
  - import os
  - import re
  - from typing import List,
• app/core/dependency_graph.py:
  - import os
  - import re
  - from dataclasses import dataclass,
  - from typing import List,
  - from app.core.dependency_detector import DependencyDetector
  - from app.utils.file_utils import safe_read_file
• app/core/file_reader.py:
  - import os
  - from app.utils.file_utils import safe_read_file
• app/core/file_selector.py:
  - from typing import List,
  - from app.models.project import ProjectSelection
• app/core/intelligent_context.py:
  - import os
  - import re
  - from dataclasses import dataclass
  - from typing import List,
  - from app.core.dependency_detector import DependencyDetector
  - from app.utils.file_utils import get_file_size,
• app/core/project_analyzer.py:
  - import os
  - import re
  - import json
  - from collections import Counter
  - from dataclasses import dataclass,
  - from datetime import datetime
  - from typing import Dict,
  - from app.core.dependency_detector import DependencyDetector
  - from app.core.project_structure import build_folder_tree_str
  - from app.models.project import DEFAULT_ALLOWED_EXTENSIONS
  - from app.core.storage.database import get_database
• app/core/project_scanner.py:
  - import os
  - import threading
  - from typing import Set,
  - from app.utils.file_utils import KNOWN_BINARY_EXTENSIONS
• app/core/project_structure.py:
  - import os
  - from typing import Set,
• app/core/storage/__init__.py:
  - from app.core.storage.database import Database,
• app/core/storage/database.py:
  - import os
  - import sqlite3
  - from typing import Dict,
• app/generators/__init__.py:
  - from app.generators.markdown_generator import generate_markdown_bundle
  - from app.generators.text_generator import generate_text_bundle
  - from app.generators.prompt_generator import PromptGenerator
  - from app.generators.standalone_prompt_generator import generate_standalone_prompt
• app/generators/markdown_generator.py:
  - import os
  - from collections import Counter
  - from datetime import datetime
  - from typing import Tuple,
  - from app.models.project import ProjectSelection,
  - from app.core.file_reader import read_and_format_file
  - from app.core.project_structure import build_folder_tree_str
  - from app.core.dependency_detector import DependencyDetector
  - from app.models.analysis_types import get_analysis_profile
  - from app.models.analysis_modes import get_analysis_mode_config,
  - from app.utils.file_utils import is_binary_file,
• app/generators/prompt_generator.py:
  - from typing import Tuple
  - from app.models.project import ProjectSelection,
  - from app.generators.markdown_generator import generate_markdown_bundle
  - from app.generators.text_generator import generate_text_bundle
• app/generators/standalone_prompt_generator.py:
  - from app.models.analysis_types import get_analysis_profile
  - from app.models.analysis_modes import get_analysis_mode_config,
• app/generators/text_generator.py:
  - import os
  - from collections import Counter
  - from datetime import datetime
  - from typing import Tuple,
  - from app.models.project import ProjectSelection,
  - from app.core.file_reader import read_and_format_file
  - from app.core.project_structure import build_folder_tree_str
  - from app.core.dependency_detector import DependencyDetector
  - from app.models.analysis_types import get_analysis_profile
  - from app.models.analysis_modes import get_analysis_mode_config,
  - from app.utils.file_utils import is_binary_file,
• app/gui/__init__.py:
  - from app.gui.file_tree import CheckboxTreeview
  - from app.gui.main_window import MainWindow
• app/gui/analysis_dialog.py:
  - import tkinter
  - from tkinter import ttk,
  - from typing import List,
  - from app.core.project_analyzer import ProjectAnalysisResult
  - from app.utils.file_utils import copy_to_clipboard,
• app/gui/dependency_tree_dialog.py:
  - import tkinter
  - from tkinter import ttk
  - from typing import Callable,
  - from app.core.dependency_graph import DependencyResolver,
  - from app.gui.file_tree import CheckboxTreeview
• app/gui/dialogs.py:
  - from tkinter import messagebox,
  - from typing import Optional,
• app/gui/file_search_dialog.py:
  - import os
  - import queue
  - import threading
  - import tkinter
  - from tkinter import ttk
  - from typing import Callable,
  - from app.core.project_scanner import scan_directory
  - from app.core.storage.database import get_database
• app/gui/file_tree.py:
  - import tkinter
  - from tkinter import ttk
  - from typing import Set,
• app/gui/intelligent_context_dialog.py:
  - import os
  - import tkinter
  - from tkinter import ttk
  - from typing import List,
  - from app.utils.file_utils import format_bytes
• app/gui/main_window.py:
  - import os
  - import sys
  - import subprocess
  - import tkinter
  - from tkinter import ttk,
  - from typing import List,
  - from app.models.project import ExportConfig,
  - from app.core.file_selector import FileSelectorManager
  - from app.generators.prompt_generator import PromptGenerator
  - from app.generators.markdown_generator import generate_markdown_bundle
  - from app.generators.text_generator import generate_text_bundle
  - from app.generators.standalone_prompt_generator import generate_standalone_prompt
  - from app.gui.file_tree import CheckboxTreeview
  - from app.gui.analysis_dialog import ProjectAnalysisDialog
  - from app.core.project_analyzer import ProjectAnalyzer
• app/models/__init__.py:
  - from app.models.project import ProjectSelection,
• app/models/analysis_modes.py:
  - from dataclasses import dataclass
  - from typing import Dict
• app/models/analysis_types.py:
  - from dataclasses import dataclass
  - from typing import Dict,
• app/models/project.py:
  - from dataclasses import dataclass,
  - from typing import Set,
  - import os
• app/utils/__init__.py:
  - from app.utils.path_utils import normalize_path,
  - from app.utils.file_utils import safe_read_file,
• app/utils/file_utils.py:
  - import os
  - import tkinter
  - from typing import Tuple
• app/utils/path_utils.py:
  - import os
• apply_changes.py:
  - import argparse
  - import os
  - import shutil
  - import sys
  - from datetime import datetime
  - from pathlib import Path
  - import re
  - from dataclasses import dataclass,
  - from typing import List,
  - from app.core.dependency_detector import DependencyDetector
  - from app.utils.file_utils import safe_read_file
  - import tkinter
  - from tkinter import ttk
  - from typing import Callable,
  - from app.core.dependency_graph import DependencyResolver,
• apply_phase1_sqlite.py:
  - import argparse
  - import os
  - import shutil
  - import sys
  - import py_compile
  - from datetime import datetime
  - from pathlib import Path
  - from app.core.storage.database import Database,
  - import sqlite3
  - from typing import Dict,
  - from app.core.storage.database import get_database
• apply_phase2_delta_scan.py:
  - import argparse
  - from datetime import datetime
  - from pathlib import Path
• apply_search_perf.py:
  - import argparse
  - import os
  - import shutil
  - import sys
  - import py_compile
  - from datetime import datetime
  - from pathlib import Path
  - from app.core.storage.database import get_database
• deepseek_gui.py:
  - from main import main
• main.py:
  - import sys
  - import os
  - import tkinter
  - from app.gui.main_window import MainWindow
• nuevo_script.py:
  - import argparse
  - import os
  - import shutil
  - import sys
  - import py_compile
  - from datetime import datetime
  - from pathlib import Path
  - from app.core.storage.database import Database,
  - import sqlite3
  - from typing import Dict,
  - from app.core.storage.database import get_database
• parche_quasar.py:
  - import argparse
  - import shutil
  - import sys
  - from datetime import datetime
  - from pathlib import Path
• reparar.py:
  - import argparse
  - import shutil
  - import sys
  - from datetime import datetime
  - from pathlib import Path
• resume_phase1_sqlite.py:
  - import argparse
  - import shutil
  - import sys
  - import py_compile
  - from datetime import datetime
  - from pathlib import Path
• tests/test_analysis_modes.py:
  - import unittest
  - from app.models.project import ExportConfig,
  - from app.generators.standalone_prompt_generator import generate_standalone_prompt
  - from app.generators.markdown_generator import generate_markdown_bundle
  - from app.generators.text_generator import generate_text_bundle
• tests/test_analysis_types.py:
  - import os
  - import sys
  - import unittest
  - from unittest.mock import patch
  - import tkinter
  - from app.models.project import ExportConfig,
  - from app.generators.standalone_prompt_generator import generate_standalone_prompt
  - from app.generators.markdown_generator import generate_markdown_bundle
  - from app.generators.text_generator import generate_text_bundle
  - from app.gui.main_window import MainWindow
• tests/test_dependency_graph.py:
  - import os
  - import shutil
  - import tempfile
  - import unittest
  - from app.core.dependency_graph import DependencyResolver
• tests/test_file_search_dialog.py:
  - import os
  - import shutil
  - import tempfile
  - import time
  - import unittest
  - import tkinter
  - from app.core.project_scanner import scan_directory,
  - from app.gui.file_search_dialog import FileSearchDialog,
• tests/test_integration_gui.py:
  - import os
  - import sys
  - import unittest
  - from unittest.mock import patch
  - import tkinter
  - from app.gui.main_window import MainWindow
  - from app.gui.analysis_dialog import ProjectAnalysisDialog
  - from app.core.project_analyzer import ProjectAnalyzer
• tests/test_intelligent_context.py:
  - import os
  - import shutil
  - import tempfile
  - import unittest
• tests/test_project_analyzer.py:
  - import os
  - import sys
  - import shutil
  - import tempfile
  - import unittest
  - import tkinter
  - from app.core.project_analyzer import ProjectAnalyzer,
  - from app.gui.file_tree import CheckboxTreeview

--------------------------------------------------------------
INSTRUCCIONES OBLIGATORIAS PARA DEEPSEEK (DETECT ERRORS)
--------------------------------------------------------------
El análisis debe ser CONCRETO, TÉCNICO y ORIENTADO A LA ACCIÓN. Concéntrate exclusivamente en fallos reproducibles y errores verificables. Omite comentarios estilísticos o divagaciones teóricas que no resuelvan un error.

Tu respuesta DEBE seguir exactamente la siguiente estructura Markdown adaptada al perfil:

# DIAGNOSIS
## Detected Bugs
[Lista técnica de los bugs encontrados con su causa raíz exacta]

# FILES TO MODIFY
## 1. [ruta/relativa/archivo.ext]
Approximate line: [número]
### Bug Description
[Explicación concisa del error]
### Current Code
```
[código con error]
```
### Bugfix Code
```
[código corregido listo para sustituir]
```

# VERIFICATION & EDGE CASES
[Prueba o caso límite para verificar que el bug fue resuelto]

REGLA OBLIGATORIA: No respondas con JSON. Responde con el Markdown estructurado exacto indicado arriba.

Estructura de Directorios:
```
agente/
├── .backup/
│   └── app/
│       ├── core/
│       │   ├── project_analyzer.py
│       │   └── storage/
│       │       └── database.py
│       └── gui/
│           ├── file_tree.py
│           └── main_window.py
├── .backup_apply_changes
├── .backup_search_perf/
│   └── app/
│       ├── core/
│       │   ├── project_scanner.py
│       │   └── storage/
│       │       └── database.py
│       └── gui/
│           └── file_search_dialog.py
├── .cache
├── README.md
├── app/
│   ├── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── dependency_detector.py
│   │   ├── dependency_graph.py
│   │   ├── file_reader.py
│   │   ├── file_selector.py
│   │   ├── intelligent_context.py
│   │   ├── project_analyzer.py
│   │   ├── project_scanner.py
│   │   ├── project_structure.py
│   │   └── storage/
│   │       ├── __init__.py
│   │       └── database.py
│   ├── generators/
│   │   ├── __init__.py
│   │   ├── markdown_generator.py
│   │   ├── prompt_generator.py
│   │   ├── standalone_prompt_generator.py
│   │   └── text_generator.py
│   ├── gui/
│   │   ├── __init__.py
│   │   ├── analysis_dialog.py
│   │   ├── dependency_tree_dialog.py
│   │   ├── dialogs.py
│   │   ├── file_search_dialog.py
│   │   ├── file_tree.py
│   │   ├── intelligent_context_dialog.py
│   │   └── main_window.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── analysis_modes.py
│   │   ├── analysis_types.py
│   │   └── project.py
│   └── utils/
│       ├── __init__.py
│       ├── file_utils.py
│       └── path_utils.py
├── apply_changes.py
├── apply_phase1_sqlite.py
├── apply_phase2_delta_scan.py
├── apply_search_perf.py
├── deepseek_gui.py
├── ejecutar.bat
├── ejecutar_con_consola.bat
├── iniciar_deepseek_debugger.sh
├── main.py
├── nuevo_script.py
├── output/
│   ├── deepseek_project_context.md
│   ├── deepseek_project_context.txt
│   ├── deepseek_prompt.md
│   └── etapas_produccion_export_2026-08-27_105739.sql
├── parche_quasar.py
├── reparar.py
├── requirements.txt
├── resume_phase1_sqlite.py
├── run.bat
└── tests/
    ├── test_analysis_modes.py
    ├── test_analysis_types.py
    ├── test_dependency_graph.py
    ├── test_file_search_dialog.py
    ├── test_integration_gui.py
    ├── test_intelligent_context.py
    └── test_project_analyzer.py
```


==============================================================
ATTACHMENTS / ARCHIVOS Y CÓDIGO FUENTE
==============================================================

==============================================================
FILE: .backup/app/core/project_analyzer.py
==============================================================
```py
LINE   1 | """
LINE   2 | Project Analyzer module.
LINE   3 | Performs automatic scanning and analysis of project codebases:
LINE   4 | - Primary language & framework detection (Python, JS/TS, Vue, Quasar, PHP/Laravel, Go, Rust, Java, etc.)
LINE   5 | - Package manager detection (pip, npm, yarn, pnpm, bun, composer, cargo, etc.)
LINE   6 | - Configuration files and entry points detection
LINE   7 | - File and line counts, extensions breakdown
LINE   8 | - Dependency detection (manifests + DependencyDetector source scan)
LINE   9 | - Important files, large files (with warnings), and recently modified files
LINE  10 | - Project structure tree representation
LINE  11 | - Recommended file selection for context generation
LINE  12 | - Excluded directories detection
LINE  13 | """
LINE  14 | import os
LINE  15 | import re
LINE  16 | import json
LINE  17 | from collections import Counter
LINE  18 | from dataclasses import dataclass, field
LINE  19 | from datetime import datetime
LINE  20 | from typing import Dict, List, Set, Any, Optional, Tuple
LINE  21 | 
LINE  22 | from app.core.dependency_detector import DependencyDetector
LINE  23 | from app.core.project_structure import build_folder_tree_str
LINE  24 | from app.models.project import DEFAULT_ALLOWED_EXTENSIONS
LINE  25 | from app.utils.file_utils import (
LINE  26 |     is_binary_file, get_file_size, safe_read_file, format_bytes, KNOWN_BINARY_EXTENSIONS
LINE  27 | )
LINE  28 | 
LINE  29 | # Common directories that should be excluded
LINE  30 | DEFAULT_ANALYZER_EXCLUSIONS = {
LINE  31 |     ".git", "node_modules", "__pycache__", "venv", ".venv",
LINE  32 |     "dist", "build", ".idea", ".vscode", "vendor", ".quasar", ".github", "public"
LINE  33 | }
LINE  34 | 
LINE  35 | # Known entry point filenames
LINE  36 | KNOWN_ENTRY_POINTS = {
LINE  37 |     "main.py", "app.py", "manage.py", "wsgi.py", "asgi.py", "run.py", "server.py", "index.py", "__main__.py",
LINE  38 |     "main.js", "main.ts", "index.js", "index.ts", "app.js", "app.ts", "server.js",
LINE  39 |     "artisan", "server.php", "index.php", "main.go", "lib.rs", "main.rs"
LINE  40 | }
LINE  41 | 
LINE  42 | # Known configuration filenames
LINE  43 | KNOWN_CONFIG_FILES = {
LINE  44 |     "package.json", "package-lock.json", "composer.json", "composer.lock",
LINE  45 |     "tsconfig.json", "jsconfig.json", "quasar.config.js", "quasar.config.ts",
LINE  46 |     "quasar.conf.js", "vite.config.js", "vite.config.ts", "webpack.config.js",
LINE  47 |     "babel.config.js", "tailwind.config.js", "postcss.config.js", "eslint.config.js",
LINE  48 |     "requirements.txt", "pyproject.toml", "setup.py", "setup.cfg", "Pipfile", "Pipfile.lock",
LINE  49 |     "Dockerfile", "docker-compose.yml", "docker-compose.yaml",
LINE  50 |     ".env.example", ".env", "Makefile", "Cargo.toml", "Cargo.lock", "go.mod", "go.sum",
LINE  51 |     "pom.xml", "build.gradle", "build.gradle.kts"
LINE  52 | }
LINE  53 | 
LINE  54 | # Extension to language mapping
LINE  55 | EXTENSION_LANGUAGE_MAP = {
LINE  56 |     ".py": "Python",
LINE  57 |     ".js": "JavaScript",
LINE  58 |     ".mjs": "JavaScript",
LINE  59 |     ".cjs": "JavaScript",
LINE  60 |     ".jsx": "JavaScript (React)",
LINE  61 |     ".ts": "TypeScript",
LINE  62 |     ".tsx": "TypeScript (React)",
LINE  63 |     ".vue": "Vue.js",
LINE  64 |     ".php": "PHP",
LINE  65 |     ".html": "HTML",
LINE  66 |     ".htm": "HTML",
LINE  67 |     ".css": "CSS",
LINE  68 |     ".scss": "SCSS",
LINE  69 |     ".sass": "Sass",
LINE  70 |     ".less": "Less",
LINE  71 |     ".java": "Java",
LINE  72 |     ".c": "C",
LINE  73 |     ".cpp": "C++",
LINE  74 |     ".cc": "C++",
LINE  75 |     ".h": "C/C++ Header",
LINE  76 |     ".hpp": "C++ Header",
LINE  77 |     ".cs": "C#",
LINE  78 |     ".go": "Go",
LINE  79 |     ".rs": "Rust",
LINE  80 |     ".rb": "Ruby",
LINE  81 |     ".sql": "SQL",
LINE  82 |     ".sh": "Shell Script",
LINE  83 |     ".bat": "Batch",
LINE  84 |     ".cmd": "Batch",
LINE  85 |     ".ps1": "PowerShell",
LINE  86 |     ".json": "JSON",
LINE  87 |     ".yaml": "YAML",
LINE  88 |     ".yml": "YAML",
LINE  89 |     ".xml": "XML",
LINE  90 | }
LINE  91 | 
LINE  92 | 
LINE  93 | @dataclass
LINE  94 | class FileMetric:
LINE  95 |     rel_path: str
LINE  96 |     abs_path: str
LINE  97 |     size_bytes: int
LINE  98 |     lines: int
LINE  99 |     mtime: float
LINE 100 |     mtime_formatted: str
LINE 101 |     is_entry_point: bool = False
LINE 102 |     is_config: bool = False
LINE 103 |     is_important: bool = False
LINE 104 |     score: int = 0
LINE 105 | 
LINE 106 | 
LINE 107 | @dataclass
LINE 108 | class ProjectAnalysisResult:
LINE 109 |     folder_path: str
LINE 110 |     project_name: str
LINE 111 |     primary_language: str
LINE 112 |     language_summary: Dict[str, Dict[str, int]]  # lang -> {files: N, lines: N}
LINE 113 |     framework: str
LINE 114 |     framework_details: str
LINE 115 |     package_manager: str
LINE 116 |     config_files: List[str]
LINE 117 |     entry_points: List[str]
LINE 118 |     total_files: int
LINE 119 |     total_lines: int
LINE 120 |     total_size_bytes: int
LINE 121 |     extension_counts: Dict[str, int]
LINE 122 |     extension_lines: Dict[str, int]
LINE 123 |     manifest_dependencies: Dict[str, List[str]]
LINE 124 |     code_dependencies: Dict[str, List[str]]
LINE 125 |     important_files: List[str]
LINE 126 |     large_files: List[Dict[str, Any]]
LINE 127 |     recently_modified_files: List[Dict[str, Any]]
LINE 128 |     project_structure_tree: str
LINE 129 |     recommended_files: List[str]
LINE 130 |     excluded_dirs_found: List[str]
LINE 131 |     configured_exclusions: List[str]
LINE 132 | 
LINE 133 |     def to_formatted_report(self) -> str:
LINE 134 |         """Produces a human-readable structured text report."""
LINE 135 |         lines = [
LINE 136 |             "==============================================================",
LINE 137 |             f"REPORTE DE ANÁLISIS AUTOMÁTICO: {self.project_name}",
LINE 138 |             "==============================================================",
LINE 139 |             f"• Carpeta: {self.folder_path}",
LINE 140 |             f"• Lenguaje principal: {self.primary_language}",
LINE 141 |             f"• Framework: {self.framework}" + (f" ({self.framework_details})" if self.framework_details else ""),
LINE 142 |             f"• Gestor de paquetes: {self.package_manager}",
LINE 143 |             f"• Total archivos analizados: {self.total_files}",
LINE 144 |             f"• Total líneas de código: {self.total_lines:,}",
LINE 145 |             f"• Tamaño total: {format_bytes(self.total_size_bytes)}",
LINE 146 |             "",
LINE 147 |             "--------------------------------------------------------------",
LINE 148 |             "RESUMEN POR EXTENSIÓN",
LINE 149 |             "--------------------------------------------------------------",
LINE 150 |         ]
LINE 151 |         for ext, count in sorted(self.extension_counts.items(), key=lambda x: x[1], reverse=True):
LINE 152 |             ext_lines = self.extension_lines.get(ext, 0)
LINE 153 |             lines.append(f"  {ext}: {count} archivo(s) · {ext_lines:,} líneas")
LINE 154 | 
LINE 155 |         lines.extend([
LINE 156 |             "",
LINE 157 |             "--------------------------------------------------------------",
LINE 158 |             "ENTRY POINTS Y ARCHIVOS DE CONFIGURACIÓN",
LINE 159 |             "--------------------------------------------------------------",
LINE 160 |         ])
LINE 161 |         if self.entry_points:
LINE 162 |             lines.append("Entry points:")
LINE 163 |             for ep in self.entry_points:
LINE 164 |                 lines.append(f"  ⚡ {ep}")
LINE 165 |         else:
LINE 166 |             lines.append("Entry points: (No detectados en raíz)")
LINE 167 | 
LINE 168 |         if self.config_files:
LINE 169 |             lines.append("Configuración:")
LINE 170 |             for cf in self.config_files:
LINE 171 |                 lines.append(f"  ⚙️ {cf}")
LINE 172 | 
LINE 173 |         if self.manifest_dependencies:
LINE 174 |             lines.extend([
LINE 175 |                 "",
LINE 176 |                 "--------------------------------------------------------------",
LINE 177 |                 "DEPENDENCIAS DETECTADAS (MANIFIESTOS)",
LINE 178 |                 "--------------------------------------------------------------",
LINE 179 |             ])
LINE 180 |             for manifest, deps in self.manifest_dependencies.items():
LINE 181 |                 lines.append(f"• {manifest}:")
LINE 182 |                 for d in deps[:20]:
LINE 183 |                     lines.append(f"  - {d}")
LINE 184 |                 if len(deps) > 20:
LINE 185 |                     lines.append(f"  ... (+{len(deps) - 20} dependencias más)")
LINE 186 | 
LINE 187 |         if self.large_files:
LINE 188 |             lines.extend([
LINE 189 |                 "",
LINE 190 |                 "--------------------------------------------------------------",
LINE 191 |                 "ARCHIVOS MÁS GRANDES",
LINE 192 |                 "--------------------------------------------------------------",
LINE 193 |             ])
LINE 194 |             for f in self.large_files[:5]:
LINE 195 |                 warn = " ⚠️ [GRANDE]" if f.get("is_warning") else ""
LINE 196 |                 lines.append(f"  • {f['path']} ({format_bytes(f['size_bytes'])}, {f['lines']:,} líneas){warn}")
LINE 197 | 
LINE 198 |         if self.recently_modified_files:
LINE 199 |             lines.extend([
LINE 200 |                 "",
LINE 201 |                 "--------------------------------------------------------------",
LINE 202 |                 "ARCHIVOS MODIFICADOS RECIENTEMENTE",
LINE 203 |                 "--------------------------------------------------------------",
LINE 204 |             ])
LINE 205 |             for f in self.recently_modified_files[:5]:
LINE 206 |                 lines.append(f"  • {f['path']} ({f['mtime_formatted']})")
LINE 207 | 
LINE 208 |         lines.extend([
LINE 209 |             "",
LINE 210 |             "--------------------------------------------------------------",
LINE 211 |             "ARCHIVOS RECOMENDADOS PARA ANALIZAR",
LINE 212 |             "--------------------------------------------------------------",
LINE 213 |         ])
LINE 214 |         for rf in self.recommended_files:
LINE 215 |             lines.append(f"  ✓ {rf}")
LINE 216 | 
LINE 217 |         lines.extend([
LINE 218 |             "",
LINE 219 |             "--------------------------------------------------------------",
LINE 220 |             "DIRECTORIOS EXCLUIDOS",
LINE 221 |             "--------------------------------------------------------------",
LINE 222 |         ])
LINE 223 |         for ex in self.configured_exclusions:
LINE 224 |             present = " (presente en proyecto)" if ex in self.excluded_dirs_found else ""
LINE 225 |             lines.append(f"  ⚠️ {ex}/{present}")
LINE 226 | 
LINE 227 |         return "\n".join(lines)
LINE 228 | 
LINE 229 | 
LINE 230 | class ProjectAnalyzer:
LINE 231 |     """Analyzes a project directory to detect architecture, tech stack, dependencies and key files."""
LINE 232 | 
LINE 233 |     def __init__(self, excluded_dirs: Optional[Set[str]] = None, allowed_extensions: Optional[Set[str]] = None):
LINE 234 |         self.excluded_dirs = set(excluded_dirs) if excluded_dirs is not None else set(DEFAULT_ANALYZER_EXCLUSIONS)
LINE 235 |         self.allowed_extensions = set(allowed_extensions) if allowed_extensions is not None else set(DEFAULT_ALLOWED_EXTENSIONS)
LINE 236 |         self.dep_detector = DependencyDetector()
LINE 237 | 
LINE 238 |     def analyze(self, folder_path: str, max_file_size_mb: float = 2.0) -> ProjectAnalysisResult:
LINE 239 |         """Executes full scan and analysis on the given folder."""
LINE 240 |         folder_path = os.path.abspath(folder_path)
LINE 241 |         project_name = os.path.basename(folder_path) or folder_path
LINE 242 | 
LINE 243 |         files_metrics: List[FileMetric] = []
LINE 244 |         extension_counts: Counter = Counter()
LINE 245 |         extension_lines: Counter = Counter()
LINE 246 |         languages_stats: Dict[str, Dict[str, int]] = {}
LINE 247 |         excluded_dirs_found: Set[str] = set()
LINE 248 | 
LINE 249 |         total_files = 0
LINE 250 |         total_lines = 0
LINE 251 |         total_size = 0
LINE 252 |         max_file_bytes = int(max_file_size_mb * 1024 * 1024)
LINE 253 | 
LINE 254 |         # 1. Recursive scan with exclusions
LINE 255 |         for dirpath, dirnames, filenames in os.walk(folder_path):
LINE 256 |             # Check for excluded directories present in the project
LINE 257 |             for d in list(dirnames):
LINE 258 |                 if d in self.excluded_dirs:
LINE 259 |                     excluded_dirs_found.add(d)
LINE 260 |             # Exclude directories
LINE 261 |             dirnames[:] = [d for d in sorted(dirnames) if d not in self.excluded_dirs]
LINE 262 |             rel_dir = os.path.relpath(dirpath, folder_path)
LINE 263 | 
LINE 264 |             for f in sorted(filenames):
LINE 265 |                 rel_file = f if rel_dir == "." else os.path.join(rel_dir, f)
LINE 266 |                 full_path = os.path.join(dirpath, f)
LINE 267 |                 ext = os.path.splitext(f)[1].lower()
LINE 268 | 
LINE 269 |                 if self.allowed_extensions and ext not in self.allowed_extensions and f not in KNOWN_CONFIG_FILES and f not in KNOWN_ENTRY_POINTS:
LINE 270 |                     continue
LINE 271 | 
LINE 272 |                 if is_binary_file(full_path):
LINE 273 |                     continue
LINE 274 | 
LINE 275 |                 try:
LINE 276 |                     stat = os.stat(full_path)
LINE 277 |                     size_bytes = stat.st_size
LINE 278 |                     mtime = stat.st_mtime
LINE 279 |                     mtime_fmt = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M:%S")
LINE 280 |                 except Exception:
LINE 281 |                     size_bytes = 0
LINE 282 |                     mtime = 0
LINE 283 |                     mtime_fmt = "Desconocido"
LINE 284 | 
LINE 285 |                 # Count lines safely
LINE 286 |                 lines_in_file = 0
LINE 287 |                 if size_bytes <= max_file_bytes:
LINE 288 |                     try:
LINE 289 |                         with open(full_path, "r", encoding="utf-8", errors="ignore") as fp:
LINE 290 |                             lines_in_file = sum(1 for _ in fp)
LINE 291 |                     except Exception:
LINE 292 |                         lines_in_file = 0
LINE 293 | 
LINE 294 |                 norm_rel = rel_file.replace("\\", "/")
LINE 295 |                 is_ep = self._is_entry_point(norm_rel)
LINE 296 |                 is_cfg = self._is_config_file(norm_rel)
LINE 297 |                 is_imp = self._is_important_file(norm_rel, is_ep, is_cfg)
LINE 298 | 
LINE 299 |                 metric = FileMetric(
LINE 300 |                     rel_path=norm_rel,
LINE 301 |                     abs_path=full_path,
LINE 302 |                     size_bytes=size_bytes,
LINE 303 |                     lines=lines_in_file,
LINE 304 |                     mtime=mtime,
LINE 305 |                     mtime_formatted=mtime_fmt,
LINE 306 |                     is_entry_point=is_ep,
LINE 307 |                     is_config=is_cfg,
LINE 308 |                     is_important=is_imp,
LINE 309 |                 )
LINE 310 |                 files_metrics.append(metric)
LINE 311 | 
LINE 312 |                 total_files += 1
LINE 313 |                 total_lines += lines_in_file
LINE 314 |                 total_size += size_bytes
LINE 315 |                 extension_counts[ext or "[sin extensión]"] += 1
LINE 316 |                 extension_lines[ext or "[sin extensión]"] += lines_in_file
LINE 317 | 
LINE 318 |                 lang = EXTENSION_LANGUAGE_MAP.get(ext, "Otro")
LINE 319 |                 if lang not in languages_stats:
LINE 320 |                     languages_stats[lang] = {"files": 0, "lines": 0}
LINE 321 |                 languages_stats[lang]["files"] += 1
LINE 322 |                 languages_stats[lang]["lines"] += lines_in_file
LINE 323 | 
LINE 324 |         # 2. Determine Primary Language
LINE 325 |         primary_lang = "Desconocido"
LINE 326 |         if languages_stats:
LINE 327 |             code_langs = {k: v for k, v in languages_stats.items() if k not in ("JSON", "YAML", "XML", "Otro")}
LINE 328 |             if code_langs:
LINE 329 |                 primary_lang = max(code_langs.items(), key=lambda item: (item[1]["lines"], item[1]["files"]))[0]
LINE 330 |             else:
LINE 331 |                 primary_lang = max(languages_stats.items(), key=lambda item: (item[1]["lines"], item[1]["files"]))[0]
LINE 332 | 
LINE 333 |         # 3. Detect Package Manager & Manifest Dependencies
LINE 334 |         pkg_manager, manifest_deps = self._detect_package_manager_and_manifests(folder_path)
LINE 335 | 
LINE 336 |         # 4. Detect Framework
LINE 337 |         framework, framework_details = self._detect_framework(folder_path, primary_lang, manifest_deps, files_metrics)
LINE 338 | 
LINE 339 |         # 5. Detect Code Dependencies using DependencyDetector
LINE 340 |         code_dependencies = self._scan_code_dependencies(files_metrics)
LINE 341 | 
LINE 342 |         # 6. Categorize Files: Entry points, Configs, Important, Large, Recent
LINE 343 |         entry_points = [m.rel_path for m in files_metrics if m.is_entry_point]
LINE 344 |         config_files = [m.rel_path for m in files_metrics if m.is_config]
LINE 345 |         important_files = [m.rel_path for m in files_metrics if m.is_important]
LINE 346 | 
LINE 347 |         # Large files (top 10 by size)
LINE 348 |         large_files = []
LINE 349 |         for m in sorted(files_metrics, key=lambda x: x.size_bytes, reverse=True)[:10]:
LINE 350 |             large_files.append({
LINE 351 |                 "path": m.rel_path,
LINE 352 |                 "size_bytes": m.size_bytes,
LINE 353 |                 "lines": m.lines,
LINE 354 |                 "is_warning": m.size_bytes > max_file_bytes or m.size_bytes > 1_048_576
LINE 355 |             })
LINE 356 | 
LINE 357 |         # Recently modified files (top 10 by mtime)
LINE 358 |         recent_files = []
LINE 359 |         for m in sorted(files_metrics, key=lambda x: x.mtime, reverse=True)[:10]:
LINE 360 |             recent_files.append({
LINE 361 |                 "path": m.rel_path,
LINE 362 |                 "mtime": m.mtime,
LINE 363 |                 "mtime_formatted": m.mtime_formatted,
LINE 364 |                 "size_bytes": m.size_bytes,
LINE 365 |                 "lines": m.lines
LINE 366 |             })
LINE 367 | 
LINE 368 |         # 7. Generate Recommended File Selection
LINE 369 |         recommended_files = self._select_recommended_files(files_metrics, entry_points, config_files, recent_files)
LINE 370 | 
LINE 371 |         # 8. Project Structure Tree
LINE 372 |         structure_tree = build_folder_tree_str(
LINE 373 |             folder_path,
LINE 374 |             [m.rel_path for m in files_metrics if not m.rel_path.count("/") > 2],
LINE 375 |             self.excluded_dirs
LINE 376 |         )
LINE 377 | 
LINE 378 |         return ProjectAnalysisResult(
LINE 379 |             folder_path=folder_path,
LINE 380 |             project_name=project_name,
LINE 381 |             primary_language=primary_lang,
LINE 382 |             language_summary=languages_stats,
LINE 383 |             framework=framework,
LINE 384 |             framework_details=framework_details,
LINE 385 |             package_manager=pkg_manager,
LINE 386 |             config_files=sorted(config_files),
LINE 387 |             entry_points=sorted(entry_points),
LINE 388 |             total_files=total_files,
LINE 389 |             total_lines=total_lines,
LINE 390 |             total_size_bytes=total_size,
LINE 391 |             extension_counts=dict(extension_counts),
LINE 392 |             extension_lines=dict(extension_lines),
LINE 393 |             manifest_dependencies=manifest_deps,
LINE 394 |             code_dependencies=code_dependencies,
LINE 395 |             important_files=sorted(important_files),
LINE 396 |             large_files=large_files,
LINE 397 |             recently_modified_files=recent_files,
LINE 398 |             project_structure_tree=structure_tree,
LINE 399 |             recommended_files=recommended_files,
LINE 400 |             excluded_dirs_found=sorted(list(excluded_dirs_found)),
LINE 401 |             configured_exclusions=sorted(list(self.excluded_dirs)),
LINE 402 |         )
LINE 403 | 
LINE 404 |     def _is_entry_point(self, rel_path: str) -> bool:
LINE 405 |         """Determines if relative path is an entry point."""
LINE 406 |         base = os.path.basename(rel_path).lower()
LINE 407 |         if base in KNOWN_ENTRY_POINTS:
LINE 408 |             parts = rel_path.split("/")
LINE 409 |             if len(parts) <= 3:
LINE 410 |                 return True
LINE 411 |         if rel_path in ("src/main.js", "src/main.ts", "src/index.js", "src/index.ts", "src/App.vue", "src/App.tsx"):
LINE 412 |             return True
LINE 413 |         if rel_path.endswith("artisan") or rel_path.endswith("public/index.php"):
LINE 414 |             return True
LINE 415 |         return False
LINE 416 | 
LINE 417 |     def _is_config_file(self, rel_path: str) -> bool:
LINE 418 |         """Determines if file is a configuration file."""
LINE 419 |         base = os.path.basename(rel_path).lower()
LINE 420 |         if base in KNOWN_CONFIG_FILES:
LINE 421 |             return True
LINE 422 |         if base.startswith(".env") or base.endswith(".config.js") or base.endswith(".config.ts"):
LINE 423 |             return True
LINE 424 |         return False
LINE 425 | 
LINE 426 |     def _is_important_file(self, rel_path: str, is_ep: bool, is_cfg: bool) -> bool:
LINE 427 |         """Identifies important architectural files (services, controllers, models, routes)."""
LINE 428 |         if is_ep or is_cfg:
LINE 429 |             return True
LINE 430 |         p_lower = rel_path.lower()
LINE 431 |         keywords = ("service", "controller", "model", "route", "router", "handler", "api", "repository")
LINE 432 |         for kw in keywords:
LINE 433 |             if kw in p_lower:
LINE 434 |                 return True
LINE 435 |         return False
LINE 436 | 
LINE 437 |     def _detect_package_manager_and_manifests(self, folder: str) -> Tuple[str, Dict[str, List[str]]]:
LINE 438 |         """Detects package manager and extracts declared dependencies from manifests."""
LINE 439 |         manifest_deps: Dict[str, List[str]] = {}
LINE 440 |         detected_managers = []
LINE 441 | 
LINE 442 |         # 1. Composer (PHP)
LINE 443 |         composer_json = os.path.join(folder, "composer.json")
LINE 444 |         if os.path.isfile(composer_json):
LINE 445 |             mgr = "Composer"
LINE 446 |             detected_managers.append(mgr)
LINE 447 |             try:
LINE 448 |                 with open(composer_json, "r", encoding="utf-8") as fp:
LINE 449 |                     data = json.load(fp)
LINE 450 |                 reqs = []
LINE 451 |                 for pkg, ver in data.get("require", {}).items():
LINE 452 |                     reqs.append(f"{pkg}: {ver}")
LINE 453 |                 for pkg, ver in data.get("require-dev", {}).items():
LINE 454 |                     reqs.append(f"{pkg} (dev): {ver}")
LINE 455 |                 if reqs:
LINE 456 |                     manifest_deps["composer.json"] = reqs
LINE 457 |             except Exception:
LINE 458 |                 pass
LINE 459 | 
LINE 460 |         # 2. Node / JS (npm, yarn, pnpm, bun)
LINE 461 |         pkg_json = os.path.join(folder, "package.json")
LINE 462 |         if os.path.isfile(pkg_json):
LINE 463 |             js_mgr = "npm"
LINE 464 |             if os.path.isfile(os.path.join(folder, "pnpm-lock.yaml")):
LINE 465 |                 js_mgr = "pnpm"
LINE 466 |             elif os.path.isfile(os.path.join(folder, "yarn.lock")):
LINE 467 |                 js_mgr = "Yarn"
LINE 468 |             elif os.path.isfile(os.path.join(folder, "bun.lockb")) or os.path.isfile(os.path.join(folder, "bun.lock")):
LINE 469 |                 js_mgr = "Bun"
LINE 470 |             detected_managers.append(js_mgr)
LINE 471 |             try:
LINE 472 |                 with open(pkg_json, "r", encoding="utf-8") as fp:
LINE 473 |                     data = json.load(fp)
LINE 474 |                 deps = []
LINE 475 |                 for pkg, ver in data.get("dependencies", {}).items():
LINE 476 |                     deps.append(f"{pkg}: {ver}")
LINE 477 |                 for pkg, ver in data.get("devDependencies", {}).items():
LINE 478 |                     deps.append(f"{pkg} (dev): {ver}")
LINE 479 |                 if deps:
LINE 480 |                     manifest_deps["package.json"] = deps
LINE 481 |             except Exception:
LINE 482 |                 pass
LINE 483 | 
LINE 484 |         # 3. Python (pip, poetry, pipenv, conda)
LINE 485 |         req_txt = os.path.join(folder, "requirements.txt")
LINE 486 |         if os.path.isfile(req_txt):
LINE 487 |             detected_managers.append("pip")
LINE 488 |             try:
LINE 489 |                 with open(req_txt, "r", encoding="utf-8") as fp:
LINE 490 |                     lines = [l.strip() for l in fp if l.strip() and not l.strip().startswith("#")]
LINE 491 |                 if lines:
LINE 492 |                     manifest_deps["requirements.txt"] = lines
LINE 493 |             except Exception:
LINE 494 |                 pass
LINE 495 | 
LINE 496 |         pyproject = os.path.join(folder, "pyproject.toml")
LINE 497 |         if os.path.isfile(pyproject):
LINE 498 |             if os.path.isfile(os.path.join(folder, "poetry.lock")):
LINE 499 |                 detected_managers.append("Poetry")
LINE 500 |             else:
LINE 501 |                 detected_managers.append("pip/pyproject.toml")
LINE 502 | 
LINE 503 |         pipfile = os.path.join(folder, "Pipfile")
LINE 504 |         if os.path.isfile(pipfile):
LINE 505 |             detected_managers.append("Pipenv")
LINE 506 | 
LINE 507 |         # 4. Rust (Cargo)
LINE 508 |         if os.path.isfile(os.path.join(folder, "Cargo.toml")):
LINE 509 |             detected_managers.append("Cargo")
LINE 510 | 
LINE 511 |         # 5. Go (Go Modules)
LINE 512 |         if os.path.isfile(os.path.join(folder, "go.mod")):
LINE 513 |             detected_managers.append("Go Modules")
LINE 514 | 
LINE 515 |         # 6. Java (Maven / Gradle)
LINE 516 |         if os.path.isfile(os.path.join(folder, "pom.xml")):
LINE 517 |             detected_managers.append("Maven")
LINE 518 |         elif os.path.isfile(os.path.join(folder, "build.gradle")) or os.path.isfile(os.path.join(folder, "build.gradle.kts")):
LINE 519 |             detected_managers.append("Gradle")
LINE 520 | 
LINE 521 |         primary_mgr = ", ".join(detected_managers) if detected_managers else "Ninguno detectado"
LINE 522 |         return primary_mgr, manifest_deps
LINE 523 | 
LINE 524 |     def _detect_framework(
LINE 525 |         self, folder: str, primary_lang: str, manifest_deps: Dict[str, List[str]], files: List[FileMetric]
LINE 526 |     ) -> Tuple[str, str]:
LINE 527 |         """Detects framework (Laravel, Quasar, Vue, React, FastAPI, Django, Tkinter, etc.)."""
LINE 528 |         # --- PHP / Laravel detection ---
LINE 529 |         if os.path.isfile(os.path.join(folder, "artisan")) or any("laravel/framework" in d for d in manifest_deps.get("composer.json", [])):
LINE 530 |             ver = "Laravel"
LINE 531 |             for d in manifest_deps.get("composer.json", []):
LINE 532 |                 if "laravel/framework" in d:
LINE 533 |                     ver = f"Laravel ({d.split(':')[-1].strip()})"
LINE 534 |                     break
LINE 535 |             return "Laravel", ver
LINE 536 | 
LINE 537 |         if any("symfony" in d.lower() for d in manifest_deps.get("composer.json", [])):
LINE 538 |             return "Symfony", "Framework PHP Symfony"
LINE 539 | 
LINE 540 |         # --- Quasar Framework detection ---
LINE 541 |         quasar_configs = [
LINE 542 |             os.path.isfile(os.path.join(folder, "quasar.config.js")),
LINE 543 |             os.path.isfile(os.path.join(folder, "quasar.config.ts")),
LINE 544 |             os.path.isfile(os.path.join(folder, "quasar.conf.js")),
LINE 545 |         ]
LINE 546 |         pkg_deps = " ".join(manifest_deps.get("package.json", [])).lower()
LINE 547 |         if any(quasar_configs) or "quasar" in pkg_deps or "@quasar/app" in pkg_deps:
LINE 548 |             return "Quasar Framework", "Vue.js + Quasar CLI"
LINE 549 | 
LINE 550 |         # --- Vue / React / Next / Nuxt / Angular / Nest / Express ---
LINE 551 |         if "next" in pkg_deps and "react" in pkg_deps:
LINE 552 |             return "Next.js", "React Framework"
LINE 553 |         if "nuxt" in pkg_deps:
LINE 554 |             return "Nuxt.js", "Vue.js Framework"
LINE 555 |         if "@nestjs/core" in pkg_deps:
LINE 556 |             return "NestJS", "Node.js Framework"
LINE 557 |         if "vue" in pkg_deps:
LINE 558 |             return "Vue.js", "Frontend Framework"
LINE 559 |         if "react" in pkg_deps:
LINE 560 |             return "React", "Frontend Library"
LINE 561 |         if "@angular/core" in pkg_deps:
LINE 562 |             return "Angular", "Frontend Framework"
LINE 563 |         if "express" in pkg_deps:
LINE 564 |             return "Express.js", "Node.js Backend"
LINE 565 | 
LINE 566 |         # --- Python frameworks ---
LINE 567 |         py_reqs = " ".join(manifest_deps.get("requirements.txt", [])).lower()
LINE 568 |         if "django" in py_reqs:
LINE 569 |             return "Django", "Web Framework"
LINE 570 |         if "fastapi" in py_reqs:
LINE 571 |             return "FastAPI", "Modern ASGI Web Framework"
LINE 572 |         if "flask" in py_reqs:
LINE 573 |             return "Flask", "Micro Web Framework"
LINE 574 |         if "streamlit" in py_reqs:
LINE 575 |             return "Streamlit", "Data App Framework"
LINE 576 | 
LINE 577 |         # Check Python imports across scanned files
LINE 578 |         has_tkinter = False
LINE 579 |         has_fastapi = False
LINE 580 |         has_flask = False
LINE 581 |         has_django = False
LINE 582 |         has_pyside = False
LINE 583 | 
LINE 584 |         scanned_py = 0
LINE 585 |         max_py_scan = 150
LINE 586 | 
LINE 587 |         for f in files:
LINE 588 |             if f.rel_path.endswith(".py"):
LINE 589 |                 if scanned_py >= max_py_scan:
LINE 590 |                     break
LINE 591 |                 scanned_py += 1
LINE 592 |                 try:
LINE 593 |                     with open(f.abs_path, "r", encoding="utf-8", errors="ignore") as fp:
LINE 594 |                         content = fp.read(4096)
LINE 595 |                         if "tkinter" in content:
LINE 596 |                             has_tkinter = True
LINE 597 |                         if "fastapi" in content:
LINE 598 |                             has_fastapi = True
LINE 599 |                         if "flask" in content:
LINE 600 |                             has_flask = True
LINE 601 |                         if "django" in content:
LINE 602 |                             has_django = True
LINE 603 |                         if "PyQt" in content or "PySide" in content:
LINE 604 |                             has_pyside = True
LINE 605 |                 except Exception:
LINE 606 |                     pass
LINE 607 | 
LINE 608 |         if has_fastapi:
LINE 609 |             return "FastAPI", "Python ASGI Framework"
LINE 610 |         if has_django:
LINE 611 |             return "Django", "Python Web Framework"
LINE 612 |         if has_flask:
LINE 613 |             return "Flask", "Python Web Framework"
LINE 614 |         if has_pyside:
LINE 615 |             return "PyQt / PySide", "Desktop GUI Framework"
LINE 616 |         if has_tkinter:
LINE 617 |             return "Tkinter", "Python Desktop GUI Standard"
LINE 618 | 
LINE 619 |         # Fallback based on primary language
LINE 620 |         if primary_lang in ("Python", "JavaScript", "TypeScript", "PHP"):
LINE 621 |             return "Estándar / Vanilla", f"Proyecto {primary_lang} modular"
LINE 622 | 
LINE 623 |         return "No detectado", ""
LINE 624 | 
LINE 625 |     def _scan_code_dependencies(self, files: List[FileMetric]) -> Dict[str, List[str]]:
LINE 626 |         """Scans code files using DependencyDetector for imports and dependencies."""
LINE 627 |         code_deps: Dict[str, List[str]] = {}
LINE 628 |         key_files = [f for f in files if f.is_entry_point or f.is_important][:50]
LINE 629 |         if not key_files:
LINE 630 |             key_files = files[:30]
LINE 631 | 
LINE 632 |         for f in key_files:
LINE 633 |             try:
LINE 634 |                 raw_text = safe_read_file(f.abs_path, max_bytes=100_000)
LINE 635 |                 deps = self.dep_detector.detect_file_dependencies(f.rel_path, raw_text)
LINE 636 |                 if deps:
LINE 637 |                     code_deps[f.rel_path] = deps
LINE 638 |             except Exception:
LINE 639 |                 pass
LINE 640 | 
LINE 641 |         return code_deps
LINE 642 | 
LINE 643 |     def _select_recommended_files(
LINE 644 |         self, files: List[FileMetric], entry_points: List[str], config_files: List[str], recent_files: List[Dict[str, Any]]
LINE 645 |     ) -> List[str]:
LINE 646 |         """
LINE 647 |         Smart heuristic algorithm that scores and pre-selects the most relevant files for context.
LINE 648 |         Prioritizes:
LINE 649 |         1. Entry points (main.py, artisan, src/main.js)
LINE 650 |         2. Key configuration and dependency manifests (requirements.txt, package.json, composer.json)
LINE 651 |         3. Core services, controllers, models, routes
LINE 652 |         4. Recently modified files
LINE 653 |         Excludes minified, lockfiles, heavy test files, binaries, or excluded directories.
LINE 654 |         """
LINE 655 |         recent_paths = {rf["path"] for rf in recent_files[:5]}
LINE 656 | 
LINE 657 |         for m in files:
LINE 658 |             score = 0
LINE 659 |             rel = m.rel_path.lower()
LINE 660 | 
LINE 661 |             if m.is_entry_point:
LINE 662 |                 score += 120
LINE 663 | 
LINE 664 |             if m.is_config:
LINE 665 |                 base = os.path.basename(rel)
LINE 666 |                 if base in ("requirements.txt", "package.json", "composer.json", "pyproject.toml", "quasar.config.js", "quasar.config.ts"):
LINE 667 |                     score += 100
LINE 668 |                 elif base.endswith("lock") or base.endswith("lock.json"):
LINE 669 |                     score -= 50
LINE 670 |                 else:
LINE 671 |                     score += 50
LINE 672 | 
LINE 673 |             if m.is_important:
LINE 674 |                 score += 80
LINE 675 | 
LINE 676 |             if rel.startswith("app/") or rel.startswith("src/") or rel.startswith("core/"):
LINE 677 |                 score += 40
LINE 678 | 
LINE 679 |             if m.rel_path in recent_paths:
LINE 680 |                 score += 35
LINE 681 | 
LINE 682 |             if m.size_bytes > 300 * 1024:
LINE 683 |                 score -= 40
LINE 684 |             if ".min." in rel or rel.endswith(".map"):
LINE 685 |                 score -= 100
LINE 686 |             if "test" in rel or "spec" in rel:
LINE 687 |                 score -= 20
LINE 688 | 
LINE 689 |             m.score = score
LINE 690 | 
LINE 691 |         sorted_files = sorted(files, key=lambda x: x.score, reverse=True)
LINE 692 | 
LINE 693 |         recommended = []
LINE 694 |         target_limit = min(max(len(sorted_files), 1), 25)
LINE 695 | 
LINE 696 |         for m in sorted_files:
LINE 697 |             if m.score > 0 or len(recommended) < 5:
LINE 698 |                 base = os.path.basename(m.rel_path).lower()
LINE 699 |                 if base.endswith(".lock") or base in ("package-lock.json", "yarn.lock", "composer.lock"):
LINE 700 |                     continue
LINE 701 |                 if ".min." in base:
LINE 702 |                     continue
LINE 703 |                 recommended.append(m.rel_path)
LINE 704 |             if len(recommended) >= target_limit:
LINE 705 |                 break
LINE 706 | 
LINE 707 |         # Always ensure entry points and primary manifests are in recommended
LINE 708 |         for ep in entry_points:
LINE 709 |             if ep not in recommended:
LINE 710 |                 recommended.insert(0, ep)
LINE 711 |         for cfg in config_files:
LINE 712 |             base = os.path.basename(cfg).lower()
LINE 713 |             if base in ("requirements.txt", "package.json", "composer.json") and cfg not in recommended:
LINE 714 |                 recommended.append(cfg)
LINE 715 | 
LINE 716 |         return sorted(list(dict.fromkeys(recommended)))
```

==============================================================
FILE: .backup/app/core/storage/database.py
==============================================================
```py
LINE   1 | """
LINE   2 | SQLite persistence layer for project nodes, metrics and dependencies (Phase 1).
LINE   3 | 
LINE   4 | This module is intentionally restricted to:
LINE   5 |   - Opening / creating the SQLite database.
LINE   6 |   - Initializing the schema.
LINE   7 |   - Executing queries and updates.
LINE   8 |   - Managing transactions.
LINE   9 |   - Providing the CRUD operations required for projects and nodes.
LINE  10 | 
LINE  11 | No Delta Scan or incremental change detection logic is implemented here.
LINE  12 | """
LINE  13 | import os
LINE  14 | import sqlite3
LINE  15 | from typing import Dict, List, Optional, Set, Tuple
LINE  16 | 
LINE  17 | 
LINE  18 | # ---------------------------------------------------------------------------
LINE  19 | # Path resolution
LINE  20 | # ---------------------------------------------------------------------------
LINE  21 | 
LINE  22 | def _find_project_root() -> Optional[str]:
LINE  23 |     """Walk up from this file to find the project root (contains main.py)."""
LINE  24 |     here = os.path.dirname(os.path.abspath(__file__))
LINE  25 |     candidate = os.path.abspath(os.path.join(here, "..", "..", ".."))
LINE  26 |     if os.path.isfile(os.path.join(candidate, "main.py")):
LINE  27 |         return candidate
LINE  28 |     return None
LINE  29 | 
LINE  30 | 
LINE  31 | def default_db_path() -> str:
LINE  32 |     """Resolve project_cache.db path.
LINE  33 | 
LINE  34 |     Prefer <project_root>/.cache/project_cache.db, fallback to
LINE  35 |     ~/.analyzer_app/project_cache.db when the project root cannot be resolved.
LINE  36 |     """
LINE  37 |     root = _find_project_root()
LINE  38 |     if root:
LINE  39 |         return os.path.join(root, ".cache", "project_cache.db")
LINE  40 |     home = os.path.expanduser("~")
LINE  41 |     return os.path.join(home, ".analyzer_app", "project_cache.db")
LINE  42 | 
LINE  43 | 
LINE  44 | # ---------------------------------------------------------------------------
LINE  45 | # Schema
LINE  46 | # ---------------------------------------------------------------------------
LINE  47 | 
LINE  48 | SCHEMA_STATEMENTS = [
LINE  49 |     """CREATE TABLE IF NOT EXISTS projects (
LINE  50 |         id INTEGER PRIMARY KEY AUTOINCREMENT,
LINE  51 |         path TEXT UNIQUE NOT NULL,
LINE  52 |         project_type TEXT,
LINE  53 |         framework TEXT,
LINE  54 |         last_scanned TIMESTAMP DEFAULT CURRENT_TIMESTAMP
LINE  55 |     )""",
LINE  56 |     """CREATE TABLE IF NOT EXISTS nodes (
LINE  57 |         id INTEGER PRIMARY KEY AUTOINCREMENT,
LINE  58 |         project_id INTEGER NOT NULL,
LINE  59 |         rel_path TEXT NOT NULL,
LINE  60 |         parent_path TEXT,
LINE  61 |         is_dir BOOLEAN NOT NULL,
LINE  62 |         mtime REAL NOT NULL,
LINE  63 |         lines_count INTEGER DEFAULT 0,
LINE  64 |         file_size INTEGER DEFAULT 0,
LINE  65 |         is_important BOOLEAN DEFAULT 0,
LINE  66 |         is_checked BOOLEAN DEFAULT 1,
LINE  67 |         FOREIGN KEY(project_id) REFERENCES projects(id) ON DELETE CASCADE,
LINE  68 |         UNIQUE(project_id, rel_path)
LINE  69 |     )""",
LINE  70 |     """CREATE TABLE IF NOT EXISTS node_dependencies (
LINE  71 |         id INTEGER PRIMARY KEY AUTOINCREMENT,
LINE  72 |         source_node_id INTEGER NOT NULL,
LINE  73 |         target_path TEXT NOT NULL,
LINE  74 |         FOREIGN KEY(source_node_id) REFERENCES nodes(id) ON DELETE CASCADE
LINE  75 |     )""",
LINE  76 |     "CREATE INDEX IF NOT EXISTS idx_nodes_rel_path ON nodes(project_id, rel_path)",
LINE  77 |     "CREATE INDEX IF NOT EXISTS idx_nodes_parent ON nodes(project_id, parent_path)",
LINE  78 | ]
LINE  79 | 
LINE  80 | 
LINE  81 | # ---------------------------------------------------------------------------
LINE  82 | # Database
LINE  83 | # ---------------------------------------------------------------------------
LINE  84 | 
LINE  85 | class Database:
LINE  86 |     """Thin SQLite wrapper for the project cache (Phase 1)."""
LINE  87 | 
LINE  88 |     def __init__(self, db_path: Optional[str] = None):
LINE  89 |         self.db_path = db_path or default_db_path()
LINE  90 |         os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
LINE  91 |         self._conn = sqlite3.connect(self.db_path, timeout=10.0)
LINE  92 |         self._conn.row_factory = sqlite3.Row
LINE  93 |         self._conn.execute("PRAGMA foreign_keys = ON")
LINE  94 |         self._conn.execute("PRAGMA journal_mode = WAL")
LINE  95 |         self._conn.execute("PRAGMA synchronous = NORMAL")
LINE  96 |         self._init_schema()
LINE  97 | 
LINE  98 |     def _init_schema(self) -> None:
LINE  99 |         with self._conn:
LINE 100 |             for stmt in SCHEMA_STATEMENTS:
LINE 101 |                 self._conn.execute(stmt)
LINE 102 | 
LINE 103 |     # ---------- projects ----------
LINE 104 | 
LINE 105 |     def get_or_create_project(self, path: str,
LINE 106 |                               project_type: Optional[str] = None,
LINE 107 |                               framework: Optional[str] = None) -> int:
LINE 108 |         cur = self._conn.cursor()
LINE 109 |         cur.execute("SELECT id FROM projects WHERE path = ?", (path,))
LINE 110 |         row = cur.fetchone()
LINE 111 |         if row:
LINE 112 |             return int(row["id"])
LINE 113 |         cur.execute(
LINE 114 |             "INSERT INTO projects (path, project_type, framework) VALUES (?, ?, ?)",
LINE 115 |             (path, project_type, framework),
LINE 116 |         )
LINE 117 |         self._conn.commit()
LINE 118 |         return int(cur.lastrowid)
LINE 119 | 
LINE 120 |     def get_project_by_path(self, path: str) -> Optional[Dict]:
LINE 121 |         cur = self._conn.cursor()
LINE 122 |         cur.execute("SELECT * FROM projects WHERE path = ?", (path,))
LINE 123 |         row = cur.fetchone()
LINE 124 |         return dict(row) if row else None
LINE 125 | 
LINE 126 |     def update_last_scanned(self, project_id: int) -> None:
LINE 127 |         with self._conn:
LINE 128 |             self._conn.execute(
LINE 129 |                 "UPDATE projects SET last_scanned = CURRENT_TIMESTAMP WHERE id = ?",
LINE 130 |                 (project_id,),
LINE 131 |             )
LINE 132 | 
LINE 133 |     def delete_project(self, path: str) -> None:
LINE 134 |         with self._conn:
LINE 135 |             self._conn.execute("DELETE FROM projects WHERE path = ?", (path,))
LINE 136 | 
LINE 137 |     # ---------- nodes ----------
LINE 138 | 
LINE 139 |     def replace_nodes(self, project_id: int, nodes: List[Dict]) -> None:
LINE 140 |         """Delete existing nodes for project and insert the new batch atomically."""
LINE 141 |         rows = [
LINE 142 |             (
LINE 143 |                 project_id,
LINE 144 |                 n["rel_path"],
LINE 145 |                 n.get("parent_path"),
LINE 146 |                 int(bool(n.get("is_dir", 0))),
LINE 147 |                 float(n.get("mtime", 0.0) or 0.0),
LINE 148 |                 int(n.get("lines_count", 0) or 0),
LINE 149 |                 int(n.get("file_size", 0) or 0),
LINE 150 |                 int(bool(n.get("is_important", 0))),
LINE 151 |                 int(bool(n.get("is_checked", 1))),
LINE 152 |             )
LINE 153 |             for n in nodes
LINE 154 |         ]
LINE 155 |         with self._conn:
LINE 156 |             self._conn.execute("DELETE FROM nodes WHERE project_id = ?", (project_id,))
LINE 157 |             if rows:
LINE 158 |                 self._conn.executemany(
LINE 159 |                     """INSERT INTO nodes
LINE 160 |                        (project_id, rel_path, parent_path, is_dir, mtime,
LINE 161 |                         lines_count, file_size, is_important, is_checked)
LINE 162 |                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
LINE 163 |                     rows,
LINE 164 |                 )
LINE 165 | 
LINE 166 |     def get_nodes(self, project_id: int) -> List[Dict]:
LINE 167 |         cur = self._conn.cursor()
LINE 168 |         cur.execute("SELECT * FROM nodes WHERE project_id = ?", (project_id,))
LINE 169 |         return [dict(r) for r in cur.fetchall()]
LINE 170 | 
LINE 171 |     def update_is_checked(self, project_id: int,
LINE 172 |                           rel_path: str, is_checked: bool) -> None:
LINE 173 |         with self._conn:
LINE 174 |             self._conn.execute(
LINE 175 |                 "UPDATE nodes SET is_checked = ? "
LINE 176 |                 "WHERE project_id = ? AND rel_path = ?",
LINE 177 |                 (int(bool(is_checked)), project_id, rel_path),
LINE 178 |             )
LINE 179 | 
LINE 180 |     def update_is_checked_batch(self, project_id: int,
LINE 181 |                                 updates: List[Tuple[str, bool]]) -> None:
LINE 182 |         rows = [(int(bool(c)), project_id, rp) for rp, c in updates]
LINE 183 |         if not rows:
LINE 184 |             return
LINE 185 |         with self._conn:
LINE 186 |             self._conn.executemany(
LINE 187 |                 "UPDATE nodes SET is_checked = ? "
LINE 188 |                 "WHERE project_id = ? AND rel_path = ?",
LINE 189 |                 rows,
LINE 190 |             )
LINE 191 | 
LINE 192 |     def load_checked_state(self, project_path: str) -> Optional[Set[str]]:
LINE 193 |         """Return the set of checked rel_paths (files only).
LINE 194 | 
LINE 195 |         Returns None when there is no persisted data for this project,
LINE 196 |         so the caller can distinguish "never saved" from "all unchecked".
LINE 197 |         """
LINE 198 |         cur = self._conn.cursor()
LINE 199 |         cur.execute("SELECT id FROM projects WHERE path = ?", (project_path,))
LINE 200 |         row = cur.fetchone()
LINE 201 |         if not row:
LINE 202 |             return None
LINE 203 |         project_id = int(row["id"])
LINE 204 |         cur.execute(
LINE 205 |             "SELECT rel_path, is_checked FROM nodes "
LINE 206 |             "WHERE project_id = ? AND is_dir = 0",
LINE 207 |             (project_id,),
LINE 208 |         )
LINE 209 |         rows = cur.fetchall()
LINE 210 |         if not rows:
LINE 211 |             return None
LINE 212 |         return {r["rel_path"] for r in rows if r["is_checked"]}
LINE 213 | 
LINE 214 |     def delete_nodes(self, project_id: int) -> None:
LINE 215 |         with self._conn:
LINE 216 |             self._conn.execute("DELETE FROM nodes WHERE project_id = ?", (project_id,))
LINE 217 | 
LINE 218 |     # ---------- dependencies ----------
LINE 219 | 
LINE 220 |     def save_dependencies_batch(self, project_id: int,
LINE 221 |                                 deps: List[Tuple[str, str]]) -> None:
LINE 222 |         """deps: list of (source_rel_path, target_path)."""
LINE 223 |         if not deps:
LINE 224 |             return
LINE 225 |         cur = self._conn.cursor()
LINE 226 |         cur.execute("SELECT id, rel_path FROM nodes WHERE project_id = ?", (project_id,))
LINE 227 |         id_map = {r["rel_path"]: int(r["id"]) for r in cur.fetchall()}
LINE 228 | 
LINE 229 |         rows = []
LINE 230 |         for src_rel, target in deps:
LINE 231 |             node_id = id_map.get(src_rel)
LINE 232 |             if node_id is None:
LINE 233 |                 continue
LINE 234 |             rows.append((node_id, target))
LINE 235 | 
LINE 236 |         with self._conn:
LINE 237 |             self._conn.execute(
LINE 238 |                 """DELETE FROM node_dependencies
LINE 239 |                    WHERE source_node_id IN
LINE 240 |                          (SELECT id FROM nodes WHERE project_id = ?)""",
LINE 241 |                 (project_id,),
LINE 242 |             )
LINE 243 |             if rows:
LINE 244 |                 self._conn.executemany(
LINE 245 |                     "INSERT INTO node_dependencies (source_node_id, target_path) "
LINE 246 |                     "VALUES (?, ?)",
LINE 247 |                     rows,
LINE 248 |                 )
LINE 249 | 
LINE 250 |     def get_dependencies(self, project_id: int) -> List[Dict]:
LINE 251 |         cur = self._conn.cursor()
LINE 252 |         cur.execute(
LINE 253 |             """SELECT n.rel_path AS source_path, d.target_path AS target_path
LINE 254 |                FROM node_dependencies d
LINE 255 |                JOIN nodes n ON n.id = d.source_node_id
LINE 256 |                WHERE n.project_id = ?""",
LINE 257 |             (project_id,),
LINE 258 |         )
LINE 259 |         return [dict(r) for r in cur.fetchall()]
LINE 260 | 
LINE 261 |     def close(self) -> None:
LINE 262 |         try:
LINE 263 |             self._conn.close()
LINE 264 |         except Exception:
LINE 265 |             pass
LINE 266 | 
LINE 267 | 
LINE 268 | # ---------------------------------------------------------------------------
LINE 269 | # Singleton accessor
LINE 270 | # ---------------------------------------------------------------------------
LINE 271 | 
LINE 272 | _db_singleton: Optional[Database] = None
LINE 273 | 
LINE 274 | 
LINE 275 | def get_database(db_path: Optional[str] = None) -> Database:
LINE 276 |     """Return the process-wide Database singleton."""
LINE 277 |     global _db_singleton
LINE 278 |     if _db_singleton is None or (db_path and db_path != _db_singleton.db_path):
LINE 279 |         _db_singleton = Database(db_path)
LINE 280 |     return _db_singleton
LINE 281 | 
LINE 282 | 
LINE 283 | def reset_database_singleton() -> None:
LINE 284 |     """For tests: close and drop the current singleton."""
LINE 285 |     global _db_singleton
LINE 286 |     if _db_singleton is not None:
LINE 287 |         _db_singleton.close()
LINE 288 |     _db_singleton = None
```

==============================================================
FILE: .backup/app/gui/file_tree.py
==============================================================
```py
LINE   1 | """CheckboxTreeview component for selecting folder files."""
LINE   2 | import tkinter as tk
LINE   3 | from tkinter import ttk
LINE   4 | from typing import Set, List
LINE   5 | 
LINE   6 | 
LINE   7 | class CheckboxTreeview(ttk.Treeview):
LINE   8 |     def __init__(self, master, **kwargs):
LINE   9 |         super().__init__(master, columns=("check", "name"), show="tree headings", **kwargs)
LINE  10 |         self.heading("#0", text="", anchor="w")
LINE  11 |         self.heading("check", text="☑", anchor="center", command=self.toggle_all_header)
LINE  12 |         self.heading("name", text="Archivo / Carpeta", anchor="w")
LINE  13 |         self.column("#0", width=35, stretch=False)
LINE  14 |         self.column("check", width=40, stretch=False, anchor="center")
LINE  15 |         self.column("name", width=260, stretch=True)
LINE  16 |         
LINE  17 |         self.tag_configure("checked", foreground="#1b5e20")
LINE  18 |         self.tag_configure("unchecked", foreground="#757575")
LINE  19 |         self.bind("<Button-1>", self.on_click)
LINE  20 |         self.checked_items: Set[str] = set()
LINE  21 |         # === PERSISTENCE: PHASE1 (attrs) ===
LINE  22 |         self._on_check_change = None
LINE  23 |         # === END PERSISTENCE: PHASE1 (attrs) ===
LINE  24 | 
LINE  25 | 
LINE  26 |     # === PERSISTENCE: PHASE1 (methods) ===
LINE  27 |     def set_check_change_callback(self, callback) -> None:
LINE  28 |         """Register callback(rel_path: str, is_checked: bool) for persistence."""
LINE  29 |         self._on_check_change = callback
LINE  30 | 
LINE  31 |     def _notify_check_change(self, rel_path: str, is_checked: bool) -> None:
LINE  32 |         if not self._on_check_change or not rel_path:
LINE  33 |             return
LINE  34 |         try:
LINE  35 |             self._on_check_change(rel_path, is_checked)
LINE  36 |         except Exception:
LINE  37 |             pass
LINE  38 |     # === END PERSISTENCE: PHASE1 (methods) ===
LINE  39 | 
LINE  40 |     def insert_file(self, parent, rel_path: str, is_checked: bool = True):
LINE  41 |         item = self.insert(parent, "end", text="📄", values=("☑" if is_checked else "☐", rel_path), tags=("checked" if is_checked else "unchecked",))
LINE  42 |         if is_checked:
LINE  43 |             self.checked_items.add(rel_path)
LINE  44 |         return item
LINE  45 | 
LINE  46 |     def insert_folder(self, parent, rel_path: str):
LINE  47 |         return self.insert(parent, "end", text="📁", values=("", rel_path), open=True)
LINE  48 | 
LINE  49 |     def check_item(self, item):
LINE  50 |         rel_path = self.set(item, "name")
LINE  51 |         if rel_path:
LINE  52 |             was_checked = rel_path in self.checked_items
LINE  53 |             self.set(item, "check", "☑")
LINE  54 |             self.item(item, tags=("checked",))
LINE  55 |             if not self.get_children(item):
LINE  56 |                 self.checked_items.add(rel_path)
LINE  57 |                 if not was_checked:
LINE  58 |                     self._notify_check_change(rel_path, True)
LINE  59 |         for child in self.get_children(item):
LINE  60 |             self.check_item(child)
LINE  61 | 
LINE  62 |     def uncheck_item(self, item):
LINE  63 |         rel_path = self.set(item, "name")
LINE  64 |         if rel_path:
LINE  65 |             self.set(item, "check", "☐")
LINE  66 |             self.item(item, tags=("unchecked",))
LINE  67 |             if rel_path in self.checked_items:
LINE  68 |                 self.checked_items.remove(rel_path)
LINE  69 |         for child in self.get_children(item):
LINE  70 |             self.uncheck_item(child)
LINE  71 | 
LINE  72 |     def toggle_item(self, item):
LINE  73 |         check_val = self.set(item, "check")
LINE  74 |         if check_val == "☑":
LINE  75 |             self.uncheck_item(item)
LINE  76 |         else:
LINE  77 |             self.check_item(item)
LINE  78 | 
LINE  79 |     def toggle_all_header(self):
LINE  80 |         all_children = self.get_children()
LINE  81 |         if not all_children:
LINE  82 |             return
LINE  83 |         all_checked = all(self.set(child, "check") == "☑" for child in all_children if self.set(child, "check") != "")
LINE  84 |         for child in all_children:
LINE  85 |             if all_checked:
LINE  86 |                 self.uncheck_item(child)
LINE  87 |             else:
LINE  88 |                 self.check_item(child)
LINE  89 | 
LINE  90 |     def on_click(self, event):
LINE  91 |         region = self.identify_region(event.x, event.y)
LINE  92 |         item = self.identify_row(event.y)
LINE  93 |         if not item:
LINE  94 |             return
LINE  95 |         column = self.identify_column(event.x)
LINE  96 |         if region == "cell" and column == "#2":
LINE  97 |             self.toggle_item(item)
LINE  98 |         elif region == "tree":
LINE  99 |             self.toggle_item(item)
LINE 100 | 
LINE 101 |     def select_all(self):
LINE 102 |         for item in self.get_children():
LINE 103 |             self.check_item(item)
LINE 104 | 
LINE 105 |     def deselect_all(self):
LINE 106 |         for item in self.get_children():
LINE 107 |             self.uncheck_item(item)
LINE 108 | 
LINE 109 |     def get_checked_files(self) -> List[str]:
LINE 110 |         return list(self.checked_items)
LINE 111 | 
LINE 112 |     def set_checked_files(self, target_rel_paths: Set[str]):
LINE 113 |         """Sets checked items to exactly match target_rel_paths."""
LINE 114 |         self.checked_items.clear()
LINE 115 |         normalized_targets = {p.replace("\\", "/") for p in target_rel_paths}
LINE 116 | 
LINE 117 |         def traverse(item):
LINE 118 |             children = self.get_children(item)
LINE 119 |             if children:
LINE 120 |                 any_child_checked = False
LINE 121 |                 all_children_checked = True
LINE 122 |                 for child in children:
LINE 123 |                     child_checked = traverse(child)
LINE 124 |                     if child_checked:
LINE 125 |                         any_child_checked = True
LINE 126 |                     else:
LINE 127 |                         all_children_checked = False
LINE 128 |                 if any_child_checked:
LINE 129 |                     self.set(item, "check", "☑")
LINE 130 |                     self.item(item, tags=("checked",))
LINE 131 |                 else:
LINE 132 |                     self.set(item, "check", "☐")
LINE 133 |                     self.item(item, tags=("unchecked",))
LINE 134 |                 return any_child_checked
LINE 135 |             else:
LINE 136 |                 rel_path = self.set(item, "name")
LINE 137 |                 norm_rel = rel_path.replace("\\", "/") if rel_path else ""
LINE 138 |                 if norm_rel and norm_rel in normalized_targets:
LINE 139 |                     self.set(item, "check", "☑")
LINE 140 |                     self.item(item, tags=("checked",))
LINE 141 |                     self.checked_items.add(rel_path)
LINE 142 |                     return True
LINE 143 |                 else:
LINE 144 |                     self.set(item, "check", "☐")
LINE 145 |                     self.item(item, tags=("unchecked",))
LINE 146 |                     return False
LINE 147 | 
LINE 148 |         for root_item in self.get_children():
LINE 149 |             traverse(root_item)
```

==============================================================
FILE: .backup/app/gui/main_window.py
==============================================================
```py
LINE    1 | """Main Tkinter window – redesigned layout with left tree, right problem pane, and full bottom stats bar."""
LINE    2 | import os
LINE    3 | import sys
LINE    4 | import subprocess
LINE    5 | import tkinter as tk
LINE    6 | from tkinter import ttk, scrolledtext
LINE    7 | from typing import List, Set
LINE    8 | 
LINE    9 | from app.models.project import ExportConfig, DEFAULT_ALLOWED_EXTENSIONS
LINE   10 | from app.models.analysis_types import (
LINE   11 |     ANALYSIS_PROFILES, get_analysis_profile, get_all_analysis_types
LINE   12 | )
LINE   13 | from app.models.analysis_modes import (
LINE   14 |     ANALYSIS_MODES, get_analysis_mode_config, MODE_PROBLEM, MODE_PROJECT
LINE   15 | )
LINE   16 | from app.core.file_selector import FileSelectorManager
LINE   17 | from app.generators.prompt_generator import PromptGenerator
LINE   18 | from app.generators.markdown_generator import generate_markdown_bundle
LINE   19 | from app.generators.text_generator import generate_text_bundle
LINE   20 | from app.generators.standalone_prompt_generator import generate_standalone_prompt
LINE   21 | from app.gui.file_tree import CheckboxTreeview
LINE   22 | from app.gui.analysis_dialog import ProjectAnalysisDialog
LINE   23 | from app.core.project_analyzer import ProjectAnalyzer
LINE   24 | from app.core.intelligent_context import IntelligentContextAnalyzer
LINE   25 | from app.gui.intelligent_context_dialog import IntelligentContextDialog
LINE   26 | from app.gui import dialogs
LINE   27 | # === AUTO-GENERATED: file_search_dependency_feature ===
LINE   28 | from app.gui.file_search_dialog import FileSearchDialog
LINE   29 | from app.gui.dependency_tree_dialog import DependencyTreeDialog
LINE   30 | # === END AUTO-GENERATED ===
LINE   31 | # === PERSISTENCE: PHASE1 (imports) ===
LINE   32 | from app.core.storage.database import get_database
LINE   33 | # === END PERSISTENCE: PHASE1 (imports) ===
LINE   34 | 
LINE   35 | 
LINE   36 | 
LINE   37 | from app.utils.file_utils import (
LINE   38 |     copy_to_clipboard, write_text_file, KNOWN_BINARY_EXTENSIONS,
LINE   39 |     is_binary_file, get_file_size,
LINE   40 | )
LINE   41 | 
LINE   42 | # ─── Colour palette ─────────────────────────────────────────────────────────
LINE   43 | C_BG        = "#1e2330"   # main background
LINE   44 | C_PANEL     = "#252b3b"   # panel background
LINE   45 | C_BORDER    = "#323a50"   # separator / border
LINE   46 | C_ACCENT    = "#4f8ef7"   # primary accent (blue)
LINE   47 | C_ACCENT_DK = "#3a6fcc"   # accent hover
LINE   48 | C_SUCCESS   = "#3ecf8e"   # green
LINE   49 | C_WARN      = "#f5a623"   # amber
LINE   50 | C_TEXT      = "#e8eaf0"   # primary text
LINE   51 | C_TEXT2     = "#8b92a8"   # secondary / muted
LINE   52 | C_ENTRY     = "#2a3148"   # entry bg
LINE   53 | C_TREE_SEL  = "#2f3d5c"   # tree selection highlight
LINE   54 | C_STAT_BG   = "#161b28"   # bottom bar bg
LINE   55 | # ────────────────────────────────────────────────────────────────────────────
LINE   56 | 
LINE   57 | 
LINE   58 | class MainWindow:
LINE   59 |     def __init__(self, root: tk.Tk):
LINE   60 |         self.root = root
LINE   61 |         self.root.title("DeepSeek Code Packager")
LINE   62 |         self.root.geometry("1340x860")
LINE   63 |         self.root.minsize(1100, 700)
LINE   64 |         self.root.configure(bg=C_BG)
LINE   65 | 
LINE   66 |         # ── State ──────────────────────────────────────────────────────────
LINE   67 |         self.selector   = FileSelectorManager()
LINE   68 |         self.config     = ExportConfig()
LINE   69 |         # === PERSISTENCE: PHASE1 (init) ===
LINE   70 |         self._persist_db = None
LINE   71 |         try:
LINE   72 |             self._persist_db = get_database()
LINE   73 |         except Exception:
LINE   74 |             self._persist_db = None
LINE   75 |         # === END PERSISTENCE: PHASE1 (init) ===
LINE   76 | 
LINE   77 | 
LINE   78 |         default_excl    = ".git, node_modules, __pycache__, venv, .venv, dist, build, .idea, .vscode, vendor, .quasar, .github, public"
LINE   79 |         default_exts    = ", ".join(sorted(DEFAULT_ALLOWED_EXTENSIONS))
LINE   80 | 
LINE   81 |         self.var_folder   = tk.StringVar()
LINE   82 |         self.var_excl     = tk.StringVar(value=default_excl)
LINE   83 |         self.var_exts     = tk.StringVar(value=default_exts)
LINE   84 |         self.var_filter   = tk.BooleanVar(value=True)
LINE   85 |         self.var_lineno   = tk.BooleanVar(value=True)
LINE   86 |         self.var_tree     = tk.BooleanVar(value=True)
LINE   87 |         self.var_instruct = tk.BooleanVar(value=True)
LINE   88 |         self.var_max_file = tk.DoubleVar(value=2.0)
LINE   89 |         self.var_max_tot  = tk.DoubleVar(value=50.0)
LINE   90 |         self.var_max_n    = tk.IntVar(value=100)
LINE   91 |         self.var_fmt      = tk.StringVar(value="markdown")
LINE   92 |         self.var_analysis_type = tk.StringVar(value="Detect errors")
LINE   93 |         self.var_analysis_mode = tk.StringVar(value=MODE_PROBLEM)
LINE   94 | 
LINE   95 |         # Bottom stats vars
LINE   96 |         self.sv_folder    = tk.StringVar(value="0")
LINE   97 |         self.sv_sel_files = tk.StringVar(value="0")
LINE   98 |         self.sv_included  = tk.StringVar(value="0")
LINE   99 |         self.sv_excluded  = tk.StringVar(value="0")
LINE  100 |         self.sv_size      = tk.StringVar(value="0.00 MB")
LINE  101 |         self.sv_lines     = tk.StringVar(value="0")
LINE  102 |         self.sv_status    = tk.StringVar(value="Listo.")
LINE  103 | 
LINE  104 |         self._setup_styles()
LINE  105 |         self._build_header()
LINE  106 |         self._build_main()
LINE  107 |         self._build_bottom()
LINE  108 | 
LINE  109 |     # ── Style helpers ─────────────────────────────────────────────────────
LINE  110 |     def _setup_styles(self):
LINE  111 |         s = ttk.Style()
LINE  112 |         s.theme_use("clam")
LINE  113 | 
LINE  114 |         common = {"background": C_BG, "foreground": C_TEXT, "fieldbackground": C_ENTRY,
LINE  115 |                   "bordercolor": C_BORDER, "lightcolor": C_BORDER, "darkcolor": C_BORDER,
LINE  116 |                   "troughcolor": C_PANEL, "selectbackground": C_TREE_SEL,
LINE  117 |                   "selectforeground": C_TEXT}
LINE  118 | 
LINE  119 |         s.configure(".",                font=("Segoe UI", 9), **common)
LINE  120 |         s.configure("TFrame",           background=C_BG)
LINE  121 |         s.configure("TLabel",           background=C_BG, foreground=C_TEXT)
LINE  122 |         s.configure("TEntry",           fieldbackground=C_ENTRY, foreground=C_TEXT,
LINE  123 |                     insertcolor=C_TEXT, bordercolor=C_BORDER)
LINE  124 |         s.configure("TCheckbutton",     background=C_BG, foreground=C_TEXT2)
LINE  125 |         s.configure("TRadiobutton",     background=C_BG, foreground=C_TEXT2)
LINE  126 |         s.configure("Vertical.TScrollbar",   background=C_BORDER, troughcolor=C_PANEL)
LINE  127 |         s.configure("Horizontal.TScrollbar", background=C_BORDER, troughcolor=C_PANEL)
LINE  128 |         s.configure("TSeparator",       background=C_BORDER)
LINE  129 |         s.configure("TPanedwindow",     background=C_BORDER)
LINE  130 |         s.configure("TSpinbox",         fieldbackground=C_ENTRY, foreground=C_TEXT,
LINE  131 |                     insertcolor=C_TEXT, bordercolor=C_BORDER, arrowcolor=C_TEXT2)
LINE  132 | 
LINE  133 |         # Panel labels
LINE  134 |         s.configure("Panel.TFrame",     background=C_PANEL)
LINE  135 |         s.configure("Panel.TLabel",     background=C_PANEL, foreground=C_TEXT)
LINE  136 |         s.configure("Muted.TLabel",     background=C_PANEL, foreground=C_TEXT2,
LINE  137 |                     font=("Segoe UI", 8))
LINE  138 |         s.configure("Title.TLabel",     background=C_BG, foreground=C_TEXT,
LINE  139 |                     font=("Segoe UI", 15, "bold"))
LINE  140 |         s.configure("Sub.TLabel",       background=C_BG, foreground=C_TEXT2,
LINE  141 |                     font=("Segoe UI", 9))
LINE  142 |         s.configure("Sec.TLabel",       background=C_PANEL, foreground=C_ACCENT,
LINE  143 |                     font=("Segoe UI", 9, "bold"))
LINE  144 |         s.configure("StatKey.TLabel",   background=C_STAT_BG, foreground=C_TEXT2,
LINE  145 |                     font=("Segoe UI", 8))
LINE  146 |         s.configure("StatVal.TLabel",   background=C_STAT_BG, foreground=C_TEXT,
LINE  147 |                     font=("Segoe UI", 10, "bold"))
LINE  148 |         s.configure("Status.TLabel",    background=C_STAT_BG, foreground=C_TEXT2,
LINE  149 |                     font=("Segoe UI", 8, "italic"))
LINE  150 | 
LINE  151 |         # Treeview
LINE  152 |         s.configure("Treeview",         background=C_PANEL, foreground=C_TEXT,
LINE  153 |                     fieldbackground=C_PANEL, bordercolor=C_BORDER, rowheight=22)
LINE  154 |         s.configure("Treeview.Heading", background=C_BORDER, foreground=C_TEXT2,
LINE  155 |                     relief="flat", font=("Segoe UI", 8, "bold"))
LINE  156 |         s.map("Treeview",               background=[("selected", C_TREE_SEL)],
LINE  157 |                                         foreground=[("selected", C_TEXT)])
LINE  158 |         s.map("Treeview.Heading",       background=[("active", C_BORDER)])
LINE  159 | 
LINE  160 |         # Buttons
LINE  161 |         for name, bg, hover in [
LINE  162 |             ("Accent.TButton",  C_ACCENT,   C_ACCENT_DK),
LINE  163 |             ("Success.TButton", C_SUCCESS,  "#2faa75"),
LINE  164 |             ("Neutral.TButton", C_BORDER,   "#404860"),
LINE  165 |             ("Warn.TButton",    C_WARN,     "#cc8b1a"),
LINE  166 |         ]:
LINE  167 |             s.configure(name, background=bg, foreground=C_BG if name != "Neutral.TButton" else C_TEXT,
LINE  168 |                         relief="flat", font=("Segoe UI", 9, "bold"), padding=(10, 5))
LINE  169 |             s.map(name, background=[("active", hover)])
LINE  170 | 
LINE  171 |     # ── Header ────────────────────────────────────────────────────────────
LINE  172 |     def _build_header(self):
LINE  173 |         bar = ttk.Frame(self.root, padding=(16, 10, 16, 8))
LINE  174 |         bar.pack(fill=tk.X)
LINE  175 | 
LINE  176 |         ttk.Label(bar, text="📦  DeepSeek Code Packager", style="Title.TLabel").pack(side=tk.LEFT)
LINE  177 | 
LINE  178 |         right = ttk.Frame(bar)
LINE  179 |         right.pack(side=tk.RIGHT)
LINE  180 |         ttk.Label(right,
LINE  181 |                   text="Sin API · Sin conexión · Proyectos grandes seguros",
LINE  182 |                   style="Sub.TLabel").pack(anchor="e")
LINE  183 | 
LINE  184 |         ttk.Separator(self.root).pack(fill=tk.X)
LINE  185 | 
LINE  186 |     # ── Main 3-pane layout ────────────────────────────────────────────────
LINE  187 |     def _build_main(self):
LINE  188 |         paned = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
LINE  189 |         paned.pack(fill=tk.BOTH, expand=True, padx=8, pady=6)
LINE  190 | 
LINE  191 |         self._build_left(paned)
LINE  192 |         self._build_right(paned)
LINE  193 | 
LINE  194 |     # ──────────────────────────────────────────────────────────────────────
LINE  195 |     # LEFT pane  –  project tree
LINE  196 |     # ──────────────────────────────────────────────────────────────────────
LINE  197 |     def _build_left(self, paned):
LINE  198 |         left = ttk.Frame(paned, style="Panel.TFrame", padding=0)
LINE  199 |         paned.add(left, weight=2)
LINE  200 | 
LINE  201 |         # ── Folder row
LINE  202 |         folder_bar = ttk.Frame(left, style="Panel.TFrame", padding=(8, 6))
LINE  203 |         folder_bar.pack(fill=tk.X)
LINE  204 | 
LINE  205 |         ttk.Label(folder_bar, text="📂  Carpeta del proyecto", style="Sec.TLabel").pack(anchor="w")
LINE  206 | 
LINE  207 |         fe = ttk.Frame(folder_bar, style="Panel.TFrame")
LINE  208 |         fe.pack(fill=tk.X, pady=(4, 0))
LINE  209 | 
LINE  210 |         self.folder_entry = ttk.Entry(fe, textvariable=self.var_folder, state="readonly")
LINE  211 |         self.folder_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 4))
LINE  212 | 
LINE  213 |         ttk.Button(fe, text="📂 Seleccionar carpeta",
LINE  214 |                    style="Accent.TButton",
LINE  215 |                    command=self.on_select_folder).pack(side=tk.LEFT, padx=(0, 3))
LINE  216 |         ttk.Button(fe, text="🔬 Analizar",
LINE  217 |                    style="Accent.TButton",
LINE  218 |                    command=self.on_analyze_project).pack(side=tk.LEFT, padx=(0, 3))
LINE  219 |         ttk.Button(fe, text="✖",
LINE  220 |                    style="Neutral.TButton",
LINE  221 |                    command=self.on_remove_folder, width=3).pack(side=tk.LEFT)
LINE  222 | 
LINE  223 |         ttk.Separator(left).pack(fill=tk.X, pady=4)
LINE  224 | 
LINE  225 |         # ── Filters row (collapsed / compact)
LINE  226 |         flt = ttk.Frame(left, style="Panel.TFrame", padding=(8, 0))
LINE  227 |         flt.pack(fill=tk.X)
LINE  228 | 
LINE  229 |         fl1 = ttk.Frame(flt, style="Panel.TFrame")
LINE  230 |         fl1.pack(fill=tk.X, pady=2)
LINE  231 |         ttk.Label(fl1, text="Excluir carpetas:", style="Muted.TLabel").pack(side=tk.LEFT, padx=(0, 4))
LINE  232 |         ex = ttk.Entry(fl1, textvariable=self.var_excl, font=("Consolas", 8))
LINE  233 |         ex.pack(side=tk.LEFT, fill=tk.X, expand=True)
LINE  234 |         ex.bind("<FocusOut>", lambda _: self.reload_tree())
LINE  235 | 
LINE  236 |         fl2 = ttk.Frame(flt, style="Panel.TFrame")
LINE  237 |         fl2.pack(fill=tk.X, pady=2)
LINE  238 |         ttk.Checkbutton(fl2, text="Filtrar extensiones:", variable=self.var_filter,
LINE  239 |                         command=self.reload_tree, style="TCheckbutton").pack(side=tk.LEFT, padx=(0, 4))
LINE  240 |         ext_e = ttk.Entry(fl2, textvariable=self.var_exts, font=("Consolas", 8))
LINE  241 |         ext_e.pack(side=tk.LEFT, fill=tk.X, expand=True)
LINE  242 |         ext_e.bind("<FocusOut>", lambda _: self.reload_tree())
LINE  243 | 
LINE  244 |         ttk.Separator(left).pack(fill=tk.X, pady=4)
LINE  245 | 
LINE  246 |         # ── Tree toolbar
LINE  247 |         tb = ttk.Frame(left, style="Panel.TFrame", padding=(8, 0, 8, 4))
LINE  248 |         tb.pack(fill=tk.X)
LINE  249 |         ttk.Button(tb, text="☑ Todos", style="Neutral.TButton",
LINE  250 |                    command=self.on_select_all_tree).pack(side=tk.LEFT, padx=(0, 4))
LINE  251 |         ttk.Button(tb, text="☐ Ninguno", style="Neutral.TButton",
LINE  252 |                    command=self.on_deselect_all_tree).pack(side=tk.LEFT, padx=(0, 4))
LINE  253 |         ttk.Button(tb, text="🔬 Analizar proyecto", style="Accent.TButton",
LINE  254 |                    command=self.on_analyze_project).pack(side=tk.LEFT, padx=(0, 4))
LINE  255 |         ttk.Button(tb, text="🧠 Selección Inteligente", style="Accent.TButton",
LINE  256 |                    command=self.on_intelligent_context_select).pack(side=tk.LEFT, padx=(0, 4))
LINE  257 |         ttk.Button(tb, text="🔎 Buscador", style="Accent.TButton",
LINE  258 |                    command=self.on_open_file_search).pack(side=tk.LEFT, padx=(0, 4))
LINE  259 |         ttk.Button(tb, text="🔄 Recargar", style="Neutral.TButton",
LINE  260 |                    command=self.reload_tree).pack(side=tk.RIGHT)
LINE  261 | 
LINE  262 |         # ── Tree widget
LINE  263 |         tc = ttk.Frame(left, style="Panel.TFrame", padding=(4, 0, 4, 4))
LINE  264 |         tc.pack(fill=tk.BOTH, expand=True)
LINE  265 | 
LINE  266 |         self.tree = CheckboxTreeview(tc)
LINE  267 |         sy = ttk.Scrollbar(tc, orient=tk.VERTICAL,   command=self.tree.yview)
LINE  268 |         sx = ttk.Scrollbar(tc, orient=tk.HORIZONTAL, command=self.tree.xview)
LINE  269 |         self.tree.configure(yscrollcommand=sy.set, xscrollcommand=sx.set)
LINE  270 |         sy.pack(side=tk.RIGHT, fill=tk.Y)
LINE  271 |         sx.pack(side=tk.BOTTOM, fill=tk.X)
LINE  272 |         self.tree.pack(fill=tk.BOTH, expand=True)
LINE  273 |         self.tree.bind("<<TreeviewSelect>>", lambda _: self._refresh_selection_stats())
LINE  274 |         self.tree.bind("<ButtonRelease-1>",  lambda _: self.root.after(50, self._refresh_selection_stats))
LINE  275 |         # === PERSISTENCE: PHASE1 (callback) ===
LINE  276 |         if self._persist_db is not None:
LINE  277 |             self.tree.set_check_change_callback(self._on_tree_check_change)
LINE  278 |         # === END PERSISTENCE: PHASE1 (callback) ===
LINE  279 | 
LINE  280 | 
LINE  281 |         ttk.Separator(left).pack(fill=tk.X, pady=4)
LINE  282 | 
LINE  283 |         # ── Individual files list
LINE  284 |         il = ttk.Frame(left, style="Panel.TFrame", padding=(8, 0))
LINE  285 |         il.pack(fill=tk.X)
LINE  286 | 
LINE  287 |         ttk.Label(il, text="📄  Archivos individuales adicionales", style="Sec.TLabel").pack(anchor="w")
LINE  288 | 
LINE  289 |         il_tb = ttk.Frame(il, style="Panel.TFrame")
LINE  290 |         il_tb.pack(fill=tk.X, pady=(4, 3))
LINE  291 |         ttk.Button(il_tb, text="➕ Agregar archivos",
LINE  292 |                    style="Neutral.TButton",
LINE  293 |                    command=self.on_add_individual_files).pack(side=tk.LEFT, padx=(0, 4))
LINE  294 |         ttk.Button(il_tb, text="🗑 Quitar",
LINE  295 |                    style="Neutral.TButton",
LINE  296 |                    command=self.on_remove_individual_file).pack(side=tk.LEFT, padx=(0, 4))
LINE  297 |         ttk.Button(il_tb, text="🧹 Limpiar",
LINE  298 |                    style="Neutral.TButton",
LINE  299 |                    command=self.on_clear_individual_files).pack(side=tk.RIGHT)
LINE  300 | 
LINE  301 |         lc = ttk.Frame(il, style="Panel.TFrame", padding=(0, 0, 0, 6))
LINE  302 |         lc.pack(fill=tk.X)
LINE  303 |         self.file_listbox = tk.Listbox(
LINE  304 |             lc, height=4, selectmode=tk.SINGLE,
LINE  305 |             font=("Consolas", 8),
LINE  306 |             bg=C_ENTRY, fg=C_TEXT,
LINE  307 |             selectbackground=C_TREE_SEL, selectforeground=C_TEXT,
LINE  308 |             relief="flat", bd=0, highlightthickness=0,
LINE  309 |         )
LINE  310 |         ls = ttk.Scrollbar(lc, orient=tk.VERTICAL, command=self.file_listbox.yview)
LINE  311 |         self.file_listbox.configure(yscrollcommand=ls.set)
LINE  312 |         ls.pack(side=tk.RIGHT, fill=tk.Y)
LINE  313 |         self.file_listbox.pack(fill=tk.X, expand=True)
LINE  314 | 
LINE  315 |     # ──────────────────────────────────────────────────────────────────────
LINE  316 |     # RIGHT pane  –  problem description + settings + preview
LINE  317 |     # ──────────────────────────────────────────────────────────────────────
LINE  318 |     def _build_right(self, paned):
LINE  319 |         right = ttk.Frame(paned, style="Panel.TFrame", padding=0)
LINE  320 |         paned.add(right, weight=3)
LINE  321 | 
LINE  322 |         # ── Analysis Type selector (top of right pane)
LINE  323 |         type_hdr = ttk.Frame(right, style="Panel.TFrame", padding=(10, 8, 10, 2))
LINE  324 |         type_hdr.pack(fill=tk.X)
LINE  325 | 
LINE  326 |         t_row = ttk.Frame(type_hdr, style="Panel.TFrame")
LINE  327 |         t_row.pack(fill=tk.X)
LINE  328 | 
LINE  329 |         ttk.Label(t_row, text="🎯  Tipo de análisis:", style="Sec.TLabel").pack(side=tk.LEFT, padx=(0, 6))
LINE  330 | 
LINE  331 |         self.cb_analysis_type = ttk.Combobox(
LINE  332 |             t_row,
LINE  333 |             textvariable=self.var_analysis_type,
LINE  334 |             values=get_all_analysis_types(),
LINE  335 |             state="readonly",
LINE  336 |             font=("Segoe UI", 9, "bold"),
LINE  337 |             width=26
LINE  338 |         )
LINE  339 |         self.cb_analysis_type.pack(side=tk.LEFT, padx=(0, 10))
LINE  340 |         self.cb_analysis_type.bind("<<ComboboxSelected>>", self._on_analysis_type_changed)
LINE  341 | 
LINE  342 |         self.lbl_profile_hint = ttk.Label(
LINE  343 |             type_hdr,
LINE  344 |             text="",
LINE  345 |             style="Muted.TLabel",
LINE  346 |             wraplength=600,
LINE  347 |             justify=tk.LEFT
LINE  348 |         )
LINE  349 |         self.lbl_profile_hint.pack(anchor="w", pady=(3, 0))
LINE  350 | 
LINE  351 |         ttk.Separator(right).pack(fill=tk.X, pady=(4, 2))
LINE  352 | 
LINE  353 |         # ── Analysis Mode selector
LINE  354 |         mode_frame = ttk.Frame(right, style="Panel.TFrame", padding=(10, 6, 10, 2))
LINE  355 |         mode_frame.pack(fill=tk.X)
LINE  356 | 
LINE  357 |         ttk.Label(mode_frame, text="🔁  Modo de análisis:", style="Sec.TLabel").pack(anchor="w", pady=(0, 4))
LINE  358 | 
LINE  359 |         mode_btn_row = ttk.Frame(mode_frame, style="Panel.TFrame")
LINE  360 |         mode_btn_row.pack(fill=tk.X)
LINE  361 | 
LINE  362 |         for mode_key, mode_cfg in ANALYSIS_MODES.items():
LINE  363 |             ttk.Radiobutton(
LINE  364 |                 mode_btn_row,
LINE  365 |                 text=f"{mode_cfg.icon}  {mode_cfg.display_name}",
LINE  366 |                 variable=self.var_analysis_mode,
LINE  367 |                 value=mode_key,
LINE  368 |                 command=self._on_analysis_mode_changed,
LINE  369 |             ).pack(side=tk.LEFT, padx=(0, 18))
LINE  370 | 
LINE  371 |         self.lbl_mode_hint = ttk.Label(
LINE  372 |             mode_frame,
LINE  373 |             text="",
LINE  374 |             style="Muted.TLabel",
LINE  375 |             wraplength=600,
LINE  376 |             justify=tk.LEFT,
LINE  377 |         )
LINE  378 |         self.lbl_mode_hint.pack(anchor="w", pady=(3, 0))
LINE  379 | 
LINE  380 |         ttk.Separator(right).pack(fill=tk.X, pady=(4, 2))
LINE  381 | 
LINE  382 |         # ── Problem container (visible in Problem Mode, hidden in Project Mode)
LINE  383 |         self.problem_container = ttk.Frame(right, style="Panel.TFrame")
LINE  384 |         self.problem_container.pack(fill=tk.X)
LINE  385 | 
LINE  386 |         desc_hdr = ttk.Frame(self.problem_container, style="Panel.TFrame", padding=(10, 6, 10, 4))
LINE  387 |         desc_hdr.pack(fill=tk.X)
LINE  388 |         ttk.Label(desc_hdr, text="📝  Describe el problema / objetivo", style="Sec.TLabel").pack(anchor="w")
LINE  389 |         ttk.Label(desc_hdr,
LINE  390 |                   text="Este texto se incluirá en deepseek_prompt.md como REPORTED PROBLEM OR GOAL",
LINE  391 |                   style="Muted.TLabel").pack(anchor="w")
LINE  392 | 
LINE  393 |         desc_body = ttk.Frame(self.problem_container, style="Panel.TFrame", padding=(10, 0))
LINE  394 |         desc_body.pack(fill=tk.X)
LINE  395 |         self.problem_text = scrolledtext.ScrolledText(
LINE  396 |             desc_body, height=5,
LINE  397 |             font=("Segoe UI", 10),
LINE  398 |             bg=C_ENTRY, fg=C_TEXT,
LINE  399 |             insertbackground=C_TEXT,
LINE  400 |             selectbackground=C_TREE_SEL, selectforeground=C_TEXT,
LINE  401 |             relief="flat", bd=1, padx=8, pady=6,
LINE  402 |             wrap=tk.WORD,
LINE  403 |         )
LINE  404 |         self.problem_text.pack(fill=tk.X, expand=True)
LINE  405 | 
LINE  406 |         # ── Project Mode info card (visible in Project Mode, hidden in Problem Mode)
LINE  407 |         self.project_mode_container = ttk.Frame(right, style="Panel.TFrame")
LINE  408 |         # not packed initially — shown by _on_analysis_mode_changed
LINE  409 | 
LINE  410 |         proj_card = ttk.Frame(self.project_mode_container, style="Panel.TFrame", padding=(10, 8))
LINE  411 |         proj_card.pack(fill=tk.X, padx=10, pady=4)
LINE  412 |         ttk.Label(proj_card, text="🏗️  Modo Proyecto — Auditoría Holística", style="Sec.TLabel").pack(anchor="w")
LINE  413 |         ttk.Label(
LINE  414 |             proj_card,
LINE  415 |             text=(
LINE  416 |                 "La IA analizará el proyecto completo de forma transversal:\n"
LINE  417 |                 "  • Errores y bugs latentes\n"
LINE  418 |                 "  • Código duplicado y deuda técnica (DRY)\n"
LINE  419 |                 "  • Malas prácticas e ineficiencias de diseño\n"
LINE  420 |                 "  • Problemas arquitectónicos y acoplamiento\n"
LINE  421 |                 "  • Vulnerabilidades de seguridad (OWASP)\n"
LINE  422 |                 "  • Oportunidades de optimización de rendimiento\n\n"
LINE  423 |                 "Genera una matriz de hallazgos priorizados y un plan de acción por fases."
LINE  424 |             ),
LINE  425 |             style="Muted.TLabel",
LINE  426 |             justify=tk.LEFT,
LINE  427 |         ).pack(anchor="w", pady=(4, 0))
LINE  428 | 
LINE  429 |         self._on_analysis_type_changed(init=True)
LINE  430 |         self._on_analysis_mode_changed(init=True)
LINE  431 | 
LINE  432 |         ttk.Separator(right).pack(fill=tk.X, pady=6)
LINE  433 | 
LINE  434 |         # ── Generation settings (collapsible look)
LINE  435 |         cfg = ttk.Frame(right, style="Panel.TFrame", padding=(10, 0))
LINE  436 |         cfg.pack(fill=tk.X)
LINE  437 | 
LINE  438 |         ttk.Label(cfg, text="⚙️  Configuración de generación", style="Sec.TLabel").pack(anchor="w", pady=(0, 4))
LINE  439 | 
LINE  440 |         r1 = ttk.Frame(cfg, style="Panel.TFrame")
LINE  441 |         r1.pack(fill=tk.X, pady=2)
LINE  442 |         ttk.Label(r1, text="Máx. archivo:", style="Muted.TLabel").pack(side=tk.LEFT, padx=(0, 3))
LINE  443 |         ttk.Spinbox(r1, from_=0.1, to=50.0, increment=0.5,
LINE  444 |                     textvariable=self.var_max_file, width=5).pack(side=tk.LEFT, padx=(0, 12))
LINE  445 |         ttk.Label(r1, text="MB  ·  Máx. total:", style="Muted.TLabel").pack(side=tk.LEFT, padx=(0, 3))
LINE  446 |         ttk.Spinbox(r1, from_=1.0, to=500.0, increment=5.0,
LINE  447 |                     textvariable=self.var_max_tot, width=6).pack(side=tk.LEFT, padx=(0, 12))
LINE  448 |         ttk.Label(r1, text="MB  ·  Máx. archivos:", style="Muted.TLabel").pack(side=tk.LEFT, padx=(0, 3))
LINE  449 |         ttk.Spinbox(r1, from_=1, to=5000, increment=10,
LINE  450 |                     textvariable=self.var_max_n, width=5).pack(side=tk.LEFT)
LINE  451 | 
LINE  452 |         r2 = ttk.Frame(cfg, style="Panel.TFrame")
LINE  453 |         r2.pack(fill=tk.X, pady=2)
LINE  454 |         for txt, var in [
LINE  455 |             ("Nº de línea", self.var_lineno),
LINE  456 |             ("Árbol de carpetas", self.var_tree),
LINE  457 |             ("Instrucciones DeepSeek", self.var_instruct),
LINE  458 |             ("Filtrar por extensión", self.var_filter),
LINE  459 |         ]:
LINE  460 |             ttk.Checkbutton(r2, text=txt, variable=var).pack(side=tk.LEFT, padx=(0, 14))
LINE  461 |         ttk.Label(r2, text="Formato:", style="Muted.TLabel").pack(side=tk.LEFT, padx=(8, 3))
LINE  462 |         ttk.Radiobutton(r2, text="Markdown", value="markdown", variable=self.var_fmt).pack(side=tk.LEFT, padx=(0, 6))
LINE  463 |         ttk.Radiobutton(r2, text="Texto",    value="text",     variable=self.var_fmt).pack(side=tk.LEFT)
LINE  464 | 
LINE  465 |         ttk.Separator(right).pack(fill=tk.X, pady=6)
LINE  466 | 
LINE  467 |         # ── Preview label
LINE  468 |         prev_hdr = ttk.Frame(right, style="Panel.TFrame", padding=(10, 0))
LINE  469 |         prev_hdr.pack(fill=tk.X)
LINE  470 |         ttk.Label(prev_hdr, text="🔍  Vista previa del documento generado", style="Sec.TLabel").pack(anchor="w")
LINE  471 | 
LINE  472 |         # ── Preview area
LINE  473 |         prev_body = ttk.Frame(right, style="Panel.TFrame", padding=(10, 4, 10, 4))
LINE  474 |         prev_body.pack(fill=tk.BOTH, expand=True)
LINE  475 |         self.preview_text = scrolledtext.ScrolledText(
LINE  476 |             prev_body, wrap=tk.NONE,
LINE  477 |             font=("Consolas", 9),
LINE  478 |             bg=C_ENTRY, fg=C_TEXT,
LINE  479 |             insertbackground=C_TEXT,
LINE  480 |             selectbackground=C_TREE_SEL, selectforeground=C_TEXT,
LINE  481 |             relief="flat", bd=0, padx=8, pady=6,
LINE  482 |         )
LINE  483 |         self.preview_text.pack(fill=tk.BOTH, expand=True)
LINE  484 | 
LINE  485 |     # ──────────────────────────────────────────────────────────────────────
LINE  486 |     # BOTTOM  –  stats bar + action buttons
LINE  487 |     # ──────────────────────────────────────────────────────────────────────
LINE  488 |     def _build_bottom(self):
LINE  489 |         ttk.Separator(self.root).pack(fill=tk.X)
LINE  490 | 
LINE  491 |         bottom = tk.Frame(self.root, bg=C_STAT_BG)
LINE  492 |         bottom.pack(fill=tk.X, side=tk.BOTTOM)
LINE  493 | 
LINE  494 |         # ── Action buttons (left side of bottom bar)
LINE  495 |         btn_strip = tk.Frame(bottom, bg=C_STAT_BG, padx=8, pady=6)
LINE  496 |         btn_strip.pack(side=tk.LEFT)
LINE  497 | 
LINE  498 |         ttk.Button(btn_strip, text="🔬 Analizar proyecto",
LINE  499 |                    style="Neutral.TButton",
LINE  500 |                    command=self.on_analyze_project).pack(side=tk.LEFT, padx=(0, 5))
LINE  501 |         ttk.Button(btn_strip, text="⚡ Generar contexto",
LINE  502 |                    style="Accent.TButton",
LINE  503 |                    command=self.on_generate_prompt).pack(side=tk.LEFT, padx=(0, 5))
LINE  504 |         ttk.Button(btn_strip, text="📁 Abrir carpeta resultados",
LINE  505 |                    style="Success.TButton",
LINE  506 |                    command=self.on_open_results_folder).pack(side=tk.LEFT, padx=(0, 5))
LINE  507 |         ttk.Button(btn_strip, text="📋 Copiar prompt",
LINE  508 |                    style="Neutral.TButton",
LINE  509 |                    command=self.on_copy_clipboard).pack(side=tk.LEFT, padx=(0, 5))
LINE  510 |         ttk.Button(btn_strip, text="💾 Guardar como…",
LINE  511 |                    style="Neutral.TButton",
LINE  512 |                    command=self.on_export_file).pack(side=tk.LEFT, padx=(0, 5))
LINE  513 |         ttk.Button(btn_strip, text="🗑 Limpiar selección",
LINE  514 |                    style="Neutral.TButton",
LINE  515 |                    command=self.on_clear_all).pack(side=tk.LEFT)
LINE  516 | 
LINE  517 |         # ── Stat tiles (right side of bottom bar)
LINE  518 |         stats = tk.Frame(bottom, bg=C_STAT_BG, padx=12, pady=4)
LINE  519 |         stats.pack(side=tk.RIGHT)
LINE  520 | 
LINE  521 |         def _stat(parent, key):
LINE  522 |             cell = tk.Frame(parent, bg=C_STAT_BG, padx=10, pady=2)
LINE  523 |             cell.pack(side=tk.LEFT)
LINE  524 |             var = tk.StringVar(value="—")
LINE  525 |             tk.Label(cell, text=key, bg=C_STAT_BG, fg=C_TEXT2,
LINE  526 |                      font=("Segoe UI", 8)).pack()
LINE  527 |             tk.Label(cell, textvariable=var, bg=C_STAT_BG, fg=C_TEXT,
LINE  528 |                      font=("Segoe UI", 11, "bold")).pack()
LINE  529 |             return var
LINE  530 | 
LINE  531 |         self.sv_folder    = _stat(stats, "Carpeta")
LINE  532 |         self.sv_sel_files = _stat(stats, "Archivos sel.")
LINE  533 |         self.sv_included  = _stat(stats, "Incluidos")
LINE  534 |         self.sv_excluded  = _stat(stats, "Excluidos")
LINE  535 |         self.sv_size      = _stat(stats, "Tamaño total")
LINE  536 |         self.sv_lines     = _stat(stats, "Líneas")
LINE  537 | 
LINE  538 |         # ── Status text (very bottom strip)
LINE  539 |         status_bar = tk.Frame(self.root, bg="#0f1320", pady=2)
LINE  540 |         status_bar.pack(fill=tk.X, side=tk.BOTTOM)
LINE  541 |         tk.Label(status_bar, textvariable=self.sv_status,
LINE  542 |                  bg="#0f1320", fg=C_TEXT2,
LINE  543 |                  font=("Segoe UI", 8, "italic"),
LINE  544 |                  anchor="w", padx=10).pack(fill=tk.X)
LINE  545 | 
LINE  546 |         self.sv_status.set("Listo. Selecciona una carpeta para comenzar.")
LINE  547 | 
LINE  548 |     # ── Stat refresh ─────────────────────────────────────────────────────
LINE  549 |     def _refresh_selection_stats(self):
LINE  550 |         folder  = self.var_folder.get()
LINE  551 |         has_fld = 1 if folder else 0
LINE  552 |         sel_files = len(self.tree.get_checked_files()) + len(self.selector.get_selection().individual_files)
LINE  553 | 
LINE  554 |         # Count binary vs. included among selected files
LINE  555 |         included = 0
LINE  556 |         excluded = 0
LINE  557 |         total_bytes = 0
LINE  558 | 
LINE  559 |         checked = self.tree.get_checked_files()
LINE  560 |         ind     = self.selector.get_selection().individual_files
LINE  561 | 
LINE  562 |         all_paths = []
LINE  563 |         if folder:
LINE  564 |             for rel in checked:
LINE  565 |                 all_paths.append(os.path.join(folder, rel))
LINE  566 |         for abs_p in ind:
LINE  567 |             all_paths.append(abs_p)
LINE  568 | 
LINE  569 |         for fp in all_paths:
LINE  570 |             if not os.path.isfile(fp):
LINE  571 |                 continue
LINE  572 |             if is_binary_file(fp):
LINE  573 |                 excluded += 1
LINE  574 |             else:
LINE  575 |                 included += 1
LINE  576 |                 total_bytes += get_file_size(fp)
LINE  577 | 
LINE  578 |         size_mb = total_bytes / (1024 * 1024)
LINE  579 | 
LINE  580 |         self.sv_folder.set(str(has_fld))
LINE  581 |         self.sv_sel_files.set(str(sel_files))
LINE  582 |         self.sv_included.set(str(included))
LINE  583 |         self.sv_excluded.set(str(excluded))
LINE  584 |         self.sv_size.set(f"{size_mb:.2f} MB")
LINE  585 |         # Lines shown only after generation
LINE  586 |         # self.sv_lines is updated in on_generate_prompt
LINE  587 | 
LINE  588 |     # ── UI event handlers ────────────────────────────────────────────────
LINE  589 |     # === PERSISTENCE: PHASE1 (method) ===
LINE  590 |     def _on_tree_check_change(self, rel_path: str, is_checked: bool):
LINE  591 |         """Persist checkbox changes to SQLite (Phase 1)."""
LINE  592 |         if self._persist_db is None:
LINE  593 |             return
LINE  594 |         folder = self.var_folder.get()
LINE  595 |         if not folder:
LINE  596 |             return
LINE  597 |         try:
LINE  598 |             project_id = self._persist_db.get_or_create_project(folder)
LINE  599 |             self._persist_db.update_is_checked(project_id, rel_path, is_checked)
LINE  600 |         except Exception:
LINE  601 |             pass
LINE  602 |     # === END PERSISTENCE: PHASE1 (method) ===
LINE  603 | 
LINE  604 |     def on_select_folder(self):
LINE  605 |         folder = dialogs.ask_folder("Seleccionar Carpeta del Proyecto")
LINE  606 |         if folder:
LINE  607 |             self.selector.set_folder(folder)
LINE  608 |             self.var_folder.set(folder)
LINE  609 |             self.reload_tree()
LINE  610 |             self._refresh_selection_stats()
LINE  611 |             self.sv_status.set(f"Carpeta seleccionada: {folder}")
LINE  612 | 
LINE  613 |     def on_analyze_project(self):
LINE  614 |         folder = self.var_folder.get()
LINE  615 |         if not folder or not os.path.isdir(folder):
LINE  616 |             folder = dialogs.ask_folder("Seleccionar Carpeta para Analizar")
LINE  617 |             if not folder:
LINE  618 |                 return
LINE  619 |             self.selector.set_folder(folder)
LINE  620 |             self.var_folder.set(folder)
LINE  621 |             self.reload_tree()
LINE  622 | 
LINE  623 |         self.sv_status.set("Analizando estructura, tecnologías y dependencias del proyecto...")
LINE  624 |         self.root.update_idletasks()
LINE  625 | 
LINE  626 |         self.selector.set_exclusions_from_string(self.var_excl.get())
LINE  627 |         excluded = self.selector.get_selection().excluded_dirs
LINE  628 | 
LINE  629 |         try:
LINE  630 |             max_file_mb = float(self.var_max_file.get())
LINE  631 |         except ValueError:
LINE  632 |             max_file_mb = 2.0
LINE  633 | 
LINE  634 |         analyzer = ProjectAnalyzer(excluded_dirs=excluded)
LINE  635 |         result = analyzer.analyze(folder, max_file_size_mb=max_file_mb)
LINE  636 |         # === PERSISTENCE: PHASE1 (analyze) ===
LINE  637 |         try:
LINE  638 |             analyzer.persist_result(result)
LINE  639 |         except Exception:
LINE  640 |             pass
LINE  641 |         # === END PERSISTENCE: PHASE1 (analyze) ===
LINE  642 | 
LINE  643 | 
LINE  644 |         self.sv_status.set(
LINE  645 |             f"Análisis completado: {result.total_files} archivos, {result.total_lines:,} líneas. "
LINE  646 |             f"Lenguaje: {result.primary_language} · Framework: {result.framework}"
LINE  647 |         )
LINE  648 | 
LINE  649 |         ProjectAnalysisDialog(
LINE  650 |             self.root,
LINE  651 |             analysis=result,
LINE  652 |             on_apply_selection=self.apply_recommended_selection
LINE  653 |         )
LINE  654 | 
LINE  655 |     def on_intelligent_context_select(self):
LINE  656 |         folder = self.var_folder.get()
LINE  657 |         if not folder or not os.path.isdir(folder):
LINE  658 |             dialogs.show_warning("Atención", "Selecciona una carpeta del proyecto primero.")
LINE  659 |             return
LINE  660 | 
LINE  661 |         problem_desc = self.problem_text.get("1.0", tk.END).strip()
LINE  662 |         if not problem_desc:
LINE  663 |             dialogs.show_warning(
LINE  664 |                 "Atención",
LINE  665 |                 "Ingresa una descripción del problema en el panel derecho para realizar la selección inteligente."
LINE  666 |             )
LINE  667 |             return
LINE  668 | 
LINE  669 |         self.sv_status.set("Ejecutando Selección Inteligente de Contexto...")
LINE  670 |         self.root.update_idletasks()
LINE  671 | 
LINE  672 |         # Get candidate files (all checked files in tree, or all files in tree if none checked)
LINE  673 |         candidate_files = self.tree.get_checked_files()
LINE  674 |         if not candidate_files:
LINE  675 |             all_files = []
LINE  676 |             def _gather(item):
LINE  677 |                 if not self.tree.get_children(item):
LINE  678 |                     name = self.tree.set(item, "name")
LINE  679 |                     if name:
LINE  680 |                         all_files.append(name)
LINE  681 |                 for child in self.tree.get_children(item):
LINE  682 |                     _gather(child)
LINE  683 |             for r in self.tree.get_children():
LINE  684 |                 _gather(r)
LINE  685 |             candidate_files = all_files
LINE  686 | 
LINE  687 |         try:
LINE  688 |             max_file_mb = float(self.var_max_file.get())
LINE  689 |             max_tot_mb = float(self.var_max_tot.get())
LINE  690 |             max_n = int(self.var_max_n.get())
LINE  691 |         except ValueError:
LINE  692 |             max_file_mb, max_tot_mb, max_n = 2.0, 50.0, 100
LINE  693 | 
LINE  694 |         analyzer = IntelligentContextAnalyzer()
LINE  695 |         prioritized = analyzer.analyze(
LINE  696 |             folder_path=folder,
LINE  697 |             candidate_rel_files=candidate_files,
LINE  698 |             problem_desc=problem_desc,
LINE  699 |             max_file_size_mb=max_file_mb,
LINE  700 |             max_total_size_mb=max_tot_mb,
LINE  701 |             max_files=max_n
LINE  702 |         )
LINE  703 | 
LINE  704 |         IntelligentContextDialog(
LINE  705 |             self.root,
LINE  706 |             problem_desc=problem_desc,
LINE  707 |             prioritized_files=prioritized,
LINE  708 |             on_confirm=self.apply_recommended_selection
LINE  709 |         )
LINE  710 |         self.sv_status.set("Selección Inteligente completada.")
LINE  711 | 
LINE  712 |     def _on_analysis_type_changed(self, event=None, init: bool = False):
LINE  713 |         selected = self.var_analysis_type.get()
LINE  714 |         profile = get_analysis_profile(selected)
LINE  715 |         if hasattr(self, "lbl_profile_hint"):
LINE  716 |             self.lbl_profile_hint.config(
LINE  717 |                 text=f"{profile.icon} {profile.objective}\nEnfoque: {profile.focus}"
LINE  718 |             )
LINE  719 |         if hasattr(self, "problem_text"):
LINE  720 |             current_text = self.problem_text.get("1.0", tk.END).strip()
LINE  721 |             all_hints = {p.default_prompt_hint for p in ANALYSIS_PROFILES.values()}
LINE  722 |             all_hints.add("Por favor analiza el siguiente código del proyecto. Identifica posibles errores, refactorizaciones recomendadas y soluciones al problema.")
LINE  723 | 
LINE  724 |             if not current_text or current_text in all_hints or init:
LINE  725 |                 self.problem_text.delete("1.0", tk.END)
LINE  726 |                 self.problem_text.insert("1.0", profile.default_prompt_hint)
LINE  727 | 
LINE  728 |     def _on_analysis_mode_changed(self, event=None, init: bool = False):
LINE  729 |         """Shows/hides problem container vs project-mode card based on selected mode."""
LINE  730 |         mode_key = self.var_analysis_mode.get()
LINE  731 |         mode_cfg = get_analysis_mode_config(mode_key)
LINE  732 | 
LINE  733 |         if hasattr(self, "lbl_mode_hint"):
LINE  734 |             self.lbl_mode_hint.config(text=mode_cfg.description)
LINE  735 | 
LINE  736 |         if mode_key == MODE_PROJECT:
LINE  737 |             if hasattr(self, "problem_container"):
LINE  738 |                 self.problem_container.pack_forget()
LINE  739 |             if hasattr(self, "project_mode_container"):
LINE  740 |                 self.project_mode_container.pack(fill=tk.X, after=None)
LINE  741 |                 # Insert after the separator that precedes the problem_container
LINE  742 |                 self.project_mode_container.pack(fill=tk.X)
LINE  743 |         else:
LINE  744 |             if hasattr(self, "project_mode_container"):
LINE  745 |                 self.project_mode_container.pack_forget()
LINE  746 |             if hasattr(self, "problem_container"):
LINE  747 |                 self.problem_container.pack(fill=tk.X)
LINE  748 | 
LINE  749 |     def apply_recommended_selection(self, selected_files: List[str], notify: bool = True):
LINE  750 |         if not selected_files:
LINE  751 |             if notify:
LINE  752 |                 dialogs.show_warning("Atención", "No se seleccionó ningún archivo recomendado.")
LINE  753 |             return
LINE  754 | 
LINE  755 |         self.tree.set_checked_files(set(selected_files))
LINE  756 |         self.selector.set_checked_folder_files(self.tree.get_checked_files())
LINE  757 |         self._refresh_selection_stats()
LINE  758 |         count = len(selected_files)
LINE  759 |         self.sv_status.set(f"✓ Selección recomendada aplicada: {count} archivo(s) preparados para contexto.")
LINE  760 |         if notify:
LINE  761 |             dialogs.show_info(
LINE  762 |                 "Selección Aplicada",
LINE  763 |                 f"Se han aplicado {count} archivo(s) recomendados para el contexto.\n\n"
LINE  764 |                 "Puedes pulsar '⚡ Generar contexto' directamente cuando estés listo."
LINE  765 |             )
LINE  766 | 
LINE  767 |     def on_remove_folder(self):
LINE  768 |         self.selector.remove_folder()
LINE  769 |         self.var_folder.set("")
LINE  770 |         for item in self.tree.get_children():
LINE  771 |             self.tree.delete(item)
LINE  772 |         self.tree.checked_items.clear()
LINE  773 |         self._refresh_selection_stats()
LINE  774 |         self.sv_status.set("Carpeta removida.")
LINE  775 | 
LINE  776 |     def on_clear_all(self):
LINE  777 |         self.on_remove_folder()
LINE  778 |         self.on_clear_individual_files()
LINE  779 |         self.preview_text.delete("1.0", tk.END)
LINE  780 |         self.sv_lines.set("0")
LINE  781 |         self.sv_status.set("Selección limpiada.")
LINE  782 | 
LINE  783 |     def reload_tree(self):
LINE  784 |         for item in self.tree.get_children():
LINE  785 |             self.tree.delete(item)
LINE  786 |         self.tree.checked_items.clear()
LINE  787 | 
LINE  788 |         folder = self.var_folder.get()
LINE  789 |         if not folder or not os.path.isdir(folder):
LINE  790 |             return
LINE  791 | 
LINE  792 |         self.selector.set_exclusions_from_string(self.var_excl.get())
LINE  793 |         excluded_dirs = self.selector.get_selection().excluded_dirs
LINE  794 |         allowed_exts  = self._get_exts()
LINE  795 |         filter_ext    = self.var_filter.get()
LINE  796 | 
LINE  797 |         root_item = self.tree.insert("", "end", text="📁",
LINE  798 |                                      values=("", os.path.basename(folder)), open=True)
LINE  799 |         folder_items = {".": root_item}
LINE  800 | 
LINE  801 |         for dirpath, dirnames, filenames in os.walk(folder):
LINE  802 |             dirnames[:] = [d for d in sorted(dirnames) if d not in excluded_dirs]
LINE  803 |             rel_dir = os.path.relpath(dirpath, folder)
LINE  804 | 
LINE  805 |             parent_item = folder_items.get(rel_dir)
LINE  806 |             if not parent_item:
LINE  807 |                 continue
LINE  808 | 
LINE  809 |             for d in dirnames:
LINE  810 |                 rel_sub = os.path.join(rel_dir, d) if rel_dir != "." else d
LINE  811 |                 item = self.tree.insert_folder(parent_item, rel_sub)
LINE  812 |                 folder_items[rel_sub] = item
LINE  813 | 
LINE  814 |             for f in sorted(filenames):
LINE  815 |                 ext = os.path.splitext(f)[1].lower()
LINE  816 |                 if ext in KNOWN_BINARY_EXTENSIONS:
LINE  817 |                     continue
LINE  818 |                 if filter_ext and allowed_exts and ext not in allowed_exts:
LINE  819 |                     continue
LINE  820 |                 rel_file = os.path.join(rel_dir, f) if rel_dir != "." else f
LINE  821 |                 self.tree.insert_file(parent_item, rel_file)
LINE  822 |         # === PERSISTENCE: PHASE1 (reload) ===
LINE  823 |         if self._persist_db is not None:
LINE  824 |             try:
LINE  825 |                 saved = self._persist_db.load_checked_state(folder)
LINE  826 |                 if saved is not None:
LINE  827 |                     self.tree.set_checked_files(saved)
LINE  828 |                     self.selector.set_checked_folder_files(
LINE  829 |                         self.tree.get_checked_files()
LINE  830 |                     )
LINE  831 |             except Exception:
LINE  832 |                 pass
LINE  833 |         # === END PERSISTENCE: PHASE1 (reload) ===
LINE  834 | 
LINE  835 | 
LINE  836 |         self._refresh_selection_stats()
LINE  837 | 
LINE  838 |     def _find_folder_item(self, rel_path: str):
LINE  839 |         def search(item):
LINE  840 |             if self.tree.set(item, "name") == rel_path:
LINE  841 |                 return item
LINE  842 |             for ch in self.tree.get_children(item):
LINE  843 |                 found = search(ch)
LINE  844 |                 if found:
LINE  845 |                     return found
LINE  846 |             return None
LINE  847 |         for item in self.tree.get_children():
LINE  848 |             found = search(item)
LINE  849 |             if found:
LINE  850 |                 return found
LINE  851 |         return None
LINE  852 | 
LINE  853 |     def _get_exts(self) -> set:
LINE  854 |         exts = set()
LINE  855 |         for e in self.var_exts.get().split(","):
LINE  856 |             c = e.strip().lower()
LINE  857 |             if c:
LINE  858 |                 exts.add(c if c.startswith(".") else "." + c)
LINE  859 |         return exts
LINE  860 | 
LINE  861 |     def on_select_all_tree(self):
LINE  862 |         self.tree.select_all()
LINE  863 |         self._refresh_selection_stats()
LINE  864 | 
LINE  865 |     def on_deselect_all_tree(self):
LINE  866 |         self.tree.deselect_all()
LINE  867 |         self._refresh_selection_stats()
LINE  868 | 
LINE  869 |     def on_add_individual_files(self):
LINE  870 |         files = dialogs.ask_files("Seleccionar Archivos Individuales")
LINE  871 |         if files:
LINE  872 |             added = self.selector.add_individual_files(files)
LINE  873 |             self.file_listbox.delete(0, tk.END)
LINE  874 |             for f in self.selector.get_selection().individual_files:
LINE  875 |                 self.file_listbox.insert(tk.END, f)
LINE  876 |             self._refresh_selection_stats()
LINE  877 |             self.sv_status.set(f"Se agregaron {added} archivo(s) individual(es).")
LINE  878 | 
LINE  879 |     def on_remove_individual_file(self):
LINE  880 |         sel = self.file_listbox.curselection()
LINE  881 |         if sel:
LINE  882 |             val = self.file_listbox.get(sel[0])
LINE  883 |             self.selector.remove_individual_file(val)
LINE  884 |             self.file_listbox.delete(sel[0])
LINE  885 |             self._refresh_selection_stats()
LINE  886 |             self.sv_status.set(f"Archivo removido: {os.path.basename(val)}")
LINE  887 | 
LINE  888 |     def on_clear_individual_files(self):
LINE  889 |         self.selector.clear_individual_files()
LINE  890 |         self.file_listbox.delete(0, tk.END)
LINE  891 |         self._refresh_selection_stats()
LINE  892 |         self.sv_status.set("Lista de archivos individuales limpiada.")
LINE  893 | 
LINE  894 |     def get_output_dir(self) -> str:
LINE  895 |         out_dir = os.path.join(
LINE  896 |             os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "output"
LINE  897 |         )
LINE  898 |         os.makedirs(out_dir, exist_ok=True)
LINE  899 |         return out_dir
LINE  900 | 
LINE  901 |     def on_open_results_folder(self):
LINE  902 |         out_dir = self.get_output_dir()
LINE  903 |         try:
LINE  904 |             if os.name == "nt":
LINE  905 |                 os.startfile(out_dir)
LINE  906 |             else:
LINE  907 |                 subprocess.run(["open" if sys.platform == "darwin" else "xdg-open", out_dir])
LINE  908 |             self.sv_status.set(f"Carpeta de resultados abierta: {out_dir}")
LINE  909 |         except Exception as exc:
LINE  910 |             dialogs.show_error("Error", f"No se pudo abrir la carpeta: {exc}")
LINE  911 | 
LINE  912 |     def on_generate_prompt(self):
LINE  913 |         folder = self.var_folder.get()
LINE  914 |         ind    = self.selector.get_selection().individual_files
LINE  915 | 
LINE  916 |         if not folder and not ind:
LINE  917 |             dialogs.show_warning("Atención",
LINE  918 |                                  "Selecciona una carpeta o al menos un archivo individual.")
LINE  919 |             return
LINE  920 | 
LINE  921 |         self.selector.set_checked_folder_files(self.tree.get_checked_files())
LINE  922 |         self.selector.set_exclusions_from_string(self.var_excl.get())
LINE  923 | 
LINE  924 |         try: self.config.max_file_size_mb  = float(self.var_max_file.get())
LINE  925 |         except ValueError: self.config.max_file_size_mb = 2.0
LINE  926 | 
LINE  927 |         try: self.config.max_total_size_mb = float(self.var_max_tot.get())
LINE  928 |         except ValueError: self.config.max_total_size_mb = 50.0
LINE  929 | 
LINE  930 |         try: self.config.max_files = int(self.var_max_n.get())
LINE  931 |         except ValueError: self.config.max_files = 100
LINE  932 | 
LINE  933 |         self.config.add_line_numbers        = self.var_lineno.get()
LINE  934 |         self.config.include_tree            = self.var_tree.get()
LINE  935 |         self.config.include_system_instructions = self.var_instruct.get()
LINE  936 |         self.config.output_format           = self.var_fmt.get()
LINE  937 |         self.config.analysis_type           = self.var_analysis_type.get()
LINE  938 |         self.config.analysis_mode           = self.var_analysis_mode.get()
LINE  939 | 
LINE  940 |         problem_desc = self.problem_text.get("1.0", tk.END).strip()
LINE  941 |         # In Project Mode, ignore the problem text field
LINE  942 |         if self.config.analysis_mode == MODE_PROJECT:
LINE  943 |             problem_desc = ""
LINE  944 |         gen = PromptGenerator(self.config)
LINE  945 | 
LINE  946 |         doc_text, included, excluded, omitted, total_lines = gen.generate(
LINE  947 |             self.selector.get_selection(), problem_desc
LINE  948 |         )
LINE  949 | 
LINE  950 |         if included == 0 and omitted == 0:
LINE  951 |             dialogs.show_warning("Atención",
LINE  952 |                                  "No hay archivos de código válidos seleccionados.")
LINE  953 |             return
LINE  954 | 
LINE  955 |         # Preview
LINE  956 |         self.preview_text.delete("1.0", tk.END)
LINE  957 |         self.preview_text.insert(tk.END, doc_text)
LINE  958 | 
LINE  959 |         # Update bottom stats
LINE  960 |         self._refresh_selection_stats()
LINE  961 |         self.sv_included.set(str(included))
LINE  962 |         self.sv_excluded.set(str(excluded))
LINE  963 |         self.sv_lines.set(f"{total_lines:,}")
LINE  964 | 
LINE  965 |         # Save output files
LINE  966 |         out_dir     = self.get_output_dir()
LINE  967 |         md_text, _, _, _, _  = generate_markdown_bundle(
LINE  968 |             self.selector.get_selection(), problem_desc, self.config)
LINE  969 |         txt_text, _, _, _, _ = generate_text_bundle(
LINE  970 |             self.selector.get_selection(), problem_desc, self.config)
LINE  971 |         prompt_text = generate_standalone_prompt(
LINE  972 |             problem_desc,
LINE  973 |             analysis_type=self.config.analysis_type,
LINE  974 |             analysis_mode=self.config.analysis_mode,
LINE  975 |         )
LINE  976 | 
LINE  977 |         write_text_file(os.path.join(out_dir, "deepseek_project_context.md"),  md_text)
LINE  978 |         write_text_file(os.path.join(out_dir, "deepseek_project_context.txt"), txt_text)
LINE  979 |         write_text_file(os.path.join(out_dir, "deepseek_prompt.md"),           prompt_text)
LINE  980 | 
LINE  981 |         dialogs.show_info(
LINE  982 |             "✅ Archivos Preparados",
LINE  983 |             f"Archivos generados en:\n{out_dir}\n\n"
LINE  984 |             f"• Incluidos:  {included}\n"
LINE  985 |             f"• Excluidos:  {excluded}\n"
LINE  986 |             f"• Omitidos:   {omitted}\n"
LINE  987 |             f"• Líneas:     {total_lines:,}\n\n"
LINE  988 |             "Abre DeepSeek en tu navegador y adjunta:\n"
LINE  989 |             "  1. deepseek_prompt.md\n"
LINE  990 |             "  2. deepseek_project_context.md\n"
LINE  991 |             "  3. deepseek_project_context.txt"
LINE  992 |         )
LINE  993 |         self.sv_status.set(
LINE  994 |             f"Listo · Incluidos: {included} · Excluidos: {excluded} · Omitidos: {omitted} · Líneas: {total_lines:,}"
LINE  995 |         )
LINE  996 | 
LINE  997 |     # === AUTO-GENERATED: file_search_dependency_feature ===
LINE  998 |     def on_open_file_search(self):
LINE  999 |         folder = self.var_folder.get()
LINE 1000 |         if not folder or not os.path.isdir(folder):
LINE 1001 |             dialogs.show_warning("Atención", "Selecciona una carpeta del proyecto primero.")
LINE 1002 |             return
LINE 1003 | 
LINE 1004 |         excluded = self.selector.get_selection().excluded_dirs
LINE 1005 |         FileSearchDialog(
LINE 1006 |             self.root,
LINE 1007 |             folder,
LINE 1008 |             excluded_dirs=excluded,
LINE 1009 |             on_analyze_dependencies=self.open_dependency_tree,
LINE 1010 |         )
LINE 1011 | 
LINE 1012 |     def open_dependency_tree(self, rel_path: str):
LINE 1013 |         folder = self.var_folder.get()
LINE 1014 |         if not folder or not os.path.isdir(folder):
LINE 1015 |             dialogs.show_warning("Atención", "Selecciona una carpeta del proyecto primero.")
LINE 1016 |             return
LINE 1017 | 
LINE 1018 |         excluded = self.selector.get_selection().excluded_dirs
LINE 1019 |         DependencyTreeDialog(
LINE 1020 |             self.root,
LINE 1021 |             folder,
LINE 1022 |             rel_path,
LINE 1023 |             excluded_dirs=excluded,
LINE 1024 |             on_apply_selection=self.apply_dependency_selection,
LINE 1025 |         )
LINE 1026 | 
LINE 1027 |     def apply_dependency_selection(self, selected_files: List[str]):
LINE 1028 |         if not selected_files:
LINE 1029 |             return
LINE 1030 | 
LINE 1031 |         existing = set(self.tree.get_checked_files())
LINE 1032 |         combined = existing | set(selected_files)
LINE 1033 | 
LINE 1034 |         self.tree.set_checked_files(combined)
LINE 1035 |         self.selector.set_checked_folder_files(self.tree.get_checked_files())
LINE 1036 |         self._refresh_selection_stats()
LINE 1037 | 
LINE 1038 |         self.sv_status.set(
LINE 1039 |             f"✓ {len(selected_files)} dependencia(s) agregadas/actualizadas en la selección."
LINE 1040 |         )
LINE 1041 |     # === END AUTO-GENERATED ===
LINE 1042 | 
LINE 1043 |     def on_copy_clipboard(self):
LINE 1044 | 
LINE 1045 | 
LINE 1046 |         content = self.preview_text.get("1.0", tk.END).strip()
LINE 1047 |         if not content:
LINE 1048 |             dialogs.show_warning("Atención",
LINE 1049 |                                  "Genera el contexto primero (⚡ Generar contexto).")
LINE 1050 |             return
LINE 1051 |         if copy_to_clipboard(self.root, content):
LINE 1052 |             self.sv_status.set("Contenido copiado al portapapeles.")
LINE 1053 | 
LINE 1054 |     def on_export_file(self):
LINE 1055 |         content = self.preview_text.get("1.0", tk.END).strip()
LINE 1056 |         if not content:
LINE 1057 |             dialogs.show_warning("Atención",
LINE 1058 |                                  "Genera el contexto primero (⚡ Generar contexto).")
LINE 1059 |             return
LINE 1060 |         ext = ".md" if self.var_fmt.get() == "markdown" else ".txt"
LINE 1061 |         fp  = dialogs.ask_save_file("Guardar Documento", default_ext=ext)
LINE 1062 |         if fp:
LINE 1063 |             ok, msg = write_text_file(fp, content)
LINE 1064 |             if ok:
LINE 1065 |                 self.sv_status.set(f"Guardado: {os.path.basename(fp)}")
LINE 1066 |                 dialogs.show_info("Guardado", f"Archivo guardado en:\n{fp}")
LINE 1067 |             else:
LINE 1068 |                 dialogs.show_error("Error", f"No se pudo guardar: {msg}")
```

==============================================================
FILE: .backup_search_perf/app/core/project_scanner.py
==============================================================
```py
LINE   1 | """Project scanner module for scanning directory structures with caching."""
LINE   2 | import os
LINE   3 | import threading
LINE   4 | from typing import Set, Dict, Any, List, Optional, Tuple
LINE   5 | from app.utils.file_utils import KNOWN_BINARY_EXTENSIONS
LINE   6 | 
LINE   7 | _cache_lock = threading.Lock()
LINE   8 | # Cache mapping: key -> (folder_mtime, valid_files)
LINE   9 | _SCAN_CACHE: Dict[Tuple, Tuple[float, List[str]]] = {}
LINE  10 | _MAX_CACHE_ENTRIES = 50
LINE  11 | 
LINE  12 | 
LINE  13 | def clear_scan_cache() -> None:
LINE  14 |     """Clears the scan directory cache."""
LINE  15 |     with _cache_lock:
LINE  16 |         _SCAN_CACHE.clear()
LINE  17 | 
LINE  18 | 
LINE  19 | def is_file_allowed(filename: str, allowed_extensions: Optional[Set[str]], filter_by_ext: bool = True) -> bool:
LINE  20 |     """Checks if file is allowed (not binary media and matching allowed extensions)."""
LINE  21 |     ext = os.path.splitext(filename)[1].lower()
LINE  22 |     if ext in KNOWN_BINARY_EXTENSIONS:
LINE  23 |         return False
LINE  24 |     if filter_by_ext and allowed_extensions:
LINE  25 |         return ext in allowed_extensions
LINE  26 |     return True
LINE  27 | 
LINE  28 | 
LINE  29 | def scan_directory(
LINE  30 |     folder_path: str,
LINE  31 |     excluded_dirs: Optional[Set[str]] = None,
LINE  32 |     allowed_extensions: Optional[Set[str]] = None,
LINE  33 |     use_cache: bool = True,
LINE  34 |     force_refresh: bool = False,
LINE  35 | ) -> List[str]:
LINE  36 |     """
LINE  37 |     Recursively scans folder_path ignoring excluded_dirs and non-allowed file extensions.
LINE  38 |     Returns sorted list of relative file paths. Uses thread-safe caching with mtime checking.
LINE  39 |     """
LINE  40 |     if not folder_path or not os.path.isdir(folder_path):
LINE  41 |         return []
LINE  42 | 
LINE  43 |     abs_folder = os.path.abspath(folder_path)
LINE  44 |     excluded_set = set(excluded_dirs) if excluded_dirs else set()
LINE  45 |     allowed_tuple = tuple(sorted(allowed_extensions)) if allowed_extensions else None
LINE  46 |     cache_key = (abs_folder, tuple(sorted(excluded_set)), allowed_tuple)
LINE  47 | 
LINE  48 |     # FIX: firma de invalidación recursiva ligera (raíz + subdirectorios
LINE  49 |     # inmediatos). No es perfecta, pero evita devolver caché obsoleta cuando
LINE  50 |     # cambian archivos dentro de subcarpetas de primer nivel, sin coste de
LINE  51 |     # os.walk completo.
LINE  52 |     signature = 0.0
LINE  53 |     try:
LINE  54 |         signature = os.path.getmtime(abs_folder)
LINE  55 |         with os.scandir(abs_folder) as it:
LINE  56 |             for entry in it:
LINE  57 |                 if entry.is_dir(follow_symlinks=False):
LINE  58 |                     try:
LINE  59 |                         signature = max(
LINE  60 |                             signature,
LINE  61 |                             entry.stat(follow_symlinks=False).st_mtime,
LINE  62 |                         )
LINE  63 |                     except OSError:
LINE  64 |                         continue
LINE  65 |     except OSError:
LINE  66 |         pass
LINE  67 | 
LINE  68 |     if use_cache and not force_refresh:
LINE  69 |         with _cache_lock:
LINE  70 |             if cache_key in _SCAN_CACHE:
LINE  71 |                 cached_mtime, cached_files = _SCAN_CACHE[cache_key]
LINE  72 |                 if cached_mtime == signature:
LINE  73 |                     return list(cached_files)
LINE  74 | 
LINE  75 |     valid_files = []
LINE  76 | 
LINE  77 |     def _walk_error(err: OSError):
LINE  78 |         pass  # Ignore permission/access errors gracefully
LINE  79 | 
LINE  80 |     try:
LINE  81 |         for dirpath, dirnames, filenames in os.walk(abs_folder, onerror=_walk_error):
LINE  82 |             dirnames[:] = [d for d in dirnames if d not in excluded_set]
LINE  83 |             rel_dir = os.path.relpath(dirpath, abs_folder)
LINE  84 | 
LINE  85 |             for f in filenames:
LINE  86 |                 try:
LINE  87 |                     if is_file_allowed(f, allowed_extensions):
LINE  88 |                         rel_file = f if rel_dir == '.' else os.path.join(rel_dir, f)
LINE  89 |                         valid_files.append(rel_file.replace("\\", "/"))
LINE  90 |                 except Exception:
LINE  91 |                     continue
LINE  92 |     except Exception:
LINE  93 |         pass
LINE  94 | 
LINE  95 |     valid_files = sorted(valid_files)
LINE  96 | 
LINE  97 |     if use_cache:
LINE  98 |         with _cache_lock:
LINE  99 |             if len(_SCAN_CACHE) >= _MAX_CACHE_ENTRIES:
LINE 100 |                 try:
LINE 101 |                     first_key = next(iter(_SCAN_CACHE))
LINE 102 |                     del _SCAN_CACHE[first_key]
LINE 103 |                 except (StopIteration, KeyError):
LINE 104 |                     pass
LINE 105 |             _SCAN_CACHE[cache_key] = (folder_mtime, valid_files)
LINE 106 | 
LINE 107 |     return valid_files
```

==============================================================
FILE: .backup_search_perf/app/core/storage/database.py
==============================================================
```py
LINE   1 | """
LINE   2 | SQLite persistence layer for project nodes, metrics and dependencies (Phase 1).
LINE   3 | 
LINE   4 | This module is intentionally restricted to:
LINE   5 |   - Opening / creating the SQLite database.
LINE   6 |   - Initializing the schema.
LINE   7 |   - Executing queries and updates.
LINE   8 |   - Managing transactions.
LINE   9 |   - Providing the CRUD operations required for projects and nodes.
LINE  10 | 
LINE  11 | No Delta Scan or incremental change detection logic is implemented here.
LINE  12 | """
LINE  13 | import os
LINE  14 | import sqlite3
LINE  15 | from typing import Dict, List, Optional, Set, Tuple
LINE  16 | 
LINE  17 | 
LINE  18 | # ---------------------------------------------------------------------------
LINE  19 | # Path resolution
LINE  20 | # ---------------------------------------------------------------------------
LINE  21 | 
LINE  22 | def _find_project_root() -> Optional[str]:
LINE  23 |     """Walk up from this file to find the project root (contains main.py)."""
LINE  24 |     here = os.path.dirname(os.path.abspath(__file__))
LINE  25 |     candidate = os.path.abspath(os.path.join(here, "..", "..", ".."))
LINE  26 |     if os.path.isfile(os.path.join(candidate, "main.py")):
LINE  27 |         return candidate
LINE  28 |     return None
LINE  29 | 
LINE  30 | 
LINE  31 | def default_db_path() -> str:
LINE  32 |     """Resolve project_cache.db path.
LINE  33 | 
LINE  34 |     Prefer <project_root>/.cache/project_cache.db, fallback to
LINE  35 |     ~/.analyzer_app/project_cache.db when the project root cannot be resolved.
LINE  36 |     """
LINE  37 |     root = _find_project_root()
LINE  38 |     if root:
LINE  39 |         return os.path.join(root, ".cache", "project_cache.db")
LINE  40 |     home = os.path.expanduser("~")
LINE  41 |     return os.path.join(home, ".analyzer_app", "project_cache.db")
LINE  42 | 
LINE  43 | 
LINE  44 | # ---------------------------------------------------------------------------
LINE  45 | # Schema
LINE  46 | # ---------------------------------------------------------------------------
LINE  47 | 
LINE  48 | SCHEMA_STATEMENTS = [
LINE  49 |     """CREATE TABLE IF NOT EXISTS projects (
LINE  50 |         id INTEGER PRIMARY KEY AUTOINCREMENT,
LINE  51 |         path TEXT UNIQUE NOT NULL,
LINE  52 |         project_type TEXT,
LINE  53 |         framework TEXT,
LINE  54 |         last_scanned TIMESTAMP DEFAULT CURRENT_TIMESTAMP
LINE  55 |     )""",
LINE  56 |     """CREATE TABLE IF NOT EXISTS nodes (
LINE  57 |         id INTEGER PRIMARY KEY AUTOINCREMENT,
LINE  58 |         project_id INTEGER NOT NULL,
LINE  59 |         rel_path TEXT NOT NULL,
LINE  60 |         parent_path TEXT,
LINE  61 |         is_dir BOOLEAN NOT NULL,
LINE  62 |         mtime REAL NOT NULL,
LINE  63 |         lines_count INTEGER DEFAULT 0,
LINE  64 |         file_size INTEGER DEFAULT 0,
LINE  65 |         is_important BOOLEAN DEFAULT 0,
LINE  66 |         is_checked BOOLEAN DEFAULT 1,
LINE  67 |         FOREIGN KEY(project_id) REFERENCES projects(id) ON DELETE CASCADE,
LINE  68 |         UNIQUE(project_id, rel_path)
LINE  69 |     )""",
LINE  70 |     """CREATE TABLE IF NOT EXISTS node_dependencies (
LINE  71 |         id INTEGER PRIMARY KEY AUTOINCREMENT,
LINE  72 |         source_node_id INTEGER NOT NULL,
LINE  73 |         target_path TEXT NOT NULL,
LINE  74 |         FOREIGN KEY(source_node_id) REFERENCES nodes(id) ON DELETE CASCADE
LINE  75 |     )""",
LINE  76 |     "CREATE INDEX IF NOT EXISTS idx_nodes_rel_path ON nodes(project_id, rel_path)",
LINE  77 |     "CREATE INDEX IF NOT EXISTS idx_nodes_parent ON nodes(project_id, parent_path)",
LINE  78 | ]
LINE  79 | 
LINE  80 | 
LINE  81 | # ---------------------------------------------------------------------------
LINE  82 | # Database
LINE  83 | # ---------------------------------------------------------------------------
LINE  84 | 
LINE  85 | class Database:
LINE  86 |     """Thin SQLite wrapper for the project cache (Phase 1)."""
LINE  87 | 
LINE  88 |     def __init__(self, db_path: Optional[str] = None):
LINE  89 |         self.db_path = db_path or default_db_path()
LINE  90 |         os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
LINE  91 |         self._conn = sqlite3.connect(self.db_path, timeout=10.0)
LINE  92 |         self._conn.row_factory = sqlite3.Row
LINE  93 |         self._conn.execute("PRAGMA foreign_keys = ON")
LINE  94 |         self._conn.execute("PRAGMA journal_mode = WAL")
LINE  95 |         self._conn.execute("PRAGMA synchronous = NORMAL")
LINE  96 |         self._init_schema()
LINE  97 | 
LINE  98 |     def _init_schema(self) -> None:
LINE  99 |         with self._conn:
LINE 100 |             for stmt in SCHEMA_STATEMENTS:
LINE 101 |                 self._conn.execute(stmt)
LINE 102 | 
LINE 103 |     # ---------- projects ----------
LINE 104 | 
LINE 105 |     def get_or_create_project(self, path: str,
LINE 106 |                               project_type: Optional[str] = None,
LINE 107 |                               framework: Optional[str] = None) -> int:
LINE 108 |         cur = self._conn.cursor()
LINE 109 |         cur.execute("SELECT id FROM projects WHERE path = ?", (path,))
LINE 110 |         row = cur.fetchone()
LINE 111 |         if row:
LINE 112 |             return int(row["id"])
LINE 113 |         cur.execute(
LINE 114 |             "INSERT INTO projects (path, project_type, framework) VALUES (?, ?, ?)",
LINE 115 |             (path, project_type, framework),
LINE 116 |         )
LINE 117 |         self._conn.commit()
LINE 118 |         return int(cur.lastrowid)
LINE 119 | 
LINE 120 |     def get_project_by_path(self, path: str) -> Optional[Dict]:
LINE 121 |         cur = self._conn.cursor()
LINE 122 |         cur.execute("SELECT * FROM projects WHERE path = ?", (path,))
LINE 123 |         row = cur.fetchone()
LINE 124 |         return dict(row) if row else None
LINE 125 | 
LINE 126 |     def update_last_scanned(self, project_id: int) -> None:
LINE 127 |         with self._conn:
LINE 128 |             self._conn.execute(
LINE 129 |                 "UPDATE projects SET last_scanned = CURRENT_TIMESTAMP WHERE id = ?",
LINE 130 |                 (project_id,),
LINE 131 |             )
LINE 132 | 
LINE 133 |     def delete_project(self, path: str) -> None:
LINE 134 |         with self._conn:
LINE 135 |             self._conn.execute("DELETE FROM projects WHERE path = ?", (path,))
LINE 136 | 
LINE 137 |     # ---------- nodes ----------
LINE 138 | 
LINE 139 |     def replace_nodes(self, project_id: int, nodes: List[Dict]) -> None:
LINE 140 |         """Delete existing nodes for project and insert the new batch atomically."""
LINE 141 |         rows = [
LINE 142 |             (
LINE 143 |                 project_id,
LINE 144 |                 n["rel_path"],
LINE 145 |                 n.get("parent_path"),
LINE 146 |                 int(bool(n.get("is_dir", 0))),
LINE 147 |                 float(n.get("mtime", 0.0) or 0.0),
LINE 148 |                 int(n.get("lines_count", 0) or 0),
LINE 149 |                 int(n.get("file_size", 0) or 0),
LINE 150 |                 int(bool(n.get("is_important", 0))),
LINE 151 |                 int(bool(n.get("is_checked", 1))),
LINE 152 |             )
LINE 153 |             for n in nodes
LINE 154 |         ]
LINE 155 |         with self._conn:
LINE 156 |             self._conn.execute("DELETE FROM nodes WHERE project_id = ?", (project_id,))
LINE 157 |             if rows:
LINE 158 |                 self._conn.executemany(
LINE 159 |                     """INSERT INTO nodes
LINE 160 |                        (project_id, rel_path, parent_path, is_dir, mtime,
LINE 161 |                         lines_count, file_size, is_important, is_checked)
LINE 162 |                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
LINE 163 |                     rows,
LINE 164 |                 )
LINE 165 | 
LINE 166 |     def get_nodes(self, project_id: int) -> List[Dict]:
LINE 167 |         cur = self._conn.cursor()
LINE 168 |         cur.execute("SELECT * FROM nodes WHERE project_id = ?", (project_id,))
LINE 169 |         return [dict(r) for r in cur.fetchall()]
LINE 170 | 
LINE 171 |     def update_is_checked(self, project_id: int,
LINE 172 |                           rel_path: str, is_checked: bool) -> None:
LINE 173 |         with self._conn:
LINE 174 |             self._conn.execute(
LINE 175 |                 "UPDATE nodes SET is_checked = ? "
LINE 176 |                 "WHERE project_id = ? AND rel_path = ?",
LINE 177 |                 (int(bool(is_checked)), project_id, rel_path),
LINE 178 |             )
LINE 179 | 
LINE 180 |     def update_is_checked_batch(self, project_id: int,
LINE 181 |                                 updates: List[Tuple[str, bool]]) -> None:
LINE 182 |         rows = [(int(bool(c)), project_id, rp) for rp, c in updates]
LINE 183 |         if not rows:
LINE 184 |             return
LINE 185 |         with self._conn:
LINE 186 |             self._conn.executemany(
LINE 187 |                 "UPDATE nodes SET is_checked = ? "
LINE 188 |                 "WHERE project_id = ? AND rel_path = ?",
LINE 189 |                 rows,
LINE 190 |             )
LINE 191 | 
LINE 192 |     def load_checked_state(self, project_path: str) -> Optional[Set[str]]:
LINE 193 |         """Return the set of checked rel_paths (files only).
LINE 194 | 
LINE 195 |         Returns None when there is no persisted data for this project,
LINE 196 |         so the caller can distinguish "never saved" from "all unchecked".
LINE 197 |         """
LINE 198 |         cur = self._conn.cursor()
LINE 199 |         cur.execute("SELECT id FROM projects WHERE path = ?", (project_path,))
LINE 200 |         row = cur.fetchone()
LINE 201 |         if not row:
LINE 202 |             return None
LINE 203 |         project_id = int(row["id"])
LINE 204 |         cur.execute(
LINE 205 |             "SELECT rel_path, is_checked FROM nodes "
LINE 206 |             "WHERE project_id = ? AND is_dir = 0",
LINE 207 |             (project_id,),
LINE 208 |         )
LINE 209 |         rows = cur.fetchall()
LINE 210 |         if not rows:
LINE 211 |             return None
LINE 212 |         return {r["rel_path"] for r in rows if r["is_checked"]}
LINE 213 | 
LINE 214 |     def delete_nodes(self, project_id: int) -> None:
LINE 215 |         with self._conn:
LINE 216 |             self._conn.execute("DELETE FROM nodes WHERE project_id = ?", (project_id,))
LINE 217 | 
LINE 218 |     # ---------- dependencies ----------
LINE 219 | 
LINE 220 |     def save_dependencies_batch(self, project_id: int,
LINE 221 |                                 deps: List[Tuple[str, str]]) -> None:
LINE 222 |         """deps: list of (source_rel_path, target_path)."""
LINE 223 |         if not deps:
LINE 224 |             return
LINE 225 |         cur = self._conn.cursor()
LINE 226 |         cur.execute("SELECT id, rel_path FROM nodes WHERE project_id = ?", (project_id,))
LINE 227 |         id_map = {r["rel_path"]: int(r["id"]) for r in cur.fetchall()}
LINE 228 | 
LINE 229 |         rows = []
LINE 230 |         for src_rel, target in deps:
LINE 231 |             node_id = id_map.get(src_rel)
LINE 232 |             if node_id is None:
LINE 233 |                 continue
LINE 234 |             rows.append((node_id, target))
LINE 235 | 
LINE 236 |         with self._conn:
LINE 237 |             self._conn.execute(
LINE 238 |                 """DELETE FROM node_dependencies
LINE 239 |                    WHERE source_node_id IN
LINE 240 |                          (SELECT id FROM nodes WHERE project_id = ?)""",
LINE 241 |                 (project_id,),
LINE 242 |             )
LINE 243 |             if rows:
LINE 244 |                 self._conn.executemany(
LINE 245 |                     "INSERT INTO node_dependencies (source_node_id, target_path) "
LINE 246 |                     "VALUES (?, ?)",
LINE 247 |                     rows,
LINE 248 |                 )
LINE 249 | 
LINE 250 |     def get_dependencies(self, project_id: int) -> List[Dict]:
LINE 251 |         cur = self._conn.cursor()
LINE 252 |         cur.execute(
LINE 253 |             """SELECT n.rel_path AS source_path, d.target_path AS target_path
LINE 254 |                FROM node_dependencies d
LINE 255 |                JOIN nodes n ON n.id = d.source_node_id
LINE 256 |                WHERE n.project_id = ?""",
LINE 257 |             (project_id,),
LINE 258 |         )
LINE 259 |         return [dict(r) for r in cur.fetchall()]
LINE 260 | 
LINE 261 |     # === PHASE 2: DELTA SCAN ===
LINE 262 |     def load_nodes_map(self, project_path: str):
LINE 263 |         cur = self._conn.cursor()
LINE 264 |         cur.execute("SELECT id FROM projects WHERE path = ?", (project_path,))
LINE 265 |         row = cur.fetchone()
LINE 266 |         if not row:
LINE 267 |             return None
LINE 268 |         project_id = int(row["id"])
LINE 269 |         cur.execute(
LINE 270 |             "SELECT id, rel_path, parent_path, is_dir, mtime, lines_count, "
LINE 271 |             "file_size, is_important, is_checked FROM nodes WHERE project_id = ?",
LINE 272 |             (project_id,),
LINE 273 |         )
LINE 274 |         return {r["rel_path"]: dict(r) for r in cur.fetchall()}
LINE 275 | 
LINE 276 |     def apply_delta(self, project_id, to_insert, to_update,
LINE 277 |                     to_delete_paths, dep_pairs):
LINE 278 |         if to_delete_paths:
LINE 279 |             with self._conn:
LINE 280 |                 self._conn.executemany(
LINE 281 |                     "DELETE FROM nodes WHERE project_id = ? AND rel_path = ?",
LINE 282 |                     [(project_id, rp) for rp in to_delete_paths],
LINE 283 |                 )
LINE 284 |         if to_update:
LINE 285 |             with self._conn:
LINE 286 |                 self._conn.executemany(
LINE 287 |                     """UPDATE nodes SET mtime=?, lines_count=?, file_size=?,
LINE 288 |                                        is_important=?
LINE 289 |                        WHERE project_id=? AND rel_path=?""",
LINE 290 |                     [(n["mtime"], n["lines_count"], n["file_size"],
LINE 291 |                       int(bool(n.get("is_important", 0))),
LINE 292 |                       project_id, n["rel_path"]) for n in to_update],
LINE 293 |                 )
LINE 294 |         if to_insert:
LINE 295 |             with self._conn:
LINE 296 |                 self._conn.executemany(
LINE 297 |                     """INSERT INTO nodes
LINE 298 |                        (project_id, rel_path, parent_path, is_dir, mtime,
LINE 299 |                         lines_count, file_size, is_important, is_checked)
LINE 300 |                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
LINE 301 |                     [(project_id, n["rel_path"], n.get("parent_path"),
LINE 302 |                       int(bool(n.get("is_dir", 0))),
LINE 303 |                       float(n.get("mtime", 0.0)),
LINE 304 |                       int(n.get("lines_count", 0) or 0),
LINE 305 |                       int(n.get("file_size", 0) or 0),
LINE 306 |                       int(bool(n.get("is_important", 0))),
LINE 307 |                       int(bool(n.get("is_checked", 1))))
LINE 308 |                      for n in to_insert],
LINE 309 |                 )
LINE 310 |         if to_update or to_insert or to_delete_paths:
LINE 311 |             with self._conn:
LINE 312 |                 pairs = ([(project_id, n["rel_path"]) for n in to_update] +
LINE 313 |                          [(project_id, n["rel_path"]) for n in to_insert] +
LINE 314 |                          [(project_id, rp) for rp in to_delete_paths])
LINE 315 |                 self._conn.executemany(
LINE 316 |                     """DELETE FROM node_dependencies
LINE 317 |                        WHERE source_node_id IN
LINE 318 |                          (SELECT id FROM nodes WHERE project_id=? AND rel_path=?)""",
LINE 319 |                     pairs,
LINE 320 |                 )
LINE 321 |                 if dep_pairs:
LINE 322 |                     cur = self._conn.cursor()
LINE 323 |                     cur.execute(
LINE 324 |                         "SELECT id, rel_path FROM nodes WHERE project_id=?",
LINE 325 |                         (project_id,))
LINE 326 |                     id_map = {r["rel_path"]: int(r["id"])
LINE 327 |                               for r in cur.fetchall()}
LINE 328 |                     rows = [(id_map[s], t) for s, t in dep_pairs if s in id_map]
LINE 329 |                     if rows:
LINE 330 |                         self._conn.executemany(
LINE 331 |                             "INSERT INTO node_dependencies "
LINE 332 |                             "(source_node_id, target_path) VALUES (?, ?)",
LINE 333 |                             rows,
LINE 334 |                         )
LINE 335 |         self.update_last_scanned(project_id)
LINE 336 |     # === END PHASE 2 ===
LINE 337 | 
LINE 338 |     def close(self) -> None:
LINE 339 |         try:
LINE 340 |             self._conn.close()
LINE 341 |         except Exception:
LINE 342 |             pass
LINE 343 | 
LINE 344 | 
LINE 345 | # ---------------------------------------------------------------------------
LINE 346 | # Singleton accessor
LINE 347 | # ---------------------------------------------------------------------------
LINE 348 | 
LINE 349 | _db_singleton: Optional[Database] = None
LINE 350 | 
LINE 351 | 
LINE 352 | def get_database(db_path: Optional[str] = None) -> Database:
LINE 353 |     """Return the process-wide Database singleton."""
LINE 354 |     global _db_singleton
LINE 355 |     if _db_singleton is None or (db_path and db_path != _db_singleton.db_path):
LINE 356 |         _db_singleton = Database(db_path)
LINE 357 |     return _db_singleton
LINE 358 | 
LINE 359 | 
LINE 360 | def reset_database_singleton() -> None:
LINE 361 |     """For tests: close and drop the current singleton."""
LINE 362 |     global _db_singleton
LINE 363 |     if _db_singleton is not None:
LINE 364 |         _db_singleton.close()
LINE 365 |     _db_singleton = None
```

==============================================================
FILE: .backup_search_perf/app/gui/file_search_dialog.py
==============================================================
```py
LINE   1 | """File search dialog with per-file dependency analysis action and optimized performance."""
LINE   2 | import os
LINE   3 | import queue
LINE   4 | import threading
LINE   5 | import tkinter as tk
LINE   6 | from tkinter import ttk
LINE   7 | from typing import Callable, List, Optional, Set, Tuple
LINE   8 | 
LINE   9 | from app.core.project_scanner import scan_directory
LINE  10 | 
LINE  11 | C_BG = "#1e2330"
LINE  12 | C_PANEL = "#252b3b"
LINE  13 | C_BORDER = "#323a50"
LINE  14 | C_ACCENT = "#4f8ef7"
LINE  15 | C_TEXT = "#e8eaf0"
LINE  16 | C_TEXT2 = "#8b92a8"
LINE  17 | C_ENTRY = "#2a3148"
LINE  18 | 
LINE  19 | MAX_RENDER_LIMIT = 500
LINE  20 | BATCH_SIZE = 25              # 100 -> 25 : tandas más pequeñas, sin bloquear el mainloop
LINE  21 | DEBOUNCE_MS = 150
LINE  22 | LOADING_DELAY_MS = 200
LINE  23 | QUEUE_CHECK_MS = 20
LINE  24 | RENDER_BATCH_DELAY_MS = 15   # 1 -> 15 : cede el hilo entre tandas
LINE  25 | 
LINE  26 | 
LINE  27 | class FileSearchDialog(tk.Toplevel):
LINE  28 |     def __init__(
LINE  29 |         self,
LINE  30 |         parent: tk.Tk,
LINE  31 |         folder_path: str,
LINE  32 |         excluded_dirs: Optional[Set[str]] = None,
LINE  33 |         on_analyze_dependencies: Optional[Callable[[str], None]] = None,
LINE  34 |     ):
LINE  35 |         super().__init__(parent)
LINE  36 |         self.folder_path = folder_path
LINE  37 |         self.excluded_dirs = excluded_dirs or set()
LINE  38 |         self.on_analyze_dependencies = on_analyze_dependencies
LINE  39 | 
LINE  40 |         self.title("🔎 Buscador de archivos")
LINE  41 |         self.geometry("820x560")
LINE  42 |         self.minsize(640, 420)
LINE  43 |         self.configure(bg=C_BG)
LINE  44 | 
LINE  45 |         self.transient(parent)
LINE  46 |         self.grab_set()
LINE  47 | 
LINE  48 |         self.search_var = tk.StringVar()
LINE  49 |         self.all_files: List[str] = []
LINE  50 |         self._files_indexed: List[Tuple[str, str]] = []  # [(rel_path, rel_path_lower)]
LINE  51 | 
LINE  52 |         self._scan_id: int = 0
LINE  53 |         self._scan_queue: queue.Queue = queue.Queue()
LINE  54 | 
LINE  55 |         self._debounce_timer: Optional[str] = None
LINE  56 |         self._loading_timer: Optional[str] = None
LINE  57 |         self._render_timer: Optional[str] = None
LINE  58 |         self._poll_timer: Optional[str] = None
LINE  59 |         self._last_query: Optional[str] = None
LINE  60 | 
LINE  61 |         self.lbl_loading: Optional[tk.Label] = None
LINE  62 | 
LINE  63 |         self._build_header()
LINE  64 |         self._build_results()
LINE  65 | 
LINE  66 |         # Bind trace on search_var for debounced searching
LINE  67 |         self._trace_id = self.search_var.trace_add("write", self._on_query_trace)
LINE  68 | 
LINE  69 |         # Cleanup on destroy
LINE  70 |         self.bind("<Destroy>", self._on_destroy)
LINE  71 | 
LINE  72 |         self._load_files()
LINE  73 | 
LINE  74 |     def _build_header(self):
LINE  75 |         hdr = tk.Frame(self, bg=C_PANEL, padx=12, pady=10)
LINE  76 |         hdr.pack(fill=tk.X)
LINE  77 | 
LINE  78 |         header_top = tk.Frame(hdr, bg=C_PANEL)
LINE  79 |         header_top.pack(fill=tk.X)
LINE  80 | 
LINE  81 |         tk.Label(
LINE  82 |             header_top,
LINE  83 |             text="🔎 Buscar archivos del proyecto",
LINE  84 |             font=("Segoe UI", 12, "bold"),
LINE  85 |             bg=C_PANEL,
LINE  86 |             fg=C_TEXT,
LINE  87 |         ).pack(side=tk.LEFT, anchor="w")
LINE  88 | 
LINE  89 |         self.lbl_loading = tk.Label(
LINE  90 |             header_top,
LINE  91 |             text="⏳ Escaneando...",
LINE  92 |             font=("Segoe UI", 9, "italic"),
LINE  93 |             bg=C_PANEL,
LINE  94 |             fg=C_ACCENT,
LINE  95 |         )
LINE  96 | 
LINE  97 |         row = tk.Frame(hdr, bg=C_PANEL)
LINE  98 |         row.pack(fill=tk.X, pady=(6, 0))
LINE  99 | 
LINE 100 |         self.entry = ttk.Entry(row, textvariable=self.search_var, font=("Consolas", 9))
LINE 101 |         self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 6))
LINE 102 | 
LINE 103 |         ttk.Button(row, text="Buscar", command=self._force_refresh_results).pack(side=tk.LEFT)
LINE 104 |         ttk.Button(row, text="Limpiar", command=self._clear_search).pack(side=tk.LEFT, padx=(6, 0))
LINE 105 | 
LINE 106 |     def _build_results(self):
LINE 107 |         container = tk.Frame(
LINE 108 |             self,
LINE 109 |             bg=C_ENTRY,
LINE 110 |             bd=1,
LINE 111 |             relief="flat",
LINE 112 |             highlightbackground=C_BORDER,
LINE 113 |             highlightthickness=1,
LINE 114 |         )
LINE 115 |         container.pack(fill=tk.BOTH, expand=True, padx=12, pady=8)
LINE 116 | 
LINE 117 |         self.canvas = tk.Canvas(container, bg=C_ENTRY, bd=0, highlightthickness=0)
LINE 118 |         scrollbar = ttk.Scrollbar(container, orient=tk.VERTICAL, command=self.canvas.yview)
LINE 119 |         self.scroll_frame = tk.Frame(self.canvas, bg=C_ENTRY)
LINE 120 | 
LINE 121 |         self.scroll_frame.bind(
LINE 122 |             "<Configure>",
LINE 123 |             lambda _e: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
LINE 124 |         )
LINE 125 |         self.canvas_window = self.canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")
LINE 126 | 
LINE 127 |         def _on_resize(event):
LINE 128 |             if self.winfo_exists():
LINE 129 |                 self.canvas.itemconfig(self.canvas_window, width=event.width)
LINE 130 | 
LINE 131 |         self.canvas.bind("<Configure>", _on_resize)
LINE 132 | 
LINE 133 |         # Scoped mousewheel binding directly to canvas and scroll_frame
LINE 134 |         def _on_mousewheel(event):
LINE 135 |             if not self.winfo_exists():
LINE 136 |                 return
LINE 137 |             if event.delta:
LINE 138 |                 self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
LINE 139 |             elif event.num == 4:
LINE 140 |                 self.canvas.yview_scroll(-1, "units")
LINE 141 |             elif event.num == 5:
LINE 142 |                 self.canvas.yview_scroll(1, "units")
LINE 143 | 
LINE 144 |         self.canvas.bind("<MouseWheel>", _on_mousewheel)
LINE 145 |         self.canvas.bind("<Button-4>", _on_mousewheel)
LINE 146 |         self.canvas.bind("<Button-5>", _on_mousewheel)
LINE 147 |         self.scroll_frame.bind("<MouseWheel>", _on_mousewheel)
LINE 148 |         self.scroll_frame.bind("<Button-4>", _on_mousewheel)
LINE 149 |         self.scroll_frame.bind("<Button-5>", _on_mousewheel)
LINE 150 | 
LINE 151 |         self.canvas.configure(yscrollcommand=scrollbar.set)
LINE 152 |         scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
LINE 153 |         self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
LINE 154 | 
LINE 155 |     def _load_files(self, force_refresh: bool = False):
LINE 156 |         self._scan_id += 1
LINE 157 |         current_scan_id = self._scan_id
LINE 158 | 
LINE 159 |         # Schedule delayed loading indicator after 200ms
LINE 160 |         self._cancel_timer("_loading_timer")
LINE 161 |         self._loading_timer = self.after(
LINE 162 |             LOADING_DELAY_MS, lambda: self._show_loading(current_scan_id)
LINE 163 |         )
LINE 164 | 
LINE 165 |         # FIX: launch background worker: DB-first, os.walk fallback
LINE 166 |         threading.Thread(
LINE 167 |             target=self._async_scan_worker,
LINE 168 |             args=(
LINE 169 |                 current_scan_id,
LINE 170 |                 self.folder_path,
LINE 171 |                 self.excluded_dirs,
LINE 172 |                 self._scan_queue,
LINE 173 |                 force_refresh,
LINE 174 |             ),
LINE 175 |             daemon=True,
LINE 176 |         ).start()
LINE 177 | 
LINE 178 |         # Start queue polling loop on main GUI thread
LINE 179 |         self._schedule_queue_check()
LINE 180 | 
LINE 181 |     def _schedule_queue_check(self):
LINE 182 |         self._cancel_timer("_poll_timer")
LINE 183 |         if self.winfo_exists():
LINE 184 |             self._poll_timer = self.after(QUEUE_CHECK_MS, self._check_scan_queue)
LINE 185 | 
LINE 186 |     def _check_scan_queue(self):
LINE 187 |         if not self.winfo_exists():
LINE 188 |             return
LINE 189 | 
LINE 190 |         received = False
LINE 191 |         latest_files = None
LINE 192 |         source = None
LINE 193 | 
LINE 194 |         while True:
LINE 195 |             try:
LINE 196 |                 sid, files, src = self._scan_queue.get_nowait()
LINE 197 |                 if sid == self._scan_id:
LINE 198 |                     latest_files = files
LINE 199 |                     source = src
LINE 200 |                     received = True
LINE 201 |             except queue.Empty:
LINE 202 |                 break
LINE 203 | 
LINE 204 |         if received and latest_files is not None:
LINE 205 |             self._hide_loading()
LINE 206 |             self.all_files = latest_files
LINE 207 |             self._files_indexed = [(f, f.lower()) for f in latest_files]
LINE 208 |             if self.lbl_loading is not None and self.winfo_exists():
LINE 209 |                 tag = "caché DB" if source == "db" else "escaneo"
LINE 210 |                 self.lbl_loading.config(
LINE 211 |                     text=f"✓ {len(latest_files)} archivos ({tag})"
LINE 212 |                 )
LINE 213 |             self._refresh_results(force=True)
LINE 214 |         else:
LINE 215 |             # Reschedule queue check
LINE 216 |             self._schedule_queue_check()
LINE 217 | 
LINE 218 |     @staticmethod
LINE 219 |     def _async_scan_worker(
LINE 220 |         scan_id: int,
LINE 221 |         folder_path: str,
LINE 222 |         excluded_dirs: Set[str],
LINE 223 |         res_queue: queue.Queue,
LINE 224 |         force_refresh: bool = False,
LINE 225 |     ):
LINE 226 |         """Worker thread entry point: DB-first con fallback a os.walk.
LINE 227 | 
LINE 228 |         Estrategia:
LINE 229 |           1) Si !force_refresh, consultar SQLite (project_cache.db). ~1 ms.
LINE 230 |           2) Si la DB no tiene filas o el usuario forzó refresco, os.walk.
LINE 231 |         """
LINE 232 |         files: List[str] = []
LINE 233 |         source = "scan"
LINE 234 |         try:
LINE 235 |             from app.core.storage.database import get_database
LINE 236 | 
LINE 237 |             if not force_refresh:
LINE 238 |                 db = get_database()
LINE 239 |                 db_files, _last_scanned, exists = db.load_file_paths(folder_path)
LINE 240 |                 if exists and db_files:
LINE 241 |                     files = db_files
LINE 242 |                     source = "db"
LINE 243 | 
LINE 244 |             if not files:
LINE 245 |                 files = scan_directory(
LINE 246 |                     folder_path, excluded_dirs, allowed_extensions=None
LINE 247 |                 )
LINE 248 |                 source = "scan"
LINE 249 |         except Exception:
LINE 250 |             # Ante cualquier fallo, caer a escaneo directo
LINE 251 |             try:
LINE 252 |                 files = scan_directory(
LINE 253 |                     folder_path, excluded_dirs, allowed_extensions=None
LINE 254 |                 )
LINE 255 |             except Exception:
LINE 256 |                 files = []
LINE 257 |             source = "scan"
LINE 258 | 
LINE 259 |         res_queue.put((scan_id, files, source))
LINE 260 | 
LINE 261 |     def _show_loading(self, scan_id: int):
LINE 262 |         if not self.winfo_exists():
LINE 263 |             return
LINE 264 |         if scan_id == self._scan_id and self.lbl_loading:
LINE 265 |             self.lbl_loading.pack(side=tk.RIGHT)
LINE 266 | 
LINE 267 |     def _hide_loading(self):
LINE 268 |         self._cancel_timer("_loading_timer")
LINE 269 |         if self.winfo_exists() and self.lbl_loading:
LINE 270 |             self.lbl_loading.pack_forget()
LINE 271 | 
LINE 272 |     def _on_query_trace(self, *args):
LINE 273 |         self._cancel_timer("_debounce_timer")
LINE 274 |         self._debounce_timer = self.after(DEBOUNCE_MS, self._refresh_results)
LINE 275 | 
LINE 276 |     def _force_refresh_results(self):
LINE 277 |         self._cancel_timer("_debounce_timer")
LINE 278 |         self._refresh_results(force=True)
LINE 279 | 
LINE 280 |     def _clear_search(self):
LINE 281 |         self.search_var.set("")
LINE 282 |         self._force_refresh_results()
LINE 283 | 
LINE 284 |     def _cancel_timer(self, attr_name: str):
LINE 285 |         timer_id = getattr(self, attr_name, None)
LINE 286 |         if timer_id:
LINE 287 |             try:
LINE 288 |                 self.after_cancel(timer_id)
LINE 289 |             except Exception:
LINE 290 |                 pass
LINE 291 |             setattr(self, attr_name, None)
LINE 292 | 
LINE 293 |     def _cancel_render_task(self):
LINE 294 |         self._cancel_timer("_render_timer")
LINE 295 | 
LINE 296 |     def _refresh_results(self, force: bool = False):
LINE 297 |         if not self.winfo_exists():
LINE 298 |             return
LINE 299 | 
LINE 300 |         query = self.search_var.get().strip().lower()
LINE 301 |         if not force and self._last_query == query:
LINE 302 |             return
LINE 303 |         self._last_query = query
LINE 304 | 
LINE 305 |         self._cancel_render_task()
LINE 306 | 
LINE 307 |         # Clear existing scroll_frame children
LINE 308 |         for child in self.scroll_frame.winfo_children():
LINE 309 |             child.destroy()
LINE 310 | 
LINE 311 |         matches = [
LINE 312 |             rel for rel, rel_lower in self._files_indexed
LINE 313 |             if not query or query in rel_lower
LINE 314 |         ]
LINE 315 | 
LINE 316 |         if not matches:
LINE 317 |             tk.Label(
LINE 318 |                 self.scroll_frame,
LINE 319 |                 text="(Sin resultados)",
LINE 320 |                 font=("Segoe UI", 9, "italic"),
LINE 321 |                 bg=C_ENTRY,
LINE 322 |                 fg=C_TEXT2,
LINE 323 |             ).pack(anchor="w", padx=10, pady=10)
LINE 324 |             return
LINE 325 | 
LINE 326 |         total_matches = len(matches)
LINE 327 |         matches_to_render = matches[:MAX_RENDER_LIMIT]
LINE 328 | 
LINE 329 |         # FIX: incluso la primera tanda se agenda con after(0, ...) para no
LINE 330 |         # bloquear el hilo de la GUI dentro de _refresh_results.
LINE 331 |         self._render_timer = self.after(
LINE 332 |             0,
LINE 333 |             lambda: self._render_batch(matches_to_render, 0, total_matches),
LINE 334 |         )
LINE 335 | 
LINE 336 |     def _render_batch(self, matches_subset: List[str], start_idx: int, total_matches: int):
LINE 337 |         if not self.winfo_exists():
LINE 338 |             return
LINE 339 | 
LINE 340 |         end_idx = min(start_idx + BATCH_SIZE, len(matches_subset))
LINE 341 | 
LINE 342 |         for idx in range(start_idx, end_idx):
LINE 343 |             rel = matches_subset[idx]
LINE 344 |             row = tk.Frame(self.scroll_frame, bg=C_ENTRY, padx=8, pady=3)
LINE 345 |             row.pack(fill=tk.X)
LINE 346 | 
LINE 347 |             tk.Label(
LINE 348 |                 row,
LINE 349 |                 text=rel,
LINE 350 |                 font=("Consolas", 9),
LINE 351 |                 bg=C_ENTRY,
LINE 352 |                 fg=C_TEXT,
LINE 353 |                 anchor="w",
LINE 354 |             ).pack(side=tk.LEFT, fill=tk.X, expand=True)
LINE 355 | 
LINE 356 |             ttk.Button(
LINE 357 |                 row,
LINE 358 |                 text="🔗 Dependencias",
LINE 359 |                 command=lambda r=rel: self._analyze(r),
LINE 360 |             ).pack(side=tk.RIGHT)
LINE 361 | 
LINE 362 |         if end_idx < len(matches_subset):
LINE 363 |             # FIX: 15 ms en lugar de 1 ms para que el mainloop procese eventos
LINE 364 |             # (redibujado, teclado, ratón) entre tandas.
LINE 365 |             self._render_timer = self.after(
LINE 366 |                 RENDER_BATCH_DELAY_MS,
LINE 367 |                 lambda: self._render_batch(matches_subset, end_idx, total_matches),
LINE 368 |             )
LINE 369 |         else:
LINE 370 |             # Batch complete, display total matches summary if hard limit hit
LINE 371 |             if total_matches > MAX_RENDER_LIMIT:
LINE 372 |                 footer = tk.Frame(self.scroll_frame, bg=C_ENTRY, padx=8, pady=6)
LINE 373 |                 footer.pack(fill=tk.X)
LINE 374 |                 tk.Label(
LINE 375 |                     footer,
LINE 376 |                     text=f"Mostrando {MAX_RENDER_LIMIT} de {total_matches:,} resultados. Afina la búsqueda para ver más.",
LINE 377 |                     font=("Segoe UI", 8, "italic"),
LINE 378 |                     bg=C_ENTRY,
LINE 379 |                     fg=C_TEXT2,
LINE 380 |                 ).pack(anchor="w")
LINE 381 | 
LINE 382 |     def _analyze(self, rel_path: str):
LINE 383 |         if self.on_analyze_dependencies:
LINE 384 |             self.on_analyze_dependencies(rel_path)
LINE 385 | 
LINE 386 |     def _on_destroy(self, event):
LINE 387 |         if event.widget == self:
LINE 388 |             self._cancel_timer("_debounce_timer")
LINE 389 |             self._cancel_timer("_loading_timer")
LINE 390 |             self._cancel_timer("_render_timer")
LINE 391 |             self._cancel_timer("_poll_timer")
LINE 392 |             self._scan_id += 1  # invalidate any pending scan callbacks
LINE 393 |             try:
LINE 394 |                 self.search_var.trace_remove("write", self._trace_id)
LINE 395 |             except Exception:
LINE 396 |                 pass
```

==============================================================
FILE: README.md
==============================================================
```md
LINE  1 | # 📦 DeepSeek Code Packager (Modular Architecture)
LINE  2 | 
LINE  3 | **DeepSeek Code Packager** es una herramienta de escritorio desacoplada y modular diseñada para empaquetar código fuente de proyectos en documentos estructurados `.md` (Markdown) o `.txt` (Texto Plano), optimizada para subir y analizar manualmente en el chat web de **DeepSeek**, **ChatGPT** o **Claude**.
LINE  4 | 
LINE  5 | ---
LINE  6 | 
LINE  7 | ## 🏗️ Arquitectura del Proyecto
LINE  8 | 
LINE  9 | El proyecto sigue el principio de separación de responsabilidades (*Separation of Concerns*), manteniendo la lógica de escaneo, modelos de datos, lectura de archivos y generación de prompts completamente independientes de la interfaz gráfica.
LINE 10 | 
LINE 11 | ```
LINE 12 | deepseek_debugger/
LINE 13 | │
LINE 14 | ├── main.py                         # Punto de entrada principal
LINE 15 | ├── deepseek_gui.py                 # Wrapper ejecutable de compatibilidad
LINE 16 | │
LINE 17 | ├── app/                            # Módulo principal del sistema
LINE 18 | │   ├── __init__.py
LINE 19 | │   │
LINE 20 | │   ├── gui/                        # Capa de Interfaz Gráfica (Tkinter/ttk)
LINE 21 | │   │   ├── __init__.py
LINE 22 | │   │   ├── main_window.py          # Ventana principal y control de eventos
LINE 23 | │   │   ├── file_tree.py            # Componente de árbol con checkboxes
LINE 24 | │   │   └── dialogs.py              # Envoltorios de diálogos y alertas
LINE 25 | │   │
LINE 26 | │   ├── core/                       # Lógica central del sistema
LINE 27 | │   │   ├── __init__.py
LINE 28 | │   │   ├── project_scanner.py      # Escaneo recursivo de directorios
LINE 29 | │   │   ├── file_selector.py        # Gestor de estado de selección (1 carpeta + N archivos)
LINE 30 | │   │   ├── file_reader.py          # Lectura segura y numeración de líneas
LINE 31 | │   │   └── project_structure.py    # Generador de estructura en árbol ASCII
LINE 32 | │   │
LINE 33 | │   ├── generators/                 # Generadores de documentos
LINE 34 | │   │   ├── __init__.py
LINE 35 | │   │   ├── markdown_generator.py   # Formateador en formato Markdown (.md)
LINE 36 | │   │   ├── text_generator.py       # Formateador en texto plano (.txt)
LINE 37 | │   │   └── prompt_generator.py     # Orquestador principal de generación
LINE 38 | │   │
LINE 39 | │   ├── models/                     # Modelos de datos
LINE 40 | │   │   ├── __init__.py
LINE 41 | │   │   └── project.py              # Clases de datos (ProjectSelection, ExportConfig)
LINE 42 | │   │
LINE 43 | │   └── utils/                      # Utilidades del sistema
LINE 44 | │       ├── __init__.py
LINE 45 | │       ├── file_utils.py           # Lectura/Escritura I/O y portapapeles
LINE 46 | │       └── path_utils.py           # Resolución de rutas relativas y absolutas
LINE 47 | │
LINE 48 | ├── output/                         # Carpeta por defecto para exportaciones
LINE 49 | ├── requirements.txt
LINE 50 | ├── ejecutar.bat                    # Script de inicio silencioso en Windows
LINE 51 | ├── ejecutar_con_consola.bat        # Script de inicio en modo consola/debug
LINE 52 | └── README.md
LINE 53 | ```
LINE 54 | 
LINE 55 | ---
LINE 56 | 
LINE 57 | ## 🚀 Características Principales
LINE 58 | 
LINE 59 | 1. **Sin dependencias de API ni llamadas HTTP**: Funciona 100% offline y sin necesidad de claves de API.
LINE 60 | 2. **Selección Flexible de Archivos**:
LINE 61 |    - **Máximo 1 Carpeta de Proyecto**: Al seleccionar una nueva carpeta, se reemplaza la anterior.
LINE 62 |    - **N Archivos Individuales**: Permite sumar cualquier cantidad de archivos sueltos desde distintas ubicaciones.
LINE 63 |    - Soporta combinaciones: `1 Carpeta + N Archivos`, `Solo 1 Carpeta`, o `Solo N Archivos`.
LINE 64 | 3. **Exclusiones Dinámicas Configurables**:
LINE 65 |    - Omite por defecto `.git`, `node_modules`, `__pycache__`, `venv`, `.venv`, `dist`, `build`, `.idea`, `.vscode`.
LINE 66 |    - Permite editar la lista de directorios excluidos directamente desde la interfaz.
LINE 67 | 4. **Formateo para LLM Web Chat**:
LINE 68 |    - Agrega árbol de directorio de la carpeta del proyecto.
LINE 69 |    - Formatea el código con números de línea (`1 | código...`).
LINE 70 |    - Permite copiar directamente al portapapeles o guardar el documento generado en la carpeta `output/` o donde desees.
LINE 71 | 
LINE 72 | ---
LINE 73 | 
LINE 74 | ## 💻 Ejecución
LINE 75 | 
LINE 76 | ### Desde Scripts `.bat` (Windows):
LINE 77 | - Haz doble clic en `ejecutar.bat` (Modo Ventana).
LINE 78 | - O en `ejecutar_con_consola.bat` (Modo Consola / Debug).
LINE 79 | 
LINE 80 | ### Desde la Consola de Comandos (Python):
LINE 81 | ```bash
LINE 82 | python main.py
LINE 83 | ```
LINE 84 | O usando el wrapper de compatibilidad:
LINE 85 | ```bash
LINE 86 | python deepseek_gui.py
LINE 87 | ```
```

==============================================================
FILE: app/__init__.py
==============================================================
```py
LINE 1 | """App package initialization."""
LINE 2 | __version__ = "2.0.0"
```

==============================================================
FILE: app/core/__init__.py
==============================================================
```py
LINE  1 | """Core package initialization."""
LINE  2 | from app.core.project_scanner import scan_directory
LINE  3 | from app.core.file_selector import FileSelectorManager
LINE  4 | from app.core.file_reader import read_and_format_file
LINE  5 | from app.core.project_structure import build_folder_tree_str
LINE  6 | from app.core.dependency_detector import DependencyDetector, detect_project_dependencies
LINE  7 | from app.core.dependency_graph import DependencyResolver, DependencyNode
LINE  8 | 
LINE  9 | __all__ = [
LINE 10 |     "scan_directory",
LINE 11 |     "FileSelectorManager",
LINE 12 |     "read_and_format_file",
LINE 13 |     "build_folder_tree_str",
LINE 14 |     "DependencyDetector",
LINE 15 |     "detect_project_dependencies",
LINE 16 |     "DependencyResolver",
LINE 17 |     "DependencyNode",
LINE 18 | ]
```

==============================================================
FILE: app/core/dependency_detector.py
==============================================================
```py
LINE  1 | """
LINE  2 | Modular dependency and reference detector.
LINE  3 | Scans source code for imports, includes, and requires across multiple languages.
LINE  4 | Designed so full AST parsers can be easily plugged in per language later.
LINE  5 | """
LINE  6 | import os
LINE  7 | import re
LINE  8 | from typing import List, Dict
LINE  9 | 
LINE 10 | 
LINE 11 | class DependencyDetector:
LINE 12 |     def __init__(self):
LINE 13 |         # Regex patterns for fast, robust import detection
LINE 14 |         self._py_pattern = re.compile(r'^\s*(?:import\s+[\w\.]+|from\s+[\w\.]+\s+import\s+[\w\*\,]+)', re.MULTILINE)
LINE 15 |         self._js_pattern = re.compile(
LINE 16 |             r'^\s*(?:import\s+.*?from\s+[\'"].*?[\'"]|import\s*[\'"].*?[\'"]|const\s+.*?=\s*require\([\'"].*?[\'"]\)|require\([\'"].*?[\'"]\))', 
LINE 17 |             re.MULTILINE
LINE 18 |         )
LINE 19 |         self._php_pattern = re.compile(
LINE 20 |             r'^\s*(?:require(?:_once)?\s*\(?[\'"].*?[\'"]\)?|include(?:_once)?\s*\(?[\'"].*?[\'"]\)?|use\s+[\w\\]+;)', 
LINE 21 |             re.MULTILINE | re.IGNORECASE
LINE 22 |         )
LINE 23 |         self._cpp_pattern = re.compile(r'^\s*#include\s+[<"].*?[>"]', re.MULTILINE)
LINE 24 |         self._java_pattern = re.compile(r'^\s*(?:import\s+[\w\.\*]+;|using\s+[\w\.]+;)', re.MULTILINE)
LINE 25 | 
LINE 26 |     def detect_file_dependencies(self, rel_path: str, raw_content: str) -> List[str]:
LINE 27 |         """
LINE 28 |         Extracts import and dependency statements from source code content.
LINE 29 |         Returns a clean list of detected dependency strings.
LINE 30 |         """
LINE 31 |         if not raw_content or raw_content.startswith("[OMITIDO"):
LINE 32 |             return []
LINE 33 | 
LINE 34 |         ext = os.path.splitext(rel_path)[1].lower()
LINE 35 |         found = []
LINE 36 | 
LINE 37 |         if ext == ".py":
LINE 38 |             found = self._scan_pattern(self._py_pattern, raw_content)
LINE 39 |         elif ext in (".js", ".jsx", ".ts", ".tsx", ".vue"):
LINE 40 |             found = self._scan_pattern(self._js_pattern, raw_content)
LINE 41 |         elif ext == ".php":
LINE 42 |             found = self._scan_pattern(self._php_pattern, raw_content)
LINE 43 |         elif ext in (".c", ".cpp", ".h", ".hpp"):
LINE 44 |             found = self._scan_pattern(self._cpp_pattern, raw_content)
LINE 45 |         elif ext in (".java", ".cs"):
LINE 46 |             found = self._scan_pattern(self._java_pattern, raw_content)
LINE 47 | 
LINE 48 |         return found[:15]  # Limit to top 15 dependencies per file to keep context clean
LINE 49 | 
LINE 50 |     def _scan_pattern(self, pattern: re.Pattern, content: str) -> List[str]:
LINE 51 |         matches = pattern.findall(content)
LINE 52 |         results = []
LINE 53 |         for m in matches:
LINE 54 |             cleaned = ' '.join(m.strip().split())
LINE 55 |             if cleaned and cleaned not in results:
LINE 56 |                 results.append(cleaned)
LINE 57 |         return results
LINE 58 | 
LINE 59 | 
LINE 60 | def detect_project_dependencies(files_dict: Dict[str, str]) -> Dict[str, List[str]]:
LINE 61 |     """
LINE 62 |     Scans a dictionary mapping file rel_paths -> file contents.
LINE 63 |     Returns dict of rel_path -> list of detected dependency strings.
LINE 64 |     """
LINE 65 |     detector = DependencyDetector()
LINE 66 |     project_deps = {}
LINE 67 |     for rel_path, content in files_dict.items():
LINE 68 |         deps = detector.detect_file_dependencies(rel_path, content)
LINE 69 |         if deps:
LINE 70 |             project_deps[rel_path] = deps
LINE 71 |     return project_deps
```

==============================================================
FILE: app/core/dependency_graph.py
==============================================================
```py
LINE   1 | """
LINE   2 | Dependency graph/resolver for project files.
LINE   3 | Resolves imports/includes/requires to real project files and builds a dependency tree.
LINE   4 | """
LINE   5 | import os
LINE   6 | import re
LINE   7 | from dataclasses import dataclass, field
LINE   8 | from typing import List, Dict, Set, Optional
LINE   9 | 
LINE  10 | from app.core.dependency_detector import DependencyDetector
LINE  11 | from app.utils.file_utils import safe_read_file
LINE  12 | 
LINE  13 | 
LINE  14 | @dataclass
LINE  15 | class DependencyNode:
LINE  16 |     rel_path: str
LINE  17 |     depth: int
LINE  18 |     children: List["DependencyNode"] = field(default_factory=list)
LINE  19 |     is_cycle: bool = False
LINE  20 |     is_repeated: bool = False
LINE  21 |     external: Optional[str] = None
LINE  22 | 
LINE  23 | 
LINE  24 | class DependencyResolver:
LINE  25 |     def __init__(
LINE  26 |         self,
LINE  27 |         folder_path: str,
LINE  28 |         excluded_dirs: Optional[Set[str]] = None,
LINE  29 |         detector: Optional[DependencyDetector] = None,
LINE  30 |         max_read_bytes: int = 200_000,
LINE  31 |     ):
LINE  32 |         self.folder_path = os.path.abspath(folder_path)
LINE  33 |         self.excluded_dirs = set(excluded_dirs or [])
LINE  34 |         self.detector = detector or DependencyDetector()
LINE  35 |         self.max_read_bytes = max_read_bytes
LINE  36 | 
LINE  37 |         self._file_index: Dict[str, str] = {}
LINE  38 |         self._module_index: Dict[str, str] = {}
LINE  39 |         self._content_cache: Dict[str, str] = {}
LINE  40 |         self._deps_cache: Dict[str, List[str]] = {}
LINE  41 |         self._expanded: Set[str] = set()
LINE  42 | 
LINE  43 |         self._build_index()
LINE  44 | 
LINE  45 |     # ------------------------------------------------------------------
LINE  46 |     # Index
LINE  47 |     # ------------------------------------------------------------------
LINE  48 |     def _build_index(self) -> None:
LINE  49 |         if not self.folder_path or not os.path.isdir(self.folder_path):
LINE  50 |             return
LINE  51 | 
LINE  52 |         for dirpath, dirnames, filenames in os.walk(self.folder_path):
LINE  53 |             dirnames[:] = [d for d in dirnames if d not in self.excluded_dirs]
LINE  54 | 
LINE  55 |             for f in filenames:
LINE  56 |                 abs_p = os.path.join(dirpath, f)
LINE  57 |                 rel = os.path.relpath(abs_p, self.folder_path).replace("\\", "/")
LINE  58 |                 self._file_index[rel] = abs_p
LINE  59 | 
LINE  60 |                 if f.endswith(".py"):
LINE  61 |                     mod = rel[:-3].replace("/", ".")
LINE  62 |                     if mod.endswith(".__init__"):
LINE  63 |                         mod = mod[: -len(".__init__")]
LINE  64 |                     self._module_index[mod] = rel
LINE  65 | 
LINE  66 |     def _normalize(self, rel_path: str) -> str:
LINE  67 |         return rel_path.replace("\\", "/").lstrip("./")
LINE  68 | 
LINE  69 |     def _read(self, rel_path: str) -> str:
LINE  70 |         rel_path = self._normalize(rel_path)
LINE  71 |         if rel_path in self._content_cache:
LINE  72 |             return self._content_cache[rel_path]
LINE  73 | 
LINE  74 |         abs_p = self._file_index.get(rel_path)
LINE  75 |         if not abs_p or not os.path.isfile(abs_p):
LINE  76 |             self._content_cache[rel_path] = ""
LINE  77 |             return ""
LINE  78 | 
LINE  79 |         content = safe_read_file(abs_p, max_bytes=self.max_read_bytes)
LINE  80 |         self._content_cache[rel_path] = content
LINE  81 |         return content
LINE  82 | 
LINE  83 |     # ------------------------------------------------------------------
LINE  84 |     # Dependency detection
LINE  85 |     # ------------------------------------------------------------------
LINE  86 |     def get_dependencies(self, rel_path: str) -> List[str]:
LINE  87 |         rel_path = self._normalize(rel_path)
LINE  88 |         if rel_path in self._deps_cache:
LINE  89 |             return self._deps_cache[rel_path]
LINE  90 | 
LINE  91 |         content = self._read(rel_path)
LINE  92 |         if not content:
LINE  93 |             self._deps_cache[rel_path] = []
LINE  94 |             return []
LINE  95 | 
LINE  96 |         deps = self.detector.detect_file_dependencies(rel_path, content)
LINE  97 |         self._deps_cache[rel_path] = deps
LINE  98 |         return deps
LINE  99 | 
LINE 100 |     # ------------------------------------------------------------------
LINE 101 |     # Resolution
LINE 102 |     # ------------------------------------------------------------------
LINE 103 |     def resolve_dependency(self, source_rel_path: str, dep_string: str) -> List[str]:
LINE 104 |         source_rel_path = self._normalize(source_rel_path)
LINE 105 |         ext = os.path.splitext(source_rel_path)[1].lower()
LINE 106 | 
LINE 107 |         if ext == ".py":
LINE 108 |             candidates = self._resolve_python_dep(source_rel_path, dep_string)
LINE 109 |         elif ext in (".js", ".jsx", ".ts", ".tsx", ".vue", ".mjs", ".cjs"):
LINE 110 |             candidates = self._resolve_js_dep(source_rel_path, dep_string)
LINE 111 |         elif ext == ".php":
LINE 112 |             candidates = self._resolve_php_dep(source_rel_path, dep_string)
LINE 113 |         else:
LINE 114 |             candidates = self._resolve_by_basename(dep_string)
LINE 115 | 
LINE 116 |         result: List[str] = []
LINE 117 |         for c in candidates:
LINE 118 |             norm = self._normalize(c)
LINE 119 |             if norm in self._file_index and norm not in result:
LINE 120 |                 result.append(norm)
LINE 121 |         return result
LINE 122 | 
LINE 123 |     def _resolve_python_dep(self, source_rel: str, dep: str) -> List[str]:
LINE 124 |         dep = dep.strip()
LINE 125 | 
LINE 126 |         if dep.startswith("import "):
LINE 127 |             rest = dep[len("import "):].strip()
LINE 128 |             parts = [p.strip() for p in rest.split(",")]
LINE 129 |             result: List[str] = []
LINE 130 |             for p in parts:
LINE 131 |                 p = p.split(" as ")[0].strip()
LINE 132 |                 result.extend(self._module_to_rel(p))
LINE 133 |             return result
LINE 134 | 
LINE 135 |         if dep.startswith("from "):
LINE 136 |             rest = dep[len("from "):].strip()
LINE 137 |             if " import " not in rest:
LINE 138 |                 return []
LINE 139 | 
LINE 140 |             module, _names = rest.split(" import ", 1)
LINE 141 |             module = module.strip()
LINE 142 | 
LINE 143 |             if module.startswith("."):
LINE 144 |                 base_dir = os.path.dirname(source_rel)
LINE 145 |                 dots = len(module) - len(module.lstrip("."))
LINE 146 |                 module_name = module.lstrip(".")
LINE 147 | 
LINE 148 |                 up = max(0, dots - 1)
LINE 149 |                 parts = base_dir.split("/") if base_dir else []
LINE 150 |                 if up > 0:
LINE 151 |                     parts = parts[:-up] if up <= len(parts) else []
LINE 152 | 
LINE 153 |                 rel_dir = "/".join(parts)
LINE 154 |                 if module_name:
LINE 155 |                     mod_path = (rel_dir + "/" + module_name.replace(".", "/")) if rel_dir else module_name.replace(".", "/")
LINE 156 |                 else:
LINE 157 |                     mod_path = rel_dir
LINE 158 | 
LINE 159 |                 return self._path_to_rel_candidates(mod_path)
LINE 160 | 
LINE 161 |             return self._module_to_rel(module)
LINE 162 | 
LINE 163 |         return []
LINE 164 | 
LINE 165 |     def _module_to_rel(self, module: str) -> List[str]:
LINE 166 |         module = module.strip()
LINE 167 |         if not module:
LINE 168 |             return []
LINE 169 | 
LINE 170 |         if module in self._module_index:
LINE 171 |             return [self._module_index[module]]
LINE 172 | 
LINE 173 |         pkg_init = module + ".__init__"
LINE 174 |         if pkg_init in self._module_index:
LINE 175 |             return [self._module_index[pkg_init]]
LINE 176 | 
LINE 177 |         path_py = module.replace(".", "/") + ".py"
LINE 178 |         if path_py in self._file_index:
LINE 179 |             return [path_py]
LINE 180 | 
LINE 181 |         path_init = module.replace(".", "/") + "/__init__.py"
LINE 182 |         if path_init in self._file_index:
LINE 183 |             return [path_init]
LINE 184 | 
LINE 185 |         return []
LINE 186 | 
LINE 187 |     def _path_to_rel_candidates(self, base_path: str) -> List[str]:
LINE 188 |         base_path = self._normalize(base_path)
LINE 189 |         candidates = []
LINE 190 |         for cand in (
LINE 191 |             base_path + ".py",
LINE 192 |             base_path + "/__init__.py",
LINE 193 |             base_path,
LINE 194 |         ):
LINE 195 |             if cand in self._file_index:
LINE 196 |                 candidates.append(cand)
LINE 197 |         return candidates
LINE 198 | 
LINE 199 |     def _resolve_js_dep(self, source_rel: str, dep: str) -> List[str]:
LINE 200 |         m = re.search(r'[\'"]([^\'"]+)[\'"]', dep)
LINE 201 |         if not m:
LINE 202 |             return []
LINE 203 | 
LINE 204 |         raw = m.group(1).strip()
LINE 205 | 
LINE 206 |         # 1. Import relativo: "./x" o "../x"
LINE 207 |         if raw.startswith("."):
LINE 208 |             base_dir = os.path.dirname(source_rel)
LINE 209 |             target = os.path.normpath(os.path.join(base_dir, raw)).replace("\\", "/")
LINE 210 |             return self._js_candidates(target)
LINE 211 | 
LINE 212 |         # 2. Import con alias Quasar / Vue CLI / Vite
LINE 213 |         alias_targets = self._resolve_js_alias(raw)
LINE 214 |         for target in alias_targets:
LINE 215 |             hits = self._js_candidates(target)
LINE 216 |             if hits:
LINE 217 |                 return hits
LINE 218 | 
LINE 219 |         # 3. Fallback: probar como ruta relativa al folder_path
LINE 220 |         if "/" in raw:
LINE 221 |             hits = self._js_candidates(raw)
LINE 222 |             if hits:
LINE 223 |                 return hits
LINE 224 | 
LINE 225 |         # 4. Import externo (vue, quasar, axios, @quasar/app, ...)
LINE 226 |         return []
LINE 227 | 
LINE 228 |     def _resolve_js_alias(self, raw: str) -> List[str]:
LINE 229 |         """
LINE 230 |         Devuelve rutas base candidatas (relativas al folder_path) para un import
LINE 231 |         con alias. Se prueban varias variantes porque no sabemos si el usuario
LINE 232 |         seleccionó la raíz del proyecto (con src/) o el propio src/.
LINE 233 |         """
LINE 234 |         aliases = {
LINE 235 |             "src/":         ["src/", ""],
LINE 236 |             "@/":           ["src/", ""],
LINE 237 |             "app/":         ["src/", ""],
LINE 238 |             "components/":  ["src/components/", "components/"],
LINE 239 |             "layouts/":     ["src/layouts/",    "layouts/"],
LINE 240 |             "pages/":       ["src/pages/",      "pages/"],
LINE 241 |             "assets/":      ["src/assets/",     "assets/"],
LINE 242 |             "boot/":        ["src/boot/",       "boot/"],
LINE 243 |             "stores/":      ["src/stores/",     "stores/"],
LINE 244 |             "router/":      ["src/router/",     "router/"],
LINE 245 |             "composables/": ["src/composables/","composables/"],
LINE 246 |             "mixins/":      ["src/mixins/",     "mixins/"],
LINE 247 |             "directives/":  ["src/directives/", "directives/"],
LINE 248 |             "plugins/":     ["src/plugins/",    "plugins/"],
LINE 249 |             "services/":    ["src/services/",   "services/"],
LINE 250 |             "helpers/":     ["src/helpers/",    "helpers/"],
LINE 251 |         }
LINE 252 |         for alias, prefixes in aliases.items():
LINE 253 |             if raw.startswith(alias):
LINE 254 |                 rest = raw[len(alias):]
LINE 255 |                 return [p + rest for p in prefixes]
LINE 256 |         return []
LINE 257 | 
LINE 258 |     def _js_candidates(self, target: str) -> List[str]:
LINE 259 |         """Prueba target + extensiones y target/index.<ext> contra el índice."""
LINE 260 |         target = self._normalize(target)
LINE 261 |         out = []
LINE 262 |         for ext in ("", ".js", ".jsx", ".ts", ".tsx", ".vue", ".json", ".mjs", ".cjs"):
LINE 263 |             cand = target + ext
LINE 264 |             if cand in self._file_index:
LINE 265 |                 out.append(cand)
LINE 266 |         for ext in (".js", ".jsx", ".ts", ".tsx", ".vue"):
LINE 267 |             cand = target + "/index" + ext
LINE 268 |             if cand in self._file_index:
LINE 269 |                 out.append(cand)
LINE 270 |         seen = set()
LINE 271 |         result = []
LINE 272 |         for c in out:
LINE 273 |             if c not in seen:
LINE 274 |                 seen.add(c)
LINE 275 |                 result.append(c)
LINE 276 |         return result
LINE 277 | 
LINE 278 |     def _resolve_php_dep(self, source_rel: str, dep: str) -> List[str]:
LINE 279 |         m = re.search(r'[\'"]([^\'"]+)[\'"]', dep)
LINE 280 |         if not m:
LINE 281 |             return []
LINE 282 | 
LINE 283 |         raw = m.group(1)
LINE 284 | 
LINE 285 |         if raw.startswith("."):
LINE 286 |             base_dir = os.path.dirname(source_rel)
LINE 287 |             target = os.path.normpath(os.path.join(base_dir, raw)).replace("\\", "/")
LINE 288 |             for cand in (target, target + ".php"):
LINE 289 |                 if cand in self._file_index:
LINE 290 |                     return [cand]
LINE 291 |             return []
LINE 292 | 
LINE 293 |         for cand in (raw, raw + ".php"):
LINE 294 |             if cand in self._file_index:
LINE 295 |                 return [cand]
LINE 296 | 
LINE 297 |         return []
LINE 298 | 
LINE 299 |     def _resolve_by_basename(self, dep: str) -> List[str]:
LINE 300 |         base = os.path.basename(dep)
LINE 301 |         return [rel for rel in self._file_index if os.path.basename(rel) == base]
LINE 302 | 
LINE 303 |     # ------------------------------------------------------------------
LINE 304 |     # Tree building
LINE 305 |     # ------------------------------------------------------------------
LINE 306 |     def build_tree(self, root_rel_path: str, max_depth: int = 50) -> DependencyNode:
LINE 307 |         root_rel_path = self._normalize(root_rel_path)
LINE 308 |         self._expanded.clear()
LINE 309 |         return self._build_node(root_rel_path, depth=0, ancestors=set(), max_depth=max_depth)
LINE 310 | 
LINE 311 |     def _build_node(
LINE 312 |         self,
LINE 313 |         rel_path: str,
LINE 314 |         depth: int,
LINE 315 |         ancestors: Set[str],
LINE 316 |         max_depth: int,
LINE 317 |     ) -> DependencyNode:
LINE 318 |         node = DependencyNode(rel_path=rel_path, depth=depth)
LINE 319 | 
LINE 320 |         if depth >= max_depth:
LINE 321 |             return node
LINE 322 | 
LINE 323 |         if rel_path in ancestors:
LINE 324 |             node.is_cycle = True
LINE 325 |             return node
LINE 326 | 
LINE 327 |         if rel_path in self._expanded:
LINE 328 |             node.is_repeated = True
LINE 329 |             return node
LINE 330 | 
LINE 331 |         self._expanded.add(rel_path)
LINE 332 | 
LINE 333 |         new_ancestors = set(ancestors)
LINE 334 |         new_ancestors.add(rel_path)
LINE 335 | 
LINE 336 |         for dep in self.get_dependencies(rel_path):
LINE 337 |             for child_rel in self.resolve_dependency(rel_path, dep):
LINE 338 |                 child = self._build_node(
LINE 339 |                     child_rel,
LINE 340 |                     depth=depth + 1,
LINE 341 |                     ancestors=new_ancestors,
LINE 342 |                     max_depth=max_depth,
LINE 343 |                 )
LINE 344 |                 node.children.append(child)
LINE 345 | 
LINE 346 |         return node
```

==============================================================
FILE: app/core/file_reader.py
==============================================================
```py
LINE  1 | """File reading and code line numbering formatting core module."""
LINE  2 | import os
LINE  3 | from app.utils.file_utils import safe_read_file
LINE  4 | 
LINE  5 | 
LINE  6 | def format_line_numbers(content: str, add_line_numbers: bool = True) -> str:
LINE  7 |     """Adds formatted LINE X | line numbers to code string."""
LINE  8 |     if not add_line_numbers:
LINE  9 |         return content
LINE 10 |     lines = content.splitlines()
LINE 11 |     width = max(len(str(len(lines))), 1)
LINE 12 |     numbered = [f"LINE {i+1:{width}d} | {line}" for i, line in enumerate(lines)]
LINE 13 |     return '\n'.join(numbered)
LINE 14 | 
LINE 15 | 
LINE 16 | def read_and_format_file(abs_path: str, add_line_numbers: bool = True, max_file_size_mb: float = 1.0) -> str:
LINE 17 |     """Reads file content safely with size limit protection and formats line numbers."""
LINE 18 |     if not os.path.isfile(abs_path):
LINE 19 |         return f"[Archivo no encontrado: {abs_path}]"
LINE 20 |     
LINE 21 |     max_bytes = int(max_file_size_mb * 1024 * 1024)
LINE 22 |     raw_content = safe_read_file(abs_path, max_bytes=max_bytes)
LINE 23 |     return format_line_numbers(raw_content, add_line_numbers)
```

==============================================================
FILE: app/core/file_selector.py
==============================================================
```py
LINE  1 | """State manager for 1 folder + N individual files selections."""
LINE  2 | from typing import List, Set, Optional
LINE  3 | from app.models.project import ProjectSelection
LINE  4 | 
LINE  5 | 
LINE  6 | class FileSelectorManager:
LINE  7 |     def __init__(self):
LINE  8 |         self.selection = ProjectSelection()
LINE  9 | 
LINE 10 |     def set_folder(self, folder_path: str) -> None:
LINE 11 |         self.selection.set_folder(folder_path)
LINE 12 | 
LINE 13 |     def remove_folder(self) -> None:
LINE 14 |         self.selection.remove_folder()
LINE 15 | 
LINE 16 |     def set_checked_folder_files(self, rel_paths: List[str]) -> None:
LINE 17 |         self.selection.checked_folder_files = set(rel_paths)
LINE 18 | 
LINE 19 |     def add_individual_files(self, paths: List[str]) -> int:
LINE 20 |         return self.selection.add_individual_files(paths)
LINE 21 | 
LINE 22 |     def remove_individual_file(self, path: str) -> None:
LINE 23 |         self.selection.remove_individual_file(path)
LINE 24 | 
LINE 25 |     def clear_individual_files(self) -> None:
LINE 26 |         self.selection.clear_individual_files()
LINE 27 | 
LINE 28 |     def set_exclusions_from_string(self, exclusions_str: str) -> None:
LINE 29 |         parsed = {d.strip() for d in exclusions_str.split(',') if d.strip()}
LINE 30 |         self.selection.excluded_dirs = parsed
LINE 31 | 
LINE 32 |     def get_selection(self) -> ProjectSelection:
LINE 33 |         return self.selection
```

==============================================================
FILE: app/core/intelligent_context.py
==============================================================
```py
LINE   1 | """
LINE   2 | Intelligent Context Analyzer engine.
LINE   3 | Analyzes problem descriptions, matches filenames and content symbols,
LINE   4 | inspects dependency graphs, assigns priority levels (Critical, Important, Related, Secondary),
LINE   5 | and enforces size/file count constraints prioritizing high-relevance code files.
LINE   6 | """
LINE   7 | import os
LINE   8 | import re
LINE   9 | from dataclasses import dataclass
LINE  10 | from typing import List, Dict, Set, Tuple, Optional
LINE  11 | 
LINE  12 | from app.core.dependency_detector import DependencyDetector
LINE  13 | from app.utils.file_utils import get_file_size, is_binary_file, safe_read_file
LINE  14 | 
LINE  15 | 
LINE  16 | PRIORITY_CRITICAL = 1
LINE  17 | PRIORITY_IMPORTANT = 2
LINE  18 | PRIORITY_RELATED = 3
LINE  19 | PRIORITY_SECONDARY = 4
LINE  20 | 
LINE  21 | PRIORITY_META = {
LINE  22 |     PRIORITY_CRITICAL: {"icon": "🔴", "label": "Crítico", "desc": "Archivo directamente involucrado en el problema"},
LINE  23 |     PRIORITY_IMPORTANT: {"icon": "🟠", "label": "Importante", "desc": "Dependencia directa o flujo afectado"},
LINE  24 |     PRIORITY_RELATED: {"icon": "🟡", "label": "Relacionado", "desc": "Dependencia indirecta o configuración relevante"},
LINE  25 |     PRIORITY_SECONDARY: {"icon": "⚪", "label": "Secundario", "desc": "Archivo de contexto general o débilmente relacionado"},
LINE  26 | }
LINE  27 | 
LINE  28 | STOP_WORDS = {
LINE  29 |     "error", "failed", "failure", "issue", "bug", "problem", "cannot", "cant",
LINE  30 |     "unable", "to", "in", "the", "a", "an", "of", "and", "or", "for", "with",
LINE  31 |     "de", "del", "la", "el", "en", "con", "un", "una", "al", "para", "por", "que",
LINE  32 |     "no", "se", "es", "al", "los", "las", "su", "sus", "como"
LINE  33 | }
LINE  34 | 
LINE  35 | 
LINE  36 | @dataclass
LINE  37 | class PrioritizedFile:
LINE  38 |     rel_path: str
LINE  39 |     abs_path: str
LINE  40 |     priority_level: int  # 1: Critical, 2: Important, 3: Related, 4: Secondary
LINE  41 |     score: float
LINE  42 |     reason: str
LINE  43 |     size_bytes: int
LINE  44 |     is_selected: bool = True
LINE  45 | 
LINE  46 |     @property
LINE  47 |     def priority_icon(self) -> str:
LINE  48 |         return PRIORITY_META.get(self.priority_level, {}).get("icon", "⚪")
LINE  49 | 
LINE  50 |     @property
LINE  51 |     def priority_label(self) -> str:
LINE  52 |         return PRIORITY_META.get(self.priority_level, {}).get("label", "Secundario")
LINE  53 | 
LINE  54 | 
LINE  55 | class IntelligentContextAnalyzer:
LINE  56 |     """Analyzes problem description & project files to prioritize relevant context."""
LINE  57 | 
LINE  58 |     def __init__(self):
LINE  59 |         self.detector = DependencyDetector()
LINE  60 | 
LINE  61 |     def analyze(
LINE  62 |         self,
LINE  63 |         folder_path: str,
LINE  64 |         candidate_rel_files: List[str],
LINE  65 |         problem_desc: str,
LINE  66 |         max_file_size_mb: float = 2.0,
LINE  67 |         max_total_size_mb: float = 50.0,
LINE  68 |         max_files: int = 100,
LINE  69 |     ) -> List[PrioritizedFile]:
LINE  70 |         """
LINE  71 |         Main entry point for intelligent context analysis.
LINE  72 |         Returns list of PrioritizedFile sorted by priority (1 to 4) then score.
LINE  73 |         """
LINE  74 |         if not candidate_rel_files:
LINE  75 |             return []
LINE  76 | 
LINE  77 |         # Step 1: Tokenize & extract keywords from problem description
LINE  78 |         keywords, key_phrases = self._extract_keywords(problem_desc)
LINE  79 | 
LINE  80 |         # Map rel_path -> full abs_path & read content snippets for code files
LINE  81 |         file_map: Dict[str, str] = {}
LINE  82 |         content_map: Dict[str, str] = {}
LINE  83 |         size_map: Dict[str, int] = {}
LINE  84 | 
LINE  85 |         max_read_bytes = int(max_file_size_mb * 1024 * 1024)
LINE  86 | 
LINE  87 |         for rel_f in candidate_rel_files:
LINE  88 |             abs_f = rel_f if os.path.isabs(rel_f) else os.path.join(folder_path, rel_f) if folder_path else rel_f
LINE  89 |             file_map[rel_f] = abs_f
LINE  90 |             if os.path.isfile(abs_f) and not is_binary_file(abs_f):
LINE  91 |                 sz = get_file_size(abs_f)
LINE  92 |                 size_map[rel_f] = sz
LINE  93 |                 # Safe read snippet up to 64KB for symbol analysis
LINE  94 |                 content_map[rel_f] = safe_read_file(abs_f, max_bytes=min(sz, 65536))
LINE  95 |             else:
LINE  96 |                 size_map[rel_f] = 0
LINE  97 |                 content_map[rel_f] = ""
LINE  98 | 
LINE  99 |         # Step 2: Calculate initial keyword & filename relevance scores
LINE 100 |         scores: Dict[str, float] = {}
LINE 101 |         reasons: Dict[str, List[str]] = {}
LINE 102 |         direct_matches: Set[str] = set()
LINE 103 | 
LINE 104 |         for rel_f, content in content_map.items():
LINE 105 |             score, matched_reasons, is_direct = self._score_file(rel_f, content, keywords, key_phrases)
LINE 106 |             scores[rel_f] = score
LINE 107 |             reasons[rel_f] = matched_reasons
LINE 108 |             if is_direct:
LINE 109 |                 direct_matches.add(rel_f)
LINE 110 | 
LINE 111 |         # Step 3: Dependency Graph Analysis (imports & references)
LINE 112 |         # Build dependency adjacency lists (file -> imported modules/files)
LINE 113 |         deps_map: Dict[str, List[str]] = {}
LINE 114 |         for rel_f, content in content_map.items():
LINE 115 |             if content:
LINE 116 |                 deps_map[rel_f] = self.detector.detect_file_dependencies(rel_f, content)
LINE 117 |             else:
LINE 118 |                 deps_map[rel_f] = []
LINE 119 | 
LINE 120 |         # Find direct dependencies & reverse references of Critical (direct match) files
LINE 121 |         critical_files: Set[str] = set(direct_matches)
LINE 122 | 
LINE 123 |         # If no keywords matched directly, pick top-scoring files as critical if score > 0
LINE 124 |         if not critical_files and scores:
LINE 125 |             top_scored = [f for f, s in sorted(scores.items(), key=lambda x: x[1], reverse=True) if s > 0]
LINE 126 |             if top_scored:
LINE 127 |                 critical_files.update(top_scored[:3])
LINE 128 | 
LINE 129 |         important_files: Set[str] = set()
LINE 130 |         related_files: Set[str] = set()
LINE 131 | 
LINE 132 |         # Step 4: Propagate priorities via dependency graph
LINE 133 |         # Direct dependencies or importers of Critical files become Important
LINE 134 |         for rel_f in candidate_rel_files:
LINE 135 |             if rel_f in critical_files:
LINE 136 |                 continue
LINE 137 | 
LINE 138 |             # Check if rel_f imports any critical file or is imported by any critical file
LINE 139 |             is_important = False
LINE 140 |             for crit_f in critical_files:
LINE 141 |                 crit_stem = os.path.splitext(os.path.basename(crit_f))[0].lower()
LINE 142 |                 f_stem = os.path.splitext(os.path.basename(rel_f))[0].lower()
LINE 143 | 
LINE 144 |                 # Does rel_f reference crit_f?
LINE 145 |                 for dep in deps_map.get(rel_f, []):
LINE 146 |                     if crit_stem in dep.lower() or crit_f.lower() in dep.lower():
LINE 147 |                         is_important = True
LINE 148 |                         reasons[rel_f].append(f"Importa el archivo crítico {crit_f}")
LINE 149 |                         break
LINE 150 | 
LINE 151 |                 # Does crit_f reference rel_f?
LINE 152 |                 if not is_important:
LINE 153 |                     for dep in deps_map.get(crit_f, []):
LINE 154 |                         if f_stem in dep.lower() or rel_f.lower() in dep.lower():
LINE 155 |                             is_important = True
LINE 156 |                             reasons[rel_f].append(f"Utilizado por el archivo crítico {crit_f}")
LINE 157 |                             break
LINE 158 | 
LINE 159 |                 if is_important:
LINE 160 |                     break
LINE 161 | 
LINE 162 |             if is_important:
LINE 163 |                 important_files.add(rel_f)
LINE 164 | 
LINE 165 |         # Database/Config files or indirect dependencies become Related
LINE 166 |         config_patterns = re.compile(r'(?:config|database|db|setting|env|router|index|main|app|server)', re.IGNORECASE)
LINE 167 |         for rel_f in candidate_rel_files:
LINE 168 |             if rel_f in critical_files or rel_f in important_files:
LINE 169 |                 continue
LINE 170 | 
LINE 171 |             base_name = os.path.basename(rel_f)
LINE 172 |             if config_patterns.search(base_name):
LINE 173 |                 related_files.add(rel_f)
LINE 174 |                 reasons[rel_f].append("Archivo de configuración / entrada global")
LINE 175 |             elif scores.get(rel_f, 0) > 0:
LINE 176 |                 related_files.add(rel_f)
LINE 177 |                 reasons[rel_f].append("Coincidencia parcial de términos")
LINE 178 | 
LINE 179 |         # Step 5: Assign priority levels
LINE 180 |         result_files: List[PrioritizedFile] = []
LINE 181 | 
LINE 182 |         for rel_f in candidate_rel_files:
LINE 183 |             if rel_f in critical_files:
LINE 184 |                 level = PRIORITY_CRITICAL
LINE 185 |                 reason_str = "; ".join(reasons.get(rel_f, [])) or "Coincidencia directa con el problema"
LINE 186 |             elif rel_f in important_files:
LINE 187 |                 level = PRIORITY_IMPORTANT
LINE 188 |                 reason_str = "; ".join(reasons.get(rel_f, [])) or "Dependencia directa de un archivo crítico"
LINE 189 |             elif rel_f in related_files:
LINE 190 |                 level = PRIORITY_RELATED
LINE 191 |                 reason_str = "; ".join(reasons.get(rel_f, [])) or "Configuración o coincidencia indirecta"
LINE 192 |             else:
LINE 193 |                 level = PRIORITY_SECONDARY
LINE 194 |                 reason_str = "Archivo secundario del proyecto"
LINE 195 | 
LINE 196 |             result_files.append(PrioritizedFile(
LINE 197 |                 rel_path=rel_f,
LINE 198 |                 abs_path=file_map[rel_f],
LINE 199 |                 priority_level=level,
LINE 200 |                 score=scores.get(rel_f, 0.0),
LINE 201 |                 reason=reason_str,
LINE 202 |                 size_bytes=size_map.get(rel_f, 0),
LINE 203 |                 is_selected=True
LINE 204 |             ))
LINE 205 | 
LINE 206 |         # Step 6: Sort by priority (1 to 4) then score desc
LINE 207 |         result_files.sort(key=lambda x: (x.priority_level, -x.score, x.rel_path))
LINE 208 | 
LINE 209 |         # Step 7: Apply context limits (auto-uncheck files that exceed max limits)
LINE 210 |         self.apply_limits(
LINE 211 |             result_files,
LINE 212 |             max_files=max_files,
LINE 213 |             max_file_size_mb=max_file_size_mb,
LINE 214 |             max_total_size_mb=max_total_size_mb
LINE 215 |         )
LINE 216 | 
LINE 217 |         return result_files
LINE 218 | 
LINE 219 |     def apply_limits(
LINE 220 |         self,
LINE 221 |         files: List[PrioritizedFile],
LINE 222 |         max_files: int,
LINE 223 |         max_file_size_mb: float,
LINE 224 |         max_total_size_mb: float,
LINE 225 |     ) -> None:
LINE 226 |         """
LINE 227 |         Enforces MAX_FILES, MAX_FILE_SIZE, and MAX_TOTAL_SIZE limits.
LINE 228 |         Higher-priority files are checked first; exceeding files have is_selected = False.
LINE 229 |         """
LINE 230 |         cumulative_bytes = 0
LINE 231 |         selected_count = 0
LINE 232 |         max_file_bytes = int(max_file_size_mb * 1024 * 1024)
LINE 233 |         max_total_bytes = int(max_total_size_mb * 1024 * 1024)
LINE 234 | 
LINE 235 |         for pf in files:
LINE 236 |             # Skip if oversize single file
LINE 237 |             if pf.size_bytes > max_file_bytes:
LINE 238 |                 pf.is_selected = False
LINE 239 |                 pf.reason += f" [Omitido: excede {max_file_size_mb:g}MB por archivo]"
LINE 240 |                 continue
LINE 241 | 
LINE 242 |             # Skip if max_files limit reached
LINE 243 |             if selected_count >= max_files:
LINE 244 |                 pf.is_selected = False
LINE 245 |                 pf.reason += f" [Omitido: excede límite de {max_files} archivos]"
LINE 246 |                 continue
LINE 247 | 
LINE 248 |             # Skip if max_total_bytes reached
LINE 249 |             if cumulative_bytes + pf.size_bytes > max_total_bytes:
LINE 250 |                 pf.is_selected = False
LINE 251 |                 pf.reason += f" [Omitido: excede límite de tamaño acumulado ({max_total_size_mb:g}MB)]"
LINE 252 |                 continue
LINE 253 | 
LINE 254 |             # Include file
LINE 255 |             pf.is_selected = True
LINE 256 |             selected_count += 1
LINE 257 |             cumulative_bytes += pf.size_bytes
LINE 258 | 
LINE 259 |     def _extract_keywords(self, problem_desc: str) -> Tuple[Set[str], List[str]]:
LINE 260 |         """Extracts individual tokens and key multi-word phrases from problem description."""
LINE 261 |         if not problem_desc:
LINE 262 |             return set(), []
LINE 263 | 
LINE 264 |         cleaned = problem_desc.lower()
LINE 265 |         # Find snake_case or camelCase or slash paths or dot notations
LINE 266 |         tokens = re.findall(r'[a-z0-9_\-\.\/]+', cleaned)
LINE 267 | 
LINE 268 |         keywords: Set[str] = set()
LINE 269 |         key_phrases: List[str] = []
LINE 270 | 
LINE 271 |         for t in tokens:
LINE 272 |             # Split slash paths or dot notation
LINE 273 |             sub_parts = re.split(r'[\/\.]', t)
LINE 274 |             for part in sub_parts:
LINE 275 |                 part_clean = part.strip("_ -")
LINE 276 |                 if len(part_clean) > 2 and part_clean not in STOP_WORDS:
LINE 277 |                     keywords.add(part_clean)
LINE 278 |                     # Add singular/plural variants
LINE 279 |                     if part_clean.endswith("s") and len(part_clean) > 3:
LINE 280 |                         keywords.add(part_clean[:-1])
LINE 281 |                     elif not part_clean.endswith("s"):
LINE 282 |                         keywords.add(part_clean + "s")
LINE 283 |                     
LINE 284 |                     # Add verb stem variants (-ing, -ed, -tion)
LINE 285 |                     if part_clean.endswith("ing") and len(part_clean) > 5:
LINE 286 |                         keywords.add(part_clean[:-3])
LINE 287 |                         keywords.add(part_clean[:-3] + "e")
LINE 288 |                     elif part_clean.endswith("ed") and len(part_clean) > 4:
LINE 289 |                         keywords.add(part_clean[:-2])
LINE 290 |                         keywords.add(part_clean[:-1])
LINE 291 |                     elif part_clean.endswith("tion") and len(part_clean) > 6:
LINE 292 |                         keywords.add(part_clean[:-4] + "te")
LINE 293 | 
LINE 294 |         # Multi-word phrase extraction (e.g. "creating users" -> "create user", "users")
LINE 295 |         words = [w for w in re.findall(r'[a-z0-9]+', cleaned) if len(w) > 2 and w not in STOP_WORDS]
LINE 296 |         for i in range(len(words) - 1):
LINE 297 |             key_phrases.append(f"{words[i]} {words[i+1]}")
LINE 298 | 
LINE 299 |         return keywords, key_phrases
LINE 300 | 
LINE 301 |     def _score_file(
LINE 302 |         self,
LINE 303 |         rel_path: str,
LINE 304 |         content: str,
LINE 305 |         keywords: Set[str],
LINE 306 |         key_phrases: List[str]
LINE 307 |     ) -> Tuple[float, List[str], bool]:
LINE 308 |         """Calculates relevance score and determines if file is a direct match."""
LINE 309 |         score = 0.0
LINE 310 |         reasons: List[str] = []
LINE 311 |         is_direct = False
LINE 312 | 
LINE 313 |         norm_rel = rel_path.lower().replace("\\", "/")
LINE 314 |         file_stem = os.path.splitext(os.path.basename(norm_rel))[0]
LINE 315 |         path_parts = norm_rel.split("/")
LINE 316 | 
LINE 317 |         # 1. Filename & Path Matching
LINE 318 |         for kw in keywords:
LINE 319 |             if kw in file_stem:
LINE 320 |                 score += 15.0
LINE 321 |                 reasons.append(f"Nombre de archivo contiene '{kw}'")
LINE 322 |                 is_direct = True
LINE 323 |             elif any(kw in part for part in path_parts):
LINE 324 |                 score += 8.0
LINE 325 |                 reasons.append(f"Ruta de archivo contiene '{kw}'")
LINE 326 |                 is_direct = True
LINE 327 | 
LINE 328 |         # 2. Content Symbol & Keyword Matching
LINE 329 |         if content:
LINE 330 |             lower_content = content.lower()
LINE 331 |             for kw in keywords:
LINE 332 |                 occurrences = lower_content.count(kw)
LINE 333 |                 if occurrences > 0:
LINE 334 |                     score += min(occurrences * 1.5, 10.0)
LINE 335 |                     # Check if keyword is part of class or function definition
LINE 336 |                     if re.search(r'(?:class|def|function|interface|type|struct)\s+\w*' + re.escape(kw), lower_content):
LINE 337 |                         score += 12.0
LINE 338 |                         is_direct = True
LINE 339 |                         reasons.append(f"Define símbolo/clase/función '{kw}'")
LINE 340 |                     elif not any(kw in r for r in reasons):
LINE 341 |                         reasons.append(f"Contenido menciona '{kw}' ({occurrences} veces)")
LINE 342 | 
LINE 343 |             for phrase in key_phrases:
LINE 344 |                 if phrase in lower_content:
LINE 345 |                     score += 5.0
LINE 346 | 
LINE 347 |         return score, reasons, is_direct
```

==============================================================
FILE: app/core/project_analyzer.py
==============================================================
```py
LINE   1 | """
LINE   2 | Project Analyzer module.
LINE   3 | Performs automatic scanning and analysis of project codebases:
LINE   4 | - Primary language & framework detection (Python, JS/TS, Vue, Quasar, PHP/Laravel, Go, Rust, Java, etc.)
LINE   5 | - Package manager detection (pip, npm, yarn, pnpm, bun, composer, cargo, etc.)
LINE   6 | - Configuration files and entry points detection
LINE   7 | - File and line counts, extensions breakdown
LINE   8 | - Dependency detection (manifests + DependencyDetector source scan)
LINE   9 | - Important files, large files (with warnings), and recently modified files
LINE  10 | - Project structure tree representation
LINE  11 | - Recommended file selection for context generation
LINE  12 | - Excluded directories detection
LINE  13 | """
LINE  14 | import os
LINE  15 | import re
LINE  16 | import json
LINE  17 | from collections import Counter
LINE  18 | from dataclasses import dataclass, field
LINE  19 | from datetime import datetime
LINE  20 | from typing import Dict, List, Set, Any, Optional, Tuple
LINE  21 | 
LINE  22 | from app.core.dependency_detector import DependencyDetector
LINE  23 | from app.core.project_structure import build_folder_tree_str
LINE  24 | from app.models.project import DEFAULT_ALLOWED_EXTENSIONS
LINE  25 | from app.utils.file_utils import (
LINE  26 |     is_binary_file, get_file_size, safe_read_file, format_bytes, KNOWN_BINARY_EXTENSIONS
LINE  27 | )
LINE  28 | 
LINE  29 | # Common directories that should be excluded
LINE  30 | DEFAULT_ANALYZER_EXCLUSIONS = {
LINE  31 |     ".git", "node_modules", "__pycache__", "venv", ".venv",
LINE  32 |     "dist", "build", ".idea", ".vscode", "vendor", ".quasar", ".github", "public"
LINE  33 | }
LINE  34 | 
LINE  35 | # Known entry point filenames
LINE  36 | KNOWN_ENTRY_POINTS = {
LINE  37 |     "main.py", "app.py", "manage.py", "wsgi.py", "asgi.py", "run.py", "server.py", "index.py", "__main__.py",
LINE  38 |     "main.js", "main.ts", "index.js", "index.ts", "app.js", "app.ts", "server.js",
LINE  39 |     "artisan", "server.php", "index.php", "main.go", "lib.rs", "main.rs"
LINE  40 | }
LINE  41 | 
LINE  42 | # Known configuration filenames
LINE  43 | KNOWN_CONFIG_FILES = {
LINE  44 |     "package.json", "package-lock.json", "composer.json", "composer.lock",
LINE  45 |     "tsconfig.json", "jsconfig.json", "quasar.config.js", "quasar.config.ts",
LINE  46 |     "quasar.conf.js", "vite.config.js", "vite.config.ts", "webpack.config.js",
LINE  47 |     "babel.config.js", "tailwind.config.js", "postcss.config.js", "eslint.config.js",
LINE  48 |     "requirements.txt", "pyproject.toml", "setup.py", "setup.cfg", "Pipfile", "Pipfile.lock",
LINE  49 |     "Dockerfile", "docker-compose.yml", "docker-compose.yaml",
LINE  50 |     ".env.example", ".env", "Makefile", "Cargo.toml", "Cargo.lock", "go.mod", "go.sum",
LINE  51 |     "pom.xml", "build.gradle", "build.gradle.kts"
LINE  52 | }
LINE  53 | 
LINE  54 | # Extension to language mapping
LINE  55 | EXTENSION_LANGUAGE_MAP = {
LINE  56 |     ".py": "Python",
LINE  57 |     ".js": "JavaScript",
LINE  58 |     ".mjs": "JavaScript",
LINE  59 |     ".cjs": "JavaScript",
LINE  60 |     ".jsx": "JavaScript (React)",
LINE  61 |     ".ts": "TypeScript",
LINE  62 |     ".tsx": "TypeScript (React)",
LINE  63 |     ".vue": "Vue.js",
LINE  64 |     ".php": "PHP",
LINE  65 |     ".html": "HTML",
LINE  66 |     ".htm": "HTML",
LINE  67 |     ".css": "CSS",
LINE  68 |     ".scss": "SCSS",
LINE  69 |     ".sass": "Sass",
LINE  70 |     ".less": "Less",
LINE  71 |     ".java": "Java",
LINE  72 |     ".c": "C",
LINE  73 |     ".cpp": "C++",
LINE  74 |     ".cc": "C++",
LINE  75 |     ".h": "C/C++ Header",
LINE  76 |     ".hpp": "C++ Header",
LINE  77 |     ".cs": "C#",
LINE  78 |     ".go": "Go",
LINE  79 |     ".rs": "Rust",
LINE  80 |     ".rb": "Ruby",
LINE  81 |     ".sql": "SQL",
LINE  82 |     ".sh": "Shell Script",
LINE  83 |     ".bat": "Batch",
LINE  84 |     ".cmd": "Batch",
LINE  85 |     ".ps1": "PowerShell",
LINE  86 |     ".json": "JSON",
LINE  87 |     ".yaml": "YAML",
LINE  88 |     ".yml": "YAML",
LINE  89 |     ".xml": "XML",
LINE  90 | }
LINE  91 | 
LINE  92 | 
LINE  93 | @dataclass
LINE  94 | class FileMetric:
LINE  95 |     rel_path: str
LINE  96 |     abs_path: str
LINE  97 |     size_bytes: int
LINE  98 |     lines: int
LINE  99 |     mtime: float
LINE 100 |     mtime_formatted: str
LINE 101 |     is_entry_point: bool = False
LINE 102 |     is_config: bool = False
LINE 103 |     is_important: bool = False
LINE 104 |     score: int = 0
LINE 105 | 
LINE 106 | 
LINE 107 | @dataclass
LINE 108 | class ProjectAnalysisResult:
LINE 109 |     folder_path: str
LINE 110 |     project_name: str
LINE 111 |     primary_language: str
LINE 112 |     language_summary: Dict[str, Dict[str, int]]  # lang -> {files: N, lines: N}
LINE 113 |     framework: str
LINE 114 |     framework_details: str
LINE 115 |     package_manager: str
LINE 116 |     config_files: List[str]
LINE 117 |     entry_points: List[str]
LINE 118 |     total_files: int
LINE 119 |     total_lines: int
LINE 120 |     total_size_bytes: int
LINE 121 |     extension_counts: Dict[str, int]
LINE 122 |     extension_lines: Dict[str, int]
LINE 123 |     manifest_dependencies: Dict[str, List[str]]
LINE 124 |     code_dependencies: Dict[str, List[str]]
LINE 125 |     important_files: List[str]
LINE 126 |     large_files: List[Dict[str, Any]]
LINE 127 |     recently_modified_files: List[Dict[str, Any]]
LINE 128 |     project_structure_tree: str
LINE 129 |     recommended_files: List[str]
LINE 130 |     excluded_dirs_found: List[str]
LINE 131 |     configured_exclusions: List[str]
LINE 132 | 
LINE 133 |     def to_formatted_report(self) -> str:
LINE 134 |         """Produces a human-readable structured text report."""
LINE 135 |         lines = [
LINE 136 |             "==============================================================",
LINE 137 |             f"REPORTE DE ANÁLISIS AUTOMÁTICO: {self.project_name}",
LINE 138 |             "==============================================================",
LINE 139 |             f"• Carpeta: {self.folder_path}",
LINE 140 |             f"• Lenguaje principal: {self.primary_language}",
LINE 141 |             f"• Framework: {self.framework}" + (f" ({self.framework_details})" if self.framework_details else ""),
LINE 142 |             f"• Gestor de paquetes: {self.package_manager}",
LINE 143 |             f"• Total archivos analizados: {self.total_files}",
LINE 144 |             f"• Total líneas de código: {self.total_lines:,}",
LINE 145 |             f"• Tamaño total: {format_bytes(self.total_size_bytes)}",
LINE 146 |             "",
LINE 147 |             "--------------------------------------------------------------",
LINE 148 |             "RESUMEN POR EXTENSIÓN",
LINE 149 |             "--------------------------------------------------------------",
LINE 150 |         ]
LINE 151 |         for ext, count in sorted(self.extension_counts.items(), key=lambda x: x[1], reverse=True):
LINE 152 |             ext_lines = self.extension_lines.get(ext, 0)
LINE 153 |             lines.append(f"  {ext}: {count} archivo(s) · {ext_lines:,} líneas")
LINE 154 | 
LINE 155 |         lines.extend([
LINE 156 |             "",
LINE 157 |             "--------------------------------------------------------------",
LINE 158 |             "ENTRY POINTS Y ARCHIVOS DE CONFIGURACIÓN",
LINE 159 |             "--------------------------------------------------------------",
LINE 160 |         ])
LINE 161 |         if self.entry_points:
LINE 162 |             lines.append("Entry points:")
LINE 163 |             for ep in self.entry_points:
LINE 164 |                 lines.append(f"  ⚡ {ep}")
LINE 165 |         else:
LINE 166 |             lines.append("Entry points: (No detectados en raíz)")
LINE 167 | 
LINE 168 |         if self.config_files:
LINE 169 |             lines.append("Configuración:")
LINE 170 |             for cf in self.config_files:
LINE 171 |                 lines.append(f"  ⚙️ {cf}")
LINE 172 | 
LINE 173 |         if self.manifest_dependencies:
LINE 174 |             lines.extend([
LINE 175 |                 "",
LINE 176 |                 "--------------------------------------------------------------",
LINE 177 |                 "DEPENDENCIAS DETECTADAS (MANIFIESTOS)",
LINE 178 |                 "--------------------------------------------------------------",
LINE 179 |             ])
LINE 180 |             for manifest, deps in self.manifest_dependencies.items():
LINE 181 |                 lines.append(f"• {manifest}:")
LINE 182 |                 for d in deps[:20]:
LINE 183 |                     lines.append(f"  - {d}")
LINE 184 |                 if len(deps) > 20:
LINE 185 |                     lines.append(f"  ... (+{len(deps) - 20} dependencias más)")
LINE 186 | 
LINE 187 |         if self.large_files:
LINE 188 |             lines.extend([
LINE 189 |                 "",
LINE 190 |                 "--------------------------------------------------------------",
LINE 191 |                 "ARCHIVOS MÁS GRANDES",
LINE 192 |                 "--------------------------------------------------------------",
LINE 193 |             ])
LINE 194 |             for f in self.large_files[:5]:
LINE 195 |                 warn = " ⚠️ [GRANDE]" if f.get("is_warning") else ""
LINE 196 |                 lines.append(f"  • {f['path']} ({format_bytes(f['size_bytes'])}, {f['lines']:,} líneas){warn}")
LINE 197 | 
LINE 198 |         if self.recently_modified_files:
LINE 199 |             lines.extend([
LINE 200 |                 "",
LINE 201 |                 "--------------------------------------------------------------",
LINE 202 |                 "ARCHIVOS MODIFICADOS RECIENTEMENTE",
LINE 203 |                 "--------------------------------------------------------------",
LINE 204 |             ])
LINE 205 |             for f in self.recently_modified_files[:5]:
LINE 206 |                 lines.append(f"  • {f['path']} ({f['mtime_formatted']})")
LINE 207 | 
LINE 208 |         lines.extend([
LINE 209 |             "",
LINE 210 |             "--------------------------------------------------------------",
LINE 211 |             "ARCHIVOS RECOMENDADOS PARA ANALIZAR",
LINE 212 |             "--------------------------------------------------------------",
LINE 213 |         ])
LINE 214 |         for rf in self.recommended_files:
LINE 215 |             lines.append(f"  ✓ {rf}")
LINE 216 | 
LINE 217 |         lines.extend([
LINE 218 |             "",
LINE 219 |             "--------------------------------------------------------------",
LINE 220 |             "DIRECTORIOS EXCLUIDOS",
LINE 221 |             "--------------------------------------------------------------",
LINE 222 |         ])
LINE 223 |         for ex in self.configured_exclusions:
LINE 224 |             present = " (presente en proyecto)" if ex in self.excluded_dirs_found else ""
LINE 225 |             lines.append(f"  ⚠️ {ex}/{present}")
LINE 226 | 
LINE 227 |         return "\n".join(lines)
LINE 228 | 
LINE 229 | 
LINE 230 | class ProjectAnalyzer:
LINE 231 |     """Analyzes a project directory to detect architecture, tech stack, dependencies and key files."""
LINE 232 | 
LINE 233 |     def __init__(self, excluded_dirs: Optional[Set[str]] = None, allowed_extensions: Optional[Set[str]] = None):
LINE 234 |         self.excluded_dirs = set(excluded_dirs) if excluded_dirs is not None else set(DEFAULT_ANALYZER_EXCLUSIONS)
LINE 235 |         self.allowed_extensions = set(allowed_extensions) if allowed_extensions is not None else set(DEFAULT_ALLOWED_EXTENSIONS)
LINE 236 |         self.dep_detector = DependencyDetector()
LINE 237 | 
LINE 238 |     def analyze(self, folder_path: str, max_file_size_mb: float = 2.0) -> ProjectAnalysisResult:
LINE 239 |         """Executes full scan and analysis on the given folder."""
LINE 240 |         folder_path = os.path.abspath(folder_path)
LINE 241 |         project_name = os.path.basename(folder_path) or folder_path
LINE 242 | 
LINE 243 |         files_metrics: List[FileMetric] = []
LINE 244 |         extension_counts: Counter = Counter()
LINE 245 |         extension_lines: Counter = Counter()
LINE 246 |         languages_stats: Dict[str, Dict[str, int]] = {}
LINE 247 |         excluded_dirs_found: Set[str] = set()
LINE 248 | 
LINE 249 |         total_files = 0
LINE 250 |         total_lines = 0
LINE 251 |         total_size = 0
LINE 252 |         max_file_bytes = int(max_file_size_mb * 1024 * 1024)
LINE 253 | 
LINE 254 |         # 1. Recursive scan with exclusions
LINE 255 |         for dirpath, dirnames, filenames in os.walk(folder_path):
LINE 256 |             # Check for excluded directories present in the project
LINE 257 |             for d in list(dirnames):
LINE 258 |                 if d in self.excluded_dirs:
LINE 259 |                     excluded_dirs_found.add(d)
LINE 260 |             # Exclude directories
LINE 261 |             dirnames[:] = [d for d in sorted(dirnames) if d not in self.excluded_dirs]
LINE 262 |             rel_dir = os.path.relpath(dirpath, folder_path)
LINE 263 | 
LINE 264 |             for f in sorted(filenames):
LINE 265 |                 rel_file = f if rel_dir == "." else os.path.join(rel_dir, f)
LINE 266 |                 full_path = os.path.join(dirpath, f)
LINE 267 |                 ext = os.path.splitext(f)[1].lower()
LINE 268 | 
LINE 269 |                 if self.allowed_extensions and ext not in self.allowed_extensions and f not in KNOWN_CONFIG_FILES and f not in KNOWN_ENTRY_POINTS:
LINE 270 |                     continue
LINE 271 | 
LINE 272 |                 if is_binary_file(full_path):
LINE 273 |                     continue
LINE 274 | 
LINE 275 |                 try:
LINE 276 |                     stat = os.stat(full_path)
LINE 277 |                     size_bytes = stat.st_size
LINE 278 |                     mtime = stat.st_mtime
LINE 279 |                     mtime_fmt = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M:%S")
LINE 280 |                 except Exception:
LINE 281 |                     size_bytes = 0
LINE 282 |                     mtime = 0
LINE 283 |                     mtime_fmt = "Desconocido"
LINE 284 | 
LINE 285 |                 # Count lines safely
LINE 286 |                 lines_in_file = 0
LINE 287 |                 if size_bytes <= max_file_bytes:
LINE 288 |                     try:
LINE 289 |                         with open(full_path, "r", encoding="utf-8", errors="ignore") as fp:
LINE 290 |                             lines_in_file = sum(1 for _ in fp)
LINE 291 |                     except Exception:
LINE 292 |                         lines_in_file = 0
LINE 293 | 
LINE 294 |                 norm_rel = rel_file.replace("\\", "/")
LINE 295 |                 is_ep = self._is_entry_point(norm_rel)
LINE 296 |                 is_cfg = self._is_config_file(norm_rel)
LINE 297 |                 is_imp = self._is_important_file(norm_rel, is_ep, is_cfg)
LINE 298 | 
LINE 299 |                 metric = FileMetric(
LINE 300 |                     rel_path=norm_rel,
LINE 301 |                     abs_path=full_path,
LINE 302 |                     size_bytes=size_bytes,
LINE 303 |                     lines=lines_in_file,
LINE 304 |                     mtime=mtime,
LINE 305 |                     mtime_formatted=mtime_fmt,
LINE 306 |                     is_entry_point=is_ep,
LINE 307 |                     is_config=is_cfg,
LINE 308 |                     is_important=is_imp,
LINE 309 |                 )
LINE 310 |                 files_metrics.append(metric)
LINE 311 | 
LINE 312 |                 total_files += 1
LINE 313 |                 total_lines += lines_in_file
LINE 314 |                 total_size += size_bytes
LINE 315 |                 extension_counts[ext or "[sin extensión]"] += 1
LINE 316 |                 extension_lines[ext or "[sin extensión]"] += lines_in_file
LINE 317 | 
LINE 318 |                 lang = EXTENSION_LANGUAGE_MAP.get(ext, "Otro")
LINE 319 |                 if lang not in languages_stats:
LINE 320 |                     languages_stats[lang] = {"files": 0, "lines": 0}
LINE 321 |                 languages_stats[lang]["files"] += 1
LINE 322 |                 languages_stats[lang]["lines"] += lines_in_file
LINE 323 | 
LINE 324 |         # 2. Determine Primary Language
LINE 325 |         primary_lang = "Desconocido"
LINE 326 |         if languages_stats:
LINE 327 |             code_langs = {k: v for k, v in languages_stats.items() if k not in ("JSON", "YAML", "XML", "Otro")}
LINE 328 |             if code_langs:
LINE 329 |                 primary_lang = max(code_langs.items(), key=lambda item: (item[1]["lines"], item[1]["files"]))[0]
LINE 330 |             else:
LINE 331 |                 primary_lang = max(languages_stats.items(), key=lambda item: (item[1]["lines"], item[1]["files"]))[0]
LINE 332 | 
LINE 333 |         # 3. Detect Package Manager & Manifest Dependencies
LINE 334 |         pkg_manager, manifest_deps = self._detect_package_manager_and_manifests(folder_path)
LINE 335 | 
LINE 336 |         # 4. Detect Framework
LINE 337 |         framework, framework_details = self._detect_framework(folder_path, primary_lang, manifest_deps, files_metrics)
LINE 338 | 
LINE 339 |         # 5. Detect Code Dependencies using DependencyDetector
LINE 340 |         code_dependencies = self._scan_code_dependencies(files_metrics)
LINE 341 | 
LINE 342 |         # 6. Categorize Files: Entry points, Configs, Important, Large, Recent
LINE 343 |         entry_points = [m.rel_path for m in files_metrics if m.is_entry_point]
LINE 344 |         config_files = [m.rel_path for m in files_metrics if m.is_config]
LINE 345 |         important_files = [m.rel_path for m in files_metrics if m.is_important]
LINE 346 | 
LINE 347 |         # Large files (top 10 by size)
LINE 348 |         large_files = []
LINE 349 |         for m in sorted(files_metrics, key=lambda x: x.size_bytes, reverse=True)[:10]:
LINE 350 |             large_files.append({
LINE 351 |                 "path": m.rel_path,
LINE 352 |                 "size_bytes": m.size_bytes,
LINE 353 |                 "lines": m.lines,
LINE 354 |                 "is_warning": m.size_bytes > max_file_bytes or m.size_bytes > 1_048_576
LINE 355 |             })
LINE 356 | 
LINE 357 |         # Recently modified files (top 10 by mtime)
LINE 358 |         recent_files = []
LINE 359 |         for m in sorted(files_metrics, key=lambda x: x.mtime, reverse=True)[:10]:
LINE 360 |             recent_files.append({
LINE 361 |                 "path": m.rel_path,
LINE 362 |                 "mtime": m.mtime,
LINE 363 |                 "mtime_formatted": m.mtime_formatted,
LINE 364 |                 "size_bytes": m.size_bytes,
LINE 365 |                 "lines": m.lines
LINE 366 |             })
LINE 367 | 
LINE 368 |         # 7. Generate Recommended File Selection
LINE 369 |         recommended_files = self._select_recommended_files(files_metrics, entry_points, config_files, recent_files)
LINE 370 | 
LINE 371 |         # 8. Project Structure Tree
LINE 372 |         structure_tree = build_folder_tree_str(
LINE 373 |             folder_path,
LINE 374 |             [m.rel_path for m in files_metrics if not m.rel_path.count("/") > 2],
LINE 375 |             self.excluded_dirs
LINE 376 |         )
LINE 377 | 
LINE 378 |         return ProjectAnalysisResult(
LINE 379 |             folder_path=folder_path,
LINE 380 |             project_name=project_name,
LINE 381 |             primary_language=primary_lang,
LINE 382 |             language_summary=languages_stats,
LINE 383 |             framework=framework,
LINE 384 |             framework_details=framework_details,
LINE 385 |             package_manager=pkg_manager,
LINE 386 |             config_files=sorted(config_files),
LINE 387 |             entry_points=sorted(entry_points),
LINE 388 |             total_files=total_files,
LINE 389 |             total_lines=total_lines,
LINE 390 |             total_size_bytes=total_size,
LINE 391 |             extension_counts=dict(extension_counts),
LINE 392 |             extension_lines=dict(extension_lines),
LINE 393 |             manifest_dependencies=manifest_deps,
LINE 394 |             code_dependencies=code_dependencies,
LINE 395 |             important_files=sorted(important_files),
LINE 396 |             large_files=large_files,
LINE 397 |             recently_modified_files=recent_files,
LINE 398 |             project_structure_tree=structure_tree,
LINE 399 |             recommended_files=recommended_files,
LINE 400 |             excluded_dirs_found=sorted(list(excluded_dirs_found)),
LINE 401 |             configured_exclusions=sorted(list(self.excluded_dirs)),
LINE 402 |         )
LINE 403 | 
LINE 404 |     # === PERSISTENCE: PHASE1 (persist_result) ===
LINE 405 |     def persist_result(self, result) -> None:
LINE 406 |         """Persist a ProjectAnalysisResult to the SQLite cache (Phase 1).
LINE 407 | 
LINE 408 |         This method is additive and does not modify the existing analyze()
LINE 409 |         pipeline, its return type, or FileMetric structure.
LINE 410 |         """
LINE 411 |         try:
LINE 412 |             from app.core.storage.database import get_database
LINE 413 |         except Exception:
LINE 414 |             return
LINE 415 | 
LINE 416 |         folder = getattr(result, "folder_path", None)
LINE 417 |         if not folder or not os.path.isdir(folder):
LINE 418 |             return
LINE 419 | 
LINE 420 |         try:
LINE 421 |             db = get_database()
LINE 422 |         except Exception:
LINE 423 |             return
LINE 424 | 
LINE 425 |         project_id = db.get_or_create_project(
LINE 426 |             path=folder,
LINE 427 |             project_type=getattr(result, "primary_language", None),
LINE 428 |             framework=getattr(result, "framework", None),
LINE 429 |         )
LINE 430 | 
LINE 431 |         # Preserve previously persisted is_checked state
LINE 432 |         existing_checked = db.load_checked_state(folder)
LINE 433 | 
LINE 434 |         important = set(getattr(result, "important_files", []) or [])
LINE 435 |         nodes = []
LINE 436 | 
LINE 437 |         for dirpath, dirnames, filenames in os.walk(folder):
LINE 438 |             dirnames[:] = [d for d in dirnames if d not in self.excluded_dirs]
LINE 439 |             rel_dir = os.path.relpath(dirpath, folder)
LINE 440 | 
LINE 441 |             if rel_dir != ".":
LINE 442 |                 rel_norm = rel_dir.replace("\\", "/")
LINE 443 |                 parent = os.path.dirname(rel_norm).replace("\\", "/") or None
LINE 444 |                 try:
LINE 445 |                     mtime = float(os.stat(dirpath).st_mtime)
LINE 446 |                 except Exception:
LINE 447 |                     mtime = 0.0
LINE 448 |                 nodes.append({
LINE 449 |                     "rel_path": rel_norm,
LINE 450 |                     "parent_path": parent,
LINE 451 |                     "is_dir": 1,
LINE 452 |                     "mtime": mtime,
LINE 453 |                     "lines_count": 0,
LINE 454 |                     "file_size": 0,
LINE 455 |                     "is_important": 0,
LINE 456 |                     "is_checked": 0,
LINE 457 |                 })
LINE 458 | 
LINE 459 |             for f in filenames:
LINE 460 |                 full = os.path.join(dirpath, f)
LINE 461 |                 if is_binary_file(full):
LINE 462 |                     continue
LINE 463 |                 rel_file = f if rel_dir == "." else os.path.join(rel_dir, f)
LINE 464 |                 rel_file = rel_file.replace("\\", "/")
LINE 465 |                 try:
LINE 466 |                     st = os.stat(full)
LINE 467 |                     mtime = float(st.st_mtime)
LINE 468 |                     size = int(st.st_size)
LINE 469 |                 except Exception:
LINE 470 |                     mtime = 0.0
LINE 471 |                     size = 0
LINE 472 |                 parent = os.path.dirname(rel_file).replace("\\", "/") or None
LINE 473 | 
LINE 474 |                 if existing_checked is None:
LINE 475 |                     is_checked = 1
LINE 476 |                 else:
LINE 477 |                     is_checked = 1 if rel_file in existing_checked else 0
LINE 478 | 
LINE 479 |                 nodes.append({
LINE 480 |                     "rel_path": rel_file,
LINE 481 |                     "parent_path": parent,
LINE 482 |                     "is_dir": 0,
LINE 483 |                     "mtime": mtime,
LINE 484 |                     "lines_count": 0,
LINE 485 |                     "file_size": size,
LINE 486 |                     "is_important": 1 if rel_file in important else 0,
LINE 487 |                     "is_checked": is_checked,
LINE 488 |                 })
LINE 489 | 
LINE 490 |         try:
LINE 491 |             db.replace_nodes(project_id, nodes)
LINE 492 | 
LINE 493 |             dep_pairs = []
LINE 494 |             code_deps = getattr(result, "code_dependencies", {}) or {}
LINE 495 |             for rel_path, deps in code_deps.items():
LINE 496 |                 for d in deps:
LINE 497 |                     dep_pairs.append((rel_path, d))
LINE 498 |             db.save_dependencies_batch(project_id, dep_pairs)
LINE 499 | 
LINE 500 |             db.update_last_scanned(project_id)
LINE 501 |         except Exception:
LINE 502 |             pass
LINE 503 |     # === END PERSISTENCE: PHASE1 (persist_result) ===
LINE 504 | 
LINE 505 |     def _is_entry_point(self, rel_path: str) -> bool:
LINE 506 |         """Determines if relative path is an entry point."""
LINE 507 |         base = os.path.basename(rel_path).lower()
LINE 508 |         if base in KNOWN_ENTRY_POINTS:
LINE 509 |             parts = rel_path.split("/")
LINE 510 |             if len(parts) <= 3:
LINE 511 |                 return True
LINE 512 |         if rel_path in ("src/main.js", "src/main.ts", "src/index.js", "src/index.ts", "src/App.vue", "src/App.tsx"):
LINE 513 |             return True
LINE 514 |         if rel_path.endswith("artisan") or rel_path.endswith("public/index.php"):
LINE 515 |             return True
LINE 516 |         return False
LINE 517 | 
LINE 518 |     def _is_config_file(self, rel_path: str) -> bool:
LINE 519 |         """Determines if file is a configuration file."""
LINE 520 |         base = os.path.basename(rel_path).lower()
LINE 521 |         if base in KNOWN_CONFIG_FILES:
LINE 522 |             return True
LINE 523 |         if base.startswith(".env") or base.endswith(".config.js") or base.endswith(".config.ts"):
LINE 524 |             return True
LINE 525 |         return False
LINE 526 | 
LINE 527 |     def _is_important_file(self, rel_path: str, is_ep: bool, is_cfg: bool) -> bool:
LINE 528 |         """Identifies important architectural files (services, controllers, models, routes)."""
LINE 529 |         if is_ep or is_cfg:
LINE 530 |             return True
LINE 531 |         p_lower = rel_path.lower()
LINE 532 |         keywords = ("service", "controller", "model", "route", "router", "handler", "api", "repository")
LINE 533 |         for kw in keywords:
LINE 534 |             if kw in p_lower:
LINE 535 |                 return True
LINE 536 |         return False
LINE 537 | 
LINE 538 |     def _detect_package_manager_and_manifests(self, folder: str) -> Tuple[str, Dict[str, List[str]]]:
LINE 539 |         """Detects package manager and extracts declared dependencies from manifests."""
LINE 540 |         manifest_deps: Dict[str, List[str]] = {}
LINE 541 |         detected_managers = []
LINE 542 | 
LINE 543 |         # 1. Composer (PHP)
LINE 544 |         composer_json = os.path.join(folder, "composer.json")
LINE 545 |         if os.path.isfile(composer_json):
LINE 546 |             mgr = "Composer"
LINE 547 |             detected_managers.append(mgr)
LINE 548 |             try:
LINE 549 |                 with open(composer_json, "r", encoding="utf-8") as fp:
LINE 550 |                     data = json.load(fp)
LINE 551 |                 reqs = []
LINE 552 |                 for pkg, ver in data.get("require", {}).items():
LINE 553 |                     reqs.append(f"{pkg}: {ver}")
LINE 554 |                 for pkg, ver in data.get("require-dev", {}).items():
LINE 555 |                     reqs.append(f"{pkg} (dev): {ver}")
LINE 556 |                 if reqs:
LINE 557 |                     manifest_deps["composer.json"] = reqs
LINE 558 |             except Exception:
LINE 559 |                 pass
LINE 560 | 
LINE 561 |         # 2. Node / JS (npm, yarn, pnpm, bun)
LINE 562 |         pkg_json = os.path.join(folder, "package.json")
LINE 563 |         if os.path.isfile(pkg_json):
LINE 564 |             js_mgr = "npm"
LINE 565 |             if os.path.isfile(os.path.join(folder, "pnpm-lock.yaml")):
LINE 566 |                 js_mgr = "pnpm"
LINE 567 |             elif os.path.isfile(os.path.join(folder, "yarn.lock")):
LINE 568 |                 js_mgr = "Yarn"
LINE 569 |             elif os.path.isfile(os.path.join(folder, "bun.lockb")) or os.path.isfile(os.path.join(folder, "bun.lock")):
LINE 570 |                 js_mgr = "Bun"
LINE 571 |             detected_managers.append(js_mgr)
LINE 572 |             try:
LINE 573 |                 with open(pkg_json, "r", encoding="utf-8") as fp:
LINE 574 |                     data = json.load(fp)
LINE 575 |                 deps = []
LINE 576 |                 for pkg, ver in data.get("dependencies", {}).items():
LINE 577 |                     deps.append(f"{pkg}: {ver}")
LINE 578 |                 for pkg, ver in data.get("devDependencies", {}).items():
LINE 579 |                     deps.append(f"{pkg} (dev): {ver}")
LINE 580 |                 if deps:
LINE 581 |                     manifest_deps["package.json"] = deps
LINE 582 |             except Exception:
LINE 583 |                 pass
LINE 584 | 
LINE 585 |         # 3. Python (pip, poetry, pipenv, conda)
LINE 586 |         req_txt = os.path.join(folder, "requirements.txt")
LINE 587 |         if os.path.isfile(req_txt):
LINE 588 |             detected_managers.append("pip")
LINE 589 |             try:
LINE 590 |                 with open(req_txt, "r", encoding="utf-8") as fp:
LINE 591 |                     lines = [l.strip() for l in fp if l.strip() and not l.strip().startswith("#")]
LINE 592 |                 if lines:
LINE 593 |                     manifest_deps["requirements.txt"] = lines
LINE 594 |             except Exception:
LINE 595 |                 pass
LINE 596 | 
LINE 597 |         pyproject = os.path.join(folder, "pyproject.toml")
LINE 598 |         if os.path.isfile(pyproject):
LINE 599 |             if os.path.isfile(os.path.join(folder, "poetry.lock")):
LINE 600 |                 detected_managers.append("Poetry")
LINE 601 |             else:
LINE 602 |                 detected_managers.append("pip/pyproject.toml")
LINE 603 | 
LINE 604 |         pipfile = os.path.join(folder, "Pipfile")
LINE 605 |         if os.path.isfile(pipfile):
LINE 606 |             detected_managers.append("Pipenv")
LINE 607 | 
LINE 608 |         # 4. Rust (Cargo)
LINE 609 |         if os.path.isfile(os.path.join(folder, "Cargo.toml")):
LINE 610 |             detected_managers.append("Cargo")
LINE 611 | 
LINE 612 |         # 5. Go (Go Modules)
LINE 613 |         if os.path.isfile(os.path.join(folder, "go.mod")):
LINE 614 |             detected_managers.append("Go Modules")
LINE 615 | 
LINE 616 |         # 6. Java (Maven / Gradle)
LINE 617 |         if os.path.isfile(os.path.join(folder, "pom.xml")):
LINE 618 |             detected_managers.append("Maven")
LINE 619 |         elif os.path.isfile(os.path.join(folder, "build.gradle")) or os.path.isfile(os.path.join(folder, "build.gradle.kts")):
LINE 620 |             detected_managers.append("Gradle")
LINE 621 | 
LINE 622 |         primary_mgr = ", ".join(detected_managers) if detected_managers else "Ninguno detectado"
LINE 623 |         return primary_mgr, manifest_deps
LINE 624 | 
LINE 625 |     def _detect_framework(
LINE 626 |         self, folder: str, primary_lang: str, manifest_deps: Dict[str, List[str]], files: List[FileMetric]
LINE 627 |     ) -> Tuple[str, str]:
LINE 628 |         """Detects framework (Laravel, Quasar, Vue, React, FastAPI, Django, Tkinter, etc.)."""
LINE 629 |         # --- PHP / Laravel detection ---
LINE 630 |         if os.path.isfile(os.path.join(folder, "artisan")) or any("laravel/framework" in d for d in manifest_deps.get("composer.json", [])):
LINE 631 |             ver = "Laravel"
LINE 632 |             for d in manifest_deps.get("composer.json", []):
LINE 633 |                 if "laravel/framework" in d:
LINE 634 |                     ver = f"Laravel ({d.split(':')[-1].strip()})"
LINE 635 |                     break
LINE 636 |             return "Laravel", ver
LINE 637 | 
LINE 638 |         if any("symfony" in d.lower() for d in manifest_deps.get("composer.json", [])):
LINE 639 |             return "Symfony", "Framework PHP Symfony"
LINE 640 | 
LINE 641 |         # --- Quasar Framework detection ---
LINE 642 |         quasar_configs = [
LINE 643 |             os.path.isfile(os.path.join(folder, "quasar.config.js")),
LINE 644 |             os.path.isfile(os.path.join(folder, "quasar.config.ts")),
LINE 645 |             os.path.isfile(os.path.join(folder, "quasar.conf.js")),
LINE 646 |         ]
LINE 647 |         pkg_deps = " ".join(manifest_deps.get("package.json", [])).lower()
LINE 648 |         if any(quasar_configs) or "quasar" in pkg_deps or "@quasar/app" in pkg_deps:
LINE 649 |             return "Quasar Framework", "Vue.js + Quasar CLI"
LINE 650 | 
LINE 651 |         # --- Vue / React / Next / Nuxt / Angular / Nest / Express ---
LINE 652 |         if "next" in pkg_deps and "react" in pkg_deps:
LINE 653 |             return "Next.js", "React Framework"
LINE 654 |         if "nuxt" in pkg_deps:
LINE 655 |             return "Nuxt.js", "Vue.js Framework"
LINE 656 |         if "@nestjs/core" in pkg_deps:
LINE 657 |             return "NestJS", "Node.js Framework"
LINE 658 |         if "vue" in pkg_deps:
LINE 659 |             return "Vue.js", "Frontend Framework"
LINE 660 |         if "react" in pkg_deps:
LINE 661 |             return "React", "Frontend Library"
LINE 662 |         if "@angular/core" in pkg_deps:
LINE 663 |             return "Angular", "Frontend Framework"
LINE 664 |         if "express" in pkg_deps:
LINE 665 |             return "Express.js", "Node.js Backend"
LINE 666 | 
LINE 667 |         # --- Python frameworks ---
LINE 668 |         py_reqs = " ".join(manifest_deps.get("requirements.txt", [])).lower()
LINE 669 |         if "django" in py_reqs:
LINE 670 |             return "Django", "Web Framework"
LINE 671 |         if "fastapi" in py_reqs:
LINE 672 |             return "FastAPI", "Modern ASGI Web Framework"
LINE 673 |         if "flask" in py_reqs:
LINE 674 |             return "Flask", "Micro Web Framework"
LINE 675 |         if "streamlit" in py_reqs:
LINE 676 |             return "Streamlit", "Data App Framework"
LINE 677 | 
LINE 678 |         # Check Python imports across scanned files
LINE 679 |         has_tkinter = False
LINE 680 |         has_fastapi = False
LINE 681 |         has_flask = False
LINE 682 |         has_django = False
LINE 683 |         has_pyside = False
LINE 684 | 
LINE 685 |         scanned_py = 0
LINE 686 |         max_py_scan = 150
LINE 687 | 
LINE 688 |         for f in files:
LINE 689 |             if f.rel_path.endswith(".py"):
LINE 690 |                 if scanned_py >= max_py_scan:
LINE 691 |                     break
LINE 692 |                 scanned_py += 1
LINE 693 |                 try:
LINE 694 |                     with open(f.abs_path, "r", encoding="utf-8", errors="ignore") as fp:
LINE 695 |                         content = fp.read(4096)
LINE 696 |                         if "tkinter" in content:
LINE 697 |                             has_tkinter = True
LINE 698 |                         if "fastapi" in content:
LINE 699 |                             has_fastapi = True
LINE 700 |                         if "flask" in content:
LINE 701 |                             has_flask = True
LINE 702 |                         if "django" in content:
LINE 703 |                             has_django = True
LINE 704 |                         if "PyQt" in content or "PySide" in content:
LINE 705 |                             has_pyside = True
LINE 706 |                 except Exception:
LINE 707 |                     pass
LINE 708 | 
LINE 709 |         if has_fastapi:
LINE 710 |             return "FastAPI", "Python ASGI Framework"
LINE 711 |         if has_django:
LINE 712 |             return "Django", "Python Web Framework"
LINE 713 |         if has_flask:
LINE 714 |             return "Flask", "Python Web Framework"
LINE 715 |         if has_pyside:
LINE 716 |             return "PyQt / PySide", "Desktop GUI Framework"
LINE 717 |         if has_tkinter:
LINE 718 |             return "Tkinter", "Python Desktop GUI Standard"
LINE 719 | 
LINE 720 |         # Fallback based on primary language
LINE 721 |         if primary_lang in ("Python", "JavaScript", "TypeScript", "PHP"):
LINE 722 |             return "Estándar / Vanilla", f"Proyecto {primary_lang} modular"
LINE 723 | 
LINE 724 |         return "No detectado", ""
LINE 725 | 
LINE 726 |     def _scan_code_dependencies(self, files: List[FileMetric]) -> Dict[str, List[str]]:
LINE 727 |         """Scans code files using DependencyDetector for imports and dependencies."""
LINE 728 |         code_deps: Dict[str, List[str]] = {}
LINE 729 |         key_files = [f for f in files if f.is_entry_point or f.is_important][:50]
LINE 730 |         if not key_files:
LINE 731 |             key_files = files[:30]
LINE 732 | 
LINE 733 |         for f in key_files:
LINE 734 |             try:
LINE 735 |                 raw_text = safe_read_file(f.abs_path, max_bytes=100_000)
LINE 736 |                 deps = self.dep_detector.detect_file_dependencies(f.rel_path, raw_text)
LINE 737 |                 if deps:
LINE 738 |                     code_deps[f.rel_path] = deps
LINE 739 |             except Exception:
LINE 740 |                 pass
LINE 741 | 
LINE 742 |         return code_deps
LINE 743 | 
LINE 744 |     def _select_recommended_files(
LINE 745 |         self, files: List[FileMetric], entry_points: List[str], config_files: List[str], recent_files: List[Dict[str, Any]]
LINE 746 |     ) -> List[str]:
LINE 747 |         """
LINE 748 |         Smart heuristic algorithm that scores and pre-selects the most relevant files for context.
LINE 749 |         Prioritizes:
LINE 750 |         1. Entry points (main.py, artisan, src/main.js)
LINE 751 |         2. Key configuration and dependency manifests (requirements.txt, package.json, composer.json)
LINE 752 |         3. Core services, controllers, models, routes
LINE 753 |         4. Recently modified files
LINE 754 |         Excludes minified, lockfiles, heavy test files, binaries, or excluded directories.
LINE 755 |         """
LINE 756 |         recent_paths = {rf["path"] for rf in recent_files[:5]}
LINE 757 | 
LINE 758 |         for m in files:
LINE 759 |             score = 0
LINE 760 |             rel = m.rel_path.lower()
LINE 761 | 
LINE 762 |             if m.is_entry_point:
LINE 763 |                 score += 120
LINE 764 | 
LINE 765 |             if m.is_config:
LINE 766 |                 base = os.path.basename(rel)
LINE 767 |                 if base in ("requirements.txt", "package.json", "composer.json", "pyproject.toml", "quasar.config.js", "quasar.config.ts"):
LINE 768 |                     score += 100
LINE 769 |                 elif base.endswith("lock") or base.endswith("lock.json"):
LINE 770 |                     score -= 50
LINE 771 |                 else:
LINE 772 |                     score += 50
LINE 773 | 
LINE 774 |             if m.is_important:
LINE 775 |                 score += 80
LINE 776 | 
LINE 777 |             if rel.startswith("app/") or rel.startswith("src/") or rel.startswith("core/"):
LINE 778 |                 score += 40
LINE 779 | 
LINE 780 |             if m.rel_path in recent_paths:
LINE 781 |                 score += 35
LINE 782 | 
LINE 783 |             if m.size_bytes > 300 * 1024:
LINE 784 |                 score -= 40
LINE 785 |             if ".min." in rel or rel.endswith(".map"):
LINE 786 |                 score -= 100
LINE 787 |             if "test" in rel or "spec" in rel:
LINE 788 |                 score -= 20
LINE 789 | 
LINE 790 |             m.score = score
LINE 791 | 
LINE 792 |         sorted_files = sorted(files, key=lambda x: x.score, reverse=True)
LINE 793 | 
LINE 794 |         recommended = []
LINE 795 |         target_limit = min(max(len(sorted_files), 1), 25)
LINE 796 | 
LINE 797 |         for m in sorted_files:
LINE 798 |             if m.score > 0 or len(recommended) < 5:
LINE 799 |                 base = os.path.basename(m.rel_path).lower()
LINE 800 |                 if base.endswith(".lock") or base in ("package-lock.json", "yarn.lock", "composer.lock"):
LINE 801 |                     continue
LINE 802 |                 if ".min." in base:
LINE 803 |                     continue
LINE 804 |                 recommended.append(m.rel_path)
LINE 805 |             if len(recommended) >= target_limit:
LINE 806 |                 break
LINE 807 | 
LINE 808 |         # Always ensure entry points and primary manifests are in recommended
LINE 809 |         for ep in entry_points:
LINE 810 |             if ep not in recommended:
LINE 811 |                 recommended.insert(0, ep)
LINE 812 |         for cfg in config_files:
LINE 813 |             base = os.path.basename(cfg).lower()
LINE 814 |             if base in ("requirements.txt", "package.json", "composer.json") and cfg not in recommended:
LINE 815 |                 recommended.append(cfg)
LINE 816 | 
LINE 817 |         return sorted(list(dict.fromkeys(recommended)))
```

==============================================================
FILE: app/core/project_scanner.py
==============================================================
```py
LINE   1 | """Project scanner module for scanning directory structures with caching."""
LINE   2 | import os
LINE   3 | import threading
LINE   4 | from typing import Set, Dict, Any, List, Optional, Tuple
LINE   5 | from app.utils.file_utils import KNOWN_BINARY_EXTENSIONS
LINE   6 | 
LINE   7 | _cache_lock = threading.Lock()
LINE   8 | # Cache mapping: key -> (folder_mtime, valid_files)
LINE   9 | _SCAN_CACHE: Dict[Tuple, Tuple[float, List[str]]] = {}
LINE  10 | _MAX_CACHE_ENTRIES = 50
LINE  11 | 
LINE  12 | 
LINE  13 | def clear_scan_cache() -> None:
LINE  14 |     """Clears the scan directory cache."""
LINE  15 |     with _cache_lock:
LINE  16 |         _SCAN_CACHE.clear()
LINE  17 | 
LINE  18 | 
LINE  19 | def is_file_allowed(filename: str, allowed_extensions: Optional[Set[str]], filter_by_ext: bool = True) -> bool:
LINE  20 |     """Checks if file is allowed (not binary media and matching allowed extensions)."""
LINE  21 |     ext = os.path.splitext(filename)[1].lower()
LINE  22 |     if ext in KNOWN_BINARY_EXTENSIONS:
LINE  23 |         return False
LINE  24 |     if filter_by_ext and allowed_extensions:
LINE  25 |         return ext in allowed_extensions
LINE  26 |     return True
LINE  27 | 
LINE  28 | 
LINE  29 | def scan_directory(
LINE  30 |     folder_path: str,
LINE  31 |     excluded_dirs: Optional[Set[str]] = None,
LINE  32 |     allowed_extensions: Optional[Set[str]] = None,
LINE  33 |     use_cache: bool = True,
LINE  34 |     force_refresh: bool = False,
LINE  35 | ) -> List[str]:
LINE  36 |     """
LINE  37 |     Recursively scans folder_path ignoring excluded_dirs and non-allowed file extensions.
LINE  38 |     Returns sorted list of relative file paths. Uses thread-safe caching with mtime checking.
LINE  39 |     """
LINE  40 |     if not folder_path or not os.path.isdir(folder_path):
LINE  41 |         return []
LINE  42 | 
LINE  43 |     abs_folder = os.path.abspath(folder_path)
LINE  44 |     excluded_set = set(excluded_dirs) if excluded_dirs else set()
LINE  45 |     allowed_tuple = tuple(sorted(allowed_extensions)) if allowed_extensions else None
LINE  46 |     cache_key = (abs_folder, tuple(sorted(excluded_set)), allowed_tuple)
LINE  47 | 
LINE  48 |     # FIX: firma de invalidación recursiva ligera (raíz + subdirectorios
LINE  49 |     # inmediatos). No es perfecta, pero evita devolver caché obsoleta cuando
LINE  50 |     # cambian archivos dentro de subcarpetas de primer nivel, sin coste de
LINE  51 |     # os.walk completo.
LINE  52 |     signature = 0.0
LINE  53 |     try:
LINE  54 |         signature = os.path.getmtime(abs_folder)
LINE  55 |         with os.scandir(abs_folder) as it:
LINE  56 |             for entry in it:
LINE  57 |                 if entry.is_dir(follow_symlinks=False):
LINE  58 |                     try:
LINE  59 |                         signature = max(
LINE  60 |                             signature,
LINE  61 |                             entry.stat(follow_symlinks=False).st_mtime,
LINE  62 |                         )
LINE  63 |                     except OSError:
LINE  64 |                         continue
LINE  65 |     except OSError:
LINE  66 |         pass
LINE  67 | 
LINE  68 |     if use_cache and not force_refresh:
LINE  69 |         with _cache_lock:
LINE  70 |             if cache_key in _SCAN_CACHE:
LINE  71 |                 cached_mtime, cached_files = _SCAN_CACHE[cache_key]
LINE  72 |                 if cached_mtime == signature:
LINE  73 |                     return list(cached_files)
LINE  74 | 
LINE  75 |     valid_files = []
LINE  76 | 
LINE  77 |     def _walk_error(err: OSError):
LINE  78 |         pass  # Ignore permission/access errors gracefully
LINE  79 | 
LINE  80 |     try:
LINE  81 |         for dirpath, dirnames, filenames in os.walk(abs_folder, onerror=_walk_error):
LINE  82 |             dirnames[:] = [d for d in dirnames if d not in excluded_set]
LINE  83 |             rel_dir = os.path.relpath(dirpath, abs_folder)
LINE  84 | 
LINE  85 |             for f in filenames:
LINE  86 |                 try:
LINE  87 |                     if is_file_allowed(f, allowed_extensions):
LINE  88 |                         rel_file = f if rel_dir == '.' else os.path.join(rel_dir, f)
LINE  89 |                         valid_files.append(rel_file.replace("\\", "/"))
LINE  90 |                 except Exception:
LINE  91 |                     continue
LINE  92 |     except Exception:
LINE  93 |         pass
LINE  94 | 
LINE  95 |     valid_files = sorted(valid_files)
LINE  96 | 
LINE  97 |     if use_cache:
LINE  98 |         with _cache_lock:
LINE  99 |             if len(_SCAN_CACHE) >= _MAX_CACHE_ENTRIES:
LINE 100 |                 try:
LINE 101 |                     first_key = next(iter(_SCAN_CACHE))
LINE 102 |                     del _SCAN_CACHE[first_key]
LINE 103 |                 except (StopIteration, KeyError):
LINE 104 |                     pass
LINE 105 |             _SCAN_CACHE[cache_key] = (signature, valid_files)
LINE 106 | 
LINE 107 |     return valid_files
```

==============================================================
FILE: app/core/project_structure.py
==============================================================
```py
LINE  1 | """Generates textual tree representation of a folder structure using box-drawing characters."""
LINE  2 | import os
LINE  3 | from typing import Set, List, Dict, Any
LINE  4 | 
LINE  5 | 
LINE  6 | def build_folder_tree_str(folder_path: str, checked_rel_paths: List[str], excluded_dirs: Set[str]) -> str:
LINE  7 |     """Generates ASCII/Unicode tree text representation (├──, └──, │) of checked files."""
LINE  8 |     if not folder_path or not os.path.isdir(folder_path):
LINE  9 |         return ""
LINE 10 | 
LINE 11 |     root_name = os.path.basename(folder_path) or folder_path
LINE 12 |     
LINE 13 |     # Build nested dict hierarchy of checked files
LINE 14 |     hierarchy: Dict[str, Any] = {}
LINE 15 |     for rel_path in sorted(checked_rel_paths):
LINE 16 |         parts = rel_path.split(os.sep)
LINE 17 |         curr = hierarchy
LINE 18 |         for part in parts[:-1]:
LINE 19 |             curr = curr.setdefault(part, {})
LINE 20 |         curr[parts[-1]] = None  # File leaf
LINE 21 | 
LINE 22 |     def render_node(node_dict: Dict[str, Any], prefix: str = "") -> List[str]:
LINE 23 |         lines = []
LINE 24 |         keys = list(node_dict.keys())
LINE 25 |         for idx, key in enumerate(keys):
LINE 26 |             is_last = (idx == len(keys) - 1)
LINE 27 |             connector = "└── " if is_last else "├── "
LINE 28 |             val = node_dict[key]
LINE 29 |             if val is None:
LINE 30 |                 # File
LINE 31 |                 lines.append(f"{prefix}{connector}{key}")
LINE 32 |             else:
LINE 33 |                 # Directory
LINE 34 |                 lines.append(f"{prefix}{connector}{key}/")
LINE 35 |                 new_prefix = prefix + ("    " if is_last else "│   ")
LINE 36 |                 lines.extend(render_node(val, new_prefix))
LINE 37 |         return lines
LINE 38 | 
LINE 39 |     tree_lines = [f"{root_name}/"]
LINE 40 |     tree_lines.extend(render_node(hierarchy))
LINE 41 |     return "\n".join(tree_lines)
```

==============================================================
FILE: app/core/storage/__init__.py
==============================================================
```py
LINE 1 | """Phase 1 SQLite persistence package."""
LINE 2 | from app.core.storage.database import Database, get_database, default_db_path
LINE 3 | 
LINE 4 | __all__ = ["Database", "get_database", "default_db_path"]
```

==============================================================
FILE: app/core/storage/database.py
==============================================================
```py
LINE   1 | """
LINE   2 | SQLite persistence layer for project nodes, metrics and dependencies (Phase 1).
LINE   3 | 
LINE   4 | This module is intentionally restricted to:
LINE   5 |   - Opening / creating the SQLite database.
LINE   6 |   - Initializing the schema.
LINE   7 |   - Executing queries and updates.
LINE   8 |   - Managing transactions.
LINE   9 |   - Providing the CRUD operations required for projects and nodes.
LINE  10 | 
LINE  11 | No Delta Scan or incremental change detection logic is implemented here.
LINE  12 | """
LINE  13 | import os
LINE  14 | import sqlite3
LINE  15 | from typing import Dict, List, Optional, Set, Tuple
LINE  16 | 
LINE  17 | 
LINE  18 | # ---------------------------------------------------------------------------
LINE  19 | # Path resolution
LINE  20 | # ---------------------------------------------------------------------------
LINE  21 | 
LINE  22 | def _find_project_root() -> Optional[str]:
LINE  23 |     """Walk up from this file to find the project root (contains main.py)."""
LINE  24 |     here = os.path.dirname(os.path.abspath(__file__))
LINE  25 |     candidate = os.path.abspath(os.path.join(here, "..", "..", ".."))
LINE  26 |     if os.path.isfile(os.path.join(candidate, "main.py")):
LINE  27 |         return candidate
LINE  28 |     return None
LINE  29 | 
LINE  30 | 
LINE  31 | def default_db_path() -> str:
LINE  32 |     """Resolve project_cache.db path.
LINE  33 | 
LINE  34 |     Prefer <project_root>/.cache/project_cache.db, fallback to
LINE  35 |     ~/.analyzer_app/project_cache.db when the project root cannot be resolved.
LINE  36 |     """
LINE  37 |     root = _find_project_root()
LINE  38 |     if root:
LINE  39 |         return os.path.join(root, ".cache", "project_cache.db")
LINE  40 |     home = os.path.expanduser("~")
LINE  41 |     return os.path.join(home, ".analyzer_app", "project_cache.db")
LINE  42 | 
LINE  43 | 
LINE  44 | # ---------------------------------------------------------------------------
LINE  45 | # Schema
LINE  46 | # ---------------------------------------------------------------------------
LINE  47 | 
LINE  48 | SCHEMA_STATEMENTS = [
LINE  49 |     """CREATE TABLE IF NOT EXISTS projects (
LINE  50 |         id INTEGER PRIMARY KEY AUTOINCREMENT,
LINE  51 |         path TEXT UNIQUE NOT NULL,
LINE  52 |         project_type TEXT,
LINE  53 |         framework TEXT,
LINE  54 |         last_scanned TIMESTAMP DEFAULT CURRENT_TIMESTAMP
LINE  55 |     )""",
LINE  56 |     """CREATE TABLE IF NOT EXISTS nodes (
LINE  57 |         id INTEGER PRIMARY KEY AUTOINCREMENT,
LINE  58 |         project_id INTEGER NOT NULL,
LINE  59 |         rel_path TEXT NOT NULL,
LINE  60 |         parent_path TEXT,
LINE  61 |         is_dir BOOLEAN NOT NULL,
LINE  62 |         mtime REAL NOT NULL,
LINE  63 |         lines_count INTEGER DEFAULT 0,
LINE  64 |         file_size INTEGER DEFAULT 0,
LINE  65 |         is_important BOOLEAN DEFAULT 0,
LINE  66 |         is_checked BOOLEAN DEFAULT 1,
LINE  67 |         FOREIGN KEY(project_id) REFERENCES projects(id) ON DELETE CASCADE,
LINE  68 |         UNIQUE(project_id, rel_path)
LINE  69 |     )""",
LINE  70 |     """CREATE TABLE IF NOT EXISTS node_dependencies (
LINE  71 |         id INTEGER PRIMARY KEY AUTOINCREMENT,
LINE  72 |         source_node_id INTEGER NOT NULL,
LINE  73 |         target_path TEXT NOT NULL,
LINE  74 |         FOREIGN KEY(source_node_id) REFERENCES nodes(id) ON DELETE CASCADE
LINE  75 |     )""",
LINE  76 |     "CREATE INDEX IF NOT EXISTS idx_nodes_rel_path ON nodes(project_id, rel_path)",
LINE  77 |     "CREATE INDEX IF NOT EXISTS idx_nodes_parent ON nodes(project_id, parent_path)",
LINE  78 | ]
LINE  79 | 
LINE  80 | 
LINE  81 | # ---------------------------------------------------------------------------
LINE  82 | # Database
LINE  83 | # ---------------------------------------------------------------------------
LINE  84 | 
LINE  85 | class Database:
LINE  86 |     """Thin SQLite wrapper for the project cache (Phase 1)."""
LINE  87 | 
LINE  88 |     def __init__(self, db_path: Optional[str] = None):
LINE  89 |         self.db_path = db_path or default_db_path()
LINE  90 |         os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
LINE  91 |         self._conn = sqlite3.connect(self.db_path, timeout=10.0)
LINE  92 |         self._conn.row_factory = sqlite3.Row
LINE  93 |         self._conn.execute("PRAGMA foreign_keys = ON")
LINE  94 |         self._conn.execute("PRAGMA journal_mode = WAL")
LINE  95 |         self._conn.execute("PRAGMA synchronous = NORMAL")
LINE  96 |         self._init_schema()
LINE  97 | 
LINE  98 |     def _init_schema(self) -> None:
LINE  99 |         with self._conn:
LINE 100 |             for stmt in SCHEMA_STATEMENTS:
LINE 101 |                 self._conn.execute(stmt)
LINE 102 | 
LINE 103 |     # ---------- projects ----------
LINE 104 | 
LINE 105 |     def get_or_create_project(self, path: str,
LINE 106 |                               project_type: Optional[str] = None,
LINE 107 |                               framework: Optional[str] = None) -> int:
LINE 108 |         cur = self._conn.cursor()
LINE 109 |         cur.execute("SELECT id FROM projects WHERE path = ?", (path,))
LINE 110 |         row = cur.fetchone()
LINE 111 |         if row:
LINE 112 |             return int(row["id"])
LINE 113 |         cur.execute(
LINE 114 |             "INSERT INTO projects (path, project_type, framework) VALUES (?, ?, ?)",
LINE 115 |             (path, project_type, framework),
LINE 116 |         )
LINE 117 |         self._conn.commit()
LINE 118 |         return int(cur.lastrowid)
LINE 119 | 
LINE 120 |     def get_project_by_path(self, path: str) -> Optional[Dict]:
LINE 121 |         cur = self._conn.cursor()
LINE 122 |         cur.execute("SELECT * FROM projects WHERE path = ?", (path,))
LINE 123 |         row = cur.fetchone()
LINE 124 |         return dict(row) if row else None
LINE 125 | 
LINE 126 |     def update_last_scanned(self, project_id: int) -> None:
LINE 127 |         with self._conn:
LINE 128 |             self._conn.execute(
LINE 129 |                 "UPDATE projects SET last_scanned = CURRENT_TIMESTAMP WHERE id = ?",
LINE 130 |                 (project_id,),
LINE 131 |             )
LINE 132 | 
LINE 133 |     def delete_project(self, path: str) -> None:
LINE 134 |         with self._conn:
LINE 135 |             self._conn.execute("DELETE FROM projects WHERE path = ?", (path,))
LINE 136 | 
LINE 137 |     # ---------- nodes ----------
LINE 138 | 
LINE 139 |     def replace_nodes(self, project_id: int, nodes: List[Dict]) -> None:
LINE 140 |         """Delete existing nodes for project and insert the new batch atomically."""
LINE 141 |         rows = [
LINE 142 |             (
LINE 143 |                 project_id,
LINE 144 |                 n["rel_path"],
LINE 145 |                 n.get("parent_path"),
LINE 146 |                 int(bool(n.get("is_dir", 0))),
LINE 147 |                 float(n.get("mtime", 0.0) or 0.0),
LINE 148 |                 int(n.get("lines_count", 0) or 0),
LINE 149 |                 int(n.get("file_size", 0) or 0),
LINE 150 |                 int(bool(n.get("is_important", 0))),
LINE 151 |                 int(bool(n.get("is_checked", 1))),
LINE 152 |             )
LINE 153 |             for n in nodes
LINE 154 |         ]
LINE 155 |         with self._conn:
LINE 156 |             self._conn.execute("DELETE FROM nodes WHERE project_id = ?", (project_id,))
LINE 157 |             if rows:
LINE 158 |                 self._conn.executemany(
LINE 159 |                     """INSERT INTO nodes
LINE 160 |                        (project_id, rel_path, parent_path, is_dir, mtime,
LINE 161 |                         lines_count, file_size, is_important, is_checked)
LINE 162 |                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
LINE 163 |                     rows,
LINE 164 |                 )
LINE 165 | 
LINE 166 |     def get_nodes(self, project_id: int) -> List[Dict]:
LINE 167 |         cur = self._conn.cursor()
LINE 168 |         cur.execute("SELECT * FROM nodes WHERE project_id = ?", (project_id,))
LINE 169 |         return [dict(r) for r in cur.fetchall()]
LINE 170 | 
LINE 171 |     def update_is_checked(self, project_id: int,
LINE 172 |                           rel_path: str, is_checked: bool) -> None:
LINE 173 |         with self._conn:
LINE 174 |             self._conn.execute(
LINE 175 |                 "UPDATE nodes SET is_checked = ? "
LINE 176 |                 "WHERE project_id = ? AND rel_path = ?",
LINE 177 |                 (int(bool(is_checked)), project_id, rel_path),
LINE 178 |             )
LINE 179 | 
LINE 180 |     def update_is_checked_batch(self, project_id: int,
LINE 181 |                                 updates: List[Tuple[str, bool]]) -> None:
LINE 182 |         rows = [(int(bool(c)), project_id, rp) for rp, c in updates]
LINE 183 |         if not rows:
LINE 184 |             return
LINE 185 |         with self._conn:
LINE 186 |             self._conn.executemany(
LINE 187 |                 "UPDATE nodes SET is_checked = ? "
LINE 188 |                 "WHERE project_id = ? AND rel_path = ?",
LINE 189 |                 rows,
LINE 190 |             )
LINE 191 | 
LINE 192 |     def load_checked_state(self, project_path: str) -> Optional[Set[str]]:
LINE 193 |         """Return the set of checked rel_paths (files only).
LINE 194 | 
LINE 195 |         Returns None when there is no persisted data for this project,
LINE 196 |         so the caller can distinguish "never saved" from "all unchecked".
LINE 197 |         """
LINE 198 |         cur = self._conn.cursor()
LINE 199 |         cur.execute("SELECT id FROM projects WHERE path = ?", (project_path,))
LINE 200 |         row = cur.fetchone()
LINE 201 |         if not row:
LINE 202 |             return None
LINE 203 |         project_id = int(row["id"])
LINE 204 |         cur.execute(
LINE 205 |             "SELECT rel_path, is_checked FROM nodes "
LINE 206 |             "WHERE project_id = ? AND is_dir = 0",
LINE 207 |             (project_id,),
LINE 208 |         )
LINE 209 |         rows = cur.fetchall()
LINE 210 |         if not rows:
LINE 211 |             return None
LINE 212 |         return {r["rel_path"] for r in rows if r["is_checked"]}
LINE 213 | 
LINE 214 |     def delete_nodes(self, project_id: int) -> None:
LINE 215 |         with self._conn:
LINE 216 |             self._conn.execute("DELETE FROM nodes WHERE project_id = ?", (project_id,))
LINE 217 | 
LINE 218 |     # ---------- dependencies ----------
LINE 219 | 
LINE 220 |     def save_dependencies_batch(self, project_id: int,
LINE 221 |                                 deps: List[Tuple[str, str]]) -> None:
LINE 222 |         """deps: list of (source_rel_path, target_path)."""
LINE 223 |         if not deps:
LINE 224 |             return
LINE 225 |         cur = self._conn.cursor()
LINE 226 |         cur.execute("SELECT id, rel_path FROM nodes WHERE project_id = ?", (project_id,))
LINE 227 |         id_map = {r["rel_path"]: int(r["id"]) for r in cur.fetchall()}
LINE 228 | 
LINE 229 |         rows = []
LINE 230 |         for src_rel, target in deps:
LINE 231 |             node_id = id_map.get(src_rel)
LINE 232 |             if node_id is None:
LINE 233 |                 continue
LINE 234 |             rows.append((node_id, target))
LINE 235 | 
LINE 236 |         with self._conn:
LINE 237 |             self._conn.execute(
LINE 238 |                 """DELETE FROM node_dependencies
LINE 239 |                    WHERE source_node_id IN
LINE 240 |                          (SELECT id FROM nodes WHERE project_id = ?)""",
LINE 241 |                 (project_id,),
LINE 242 |             )
LINE 243 |             if rows:
LINE 244 |                 self._conn.executemany(
LINE 245 |                     "INSERT INTO node_dependencies (source_node_id, target_path) "
LINE 246 |                     "VALUES (?, ?)",
LINE 247 |                     rows,
LINE 248 |                 )
LINE 249 | 
LINE 250 |     def get_dependencies(self, project_id: int) -> List[Dict]:
LINE 251 |         cur = self._conn.cursor()
LINE 252 |         cur.execute(
LINE 253 |             """SELECT n.rel_path AS source_path, d.target_path AS target_path
LINE 254 |                FROM node_dependencies d
LINE 255 |                JOIN nodes n ON n.id = d.source_node_id
LINE 256 |                WHERE n.project_id = ?""",
LINE 257 |             (project_id,),
LINE 258 |         )
LINE 259 |         return [dict(r) for r in cur.fetchall()]
LINE 260 | 
LINE 261 |     def load_file_paths(self, project_path: str):
LINE 262 |         """Devuelve lista plana de rutas de archivo (is_dir=0) ordenadas.
LINE 263 | 
LINE 264 |         Pensado para alimentar el buscador sin pagar el coste de os.walk.
LINE 265 |         Devuelve:
LINE 266 |             (files: List[str], last_scanned: Optional[str], exists: bool)
LINE 267 |         donde `files` es [] si el proyecto existe pero no tiene nodos.
LINE 268 |         """
LINE 269 |         cur = self._conn.cursor()
LINE 270 |         cur.execute(
LINE 271 |             "SELECT id, last_scanned FROM projects WHERE path = ?",
LINE 272 |             (project_path,),
LINE 273 |         )
LINE 274 |         row = cur.fetchone()
LINE 275 |         if not row:
LINE 276 |             return [], None, False
LINE 277 |         project_id = int(row["id"])
LINE 278 |         last_scanned = row["last_scanned"]
LINE 279 |         cur.execute(
LINE 280 |             "SELECT rel_path FROM nodes "
LINE 281 |             "WHERE project_id = ? AND is_dir = 0 "
LINE 282 |             "ORDER BY rel_path",
LINE 283 |             (project_id,),
LINE 284 |         )
LINE 285 |         files = [r["rel_path"] for r in cur.fetchall()]
LINE 286 |         return files, last_scanned, True
LINE 287 | 
LINE 288 |     # === PHASE 2: DELTA SCAN ===
LINE 289 |     def load_nodes_map(self, project_path: str):
LINE 290 |         cur = self._conn.cursor()
LINE 291 |         cur.execute("SELECT id FROM projects WHERE path = ?", (project_path,))
LINE 292 |         row = cur.fetchone()
LINE 293 |         if not row:
LINE 294 |             return None
LINE 295 |         project_id = int(row["id"])
LINE 296 |         cur.execute(
LINE 297 |             "SELECT id, rel_path, parent_path, is_dir, mtime, lines_count, "
LINE 298 |             "file_size, is_important, is_checked FROM nodes WHERE project_id = ?",
LINE 299 |             (project_id,),
LINE 300 |         )
LINE 301 |         return {r["rel_path"]: dict(r) for r in cur.fetchall()}
LINE 302 | 
LINE 303 |     def apply_delta(self, project_id, to_insert, to_update,
LINE 304 |                     to_delete_paths, dep_pairs):
LINE 305 |         if to_delete_paths:
LINE 306 |             with self._conn:
LINE 307 |                 self._conn.executemany(
LINE 308 |                     "DELETE FROM nodes WHERE project_id = ? AND rel_path = ?",
LINE 309 |                     [(project_id, rp) for rp in to_delete_paths],
LINE 310 |                 )
LINE 311 |         if to_update:
LINE 312 |             with self._conn:
LINE 313 |                 self._conn.executemany(
LINE 314 |                     """UPDATE nodes SET mtime=?, lines_count=?, file_size=?,
LINE 315 |                                        is_important=?
LINE 316 |                        WHERE project_id=? AND rel_path=?""",
LINE 317 |                     [(n["mtime"], n["lines_count"], n["file_size"],
LINE 318 |                       int(bool(n.get("is_important", 0))),
LINE 319 |                       project_id, n["rel_path"]) for n in to_update],
LINE 320 |                 )
LINE 321 |         if to_insert:
LINE 322 |             with self._conn:
LINE 323 |                 self._conn.executemany(
LINE 324 |                     """INSERT INTO nodes
LINE 325 |                        (project_id, rel_path, parent_path, is_dir, mtime,
LINE 326 |                         lines_count, file_size, is_important, is_checked)
LINE 327 |                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
LINE 328 |                     [(project_id, n["rel_path"], n.get("parent_path"),
LINE 329 |                       int(bool(n.get("is_dir", 0))),
LINE 330 |                       float(n.get("mtime", 0.0)),
LINE 331 |                       int(n.get("lines_count", 0) or 0),
LINE 332 |                       int(n.get("file_size", 0) or 0),
LINE 333 |                       int(bool(n.get("is_important", 0))),
LINE 334 |                       int(bool(n.get("is_checked", 1))))
LINE 335 |                      for n in to_insert],
LINE 336 |                 )
LINE 337 |         if to_update or to_insert or to_delete_paths:
LINE 338 |             with self._conn:
LINE 339 |                 pairs = ([(project_id, n["rel_path"]) for n in to_update] +
LINE 340 |                          [(project_id, n["rel_path"]) for n in to_insert] +
LINE 341 |                          [(project_id, rp) for rp in to_delete_paths])
LINE 342 |                 self._conn.executemany(
LINE 343 |                     """DELETE FROM node_dependencies
LINE 344 |                        WHERE source_node_id IN
LINE 345 |                          (SELECT id FROM nodes WHERE project_id=? AND rel_path=?)""",
LINE 346 |                     pairs,
LINE 347 |                 )
LINE 348 |                 if dep_pairs:
LINE 349 |                     cur = self._conn.cursor()
LINE 350 |                     cur.execute(
LINE 351 |                         "SELECT id, rel_path FROM nodes WHERE project_id=?",
LINE 352 |                         (project_id,))
LINE 353 |                     id_map = {r["rel_path"]: int(r["id"])
LINE 354 |                               for r in cur.fetchall()}
LINE 355 |                     rows = [(id_map[s], t) for s, t in dep_pairs if s in id_map]
LINE 356 |                     if rows:
LINE 357 |                         self._conn.executemany(
LINE 358 |                             "INSERT INTO node_dependencies "
LINE 359 |                             "(source_node_id, target_path) VALUES (?, ?)",
LINE 360 |                             rows,
LINE 361 |                         )
LINE 362 |         self.update_last_scanned(project_id)
LINE 363 |     # === END PHASE 2 ===
LINE 364 | 
LINE 365 |     def close(self) -> None:
LINE 366 |         try:
LINE 367 |             self._conn.close()
LINE 368 |         except Exception:
LINE 369 |             pass
LINE 370 | 
LINE 371 | 
LINE 372 | # ---------------------------------------------------------------------------
LINE 373 | # Singleton accessor
LINE 374 | # ---------------------------------------------------------------------------
LINE 375 | 
LINE 376 | _db_singleton: Optional[Database] = None
LINE 377 | 
LINE 378 | 
LINE 379 | def get_database(db_path: Optional[str] = None) -> Database:
LINE 380 |     """Return the process-wide Database singleton."""
LINE 381 |     global _db_singleton
LINE 382 |     if _db_singleton is None or (db_path and db_path != _db_singleton.db_path):
LINE 383 |         _db_singleton = Database(db_path)
LINE 384 |     return _db_singleton
LINE 385 | 
LINE 386 | 
LINE 387 | def reset_database_singleton() -> None:
LINE 388 |     """For tests: close and drop the current singleton."""
LINE 389 |     global _db_singleton
LINE 390 |     if _db_singleton is not None:
LINE 391 |         _db_singleton.close()
LINE 392 |     _db_singleton = None
```

==============================================================
FILE: app/generators/__init__.py
==============================================================
```py
LINE  1 | """Generators package initialization."""
LINE  2 | from app.generators.markdown_generator import generate_markdown_bundle
LINE  3 | from app.generators.text_generator import generate_text_bundle
LINE  4 | from app.generators.prompt_generator import PromptGenerator
LINE  5 | from app.generators.standalone_prompt_generator import generate_standalone_prompt
LINE  6 | 
LINE  7 | __all__ = [
LINE  8 |     "generate_markdown_bundle", 
LINE  9 |     "generate_text_bundle", 
LINE 10 |     "PromptGenerator", 
LINE 11 |     "generate_standalone_prompt"
LINE 12 | ]
```

==============================================================
FILE: app/generators/markdown_generator.py
==============================================================
```py
LINE   1 | """Markdown prompt bundle generator with Smart Context (File Extensions Breakdown & Dependencies)."""
LINE   2 | import os
LINE   3 | from collections import Counter
LINE   4 | from datetime import datetime
LINE   5 | from typing import Tuple, List, Dict
LINE   6 | from app.models.project import ProjectSelection, ExportConfig
LINE   7 | from app.core.file_reader import read_and_format_file
LINE   8 | from app.core.project_structure import build_folder_tree_str
LINE   9 | from app.core.dependency_detector import DependencyDetector
LINE  10 | from app.models.analysis_types import get_analysis_profile
LINE  11 | from app.models.analysis_modes import get_analysis_mode_config, MODE_PROJECT
LINE  12 | from app.utils.file_utils import is_binary_file, get_file_size, safe_read_file
LINE  13 | 
LINE  14 | 
LINE  15 | def generate_markdown_bundle(
LINE  16 |     selection: ProjectSelection, 
LINE  17 |     problem_desc: str, 
LINE  18 |     config: ExportConfig
LINE  19 | ) -> Tuple[str, int, int, int, int]:
LINE  20 |     """
LINE  21 |     Generates Markdown document with Smart Context:
LINE  22 |     1. REPORTED PROBLEM
LINE  23 |     2. PROJECT CONTEXT (Metadata, Extension Frequency Summary, Dependencies, Limits Warnings, Tree)
LINE  24 |     3. ATTACHMENTS (Selected Files with LINE X | formatting)
LINE  25 | 
LINE  26 |     Returns: (full_text, included_count, excluded_count, oversized_count, total_lines)
LINE  27 |     """
LINE  28 |     folder_path = selection.folder_path
LINE  29 |     project_name = os.path.basename(folder_path) if folder_path else "Proyecto"
LINE  30 |     base_path = os.path.abspath(folder_path) if folder_path else "N/A"
LINE  31 |     gen_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
LINE  32 | 
LINE  33 |     file_blocks = []
LINE  34 |     omitted_warnings: List[Dict[str, str]] = []
LINE  35 |     extension_counts: Counter = Counter()
LINE  36 |     file_dependencies: Dict[str, List[str]] = {}
LINE  37 | 
LINE  38 |     included_count = 0
LINE  39 |     excluded_count = 0
LINE  40 |     oversized_count = 0
LINE  41 |     total_lines = 0
LINE  42 | 
LINE  43 |     cumulative_bytes = 0
LINE  44 |     max_file_bytes = int(config.max_file_size_mb * 1024 * 1024)
LINE  45 |     max_total_bytes = int(config.max_total_size_mb * 1024 * 1024)
LINE  46 |     detector = DependencyDetector()
LINE  47 | 
LINE  48 |     def process_file(full_path: str, display_name: str):
LINE  49 |         nonlocal included_count, excluded_count, oversized_count, total_lines, cumulative_bytes
LINE  50 | 
LINE  51 |         ext = os.path.splitext(display_name)[1].lower() or "[sin extensión]"
LINE  52 | 
LINE  53 |         # 1. Binary check
LINE  54 |         if is_binary_file(full_path):
LINE  55 |             excluded_count += 1
LINE  56 |             return
LINE  57 | 
LINE  58 |         size_bytes = get_file_size(full_path)
LINE  59 | 
LINE  60 |         # 2. Check MAX_FILES limit
LINE  61 |         if included_count >= config.max_files:
LINE  62 |             oversized_count += 1
LINE  63 |             omitted_warnings.append({
LINE  64 |                 "file": display_name,
LINE  65 |                 "reason": f"Exceeds MAX_FILES limit of {config.max_files} files."
LINE  66 |             })
LINE  67 |             return
LINE  68 | 
LINE  69 |         # 3. Check MAX_FILE_SIZE limit
LINE  70 |         if size_bytes > max_file_bytes:
LINE  71 |             oversized_count += 1
LINE  72 |             omitted_warnings.append({
LINE  73 |                 "file": display_name,
LINE  74 |                 "reason": f"Exceeds the allowed limit of {config.max_file_size_mb:g} MB."
LINE  75 |             })
LINE  76 |             return
LINE  77 | 
LINE  78 |         # 4. Check MAX_TOTAL_SIZE limit
LINE  79 |         if cumulative_bytes + size_bytes > max_total_bytes:
LINE  80 |             oversized_count += 1
LINE  81 |             omitted_warnings.append({
LINE  82 |                 "file": display_name,
LINE  83 |                 "reason": f"Exceeds MAX_TOTAL_SIZE limit of {config.max_total_size_mb:g} MB (Cumulative size reached)."
LINE  84 |             })
LINE  85 |             return
LINE  86 | 
LINE  87 |         # Read content safely
LINE  88 |         raw_text = safe_read_file(full_path, max_bytes=max_file_bytes)
LINE  89 |         deps = detector.detect_file_dependencies(display_name, raw_text)
LINE  90 |         if deps:
LINE  91 |             file_dependencies[display_name] = deps
LINE  92 | 
LINE  93 |         formatted_code = read_and_format_file(
LINE  94 |             full_path, 
LINE  95 |             add_line_numbers=config.add_line_numbers,
LINE  96 |             max_file_size_mb=config.max_file_size_mb
LINE  97 |         )
LINE  98 |         lines_in_file = formatted_code.count('\n') + (1 if formatted_code else 0)
LINE  99 |         total_lines += lines_in_file
LINE 100 |         cumulative_bytes += size_bytes
LINE 101 |         extension_counts[ext] += 1
LINE 102 | 
LINE 103 |         code_ext = ext.lstrip('.')
LINE 104 |         block = [
LINE 105 |             "==============================================================",
LINE 106 |             f"FILE: {display_name}",
LINE 107 |             "==============================================================",
LINE 108 |             f"```{code_ext}",
LINE 109 |             formatted_code,
LINE 110 |             "```"
LINE 111 |         ]
LINE 112 |         file_blocks.append("\n".join(block))
LINE 113 |         included_count += 1
LINE 114 | 
LINE 115 |     # 1. Folder files
LINE 116 |     if folder_path and os.path.isdir(folder_path):
LINE 117 |         for rel_f in sorted(selection.checked_folder_files):
LINE 118 |             full_path = os.path.join(folder_path, rel_f)
LINE 119 |             if os.path.isfile(full_path):
LINE 120 |                 process_file(full_path, rel_f)
LINE 121 | 
LINE 122 |     # 2. Individual files
LINE 123 |     for abs_f in selection.individual_files:
LINE 124 |         if os.path.isfile(abs_f):
LINE 125 |             if folder_path and abs_f.startswith(folder_path):
LINE 126 |                 display_name = os.path.relpath(abs_f, folder_path)
LINE 127 |             else:
LINE 128 |                 display_name = os.path.basename(abs_f)
LINE 129 |             process_file(abs_f, display_name)
LINE 130 | 
LINE 131 |     analysis_type = getattr(config, "analysis_type", "Detect errors")
LINE 132 |     analysis_mode = getattr(config, "analysis_mode", "problem")
LINE 133 |     profile = get_analysis_profile(analysis_type)
LINE 134 |     mode_cfg = get_analysis_mode_config(analysis_mode)
LINE 135 |     is_project_mode = (mode_cfg.mode == MODE_PROJECT)
LINE 136 | 
LINE 137 |     doc = []
LINE 138 | 
LINE 139 |     # 1. REPORTED PROBLEM / HOLISTIC AUDIT SCOPE
LINE 140 |     doc.append("==============================================================")
LINE 141 |     if is_project_mode:
LINE 142 |         doc.append("HOLISTIC PROJECT AUDIT / AUDITORÍA HOLÍSTICA DEL PROYECTO")
LINE 143 |         doc.append("==============================================================")
LINE 144 |         doc.append(f"{mode_cfg.icon} {mode_cfg.display_name}")
LINE 145 |         doc.append(mode_cfg.description)
LINE 146 |     else:
LINE 147 |         doc.append("REPORTED PROBLEM OR GOAL / PROBLEMA REPORTADO U OBJETIVO")
LINE 148 |         doc.append("==============================================================")
LINE 149 |         if problem_desc.strip():
LINE 150 |             doc.append(problem_desc.strip())
LINE 151 |         else:
LINE 152 |             doc.append("[No se especificó una descripción del problema]")
LINE 153 |     doc.append("\n")
LINE 154 | 
LINE 155 |     # SELECTED ANALYSIS PROFILE
LINE 156 |     doc.append("==============================================================")
LINE 157 |     doc.append(f"SELECTED ANALYSIS PROFILE / PERFIL DE ANÁLISIS: {profile.icon} {profile.name}")
LINE 158 |     doc.append("==============================================================")
LINE 159 |     doc.append(f"• Objetivo: {profile.objective}")
LINE 160 |     doc.append(f"• Enfoque: {profile.focus}")
LINE 161 |     doc.append(f"• Prioridades: {profile.priorities}")
LINE 162 |     doc.append(f"• Resultado esperado: {profile.expected_outcome}")
LINE 163 |     doc.append(f"\n⚠️ REGLA DE CONCRECIÓN TÉCNICA: {profile.response_instructions}\n")
LINE 164 | 
LINE 165 |     # 2. PROJECT CONTEXT & SMART SUMMARY
LINE 166 |     doc.append("==============================================================")
LINE 167 |     doc.append("PROJECT CONTEXT / CONTEXTO DEL PROYECTO")
LINE 168 |     doc.append("==============================================================")
LINE 169 |     doc.append(f"• Nombre del Proyecto: {project_name}")
LINE 170 |     doc.append(f"• Ruta Base: {base_path}")
LINE 171 |     doc.append(f"• Fecha de Generación: {gen_date}\n")
LINE 172 | 
LINE 173 |     # PROJECT SUMMARY
LINE 174 |     doc.append("--------------------------------------------------------------")
LINE 175 |     doc.append("PROJECT SUMMARY")
LINE 176 |     doc.append("--------------------------------------------------------------")
LINE 177 |     doc.append(f"Selected files: {included_count}")
LINE 178 |     doc.append("File extensions:")
LINE 179 |     if extension_counts:
LINE 180 |         for ext_name, count in extension_counts.most_common():
LINE 181 |             doc.append(f"  {ext_name}: {count}")
LINE 182 |     else:
LINE 183 |         doc.append("  (Ningún archivo procesado)")
LINE 184 |     doc.append(f"\nTotal lines:\n{total_lines:,}\n")
LINE 185 | 
LINE 186 |     # DEPENDENCIES AND REFERENCES
LINE 187 |     if file_dependencies:
LINE 188 |         doc.append("--------------------------------------------------------------")
LINE 189 |         doc.append("DEPENDENCIES AND REFERENCES")
LINE 190 |         doc.append("--------------------------------------------------------------")
LINE 191 |         for f_name, deps in file_dependencies.items():
LINE 192 |             doc.append(f"• {f_name}:")
LINE 193 |             for dep in deps:
LINE 194 |                 doc.append(f"  - {dep}")
LINE 195 |         doc.append("")
LINE 196 | 
LINE 197 |     # Limits Warning Block
LINE 198 |     if omitted_warnings:
LINE 199 |         doc.append("--------------------------------------------------------------")
LINE 200 |         doc.append("⚠️ ARCHIVOS OMITIDOS POR LÍMITES DE TAMAÑO / OMITTED FILES WARNINGS")
LINE 201 |         doc.append("--------------------------------------------------------------")
LINE 202 |         for warn in omitted_warnings:
LINE 203 |             doc.append(f"File omitted:\n{warn['file']}\nReason:\n{warn['reason']}\n")
LINE 204 | 
LINE 205 |     # Mandatory System Response Format Instructions for DeepSeek
LINE 206 |     if config.include_system_instructions:
LINE 207 |         doc.append("--------------------------------------------------------------")
LINE 208 |         if is_project_mode:
LINE 209 |             doc.append(f"INSTRUCCIONES OBLIGATORIAS PARA DEEPSEEK ({mode_cfg.display_name.upper()})")
LINE 210 |             doc.append("--------------------------------------------------------------")
LINE 211 |             doc.append(mode_cfg.prompt_instructions)
LINE 212 |             doc.append("\nTu respuesta DEBE seguir exactamente la siguiente estructura Markdown adaptada al modo:")
LINE 213 |             doc.append(f"\n{mode_cfg.response_template}\n")
LINE 214 |         else:
LINE 215 |             doc.append(f"INSTRUCCIONES OBLIGATORIAS PARA DEEPSEEK ({profile.name.upper()})")
LINE 216 |             doc.append("--------------------------------------------------------------")
LINE 217 |             doc.append(profile.response_instructions)
LINE 218 |             doc.append("\nTu respuesta DEBE seguir exactamente la siguiente estructura Markdown adaptada al perfil:")
LINE 219 |             doc.append(f"\n{profile.response_template}\n")
LINE 220 |         doc.append("REGLA OBLIGATORIA: No respondas con JSON. Responde con el Markdown estructurado exacto indicado arriba.")
LINE 221 | 
LINE 222 | 
LINE 223 |     if config.include_tree and folder_path and os.path.isdir(folder_path):
LINE 224 |         tree_str = build_folder_tree_str(folder_path, list(selection.checked_folder_files), selection.excluded_dirs)
LINE 225 |         doc.append("\nEstructura de Directorios:")
LINE 226 |         doc.append(f"```\n{tree_str}\n```")
LINE 227 |     
LINE 228 |     doc.append("\n")
LINE 229 | 
LINE 230 |     # 3. ATTACHMENTS
LINE 231 |     doc.append("==============================================================")
LINE 232 |     doc.append("ATTACHMENTS / ARCHIVOS Y CÓDIGO FUENTE")
LINE 233 |     doc.append("==============================================================\n")
LINE 234 |     doc.append("\n\n".join(file_blocks))
LINE 235 | 
LINE 236 |     full_text = "\n".join(doc)
LINE 237 |     return full_text, included_count, excluded_count, oversized_count, total_lines
```

==============================================================
FILE: app/generators/prompt_generator.py
==============================================================
```py
LINE  1 | """Prompt generator orchestrator."""
LINE  2 | from typing import Tuple
LINE  3 | from app.models.project import ProjectSelection, ExportConfig
LINE  4 | from app.generators.markdown_generator import generate_markdown_bundle
LINE  5 | from app.generators.text_generator import generate_text_bundle
LINE  6 | 
LINE  7 | 
LINE  8 | class PromptGenerator:
LINE  9 |     def __init__(self, config: ExportConfig = None):
LINE 10 |         self.config = config or ExportConfig()
LINE 11 | 
LINE 12 |     def generate(self, selection: ProjectSelection, problem_desc: str) -> Tuple[str, int, int, int, int]:
LINE 13 |         """
LINE 14 |         Generates document bundle.
LINE 15 |         Returns: (full_text, included_count, excluded_count, oversized_count, total_lines)
LINE 16 |         """
LINE 17 |         if self.config.output_format == "text":
LINE 18 |             return generate_text_bundle(selection, problem_desc, self.config)
LINE 19 |         return generate_markdown_bundle(selection, problem_desc, self.config)
```

==============================================================
FILE: app/generators/standalone_prompt_generator.py
==============================================================
```py
LINE  1 | """Generates standalone professional prompt deepseek_prompt.md with structured DeepSeek response template."""
LINE  2 | from app.models.analysis_types import get_analysis_profile
LINE  3 | from app.models.analysis_modes import get_analysis_mode_config, MODE_PROJECT, MODE_PROBLEM
LINE  4 | 
LINE  5 | 
LINE  6 | def generate_standalone_prompt(
LINE  7 |     problem_desc: str = "",
LINE  8 |     analysis_type: str = "Detect errors",
LINE  9 |     analysis_mode: str = "problem"
LINE 10 | ) -> str:
LINE 11 |     """
LINE 12 |     Generates a professional copy-paste prompt instructing DeepSeek:
LINE 13 |     - Problem Mode: Focuses exclusively on diagnosing & resolving the specified problem (root cause, solution, code changes).
LINE 14 |     - Project Mode: Audits the project holistically (errors, duplicate code, bad practices, architecture, security, performance).
LINE 15 |     """
LINE 16 |     profile = get_analysis_profile(analysis_type)
LINE 17 |     mode_cfg = get_analysis_mode_config(analysis_mode)
LINE 18 |     is_project_mode = (mode_cfg.mode == MODE_PROJECT)
LINE 19 | 
LINE 20 |     if is_project_mode:
LINE 21 |         problem_block = """==============================================================
LINE 22 | SCOPE OF ANALYSIS / ALCANCE DE AUDITORÍA HOLÍSTICA (MODO PROYECTO)
LINE 23 | ==============================================================
LINE 24 | Realiza una auditoría técnica transversal completa de todo el proyecto adjunto:
LINE 25 | • Detección de errores y bugs latentes en el código.
LINE 26 | • Identificación de código duplicado y deuda técnica (DRY).
LINE 27 | • Malas prácticas de programación e ineficiencias.
LINE 28 | • Deficiencias de arquitectura, acoplamiento indebido y separación de capas.
LINE 29 | • Vulnerabilidades de seguridad (OWASP) y riesgos de exposición.
LINE 30 | • Oportunidades concretas de optimización de rendimiento (CPU, memoria, I/O)."""
LINE 31 |         response_template_to_use = mode_cfg.response_template
LINE 32 |     else:
LINE 33 |         problem_text = problem_desc.strip() if problem_desc.strip() else "[Describe aquí el problema o incidencia que deseas resolver]"
LINE 34 |         problem_block = f"""==============================================================
LINE 35 | REPORTED PROBLEM / PROBLEMA REPORTADO
LINE 36 | ==============================================================
LINE 37 | {problem_text}"""
LINE 38 |         response_template_to_use = profile.response_template
LINE 39 | 
LINE 40 |     prompt = f"""# PROMPT PROFESIONAL PARA DEEPSEEK WEB CHAT
LINE 41 | 
LINE 42 | > **Instrucción para el usuario:** Copia este texto y pégalo directamente en el chat de DeepSeek junto con los archivos adjuntos (`deepseek_project_context.md` o `deepseek_project_context.txt`).
LINE 43 | 
LINE 44 | ==============================================================
LINE 45 | MODO Y PERFIL DE ANÁLISIS SELECCIONADO
LINE 46 | ==============================================================
LINE 47 | • MODO: {mode_cfg.icon} {mode_cfg.display_name}
LINE 48 | • PERFIL: {profile.icon} {profile.name}
LINE 49 | • OBJETIVO: {profile.objective if not is_project_mode else mode_cfg.description}
LINE 50 | • ENFOQUE: {profile.focus}
LINE 51 | • PRIORIDADES: {profile.priorities}
LINE 52 | • RESULTADO ESPERADO: {profile.expected_outcome}
LINE 53 | 
LINE 54 | ⚠️ REGLA DE CONCRECIÓN TÉCNICA Y ACCIÓN:
LINE 55 | {profile.response_instructions}
LINE 56 | 
LINE 57 | {problem_block}
LINE 58 | 
LINE 59 | ==============================================================
LINE 60 | PROJECT CONTEXT / CONTEXTO E INSTRUCCIONES DEL PROYECTO
LINE 61 | ==============================================================
LINE 62 | Hola DeepSeek. Te adjunto el contexto completo de mi proyecto de software para su análisis técnico profesional bajo el modo "{mode_cfg.display_name}".
LINE 63 | 
LINE 64 | ---
LINE 65 | 
LINE 66 | ### 📋 INSTRUCCIONES DE ANÁLISIS ({mode_cfg.mode.upper()} MODE RULES)
LINE 67 | 
LINE 68 | {mode_cfg.prompt_instructions}
LINE 69 | 
LINE 70 | ---
LINE 71 | 
LINE 72 | ### 📐 FORMATO DE RESPUESTA OBLIGATORIO PARA: {mode_cfg.display_name.upper()}
LINE 73 | 
LINE 74 | Tu respuesta DEBE seguir **exactamente** la siguiente estructura Markdown adaptada al modo seleccionado. No respondas con JSON. Esta respuesta la leerá un desarrollador directamente desde el chat web.
LINE 75 | 
LINE 76 | ---
LINE 77 | 
LINE 78 | {response_template_to_use}
LINE 79 | 
LINE 80 | ---
LINE 81 | 
LINE 82 | ==============================================================
LINE 83 | ATTACHMENTS / ARCHIVOS ADJUNTOS
LINE 84 | ==============================================================
LINE 85 | Por favor revisa el archivo de contexto adjunto (`deepseek_project_context.md` / `deepseek_project_context.txt`) que contiene:
LINE 86 | - **Project Summary**: desglose de archivos seleccionados por extensión y total de líneas.
LINE 87 | - **Dependencies and References**: importaciones y dependencias detectadas automáticamente por archivo.
LINE 88 | - **Estructura del Proyecto**: diagrama en árbol jerárquico de carpetas y archivos.
LINE 89 | - **Código Fuente**: contenido de los archivos seleccionados con sus **rutas relativas** y **números de línea originales** (`LINE X | ...`).
LINE 90 | 
LINE 91 | Confirma la recepción del contexto y responde siguiendo **exactamente** el formato estructurado indicado arriba.
LINE 92 | """
LINE 93 |     return prompt
```

==============================================================
FILE: app/generators/text_generator.py
==============================================================
```py
LINE   1 | """Plain text prompt bundle generator with Smart Context (File Extensions Breakdown & Dependencies)."""
LINE   2 | import os
LINE   3 | from collections import Counter
LINE   4 | from datetime import datetime
LINE   5 | from typing import Tuple, List, Dict
LINE   6 | from app.models.project import ProjectSelection, ExportConfig
LINE   7 | from app.core.file_reader import read_and_format_file
LINE   8 | from app.core.project_structure import build_folder_tree_str
LINE   9 | from app.core.dependency_detector import DependencyDetector
LINE  10 | from app.models.analysis_types import get_analysis_profile
LINE  11 | from app.models.analysis_modes import get_analysis_mode_config, MODE_PROJECT
LINE  12 | from app.utils.file_utils import is_binary_file, get_file_size, safe_read_file
LINE  13 | 
LINE  14 | 
LINE  15 | def generate_text_bundle(
LINE  16 |     selection: ProjectSelection, 
LINE  17 |     problem_desc: str, 
LINE  18 |     config: ExportConfig
LINE  19 | ) -> Tuple[str, int, int, int, int]:
LINE  20 |     """
LINE  21 |     Generates plain text document with Smart Context:
LINE  22 |     1. REPORTED PROBLEM
LINE  23 |     2. PROJECT CONTEXT (Metadata, Extension Frequency Summary, Dependencies, Limits Warnings, Tree)
LINE  24 |     3. ATTACHMENTS (Selected Files with LINE X | formatting)
LINE  25 | 
LINE  26 |     Returns: (full_text, included_count, excluded_count, oversized_count, total_lines)
LINE  27 |     """
LINE  28 |     folder_path = selection.folder_path
LINE  29 |     project_name = os.path.basename(folder_path) if folder_path else "Proyecto"
LINE  30 |     base_path = os.path.abspath(folder_path) if folder_path else "N/A"
LINE  31 |     gen_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
LINE  32 | 
LINE  33 |     file_blocks = []
LINE  34 |     omitted_warnings: List[Dict[str, str]] = []
LINE  35 |     extension_counts: Counter = Counter()
LINE  36 |     file_dependencies: Dict[str, List[str]] = {}
LINE  37 | 
LINE  38 |     included_count = 0
LINE  39 |     excluded_count = 0
LINE  40 |     oversized_count = 0
LINE  41 |     total_lines = 0
LINE  42 | 
LINE  43 |     cumulative_bytes = 0
LINE  44 |     max_file_bytes = int(config.max_file_size_mb * 1024 * 1024)
LINE  45 |     max_total_bytes = int(config.max_total_size_mb * 1024 * 1024)
LINE  46 |     detector = DependencyDetector()
LINE  47 | 
LINE  48 |     def process_file(full_path: str, display_name: str):
LINE  49 |         nonlocal included_count, excluded_count, oversized_count, total_lines, cumulative_bytes
LINE  50 | 
LINE  51 |         ext = os.path.splitext(display_name)[1].lower() or "[sin extensión]"
LINE  52 | 
LINE  53 |         if is_binary_file(full_path):
LINE  54 |             excluded_count += 1
LINE  55 |             return
LINE  56 | 
LINE  57 |         size_bytes = get_file_size(full_path)
LINE  58 | 
LINE  59 |         if included_count >= config.max_files:
LINE  60 |             oversized_count += 1
LINE  61 |             omitted_warnings.append({
LINE  62 |                 "file": display_name,
LINE  63 |                 "reason": f"Exceeds MAX_FILES limit of {config.max_files} files."
LINE  64 |             })
LINE  65 |             return
LINE  66 | 
LINE  67 |         if size_bytes > max_file_bytes:
LINE  68 |             oversized_count += 1
LINE  69 |             omitted_warnings.append({
LINE  70 |                 "file": display_name,
LINE  71 |                 "reason": f"Exceeds the allowed limit of {config.max_file_size_mb:g} MB."
LINE  72 |             })
LINE  73 |             return
LINE  74 | 
LINE  75 |         if cumulative_bytes + size_bytes > max_total_bytes:
LINE  76 |             oversized_count += 1
LINE  77 |             omitted_warnings.append({
LINE  78 |                 "file": display_name,
LINE  79 |                 "reason": f"Exceeds MAX_TOTAL_SIZE limit of {config.max_total_size_mb:g} MB (Cumulative size reached)."
LINE  80 |             })
LINE  81 |             return
LINE  82 | 
LINE  83 |         raw_text = safe_read_file(full_path, max_bytes=max_file_bytes)
LINE  84 |         deps = detector.detect_file_dependencies(display_name, raw_text)
LINE  85 |         if deps:
LINE  86 |             file_dependencies[display_name] = deps
LINE  87 | 
LINE  88 |         formatted_code = read_and_format_file(
LINE  89 |             full_path, 
LINE  90 |             add_line_numbers=config.add_line_numbers,
LINE  91 |             max_file_size_mb=config.max_file_size_mb
LINE  92 |         )
LINE  93 |         lines_in_file = formatted_code.count('\n') + (1 if formatted_code else 0)
LINE  94 |         total_lines += lines_in_file
LINE  95 |         cumulative_bytes += size_bytes
LINE  96 |         extension_counts[ext] += 1
LINE  97 |         
LINE  98 |         block = [
LINE  99 |             "==============================================================",
LINE 100 |             f"FILE: {display_name}",
LINE 101 |             "==============================================================",
LINE 102 |             formatted_code
LINE 103 |         ]
LINE 104 |         file_blocks.append("\n".join(block))
LINE 105 |         included_count += 1
LINE 106 | 
LINE 107 |     # 1. Folder files
LINE 108 |     if folder_path and os.path.isdir(folder_path):
LINE 109 |         for rel_f in sorted(selection.checked_folder_files):
LINE 110 |             full_path = os.path.join(folder_path, rel_f)
LINE 111 |             if os.path.isfile(full_path):
LINE 112 |                 process_file(full_path, rel_f)
LINE 113 | 
LINE 114 |     # 2. Individual files
LINE 115 |     for abs_f in selection.individual_files:
LINE 116 |         if os.path.isfile(abs_f):
LINE 117 |             if folder_path and abs_f.startswith(folder_path):
LINE 118 |                 display_name = os.path.relpath(abs_f, folder_path)
LINE 119 |             else:
LINE 120 |                 display_name = os.path.basename(abs_f)
LINE 121 |             process_file(abs_f, display_name)
LINE 122 | 
LINE 123 |     analysis_type = getattr(config, "analysis_type", "Detect errors")
LINE 124 |     analysis_mode = getattr(config, "analysis_mode", "problem")
LINE 125 |     profile = get_analysis_profile(analysis_type)
LINE 126 |     mode_cfg = get_analysis_mode_config(analysis_mode)
LINE 127 |     is_project_mode = (mode_cfg.mode == MODE_PROJECT)
LINE 128 | 
LINE 129 |     doc = []
LINE 130 | 
LINE 131 |     # 1. REPORTED PROBLEM / HOLISTIC AUDIT SCOPE
LINE 132 |     doc.append("==============================================================")
LINE 133 |     if is_project_mode:
LINE 134 |         doc.append("HOLISTIC PROJECT AUDIT / AUDITORÍA HOLÍSTICA DEL PROYECTO")
LINE 135 |         doc.append("==============================================================")
LINE 136 |         doc.append(f"{mode_cfg.icon} {mode_cfg.display_name}")
LINE 137 |         doc.append(mode_cfg.description)
LINE 138 |     else:
LINE 139 |         doc.append("REPORTED PROBLEM OR GOAL / PROBLEMA REPORTADO U OBJETIVO")
LINE 140 |         doc.append("==============================================================")
LINE 141 |         if problem_desc.strip():
LINE 142 |             doc.append(problem_desc.strip())
LINE 143 |         else:
LINE 144 |             doc.append("[No se especificó una descripción del problema]")
LINE 145 |     doc.append("\n")
LINE 146 | 
LINE 147 |     # SELECTED ANALYSIS PROFILE
LINE 148 |     doc.append("==============================================================")
LINE 149 |     doc.append(f"SELECTED ANALYSIS PROFILE / PERFIL DE ANÁLISIS: {profile.icon} {profile.name}")
LINE 150 |     doc.append("==============================================================")
LINE 151 |     doc.append(f"• Objetivo: {profile.objective}")
LINE 152 |     doc.append(f"• Enfoque: {profile.focus}")
LINE 153 |     doc.append(f"• Prioridades: {profile.priorities}")
LINE 154 |     doc.append(f"• Resultado esperado: {profile.expected_outcome}")
LINE 155 |     doc.append(f"\n⚠️ REGLA DE CONCRECIÓN TÉCNICA: {profile.response_instructions}\n")
LINE 156 | 
LINE 157 | 
LINE 158 |     # 2. PROJECT CONTEXT & SMART SUMMARY
LINE 159 |     doc.append("==============================================================")
LINE 160 |     doc.append("PROJECT CONTEXT / CONTEXTO DEL PROYECTO")
LINE 161 |     doc.append("==============================================================")
LINE 162 |     doc.append(f"• Nombre del Proyecto: {project_name}")
LINE 163 |     doc.append(f"• Ruta Base: {base_path}")
LINE 164 |     doc.append(f"• Fecha de Generación: {gen_date}\n")
LINE 165 | 
LINE 166 |     # PROJECT SUMMARY
LINE 167 |     doc.append("--------------------------------------------------------------")
LINE 168 |     doc.append("PROJECT SUMMARY")
LINE 169 |     doc.append("--------------------------------------------------------------")
LINE 170 |     doc.append(f"Selected files: {included_count}")
LINE 171 |     doc.append("File extensions:")
LINE 172 |     if extension_counts:
LINE 173 |         for ext_name, count in extension_counts.most_common():
LINE 174 |             doc.append(f"  {ext_name}: {count}")
LINE 175 |     else:
LINE 176 |         doc.append("  (Ningún archivo procesado)")
LINE 177 |     doc.append(f"\nTotal lines:\n{total_lines:,}\n")
LINE 178 | 
LINE 179 |     # DEPENDENCIES AND REFERENCES
LINE 180 |     if file_dependencies:
LINE 181 |         doc.append("--------------------------------------------------------------")
LINE 182 |         doc.append("DEPENDENCIES AND REFERENCES")
LINE 183 |         doc.append("--------------------------------------------------------------")
LINE 184 |         for f_name, deps in file_dependencies.items():
LINE 185 |             doc.append(f"• {f_name}:")
LINE 186 |             for dep in deps:
LINE 187 |                 doc.append(f"  - {dep}")
LINE 188 |         doc.append("")
LINE 189 | 
LINE 190 |     if omitted_warnings:
LINE 191 |         doc.append("--------------------------------------------------------------")
LINE 192 |         doc.append("⚠️ ARCHIVOS OMITIDOS POR LÍMITES DE TAMAÑO / OMITTED FILES WARNINGS")
LINE 193 |         doc.append("--------------------------------------------------------------")
LINE 194 |         for warn in omitted_warnings:
LINE 195 |             doc.append(f"File omitted:\n{warn['file']}\nReason:\n{warn['reason']}\n")
LINE 196 | 
LINE 197 |     if config.include_system_instructions:
LINE 198 |         doc.append("--------------------------------------------------------------")
LINE 199 |         if is_project_mode:
LINE 200 |             doc.append(f"INSTRUCCIONES OBLIGATORIAS PARA DEEPSEEK ({mode_cfg.display_name.upper()})")
LINE 201 |             doc.append("--------------------------------------------------------------")
LINE 202 |             doc.append(mode_cfg.prompt_instructions)
LINE 203 |             doc.append("\nTu respuesta DEBE seguir exactamente la siguiente estructura Markdown adaptada al modo:")
LINE 204 |             doc.append(f"\n{mode_cfg.response_template}\n")
LINE 205 |         else:
LINE 206 |             doc.append(f"INSTRUCCIONES OBLIGATORIAS PARA DEEPSEEK ({profile.name.upper()})")
LINE 207 |             doc.append("--------------------------------------------------------------")
LINE 208 |             doc.append(profile.response_instructions)
LINE 209 |             doc.append("\nTu respuesta DEBE seguir exactamente la siguiente estructura Markdown adaptada al perfil:")
LINE 210 |             doc.append(f"\n{profile.response_template}\n")
LINE 211 |         doc.append("REGLA OBLIGATORIA: No respondas con JSON. Responde con el formato estructurado exacto indicado arriba.")
LINE 212 | 
LINE 213 | 
LINE 214 |     if config.include_tree and folder_path and os.path.isdir(folder_path):
LINE 215 |         tree_str = build_folder_tree_str(folder_path, list(selection.checked_folder_files), selection.excluded_dirs)
LINE 216 |         doc.append("\nEstructura de Directorios:")
LINE 217 |         doc.append(f"{tree_str}")
LINE 218 |     
LINE 219 |     doc.append("\n")
LINE 220 | 
LINE 221 |     # 3. ATTACHMENTS
LINE 222 |     doc.append("==============================================================")
LINE 223 |     doc.append("ATTACHMENTS / ARCHIVOS Y CÓDIGO FUENTE")
LINE 224 |     doc.append("==============================================================\n")
LINE 225 |     doc.append("\n\n".join(file_blocks))
LINE 226 | 
LINE 227 |     full_text = "\n".join(doc)
LINE 228 |     return full_text, included_count, excluded_count, oversized_count, total_lines
```

==============================================================
FILE: app/gui/__init__.py
==============================================================
```py
LINE 1 | """GUI package initialization."""
LINE 2 | from app.gui.file_tree import CheckboxTreeview
LINE 3 | from app.gui.main_window import MainWindow
LINE 4 | 
LINE 5 | __all__ = ["CheckboxTreeview", "MainWindow"]
```

==============================================================
FILE: app/gui/analysis_dialog.py
==============================================================
```py
LINE   1 | """
LINE   2 | Project Analysis Dialog GUI component.
LINE   3 | Displays comprehensive project diagnostics, architecture, detected dependencies,
LINE   4 | recommended file selection with interactive checkboxes, and excluded directories.
LINE   5 | """
LINE   6 | import tkinter as tk
LINE   7 | from tkinter import ttk, scrolledtext
LINE   8 | from typing import List, Callable, Optional, Dict
LINE   9 | 
LINE  10 | from app.core.project_analyzer import ProjectAnalysisResult
LINE  11 | from app.utils.file_utils import copy_to_clipboard, format_bytes
LINE  12 | 
LINE  13 | # Colour palette (aligned with main_window.py)
LINE  14 | C_BG        = "#1e2330"
LINE  15 | C_PANEL     = "#252b3b"
LINE  16 | C_BORDER    = "#323a50"
LINE  17 | C_ACCENT    = "#4f8ef7"
LINE  18 | C_ACCENT_DK = "#3a6fcc"
LINE  19 | C_SUCCESS   = "#3ecf8e"
LINE  20 | C_WARN      = "#f5a623"
LINE  21 | C_TEXT      = "#e8eaf0"
LINE  22 | C_TEXT2     = "#8b92a8"
LINE  23 | C_ENTRY     = "#2a3148"
LINE  24 | C_TREE_SEL  = "#2f3d5c"
LINE  25 | C_STAT_BG   = "#161b28"
LINE  26 | 
LINE  27 | 
LINE  28 | class ProjectAnalysisDialog(tk.Toplevel):
LINE  29 |     """Modal dialog displaying project analysis report and recommended selection."""
LINE  30 | 
LINE  31 |     def __init__(
LINE  32 |         self,
LINE  33 |         parent: tk.Tk,
LINE  34 |         analysis: ProjectAnalysisResult,
LINE  35 |         on_apply_selection: Optional[Callable[[List[str]], None]] = None
LINE  36 |     ):
LINE  37 |         super().__init__(parent)
LINE  38 |         self.analysis = analysis
LINE  39 |         self.on_apply_selection = on_apply_selection
LINE  40 |         self.file_vars: Dict[str, tk.BooleanVar] = {}
LINE  41 | 
LINE  42 |         self.title(f"🔬 Análisis del Proyecto: {analysis.project_name}")
LINE  43 |         self.geometry("980x740")
LINE  44 |         self.minsize(800, 550)
LINE  45 |         self.configure(bg=C_BG)
LINE  46 | 
LINE  47 |         # Make dialog modal and centered
LINE  48 |         self.transient(parent)
LINE  49 |         self.grab_set()
LINE  50 |         self._center_window(parent)
LINE  51 | 
LINE  52 |         self._build_header()
LINE  53 |         self._build_tabs()
LINE  54 |         self._build_bottom_bar()
LINE  55 | 
LINE  56 |     def _center_window(self, parent: tk.Tk):
LINE  57 |         self.update_idletasks()
LINE  58 |         try:
LINE  59 |             pw = parent.winfo_width()
LINE  60 |             ph = parent.winfo_height()
LINE  61 |             px = parent.winfo_rootx()
LINE  62 |             py = parent.winfo_rooty()
LINE  63 |             w = self.winfo_width()
LINE  64 |             h = self.winfo_height()
LINE  65 |             x = px + max(0, (pw - w) // 2)
LINE  66 |             y = py + max(0, (ph - h) // 2)
LINE  67 |             self.geometry(f"{w}x{h}+{x}+{y}")
LINE  68 |         except Exception:
LINE  69 |             pass
LINE  70 | 
LINE  71 |     def _build_header(self):
LINE  72 |         hdr = tk.Frame(self, bg=C_PANEL, padx=16, pady=12, highlightthickness=1, highlightbackground=C_BORDER)
LINE  73 |         hdr.pack(fill=tk.X)
LINE  74 | 
LINE  75 |         left = tk.Frame(hdr, bg=C_PANEL)
LINE  76 |         left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
LINE  77 | 
LINE  78 |         tk.Label(
LINE  79 |             left,
LINE  80 |             text=f"🔬  Análisis Automático: {self.analysis.project_name}",
LINE  81 |             font=("Segoe UI", 13, "bold"),
LINE  82 |             bg=C_PANEL, fg=C_TEXT
LINE  83 |         ).pack(anchor="w")
LINE  84 | 
LINE  85 |         tk.Label(
LINE  86 |             left,
LINE  87 |             text=self.analysis.folder_path,
LINE  88 |             font=("Consolas", 8),
LINE  89 |             bg=C_PANEL, fg=C_TEXT2
LINE  90 |         ).pack(anchor="w", pady=(2, 0))
LINE  91 | 
LINE  92 |         # Badges on right
LINE  93 |         badges = tk.Frame(hdr, bg=C_PANEL)
LINE  94 |         badges.pack(side=tk.RIGHT, padx=4)
LINE  95 | 
LINE  96 |         def _make_badge(parent, text, bg_color, fg_color="#ffffff"):
LINE  97 |             f = tk.Frame(parent, bg=bg_color, padx=8, pady=4)
LINE  98 |             f.pack(side=tk.LEFT, padx=3)
LINE  99 |             tk.Label(f, text=text, font=("Segoe UI", 8, "bold"), bg=bg_color, fg=fg_color).pack()
LINE 100 | 
LINE 101 |         # Language badge
LINE 102 |         _make_badge(badges, f"💻 {self.analysis.primary_language}", C_ACCENT)
LINE 103 |         # Framework badge
LINE 104 |         if self.analysis.framework and self.analysis.framework != "No detectado":
LINE 105 |             _make_badge(badges, f"⚡ {self.analysis.framework}", "#8e44ad")
LINE 106 |         # Package manager badge
LINE 107 |         if self.analysis.package_manager and self.analysis.package_manager != "Ninguno detectado":
LINE 108 |             _make_badge(badges, f"📦 {self.analysis.package_manager}", "#27ae60")
LINE 109 | 
LINE 110 |     def _build_tabs(self):
LINE 111 |         style = ttk.Style(self)
LINE 112 |         style.configure("Analysis.TNotebook", background=C_BG, borderwidth=0)
LINE 113 |         style.configure("Analysis.TNotebook.Tab", background=C_PANEL, foreground=C_TEXT, padding=(12, 6), font=("Segoe UI", 9, "bold"))
LINE 114 |         style.map("Analysis.TNotebook.Tab",
LINE 115 |                   background=[("selected", C_ACCENT), ("active", C_BORDER)],
LINE 116 |                   foreground=[("selected", "#ffffff"), ("active", C_TEXT)])
LINE 117 | 
LINE 118 |         notebook = ttk.Notebook(self, style="Analysis.TNotebook")
LINE 119 |         notebook.pack(fill=tk.BOTH, expand=True, padx=12, pady=8)
LINE 120 | 
LINE 121 |         # Tab 1: Recommended Selection
LINE 122 |         tab_recommend = tk.Frame(notebook, bg=C_BG)
LINE 123 |         notebook.add(tab_recommend, text="🎯 Selección Recomendada")
LINE 124 |         self._build_recommendation_tab(tab_recommend)
LINE 125 | 
LINE 126 |         # Tab 2: Full Architecture & Diagnostics
LINE 127 |         tab_report = tk.Frame(notebook, bg=C_BG)
LINE 128 |         notebook.add(tab_report, text="📊 Diagnóstico del Proyecto")
LINE 129 |         self._build_report_tab(tab_report)
LINE 130 | 
LINE 131 |     # ── Tab 1: Recommended Selection ──────────────────────────────────────
LINE 132 |     def _build_recommendation_tab(self, parent: tk.Frame):
LINE 133 |         paned = ttk.PanedWindow(parent, orient=tk.HORIZONTAL)
LINE 134 |         paned.pack(fill=tk.BOTH, expand=True, padx=4, pady=4)
LINE 135 | 
LINE 136 |         # Left Column: Recommended files with checkboxes
LINE 137 |         left_frame = tk.Frame(paned, bg=C_PANEL, padx=10, pady=8)
LINE 138 |         paned.add(left_frame, weight=3)
LINE 139 | 
LINE 140 |         top_bar = tk.Frame(left_frame, bg=C_PANEL)
LINE 141 |         top_bar.pack(fill=tk.X, pady=(0, 6))
LINE 142 | 
LINE 143 |         tk.Label(
LINE 144 |             top_bar,
LINE 145 |             text="Archivos recomendados para analizar",
LINE 146 |             font=("Segoe UI", 10, "bold"),
LINE 147 |             bg=C_PANEL, fg=C_ACCENT
LINE 148 |         ).pack(side=tk.LEFT)
LINE 149 | 
LINE 150 |         self.lbl_selected_count = tk.Label(
LINE 151 |             top_bar,
LINE 152 |             text="",
LINE 153 |             font=("Segoe UI", 8, "italic"),
LINE 154 |             bg=C_PANEL, fg=C_TEXT2
LINE 155 |         )
LINE 156 |         self.lbl_selected_count.pack(side=tk.RIGHT)
LINE 157 | 
LINE 158 |         btn_row = tk.Frame(left_frame, bg=C_PANEL)
LINE 159 |         btn_row.pack(fill=tk.X, pady=(0, 6))
LINE 160 | 
LINE 161 |         ttk.Button(btn_row, text="☑ Marcar todos", style="Neutral.TButton",
LINE 162 |                    command=self._select_all_recommended).pack(side=tk.LEFT, padx=(0, 4))
LINE 163 |         ttk.Button(btn_row, text="☐ Desmarcar todos", style="Neutral.TButton",
LINE 164 |                    command=self._deselect_all_recommended).pack(side=tk.LEFT)
LINE 165 | 
LINE 166 |         # Scrollable checkboxes list
LINE 167 |         list_container = tk.Frame(left_frame, bg=C_ENTRY, bd=1, relief="flat", highlightbackground=C_BORDER, highlightthickness=1)
LINE 168 |         list_container.pack(fill=tk.BOTH, expand=True)
LINE 169 | 
LINE 170 |         canvas = tk.Canvas(list_container, bg=C_ENTRY, bd=0, highlightthickness=0)
LINE 171 |         scrollbar = ttk.Scrollbar(list_container, orient=tk.VERTICAL, command=canvas.yview)
LINE 172 |         scroll_frame = tk.Frame(canvas, bg=C_ENTRY)
LINE 173 | 
LINE 174 |         scroll_frame.bind(
LINE 175 |             "<Configure>",
LINE 176 |             lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
LINE 177 |         )
LINE 178 |         canvas_window = canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
LINE 179 | 
LINE 180 |         def _on_canvas_resize(event):
LINE 181 |             canvas.itemconfig(canvas_window, width=event.width)
LINE 182 |         canvas.bind("<Configure>", _on_canvas_resize)
LINE 183 | 
LINE 184 |         # Mousewheel scroll binding
LINE 185 |         def _on_mousewheel(event):
LINE 186 |             if event.delta:
LINE 187 |                 canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
LINE 188 |             elif event.num == 4:
LINE 189 |                 canvas.yview_scroll(-1, "units")
LINE 190 |             elif event.num == 5:
LINE 191 |                 canvas.yview_scroll(1, "units")
LINE 192 | 
LINE 193 |         canvas.bind_all("<MouseWheel>", _on_mousewheel)
LINE 194 |         canvas.bind_all("<Button-4>", _on_mousewheel)
LINE 195 |         canvas.bind_all("<Button-5>", _on_mousewheel)
LINE 196 | 
LINE 197 |         canvas.configure(yscrollcommand=scrollbar.set)
LINE 198 |         scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
LINE 199 |         canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
LINE 200 | 
LINE 201 |         # Populate recommended files checkboxes
LINE 202 |         if not self.analysis.recommended_files:
LINE 203 |             tk.Label(
LINE 204 |                 scroll_frame,
LINE 205 |                 text="(No se encontraron archivos recomendados)",
LINE 206 |                 bg=C_ENTRY, fg=C_TEXT2, font=("Segoe UI", 9, "italic")
LINE 207 |             ).pack(anchor="w", padx=10, pady=10)
LINE 208 |         else:
LINE 209 |             for rel_file in self.analysis.recommended_files:
LINE 210 |                 var = tk.BooleanVar(value=True)  # Pre-checked by default!
LINE 211 |                 self.file_vars[rel_file] = var
LINE 212 | 
LINE 213 |                 row = tk.Frame(scroll_frame, bg=C_ENTRY, padx=6, pady=2)
LINE 214 |                 row.pack(fill=tk.X)
LINE 215 | 
LINE 216 |                 cb = tk.Checkbutton(
LINE 217 |                     row,
LINE 218 |                     text=f"✓  {rel_file}",
LINE 219 |                     variable=var,
LINE 220 |                     font=("Consolas", 9),
LINE 221 |                     bg=C_ENTRY,
LINE 222 |                     fg=C_TEXT,
LINE 223 |                     activebackground=C_ENTRY,
LINE 224 |                     activeforeground=C_ACCENT,
LINE 225 |                     selectcolor=C_PANEL,
LINE 226 |                     anchor="w",
LINE 227 |                     command=self._update_selected_count
LINE 228 |                 )
LINE 229 |                 cb.pack(side=tk.LEFT, fill=tk.X, expand=True)
LINE 230 | 
LINE 231 |         self._update_selected_count()
LINE 232 | 
LINE 233 |         # Right Column: Excluded directories & summary hints
LINE 234 |         right_frame = tk.Frame(paned, bg=C_PANEL, padx=10, pady=8)
LINE 235 |         paned.add(right_frame, weight=2)
LINE 236 | 
LINE 237 |         tk.Label(
LINE 238 |             right_frame,
LINE 239 |             text="Directorios Excluidos",
LINE 240 |             font=("Segoe UI", 10, "bold"),
LINE 241 |             bg=C_PANEL, fg=C_WARN
LINE 242 |         ).pack(anchor="w", pady=(0, 6))
LINE 243 | 
LINE 244 |         tk.Label(
LINE 245 |             right_frame,
LINE 246 |             text="Estos directorios se omiten automáticamente para evitar archivos irrelevantes o pesados:",
LINE 247 |             font=("Segoe UI", 8),
LINE 248 |             bg=C_PANEL, fg=C_TEXT2, wraplength=260, justify=tk.LEFT
LINE 249 |         ).pack(anchor="w", pady=(0, 8))
LINE 250 | 
LINE 251 |         excl_box = tk.Frame(right_frame, bg=C_ENTRY, padx=8, pady=8, highlightbackground=C_BORDER, highlightthickness=1)
LINE 252 |         excl_box.pack(fill=tk.BOTH, expand=True)
LINE 253 | 
LINE 254 |         # List excluded directories
LINE 255 |         excl_list = sorted(list(self.analysis.configured_exclusions))
LINE 256 |         for d in excl_list:
LINE 257 |             is_present = d in self.analysis.excluded_dirs_found
LINE 258 |             fg = C_WARN if is_present else C_TEXT2
LINE 259 |             mark = "⚠️" if is_present else "•"
LINE 260 |             extra = " (detectado)" if is_present else ""
LINE 261 |             lbl = tk.Label(
LINE 262 |                 excl_box,
LINE 263 |                 text=f"{mark} {d}/{extra}",
LINE 264 |                 font=("Consolas", 8, "bold" if is_present else "normal"),
LINE 265 |                 bg=C_ENTRY, fg=fg, anchor="w"
LINE 266 |             )
LINE 267 |             lbl.pack(anchor="w", pady=1)
LINE 268 | 
LINE 269 |         # Quick Tip Box
LINE 270 |         tip_box = tk.Frame(right_frame, bg="#1a2538", padx=8, pady=8, highlightbackground=C_ACCENT, highlightthickness=1)
LINE 271 |         tip_box.pack(fill=tk.X, pady=(10, 0))
LINE 272 | 
LINE 273 |         tk.Label(
LINE 274 |             tip_box,
LINE 275 |             text="💡 Consejo:",
LINE 276 |             font=("Segoe UI", 8, "bold"),
LINE 277 |             bg="#1a2538", fg=C_ACCENT
LINE 278 |         ).pack(anchor="w")
LINE 279 | 
LINE 280 |         tk.Label(
LINE 281 |             tip_box,
LINE 282 |             text="Presiona 'Aplicar selección' para transferir estos archivos seleccionados directamente a la ventana principal. El prompt se generará solo con ellos.",
LINE 283 |             font=("Segoe UI", 8),
LINE 284 |             bg="#1a2538", fg=C_TEXT, wraplength=250, justify=tk.LEFT
LINE 285 |         ).pack(anchor="w", pady=(2, 0))
LINE 286 | 
LINE 287 |     def _select_all_recommended(self):
LINE 288 |         for var in self.file_vars.values():
LINE 289 |             var.set(True)
LINE 290 |         self._update_selected_count()
LINE 291 | 
LINE 292 |     def _deselect_all_recommended(self):
LINE 293 |         for var in self.file_vars.values():
LINE 294 |             var.set(False)
LINE 295 |         self._update_selected_count()
LINE 296 | 
LINE 297 |     def _update_selected_count(self):
LINE 298 |         checked = sum(1 for v in self.file_vars.values() if v.get())
LINE 299 |         total = len(self.file_vars)
LINE 300 |         self.lbl_selected_count.config(text=f"{checked} de {total} seleccionados")
LINE 301 | 
LINE 302 |     def get_selected_recommended_files(self) -> List[str]:
LINE 303 |         return [f for f, var in self.file_vars.items() if var.get()]
LINE 304 | 
LINE 305 |     # ── Tab 2: Full Architecture & Diagnostics ────────────────────────────
LINE 306 |     def _build_report_tab(self, parent: tk.Frame):
LINE 307 |         report_text = scrolledtext.ScrolledText(
LINE 308 |             parent,
LINE 309 |             wrap=tk.WORD,
LINE 310 |             font=("Consolas", 9),
LINE 311 |             bg=C_ENTRY,
LINE 312 |             fg=C_TEXT,
LINE 313 |             insertbackground=C_TEXT,
LINE 314 |             selectbackground=C_TREE_SEL,
LINE 315 |             selectforeground=C_TEXT,
LINE 316 |             relief="flat",
LINE 317 |             bd=0,
LINE 318 |             padx=12,
LINE 319 |             pady=10
LINE 320 |         )
LINE 321 |         report_text.pack(fill=tk.BOTH, expand=True, padx=4, pady=4)
LINE 322 |         report_text.insert(tk.END, self.analysis.to_formatted_report())
LINE 323 |         report_text.config(state="disabled")
LINE 324 | 
LINE 325 |     # ── Bottom Bar ────────────────────────────────────────────────────────
LINE 326 |     def _build_bottom_bar(self):
LINE 327 |         bottom = tk.Frame(self, bg=C_STAT_BG, padx=14, pady=10, highlightthickness=1, highlightbackground=C_BORDER)
LINE 328 |         bottom.pack(fill=tk.X, side=tk.BOTTOM)
LINE 329 | 
LINE 330 |         # Left side buttons
LINE 331 |         if self.on_apply_selection:
LINE 332 |             ttk.Button(
LINE 333 |                 bottom,
LINE 334 |                 text="✅ Aplicar selección",
LINE 335 |                 style="Success.TButton",
LINE 336 |                 command=self._on_apply_clicked
LINE 337 |             ).pack(side=tk.LEFT, padx=(0, 6))
LINE 338 | 
LINE 339 |         ttk.Button(
LINE 340 |             bottom,
LINE 341 |             text="📋 Copiar reporte",
LINE 342 |             style="Neutral.TButton",
LINE 343 |             command=self._on_copy_report
LINE 344 |         ).pack(side=tk.LEFT, padx=(0, 6))
LINE 345 | 
LINE 346 |         # Right side button
LINE 347 |         ttk.Button(
LINE 348 |             bottom,
LINE 349 |             text="Cerrar",
LINE 350 |             style="Neutral.TButton",
LINE 351 |             command=self.destroy
LINE 352 |         ).pack(side=tk.RIGHT)
LINE 353 | 
LINE 354 |     def _on_apply_clicked(self):
LINE 355 |         selected = self.get_selected_recommended_files()
LINE 356 |         if self.on_apply_selection:
LINE 357 |             self.on_apply_selection(selected)
LINE 358 |         self.destroy()
LINE 359 | 
LINE 360 |     def _on_copy_report(self):
LINE 361 |         report = self.analysis.to_formatted_report()
LINE 362 |         copy_to_clipboard(self, report)
```

==============================================================
FILE: app/gui/dependency_tree_dialog.py
==============================================================
```py
LINE   1 | """Dependency tree dialog. Reuses CheckboxTreeview and integrates with existing file selection."""
LINE   2 | import tkinter as tk
LINE   3 | from tkinter import ttk
LINE   4 | from typing import Callable, List, Optional, Set
LINE   5 | 
LINE   6 | from app.core.dependency_graph import DependencyResolver, DependencyNode
LINE   7 | from app.gui.file_tree import CheckboxTreeview
LINE   8 | 
LINE   9 | C_BG = "#1e2330"
LINE  10 | C_PANEL = "#252b3b"
LINE  11 | C_BORDER = "#323a50"
LINE  12 | C_ACCENT = "#4f8ef7"
LINE  13 | C_TEXT = "#e8eaf0"
LINE  14 | C_TEXT2 = "#8b92a8"
LINE  15 | C_ENTRY = "#2a3148"
LINE  16 | 
LINE  17 | 
LINE  18 | class DependencyTreeDialog(tk.Toplevel):
LINE  19 |     def __init__(
LINE  20 |         self,
LINE  21 |         parent: tk.Tk,
LINE  22 |         folder_path: str,
LINE  23 |         root_rel_path: str,
LINE  24 |         excluded_dirs: Optional[Set[str]] = None,
LINE  25 |         on_apply_selection: Optional[Callable[[List[str]], None]] = None,
LINE  26 |     ):
LINE  27 |         super().__init__(parent)
LINE  28 |         self.folder_path = folder_path
LINE  29 |         self.root_rel_path = root_rel_path
LINE  30 |         self.on_apply_selection = on_apply_selection
LINE  31 | 
LINE  32 |         self.title(f"🌳 Dependencias: {root_rel_path}")
LINE  33 |         self.geometry("900x650")
LINE  34 |         self.minsize(700, 480)
LINE  35 |         self.configure(bg=C_BG)
LINE  36 | 
LINE  37 |         self.transient(parent)
LINE  38 |         self.grab_set()
LINE  39 | 
LINE  40 |         try:
LINE  41 |             self.resolver = DependencyResolver(folder_path, excluded_dirs=excluded_dirs)
LINE  42 |             self.root_node = self.resolver.build_tree(root_rel_path)
LINE  43 |         except Exception as exc:
LINE  44 |             tk.Label(
LINE  45 |                 self,
LINE  46 |                 text=f"Error al construir árbol: {exc}",
LINE  47 |                 bg=C_BG, fg=C_TEXT, font=("Segoe UI", 10),
LINE  48 |             ).pack(padx=20, pady=20)
LINE  49 |             self.root_node = None
LINE  50 | 
LINE  51 |         self._build_header()
LINE  52 |         self._build_tree()
LINE  53 |         self._build_buttons()
LINE  54 | 
LINE  55 |         if self.root_node is not None:
LINE  56 |             self._insert_node("", self.root_node, is_root=True)
LINE  57 | 
LINE  58 |     def _build_header(self):
LINE  59 |         hdr = tk.Frame(self, bg=C_PANEL, padx=14, pady=10)
LINE  60 |         hdr.pack(fill=tk.X)
LINE  61 | 
LINE  62 |         tk.Label(
LINE  63 |             hdr,
LINE  64 |             text=f"🌳 Árbol de dependencias: {self.root_rel_path}",
LINE  65 |             font=("Segoe UI", 12, "bold"),
LINE  66 |             bg=C_PANEL,
LINE  67 |             fg=C_TEXT,
LINE  68 |         ).pack(anchor="w")
LINE  69 | 
LINE  70 |         tk.Label(
LINE  71 |             hdr,
LINE  72 |             text="Selecciona archivos o ramas y aplícalos al contexto principal.",
LINE  73 |             font=("Segoe UI", 8),
LINE  74 |             bg=C_PANEL,
LINE  75 |             fg=C_TEXT2,
LINE  76 |         ).pack(anchor="w")
LINE  77 | 
LINE  78 |     def _build_tree(self):
LINE  79 |         container = tk.Frame(self, bg=C_BG, padx=10, pady=6)
LINE  80 |         container.pack(fill=tk.BOTH, expand=True)
LINE  81 | 
LINE  82 |         self.tree = CheckboxTreeview(container)
LINE  83 |         sy = ttk.Scrollbar(container, orient=tk.VERTICAL, command=self.tree.yview)
LINE  84 |         sx = ttk.Scrollbar(container, orient=tk.HORIZONTAL, command=self.tree.xview)
LINE  85 |         self.tree.configure(yscrollcommand=sy.set, xscrollcommand=sx.set)
LINE  86 | 
LINE  87 |         sy.pack(side=tk.RIGHT, fill=tk.Y)
LINE  88 |         sx.pack(side=tk.BOTTOM, fill=tk.X)
LINE  89 |         self.tree.pack(fill=tk.BOTH, expand=True)
LINE  90 | 
LINE  91 |     def _build_buttons(self):
LINE  92 |         bar = tk.Frame(self, bg=C_PANEL, padx=10, pady=8)
LINE  93 |         bar.pack(fill=tk.X, side=tk.BOTTOM)
LINE  94 | 
LINE  95 |         ttk.Button(bar, text="Seleccionar raíz", command=self._select_root).pack(side=tk.LEFT, padx=2)
LINE  96 |         ttk.Button(bar, text="Seleccionar rama", command=self._select_branch).pack(side=tk.LEFT, padx=2)
LINE  97 |         ttk.Button(bar, text="Seleccionar todos", command=self._select_all).pack(side=tk.LEFT, padx=2)
LINE  98 |         ttk.Button(bar, text="Deseleccionar rama", command=self._deselect_branch).pack(side=tk.LEFT, padx=2)
LINE  99 | 
LINE 100 |         ttk.Button(bar, text="✅ Aplicar selección", command=self._apply).pack(side=tk.RIGHT, padx=2)
LINE 101 |         ttk.Button(bar, text="Cerrar", command=self.destroy).pack(side=tk.RIGHT, padx=2)
LINE 102 | 
LINE 103 |     def _insert_node(self, parent_item: str, node: DependencyNode, is_root: bool = False):
LINE 104 |         notes = []
LINE 105 |         if node.is_cycle:
LINE 106 |             notes.append("⟲ ciclo")
LINE 107 |         if node.is_repeated:
LINE 108 |             notes.append("♻ ya analizado")
LINE 109 | 
LINE 110 |         icon = "📄"
LINE 111 |         if node.is_cycle:
LINE 112 |             icon = "🔁"
LINE 113 |         elif node.is_repeated:
LINE 114 |             icon = "🔂"
LINE 115 |         elif node.children:
LINE 116 |             icon = "📂"
LINE 117 | 
LINE 118 |         item = self.tree.insert(
LINE 119 |             parent_item,
LINE 120 |             "end",
LINE 121 |             text=icon,
LINE 122 |             values=("☐", node.rel_path),
LINE 123 |             tags=("unchecked",),
LINE 124 |         )
LINE 125 | 
LINE 126 |         for child in node.children:
LINE 127 |             self._insert_node(item, child)
LINE 128 | 
LINE 129 |         return item
LINE 130 | 
LINE 131 |     def _current_item(self):
LINE 132 |         sel = self.tree.selection()
LINE 133 |         return sel[0] if sel else None
LINE 134 | 
LINE 135 |     def _select_root(self):
LINE 136 |         if self.tree.get_children():
LINE 137 |             root = self.tree.get_children()[0]
LINE 138 |             self.tree.check_item(root)
LINE 139 | 
LINE 140 |     def _select_branch(self):
LINE 141 |         item = self._current_item()
LINE 142 |         if item:
LINE 143 |             self.tree.check_item(item)
LINE 144 | 
LINE 145 |     def _select_all(self):
LINE 146 |         self.tree.select_all()
LINE 147 | 
LINE 148 |     def _deselect_branch(self):
LINE 149 |         item = self._current_item()
LINE 150 |         if item:
LINE 151 |             self.tree.uncheck_item(item)
LINE 152 | 
LINE 153 |     def _apply(self):
LINE 154 |         selected = self.tree.get_checked_files()
LINE 155 |         if self.on_apply_selection:
LINE 156 |             self.on_apply_selection(selected)
LINE 157 |         self.destroy()
```

==============================================================
FILE: app/gui/dialogs.py
==============================================================
```py
LINE  1 | """Dialog helpers and alert wrappers."""
LINE  2 | from tkinter import messagebox, filedialog
LINE  3 | from typing import Optional, List
LINE  4 | 
LINE  5 | 
LINE  6 | def show_info(title: str, message: str) -> None:
LINE  7 |     messagebox.showinfo(title, message)
LINE  8 | 
LINE  9 | 
LINE 10 | def show_warning(title: str, message: str) -> None:
LINE 11 |     messagebox.showwarning(title, message)
LINE 12 | 
LINE 13 | 
LINE 14 | def show_error(title: str, message: str) -> None:
LINE 15 |     messagebox.showerror(title, message)
LINE 16 | 
LINE 17 | 
LINE 18 | def ask_folder(title: str = "Seleccionar Carpeta") -> Optional[str]:
LINE 19 |     return filedialog.askdirectory(title=title)
LINE 20 | 
LINE 21 | 
LINE 22 | def ask_files(title: str = "Seleccionar Archivos") -> List[str]:
LINE 23 |     files = filedialog.askopenfilenames(title=title)
LINE 24 |     return list(files) if files else []
LINE 25 | 
LINE 26 | 
LINE 27 | def ask_save_file(title: str = "Guardar Archivo", default_ext: str = ".md") -> Optional[str]:
LINE 28 |     return filedialog.asksaveasfilename(
LINE 29 |         title=title,
LINE 30 |         defaultextension=default_ext,
LINE 31 |         filetypes=[("Markdown Document", "*.md"), ("Text Document", "*.txt"), ("Todos los Archivos", "*.*")]
LINE 32 |     )
```

==============================================================
FILE: app/gui/file_search_dialog.py
==============================================================
```py
LINE   1 | """File search dialog with per-file dependency analysis action and optimized performance."""
LINE   2 | import os
LINE   3 | import queue
LINE   4 | import threading
LINE   5 | import tkinter as tk
LINE   6 | from tkinter import ttk
LINE   7 | from typing import Callable, List, Optional, Set, Tuple
LINE   8 | 
LINE   9 | from app.core.project_scanner import scan_directory
LINE  10 | 
LINE  11 | C_BG = "#1e2330"
LINE  12 | C_PANEL = "#252b3b"
LINE  13 | C_BORDER = "#323a50"
LINE  14 | C_ACCENT = "#4f8ef7"
LINE  15 | C_TEXT = "#e8eaf0"
LINE  16 | C_TEXT2 = "#8b92a8"
LINE  17 | C_ENTRY = "#2a3148"
LINE  18 | 
LINE  19 | MAX_RENDER_LIMIT = 500
LINE  20 | BATCH_SIZE = 25              # 100 -> 25 : tandas más pequeñas, sin bloquear el mainloop
LINE  21 | DEBOUNCE_MS = 150
LINE  22 | LOADING_DELAY_MS = 200
LINE  23 | QUEUE_CHECK_MS = 20
LINE  24 | RENDER_BATCH_DELAY_MS = 15   # 1 -> 15 : cede el hilo entre tandas
LINE  25 | 
LINE  26 | 
LINE  27 | class FileSearchDialog(tk.Toplevel):
LINE  28 |     def __init__(
LINE  29 |         self,
LINE  30 |         parent: tk.Tk,
LINE  31 |         folder_path: str,
LINE  32 |         excluded_dirs: Optional[Set[str]] = None,
LINE  33 |         on_analyze_dependencies: Optional[Callable[[str], None]] = None,
LINE  34 |     ):
LINE  35 |         super().__init__(parent)
LINE  36 |         self.folder_path = folder_path
LINE  37 |         self.excluded_dirs = excluded_dirs or set()
LINE  38 |         self.on_analyze_dependencies = on_analyze_dependencies
LINE  39 | 
LINE  40 |         self.title("🔎 Buscador de archivos")
LINE  41 |         self.geometry("820x560")
LINE  42 |         self.minsize(640, 420)
LINE  43 |         self.configure(bg=C_BG)
LINE  44 | 
LINE  45 |         self.transient(parent)
LINE  46 |         self.grab_set()
LINE  47 | 
LINE  48 |         self.search_var = tk.StringVar()
LINE  49 |         self.all_files: List[str] = []
LINE  50 |         self._files_indexed: List[Tuple[str, str]] = []  # [(rel_path, rel_path_lower)]
LINE  51 | 
LINE  52 |         self._scan_id: int = 0
LINE  53 |         self._scan_queue: queue.Queue = queue.Queue()
LINE  54 | 
LINE  55 |         self._debounce_timer: Optional[str] = None
LINE  56 |         self._loading_timer: Optional[str] = None
LINE  57 |         self._render_timer: Optional[str] = None
LINE  58 |         self._poll_timer: Optional[str] = None
LINE  59 |         self._last_query: Optional[str] = None
LINE  60 | 
LINE  61 |         self.lbl_loading: Optional[tk.Label] = None
LINE  62 | 
LINE  63 |         self._build_header()
LINE  64 |         self._build_results()
LINE  65 | 
LINE  66 |         # Bind trace on search_var for debounced searching
LINE  67 |         self._trace_id = self.search_var.trace_add("write", self._on_query_trace)
LINE  68 | 
LINE  69 |         # Cleanup on destroy
LINE  70 |         self.bind("<Destroy>", self._on_destroy)
LINE  71 | 
LINE  72 |         self._load_files()
LINE  73 | 
LINE  74 |     def _build_header(self):
LINE  75 |         hdr = tk.Frame(self, bg=C_PANEL, padx=12, pady=10)
LINE  76 |         hdr.pack(fill=tk.X)
LINE  77 | 
LINE  78 |         header_top = tk.Frame(hdr, bg=C_PANEL)
LINE  79 |         header_top.pack(fill=tk.X)
LINE  80 | 
LINE  81 |         tk.Label(
LINE  82 |             header_top,
LINE  83 |             text="🔎 Buscar archivos del proyecto",
LINE  84 |             font=("Segoe UI", 12, "bold"),
LINE  85 |             bg=C_PANEL,
LINE  86 |             fg=C_TEXT,
LINE  87 |         ).pack(side=tk.LEFT, anchor="w")
LINE  88 | 
LINE  89 |         self.lbl_loading = tk.Label(
LINE  90 |             header_top,
LINE  91 |             text="⏳ Escaneando...",
LINE  92 |             font=("Segoe UI", 9, "italic"),
LINE  93 |             bg=C_PANEL,
LINE  94 |             fg=C_ACCENT,
LINE  95 |         )
LINE  96 | 
LINE  97 |         row = tk.Frame(hdr, bg=C_PANEL)
LINE  98 |         row.pack(fill=tk.X, pady=(6, 0))
LINE  99 | 
LINE 100 |         self.entry = ttk.Entry(row, textvariable=self.search_var, font=("Consolas", 9))
LINE 101 |         self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 6))
LINE 102 | 
LINE 103 |         ttk.Button(row, text="Buscar", command=self._force_refresh_results).pack(side=tk.LEFT)
LINE 104 |         ttk.Button(row, text="Limpiar", command=self._clear_search).pack(side=tk.LEFT, padx=(6, 0))
LINE 105 |         ttk.Button(
LINE 106 |             row,
LINE 107 |             text="↻ Refrescar",
LINE 108 |             command=lambda: self._load_files(force_refresh=True),
LINE 109 |         ).pack(side=tk.LEFT, padx=(6, 0))
LINE 110 | 
LINE 111 |     def _build_results(self):
LINE 112 |         container = tk.Frame(
LINE 113 |             self,
LINE 114 |             bg=C_ENTRY,
LINE 115 |             bd=1,
LINE 116 |             relief="flat",
LINE 117 |             highlightbackground=C_BORDER,
LINE 118 |             highlightthickness=1,
LINE 119 |         )
LINE 120 |         container.pack(fill=tk.BOTH, expand=True, padx=12, pady=8)
LINE 121 | 
LINE 122 |         self.canvas = tk.Canvas(container, bg=C_ENTRY, bd=0, highlightthickness=0)
LINE 123 |         scrollbar = ttk.Scrollbar(container, orient=tk.VERTICAL, command=self.canvas.yview)
LINE 124 |         self.scroll_frame = tk.Frame(self.canvas, bg=C_ENTRY)
LINE 125 | 
LINE 126 |         self.scroll_frame.bind(
LINE 127 |             "<Configure>",
LINE 128 |             lambda _e: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
LINE 129 |         )
LINE 130 |         self.canvas_window = self.canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")
LINE 131 | 
LINE 132 |         def _on_resize(event):
LINE 133 |             if self.winfo_exists():
LINE 134 |                 self.canvas.itemconfig(self.canvas_window, width=event.width)
LINE 135 | 
LINE 136 |         self.canvas.bind("<Configure>", _on_resize)
LINE 137 | 
LINE 138 |         # Scoped mousewheel binding directly to canvas and scroll_frame
LINE 139 |         def _on_mousewheel(event):
LINE 140 |             if not self.winfo_exists():
LINE 141 |                 return
LINE 142 |             if event.delta:
LINE 143 |                 self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
LINE 144 |             elif event.num == 4:
LINE 145 |                 self.canvas.yview_scroll(-1, "units")
LINE 146 |             elif event.num == 5:
LINE 147 |                 self.canvas.yview_scroll(1, "units")
LINE 148 | 
LINE 149 |         self.canvas.bind("<MouseWheel>", _on_mousewheel)
LINE 150 |         self.canvas.bind("<Button-4>", _on_mousewheel)
LINE 151 |         self.canvas.bind("<Button-5>", _on_mousewheel)
LINE 152 |         self.scroll_frame.bind("<MouseWheel>", _on_mousewheel)
LINE 153 |         self.scroll_frame.bind("<Button-4>", _on_mousewheel)
LINE 154 |         self.scroll_frame.bind("<Button-5>", _on_mousewheel)
LINE 155 | 
LINE 156 |         self.canvas.configure(yscrollcommand=scrollbar.set)
LINE 157 |         scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
LINE 158 |         self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
LINE 159 | 
LINE 160 |     def _load_files(self, force_refresh: bool = False):
LINE 161 |         self._scan_id += 1
LINE 162 |         current_scan_id = self._scan_id
LINE 163 | 
LINE 164 |         # Schedule delayed loading indicator after 200ms
LINE 165 |         self._cancel_timer("_loading_timer")
LINE 166 |         self._loading_timer = self.after(
LINE 167 |             LOADING_DELAY_MS, lambda: self._show_loading(current_scan_id)
LINE 168 |         )
LINE 169 | 
LINE 170 |         # FIX: launch background worker: DB-first, os.walk fallback
LINE 171 |         threading.Thread(
LINE 172 |             target=self._async_scan_worker,
LINE 173 |             args=(
LINE 174 |                 current_scan_id,
LINE 175 |                 self.folder_path,
LINE 176 |                 self.excluded_dirs,
LINE 177 |                 self._scan_queue,
LINE 178 |                 force_refresh,
LINE 179 |             ),
LINE 180 |             daemon=True,
LINE 181 |         ).start()
LINE 182 | 
LINE 183 |         # Start queue polling loop on main GUI thread
LINE 184 |         self._schedule_queue_check()
LINE 185 | 
LINE 186 |     def _schedule_queue_check(self):
LINE 187 |         self._cancel_timer("_poll_timer")
LINE 188 |         if self.winfo_exists():
LINE 189 |             self._poll_timer = self.after(QUEUE_CHECK_MS, self._check_scan_queue)
LINE 190 | 
LINE 191 |     def _check_scan_queue(self):
LINE 192 |         if not self.winfo_exists():
LINE 193 |             return
LINE 194 | 
LINE 195 |         received = False
LINE 196 |         latest_files = None
LINE 197 |         source = None
LINE 198 | 
LINE 199 |         while True:
LINE 200 |             try:
LINE 201 |                 sid, files, src = self._scan_queue.get_nowait()
LINE 202 |                 if sid == self._scan_id:
LINE 203 |                     latest_files = files
LINE 204 |                     source = src
LINE 205 |                     received = True
LINE 206 |             except queue.Empty:
LINE 207 |                 break
LINE 208 | 
LINE 209 |         if received and latest_files is not None:
LINE 210 |             self._hide_loading()
LINE 211 |             self.all_files = latest_files
LINE 212 |             self._files_indexed = [(f, f.lower()) for f in latest_files]
LINE 213 |             if self.lbl_loading is not None and self.winfo_exists():
LINE 214 |                 tag = "caché DB" if source == "db" else "escaneo"
LINE 215 |                 self.lbl_loading.config(
LINE 216 |                     text=f"✓ {len(latest_files)} archivos ({tag})"
LINE 217 |                 )
LINE 218 |             self._refresh_results(force=True)
LINE 219 |         else:
LINE 220 |             # Reschedule queue check
LINE 221 |             self._schedule_queue_check()
LINE 222 | 
LINE 223 |     @staticmethod
LINE 224 |     def _async_scan_worker(
LINE 225 |         scan_id: int,
LINE 226 |         folder_path: str,
LINE 227 |         excluded_dirs: Set[str],
LINE 228 |         res_queue: queue.Queue,
LINE 229 |         force_refresh: bool = False,
LINE 230 |     ):
LINE 231 |         """Worker thread entry point: DB-first con fallback a os.walk.
LINE 232 | 
LINE 233 |         Estrategia:
LINE 234 |           1) Si !force_refresh, consultar SQLite (project_cache.db). ~1 ms.
LINE 235 |           2) Si la DB no tiene filas o el usuario forzó refresco, os.walk.
LINE 236 |         """
LINE 237 |         files: List[str] = []
LINE 238 |         source = "scan"
LINE 239 |         try:
LINE 240 |             from app.core.storage.database import get_database
LINE 241 | 
LINE 242 |             if not force_refresh:
LINE 243 |                 db = get_database()
LINE 244 |                 db_files, _last_scanned, exists = db.load_file_paths(folder_path)
LINE 245 |                 if exists and db_files:
LINE 246 |                     files = db_files
LINE 247 |                     source = "db"
LINE 248 | 
LINE 249 |             if not files:
LINE 250 |                 files = scan_directory(
LINE 251 |                     folder_path, excluded_dirs, allowed_extensions=None
LINE 252 |                 )
LINE 253 |                 source = "scan"
LINE 254 |         except Exception:
LINE 255 |             # Ante cualquier fallo, caer a escaneo directo
LINE 256 |             try:
LINE 257 |                 files = scan_directory(
LINE 258 |                     folder_path, excluded_dirs, allowed_extensions=None
LINE 259 |                 )
LINE 260 |             except Exception:
LINE 261 |                 files = []
LINE 262 |             source = "scan"
LINE 263 | 
LINE 264 |         res_queue.put((scan_id, files, source))
LINE 265 | 
LINE 266 |     def _show_loading(self, scan_id: int):
LINE 267 |         if not self.winfo_exists():
LINE 268 |             return
LINE 269 |         if scan_id == self._scan_id and self.lbl_loading:
LINE 270 |             self.lbl_loading.pack(side=tk.RIGHT)
LINE 271 | 
LINE 272 |     def _hide_loading(self):
LINE 273 |         self._cancel_timer("_loading_timer")
LINE 274 |         if self.winfo_exists() and self.lbl_loading:
LINE 275 |             self.lbl_loading.pack_forget()
LINE 276 | 
LINE 277 |     def _on_query_trace(self, *args):
LINE 278 |         self._cancel_timer("_debounce_timer")
LINE 279 |         self._debounce_timer = self.after(DEBOUNCE_MS, self._refresh_results)
LINE 280 | 
LINE 281 |     def _force_refresh_results(self):
LINE 282 |         self._cancel_timer("_debounce_timer")
LINE 283 |         self._refresh_results(force=True)
LINE 284 | 
LINE 285 |     def _clear_search(self):
LINE 286 |         self.search_var.set("")
LINE 287 |         self._force_refresh_results()
LINE 288 | 
LINE 289 |     def _cancel_timer(self, attr_name: str):
LINE 290 |         timer_id = getattr(self, attr_name, None)
LINE 291 |         if timer_id:
LINE 292 |             try:
LINE 293 |                 self.after_cancel(timer_id)
LINE 294 |             except Exception:
LINE 295 |                 pass
LINE 296 |             setattr(self, attr_name, None)
LINE 297 | 
LINE 298 |     def _cancel_render_task(self):
LINE 299 |         self._cancel_timer("_render_timer")
LINE 300 | 
LINE 301 |     def _refresh_results(self, force: bool = False):
LINE 302 |         if not self.winfo_exists():
LINE 303 |             return
LINE 304 | 
LINE 305 |         query = self.search_var.get().strip().lower()
LINE 306 |         if not force and self._last_query == query:
LINE 307 |             return
LINE 308 |         self._last_query = query
LINE 309 | 
LINE 310 |         self._cancel_render_task()
LINE 311 | 
LINE 312 |         # Clear existing scroll_frame children
LINE 313 |         for child in self.scroll_frame.winfo_children():
LINE 314 |             child.destroy()
LINE 315 | 
LINE 316 |         matches = [
LINE 317 |             rel for rel, rel_lower in self._files_indexed
LINE 318 |             if not query or query in rel_lower
LINE 319 |         ]
LINE 320 | 
LINE 321 |         if not matches:
LINE 322 |             tk.Label(
LINE 323 |                 self.scroll_frame,
LINE 324 |                 text="(Sin resultados)",
LINE 325 |                 font=("Segoe UI", 9, "italic"),
LINE 326 |                 bg=C_ENTRY,
LINE 327 |                 fg=C_TEXT2,
LINE 328 |             ).pack(anchor="w", padx=10, pady=10)
LINE 329 |             return
LINE 330 | 
LINE 331 |         total_matches = len(matches)
LINE 332 |         matches_to_render = matches[:MAX_RENDER_LIMIT]
LINE 333 | 
LINE 334 |         # FIX: incluso la primera tanda se agenda con after(0, ...) para no
LINE 335 |         # bloquear el hilo de la GUI dentro de _refresh_results.
LINE 336 |         self._render_timer = self.after(
LINE 337 |             0,
LINE 338 |             lambda: self._render_batch(matches_to_render, 0, total_matches),
LINE 339 |         )
LINE 340 | 
LINE 341 |     def _render_batch(self, matches_subset: List[str], start_idx: int, total_matches: int):
LINE 342 |         if not self.winfo_exists():
LINE 343 |             return
LINE 344 | 
LINE 345 |         end_idx = min(start_idx + BATCH_SIZE, len(matches_subset))
LINE 346 | 
LINE 347 |         for idx in range(start_idx, end_idx):
LINE 348 |             rel = matches_subset[idx]
LINE 349 |             row = tk.Frame(self.scroll_frame, bg=C_ENTRY, padx=8, pady=3)
LINE 350 |             row.pack(fill=tk.X)
LINE 351 | 
LINE 352 |             tk.Label(
LINE 353 |                 row,
LINE 354 |                 text=rel,
LINE 355 |                 font=("Consolas", 9),
LINE 356 |                 bg=C_ENTRY,
LINE 357 |                 fg=C_TEXT,
LINE 358 |                 anchor="w",
LINE 359 |             ).pack(side=tk.LEFT, fill=tk.X, expand=True)
LINE 360 | 
LINE 361 |             ttk.Button(
LINE 362 |                 row,
LINE 363 |                 text="🔗 Dependencias",
LINE 364 |                 command=lambda r=rel: self._analyze(r),
LINE 365 |             ).pack(side=tk.RIGHT)
LINE 366 | 
LINE 367 |         if end_idx < len(matches_subset):
LINE 368 |             # FIX: 15 ms en lugar de 1 ms para que el mainloop procese eventos
LINE 369 |             # (redibujado, teclado, ratón) entre tandas.
LINE 370 |             self._render_timer = self.after(
LINE 371 |                 RENDER_BATCH_DELAY_MS,
LINE 372 |                 lambda: self._render_batch(matches_subset, end_idx, total_matches),
LINE 373 |             )
LINE 374 |         else:
LINE 375 |             # Batch complete, display total matches summary if hard limit hit
LINE 376 |             if total_matches > MAX_RENDER_LIMIT:
LINE 377 |                 footer = tk.Frame(self.scroll_frame, bg=C_ENTRY, padx=8, pady=6)
LINE 378 |                 footer.pack(fill=tk.X)
LINE 379 |                 tk.Label(
LINE 380 |                     footer,
LINE 381 |                     text=f"Mostrando {MAX_RENDER_LIMIT} de {total_matches:,} resultados. Afina la búsqueda para ver más.",
LINE 382 |                     font=("Segoe UI", 8, "italic"),
LINE 383 |                     bg=C_ENTRY,
LINE 384 |                     fg=C_TEXT2,
LINE 385 |                 ).pack(anchor="w")
LINE 386 | 
LINE 387 |     def _analyze(self, rel_path: str):
LINE 388 |         if self.on_analyze_dependencies:
LINE 389 |             self.on_analyze_dependencies(rel_path)
LINE 390 | 
LINE 391 |     def _on_destroy(self, event):
LINE 392 |         if event.widget == self:
LINE 393 |             self._cancel_timer("_debounce_timer")
LINE 394 |             self._cancel_timer("_loading_timer")
LINE 395 |             self._cancel_timer("_render_timer")
LINE 396 |             self._cancel_timer("_poll_timer")
LINE 397 |             self._scan_id += 1  # invalidate any pending scan callbacks
LINE 398 |             try:
LINE 399 |                 self.search_var.trace_remove("write", self._trace_id)
LINE 400 |             except Exception:
LINE 401 |                 pass
```

==============================================================
FILE: app/gui/file_tree.py
==============================================================
```py
LINE   1 | """CheckboxTreeview component for selecting folder files."""
LINE   2 | import tkinter as tk
LINE   3 | from tkinter import ttk
LINE   4 | from typing import Set, List
LINE   5 | 
LINE   6 | 
LINE   7 | class CheckboxTreeview(ttk.Treeview):
LINE   8 |     def __init__(self, master, **kwargs):
LINE   9 |         super().__init__(master, columns=("check", "name"), show="tree headings", **kwargs)
LINE  10 |         self.heading("#0", text="", anchor="w")
LINE  11 |         self.heading("check", text="☑", anchor="center", command=self.toggle_all_header)
LINE  12 |         self.heading("name", text="Archivo / Carpeta", anchor="w")
LINE  13 |         self.column("#0", width=35, stretch=False)
LINE  14 |         self.column("check", width=40, stretch=False, anchor="center")
LINE  15 |         self.column("name", width=260, stretch=True)
LINE  16 |         
LINE  17 |         self.tag_configure("checked", foreground="#1b5e20")
LINE  18 |         self.tag_configure("unchecked", foreground="#757575")
LINE  19 |         self.bind("<Button-1>", self.on_click)
LINE  20 |         self.checked_items: Set[str] = set()
LINE  21 |         # === PERSISTENCE: PHASE1 (attrs) ===
LINE  22 |         self._on_check_change = None
LINE  23 |         # === END PERSISTENCE: PHASE1 (attrs) ===
LINE  24 | 
LINE  25 | 
LINE  26 |     # === PERSISTENCE: PHASE1 (methods) ===
LINE  27 |     def set_check_change_callback(self, callback) -> None:
LINE  28 |         """Register callback(rel_path: str, is_checked: bool) for persistence."""
LINE  29 |         self._on_check_change = callback
LINE  30 | 
LINE  31 |     def _notify_check_change(self, rel_path: str, is_checked: bool) -> None:
LINE  32 |         if not self._on_check_change or not rel_path:
LINE  33 |             return
LINE  34 |         try:
LINE  35 |             self._on_check_change(rel_path, is_checked)
LINE  36 |         except Exception:
LINE  37 |             pass
LINE  38 |     # === END PERSISTENCE: PHASE1 (methods) ===
LINE  39 | 
LINE  40 |     def insert_file(self, parent, rel_path: str, is_checked: bool = True):
LINE  41 |         item = self.insert(parent, "end", text="📄", values=("☑" if is_checked else "☐", rel_path), tags=("checked" if is_checked else "unchecked",))
LINE  42 |         if is_checked:
LINE  43 |             self.checked_items.add(rel_path)
LINE  44 |         return item
LINE  45 | 
LINE  46 |     def insert_folder(self, parent, rel_path: str):
LINE  47 |         return self.insert(parent, "end", text="📁", values=("", rel_path), open=True)
LINE  48 | 
LINE  49 |     def check_item(self, item):
LINE  50 |         rel_path = self.set(item, "name")
LINE  51 |         if rel_path:
LINE  52 |             was_checked = rel_path in self.checked_items
LINE  53 |             self.set(item, "check", "☑")
LINE  54 |             self.item(item, tags=("checked",))
LINE  55 |             if not self.get_children(item):
LINE  56 |                 self.checked_items.add(rel_path)
LINE  57 |                 if not was_checked:
LINE  58 |                     self._notify_check_change(rel_path, True)
LINE  59 |         for child in self.get_children(item):
LINE  60 |             self.check_item(child)
LINE  61 | 
LINE  62 |     def uncheck_item(self, item):
LINE  63 |         rel_path = self.set(item, "name")
LINE  64 |         if rel_path:
LINE  65 |             was_checked = rel_path in self.checked_items
LINE  66 |             self.set(item, "check", "☐")
LINE  67 |             self.item(item, tags=("unchecked",))
LINE  68 |             if rel_path in self.checked_items:
LINE  69 |                 self.checked_items.remove(rel_path)
LINE  70 |             if was_checked:
LINE  71 |                 self._notify_check_change(rel_path, False)
LINE  72 |         for child in self.get_children(item):
LINE  73 |             self.uncheck_item(child)
LINE  74 | 
LINE  75 |     def toggle_item(self, item):
LINE  76 |         check_val = self.set(item, "check")
LINE  77 |         if check_val == "☑":
LINE  78 |             self.uncheck_item(item)
LINE  79 |         else:
LINE  80 |             self.check_item(item)
LINE  81 | 
LINE  82 |     def toggle_all_header(self):
LINE  83 |         all_children = self.get_children()
LINE  84 |         if not all_children:
LINE  85 |             return
LINE  86 |         all_checked = all(self.set(child, "check") == "☑" for child in all_children if self.set(child, "check") != "")
LINE  87 |         for child in all_children:
LINE  88 |             if all_checked:
LINE  89 |                 self.uncheck_item(child)
LINE  90 |             else:
LINE  91 |                 self.check_item(child)
LINE  92 | 
LINE  93 |     def on_click(self, event):
LINE  94 |         region = self.identify_region(event.x, event.y)
LINE  95 |         item = self.identify_row(event.y)
LINE  96 |         if not item:
LINE  97 |             return
LINE  98 |         column = self.identify_column(event.x)
LINE  99 |         if region == "cell" and column == "#2":
LINE 100 |             self.toggle_item(item)
LINE 101 |         elif region == "tree":
LINE 102 |             self.toggle_item(item)
LINE 103 | 
LINE 104 |     def select_all(self):
LINE 105 |         for item in self.get_children():
LINE 106 |             self.check_item(item)
LINE 107 | 
LINE 108 |     def deselect_all(self):
LINE 109 |         for item in self.get_children():
LINE 110 |             self.uncheck_item(item)
LINE 111 | 
LINE 112 |     def get_checked_files(self) -> List[str]:
LINE 113 |         return list(self.checked_items)
LINE 114 | 
LINE 115 |     def set_checked_files(self, target_rel_paths: Set[str]):
LINE 116 |         """Sets checked items to exactly match target_rel_paths."""
LINE 117 |         self.checked_items.clear()
LINE 118 |         normalized_targets = {p.replace("\\", "/") for p in target_rel_paths}
LINE 119 | 
LINE 120 |         def traverse(item):
LINE 121 |             children = self.get_children(item)
LINE 122 |             if children:
LINE 123 |                 any_child_checked = False
LINE 124 |                 all_children_checked = True
LINE 125 |                 for child in children:
LINE 126 |                     child_checked = traverse(child)
LINE 127 |                     if child_checked:
LINE 128 |                         any_child_checked = True
LINE 129 |                     else:
LINE 130 |                         all_children_checked = False
LINE 131 |                 if any_child_checked:
LINE 132 |                     self.set(item, "check", "☑")
LINE 133 |                     self.item(item, tags=("checked",))
LINE 134 |                 else:
LINE 135 |                     self.set(item, "check", "☐")
LINE 136 |                     self.item(item, tags=("unchecked",))
LINE 137 |                 return any_child_checked
LINE 138 |             else:
LINE 139 |                 rel_path = self.set(item, "name")
LINE 140 |                 norm_rel = rel_path.replace("\\", "/") if rel_path else ""
LINE 141 |                 if norm_rel and norm_rel in normalized_targets:
LINE 142 |                     self.set(item, "check", "☑")
LINE 143 |                     self.item(item, tags=("checked",))
LINE 144 |                     self.checked_items.add(rel_path)
LINE 145 |                     return True
LINE 146 |                 else:
LINE 147 |                     self.set(item, "check", "☐")
LINE 148 |                     self.item(item, tags=("unchecked",))
LINE 149 |                     return False
LINE 150 | 
LINE 151 |         for root_item in self.get_children():
LINE 152 |             traverse(root_item)
```

==============================================================
FILE: app/gui/intelligent_context_dialog.py
==============================================================
```py
LINE   1 | """
LINE   2 | Intelligent Context Dialog GUI Component.
LINE   3 | Presents prioritized files (🔴 Critical, 🟠 Important, 🟡 Related, ⚪ Secondary),
LINE   4 | allows user review, filtering, and manual modification before context generation.
LINE   5 | """
LINE   6 | import os
LINE   7 | import tkinter as tk
LINE   8 | from tkinter import ttk
LINE   9 | from typing import List, Callable, Optional, Dict
LINE  10 | 
LINE  11 | from app.core.intelligent_context import (
LINE  12 |     PrioritizedFile,
LINE  13 |     PRIORITY_CRITICAL,
LINE  14 |     PRIORITY_IMPORTANT,
LINE  15 |     PRIORITY_RELATED,
LINE  16 |     PRIORITY_SECONDARY
LINE  17 | )
LINE  18 | from app.utils.file_utils import format_bytes
LINE  19 | 
LINE  20 | # Colour palette (aligned with main_window.py & analysis_dialog.py)
LINE  21 | C_BG        = "#1e2330"
LINE  22 | C_PANEL     = "#252b3b"
LINE  23 | C_BORDER    = "#323a50"
LINE  24 | C_ACCENT    = "#4f8ef7"
LINE  25 | C_ACCENT_DK = "#3a6fcc"
LINE  26 | C_SUCCESS   = "#3ecf8e"
LINE  27 | C_WARN      = "#f5a623"
LINE  28 | C_TEXT      = "#e8eaf0"
LINE  29 | C_TEXT2     = "#8b92a8"
LINE  30 | C_ENTRY     = "#2a3148"
LINE  31 | C_TREE_SEL  = "#2f3d5c"
LINE  32 | 
LINE  33 | 
LINE  34 | class IntelligentContextDialog(tk.Toplevel):
LINE  35 |     """Modal dialog allowing user to review and adjust intelligent context file selection."""
LINE  36 | 
LINE  37 |     def __init__(
LINE  38 |         self,
LINE  39 |         parent: tk.Tk,
LINE  40 |         problem_desc: str,
LINE  41 |         prioritized_files: List[PrioritizedFile],
LINE  42 |         on_confirm: Callable[[List[str]], None]
LINE  43 |     ):
LINE  44 |         super().__init__(parent)
LINE  45 |         self.problem_desc = problem_desc
LINE  46 |         self.prioritized_files = prioritized_files
LINE  47 |         self.on_confirm = on_confirm
LINE  48 |         self.file_vars: Dict[str, tk.BooleanVar] = {}
LINE  49 | 
LINE  50 |         self.title("🧠 Selección Inteligente de Contexto")
LINE  51 |         self.geometry("960x700")
LINE  52 |         self.minsize(800, 520)
LINE  53 |         self.configure(bg=C_BG)
LINE  54 | 
LINE  55 |         # Make dialog modal and centered
LINE  56 |         self.transient(parent)
LINE  57 |         self.grab_set()
LINE  58 |         self._center_window(parent)
LINE  59 | 
LINE  60 |         self._build_header()
LINE  61 |         self._build_summary_bar()
LINE  62 |         self._build_file_list()
LINE  63 |         self._build_bottom_bar()
LINE  64 | 
LINE  65 |     def _center_window(self, parent: tk.Tk):
LINE  66 |         self.update_idletasks()
LINE  67 |         try:
LINE  68 |             pw = parent.winfo_width()
LINE  69 |             ph = parent.winfo_height()
LINE  70 |             px = parent.winfo_rootx()
LINE  71 |             py = parent.winfo_rooty()
LINE  72 |             w = self.winfo_width()
LINE  73 |             h = self.winfo_height()
LINE  74 |             x = px + max(0, (pw - w) // 2)
LINE  75 |             y = py + max(0, (ph - h) // 2)
LINE  76 |             self.geometry(f"{w}x{h}+{x}+{y}")
LINE  77 |         except Exception:
LINE  78 |             pass
LINE  79 | 
LINE  80 |     def _build_header(self):
LINE  81 |         hdr = tk.Frame(self, bg=C_PANEL, padx=16, pady=12, highlightthickness=1, highlightbackground=C_BORDER)
LINE  82 |         hdr.pack(fill=tk.X)
LINE  83 | 
LINE  84 |         tk.Label(
LINE  85 |             hdr,
LINE  86 |             text="🧠  Selección Inteligente de Archivos de Contexto",
LINE  87 |             font=("Segoe UI", 12, "bold"),
LINE  88 |             bg=C_PANEL, fg=C_TEXT
LINE  89 |         ).pack(anchor="w")
LINE  90 | 
LINE  91 |         short_desc = (self.problem_desc[:120] + "...") if len(self.problem_desc) > 120 else (self.problem_desc or "Sin descripción especificada")
LINE  92 |         tk.Label(
LINE  93 |             hdr,
LINE  94 |             text=f"Problema reportado: \"{short_desc}\"",
LINE  95 |             font=("Segoe UI", 9, "italic"),
LINE  96 |             bg=C_PANEL, fg=C_ACCENT
LINE  97 |         ).pack(anchor="w", pady=(2, 0))
LINE  98 | 
LINE  99 |     def _build_summary_bar(self):
LINE 100 |         bar = tk.Frame(self, bg=C_BG, padx=16, pady=8)
LINE 101 |         bar.pack(fill=tk.X)
LINE 102 | 
LINE 103 |         counts = {
LINE 104 |             PRIORITY_CRITICAL: 0,
LINE 105 |             PRIORITY_IMPORTANT: 0,
LINE 106 |             PRIORITY_RELATED: 0,
LINE 107 |             PRIORITY_SECONDARY: 0
LINE 108 |         }
LINE 109 |         for pf in self.prioritized_files:
LINE 110 |             counts[pf.priority_level] = counts.get(pf.priority_level, 0) + 1
LINE 111 | 
LINE 112 |         badges_frame = tk.Frame(bar, bg=C_BG)
LINE 113 |         badges_frame.pack(side=tk.LEFT)
LINE 114 | 
LINE 115 |         def _add_badge(parent, text, bg_color):
LINE 116 |             f = tk.Frame(parent, bg=bg_color, padx=8, pady=3)
LINE 117 |             f.pack(side=tk.LEFT, padx=3)
LINE 118 |             tk.Label(f, text=text, font=("Segoe UI", 8, "bold"), bg=bg_color, fg="#ffffff").pack()
LINE 119 | 
LINE 120 |         _add_badge(badges_frame, f"🔴 Críticos ({counts[PRIORITY_CRITICAL]})", "#e74c3c")
LINE 121 |         _add_badge(badges_frame, f"🟠 Importantes ({counts[PRIORITY_IMPORTANT]})", "#e67e22")
LINE 122 |         _add_badge(badges_frame, f"🟡 Relacionados ({counts[PRIORITY_RELATED]})", "#f1c40f")
LINE 123 |         _add_badge(badges_frame, f"⚪ Secundarios ({counts[PRIORITY_SECONDARY]})", "#7f8c8d")
LINE 124 | 
LINE 125 |         self.lbl_stats = tk.Label(
LINE 126 |             bar,
LINE 127 |             text="",
LINE 128 |             font=("Segoe UI", 9, "bold"),
LINE 129 |             bg=C_BG, fg=C_TEXT
LINE 130 |         )
LINE 131 |         self.lbl_stats.pack(side=tk.RIGHT)
LINE 132 | 
LINE 133 |     def _build_file_list(self):
LINE 134 |         main_frame = tk.Frame(self, bg=C_PANEL, padx=12, pady=10, highlightthickness=1, highlightbackground=C_BORDER)
LINE 135 |         main_frame.pack(fill=tk.BOTH, expand=True, padx=16, pady=4)
LINE 136 | 
LINE 137 |         # Toolbar presets
LINE 138 |         tb = tk.Frame(main_frame, bg=C_PANEL)
LINE 139 |         tb.pack(fill=tk.X, pady=(0, 6))
LINE 140 | 
LINE 141 |         ttk.Button(tb, text="☑ Marcar todos", style="Neutral.TButton", command=self._select_all).pack(side=tk.LEFT, padx=(0, 4))
LINE 142 |         ttk.Button(tb, text="☐ Desmarcar todos", style="Neutral.TButton", command=self._deselect_all).pack(side=tk.LEFT, padx=(0, 4))
LINE 143 |         ttk.Button(tb, text="🔴 Solo Críticos e Importantes", style="Neutral.TButton", command=self._select_critical_important).pack(side=tk.LEFT)
LINE 144 | 
LINE 145 |         # Scrollable area
LINE 146 |         list_container = tk.Frame(main_frame, bg=C_ENTRY, bd=1, relief="flat", highlightbackground=C_BORDER, highlightthickness=1)
LINE 147 |         list_container.pack(fill=tk.BOTH, expand=True)
LINE 148 | 
LINE 149 |         canvas = tk.Canvas(list_container, bg=C_ENTRY, bd=0, highlightthickness=0)
LINE 150 |         scrollbar = ttk.Scrollbar(list_container, orient=tk.VERTICAL, command=canvas.yview)
LINE 151 |         scroll_frame = tk.Frame(canvas, bg=C_ENTRY)
LINE 152 | 
LINE 153 |         scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
LINE 154 |         canvas_window = canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
LINE 155 | 
LINE 156 |         def _on_resize(event):
LINE 157 |             canvas.itemconfig(canvas_window, width=event.width)
LINE 158 |         canvas.bind("<Configure>", _on_resize)
LINE 159 | 
LINE 160 |         # Mousewheel
LINE 161 |         def _on_mw(event):
LINE 162 |             if event.delta:
LINE 163 |                 canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
LINE 164 |             elif event.num == 4:
LINE 165 |                 canvas.yview_scroll(-1, "units")
LINE 166 |             elif event.num == 5:
LINE 167 |                 canvas.yview_scroll(1, "units")
LINE 168 | 
LINE 169 |         canvas.bind_all("<MouseWheel>", _on_mw)
LINE 170 |         canvas.bind_all("<Button-4>", _on_mw)
LINE 171 |         canvas.bind_all("<Button-5>", _on_mw)
LINE 172 | 
LINE 173 |         canvas.configure(yscrollcommand=scrollbar.set)
LINE 174 |         scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
LINE 175 |         canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
LINE 176 | 
LINE 177 |         # Populate rows
LINE 178 |         for pf in self.prioritized_files:
LINE 179 |             var = tk.BooleanVar(value=pf.is_selected)
LINE 180 |             self.file_vars[pf.rel_path] = var
LINE 181 | 
LINE 182 |             row = tk.Frame(scroll_frame, bg=C_ENTRY, padx=8, pady=4, bd=0)
LINE 183 |             row.pack(fill=tk.X, pady=1)
LINE 184 | 
LINE 185 |             # Icon / badge label
LINE 186 |             lbl_badge = tk.Label(
LINE 187 |                 row,
LINE 188 |                 text=f"{pf.priority_icon} {pf.priority_label}",
LINE 189 |                 font=("Segoe UI", 8, "bold"),
LINE 190 |                 bg=C_ENTRY, fg=C_TEXT, width=14, anchor="w"
LINE 191 |             )
LINE 192 |             lbl_badge.pack(side=tk.LEFT)
LINE 193 | 
LINE 194 |             # Checkbox + rel_path
LINE 195 |             cb = tk.Checkbutton(
LINE 196 |                 row,
LINE 197 |                 text=pf.rel_path,
LINE 198 |                 variable=var,
LINE 199 |                 font=("Consolas", 9, "bold" if pf.priority_level <= 2 else "normal"),
LINE 200 |                 bg=C_ENTRY,
LINE 201 |                 fg=C_TEXT if pf.priority_level <= 2 else C_TEXT2,
LINE 202 |                 activebackground=C_ENTRY,
LINE 203 |                 activeforeground=C_ACCENT,
LINE 204 |                 selectcolor=C_PANEL,
LINE 205 |                 anchor="w",
LINE 206 |                 command=self._update_stats
LINE 207 |             )
LINE 208 |             cb.pack(side=tk.LEFT, fill=tk.X, expand=True)
LINE 209 | 
LINE 210 |             # Size badge
LINE 211 |             tk.Label(
LINE 212 |                 row,
LINE 213 |                 text=format_bytes(pf.size_bytes),
LINE 214 |                 font=("Consolas", 8),
LINE 215 |                 bg=C_ENTRY, fg=C_TEXT2, width=10, anchor="e"
LINE 216 |             ).pack(side=tk.LEFT, padx=(4, 8))
LINE 217 | 
LINE 218 |             # Rationale tooltip/hint
LINE 219 |             tk.Label(
LINE 220 |                 row,
LINE 221 |                 text=pf.reason,
LINE 222 |                 font=("Segoe UI", 8, "italic"),
LINE 223 |                 bg=C_ENTRY, fg=C_TEXT2, anchor="w"
LINE 224 |             ).pack(side=tk.LEFT, padx=4)
LINE 225 | 
LINE 226 |         self._update_stats()
LINE 227 | 
LINE 228 |     def _build_bottom_bar(self):
LINE 229 |         btn_bar = tk.Frame(self, bg=C_PANEL, padx=16, pady=12, highlightthickness=1, highlightbackground=C_BORDER)
LINE 230 |         btn_bar.pack(fill=tk.X, side=tk.BOTTOM)
LINE 231 | 
LINE 232 |         ttk.Button(
LINE 233 |             btn_bar,
LINE 234 |             text="Cancelar",
LINE 235 |             style="Neutral.TButton",
LINE 236 |             command=self.destroy
LINE 237 |         ).pack(side=tk.RIGHT, padx=(8, 0))
LINE 238 | 
LINE 239 |         ttk.Button(
LINE 240 |             btn_bar,
LINE 241 |             text="⚡ Aplicar Selección e Incluir en Contexto",
LINE 242 |             style="Accent.TButton",
LINE 243 |             command=self._on_confirm
LINE 244 |         ).pack(side=tk.RIGHT)
LINE 245 | 
LINE 246 |     def _select_all(self):
LINE 247 |         for var in self.file_vars.values():
LINE 248 |             var.set(True)
LINE 249 |         self._update_stats()
LINE 250 | 
LINE 251 |     def _deselect_all(self):
LINE 252 |         for var in self.file_vars.values():
LINE 253 |             var.set(False)
LINE 254 |         self._update_stats()
LINE 255 | 
LINE 256 |     def _select_critical_important(self):
LINE 257 |         for pf in self.prioritized_files:
LINE 258 |             var = self.file_vars.get(pf.rel_path)
LINE 259 |             if var:
LINE 260 |                 var.set(pf.priority_level <= PRIORITY_IMPORTANT)
LINE 261 |         self._update_stats()
LINE 262 | 
LINE 263 |     def _update_stats(self):
LINE 264 |         selected_files = [pf for pf in self.prioritized_files if self.file_vars[pf.rel_path].get()]
LINE 265 |         total_sz = sum(pf.size_bytes for pf in selected_files)
LINE 266 |         cnt = len(selected_files)
LINE 267 |         tot = len(self.prioritized_files)
LINE 268 |         self.lbl_stats.config(text=f"Seleccionados: {cnt} de {tot} archivos ({format_bytes(total_sz)})")
LINE 269 | 
LINE 270 |     def _on_confirm(self):
LINE 271 |         selected_rel_paths = [pf.rel_path for pf in self.prioritized_files if self.file_vars[pf.rel_path].get()]
LINE 272 |         self.on_confirm(selected_rel_paths)
LINE 273 |         self.destroy()
```

==============================================================
FILE: app/gui/main_window.py
==============================================================
```py
LINE    1 | """Main Tkinter window – redesigned layout with left tree, right problem pane, and full bottom stats bar."""
LINE    2 | import os
LINE    3 | import sys
LINE    4 | import subprocess
LINE    5 | import tkinter as tk
LINE    6 | from tkinter import ttk, scrolledtext
LINE    7 | from typing import List, Set
LINE    8 | 
LINE    9 | from app.models.project import ExportConfig, DEFAULT_ALLOWED_EXTENSIONS
LINE   10 | from app.models.analysis_types import (
LINE   11 |     ANALYSIS_PROFILES, get_analysis_profile, get_all_analysis_types
LINE   12 | )
LINE   13 | from app.models.analysis_modes import (
LINE   14 |     ANALYSIS_MODES, get_analysis_mode_config, MODE_PROBLEM, MODE_PROJECT
LINE   15 | )
LINE   16 | from app.core.file_selector import FileSelectorManager
LINE   17 | from app.generators.prompt_generator import PromptGenerator
LINE   18 | from app.generators.markdown_generator import generate_markdown_bundle
LINE   19 | from app.generators.text_generator import generate_text_bundle
LINE   20 | from app.generators.standalone_prompt_generator import generate_standalone_prompt
LINE   21 | from app.gui.file_tree import CheckboxTreeview
LINE   22 | from app.gui.analysis_dialog import ProjectAnalysisDialog
LINE   23 | from app.core.project_analyzer import ProjectAnalyzer
LINE   24 | from app.core.intelligent_context import IntelligentContextAnalyzer
LINE   25 | from app.gui.intelligent_context_dialog import IntelligentContextDialog
LINE   26 | from app.gui import dialogs
LINE   27 | # === AUTO-GENERATED: file_search_dependency_feature ===
LINE   28 | from app.gui.file_search_dialog import FileSearchDialog
LINE   29 | from app.gui.dependency_tree_dialog import DependencyTreeDialog
LINE   30 | # === END AUTO-GENERATED ===
LINE   31 | # === PERSISTENCE: PHASE1 (imports) ===
LINE   32 | from app.core.storage.database import get_database
LINE   33 | # === END PERSISTENCE: PHASE1 (imports) ===
LINE   34 | 
LINE   35 | 
LINE   36 | 
LINE   37 | from app.utils.file_utils import (
LINE   38 |     copy_to_clipboard, write_text_file, KNOWN_BINARY_EXTENSIONS,
LINE   39 |     is_binary_file, get_file_size,
LINE   40 | )
LINE   41 | 
LINE   42 | # ─── Colour palette ─────────────────────────────────────────────────────────
LINE   43 | C_BG        = "#1e2330"   # main background
LINE   44 | C_PANEL     = "#252b3b"   # panel background
LINE   45 | C_BORDER    = "#323a50"   # separator / border
LINE   46 | C_ACCENT    = "#4f8ef7"   # primary accent (blue)
LINE   47 | C_ACCENT_DK = "#3a6fcc"   # accent hover
LINE   48 | C_SUCCESS   = "#3ecf8e"   # green
LINE   49 | C_WARN      = "#f5a623"   # amber
LINE   50 | C_TEXT      = "#e8eaf0"   # primary text
LINE   51 | C_TEXT2     = "#8b92a8"   # secondary / muted
LINE   52 | C_ENTRY     = "#2a3148"   # entry bg
LINE   53 | C_TREE_SEL  = "#2f3d5c"   # tree selection highlight
LINE   54 | C_STAT_BG   = "#161b28"   # bottom bar bg
LINE   55 | # ────────────────────────────────────────────────────────────────────────────
LINE   56 | 
LINE   57 | 
LINE   58 | class MainWindow:
LINE   59 |     def __init__(self, root: tk.Tk):
LINE   60 |         self.root = root
LINE   61 |         self.root.title("DeepSeek Code Packager")
LINE   62 |         self.root.geometry("1340x860")
LINE   63 |         self.root.minsize(1100, 700)
LINE   64 |         self.root.configure(bg=C_BG)
LINE   65 | 
LINE   66 |         # ── State ──────────────────────────────────────────────────────────
LINE   67 |         self.selector   = FileSelectorManager()
LINE   68 |         self.config     = ExportConfig()
LINE   69 |         # === PERSISTENCE: PHASE1 (init) ===
LINE   70 |         self._persist_db = None
LINE   71 |         try:
LINE   72 |             self._persist_db = get_database()
LINE   73 |         except Exception:
LINE   74 |             self._persist_db = None
LINE   75 |         # === END PERSISTENCE: PHASE1 (init) ===
LINE   76 |         # === PHASE 2: DEBOUNCE CHECKBOX ===
LINE   77 |         self._pending_checks = {}
LINE   78 |         self._flush_timer = None
LINE   79 |         # === END PHASE 2 ===
LINE   80 | 
LINE   81 | 
LINE   82 | 
LINE   83 |         default_excl    = ".git, node_modules, __pycache__, venv, .venv, dist, build, .idea, .vscode, vendor, .quasar, .github, public"
LINE   84 |         default_exts    = ", ".join(sorted(DEFAULT_ALLOWED_EXTENSIONS))
LINE   85 | 
LINE   86 |         self.var_folder   = tk.StringVar()
LINE   87 |         self.var_excl     = tk.StringVar(value=default_excl)
LINE   88 |         self.var_exts     = tk.StringVar(value=default_exts)
LINE   89 |         self.var_filter   = tk.BooleanVar(value=True)
LINE   90 |         self.var_lineno   = tk.BooleanVar(value=True)
LINE   91 |         self.var_tree     = tk.BooleanVar(value=True)
LINE   92 |         self.var_instruct = tk.BooleanVar(value=True)
LINE   93 |         self.var_max_file = tk.DoubleVar(value=2.0)
LINE   94 |         self.var_max_tot  = tk.DoubleVar(value=50.0)
LINE   95 |         self.var_max_n    = tk.IntVar(value=100)
LINE   96 |         self.var_fmt      = tk.StringVar(value="markdown")
LINE   97 |         self.var_analysis_type = tk.StringVar(value="Detect errors")
LINE   98 |         self.var_analysis_mode = tk.StringVar(value=MODE_PROBLEM)
LINE   99 | 
LINE  100 |         # Bottom stats vars
LINE  101 |         self.sv_folder    = tk.StringVar(value="0")
LINE  102 |         self.sv_sel_files = tk.StringVar(value="0")
LINE  103 |         self.sv_included  = tk.StringVar(value="0")
LINE  104 |         self.sv_excluded  = tk.StringVar(value="0")
LINE  105 |         self.sv_size      = tk.StringVar(value="0.00 MB")
LINE  106 |         self.sv_lines     = tk.StringVar(value="0")
LINE  107 |         self.sv_status    = tk.StringVar(value="Listo.")
LINE  108 | 
LINE  109 |         self._setup_styles()
LINE  110 |         self._build_header()
LINE  111 |         self._build_main()
LINE  112 |         self._build_bottom()
LINE  113 | 
LINE  114 |     # ── Style helpers ─────────────────────────────────────────────────────
LINE  115 |     def _setup_styles(self):
LINE  116 |         s = ttk.Style()
LINE  117 |         s.theme_use("clam")
LINE  118 | 
LINE  119 |         common = {"background": C_BG, "foreground": C_TEXT, "fieldbackground": C_ENTRY,
LINE  120 |                   "bordercolor": C_BORDER, "lightcolor": C_BORDER, "darkcolor": C_BORDER,
LINE  121 |                   "troughcolor": C_PANEL, "selectbackground": C_TREE_SEL,
LINE  122 |                   "selectforeground": C_TEXT}
LINE  123 | 
LINE  124 |         s.configure(".",                font=("Segoe UI", 9), **common)
LINE  125 |         s.configure("TFrame",           background=C_BG)
LINE  126 |         s.configure("TLabel",           background=C_BG, foreground=C_TEXT)
LINE  127 |         s.configure("TEntry",           fieldbackground=C_ENTRY, foreground=C_TEXT,
LINE  128 |                     insertcolor=C_TEXT, bordercolor=C_BORDER)
LINE  129 |         s.configure("TCheckbutton",     background=C_BG, foreground=C_TEXT2)
LINE  130 |         s.configure("TRadiobutton",     background=C_BG, foreground=C_TEXT2)
LINE  131 |         s.configure("Vertical.TScrollbar",   background=C_BORDER, troughcolor=C_PANEL)
LINE  132 |         s.configure("Horizontal.TScrollbar", background=C_BORDER, troughcolor=C_PANEL)
LINE  133 |         s.configure("TSeparator",       background=C_BORDER)
LINE  134 |         s.configure("TPanedwindow",     background=C_BORDER)
LINE  135 |         s.configure("TSpinbox",         fieldbackground=C_ENTRY, foreground=C_TEXT,
LINE  136 |                     insertcolor=C_TEXT, bordercolor=C_BORDER, arrowcolor=C_TEXT2)
LINE  137 | 
LINE  138 |         # Panel labels
LINE  139 |         s.configure("Panel.TFrame",     background=C_PANEL)
LINE  140 |         s.configure("Panel.TLabel",     background=C_PANEL, foreground=C_TEXT)
LINE  141 |         s.configure("Muted.TLabel",     background=C_PANEL, foreground=C_TEXT2,
LINE  142 |                     font=("Segoe UI", 8))
LINE  143 |         s.configure("Title.TLabel",     background=C_BG, foreground=C_TEXT,
LINE  144 |                     font=("Segoe UI", 15, "bold"))
LINE  145 |         s.configure("Sub.TLabel",       background=C_BG, foreground=C_TEXT2,
LINE  146 |                     font=("Segoe UI", 9))
LINE  147 |         s.configure("Sec.TLabel",       background=C_PANEL, foreground=C_ACCENT,
LINE  148 |                     font=("Segoe UI", 9, "bold"))
LINE  149 |         s.configure("StatKey.TLabel",   background=C_STAT_BG, foreground=C_TEXT2,
LINE  150 |                     font=("Segoe UI", 8))
LINE  151 |         s.configure("StatVal.TLabel",   background=C_STAT_BG, foreground=C_TEXT,
LINE  152 |                     font=("Segoe UI", 10, "bold"))
LINE  153 |         s.configure("Status.TLabel",    background=C_STAT_BG, foreground=C_TEXT2,
LINE  154 |                     font=("Segoe UI", 8, "italic"))
LINE  155 | 
LINE  156 |         # Treeview
LINE  157 |         s.configure("Treeview",         background=C_PANEL, foreground=C_TEXT,
LINE  158 |                     fieldbackground=C_PANEL, bordercolor=C_BORDER, rowheight=22)
LINE  159 |         s.configure("Treeview.Heading", background=C_BORDER, foreground=C_TEXT2,
LINE  160 |                     relief="flat", font=("Segoe UI", 8, "bold"))
LINE  161 |         s.map("Treeview",               background=[("selected", C_TREE_SEL)],
LINE  162 |                                         foreground=[("selected", C_TEXT)])
LINE  163 |         s.map("Treeview.Heading",       background=[("active", C_BORDER)])
LINE  164 | 
LINE  165 |         # Buttons
LINE  166 |         for name, bg, hover in [
LINE  167 |             ("Accent.TButton",  C_ACCENT,   C_ACCENT_DK),
LINE  168 |             ("Success.TButton", C_SUCCESS,  "#2faa75"),
LINE  169 |             ("Neutral.TButton", C_BORDER,   "#404860"),
LINE  170 |             ("Warn.TButton",    C_WARN,     "#cc8b1a"),
LINE  171 |         ]:
LINE  172 |             s.configure(name, background=bg, foreground=C_BG if name != "Neutral.TButton" else C_TEXT,
LINE  173 |                         relief="flat", font=("Segoe UI", 9, "bold"), padding=(10, 5))
LINE  174 |             s.map(name, background=[("active", hover)])
LINE  175 | 
LINE  176 |     # ── Header ────────────────────────────────────────────────────────────
LINE  177 |     def _build_header(self):
LINE  178 |         bar = ttk.Frame(self.root, padding=(16, 10, 16, 8))
LINE  179 |         bar.pack(fill=tk.X)
LINE  180 | 
LINE  181 |         ttk.Label(bar, text="📦  DeepSeek Code Packager", style="Title.TLabel").pack(side=tk.LEFT)
LINE  182 | 
LINE  183 |         right = ttk.Frame(bar)
LINE  184 |         right.pack(side=tk.RIGHT)
LINE  185 |         ttk.Label(right,
LINE  186 |                   text="Sin API · Sin conexión · Proyectos grandes seguros",
LINE  187 |                   style="Sub.TLabel").pack(anchor="e")
LINE  188 | 
LINE  189 |         ttk.Separator(self.root).pack(fill=tk.X)
LINE  190 | 
LINE  191 |     # ── Main 3-pane layout ────────────────────────────────────────────────
LINE  192 |     def _build_main(self):
LINE  193 |         paned = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
LINE  194 |         paned.pack(fill=tk.BOTH, expand=True, padx=8, pady=6)
LINE  195 | 
LINE  196 |         self._build_left(paned)
LINE  197 |         self._build_right(paned)
LINE  198 | 
LINE  199 |     # ──────────────────────────────────────────────────────────────────────
LINE  200 |     # LEFT pane  –  project tree
LINE  201 |     # ──────────────────────────────────────────────────────────────────────
LINE  202 |     def _build_left(self, paned):
LINE  203 |         left = ttk.Frame(paned, style="Panel.TFrame", padding=0)
LINE  204 |         paned.add(left, weight=2)
LINE  205 | 
LINE  206 |         # ── Folder row
LINE  207 |         folder_bar = ttk.Frame(left, style="Panel.TFrame", padding=(8, 6))
LINE  208 |         folder_bar.pack(fill=tk.X)
LINE  209 | 
LINE  210 |         ttk.Label(folder_bar, text="📂  Carpeta del proyecto", style="Sec.TLabel").pack(anchor="w")
LINE  211 | 
LINE  212 |         fe = ttk.Frame(folder_bar, style="Panel.TFrame")
LINE  213 |         fe.pack(fill=tk.X, pady=(4, 0))
LINE  214 | 
LINE  215 |         self.folder_entry = ttk.Entry(fe, textvariable=self.var_folder, state="readonly")
LINE  216 |         self.folder_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 4))
LINE  217 | 
LINE  218 |         ttk.Button(fe, text="📂 Seleccionar carpeta",
LINE  219 |                    style="Accent.TButton",
LINE  220 |                    command=self.on_select_folder).pack(side=tk.LEFT, padx=(0, 3))
LINE  221 |         ttk.Button(fe, text="🔬 Analizar",
LINE  222 |                    style="Accent.TButton",
LINE  223 |                    command=self.on_analyze_project).pack(side=tk.LEFT, padx=(0, 3))
LINE  224 |         ttk.Button(fe, text="✖",
LINE  225 |                    style="Neutral.TButton",
LINE  226 |                    command=self.on_remove_folder, width=3).pack(side=tk.LEFT)
LINE  227 | 
LINE  228 |         ttk.Separator(left).pack(fill=tk.X, pady=4)
LINE  229 | 
LINE  230 |         # ── Filters row (collapsed / compact)
LINE  231 |         flt = ttk.Frame(left, style="Panel.TFrame", padding=(8, 0))
LINE  232 |         flt.pack(fill=tk.X)
LINE  233 | 
LINE  234 |         fl1 = ttk.Frame(flt, style="Panel.TFrame")
LINE  235 |         fl1.pack(fill=tk.X, pady=2)
LINE  236 |         ttk.Label(fl1, text="Excluir carpetas:", style="Muted.TLabel").pack(side=tk.LEFT, padx=(0, 4))
LINE  237 |         ex = ttk.Entry(fl1, textvariable=self.var_excl, font=("Consolas", 8))
LINE  238 |         ex.pack(side=tk.LEFT, fill=tk.X, expand=True)
LINE  239 |         ex.bind("<FocusOut>", lambda _: self.reload_tree())
LINE  240 | 
LINE  241 |         fl2 = ttk.Frame(flt, style="Panel.TFrame")
LINE  242 |         fl2.pack(fill=tk.X, pady=2)
LINE  243 |         ttk.Checkbutton(fl2, text="Filtrar extensiones:", variable=self.var_filter,
LINE  244 |                         command=self.reload_tree, style="TCheckbutton").pack(side=tk.LEFT, padx=(0, 4))
LINE  245 |         ext_e = ttk.Entry(fl2, textvariable=self.var_exts, font=("Consolas", 8))
LINE  246 |         ext_e.pack(side=tk.LEFT, fill=tk.X, expand=True)
LINE  247 |         ext_e.bind("<FocusOut>", lambda _: self.reload_tree())
LINE  248 | 
LINE  249 |         ttk.Separator(left).pack(fill=tk.X, pady=4)
LINE  250 | 
LINE  251 |         # ── Tree toolbar
LINE  252 |         tb = ttk.Frame(left, style="Panel.TFrame", padding=(8, 0, 8, 4))
LINE  253 |         tb.pack(fill=tk.X)
LINE  254 |         ttk.Button(tb, text="☑ Todos", style="Neutral.TButton",
LINE  255 |                    command=self.on_select_all_tree).pack(side=tk.LEFT, padx=(0, 4))
LINE  256 |         ttk.Button(tb, text="☐ Ninguno", style="Neutral.TButton",
LINE  257 |                    command=self.on_deselect_all_tree).pack(side=tk.LEFT, padx=(0, 4))
LINE  258 |         ttk.Button(tb, text="🔬 Analizar proyecto", style="Accent.TButton",
LINE  259 |                    command=self.on_analyze_project).pack(side=tk.LEFT, padx=(0, 4))
LINE  260 |         ttk.Button(tb, text="🧠 Selección Inteligente", style="Accent.TButton",
LINE  261 |                    command=self.on_intelligent_context_select).pack(side=tk.LEFT, padx=(0, 4))
LINE  262 |         ttk.Button(tb, text="🔎 Buscador", style="Accent.TButton",
LINE  263 |                    command=self.on_open_file_search).pack(side=tk.LEFT, padx=(0, 4))
LINE  264 |         ttk.Button(tb, text="🔄 Recargar", style="Neutral.TButton",
LINE  265 |                    command=self.reload_tree).pack(side=tk.RIGHT)
LINE  266 | 
LINE  267 |         # ── Tree widget
LINE  268 |         tc = ttk.Frame(left, style="Panel.TFrame", padding=(4, 0, 4, 4))
LINE  269 |         tc.pack(fill=tk.BOTH, expand=True)
LINE  270 | 
LINE  271 |         self.tree = CheckboxTreeview(tc)
LINE  272 |         sy = ttk.Scrollbar(tc, orient=tk.VERTICAL,   command=self.tree.yview)
LINE  273 |         sx = ttk.Scrollbar(tc, orient=tk.HORIZONTAL, command=self.tree.xview)
LINE  274 |         self.tree.configure(yscrollcommand=sy.set, xscrollcommand=sx.set)
LINE  275 |         sy.pack(side=tk.RIGHT, fill=tk.Y)
LINE  276 |         sx.pack(side=tk.BOTTOM, fill=tk.X)
LINE  277 |         self.tree.pack(fill=tk.BOTH, expand=True)
LINE  278 |         self.tree.bind("<<TreeviewSelect>>", lambda _: self._refresh_selection_stats())
LINE  279 |         self.tree.bind("<ButtonRelease-1>",  lambda _: self.root.after(50, self._refresh_selection_stats))
LINE  280 |         # === PERSISTENCE: PHASE1 (callback) ===
LINE  281 |         if self._persist_db is not None:
LINE  282 |             self.tree.set_check_change_callback(self._on_tree_check_change)
LINE  283 |         # === END PERSISTENCE: PHASE1 (callback) ===
LINE  284 | 
LINE  285 | 
LINE  286 |         ttk.Separator(left).pack(fill=tk.X, pady=4)
LINE  287 | 
LINE  288 |         # ── Individual files list
LINE  289 |         il = ttk.Frame(left, style="Panel.TFrame", padding=(8, 0))
LINE  290 |         il.pack(fill=tk.X)
LINE  291 | 
LINE  292 |         ttk.Label(il, text="📄  Archivos individuales adicionales", style="Sec.TLabel").pack(anchor="w")
LINE  293 | 
LINE  294 |         il_tb = ttk.Frame(il, style="Panel.TFrame")
LINE  295 |         il_tb.pack(fill=tk.X, pady=(4, 3))
LINE  296 |         ttk.Button(il_tb, text="➕ Agregar archivos",
LINE  297 |                    style="Neutral.TButton",
LINE  298 |                    command=self.on_add_individual_files).pack(side=tk.LEFT, padx=(0, 4))
LINE  299 |         ttk.Button(il_tb, text="🗑 Quitar",
LINE  300 |                    style="Neutral.TButton",
LINE  301 |                    command=self.on_remove_individual_file).pack(side=tk.LEFT, padx=(0, 4))
LINE  302 |         ttk.Button(il_tb, text="🧹 Limpiar",
LINE  303 |                    style="Neutral.TButton",
LINE  304 |                    command=self.on_clear_individual_files).pack(side=tk.RIGHT)
LINE  305 | 
LINE  306 |         lc = ttk.Frame(il, style="Panel.TFrame", padding=(0, 0, 0, 6))
LINE  307 |         lc.pack(fill=tk.X)
LINE  308 |         self.file_listbox = tk.Listbox(
LINE  309 |             lc, height=4, selectmode=tk.SINGLE,
LINE  310 |             font=("Consolas", 8),
LINE  311 |             bg=C_ENTRY, fg=C_TEXT,
LINE  312 |             selectbackground=C_TREE_SEL, selectforeground=C_TEXT,
LINE  313 |             relief="flat", bd=0, highlightthickness=0,
LINE  314 |         )
LINE  315 |         ls = ttk.Scrollbar(lc, orient=tk.VERTICAL, command=self.file_listbox.yview)
LINE  316 |         self.file_listbox.configure(yscrollcommand=ls.set)
LINE  317 |         ls.pack(side=tk.RIGHT, fill=tk.Y)
LINE  318 |         self.file_listbox.pack(fill=tk.X, expand=True)
LINE  319 | 
LINE  320 |     # ──────────────────────────────────────────────────────────────────────
LINE  321 |     # RIGHT pane  –  problem description + settings + preview
LINE  322 |     # ──────────────────────────────────────────────────────────────────────
LINE  323 |     def _build_right(self, paned):
LINE  324 |         right = ttk.Frame(paned, style="Panel.TFrame", padding=0)
LINE  325 |         paned.add(right, weight=3)
LINE  326 | 
LINE  327 |         # ── Analysis Type selector (top of right pane)
LINE  328 |         type_hdr = ttk.Frame(right, style="Panel.TFrame", padding=(10, 8, 10, 2))
LINE  329 |         type_hdr.pack(fill=tk.X)
LINE  330 | 
LINE  331 |         t_row = ttk.Frame(type_hdr, style="Panel.TFrame")
LINE  332 |         t_row.pack(fill=tk.X)
LINE  333 | 
LINE  334 |         ttk.Label(t_row, text="🎯  Tipo de análisis:", style="Sec.TLabel").pack(side=tk.LEFT, padx=(0, 6))
LINE  335 | 
LINE  336 |         self.cb_analysis_type = ttk.Combobox(
LINE  337 |             t_row,
LINE  338 |             textvariable=self.var_analysis_type,
LINE  339 |             values=get_all_analysis_types(),
LINE  340 |             state="readonly",
LINE  341 |             font=("Segoe UI", 9, "bold"),
LINE  342 |             width=26
LINE  343 |         )
LINE  344 |         self.cb_analysis_type.pack(side=tk.LEFT, padx=(0, 10))
LINE  345 |         self.cb_analysis_type.bind("<<ComboboxSelected>>", self._on_analysis_type_changed)
LINE  346 | 
LINE  347 |         self.lbl_profile_hint = ttk.Label(
LINE  348 |             type_hdr,
LINE  349 |             text="",
LINE  350 |             style="Muted.TLabel",
LINE  351 |             wraplength=600,
LINE  352 |             justify=tk.LEFT
LINE  353 |         )
LINE  354 |         self.lbl_profile_hint.pack(anchor="w", pady=(3, 0))
LINE  355 | 
LINE  356 |         ttk.Separator(right).pack(fill=tk.X, pady=(4, 2))
LINE  357 | 
LINE  358 |         # ── Analysis Mode selector
LINE  359 |         mode_frame = ttk.Frame(right, style="Panel.TFrame", padding=(10, 6, 10, 2))
LINE  360 |         mode_frame.pack(fill=tk.X)
LINE  361 | 
LINE  362 |         ttk.Label(mode_frame, text="🔁  Modo de análisis:", style="Sec.TLabel").pack(anchor="w", pady=(0, 4))
LINE  363 | 
LINE  364 |         mode_btn_row = ttk.Frame(mode_frame, style="Panel.TFrame")
LINE  365 |         mode_btn_row.pack(fill=tk.X)
LINE  366 | 
LINE  367 |         for mode_key, mode_cfg in ANALYSIS_MODES.items():
LINE  368 |             ttk.Radiobutton(
LINE  369 |                 mode_btn_row,
LINE  370 |                 text=f"{mode_cfg.icon}  {mode_cfg.display_name}",
LINE  371 |                 variable=self.var_analysis_mode,
LINE  372 |                 value=mode_key,
LINE  373 |                 command=self._on_analysis_mode_changed,
LINE  374 |             ).pack(side=tk.LEFT, padx=(0, 18))
LINE  375 | 
LINE  376 |         self.lbl_mode_hint = ttk.Label(
LINE  377 |             mode_frame,
LINE  378 |             text="",
LINE  379 |             style="Muted.TLabel",
LINE  380 |             wraplength=600,
LINE  381 |             justify=tk.LEFT,
LINE  382 |         )
LINE  383 |         self.lbl_mode_hint.pack(anchor="w", pady=(3, 0))
LINE  384 | 
LINE  385 |         ttk.Separator(right).pack(fill=tk.X, pady=(4, 2))
LINE  386 | 
LINE  387 |         # ── Problem container (visible in Problem Mode, hidden in Project Mode)
LINE  388 |         self.problem_container = ttk.Frame(right, style="Panel.TFrame")
LINE  389 |         self.problem_container.pack(fill=tk.X)
LINE  390 | 
LINE  391 |         desc_hdr = ttk.Frame(self.problem_container, style="Panel.TFrame", padding=(10, 6, 10, 4))
LINE  392 |         desc_hdr.pack(fill=tk.X)
LINE  393 |         ttk.Label(desc_hdr, text="📝  Describe el problema / objetivo", style="Sec.TLabel").pack(anchor="w")
LINE  394 |         ttk.Label(desc_hdr,
LINE  395 |                   text="Este texto se incluirá en deepseek_prompt.md como REPORTED PROBLEM OR GOAL",
LINE  396 |                   style="Muted.TLabel").pack(anchor="w")
LINE  397 | 
LINE  398 |         desc_body = ttk.Frame(self.problem_container, style="Panel.TFrame", padding=(10, 0))
LINE  399 |         desc_body.pack(fill=tk.X)
LINE  400 |         self.problem_text = scrolledtext.ScrolledText(
LINE  401 |             desc_body, height=5,
LINE  402 |             font=("Segoe UI", 10),
LINE  403 |             bg=C_ENTRY, fg=C_TEXT,
LINE  404 |             insertbackground=C_TEXT,
LINE  405 |             selectbackground=C_TREE_SEL, selectforeground=C_TEXT,
LINE  406 |             relief="flat", bd=1, padx=8, pady=6,
LINE  407 |             wrap=tk.WORD,
LINE  408 |         )
LINE  409 |         self.problem_text.pack(fill=tk.X, expand=True)
LINE  410 | 
LINE  411 |         # ── Project Mode info card (visible in Project Mode, hidden in Problem Mode)
LINE  412 |         self.project_mode_container = ttk.Frame(right, style="Panel.TFrame")
LINE  413 |         # not packed initially — shown by _on_analysis_mode_changed
LINE  414 | 
LINE  415 |         proj_card = ttk.Frame(self.project_mode_container, style="Panel.TFrame", padding=(10, 8))
LINE  416 |         proj_card.pack(fill=tk.X, padx=10, pady=4)
LINE  417 |         ttk.Label(proj_card, text="🏗️  Modo Proyecto — Auditoría Holística", style="Sec.TLabel").pack(anchor="w")
LINE  418 |         ttk.Label(
LINE  419 |             proj_card,
LINE  420 |             text=(
LINE  421 |                 "La IA analizará el proyecto completo de forma transversal:\n"
LINE  422 |                 "  • Errores y bugs latentes\n"
LINE  423 |                 "  • Código duplicado y deuda técnica (DRY)\n"
LINE  424 |                 "  • Malas prácticas e ineficiencias de diseño\n"
LINE  425 |                 "  • Problemas arquitectónicos y acoplamiento\n"
LINE  426 |                 "  • Vulnerabilidades de seguridad (OWASP)\n"
LINE  427 |                 "  • Oportunidades de optimización de rendimiento\n\n"
LINE  428 |                 "Genera una matriz de hallazgos priorizados y un plan de acción por fases."
LINE  429 |             ),
LINE  430 |             style="Muted.TLabel",
LINE  431 |             justify=tk.LEFT,
LINE  432 |         ).pack(anchor="w", pady=(4, 0))
LINE  433 | 
LINE  434 |         self._on_analysis_type_changed(init=True)
LINE  435 |         self._on_analysis_mode_changed(init=True)
LINE  436 | 
LINE  437 |         ttk.Separator(right).pack(fill=tk.X, pady=6)
LINE  438 | 
LINE  439 |         # ── Generation settings (collapsible look)
LINE  440 |         cfg = ttk.Frame(right, style="Panel.TFrame", padding=(10, 0))
LINE  441 |         cfg.pack(fill=tk.X)
LINE  442 | 
LINE  443 |         ttk.Label(cfg, text="⚙️  Configuración de generación", style="Sec.TLabel").pack(anchor="w", pady=(0, 4))
LINE  444 | 
LINE  445 |         r1 = ttk.Frame(cfg, style="Panel.TFrame")
LINE  446 |         r1.pack(fill=tk.X, pady=2)
LINE  447 |         ttk.Label(r1, text="Máx. archivo:", style="Muted.TLabel").pack(side=tk.LEFT, padx=(0, 3))
LINE  448 |         ttk.Spinbox(r1, from_=0.1, to=50.0, increment=0.5,
LINE  449 |                     textvariable=self.var_max_file, width=5).pack(side=tk.LEFT, padx=(0, 12))
LINE  450 |         ttk.Label(r1, text="MB  ·  Máx. total:", style="Muted.TLabel").pack(side=tk.LEFT, padx=(0, 3))
LINE  451 |         ttk.Spinbox(r1, from_=1.0, to=500.0, increment=5.0,
LINE  452 |                     textvariable=self.var_max_tot, width=6).pack(side=tk.LEFT, padx=(0, 12))
LINE  453 |         ttk.Label(r1, text="MB  ·  Máx. archivos:", style="Muted.TLabel").pack(side=tk.LEFT, padx=(0, 3))
LINE  454 |         ttk.Spinbox(r1, from_=1, to=5000, increment=10,
LINE  455 |                     textvariable=self.var_max_n, width=5).pack(side=tk.LEFT)
LINE  456 | 
LINE  457 |         r2 = ttk.Frame(cfg, style="Panel.TFrame")
LINE  458 |         r2.pack(fill=tk.X, pady=2)
LINE  459 |         for txt, var in [
LINE  460 |             ("Nº de línea", self.var_lineno),
LINE  461 |             ("Árbol de carpetas", self.var_tree),
LINE  462 |             ("Instrucciones DeepSeek", self.var_instruct),
LINE  463 |             ("Filtrar por extensión", self.var_filter),
LINE  464 |         ]:
LINE  465 |             ttk.Checkbutton(r2, text=txt, variable=var).pack(side=tk.LEFT, padx=(0, 14))
LINE  466 |         ttk.Label(r2, text="Formato:", style="Muted.TLabel").pack(side=tk.LEFT, padx=(8, 3))
LINE  467 |         ttk.Radiobutton(r2, text="Markdown", value="markdown", variable=self.var_fmt).pack(side=tk.LEFT, padx=(0, 6))
LINE  468 |         ttk.Radiobutton(r2, text="Texto",    value="text",     variable=self.var_fmt).pack(side=tk.LEFT)
LINE  469 | 
LINE  470 |         ttk.Separator(right).pack(fill=tk.X, pady=6)
LINE  471 | 
LINE  472 |         # ── Preview label
LINE  473 |         prev_hdr = ttk.Frame(right, style="Panel.TFrame", padding=(10, 0))
LINE  474 |         prev_hdr.pack(fill=tk.X)
LINE  475 |         ttk.Label(prev_hdr, text="🔍  Vista previa del documento generado", style="Sec.TLabel").pack(anchor="w")
LINE  476 | 
LINE  477 |         # ── Preview area
LINE  478 |         prev_body = ttk.Frame(right, style="Panel.TFrame", padding=(10, 4, 10, 4))
LINE  479 |         prev_body.pack(fill=tk.BOTH, expand=True)
LINE  480 |         self.preview_text = scrolledtext.ScrolledText(
LINE  481 |             prev_body, wrap=tk.NONE,
LINE  482 |             font=("Consolas", 9),
LINE  483 |             bg=C_ENTRY, fg=C_TEXT,
LINE  484 |             insertbackground=C_TEXT,
LINE  485 |             selectbackground=C_TREE_SEL, selectforeground=C_TEXT,
LINE  486 |             relief="flat", bd=0, padx=8, pady=6,
LINE  487 |         )
LINE  488 |         self.preview_text.pack(fill=tk.BOTH, expand=True)
LINE  489 | 
LINE  490 |     # ──────────────────────────────────────────────────────────────────────
LINE  491 |     # BOTTOM  –  stats bar + action buttons
LINE  492 |     # ──────────────────────────────────────────────────────────────────────
LINE  493 |     def _build_bottom(self):
LINE  494 |         ttk.Separator(self.root).pack(fill=tk.X)
LINE  495 | 
LINE  496 |         bottom = tk.Frame(self.root, bg=C_STAT_BG)
LINE  497 |         bottom.pack(fill=tk.X, side=tk.BOTTOM)
LINE  498 | 
LINE  499 |         # ── Action buttons (left side of bottom bar)
LINE  500 |         btn_strip = tk.Frame(bottom, bg=C_STAT_BG, padx=8, pady=6)
LINE  501 |         btn_strip.pack(side=tk.LEFT)
LINE  502 | 
LINE  503 |         ttk.Button(btn_strip, text="🔬 Analizar proyecto",
LINE  504 |                    style="Neutral.TButton",
LINE  505 |                    command=self.on_analyze_project).pack(side=tk.LEFT, padx=(0, 5))
LINE  506 |         ttk.Button(btn_strip, text="⚡ Generar contexto",
LINE  507 |                    style="Accent.TButton",
LINE  508 |                    command=self.on_generate_prompt).pack(side=tk.LEFT, padx=(0, 5))
LINE  509 |         ttk.Button(btn_strip, text="📁 Abrir carpeta resultados",
LINE  510 |                    style="Success.TButton",
LINE  511 |                    command=self.on_open_results_folder).pack(side=tk.LEFT, padx=(0, 5))
LINE  512 |         ttk.Button(btn_strip, text="📋 Copiar prompt",
LINE  513 |                    style="Neutral.TButton",
LINE  514 |                    command=self.on_copy_clipboard).pack(side=tk.LEFT, padx=(0, 5))
LINE  515 |         ttk.Button(btn_strip, text="💾 Guardar como…",
LINE  516 |                    style="Neutral.TButton",
LINE  517 |                    command=self.on_export_file).pack(side=tk.LEFT, padx=(0, 5))
LINE  518 |         ttk.Button(btn_strip, text="🗑 Limpiar selección",
LINE  519 |                    style="Neutral.TButton",
LINE  520 |                    command=self.on_clear_all).pack(side=tk.LEFT)
LINE  521 | 
LINE  522 |         # ── Stat tiles (right side of bottom bar)
LINE  523 |         stats = tk.Frame(bottom, bg=C_STAT_BG, padx=12, pady=4)
LINE  524 |         stats.pack(side=tk.RIGHT)
LINE  525 | 
LINE  526 |         def _stat(parent, key):
LINE  527 |             cell = tk.Frame(parent, bg=C_STAT_BG, padx=10, pady=2)
LINE  528 |             cell.pack(side=tk.LEFT)
LINE  529 |             var = tk.StringVar(value="—")
LINE  530 |             tk.Label(cell, text=key, bg=C_STAT_BG, fg=C_TEXT2,
LINE  531 |                      font=("Segoe UI", 8)).pack()
LINE  532 |             tk.Label(cell, textvariable=var, bg=C_STAT_BG, fg=C_TEXT,
LINE  533 |                      font=("Segoe UI", 11, "bold")).pack()
LINE  534 |             return var
LINE  535 | 
LINE  536 |         self.sv_folder    = _stat(stats, "Carpeta")
LINE  537 |         self.sv_sel_files = _stat(stats, "Archivos sel.")
LINE  538 |         self.sv_included  = _stat(stats, "Incluidos")
LINE  539 |         self.sv_excluded  = _stat(stats, "Excluidos")
LINE  540 |         self.sv_size      = _stat(stats, "Tamaño total")
LINE  541 |         self.sv_lines     = _stat(stats, "Líneas")
LINE  542 | 
LINE  543 |         # ── Status text (very bottom strip)
LINE  544 |         status_bar = tk.Frame(self.root, bg="#0f1320", pady=2)
LINE  545 |         status_bar.pack(fill=tk.X, side=tk.BOTTOM)
LINE  546 |         tk.Label(status_bar, textvariable=self.sv_status,
LINE  547 |                  bg="#0f1320", fg=C_TEXT2,
LINE  548 |                  font=("Segoe UI", 8, "italic"),
LINE  549 |                  anchor="w", padx=10).pack(fill=tk.X)
LINE  550 | 
LINE  551 |         self.sv_status.set("Listo. Selecciona una carpeta para comenzar.")
LINE  552 | 
LINE  553 |     # ── Stat refresh ─────────────────────────────────────────────────────
LINE  554 |     def _refresh_selection_stats(self):
LINE  555 |         folder  = self.var_folder.get()
LINE  556 |         has_fld = 1 if folder else 0
LINE  557 |         sel_files = len(self.tree.get_checked_files()) + len(self.selector.get_selection().individual_files)
LINE  558 | 
LINE  559 |         # Count binary vs. included among selected files
LINE  560 |         included = 0
LINE  561 |         excluded = 0
LINE  562 |         total_bytes = 0
LINE  563 | 
LINE  564 |         checked = self.tree.get_checked_files()
LINE  565 |         ind     = self.selector.get_selection().individual_files
LINE  566 | 
LINE  567 |         all_paths = []
LINE  568 |         if folder:
LINE  569 |             for rel in checked:
LINE  570 |                 all_paths.append(os.path.join(folder, rel))
LINE  571 |         for abs_p in ind:
LINE  572 |             all_paths.append(abs_p)
LINE  573 | 
LINE  574 |         for fp in all_paths:
LINE  575 |             if not os.path.isfile(fp):
LINE  576 |                 continue
LINE  577 |             if is_binary_file(fp):
LINE  578 |                 excluded += 1
LINE  579 |             else:
LINE  580 |                 included += 1
LINE  581 |                 total_bytes += get_file_size(fp)
LINE  582 | 
LINE  583 |         size_mb = total_bytes / (1024 * 1024)
LINE  584 | 
LINE  585 |         self.sv_folder.set(str(has_fld))
LINE  586 |         self.sv_sel_files.set(str(sel_files))
LINE  587 |         self.sv_included.set(str(included))
LINE  588 |         self.sv_excluded.set(str(excluded))
LINE  589 |         self.sv_size.set(f"{size_mb:.2f} MB")
LINE  590 |         # Lines shown only after generation
LINE  591 |         # self.sv_lines is updated in on_generate_prompt
LINE  592 | 
LINE  593 |     # ── UI event handlers ────────────────────────────────────────────────
LINE  594 |     # === PERSISTENCE: PHASE1 (method) ===
LINE  595 |     def _on_tree_check_change(self, rel_path: str, is_checked: bool):
LINE  596 |         """Persist checkbox changes to SQLite (Phase 1)."""
LINE  597 |         if self._persist_db is None:
LINE  598 |             return
LINE  599 |         folder = self.var_folder.get()
LINE  600 |         if not folder:
LINE  601 |             return
LINE  602 |         try:
LINE  603 |             project_id = self._persist_db.get_or_create_project(folder)
LINE  604 |             self._persist_db.update_is_checked(project_id, rel_path, is_checked)
LINE  605 |         except Exception:
LINE  606 |             pass
LINE  607 |     # === END PERSISTENCE: PHASE1 (method) ===
LINE  608 | 
LINE  609 |     def on_select_folder(self):
LINE  610 |         folder = dialogs.ask_folder("Seleccionar Carpeta del Proyecto")
LINE  611 |         if folder:
LINE  612 |             self.selector.set_folder(folder)
LINE  613 |             self.var_folder.set(folder)
LINE  614 |             self.reload_tree()
LINE  615 |             self._refresh_selection_stats()
LINE  616 |             self.sv_status.set(f"Carpeta seleccionada: {folder}")
LINE  617 | 
LINE  618 |     def on_analyze_project(self):
LINE  619 |         folder = self.var_folder.get()
LINE  620 |         if not folder or not os.path.isdir(folder):
LINE  621 |             folder = dialogs.ask_folder("Seleccionar Carpeta para Analizar")
LINE  622 |             if not folder:
LINE  623 |                 return
LINE  624 |             self.selector.set_folder(folder)
LINE  625 |             self.var_folder.set(folder)
LINE  626 |             self.reload_tree()
LINE  627 | 
LINE  628 |         self.sv_status.set("Analizando estructura, tecnologías y dependencias del proyecto...")
LINE  629 |         self.root.update_idletasks()
LINE  630 | 
LINE  631 |         self.selector.set_exclusions_from_string(self.var_excl.get())
LINE  632 |         excluded = self.selector.get_selection().excluded_dirs
LINE  633 | 
LINE  634 |         try:
LINE  635 |             max_file_mb = float(self.var_max_file.get())
LINE  636 |         except ValueError:
LINE  637 |             max_file_mb = 2.0
LINE  638 | 
LINE  639 |         analyzer = ProjectAnalyzer(excluded_dirs=excluded)
LINE  640 |         result = analyzer.analyze(folder, max_file_size_mb=max_file_mb)
LINE  641 |         # === PERSISTENCE: PHASE1 (analyze) ===
LINE  642 |         try:
LINE  643 |             analyzer.persist_result(result)
LINE  644 |         except Exception:
LINE  645 |             pass
LINE  646 |         # === END PERSISTENCE: PHASE1 (analyze) ===
LINE  647 | 
LINE  648 | 
LINE  649 |         self.sv_status.set(
LINE  650 |             f"Análisis completado: {result.total_files} archivos, {result.total_lines:,} líneas. "
LINE  651 |             f"Lenguaje: {result.primary_language} · Framework: {result.framework}"
LINE  652 |         )
LINE  653 | 
LINE  654 |         ProjectAnalysisDialog(
LINE  655 |             self.root,
LINE  656 |             analysis=result,
LINE  657 |             on_apply_selection=self.apply_recommended_selection
LINE  658 |         )
LINE  659 | 
LINE  660 |     def on_intelligent_context_select(self):
LINE  661 |         folder = self.var_folder.get()
LINE  662 |         if not folder or not os.path.isdir(folder):
LINE  663 |             dialogs.show_warning("Atención", "Selecciona una carpeta del proyecto primero.")
LINE  664 |             return
LINE  665 | 
LINE  666 |         problem_desc = self.problem_text.get("1.0", tk.END).strip()
LINE  667 |         if not problem_desc:
LINE  668 |             dialogs.show_warning(
LINE  669 |                 "Atención",
LINE  670 |                 "Ingresa una descripción del problema en el panel derecho para realizar la selección inteligente."
LINE  671 |             )
LINE  672 |             return
LINE  673 | 
LINE  674 |         self.sv_status.set("Ejecutando Selección Inteligente de Contexto...")
LINE  675 |         self.root.update_idletasks()
LINE  676 | 
LINE  677 |         # Get candidate files (all checked files in tree, or all files in tree if none checked)
LINE  678 |         candidate_files = self.tree.get_checked_files()
LINE  679 |         if not candidate_files:
LINE  680 |             all_files = []
LINE  681 |             def _gather(item):
LINE  682 |                 if not self.tree.get_children(item):
LINE  683 |                     name = self.tree.set(item, "name")
LINE  684 |                     if name:
LINE  685 |                         all_files.append(name)
LINE  686 |                 for child in self.tree.get_children(item):
LINE  687 |                     _gather(child)
LINE  688 |             for r in self.tree.get_children():
LINE  689 |                 _gather(r)
LINE  690 |             candidate_files = all_files
LINE  691 | 
LINE  692 |         try:
LINE  693 |             max_file_mb = float(self.var_max_file.get())
LINE  694 |             max_tot_mb = float(self.var_max_tot.get())
LINE  695 |             max_n = int(self.var_max_n.get())
LINE  696 |         except ValueError:
LINE  697 |             max_file_mb, max_tot_mb, max_n = 2.0, 50.0, 100
LINE  698 | 
LINE  699 |         analyzer = IntelligentContextAnalyzer()
LINE  700 |         prioritized = analyzer.analyze(
LINE  701 |             folder_path=folder,
LINE  702 |             candidate_rel_files=candidate_files,
LINE  703 |             problem_desc=problem_desc,
LINE  704 |             max_file_size_mb=max_file_mb,
LINE  705 |             max_total_size_mb=max_tot_mb,
LINE  706 |             max_files=max_n
LINE  707 |         )
LINE  708 | 
LINE  709 |         IntelligentContextDialog(
LINE  710 |             self.root,
LINE  711 |             problem_desc=problem_desc,
LINE  712 |             prioritized_files=prioritized,
LINE  713 |             on_confirm=self.apply_recommended_selection
LINE  714 |         )
LINE  715 |         self.sv_status.set("Selección Inteligente completada.")
LINE  716 | 
LINE  717 |     def _on_analysis_type_changed(self, event=None, init: bool = False):
LINE  718 |         selected = self.var_analysis_type.get()
LINE  719 |         profile = get_analysis_profile(selected)
LINE  720 |         if hasattr(self, "lbl_profile_hint"):
LINE  721 |             self.lbl_profile_hint.config(
LINE  722 |                 text=f"{profile.icon} {profile.objective}\nEnfoque: {profile.focus}"
LINE  723 |             )
LINE  724 |         if hasattr(self, "problem_text"):
LINE  725 |             current_text = self.problem_text.get("1.0", tk.END).strip()
LINE  726 |             all_hints = {p.default_prompt_hint for p in ANALYSIS_PROFILES.values()}
LINE  727 |             all_hints.add("Por favor analiza el siguiente código del proyecto. Identifica posibles errores, refactorizaciones recomendadas y soluciones al problema.")
LINE  728 | 
LINE  729 |             if not current_text or current_text in all_hints or init:
LINE  730 |                 self.problem_text.delete("1.0", tk.END)
LINE  731 |                 self.problem_text.insert("1.0", profile.default_prompt_hint)
LINE  732 | 
LINE  733 |     def _on_analysis_mode_changed(self, event=None, init: bool = False):
LINE  734 |         """Shows/hides problem container vs project-mode card based on selected mode."""
LINE  735 |         mode_key = self.var_analysis_mode.get()
LINE  736 |         mode_cfg = get_analysis_mode_config(mode_key)
LINE  737 | 
LINE  738 |         if hasattr(self, "lbl_mode_hint"):
LINE  739 |             self.lbl_mode_hint.config(text=mode_cfg.description)
LINE  740 | 
LINE  741 |         if mode_key == MODE_PROJECT:
LINE  742 |             if hasattr(self, "problem_container"):
LINE  743 |                 self.problem_container.pack_forget()
LINE  744 |             if hasattr(self, "project_mode_container"):
LINE  745 |                 self.project_mode_container.pack(fill=tk.X, after=None)
LINE  746 |                 # Insert after the separator that precedes the problem_container
LINE  747 |                 self.project_mode_container.pack(fill=tk.X)
LINE  748 |         else:
LINE  749 |             if hasattr(self, "project_mode_container"):
LINE  750 |                 self.project_mode_container.pack_forget()
LINE  751 |             if hasattr(self, "problem_container"):
LINE  752 |                 self.problem_container.pack(fill=tk.X)
LINE  753 | 
LINE  754 |     def apply_recommended_selection(self, selected_files: List[str], notify: bool = True):
LINE  755 |         if not selected_files:
LINE  756 |             if notify:
LINE  757 |                 dialogs.show_warning("Atención", "No se seleccionó ningún archivo recomendado.")
LINE  758 |             return
LINE  759 | 
LINE  760 |         self.tree.set_checked_files(set(selected_files))
LINE  761 |         self.selector.set_checked_folder_files(self.tree.get_checked_files())
LINE  762 |         self._refresh_selection_stats()
LINE  763 |         count = len(selected_files)
LINE  764 |         self.sv_status.set(f"✓ Selección recomendada aplicada: {count} archivo(s) preparados para contexto.")
LINE  765 |         if notify:
LINE  766 |             dialogs.show_info(
LINE  767 |                 "Selección Aplicada",
LINE  768 |                 f"Se han aplicado {count} archivo(s) recomendados para el contexto.\n\n"
LINE  769 |                 "Puedes pulsar '⚡ Generar contexto' directamente cuando estés listo."
LINE  770 |             )
LINE  771 | 
LINE  772 |     def on_remove_folder(self):
LINE  773 |         self.selector.remove_folder()
LINE  774 |         self.var_folder.set("")
LINE  775 |         for item in self.tree.get_children():
LINE  776 |             self.tree.delete(item)
LINE  777 |         self.tree.checked_items.clear()
LINE  778 |         self._refresh_selection_stats()
LINE  779 |         self.sv_status.set("Carpeta removida.")
LINE  780 | 
LINE  781 |     def on_clear_all(self):
LINE  782 |         self.on_remove_folder()
LINE  783 |         self.on_clear_individual_files()
LINE  784 |         self.preview_text.delete("1.0", tk.END)
LINE  785 |         self.sv_lines.set("0")
LINE  786 |         self.sv_status.set("Selección limpiada.")
LINE  787 | 
LINE  788 |     def reload_tree(self):
LINE  789 |         for item in self.tree.get_children():
LINE  790 |             self.tree.delete(item)
LINE  791 |         self.tree.checked_items.clear()
LINE  792 | 
LINE  793 |         folder = self.var_folder.get()
LINE  794 |         if not folder or not os.path.isdir(folder):
LINE  795 |             return
LINE  796 | 
LINE  797 |         self.selector.set_exclusions_from_string(self.var_excl.get())
LINE  798 |         excluded_dirs = self.selector.get_selection().excluded_dirs
LINE  799 |         allowed_exts  = self._get_exts()
LINE  800 |         filter_ext    = self.var_filter.get()
LINE  801 | 
LINE  802 |         root_item = self.tree.insert("", "end", text="📁",
LINE  803 |                                      values=("", os.path.basename(folder)), open=True)
LINE  804 |         folder_items = {".": root_item}
LINE  805 | 
LINE  806 |         for dirpath, dirnames, filenames in os.walk(folder):
LINE  807 |             dirnames[:] = [d for d in sorted(dirnames) if d not in excluded_dirs]
LINE  808 |             rel_dir = os.path.relpath(dirpath, folder)
LINE  809 | 
LINE  810 |             parent_item = folder_items.get(rel_dir)
LINE  811 |             if not parent_item:
LINE  812 |                 continue
LINE  813 | 
LINE  814 |             for d in dirnames:
LINE  815 |                 rel_sub = os.path.join(rel_dir, d) if rel_dir != "." else d
LINE  816 |                 item = self.tree.insert_folder(parent_item, rel_sub)
LINE  817 |                 folder_items[rel_sub] = item
LINE  818 | 
LINE  819 |             for f in sorted(filenames):
LINE  820 |                 ext = os.path.splitext(f)[1].lower()
LINE  821 |                 if ext in KNOWN_BINARY_EXTENSIONS:
LINE  822 |                     continue
LINE  823 |                 if filter_ext and allowed_exts and ext not in allowed_exts:
LINE  824 |                     continue
LINE  825 |                 rel_file = os.path.join(rel_dir, f) if rel_dir != "." else f
LINE  826 |                 self.tree.insert_file(parent_item, rel_file)
LINE  827 |         # === PERSISTENCE: PHASE1 (reload) ===
LINE  828 |         if self._persist_db is not None:
LINE  829 |             try:
LINE  830 |                 saved = self._persist_db.load_checked_state(folder)
LINE  831 |                 if saved is not None:
LINE  832 |                     self.tree.set_checked_files(saved)
LINE  833 |                     self.selector.set_checked_folder_files(
LINE  834 |                         self.tree.get_checked_files()
LINE  835 |                     )
LINE  836 |             except Exception:
LINE  837 |                 pass
LINE  838 |         # === END PERSISTENCE: PHASE1 (reload) ===
LINE  839 | 
LINE  840 | 
LINE  841 |         self._refresh_selection_stats()
LINE  842 | 
LINE  843 |     def _find_folder_item(self, rel_path: str):
LINE  844 |         def search(item):
LINE  845 |             if self.tree.set(item, "name") == rel_path:
LINE  846 |                 return item
LINE  847 |             for ch in self.tree.get_children(item):
LINE  848 |                 found = search(ch)
LINE  849 |                 if found:
LINE  850 |                     return found
LINE  851 |             return None
LINE  852 |         for item in self.tree.get_children():
LINE  853 |             found = search(item)
LINE  854 |             if found:
LINE  855 |                 return found
LINE  856 |         return None
LINE  857 | 
LINE  858 |     def _get_exts(self) -> set:
LINE  859 |         exts = set()
LINE  860 |         for e in self.var_exts.get().split(","):
LINE  861 |             c = e.strip().lower()
LINE  862 |             if c:
LINE  863 |                 exts.add(c if c.startswith(".") else "." + c)
LINE  864 |         return exts
LINE  865 | 
LINE  866 |     def on_select_all_tree(self):
LINE  867 |         self.tree.select_all()
LINE  868 |         self._refresh_selection_stats()
LINE  869 | 
LINE  870 |     def on_deselect_all_tree(self):
LINE  871 |         self.tree.deselect_all()
LINE  872 |         self._refresh_selection_stats()
LINE  873 | 
LINE  874 |     def on_add_individual_files(self):
LINE  875 |         files = dialogs.ask_files("Seleccionar Archivos Individuales")
LINE  876 |         if files:
LINE  877 |             added = self.selector.add_individual_files(files)
LINE  878 |             self.file_listbox.delete(0, tk.END)
LINE  879 |             for f in self.selector.get_selection().individual_files:
LINE  880 |                 self.file_listbox.insert(tk.END, f)
LINE  881 |             self._refresh_selection_stats()
LINE  882 |             self.sv_status.set(f"Se agregaron {added} archivo(s) individual(es).")
LINE  883 | 
LINE  884 |     def on_remove_individual_file(self):
LINE  885 |         sel = self.file_listbox.curselection()
LINE  886 |         if sel:
LINE  887 |             val = self.file_listbox.get(sel[0])
LINE  888 |             self.selector.remove_individual_file(val)
LINE  889 |             self.file_listbox.delete(sel[0])
LINE  890 |             self._refresh_selection_stats()
LINE  891 |             self.sv_status.set(f"Archivo removido: {os.path.basename(val)}")
LINE  892 | 
LINE  893 |     def on_clear_individual_files(self):
LINE  894 |         self.selector.clear_individual_files()
LINE  895 |         self.file_listbox.delete(0, tk.END)
LINE  896 |         self._refresh_selection_stats()
LINE  897 |         self.sv_status.set("Lista de archivos individuales limpiada.")
LINE  898 | 
LINE  899 |     def get_output_dir(self) -> str:
LINE  900 |         out_dir = os.path.join(
LINE  901 |             os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "output"
LINE  902 |         )
LINE  903 |         os.makedirs(out_dir, exist_ok=True)
LINE  904 |         return out_dir
LINE  905 | 
LINE  906 |     def on_open_results_folder(self):
LINE  907 |         out_dir = self.get_output_dir()
LINE  908 |         try:
LINE  909 |             if os.name == "nt":
LINE  910 |                 os.startfile(out_dir)
LINE  911 |             else:
LINE  912 |                 subprocess.run(["open" if sys.platform == "darwin" else "xdg-open", out_dir])
LINE  913 |             self.sv_status.set(f"Carpeta de resultados abierta: {out_dir}")
LINE  914 |         except Exception as exc:
LINE  915 |             dialogs.show_error("Error", f"No se pudo abrir la carpeta: {exc}")
LINE  916 | 
LINE  917 |     def on_generate_prompt(self):
LINE  918 |         folder = self.var_folder.get()
LINE  919 |         ind    = self.selector.get_selection().individual_files
LINE  920 | 
LINE  921 |         if not folder and not ind:
LINE  922 |             dialogs.show_warning("Atención",
LINE  923 |                                  "Selecciona una carpeta o al menos un archivo individual.")
LINE  924 |             return
LINE  925 | 
LINE  926 |         self.selector.set_checked_folder_files(self.tree.get_checked_files())
LINE  927 |         self.selector.set_exclusions_from_string(self.var_excl.get())
LINE  928 | 
LINE  929 |         try: self.config.max_file_size_mb  = float(self.var_max_file.get())
LINE  930 |         except ValueError: self.config.max_file_size_mb = 2.0
LINE  931 | 
LINE  932 |         try: self.config.max_total_size_mb = float(self.var_max_tot.get())
LINE  933 |         except ValueError: self.config.max_total_size_mb = 50.0
LINE  934 | 
LINE  935 |         try: self.config.max_files = int(self.var_max_n.get())
LINE  936 |         except ValueError: self.config.max_files = 100
LINE  937 | 
LINE  938 |         self.config.add_line_numbers        = self.var_lineno.get()
LINE  939 |         self.config.include_tree            = self.var_tree.get()
LINE  940 |         self.config.include_system_instructions = self.var_instruct.get()
LINE  941 |         self.config.output_format           = self.var_fmt.get()
LINE  942 |         self.config.analysis_type           = self.var_analysis_type.get()
LINE  943 |         self.config.analysis_mode           = self.var_analysis_mode.get()
LINE  944 | 
LINE  945 |         problem_desc = self.problem_text.get("1.0", tk.END).strip()
LINE  946 |         # In Project Mode, ignore the problem text field
LINE  947 |         if self.config.analysis_mode == MODE_PROJECT:
LINE  948 |             problem_desc = ""
LINE  949 |         gen = PromptGenerator(self.config)
LINE  950 | 
LINE  951 |         doc_text, included, excluded, omitted, total_lines = gen.generate(
LINE  952 |             self.selector.get_selection(), problem_desc
LINE  953 |         )
LINE  954 | 
LINE  955 |         if included == 0 and omitted == 0:
LINE  956 |             dialogs.show_warning("Atención",
LINE  957 |                                  "No hay archivos de código válidos seleccionados.")
LINE  958 |             return
LINE  959 | 
LINE  960 |         # Preview
LINE  961 |         self.preview_text.delete("1.0", tk.END)
LINE  962 |         self.preview_text.insert(tk.END, doc_text)
LINE  963 | 
LINE  964 |         # Update bottom stats
LINE  965 |         self._refresh_selection_stats()
LINE  966 |         self.sv_included.set(str(included))
LINE  967 |         self.sv_excluded.set(str(excluded))
LINE  968 |         self.sv_lines.set(f"{total_lines:,}")
LINE  969 | 
LINE  970 |         # Save output files
LINE  971 |         out_dir     = self.get_output_dir()
LINE  972 |         md_text, _, _, _, _  = generate_markdown_bundle(
LINE  973 |             self.selector.get_selection(), problem_desc, self.config)
LINE  974 |         txt_text, _, _, _, _ = generate_text_bundle(
LINE  975 |             self.selector.get_selection(), problem_desc, self.config)
LINE  976 |         prompt_text = generate_standalone_prompt(
LINE  977 |             problem_desc,
LINE  978 |             analysis_type=self.config.analysis_type,
LINE  979 |             analysis_mode=self.config.analysis_mode,
LINE  980 |         )
LINE  981 | 
LINE  982 |         write_text_file(os.path.join(out_dir, "deepseek_project_context.md"),  md_text)
LINE  983 |         write_text_file(os.path.join(out_dir, "deepseek_project_context.txt"), txt_text)
LINE  984 |         write_text_file(os.path.join(out_dir, "deepseek_prompt.md"),           prompt_text)
LINE  985 | 
LINE  986 |         dialogs.show_info(
LINE  987 |             "✅ Archivos Preparados",
LINE  988 |             f"Archivos generados en:\n{out_dir}\n\n"
LINE  989 |             f"• Incluidos:  {included}\n"
LINE  990 |             f"• Excluidos:  {excluded}\n"
LINE  991 |             f"• Omitidos:   {omitted}\n"
LINE  992 |             f"• Líneas:     {total_lines:,}\n\n"
LINE  993 |             "Abre DeepSeek en tu navegador y adjunta:\n"
LINE  994 |             "  1. deepseek_prompt.md\n"
LINE  995 |             "  2. deepseek_project_context.md\n"
LINE  996 |             "  3. deepseek_project_context.txt"
LINE  997 |         )
LINE  998 |         self.sv_status.set(
LINE  999 |             f"Listo · Incluidos: {included} · Excluidos: {excluded} · Omitidos: {omitted} · Líneas: {total_lines:,}"
LINE 1000 |         )
LINE 1001 | 
LINE 1002 |     # === AUTO-GENERATED: file_search_dependency_feature ===
LINE 1003 |     def on_open_file_search(self):
LINE 1004 |         folder = self.var_folder.get()
LINE 1005 |         if not folder or not os.path.isdir(folder):
LINE 1006 |             dialogs.show_warning("Atención", "Selecciona una carpeta del proyecto primero.")
LINE 1007 |             return
LINE 1008 | 
LINE 1009 |         excluded = self.selector.get_selection().excluded_dirs
LINE 1010 |         FileSearchDialog(
LINE 1011 |             self.root,
LINE 1012 |             folder,
LINE 1013 |             excluded_dirs=excluded,
LINE 1014 |             on_analyze_dependencies=self.open_dependency_tree,
LINE 1015 |         )
LINE 1016 | 
LINE 1017 |     def open_dependency_tree(self, rel_path: str):
LINE 1018 |         folder = self.var_folder.get()
LINE 1019 |         if not folder or not os.path.isdir(folder):
LINE 1020 |             dialogs.show_warning("Atención", "Selecciona una carpeta del proyecto primero.")
LINE 1021 |             return
LINE 1022 | 
LINE 1023 |         excluded = self.selector.get_selection().excluded_dirs
LINE 1024 |         DependencyTreeDialog(
LINE 1025 |             self.root,
LINE 1026 |             folder,
LINE 1027 |             rel_path,
LINE 1028 |             excluded_dirs=excluded,
LINE 1029 |             on_apply_selection=self.apply_dependency_selection,
LINE 1030 |         )
LINE 1031 | 
LINE 1032 |     def apply_dependency_selection(self, selected_files: List[str]):
LINE 1033 |         if not selected_files:
LINE 1034 |             return
LINE 1035 | 
LINE 1036 |         existing = set(self.tree.get_checked_files())
LINE 1037 |         combined = existing | set(selected_files)
LINE 1038 | 
LINE 1039 |         self.tree.set_checked_files(combined)
LINE 1040 |         self.selector.set_checked_folder_files(self.tree.get_checked_files())
LINE 1041 |         self._refresh_selection_stats()
LINE 1042 | 
LINE 1043 |         self.sv_status.set(
LINE 1044 |             f"✓ {len(selected_files)} dependencia(s) agregadas/actualizadas en la selección."
LINE 1045 |         )
LINE 1046 |     # === END AUTO-GENERATED ===
LINE 1047 | 
LINE 1048 |     def on_copy_clipboard(self):
LINE 1049 | 
LINE 1050 | 
LINE 1051 |         content = self.preview_text.get("1.0", tk.END).strip()
LINE 1052 |         if not content:
LINE 1053 |             dialogs.show_warning("Atención",
LINE 1054 |                                  "Genera el contexto primero (⚡ Generar contexto).")
LINE 1055 |             return
LINE 1056 |         if copy_to_clipboard(self.root, content):
LINE 1057 |             self.sv_status.set("Contenido copiado al portapapeles.")
LINE 1058 | 
LINE 1059 |     def on_export_file(self):
LINE 1060 |         content = self.preview_text.get("1.0", tk.END).strip()
LINE 1061 |         if not content:
LINE 1062 |             dialogs.show_warning("Atención",
LINE 1063 |                                  "Genera el contexto primero (⚡ Generar contexto).")
LINE 1064 |             return
LINE 1065 |         ext = ".md" if self.var_fmt.get() == "markdown" else ".txt"
LINE 1066 |         fp  = dialogs.ask_save_file("Guardar Documento", default_ext=ext)
LINE 1067 |         if fp:
LINE 1068 |             ok, msg = write_text_file(fp, content)
LINE 1069 |             if ok:
LINE 1070 |                 self.sv_status.set(f"Guardado: {os.path.basename(fp)}")
LINE 1071 |                 dialogs.show_info("Guardado", f"Archivo guardado en:\n{fp}")
LINE 1072 |             else:
LINE 1073 |                 dialogs.show_error("Error", f"No se pudo guardar: {msg}")
```

==============================================================
FILE: app/models/__init__.py
==============================================================
```py
LINE 1 | """Models package initialization."""
LINE 2 | from app.models.project import ProjectSelection, FileItem, ExportConfig
LINE 3 | 
LINE 4 | __all__ = ["ProjectSelection", "FileItem", "ExportConfig"]
```

==============================================================
FILE: app/models/analysis_modes.py
==============================================================
```py
LINE   1 | """
LINE   2 | Analysis Modes definitions and directives.
LINE   3 | Supports:
LINE   4 | - MODE_PROBLEM ("problem"): Displays problem description field, focuses AI strictly on diagnosing & resolving the specified problem (root cause, solution, code changes).
LINE   5 | - MODE_PROJECT ("project"): Hides problem field, performs a holistic project audit (errors, duplicate code, bad practices, architecture, security, performance) with prioritized findings & recommended actions.
LINE   6 | """
LINE   7 | from dataclasses import dataclass
LINE   8 | from typing import Dict
LINE   9 | 
LINE  10 | MODE_PROBLEM = "problem"
LINE  11 | MODE_PROJECT = "project"
LINE  12 | 
LINE  13 | 
LINE  14 | @dataclass
LINE  15 | class AnalysisModeConfig:
LINE  16 |     mode: str
LINE  17 |     display_name: str
LINE  18 |     icon: str
LINE  19 |     description: str
LINE  20 |     prompt_instructions: str
LINE  21 |     response_template: str
LINE  22 | 
LINE  23 | 
LINE  24 | ANALYSIS_MODES: Dict[str, AnalysisModeConfig] = {
LINE  25 |     MODE_PROBLEM: AnalysisModeConfig(
LINE  26 |         mode=MODE_PROBLEM,
LINE  27 |         display_name="Modo Problema (Problem Mode)",
LINE  28 |         icon="🔧",
LINE  29 |         description="Enfoca a la IA exclusivamente en diagnosticar y resolver el problema específico reportado por el desarrollador, priorizando la causa raíz y las soluciones quirúrgicas en código.",
LINE  30 |         prompt_instructions="""### 🎯 ENFOQUE DE MODO PROBLEMA (PROBLEM MODE)
LINE  31 | 1. **Foco exclusivo en el problema especificado**: Diagnostica y resuelve directamente la incidencia descrita en "REPORTED PROBLEM".
LINE  32 | 2. **Prioriza la Causa Raíz**: Identifica el origen exacto del fallo técnico antes de proponer cambios de código.
LINE  33 | 3. **Solución quirúrgica y escalable**: Genera el código corregido listo para sustituir sin alterar funcionalidades no relacionadas.
LINE  34 | 4. **Impacto y Efectos Secundarios**: Evalúa regresiones potenciales de la modificación realizada.""",
LINE  35 |         response_template="""# DIAGNOSIS
LINE  36 | ## Reported Problem Summary
LINE  37 | [Resumen del problema especificado]
LINE  38 | 
LINE  39 | ## Root Cause
LINE  40 | [Explicación técnica detallada de la causa raíz identificada]
LINE  41 | 
LINE  42 | # FILES TO MODIFY
LINE  43 | ## 1. [ruta/relativa/archivo.ext]
LINE  44 | Approximate line: [número de línea]
LINE  45 | 
LINE  46 | ### Problem in File
LINE  47 | [Descripción técnica de la falla en este archivo]
LINE  48 | 
LINE  49 | ### Solution & Justification
LINE  50 | [Explicación concisa del arreglo]
LINE  51 | 
LINE  52 | ### Current Code
LINE  53 | ```
LINE  54 | [bloque de código actual]
LINE  55 | ```
LINE  56 | 
LINE  57 | ### Corrected Code
LINE  58 | ```
LINE  59 | [bloque de código corregido listo para copiar/pegar]
LINE  60 | ```
LINE  61 | 
LINE  62 | # NEW FILES
LINE  63 | [Lista de nuevos archivos requeridos o: No se requieren nuevos archivos.]
LINE  64 | 
LINE  65 | # RISKS OR SIDE EFFECTS
LINE  66 | [Efectos secundarios potenciales o: Sin riesgos identificados.]
LINE  67 | 
LINE  68 | # IMPLEMENTATION PLAN
LINE  69 | 1. [Paso 1 para aplicar la solución]
LINE  70 | 2. [Paso 2]"""
LINE  71 |     ),
LINE  72 | 
LINE  73 |     MODE_PROJECT: AnalysisModeConfig(
LINE  74 |         mode=MODE_PROJECT,
LINE  75 |         display_name="Modo Proyecto (Project Mode)",
LINE  76 |         icon="🏗️",
LINE  77 |         description="Analiza el proyecto de forma holística: detecta errores latentes, código duplicado, malas prácticas, vulnerabilidades de seguridad, problemas arquitectónicos y oportunidades de optimización.",
LINE  78 |         prompt_instructions="""### 🎯 ENFOQUE DE MODO PROYECTO (HOLISTIC PROJECT MODE)
LINE  79 | 1. **Análisis Holístico Transversal**: Evalúa la totalidad del proyecto analizando:
LINE  80 |    - Errores sintácticos y de lógica latentes.
LINE  81 |    - Código duplicado y deuda técnica (DRY).
LINE  82 |    - Malas prácticas e ineficiencias de diseño.
LINE  83 |    - Problemas arquitectónicos y acoplamiento indebido.
LINE  84 |    - Vulnerabilidades de seguridad (OWASP).
LINE  85 |    - Oportunidades de optimización de rendimiento.
LINE  86 | 2. **Matriz de Hallazgos Priorizada**: Clasifica cada problema encontrado por categoría y nivel de severidad (Crítica, Alta, Media, Baja).
LINE  87 | 3. **Acciones Recomendadas**: Proporciona el código de remediación directo y una hoja de ruta ordenada por impacto.""",
LINE  88 |         response_template="""# HOLISTIC PROJECT AUDIT MATRIX
LINE  89 | | Categoría | Severidad | Hallazgo Técnico | Ubicación (Archivo:Línea) |
LINE  90 | |---|---|---|---|
LINE  91 | | Errores / Bugs | [Crítica/Alta/Media/Baja] | [Descripción del error] | [Ruta:Línea] |
LINE  92 | | Código Duplicado | [Crítica/Alta/Media/Baja] | [Fragmento duplicado o smell] | [Ruta:Línea] |
LINE  93 | | Malas Prácticas | [Crítica/Alta/Media/Baja] | [Violación de estándar/convención] | [Ruta:Línea] |
LINE  94 | | Arquitectura | [Crítica/Alta/Media/Baja] | [Acoplamiento / problema estructural] | [Ruta:Línea] |
LINE  95 | | Seguridad | [Crítica/Alta/Media/Baja] | [Vulnerabilidad o riesgo] | [Ruta:Línea] |
LINE  96 | | Rendimiento | [Crítica/Alta/Media/Baja] | [Iniciativa de optimización] | [Ruta:Línea] |
LINE  97 | 
LINE  98 | # PRIORITIZED REMEDIATION CODE
LINE  99 | ## 1. [Hallazgo de mayor severidad]
LINE 100 | File: [ruta/relativa/archivo.ext]
LINE 101 | Approximate line: [número]
LINE 102 | 
LINE 103 | ### Issue & Impact
LINE 104 | [Explicación técnica del problema y su riesgo]
LINE 105 | 
LINE 106 | ### Current Vulnerable/Inefficient Code
LINE 107 | ```
LINE 108 | [código actual]
LINE 109 | ```
LINE 110 | 
LINE 111 | ### Recommended Production Code
LINE 112 | ```
LINE 113 | [código corregido u optimizado]
LINE 114 | ```
LINE 115 | 
LINE 116 | # RECOMMENDED ACTION PLAN
LINE 117 | ## Fase 1 (Inmediato - Correcciones Críticas y de Seguridad)
LINE 118 | 1. [Acción 1]
LINE 119 | 2. [Acción 2]
LINE 120 | 
LINE 121 | ## Fase 2 (Corto Plazo - Refactorización y Limpieza de Duplicación)
LINE 122 | 1. [Acción 1]
LINE 123 | 
LINE 124 | ## Fase 3 (Mediano Plazo - Arquitectura y Rendimiento)
LINE 125 | 1. [Acción 1]"""
LINE 126 |     )
LINE 127 | }
LINE 128 | 
LINE 129 | 
LINE 130 | def get_analysis_mode_config(mode_key: str) -> AnalysisModeConfig:
LINE 131 |     """Returns the AnalysisModeConfig for the given mode key, defaulting to MODE_PROBLEM."""
LINE 132 |     k = mode_key.strip().lower() if mode_key else MODE_PROBLEM
LINE 133 |     if k in ANALYSIS_MODES:
LINE 134 |         return ANALYSIS_MODES[k]
LINE 135 |     return ANALYSIS_MODES[MODE_PROBLEM]
```

==============================================================
FILE: app/models/analysis_types.py
==============================================================
```py
LINE   1 | """
LINE   2 | Analysis Types and Profiles for DeepSeek prompt customization.
LINE   3 | Defines 10 specialized analysis profiles that dynamically shape the LLM prompt's:
LINE   4 | - Objective
LINE   5 | - Focus
LINE   6 | - Priorities
LINE   7 | - Expected Outcome
LINE   8 | - Structured Response Template
LINE   9 | """
LINE  10 | from dataclasses import dataclass
LINE  11 | from typing import Dict, List, Optional
LINE  12 | 
LINE  13 | 
LINE  14 | @dataclass
LINE  15 | class AnalysisProfile:
LINE  16 |     name: str
LINE  17 |     display_name: str
LINE  18 |     icon: str
LINE  19 |     objective: str
LINE  20 |     focus: str
LINE  21 |     priorities: str
LINE  22 |     expected_outcome: str
LINE  23 |     default_prompt_hint: str
LINE  24 |     response_instructions: str
LINE  25 |     response_template: str
LINE  26 | 
LINE  27 | 
LINE  28 | ANALYSIS_PROFILES: Dict[str, AnalysisProfile] = {
LINE  29 |     "Detect errors": AnalysisProfile(
LINE  30 |         name="Detect errors",
LINE  31 |         display_name="Detect errors (Detectar errores)",
LINE  32 |         icon="🐞",
LINE  33 |         objective="Identificar errores de sintaxis, bugs lógicos, excepciones no controladas, condiciones de carrera y fallos de tipo en el código.",
LINE  34 |         focus="Detección exhaustiva de bugs, casos límite (edge cases), seguridad de nulos/undefined, control de flujo y manejo robusto de excepciones.",
LINE  35 |         priorities="1. Crashes y errores que detienen la ejecución. 2. Fallos silenciosos y corrupción de estado. 3. Manejo deficiente de excepciones. 4. Regresiones potenciales.",
LINE  36 |         expected_outcome="Localización exacta de cada error (archivo y línea), causa raíz técnica, código corregido listo para copiar/pegar y caso de prueba de verificación.",
LINE  37 |         default_prompt_hint="Por favor audita y detecta todos los errores, excepciones no controladas, fallos lógicos o condiciones de carrera presentes en el código adjunto.",
LINE  38 |         response_instructions="El análisis debe ser CONCRETO, TÉCNICO y ORIENTADO A LA ACCIÓN. Concéntrate exclusivamente en fallos reproducibles y errores verificables. Omite comentarios estilísticos o divagaciones teóricas que no resuelvan un error.",
LINE  39 |         response_template="""# DIAGNOSIS
LINE  40 | ## Detected Bugs
LINE  41 | [Lista técnica de los bugs encontrados con su causa raíz exacta]
LINE  42 | 
LINE  43 | # FILES TO MODIFY
LINE  44 | ## 1. [ruta/relativa/archivo.ext]
LINE  45 | Approximate line: [número]
LINE  46 | ### Bug Description
LINE  47 | [Explicación concisa del error]
LINE  48 | ### Current Code
LINE  49 | ```
LINE  50 | [código con error]
LINE  51 | ```
LINE  52 | ### Bugfix Code
LINE  53 | ```
LINE  54 | [código corregido listo para sustituir]
LINE  55 | ```
LINE  56 | 
LINE  57 | # VERIFICATION & EDGE CASES
LINE  58 | [Prueba o caso límite para verificar que el bug fue resuelto]"""
LINE  59 |     ),
LINE  60 | 
LINE  61 |     "Solve problem": AnalysisProfile(
LINE  62 |         name="Solve problem",
LINE  63 |         display_name="Solve problem (Resolver problema)",
LINE  64 |         icon="🔧",
LINE  65 |         objective="Diagnosticar la causa raíz y resolver quirúrgicamente el problema específico reportado por el desarrollador.",
LINE  66 |         focus="Solución directa, eficaz y de mínimo impacto colateral para la incidencia descrita.",
LINE  67 |         priorities="1. Causa raíz del síntoma reportado. 2. Corrección quirúrgica y mantenible. 3. Preservación estricta de la funcionalidad adyacente.",
LINE  68 |         expected_outcome="Diagnóstico directo, archivos exactos a modificar con líneas aproximadas, código de sustitución listo y plan de implementación paso a paso.",
LINE  69 |         default_prompt_hint="Tengo el siguiente problema en el proyecto: [Describe aquí el error exacto, mensaje de excepción o comportamiento inesperado que deseas resolver].",
LINE  70 |         response_instructions="El análisis debe ser CONCRETO, TÉCNICO y ORIENTADO A LA ACCIÓN. Enfócate exclusivamente en resolver el problema reportado de raíz, sin desviarte a refactorizaciones no solicitadas.",
LINE  71 |         response_template="""# DIAGNOSIS
LINE  72 | ## Problem
LINE  73 | [Descripción técnica del problema reportado]
LINE  74 | ## Root Cause
LINE  75 | [Causa raíz exacta en el código]
LINE  76 | 
LINE  77 | # FILES TO MODIFY
LINE  78 | ## 1. [ruta/relativa/archivo.ext]
LINE  79 | Approximate line: [número]
LINE  80 | ### Problem
LINE  81 | [Problema en este archivo]
LINE  82 | ### Solution
LINE  83 | [Solución aplicada]
LINE  84 | ### Current Code
LINE  85 | ```
LINE  86 | [código actual]
LINE  87 | ```
LINE  88 | ### Corrected Code
LINE  89 | ```
LINE  90 | [código corregido]
LINE  91 | ```
LINE  92 | 
LINE  93 | # NEW FILES
LINE  94 | [Nuevos archivos requeridos o: No se requieren nuevos archivos.]
LINE  95 | 
LINE  96 | # RISKS OR SIDE EFFECTS
LINE  97 | [Riesgos identificados o: Sin riesgos identificados.]
LINE  98 | 
LINE  99 | # IMPLEMENTATION PLAN
LINE 100 | 1. [Paso 1]
LINE 101 | 2. [Paso 2]"""
LINE 102 |     ),
LINE 103 | 
LINE 104 |     "Refactoring": AnalysisProfile(
LINE 105 |         name="Refactoring",
LINE 106 |         display_name="Refactoring (Refactorización)",
LINE 107 |         icon="♻️",
LINE 108 |         objective="Simplificar, limpiar y estructurar el código existente para mejorar su legibilidad, mantenibilidad y reducir deuda técnica sin alterar su comportamiento externo.",
LINE 109 |         focus="Eliminación de duplicación (DRY), reducción de complejidad ciclomática, desacoplamiento, nombres expresivos y adopción de modismos limpios del lenguaje.",
LINE 110 |         priorities="1. Métodos y clases gigantes (God classes/functions). 2. Código duplicado. 3. Anidamiento excesivo. 4. Mejoras de legibilidad con contratos idénticos.",
LINE 111 |         expected_outcome="Comparativa de código antes/después con explicaciones de la mejora aplicada, asegurando compatibilidad 100% con el comportamiento existente.",
LINE 112 |         default_prompt_hint="Por favor revisa el código para refactorizarlo: simplificar lógica compleja, eliminar código duplicado, mejorar la legibilidad y aplicar buenas prácticas sin alterar la funcionalidad externa.",
LINE 113 |         response_instructions="El análisis debe ser CONCRETO, TÉCNICO y ORIENTADO A LA ACCIÓN. Concéntrate en transformaciones de código medibles que reduzcan la deuda técnica. No alteres la interfaz pública ni los contratos existentes.",
LINE 114 |         response_template="""# REFACTORING DIAGNOSIS
LINE 115 | ## Code Smells & Debt
LINE 116 | [Lista de puntos críticos de deuda técnica, duplicación o complejidad excesiva]
LINE 117 | 
LINE 118 | # REFACTORED FILES
LINE 119 | ## 1. [ruta/relativa/archivo.ext]
LINE 120 | Approximate line: [número]
LINE 121 | ### Target Smell
LINE 122 | [Smell o problema de diseño corregido]
LINE 123 | ### Before Refactor
LINE 124 | ```
LINE 125 | [código original complejo o duplicado]
LINE 126 | ```
LINE 127 | ### After Refactor
LINE 128 | ```
LINE 129 | [código refactorizado limpio y desacoplado]
LINE 130 | ```
LINE 131 | ### Improvements Achieved
LINE 132 | - Complejidad ciclomática reducida
LINE 133 | - Cohesión mejorada
LINE 134 | 
LINE 135 | # CONTRACT PRESERVATION CHECK
LINE 136 | [Confirmación de que los contratos y comportamientos existentes se mantienen intactos]"""
LINE 137 |     ),
LINE 138 | 
LINE 139 |     "Improve architecture": AnalysisProfile(
LINE 140 |         name="Improve architecture",
LINE 141 |         display_name="Improve architecture (Mejorar arquitectura)",
LINE 142 |         icon="🏛️",
LINE 143 |         objective="Evaluar y optimizar la estructura global del sistema, límites modulares, separación de responsabilidades y patrones de diseño para máxima escalabilidad.",
LINE 144 |         focus="Principios SOLID, Clean/Hexagonal Architecture, inyección de dependencias, límites de capas y organización coherente de módulos.",
LINE 145 |         priorities="1. Acoplamiento indebido entre capas. 2. Dependencias circulares. 3. Fuga de detalles de infraestructura al dominio. 4. Escalabilidad modular.",
LINE 146 |         expected_outcome="Diagnóstico de dependencias y límites, propuesta de redistribución de módulos/capas, interfaces desacopladas y plan de migración arquitectónica.",
LINE 147 |         default_prompt_hint="Por favor evalúa la arquitectura general del proyecto. Propón mejoras en la separación de capas, desacoplamiento de componentes, inyección de dependencias y organización estructural.",
LINE 148 |         response_instructions="El análisis debe ser CONCRETO, TÉCNICO y ORIENTADO A LA ACCIÓN. Enfócate en estructura, capas, límites modulares y contratos entre componentes. Evita filosofías abstractas sin soporte de código concreto.",
LINE 149 |         response_template="""# ARCHITECTURAL ASSESSMENT
LINE 150 | ## Current Bottlenecks & Violations
LINE 151 | [Análisis de acoplamientos indebidos, dependencias circulares o violación de capas]
LINE 152 | 
LINE 153 | ## Target Architecture
LINE 154 | [Diseño propuesto de capas, módulos y flujo de dependencias]
LINE 155 | 
LINE 156 | # STRUCTURAL & COMPONENT CHANGES
LINE 157 | ## 1. [Interfaces / Abstracciones clave]
LINE 158 | ```
LINE 159 | [código de interfaces o contratos desacoplados]
LINE 160 | ```
LINE 161 | 
LINE 162 | ## 2. [Modificaciones a módulos existentes]
LINE 163 | ### [ruta/relativa/archivo.ext]
LINE 164 | Approximate line: [número]
LINE 165 | ```
LINE 166 | [código reestructurado alineado a la nueva arquitectura]
LINE 167 | ```
LINE 168 | 
LINE 169 | # NEW FILES & DIRECTORY REORGANIZATION
LINE 170 | [Estructura de carpetas o nuevos archivos requeridos para la arquitectura]
LINE 171 | 
LINE 172 | # MIGRATION STRATEGY
LINE 173 | 1. [Paso 1 de migración gradual sin romper el sistema]
LINE 174 | 2. [Paso 2]"""
LINE 175 |     ),
LINE 176 | 
LINE 177 |     "Optimize performance": AnalysisProfile(
LINE 178 |         name="Optimize performance",
LINE 179 |         display_name="Optimize performance (Optimizar rendimiento)",
LINE 180 |         icon="⚡",
LINE 181 |         objective="Detectar cuellos de botella de latencia, uso ineficiente de memoria, operaciones bloqueantes y sobrecarga computacional en CPU e I/O.",
LINE 182 |         focus="Complejidad algorítmica (Big-O), alocaciones innecesarias, I/O bloqueante, consultas redundantes, sincronismo evitable y fugas de memoria.",
LINE 183 |         priorities="1. Bucles críticos y operaciones de alta frecuencia. 2. Operaciones I/O no asíncronas o no indexadas. 3. Reducción de huella de memoria. 4. Caching y computación perezosa.",
LINE 184 |         expected_outcome="Análisis de complejidad temporal/espacial, reemplazo quirúrgico de código ineficiente por alternativas de alto rendimiento y directrices de benchmarking.",
LINE 185 |         default_prompt_hint="Por favor analiza el rendimiento del código adjunto: detecta cuellos de botella de CPU, memoria, operaciones de entrada/salida o algoritmos lentos, y proporciona optimizaciones concretas de alto impacto.",
LINE 186 |         response_instructions="El análisis debe ser CONCRETO, TÉCNICO y ORIENTADO A LA ACCIÓN. Justifica cada optimización con impacto en complejidad temporal (Big-O) o uso de memoria. No sugieras micro-optimizaciones que sacrifiquen legibilidad sin beneficio real.",
LINE 187 |         response_template="""# PERFORMANCE BOTTLENECKS
LINE 188 | ## Identified Hotspots
LINE 189 | [Lista técnica de cuellos de botella identificados con su impacto estimado]
LINE 190 | 
LINE 191 | # CODE OPTIMIZATIONS
LINE 192 | ## 1. [ruta/relativa/archivo.ext]
LINE 193 | Approximate line: [número]
LINE 194 | ### Bottleneck
LINE 195 | [Operación costosa: complejidad actual O(...), consumo de memoria, bloqueo I/O]
LINE 196 | ### Current Inefficient Code
LINE 197 | ```
LINE 198 | [código lento actual]
LINE 199 | ```
LINE 200 | ### High-Performance Optimized Code
LINE 201 | ```
LINE 202 | [código optimizado de alto rendimiento: O(...)]
LINE 203 | ```
LINE 204 | ### Benchmark & Impact
LINE 205 | - Complejidad antes vs después
LINE 206 | - Reducción esperada en latencia o consumo
LINE 207 | 
LINE 208 | # CACHING & CONCURRENCY RECOMMENDATIONS
LINE 209 | [Estrategias de paralelismo, concurrencia o cache si aplican]"""
LINE 210 |     ),
LINE 211 | 
LINE 212 |     "Review security": AnalysisProfile(
LINE 213 |         name="Review security",
LINE 214 |         display_name="Review security (Revisión de seguridad)",
LINE 215 |         icon="🛡️",
LINE 216 |         objective="Auditar el código en busca de vulnerabilidades de seguridad, vectores de explotación, fugas de datos y violaciones a estándares OWASP.",
LINE 217 |         focus="Inyecciones (SQLi, XSS, Command Injection), autenticación, autorización, validación de inputs, deserialización insegura y exposición de secretos.",
LINE 218 |         priorities="1. Vulnerabilidades críticas explotables remotamente. 2. Exposición de credenciales/tokens. 3. Falla en control de accesos. 4. Endurecimiento de configuraciones.",
LINE 219 |         expected_outcome="Matriz de vulnerabilidades con severidad (Crítica/Alta/Media/Baja), vector de ataque, parche de mitigación en código y recomendaciones preventivas.",
LINE 220 |         default_prompt_hint="Por favor realiza una auditoría de seguridad exhaustiva en el código: detecta vulnerabilidades OWASP, fallos de inyección, autenticación, autorización, manejo de datos sensibles y provee los parches de seguridad correspondientes.",
LINE 221 |         response_instructions="El análisis debe ser CONCRETO, TÉCNICO y ORIENTADO A LA ACCIÓN. Describe con precisión el vector de ataque y provee el parche exacto para neutralizar la vulnerabilidad de inmediato.",
LINE 222 |         response_template="""# SECURITY AUDIT
LINE 223 | ## Vulnerability Summary
LINE 224 | | Vulnerabilidad | Severidad | Vector de Ataque | Archivo |
LINE 225 | |---|---|---|---|
LINE 226 | | [Nombre] | [Crítica/Alta/Media/Baja] | [Vector] | [Ruta] |
LINE 227 | 
LINE 228 | # VULNERABILITY REMEDIATION
LINE 229 | ## 1. [Nombre de la vulnerabilidad]
LINE 230 | Severity: [Crítica / Alta / Media / Baja]
LINE 231 | File: [ruta/relativa/archivo.ext]
LINE 232 | Approximate line: [número]
LINE 233 | 
LINE 234 | ### Attack Vector & Risk
LINE 235 | [Cómo puede explotarse y qué impacto tiene]
LINE 236 | 
LINE 237 | ### Vulnerable Code
LINE 238 | ```
LINE 239 | [código vulnerable actual]
LINE 240 | ```
LINE 241 | 
LINE 242 | ### Secured Remediation Patch
LINE 243 | ```
LINE 244 | [código seguro con validación, escape o mitigación aplicada]
LINE 245 | ```
LINE 246 | 
LINE 247 | # HARDENING & SECURE BEST PRACTICES
LINE 248 | [Medidas preventivas complementarias en configuración o dependencias]"""
LINE 249 |     ),
LINE 250 | 
LINE 251 |     "Create new functionality": AnalysisProfile(
LINE 252 |         name="Create new functionality",
LINE 253 |         display_name="Create new functionality (Crear nueva funcionalidad)",
LINE 254 |         icon="✨",
LINE 255 |         objective="Diseñar e implementar una nueva funcionalidad o módulo respetando la arquitectura, patrones y convenciones del proyecto existente.",
LINE 256 |         focus="Diseño no invasivo, interfaces claras, flujo de datos coherente, extensión limpia de modelos y servicios existentes sin romper compatibilidad.",
LINE 257 |         priorities="1. Integración natural con la base de código actual. 2. Completitud funcional del requerimiento. 3. Cero regresiones en código existente.",
LINE 258 |         expected_outcome="Especificación técnica de la funcionalidad, código completo listo para producción de los nuevos archivos y modificaciones precisas a los existentes.",
LINE 259 |         default_prompt_hint="Deseo agregar la siguiente nueva funcionalidad al proyecto: [Describe detalladamente la característica que deseas construir, entradas esperadas y resultado requerido].",
LINE 260 |         response_instructions="El análisis debe ser CONCRETO, TÉCNICO y ORIENTADO A LA ACCIÓN. Proporciona código funcional completo para producción, no pseudo-código ni fragmentos incompletos con '// resto del código'.",
LINE 261 |         response_template="""# FEATURE SPECIFICATION
LINE 262 | ## Requirements & Scope
LINE 263 | [Descripción técnica de la nueva funcionalidad]
LINE 264 | 
LINE 265 | ## Architecture Integration
LINE 266 | [Cómo se conecta con los modelos, servicios y controladores existentes]
LINE 267 | 
LINE 268 | # NEW FILES TO CREATE
LINE 269 | ## 1. [ruta/relativa/nuevo_archivo.ext]
LINE 270 | Purpose: [Propósito del archivo]
LINE 271 | ```
LINE 272 | [código fuente completo listo para producción]
LINE 273 | ```
LINE 274 | 
LINE 275 | # MODIFICATIONS TO EXISTING FILES
LINE 276 | ## 1. [ruta/relativa/archivo_existente.ext]
LINE 277 | Approximate line: [número]
LINE 278 | ### Integration Point
LINE 279 | [Punto exacto de integración]
LINE 280 | ### Modified Code
LINE 281 | ```
LINE 282 | [código modificado con la integración de la nueva característica]
LINE 283 | ```
LINE 284 | 
LINE 285 | # USAGE EXAMPLE & TESTING
LINE 286 | ```
LINE 287 | [ejemplo concreto de invocación o prueba de la nueva funcionalidad]
LINE 288 | ```"""
LINE 289 |     ),
LINE 290 | 
LINE 291 |     "Explain project": AnalysisProfile(
LINE 292 |         name="Explain project",
LINE 293 |         display_name="Explain project (Explicar proyecto)",
LINE 294 |         icon="📖",
LINE 295 |         objective="Proporcionar una explicación técnica integral, rigurosa y pedagógica del funcionamiento, flujo de datos y arquitectura del proyecto.",
LINE 296 |         focus="Ciclo de vida de la ejecución, responsabilidades de cada módulo/capa, flujo de información de entrada a salida y abstracciones clave.",
LINE 297 |         priorities="1. Flujo de ejecución principal desde los entry points. 2. Rol y responsabilidad de cada componente. 3. Manejo de estado y persistencia.",
LINE 298 |         expected_outcome="Explicación técnica estructurada, diagrama o descripción del flujo de datos, desglose de componentes clave y guía para nuevos desarrolladores.",
LINE 299 |         default_prompt_hint="Por favor explica en profundidad este proyecto: su propósito principal, arquitectura general, flujo de datos desde los puntos de entrada y el rol de cada módulo clave.",
LINE 300 |         response_instructions="El análisis debe ser CONCRETO, TÉCNICO y ORIENTADO A LA ACCIÓN. Concéntrate en la realidad técnica del código adjunto sin inventar suposiciones. No propongas código de refactorización innecesario.",
LINE 301 |         response_template="""# PROJECT OVERVIEW
LINE 302 | ## Core Purpose & Tech Stack
LINE 303 | [Qué hace el proyecto, tecnologías clave y problema que resuelve]
LINE 304 | 
LINE 305 | # ARCHITECTURE & DESIGN
LINE 306 | ## Structural Breakdown
LINE 307 | [Organización de carpetas, capas y módulos principales con sus responsabilidades]
LINE 308 | 
LINE 309 | ## Key Abstractions
LINE 310 | [Clases, servicios o componentes centrales y cómo interactúan]
LINE 311 | 
LINE 312 | # EXECUTION FLOW & DATA PIPELINE
LINE 313 | 1. [Punto de entrada: inicio del ciclo de vida]
LINE 314 | 2. [Paso intermedio: procesamiento o lógica de negocio]
LINE 315 | 3. [Salida: respuesta, persistencia o interfaz gráfica]
LINE 316 | 
LINE 317 | # KEY EXTENSION POINTS
LINE 318 | [Dónde y cómo debe un desarrollador extender el proyecto si desea añadir funciones]"""
LINE 319 |     ),
LINE 320 | 
LINE 321 |     "Document project": AnalysisProfile(
LINE 322 |         name="Document project",
LINE 323 |         display_name="Document project (Documentar proyecto)",
LINE 324 |         icon="📝",
LINE 325 |         objective="Generar documentación técnica profesional, estandarizada y completa para APIs, módulos, docstrings y guía de uso del proyecto.",
LINE 326 |         focus="Firmas de funciones/métodos, tipos de entrada/salida, descripciones de parámetros, excepciones arrojadas, ejemplos de uso y README técnico.",
LINE 327 |         priorities="1. Interfaces públicas no documentadas. 2. Servicios de negocio críticos. 3. Endpoints o contratos de API. 4. Guía de instalación y ejecución.",
LINE 328 |         expected_outcome="Docstrings estándar (Google/Sphinx/JSDoc/PHPDoc) listos para integrar, documentación de API en Markdown y guía técnica para el repositorio.",
LINE 329 |         default_prompt_hint="Por favor genera documentación técnica completa para el proyecto: docstrings profesionales para funciones/clases clave, especificaciones de tipos, ejemplos de uso y una guía técnica estructurada.",
LINE 330 |         response_instructions="El análisis debe ser CONCRETO, TÉCNICO y ORIENTADO A LA ACCIÓN. Genera documentación directamente utilizable con ejemplos de código ejecutables y especificaciones de tipos rigurosas.",
LINE 331 |         response_template="""# PROJECT DOCUMENTATION
LINE 332 | ## Executive Technical Summary
LINE 333 | [Resumen conciso del sistema para desarrolladores]
LINE 334 | 
LINE 335 | # API & COMPONENT REFERENCE
LINE 336 | ## 1. [Componente / Servicio / Módulo]
LINE 337 | File: [ruta/relativa/archivo.ext]
LINE 338 | 
LINE 339 | ### Methods & Functions
LINE 340 | #### `nombreFuncion(param1: Tipo, param2: Tipo) -> Retorno`
LINE 341 | - **Descripción**: [Propósito claro]
LINE 342 | - **Parámetros**:
LINE 343 |   - `param1`: [descripción y restricciones]
LINE 344 |   - `param2`: [descripción]
LINE 345 | - **Retorno**: [tipo y significado]
LINE 346 | - **Excepciones**: [errores potenciales]
LINE 347 | - **Ejemplo**:
LINE 348 | ```
LINE 349 | [código de ejemplo de llamada]
LINE 350 | ```
LINE 351 | 
LINE 352 | # READY-TO-PASTE DOCSTRINGS
LINE 353 | ## [ruta/relativa/archivo.ext]
LINE 354 | ```
LINE 355 | [bloque con los docstrings listos para insertar en el archivo]
LINE 356 | ```
LINE 357 | 
LINE 358 | # ENVIRONMENT & SETUP GUIDE
LINE 359 | [Variables requeridas, comandos de instalación y pasos de despliegue]"""
LINE 360 |     ),
LINE 361 | 
LINE 362 |     "Comprehensive review": AnalysisProfile(
LINE 363 |         name="Comprehensive review",
LINE 364 |         display_name="Comprehensive review (Revisión integral)",
LINE 365 |         icon="🔍",
LINE 366 |         objective="Realizar una auditoría técnica 360° que evalúe errores, vulnerabilidades de seguridad, calidad arquitectónica, rendimiento y mantenibilidad.",
LINE 367 |         focus="Balance global de la salud de ingeniería de software del proyecto, identificando desde bugs inmediatos hasta mejoras estructurales estratégicas.",
LINE 368 |         priorities="1. Errores críticos y vulnerabilidades de seguridad. 2. Cuellos de botella graves de rendimiento. 3. Puntos neurálgicos de refactorización. 4. Plan de acción por fases.",
LINE 369 |         expected_outcome="Matriz holística de hallazgos categorizados por impacto/urgencia, correcciones quirúrgicas inmediatas y hoja de ruta de mejoras recomendadas.",
LINE 370 |         default_prompt_hint="Por favor realiza una revisión integral 360° del proyecto: analiza errores, seguridad, arquitectura, rendimiento y calidad de código, entregando una matriz de hallazgos priorizados y correcciones listas para aplicar.",
LINE 371 |         response_instructions="El análisis debe ser CONCRETO, TÉCNICO y ORIENTADO A LA ACCIÓN. Prioriza los hallazgos por severidad y provee soluciones específicas con código listo para producción.",
LINE 372 |         response_template="""# COMPREHENSIVE 360° AUDIT MATRIX
LINE 373 | | Categoría | Severidad | Hallazgo Técnico | Archivo Afectado |
LINE 374 | |---|---|---|---|
LINE 375 | | Bugs | Alta/Med/Baja | [Descripción] | [Ruta] |
LINE 376 | | Seguridad | Alta/Med/Baja | [Descripción] | [Ruta] |
LINE 377 | | Rendimiento | Alta/Med/Baja | [Descripción] | [Ruta] |
LINE 378 | | Arquitectura | Alta/Med/Baja | [Descripción] | [Ruta] |
LINE 379 | 
LINE 380 | # CRITICAL & HIGH PRIORITY FIXES
LINE 381 | ## 1. [Nombre del hallazgo prioritario]
LINE 382 | File: [ruta/relativa/archivo.ext]
LINE 383 | Approximate line: [número]
LINE 384 | ### Current Code
LINE 385 | ```
LINE 386 | [código problemático]
LINE 387 | ```
LINE 388 | ### Corrected Production Code
LINE 389 | ```
LINE 390 | [código corregido y seguro]
LINE 391 | ```
LINE 392 | 
LINE 393 | # ARCHITECTURAL & QUALITY ENHANCEMENTS
LINE 394 | [Recomendaciones estructurales clave y desacoplamiento]
LINE 395 | 
LINE 396 | # ACTIONABLE ROADMAP
LINE 397 | - **Fase 1 (Inmediato)**: Parchear bugs críticos y seguridad.
LINE 398 | - **Fase 2 (Corto plazo)**: Optimizar cuellos de botella y refactorizar componentes acoplados.
LINE 399 | - **Fase 3 (Mediano plazo)**: Fortalecer pruebas y documentación."""
LINE 400 |     )
LINE 401 | }
LINE 402 | 
LINE 403 | # Ordered list of keys matching user request exactly
LINE 404 | ANALYSIS_TYPE_KEYS: List[str] = [
LINE 405 |     "Detect errors",
LINE 406 |     "Solve problem",
LINE 407 |     "Refactoring",
LINE 408 |     "Improve architecture",
LINE 409 |     "Optimize performance",
LINE 410 |     "Review security",
LINE 411 |     "Create new functionality",
LINE 412 |     "Explain project",
LINE 413 |     "Document project",
LINE 414 |     "Comprehensive review",
LINE 415 | ]
LINE 416 | 
LINE 417 | 
LINE 418 | def get_analysis_profile(key: str) -> AnalysisProfile:
LINE 419 |     """Returns the AnalysisProfile for a given key, falling back to 'Detect errors'."""
LINE 420 |     if key in ANALYSIS_PROFILES:
LINE 421 |         return ANALYSIS_PROFILES[key]
LINE 422 |     # Check case-insensitive match
LINE 423 |     k_lower = key.strip().lower()
LINE 424 |     for k, profile in ANALYSIS_PROFILES.items():
LINE 425 |         if k.lower() == k_lower or profile.display_name.lower() == k_lower:
LINE 426 |             return profile
LINE 427 |     return ANALYSIS_PROFILES["Detect errors"]
LINE 428 | 
LINE 429 | 
LINE 430 | def get_all_analysis_types() -> List[str]:
LINE 431 |     """Returns list of canonical analysis type names."""
LINE 432 |     return list(ANALYSIS_TYPE_KEYS)
```

==============================================================
FILE: app/models/project.py
==============================================================
```py
LINE  1 | """Data models for project selection, files, and export configuration."""
LINE  2 | from dataclasses import dataclass, field
LINE  3 | from typing import Set, List, Optional
LINE  4 | import os
LINE  5 | 
LINE  6 | DEFAULT_ALLOWED_EXTENSIONS = {
LINE  7 |     ".py", ".js", ".jsx", ".ts", ".tsx", ".vue", ".php", ".html", ".htm",
LINE  8 |     ".css", ".scss", ".sass", ".less", ".json", ".sql", ".md", ".txt",
LINE  9 |     ".java", ".cpp", ".c", ".h", ".hpp", ".cs", ".go", ".rs", ".rb",
LINE 10 |     ".sh", ".bat", ".cmd", ".ps1", ".yaml", ".yml", ".xml", ".ini", ".env", ".config"
LINE 11 | }
LINE 12 | 
LINE 13 | 
LINE 14 | @dataclass
LINE 15 | class FileItem:
LINE 16 |     """Represents an individual file item in the selection."""
LINE 17 |     path: str
LINE 18 |     rel_path: str = ""
LINE 19 |     is_checked: bool = True
LINE 20 |     is_individual: bool = False
LINE 21 |     size: int = 0
LINE 22 | 
LINE 23 |     def __post_init__(self):
LINE 24 |         if not self.rel_path:
LINE 25 |             self.rel_path = os.path.basename(self.path)
LINE 26 | 
LINE 27 | 
LINE 28 | @dataclass
LINE 29 | class ProjectSelection:
LINE 30 |     """Stores current selection state: 1 folder + N individual files."""
LINE 31 |     folder_path: Optional[str] = None
LINE 32 |     checked_folder_files: Set[str] = field(default_factory=set)
LINE 33 |     individual_files: List[str] = field(default_factory=list)
LINE 34 |     excluded_dirs: Set[str] = field(
LINE 35 |         default_factory=lambda: {
LINE 36 |             ".git", "node_modules", "__pycache__", "venv", ".venv", 
LINE 37 |             "dist", "build", ".idea", ".vscode", "vendor", ".quasar", ".github", "public"
LINE 38 |         }
LINE 39 |     )
LINE 40 |     allowed_extensions: Set[str] = field(default_factory=lambda: set(DEFAULT_ALLOWED_EXTENSIONS))
LINE 41 |     filter_by_extension: bool = True
LINE 42 | 
LINE 43 |     def set_folder(self, folder_path: str) -> None:
LINE 44 |         """Sets single project folder (replaces any previous folder)."""
LINE 45 |         self.folder_path = folder_path
LINE 46 |         self.checked_folder_files.clear()
LINE 47 | 
LINE 48 |     def remove_folder(self) -> None:
LINE 49 |         """Clears single project folder."""
LINE 50 |         self.folder_path = None
LINE 51 |         self.checked_folder_files.clear()
LINE 52 | 
LINE 53 |     def add_individual_files(self, paths: List[str]) -> int:
LINE 54 |         """Adds unique individual file paths."""
LINE 55 |         added = 0
LINE 56 |         for p in paths:
LINE 57 |             abs_p = os.path.abspath(p)
LINE 58 |             if abs_p not in self.individual_files:
LINE 59 |                 self.individual_files.append(abs_p)
LINE 60 |                 added += 1
LINE 61 |         return added
LINE 62 | 
LINE 63 |     def remove_individual_file(self, path: str) -> None:
LINE 64 |         """Removes a file from individual files list."""
LINE 65 |         if path in self.individual_files:
LINE 66 |             self.individual_files.remove(path)
LINE 67 | 
LINE 68 |     def clear_individual_files(self) -> None:
LINE 69 |         """Clears all individual files."""
LINE 70 |         self.individual_files.clear()
LINE 71 | 
LINE 72 |     def is_file_extension_allowed(self, filename: str) -> bool:
LINE 73 |         """Checks if file extension is allowed."""
LINE 74 |         if not self.filter_by_extension or not self.allowed_extensions:
LINE 75 |             return True
LINE 76 |         ext = os.path.splitext(filename)[1].lower()
LINE 77 |         return ext in self.allowed_extensions
LINE 78 | 
LINE 79 | 
LINE 80 | @dataclass
LINE 81 | class ExportConfig:
LINE 82 |     """Export and formatting configurations with size & file limits."""
LINE 83 |     add_line_numbers: bool = True
LINE 84 |     include_tree: bool = True
LINE 85 |     include_system_instructions: bool = True
LINE 86 |     max_file_size_mb: float = 2.0
LINE 87 |     max_total_size_mb: float = 50.0
LINE 88 |     max_files: int = 100
LINE 89 |     output_format: str = "markdown"  # "markdown" or "text"
LINE 90 |     max_chars_per_file: int = 60000
LINE 91 |     analysis_type: str = "Detect errors"
LINE 92 |     analysis_mode: str = "problem"  # "problem" or "project"
LINE 93 | 
```

==============================================================
FILE: app/utils/__init__.py
==============================================================
```py
LINE 1 | """Utils package initialization."""
LINE 2 | from app.utils.path_utils import normalize_path, get_relative_path
LINE 3 | from app.utils.file_utils import safe_read_file, copy_to_clipboard, write_text_file, format_bytes
LINE 4 | 
LINE 5 | __all__ = ["normalize_path", "get_relative_path", "safe_read_file", "copy_to_clipboard", "write_text_file", "format_bytes"]
```

==============================================================
FILE: app/utils/file_utils.py
==============================================================
```py
LINE   1 | """File system I/O operations, binary detection, and memory-safe reading."""
LINE   2 | import os
LINE   3 | import tkinter as tk
LINE   4 | from typing import Tuple
LINE   5 | 
LINE   6 | # Common non-code / binary / media extensions
LINE   7 | KNOWN_BINARY_EXTENSIONS = {
LINE   8 |     # Images
LINE   9 |     ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".ico", ".svg", ".webp", ".tiff", ".psd",
LINE  10 |     # Videos & Audio
LINE  11 |     ".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm", ".mp3", ".wav", ".ogg", ".flac",
LINE  12 |     # Executables & Compiled Binaries
LINE  13 |     ".exe", ".dll", ".so", ".dylib", ".bin", ".dat", ".o", ".a", ".pyc", ".pyo", ".class", ".sys",
LINE  14 |     # Archives & Compressed
LINE  15 |     ".zip", ".tar", ".gz", ".7z", ".rar", ".bz2", ".xz", ".iso", ".jar",
LINE  16 |     # Documents / Databases
LINE  17 |     ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".db", ".sqlite", ".sqlite3"
LINE  18 | }
LINE  19 | 
LINE  20 | 
LINE  21 | def is_binary_file(path: str) -> bool:
LINE  22 |     """
LINE  23 |     Checks if a file is binary by extension and by inspecting the first 1024 bytes
LINE  24 |     for null characters or non-text control bytes.
LINE  25 |     """
LINE  26 |     ext = os.path.splitext(path)[1].lower()
LINE  27 |     if ext in KNOWN_BINARY_EXTENSIONS:
LINE  28 |         return True
LINE  29 | 
LINE  30 |     try:
LINE  31 |         with open(path, 'rb') as f:
LINE  32 |             chunk = f.read(1024)
LINE  33 |             if b'\x00' in chunk:
LINE  34 |                 return True
LINE  35 |             # High proportion of non-printable bytes indicates binary
LINE  36 |             if chunk:
LINE  37 |                 non_text = sum(1 for byte in chunk if byte < 9 or (13 < byte < 32) or byte == 127)
LINE  38 |                 if non_text / len(chunk) > 0.3:
LINE  39 |                     return True
LINE  40 |     except Exception:
LINE  41 |         pass
LINE  42 |     return False
LINE  43 | 
LINE  44 | 
LINE  45 | def get_file_size(path: str) -> int:
LINE  46 |     """Returns size of file in bytes."""
LINE  47 |     try:
LINE  48 |         return os.path.getsize(path)
LINE  49 |     except Exception:
LINE  50 |         return 0
LINE  51 | 
LINE  52 | 
LINE  53 | def safe_read_file(path: str, max_bytes: int = 1_048_576) -> str:
LINE  54 |     """
LINE  55 |     Reads file content safely using common encodings.
LINE  56 |     Truncates content if size exceeds max_bytes to protect memory usage.
LINE  57 |     """
LINE  58 |     if is_binary_file(path):
LINE  59 |         return f"[OMITIDO: Archivo binario no textual - {os.path.basename(path)}]"
LINE  60 | 
LINE  61 |     file_size = get_file_size(path)
LINE  62 |     is_truncated = False
LINE  63 |     
LINE  64 |     if file_size > max_bytes:
LINE  65 |         is_truncated = True
LINE  66 | 
LINE  67 |     encodings = ['utf-8', 'utf-8-sig', 'latin-1', 'cp1252']
LINE  68 |     content = None
LINE  69 | 
LINE  70 |     for enc in encodings:
LINE  71 |         try:
LINE  72 |             with open(path, 'r', encoding=enc) as f:
LINE  73 |                 if is_truncated:
LINE  74 |                     content = f.read(max_bytes)
LINE  75 |                 else:
LINE  76 |                     content = f.read()
LINE  77 |                 break
LINE  78 |         except (UnicodeDecodeError, Exception):
LINE  79 |             continue
LINE  80 | 
LINE  81 |     if content is None:
LINE  82 |         try:
LINE  83 |             with open(path, 'r', encoding='utf-8', errors='ignore') as f:
LINE  84 |                 content = f.read(max_bytes) if is_truncated else f.read()
LINE  85 |         except Exception as e:
LINE  86 |             return f"[Error critico al leer archivo: {e}]"
LINE  87 | 
LINE  88 |     if is_truncated:
LINE  89 |         size_mb = file_size / (1024 * 1024)
LINE  90 |         limit_mb = max_bytes / (1024 * 1024)
LINE  91 |         content += f"\n\n... [CONTENIDO TRUNCADO: El archivo supera el límite de {limit_mb:.1f} MB (Tamaño real: {size_mb:.2f} MB)] ..."
LINE  92 | 
LINE  93 |     return content
LINE  94 | 
LINE  95 | 
LINE  96 | def write_text_file(path: str, content: str) -> Tuple[bool, str]:
LINE  97 |     """Writes text content to file safely with UTF-8 encoding."""
LINE  98 |     try:
LINE  99 |         os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
LINE 100 |         with open(path, 'w', encoding='utf-8') as f:
LINE 101 |             f.write(content)
LINE 102 |         return True, "Guardado exitosamente."
LINE 103 |     except Exception as e:
LINE 104 |         return False, str(e)
LINE 105 | 
LINE 106 | 
LINE 107 | def copy_to_clipboard(root: tk.Tk, text: str) -> bool:
LINE 108 |     """Copies text string to system clipboard using Tkinter."""
LINE 109 |     try:
LINE 110 |         root.clipboard_clear()
LINE 111 |         root.clipboard_append(text)
LINE 112 |         root.update()
LINE 113 |         return True
LINE 114 |     except Exception:
LINE 115 |         return False
LINE 116 | 
LINE 117 | 
LINE 118 | def format_bytes(size_bytes: int) -> str:
LINE 119 |     """Formats raw bytes into human readable string (KB, MB)."""
LINE 120 |     if size_bytes < 1024:
LINE 121 |         return f"{size_bytes} B"
LINE 122 |     elif size_bytes < 1024 * 1024:
LINE 123 |         return f"{size_bytes / 1024:.1f} KB"
LINE 124 |     else:
LINE 125 |         return f"{size_bytes / (1024 * 1024):.2f} MB"
```

==============================================================
FILE: app/utils/path_utils.py
==============================================================
```py
LINE  1 | """Path resolution and string formatting utilities."""
LINE  2 | import os
LINE  3 | 
LINE  4 | 
LINE  5 | def normalize_path(path: str) -> str:
LINE  6 |     """Normalizes path for cross-platform consistency."""
LINE  7 |     if not path:
LINE  8 |         return ""
LINE  9 |     return os.path.abspath(os.path.normpath(path))
LINE 10 | 
LINE 11 | 
LINE 12 | def get_relative_path(path: str, start_dir: str) -> str:
LINE 13 |     """Returns path relative to start_dir if possible, otherwise absolute path."""
LINE 14 |     try:
LINE 15 |         norm_path = normalize_path(path)
LINE 16 |         norm_start = normalize_path(start_dir)
LINE 17 |         if norm_path.startswith(norm_start):
LINE 18 |             return os.path.relpath(norm_path, norm_start)
LINE 19 |     except Exception:
LINE 20 |         pass
LINE 21 |     return os.path.basename(path)
```

==============================================================
FILE: apply_changes.py
==============================================================
```py
LINE    1 | #!/usr/bin/env python3
LINE    2 | # -*- coding: utf-8 -*-
LINE    3 | """
LINE    4 | apply_changes.py
LINE    5 | Script para aplicar automáticamente todos los cambios del buscador de archivos
LINE    6 | y árbol de dependencias al proyecto "agente".
LINE    7 | 
LINE    8 | Uso:
LINE    9 |     python apply_changes.py                     # Aplica sobre el directorio actual
LINE   10 |     python apply_changes.py --root /ruta/proyecto
LINE   11 |     python apply_changes.py --dry-run           # Solo muestra qué haría
LINE   12 |     python apply_changes.py --no-backup         # No crea respaldos
LINE   13 | 
LINE   14 | El script es idempotente: puede ejecutarse varias veces sin dañar el proyecto.
LINE   15 | """
LINE   16 | 
LINE   17 | import argparse
LINE   18 | import os
LINE   19 | import shutil
LINE   20 | import sys
LINE   21 | from datetime import datetime
LINE   22 | from pathlib import Path
LINE   23 | 
LINE   24 | 
LINE   25 | # ---------------------------------------------------------------------------
LINE   26 | # Utilidades
LINE   27 | # ---------------------------------------------------------------------------
LINE   28 | 
LINE   29 | BACKUP_DIRNAME = ".backup_apply_changes"
LINE   30 | MARKER_NEW_FILES = "# === AUTO-GENERATED: file_search_dependency_feature ==="
LINE   31 | 
LINE   32 | 
LINE   33 | def log(msg, level="INFO"):
LINE   34 |     prefix = {
LINE   35 |         "INFO": "[INFO]",
LINE   36 |         "OK":   "[  OK ]",
LINE   37 |         "WARN": "[WARN]",
LINE   38 |         "ERR":  "[FAIL]",
LINE   39 |         "SKIP": "[SKIP]",
LINE   40 |     }.get(level, "[INFO]")
LINE   41 |     print(f"{prefix} {msg}")
LINE   42 | 
LINE   43 | 
LINE   44 | def ensure_dir(path: Path):
LINE   45 |     path.mkdir(parents=True, exist_ok=True)
LINE   46 | 
LINE   47 | 
LINE   48 | def backup_file(path: Path, backup_root: Path, dry_run: bool = False):
LINE   49 |     if not path.is_file():
LINE   50 |         return
LINE   51 |     rel = path.name
LINE   52 |     ts = datetime.now().strftime("%Y%m%d_%H%M%S")
LINE   53 |     dst = backup_root / f"{rel}.{ts}.bak"
LINE   54 |     if dry_run:
LINE   55 |         log(f"(dry-run) respaldaría {path} -> {dst}", "SKIP")
LINE   56 |         return
LINE   57 |     ensure_dir(backup_root)
LINE   58 |     shutil.copy2(path, dst)
LINE   59 |     log(f"Respaldo creado: {dst}", "OK")
LINE   60 | 
LINE   61 | 
LINE   62 | def write_file(path: Path, content: str, dry_run: bool = False, force: bool = False):
LINE   63 |     """Escribe un archivo. Si existe y no es force, avisa y omite."""
LINE   64 |     if path.exists() and not force:
LINE   65 |         log(f"Ya existe (no se sobreescribe): {path}", "SKIP")
LINE   66 |         return False
LINE   67 |     if dry_run:
LINE   68 |         log(f"(dry-run) escribiría {path} ({len(content)} bytes)", "SKIP")
LINE   69 |         return True
LINE   70 |     ensure_dir(path.parent)
LINE   71 |     with open(path, "w", encoding="utf-8") as f:
LINE   72 |         f.write(content)
LINE   73 |     log(f"Archivo escrito: {path}", "OK")
LINE   74 |     return True
LINE   75 | 
LINE   76 | 
LINE   77 | def append_block_if_missing(path: Path, marker: str, block: str,
LINE   78 |                             dry_run: bool = False, position: str = "end",
LINE   79 |                             anchor: str = None):
LINE   80 |     """
LINE   81 |     Agrega un bloque al archivo solo si el marcador no está presente.
LINE   82 |     position = 'end' | 'after_anchor'
LINE   83 |     """
LINE   84 |     if not path.is_file():
LINE   85 |         log(f"No existe, se omite: {path}", "ERR")
LINE   86 |         return False
LINE   87 | 
LINE   88 |     text = path.read_text(encoding="utf-8")
LINE   89 | 
LINE   90 |     if marker in text:
LINE   91 |         log(f"Bloque ya presente en {path} (marcador encontrado)", "SKIP")
LINE   92 |         return False
LINE   93 | 
LINE   94 |     if dry_run:
LINE   95 |         log(f"(dry-run) agregaría bloque a {path}", "SKIP")
LINE   96 |         return True
LINE   97 | 
LINE   98 |     if position == "after_anchor" and anchor and anchor in text:
LINE   99 |         idx = text.index(anchor) + len(anchor)
LINE  100 |         new_text = text[:idx] + "\n" + block + "\n" + text[idx:]
LINE  101 |     else:
LINE  102 |         if not text.endswith("\n"):
LINE  103 |             text += "\n"
LINE  104 |         new_text = text + "\n" + block + "\n"
LINE  105 | 
LINE  106 |     with open(path, "w", encoding="utf-8") as f:
LINE  107 |         f.write(new_text)
LINE  108 |     log(f"Bloque agregado a {path}", "OK")
LINE  109 |     return True
LINE  110 | 
LINE  111 | 
LINE  112 | def replace_block(path: Path, old: str, new: str,
LINE  113 |                   dry_run: bool = False) -> bool:
LINE  114 |     """Reemplaza una subcadena exacta por otra. Solo si old está presente."""
LINE  115 |     if not path.is_file():
LINE  116 |         log(f"No existe: {path}", "ERR")
LINE  117 |         return False
LINE  118 | 
LINE  119 |     text = path.read_text(encoding="utf-8")
LINE  120 |     if old not in text:
LINE  121 |         log(f"Patrón no encontrado en {path}", "SKIP")
LINE  122 |         return False
LINE  123 | 
LINE  124 |     if dry_run:
LINE  125 |         log(f"(dry-run) reemplazaría bloque en {path}", "SKIP")
LINE  126 |         return True
LINE  127 | 
LINE  128 |     new_text = text.replace(old, new, 1)
LINE  129 |     with open(path, "w", encoding="utf-8") as f:
LINE  130 |         f.write(new_text)
LINE  131 |     log(f"Bloque reemplazado en {path}", "OK")
LINE  132 |     return True
LINE  133 | 
LINE  134 | 
LINE  135 | # ---------------------------------------------------------------------------
LINE  136 | # Contenido de archivos nuevos
LINE  137 | # ---------------------------------------------------------------------------
LINE  138 | 
LINE  139 | DEPENDENCY_GRAPH_PY = '''"""
LINE  140 | Dependency graph/resolver for project files.
LINE  141 | Resolves imports/includes/requires to real project files and builds a dependency tree.
LINE  142 | """
LINE  143 | import os
LINE  144 | import re
LINE  145 | from dataclasses import dataclass, field
LINE  146 | from typing import List, Dict, Set, Optional
LINE  147 | 
LINE  148 | from app.core.dependency_detector import DependencyDetector
LINE  149 | from app.utils.file_utils import safe_read_file
LINE  150 | 
LINE  151 | 
LINE  152 | @dataclass
LINE  153 | class DependencyNode:
LINE  154 |     rel_path: str
LINE  155 |     depth: int
LINE  156 |     children: List["DependencyNode"] = field(default_factory=list)
LINE  157 |     is_cycle: bool = False
LINE  158 |     is_repeated: bool = False
LINE  159 |     external: Optional[str] = None
LINE  160 | 
LINE  161 | 
LINE  162 | class DependencyResolver:
LINE  163 |     def __init__(
LINE  164 |         self,
LINE  165 |         folder_path: str,
LINE  166 |         excluded_dirs: Optional[Set[str]] = None,
LINE  167 |         detector: Optional[DependencyDetector] = None,
LINE  168 |         max_read_bytes: int = 200_000,
LINE  169 |     ):
LINE  170 |         self.folder_path = os.path.abspath(folder_path)
LINE  171 |         self.excluded_dirs = set(excluded_dirs or [])
LINE  172 |         self.detector = detector or DependencyDetector()
LINE  173 |         self.max_read_bytes = max_read_bytes
LINE  174 | 
LINE  175 |         self._file_index: Dict[str, str] = {}
LINE  176 |         self._module_index: Dict[str, str] = {}
LINE  177 |         self._content_cache: Dict[str, str] = {}
LINE  178 |         self._deps_cache: Dict[str, List[str]] = {}
LINE  179 |         self._expanded: Set[str] = set()
LINE  180 | 
LINE  181 |         self._build_index()
LINE  182 | 
LINE  183 |     # ------------------------------------------------------------------
LINE  184 |     # Index
LINE  185 |     # ------------------------------------------------------------------
LINE  186 |     def _build_index(self) -> None:
LINE  187 |         if not self.folder_path or not os.path.isdir(self.folder_path):
LINE  188 |             return
LINE  189 | 
LINE  190 |         for dirpath, dirnames, filenames in os.walk(self.folder_path):
LINE  191 |             dirnames[:] = [d for d in dirnames if d not in self.excluded_dirs]
LINE  192 | 
LINE  193 |             for f in filenames:
LINE  194 |                 abs_p = os.path.join(dirpath, f)
LINE  195 |                 rel = os.path.relpath(abs_p, self.folder_path).replace("\\\\", "/")
LINE  196 |                 self._file_index[rel] = abs_p
LINE  197 | 
LINE  198 |                 if f.endswith(".py"):
LINE  199 |                     mod = rel[:-3].replace("/", ".")
LINE  200 |                     if mod.endswith(".__init__"):
LINE  201 |                         mod = mod[: -len(".__init__")]
LINE  202 |                     self._module_index[mod] = rel
LINE  203 | 
LINE  204 |     def _normalize(self, rel_path: str) -> str:
LINE  205 |         return rel_path.replace("\\\\", "/").lstrip("./")
LINE  206 | 
LINE  207 |     def _read(self, rel_path: str) -> str:
LINE  208 |         rel_path = self._normalize(rel_path)
LINE  209 |         if rel_path in self._content_cache:
LINE  210 |             return self._content_cache[rel_path]
LINE  211 | 
LINE  212 |         abs_p = self._file_index.get(rel_path)
LINE  213 |         if not abs_p or not os.path.isfile(abs_p):
LINE  214 |             self._content_cache[rel_path] = ""
LINE  215 |             return ""
LINE  216 | 
LINE  217 |         content = safe_read_file(abs_p, max_bytes=self.max_read_bytes)
LINE  218 |         self._content_cache[rel_path] = content
LINE  219 |         return content
LINE  220 | 
LINE  221 |     # ------------------------------------------------------------------
LINE  222 |     # Dependency detection
LINE  223 |     # ------------------------------------------------------------------
LINE  224 |     def get_dependencies(self, rel_path: str) -> List[str]:
LINE  225 |         rel_path = self._normalize(rel_path)
LINE  226 |         if rel_path in self._deps_cache:
LINE  227 |             return self._deps_cache[rel_path]
LINE  228 | 
LINE  229 |         content = self._read(rel_path)
LINE  230 |         if not content:
LINE  231 |             self._deps_cache[rel_path] = []
LINE  232 |             return []
LINE  233 | 
LINE  234 |         deps = self.detector.detect_file_dependencies(rel_path, content)
LINE  235 |         self._deps_cache[rel_path] = deps
LINE  236 |         return deps
LINE  237 | 
LINE  238 |     # ------------------------------------------------------------------
LINE  239 |     # Resolution
LINE  240 |     # ------------------------------------------------------------------
LINE  241 |     def resolve_dependency(self, source_rel_path: str, dep_string: str) -> List[str]:
LINE  242 |         source_rel_path = self._normalize(source_rel_path)
LINE  243 |         ext = os.path.splitext(source_rel_path)[1].lower()
LINE  244 | 
LINE  245 |         if ext == ".py":
LINE  246 |             candidates = self._resolve_python_dep(source_rel_path, dep_string)
LINE  247 |         elif ext in (".js", ".jsx", ".ts", ".tsx", ".vue", ".mjs", ".cjs"):
LINE  248 |             candidates = self._resolve_js_dep(source_rel_path, dep_string)
LINE  249 |         elif ext == ".php":
LINE  250 |             candidates = self._resolve_php_dep(source_rel_path, dep_string)
LINE  251 |         else:
LINE  252 |             candidates = self._resolve_by_basename(dep_string)
LINE  253 | 
LINE  254 |         result: List[str] = []
LINE  255 |         for c in candidates:
LINE  256 |             norm = self._normalize(c)
LINE  257 |             if norm in self._file_index and norm not in result:
LINE  258 |                 result.append(norm)
LINE  259 |         return result
LINE  260 | 
LINE  261 |     def _resolve_python_dep(self, source_rel: str, dep: str) -> List[str]:
LINE  262 |         dep = dep.strip()
LINE  263 | 
LINE  264 |         if dep.startswith("import "):
LINE  265 |             rest = dep[len("import "):].strip()
LINE  266 |             parts = [p.strip() for p in rest.split(",")]
LINE  267 |             result: List[str] = []
LINE  268 |             for p in parts:
LINE  269 |                 p = p.split(" as ")[0].strip()
LINE  270 |                 result.extend(self._module_to_rel(p))
LINE  271 |             return result
LINE  272 | 
LINE  273 |         if dep.startswith("from "):
LINE  274 |             rest = dep[len("from "):].strip()
LINE  275 |             if " import " not in rest:
LINE  276 |                 return []
LINE  277 | 
LINE  278 |             module, _names = rest.split(" import ", 1)
LINE  279 |             module = module.strip()
LINE  280 | 
LINE  281 |             if module.startswith("."):
LINE  282 |                 base_dir = os.path.dirname(source_rel)
LINE  283 |                 dots = len(module) - len(module.lstrip("."))
LINE  284 |                 module_name = module.lstrip(".")
LINE  285 | 
LINE  286 |                 up = max(0, dots - 1)
LINE  287 |                 parts = base_dir.split("/") if base_dir else []
LINE  288 |                 if up > 0:
LINE  289 |                     parts = parts[:-up] if up <= len(parts) else []
LINE  290 | 
LINE  291 |                 rel_dir = "/".join(parts)
LINE  292 |                 if module_name:
LINE  293 |                     mod_path = (rel_dir + "/" + module_name.replace(".", "/")) if rel_dir else module_name.replace(".", "/")
LINE  294 |                 else:
LINE  295 |                     mod_path = rel_dir
LINE  296 | 
LINE  297 |                 return self._path_to_rel_candidates(mod_path)
LINE  298 | 
LINE  299 |             return self._module_to_rel(module)
LINE  300 | 
LINE  301 |         return []
LINE  302 | 
LINE  303 |     def _module_to_rel(self, module: str) -> List[str]:
LINE  304 |         module = module.strip()
LINE  305 |         if not module:
LINE  306 |             return []
LINE  307 | 
LINE  308 |         if module in self._module_index:
LINE  309 |             return [self._module_index[module]]
LINE  310 | 
LINE  311 |         pkg_init = module + ".__init__"
LINE  312 |         if pkg_init in self._module_index:
LINE  313 |             return [self._module_index[pkg_init]]
LINE  314 | 
LINE  315 |         path_py = module.replace(".", "/") + ".py"
LINE  316 |         if path_py in self._file_index:
LINE  317 |             return [path_py]
LINE  318 | 
LINE  319 |         path_init = module.replace(".", "/") + "/__init__.py"
LINE  320 |         if path_init in self._file_index:
LINE  321 |             return [path_init]
LINE  322 | 
LINE  323 |         return []
LINE  324 | 
LINE  325 |     def _path_to_rel_candidates(self, base_path: str) -> List[str]:
LINE  326 |         base_path = self._normalize(base_path)
LINE  327 |         candidates = []
LINE  328 |         for cand in (
LINE  329 |             base_path + ".py",
LINE  330 |             base_path + "/__init__.py",
LINE  331 |             base_path,
LINE  332 |         ):
LINE  333 |             if cand in self._file_index:
LINE  334 |                 candidates.append(cand)
LINE  335 |         return candidates
LINE  336 | 
LINE  337 |     def _resolve_js_dep(self, source_rel: str, dep: str) -> List[str]:
LINE  338 |         m = re.search(r'[\\'"]([^\\'"]+)[\\'"]', dep)
LINE  339 |         if not m:
LINE  340 |             return []
LINE  341 | 
LINE  342 |         raw = m.group(1)
LINE  343 |         if not raw.startswith("."):
LINE  344 |             return []
LINE  345 | 
LINE  346 |         base_dir = os.path.dirname(source_rel)
LINE  347 |         target = os.path.normpath(os.path.join(base_dir, raw)).replace("\\\\", "/")
LINE  348 | 
LINE  349 |         candidates: List[str] = []
LINE  350 |         for ext in ("", ".js", ".jsx", ".ts", ".tsx", ".vue", ".json", ".mjs", ".cjs"):
LINE  351 |             cand = target + ext
LINE  352 |             if cand in self._file_index:
LINE  353 |                 candidates.append(cand)
LINE  354 | 
LINE  355 |         for ext in (".js", ".jsx", ".ts", ".tsx", ".vue"):
LINE  356 |             cand = target + "/index" + ext
LINE  357 |             if cand in self._file_index:
LINE  358 |                 candidates.append(cand)
LINE  359 | 
LINE  360 |         return candidates
LINE  361 | 
LINE  362 |     def _resolve_php_dep(self, source_rel: str, dep: str) -> List[str]:
LINE  363 |         m = re.search(r'[\\'"]([^\\'"]+)[\\'"]', dep)
LINE  364 |         if not m:
LINE  365 |             return []
LINE  366 | 
LINE  367 |         raw = m.group(1)
LINE  368 | 
LINE  369 |         if raw.startswith("."):
LINE  370 |             base_dir = os.path.dirname(source_rel)
LINE  371 |             target = os.path.normpath(os.path.join(base_dir, raw)).replace("\\\\", "/")
LINE  372 |             for cand in (target, target + ".php"):
LINE  373 |                 if cand in self._file_index:
LINE  374 |                     return [cand]
LINE  375 |             return []
LINE  376 | 
LINE  377 |         for cand in (raw, raw + ".php"):
LINE  378 |             if cand in self._file_index:
LINE  379 |                 return [cand]
LINE  380 | 
LINE  381 |         return []
LINE  382 | 
LINE  383 |     def _resolve_by_basename(self, dep: str) -> List[str]:
LINE  384 |         base = os.path.basename(dep)
LINE  385 |         return [rel for rel in self._file_index if os.path.basename(rel) == base]
LINE  386 | 
LINE  387 |     # ------------------------------------------------------------------
LINE  388 |     # Tree building
LINE  389 |     # ------------------------------------------------------------------
LINE  390 |     def build_tree(self, root_rel_path: str, max_depth: int = 50) -> DependencyNode:
LINE  391 |         root_rel_path = self._normalize(root_rel_path)
LINE  392 |         self._expanded.clear()
LINE  393 |         return self._build_node(root_rel_path, depth=0, ancestors=set(), max_depth=max_depth)
LINE  394 | 
LINE  395 |     def _build_node(
LINE  396 |         self,
LINE  397 |         rel_path: str,
LINE  398 |         depth: int,
LINE  399 |         ancestors: Set[str],
LINE  400 |         max_depth: int,
LINE  401 |     ) -> DependencyNode:
LINE  402 |         node = DependencyNode(rel_path=rel_path, depth=depth)
LINE  403 | 
LINE  404 |         if depth >= max_depth:
LINE  405 |             return node
LINE  406 | 
LINE  407 |         if rel_path in ancestors:
LINE  408 |             node.is_cycle = True
LINE  409 |             return node
LINE  410 | 
LINE  411 |         if rel_path in self._expanded:
LINE  412 |             node.is_repeated = True
LINE  413 |             return node
LINE  414 | 
LINE  415 |         self._expanded.add(rel_path)
LINE  416 | 
LINE  417 |         new_ancestors = set(ancestors)
LINE  418 |         new_ancestors.add(rel_path)
LINE  419 | 
LINE  420 |         for dep in self.get_dependencies(rel_path):
LINE  421 |             for child_rel in self.resolve_dependency(rel_path, dep):
LINE  422 |                 child = self._build_node(
LINE  423 |                     child_rel,
LINE  424 |                     depth=depth + 1,
LINE  425 |                     ancestors=new_ancestors,
LINE  426 |                     max_depth=max_depth,
LINE  427 |                 )
LINE  428 |                 node.children.append(child)
LINE  429 | 
LINE  430 |         return node
LINE  431 | '''
LINE  432 | 
LINE  433 | 
LINE  434 | DEPENDENCY_TREE_DIALOG_PY = '''"""Dependency tree dialog. Reuses CheckboxTreeview and integrates with existing file selection."""
LINE  435 | import tkinter as tk
LINE  436 | from tkinter import ttk
LINE  437 | from typing import Callable, List, Optional, Set
LINE  438 | 
LINE  439 | from app.core.dependency_graph import DependencyResolver, DependencyNode
LINE  440 | from app.gui.file_tree import CheckboxTreeview
LINE  441 | 
LINE  442 | C_BG = "#1e2330"
LINE  443 | C_PANEL = "#252b3b"
LINE  444 | C_BORDER = "#323a50"
LINE  445 | C_ACCENT = "#4f8ef7"
LINE  446 | C_TEXT = "#e8eaf0"
LINE  447 | C_TEXT2 = "#8b92a8"
LINE  448 | C_ENTRY = "#2a3148"
LINE  449 | 
LINE  450 | 
LINE  451 | class DependencyTreeDialog(tk.Toplevel):
LINE  452 |     def __init__(
LINE  453 |         self,
LINE  454 |         parent: tk.Tk,
LINE  455 |         folder_path: str,
LINE  456 |         root_rel_path: str,
LINE  457 |         excluded_dirs: Optional[Set[str]] = None,
LINE  458 |         on_apply_selection: Optional[Callable[[List[str]], None]] = None,
LINE  459 |     ):
LINE  460 |         super().__init__(parent)
LINE  461 |         self.folder_path = folder_path
LINE  462 |         self.root_rel_path = root_rel_path
LINE  463 |         self.on_apply_selection = on_apply_selection
LINE  464 | 
LINE  465 |         self.title(f"🌳 Dependencias: {root_rel_path}")
LINE  466 |         self.geometry("900x650")
LINE  467 |         self.minsize(700, 480)
LINE  468 |         self.configure(bg=C_BG)
LINE  469 | 
LINE  470 |         self.transient(parent)
LINE  471 |         self.grab_set()
LINE  472 | 
LINE  473 |         try:
LINE  474 |             self.resolver = DependencyResolver(folder_path, excluded_dirs=excluded_dirs)
LINE  475 |             self.root_node = self.resolver.build_tree(root_rel_path)
LINE  476 |         except Exception as exc:
LINE  477 |             tk.Label(
LINE  478 |                 self,
LINE  479 |                 text=f"Error al construir árbol: {exc}",
LINE  480 |                 bg=C_BG, fg=C_TEXT, font=("Segoe UI", 10),
LINE  481 |             ).pack(padx=20, pady=20)
LINE  482 |             self.root_node = None
LINE  483 | 
LINE  484 |         self._build_header()
LINE  485 |         self._build_tree()
LINE  486 |         self._build_buttons()
LINE  487 | 
LINE  488 |         if self.root_node is not None:
LINE  489 |             self._insert_node("", self.root_node, is_root=True)
LINE  490 | 
LINE  491 |     def _build_header(self):
LINE  492 |         hdr = tk.Frame(self, bg=C_PANEL, padx=14, pady=10)
LINE  493 |         hdr.pack(fill=tk.X)
LINE  494 | 
LINE  495 |         tk.Label(
LINE  496 |             hdr,
LINE  497 |             text=f"🌳 Árbol de dependencias: {self.root_rel_path}",
LINE  498 |             font=("Segoe UI", 12, "bold"),
LINE  499 |             bg=C_PANEL,
LINE  500 |             fg=C_TEXT,
LINE  501 |         ).pack(anchor="w")
LINE  502 | 
LINE  503 |         tk.Label(
LINE  504 |             hdr,
LINE  505 |             text="Selecciona archivos o ramas y aplícalos al contexto principal.",
LINE  506 |             font=("Segoe UI", 8),
LINE  507 |             bg=C_PANEL,
LINE  508 |             fg=C_TEXT2,
LINE  509 |         ).pack(anchor="w")
LINE  510 | 
LINE  511 |     def _build_tree(self):
LINE  512 |         container = tk.Frame(self, bg=C_BG, padx=10, pady=6)
LINE  513 |         container.pack(fill=tk.BOTH, expand=True)
LINE  514 | 
LINE  515 |         self.tree = CheckboxTreeview(container)
LINE  516 |         sy = ttk.Scrollbar(container, orient=tk.VERTICAL, command=self.tree.yview)
LINE  517 |         sx = ttk.Scrollbar(container, orient=tk.HORIZONTAL, command=self.tree.xview)
LINE  518 |         self.tree.configure(yscrollcommand=sy.set, xscrollcommand=sx.set)
LINE  519 | 
LINE  520 |         sy.pack(side=tk.RIGHT, fill=tk.Y)
LINE  521 |         sx.pack(side=tk.BOTTOM, fill=tk.X)
LINE  522 |         self.tree.pack(fill=tk.BOTH, expand=True)
LINE  523 | 
LINE  524 |     def _build_buttons(self):
LINE  525 |         bar = tk.Frame(self, bg=C_PANEL, padx=10, pady=8)
LINE  526 |         bar.pack(fill=tk.X, side=tk.BOTTOM)
LINE  527 | 
LINE  528 |         ttk.Button(bar, text="Seleccionar raíz", command=self._select_root).pack(side=tk.LEFT, padx=2)
LINE  529 |         ttk.Button(bar, text="Seleccionar rama", command=self._select_branch).pack(side=tk.LEFT, padx=2)
LINE  530 |         ttk.Button(bar, text="Seleccionar todos", command=self._select_all).pack(side=tk.LEFT, padx=2)
LINE  531 |         ttk.Button(bar, text="Deseleccionar rama", command=self._deselect_branch).pack(side=tk.LEFT, padx=2)
LINE  532 | 
LINE  533 |         ttk.Button(bar, text="✅ Aplicar selección", command=self._apply).pack(side=tk.RIGHT, padx=2)
LINE  534 |         ttk.Button(bar, text="Cerrar", command=self.destroy).pack(side=tk.RIGHT, padx=2)
LINE  535 | 
LINE  536 |     def _insert_node(self, parent_item: str, node: DependencyNode, is_root: bool = False):
LINE  537 |         notes = []
LINE  538 |         if node.is_cycle:
LINE  539 |             notes.append("⟲ ciclo")
LINE  540 |         if node.is_repeated:
LINE  541 |             notes.append("♻ ya analizado")
LINE  542 | 
LINE  543 |         icon = "📄"
LINE  544 |         if node.is_cycle:
LINE  545 |             icon = "🔁"
LINE  546 |         elif node.is_repeated:
LINE  547 |             icon = "🔂"
LINE  548 |         elif node.children:
LINE  549 |             icon = "📂"
LINE  550 | 
LINE  551 |         item = self.tree.insert(
LINE  552 |             parent_item,
LINE  553 |             "end",
LINE  554 |             text=icon,
LINE  555 |             values=("☐", node.rel_path),
LINE  556 |             tags=("unchecked",),
LINE  557 |         )
LINE  558 | 
LINE  559 |         for child in node.children:
LINE  560 |             self._insert_node(item, child)
LINE  561 | 
LINE  562 |         return item
LINE  563 | 
LINE  564 |     def _current_item(self):
LINE  565 |         sel = self.tree.selection()
LINE  566 |         return sel[0] if sel else None
LINE  567 | 
LINE  568 |     def _select_root(self):
LINE  569 |         if self.tree.get_children():
LINE  570 |             root = self.tree.get_children()[0]
LINE  571 |             self.tree.check_item(root)
LINE  572 | 
LINE  573 |     def _select_branch(self):
LINE  574 |         item = self._current_item()
LINE  575 |         if item:
LINE  576 |             self.tree.check_item(item)
LINE  577 | 
LINE  578 |     def _select_all(self):
LINE  579 |         self.tree.select_all()
LINE  580 | 
LINE  581 |     def _deselect_branch(self):
LINE  582 |         item = self._current_item()
LINE  583 |         if item:
LINE  584 |             self.tree.uncheck_item(item)
LINE  585 | 
LINE  586 |     def _apply(self):
LINE  587 |         selected = self.tree.get_checked_files()
LINE  588 |         if self.on_apply_selection:
LINE  589 |             self.on_apply_selection(selected)
LINE  590 |         self.destroy()
LINE  591 | '''
LINE  592 | 
LINE  593 | 
LINE  594 | FILE_SEARCH_DIALOG_PY = '''"""File search dialog with per-file dependency analysis action."""
LINE  595 | import os
LINE  596 | import tkinter as tk
LINE  597 | from tkinter import ttk
LINE  598 | from typing import Callable, List, Optional, Set
LINE  599 | 
LINE  600 | from app.core.project_scanner import scan_directory
LINE  601 | 
LINE  602 | C_BG = "#1e2330"
LINE  603 | C_PANEL = "#252b3b"
LINE  604 | C_BORDER = "#323a50"
LINE  605 | C_ACCENT = "#4f8ef7"
LINE  606 | C_TEXT = "#e8eaf0"
LINE  607 | C_TEXT2 = "#8b92a8"
LINE  608 | C_ENTRY = "#2a3148"
LINE  609 | 
LINE  610 | 
LINE  611 | class FileSearchDialog(tk.Toplevel):
LINE  612 |     def __init__(
LINE  613 |         self,
LINE  614 |         parent: tk.Tk,
LINE  615 |         folder_path: str,
LINE  616 |         excluded_dirs: Optional[Set[str]] = None,
LINE  617 |         on_analyze_dependencies: Optional[Callable[[str], None]] = None,
LINE  618 |     ):
LINE  619 |         super().__init__(parent)
LINE  620 |         self.folder_path = folder_path
LINE  621 |         self.excluded_dirs = excluded_dirs or set()
LINE  622 |         self.on_analyze_dependencies = on_analyze_dependencies
LINE  623 | 
LINE  624 |         self.title("🔎 Buscador de archivos")
LINE  625 |         self.geometry("820x560")
LINE  626 |         self.minsize(640, 420)
LINE  627 |         self.configure(bg=C_BG)
LINE  628 | 
LINE  629 |         self.transient(parent)
LINE  630 |         self.grab_set()
LINE  631 | 
LINE  632 |         self.search_var = tk.StringVar()
LINE  633 |         self.all_files: List[str] = []
LINE  634 | 
LINE  635 |         self._build_header()
LINE  636 |         self._build_results()
LINE  637 |         self._load_files()
LINE  638 | 
LINE  639 |     def _build_header(self):
LINE  640 |         hdr = tk.Frame(self, bg=C_PANEL, padx=12, pady=10)
LINE  641 |         hdr.pack(fill=tk.X)
LINE  642 | 
LINE  643 |         tk.Label(
LINE  644 |             hdr,
LINE  645 |             text="🔎 Buscar archivos del proyecto",
LINE  646 |             font=("Segoe UI", 12, "bold"),
LINE  647 |             bg=C_PANEL,
LINE  648 |             fg=C_TEXT,
LINE  649 |         ).pack(anchor="w")
LINE  650 | 
LINE  651 |         row = tk.Frame(hdr, bg=C_PANEL)
LINE  652 |         row.pack(fill=tk.X, pady=(6, 0))
LINE  653 | 
LINE  654 |         self.entry = ttk.Entry(row, textvariable=self.search_var, font=("Consolas", 9))
LINE  655 |         self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 6))
LINE  656 |         self.entry.bind("<KeyRelease>", lambda _e: self._refresh_results())
LINE  657 | 
LINE  658 |         ttk.Button(row, text="Buscar", command=self._refresh_results).pack(side=tk.LEFT)
LINE  659 |         ttk.Button(row, text="Limpiar", command=self._clear_search).pack(side=tk.LEFT, padx=(6, 0))
LINE  660 | 
LINE  661 |     def _build_results(self):
LINE  662 |         container = tk.Frame(self, bg=C_ENTRY, bd=1, relief="flat",
LINE  663 |                              highlightbackground=C_BORDER, highlightthickness=1)
LINE  664 |         container.pack(fill=tk.BOTH, expand=True, padx=12, pady=8)
LINE  665 | 
LINE  666 |         self.canvas = tk.Canvas(container, bg=C_ENTRY, bd=0, highlightthickness=0)
LINE  667 |         scrollbar = ttk.Scrollbar(container, orient=tk.VERTICAL, command=self.canvas.yview)
LINE  668 |         self.scroll_frame = tk.Frame(self.canvas, bg=C_ENTRY)
LINE  669 | 
LINE  670 |         self.scroll_frame.bind(
LINE  671 |             "<Configure>",
LINE  672 |             lambda _e: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
LINE  673 |         )
LINE  674 |         self.canvas_window = self.canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")
LINE  675 | 
LINE  676 |         def _on_resize(event):
LINE  677 |             self.canvas.itemconfig(self.canvas_window, width=event.width)
LINE  678 | 
LINE  679 |         self.canvas.bind("<Configure>", _on_resize)
LINE  680 | 
LINE  681 |         def _on_mousewheel(event):
LINE  682 |             if event.delta:
LINE  683 |                 self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
LINE  684 |             elif event.num == 4:
LINE  685 |                 self.canvas.yview_scroll(-1, "units")
LINE  686 |             elif event.num == 5:
LINE  687 |                 self.canvas.yview_scroll(1, "units")
LINE  688 | 
LINE  689 |         self.canvas.bind_all("<MouseWheel>", _on_mousewheel)
LINE  690 |         self.canvas.bind_all("<Button-4>", _on_mousewheel)
LINE  691 |         self.canvas.bind_all("<Button-5>", _on_mousewheel)
LINE  692 | 
LINE  693 |         self.canvas.configure(yscrollcommand=scrollbar.set)
LINE  694 |         scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
LINE  695 |         self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
LINE  696 | 
LINE  697 |     def _load_files(self):
LINE  698 |         try:
LINE  699 |             self.all_files = scan_directory(
LINE  700 |                 self.folder_path,
LINE  701 |                 self.excluded_dirs,
LINE  702 |                 allowed_extensions=None,
LINE  703 |             )
LINE  704 |         except Exception:
LINE  705 |             self.all_files = []
LINE  706 |         self._refresh_results()
LINE  707 | 
LINE  708 |     def _clear_search(self):
LINE  709 |         self.search_var.set("")
LINE  710 |         self._refresh_results()
LINE  711 | 
LINE  712 |     def _refresh_results(self):
LINE  713 |         query = self.search_var.get().strip().lower()
LINE  714 | 
LINE  715 |         for child in self.scroll_frame.winfo_children():
LINE  716 |             child.destroy()
LINE  717 | 
LINE  718 |         matches = [
LINE  719 |             rel for rel in self.all_files
LINE  720 |             if not query or query in rel.lower()
LINE  721 |         ]
LINE  722 | 
LINE  723 |         if not matches:
LINE  724 |             tk.Label(
LINE  725 |                 self.scroll_frame,
LINE  726 |                 text="(Sin resultados)",
LINE  727 |                 font=("Segoe UI", 9, "italic"),
LINE  728 |                 bg=C_ENTRY,
LINE  729 |                 fg=C_TEXT2,
LINE  730 |             ).pack(anchor="w", padx=10, pady=10)
LINE  731 |             return
LINE  732 | 
LINE  733 |         for rel in matches:
LINE  734 |             row = tk.Frame(self.scroll_frame, bg=C_ENTRY, padx=8, pady=3)
LINE  735 |             row.pack(fill=tk.X)
LINE  736 | 
LINE  737 |             tk.Label(
LINE  738 |                 row,
LINE  739 |                 text=rel,
LINE  740 |                 font=("Consolas", 9),
LINE  741 |                 bg=C_ENTRY,
LINE  742 |                 fg=C_TEXT,
LINE  743 |                 anchor="w",
LINE  744 |             ).pack(side=tk.LEFT, fill=tk.X, expand=True)
LINE  745 | 
LINE  746 |             ttk.Button(
LINE  747 |                 row,
LINE  748 |                 text="🔗 Dependencias",
LINE  749 |                 command=lambda r=rel: self._analyze(r),
LINE  750 |             ).pack(side=tk.RIGHT)
LINE  751 | 
LINE  752 |     def _analyze(self, rel_path: str):
LINE  753 |         if self.on_analyze_dependencies:
LINE  754 |             self.on_analyze_dependencies(rel_path)
LINE  755 | '''
LINE  756 | 
LINE  757 | 
LINE  758 | TEST_DEPENDENCY_GRAPH_PY = '''import os
LINE  759 | import shutil
LINE  760 | import tempfile
LINE  761 | import unittest
LINE  762 | 
LINE  763 | from app.core.dependency_graph import DependencyResolver
LINE  764 | 
LINE  765 | 
LINE  766 | class TestDependencyResolver(unittest.TestCase):
LINE  767 | 
LINE  768 |     def setUp(self):
LINE  769 |         self.tmp = tempfile.mkdtemp(prefix="test_dep_graph_")
LINE  770 | 
LINE  771 |     def tearDown(self):
LINE  772 |         shutil.rmtree(self.tmp, ignore_errors=True)
LINE  773 | 
LINE  774 |     def _write(self, rel_path, content):
LINE  775 |         path = os.path.join(self.tmp, rel_path)
LINE  776 |         os.makedirs(os.path.dirname(path), exist_ok=True)
LINE  777 |         with open(path, "w", encoding="utf-8") as f:
LINE  778 |             f.write(content)
LINE  779 | 
LINE  780 |     def test_file_without_dependencies(self):
LINE  781 |         self._write("a.py", "x = 1\\n")
LINE  782 |         resolver = DependencyResolver(self.tmp)
LINE  783 |         node = resolver.build_tree("a.py")
LINE  784 |         self.assertEqual(node.rel_path, "a.py")
LINE  785 |         self.assertEqual(node.children, [])
LINE  786 | 
LINE  787 |     def test_single_dependency(self):
LINE  788 |         self._write("a.py", "import b\\n")
LINE  789 |         self._write("b.py", "x = 1\\n")
LINE  790 |         resolver = DependencyResolver(self.tmp)
LINE  791 |         node = resolver.build_tree("a.py")
LINE  792 |         self.assertEqual(len(node.children), 1)
LINE  793 |         self.assertEqual(node.children[0].rel_path, "b.py")
LINE  794 | 
LINE  795 |     def test_chain_dependencies(self):
LINE  796 |         self._write("a.py", "import b\\n")
LINE  797 |         self._write("b.py", "import c\\n")
LINE  798 |         self._write("c.py", "x = 1\\n")
LINE  799 |         resolver = DependencyResolver(self.tmp)
LINE  800 |         node = resolver.build_tree("a.py")
LINE  801 |         self.assertEqual(node.children[0].rel_path, "b.py")
LINE  802 |         self.assertEqual(node.children[0].children[0].rel_path, "c.py")
LINE  803 | 
LINE  804 |     def test_circular_dependency(self):
LINE  805 |         self._write("a.py", "import b\\n")
LINE  806 |         self._write("b.py", "import c\\n")
LINE  807 |         self._write("c.py", "import a\\n")
LINE  808 |         resolver = DependencyResolver(self.tmp)
LINE  809 |         node = resolver.build_tree("a.py")
LINE  810 |         c = node.children[0].children[0]
LINE  811 |         self.assertEqual(c.rel_path, "c.py")
LINE  812 |         self.assertTrue(c.children[0].is_cycle)
LINE  813 | 
LINE  814 |     def test_repeated_dependency(self):
LINE  815 |         self._write("a.py", "import b\\nimport c\\n")
LINE  816 |         self._write("b.py", "import d\\n")
LINE  817 |         self._write("c.py", "import d\\n")
LINE  818 |         self._write("d.py", "x = 1\\n")
LINE  819 |         resolver = DependencyResolver(self.tmp)
LINE  820 |         node = resolver.build_tree("a.py")
LINE  821 |         b = next(ch for ch in node.children if ch.rel_path == "b.py")
LINE  822 |         c = next(ch for ch in node.children if ch.rel_path == "c.py")
LINE  823 |         self.assertEqual(b.children[0].rel_path, "d.py")
LINE  824 |         self.assertEqual(c.children[0].rel_path, "d.py")
LINE  825 |         self.assertTrue(c.children[0].is_repeated)
LINE  826 | 
LINE  827 |     def test_external_dependency_ignored(self):
LINE  828 |         self._write("a.py", "import os\\n")
LINE  829 |         resolver = DependencyResolver(self.tmp)
LINE  830 |         node = resolver.build_tree("a.py")
LINE  831 |         self.assertEqual(node.children, [])
LINE  832 | 
LINE  833 |     def test_missing_dependency_ignored(self):
LINE  834 |         self._write("a.py", "import missing_module\\n")
LINE  835 |         resolver = DependencyResolver(self.tmp)
LINE  836 |         node = resolver.build_tree("a.py")
LINE  837 |         self.assertEqual(node.children, [])
LINE  838 | 
LINE  839 | 
LINE  840 | if __name__ == "__main__":
LINE  841 |     unittest.main()
LINE  842 | '''
LINE  843 | 
LINE  844 | 
LINE  845 | # ---------------------------------------------------------------------------
LINE  846 | # Bloques de código a insertar en main_window.py
LINE  847 | # ---------------------------------------------------------------------------
LINE  848 | 
LINE  849 | MAIN_WINDOW_IMPORTS_BLOCK = """# === AUTO-GENERATED: file_search_dependency_feature ===
LINE  850 | from app.gui.file_search_dialog import FileSearchDialog
LINE  851 | from app.gui.dependency_tree_dialog import DependencyTreeDialog
LINE  852 | # === END AUTO-GENERATED ===
LINE  853 | """
LINE  854 | 
LINE  855 | MAIN_WINDOW_METHODS_BLOCK = """    # === AUTO-GENERATED: file_search_dependency_feature ===
LINE  856 |     def on_open_file_search(self):
LINE  857 |         folder = self.var_folder.get()
LINE  858 |         if not folder or not os.path.isdir(folder):
LINE  859 |             dialogs.show_warning("Atención", "Selecciona una carpeta del proyecto primero.")
LINE  860 |             return
LINE  861 | 
LINE  862 |         excluded = self.selector.get_selection().excluded_dirs
LINE  863 |         FileSearchDialog(
LINE  864 |             self.root,
LINE  865 |             folder,
LINE  866 |             excluded_dirs=excluded,
LINE  867 |             on_analyze_dependencies=self.open_dependency_tree,
LINE  868 |         )
LINE  869 | 
LINE  870 |     def open_dependency_tree(self, rel_path: str):
LINE  871 |         folder = self.var_folder.get()
LINE  872 |         if not folder or not os.path.isdir(folder):
LINE  873 |             dialogs.show_warning("Atención", "Selecciona una carpeta del proyecto primero.")
LINE  874 |             return
LINE  875 | 
LINE  876 |         excluded = self.selector.get_selection().excluded_dirs
LINE  877 |         DependencyTreeDialog(
LINE  878 |             self.root,
LINE  879 |             folder,
LINE  880 |             rel_path,
LINE  881 |             excluded_dirs=excluded,
LINE  882 |             on_apply_selection=self.apply_dependency_selection,
LINE  883 |         )
LINE  884 | 
LINE  885 |     def apply_dependency_selection(self, selected_files: List[str]):
LINE  886 |         if not selected_files:
LINE  887 |             return
LINE  888 | 
LINE  889 |         existing = set(self.tree.get_checked_files())
LINE  890 |         combined = existing | set(selected_files)
LINE  891 | 
LINE  892 |         self.tree.set_checked_files(combined)
LINE  893 |         self.selector.set_checked_folder_files(self.tree.get_checked_files())
LINE  894 |         self._refresh_selection_stats()
LINE  895 | 
LINE  896 |         self.sv_status.set(
LINE  897 |             f"✓ {len(selected_files)} dependencia(s) agregadas/actualizadas en la selección."
LINE  898 |         )
LINE  899 |     # === END AUTO-GENERATED ===
LINE  900 | """
LINE  901 | 
LINE  902 | 
LINE  903 | CORE_INIT_NEW = '''"""Core package initialization."""
LINE  904 | from app.core.project_scanner import scan_directory
LINE  905 | from app.core.file_selector import FileSelectorManager
LINE  906 | from app.core.file_reader import read_and_format_file
LINE  907 | from app.core.project_structure import build_folder_tree_str
LINE  908 | from app.core.dependency_detector import DependencyDetector, detect_project_dependencies
LINE  909 | from app.core.dependency_graph import DependencyResolver, DependencyNode
LINE  910 | 
LINE  911 | __all__ = [
LINE  912 |     "scan_directory",
LINE  913 |     "FileSelectorManager",
LINE  914 |     "read_and_format_file",
LINE  915 |     "build_folder_tree_str",
LINE  916 |     "DependencyDetector",
LINE  917 |     "detect_project_dependencies",
LINE  918 |     "DependencyResolver",
LINE  919 |     "DependencyNode",
LINE  920 | ]
LINE  921 | '''
LINE  922 | 
LINE  923 | 
LINE  924 | # ---------------------------------------------------------------------------
LINE  925 | # Aplicación de cambios
LINE  926 | # ---------------------------------------------------------------------------
LINE  927 | 
LINE  928 | def apply_changes(root: Path, dry_run: bool = False, backup: bool = True):
LINE  929 |     backup_root = root / BACKUP_DIRNAME
LINE  930 |     if backup and not dry_run:
LINE  931 |         ensure_dir(backup_root)
LINE  932 | 
LINE  933 |     log(f"Raíz del proyecto: {root}")
LINE  934 |     log(f"Modo dry-run: {dry_run}")
LINE  935 |     log(f"Respaldos: {'activado' if backup else 'desactivado'}")
LINE  936 |     print()
LINE  937 | 
LINE  938 |     # -----------------------------------------------------------------
LINE  939 |     # 1. Verificación básica de estructura
LINE  940 |     # -----------------------------------------------------------------
LINE  941 |     required = [
LINE  942 |         root / "app" / "core" / "dependency_detector.py",
LINE  943 |         root / "app" / "core" / "file_selector.py",
LINE  944 |         root / "app" / "core" / "project_scanner.py",
LINE  945 |         root / "app" / "gui" / "file_tree.py",
LINE  946 |         root / "app" / "gui" / "main_window.py",
LINE  947 |         root / "app" / "models" / "project.py",
LINE  948 |     ]
LINE  949 |     missing = [str(p) for p in required if not p.is_file()]
LINE  950 |     if missing:
LINE  951 |         log("Estructura del proyecto no reconocida. Archivos faltantes:", "ERR")
LINE  952 |         for m in missing:
LINE  953 |             log(f"  - {m}", "ERR")
LINE  954 |         sys.exit(1)
LINE  955 | 
LINE  956 |     # -----------------------------------------------------------------
LINE  957 |     # 2. Respaldos
LINE  958 |     # -----------------------------------------------------------------
LINE  959 |     if backup:
LINE  960 |         log("--- Creando respaldos ---")
LINE  961 |         for f in [
LINE  962 |             root / "app" / "core" / "__init__.py",
LINE  963 |             root / "app" / "gui" / "main_window.py",
LINE  964 |         ]:
LINE  965 |             backup_file(f, backup_root, dry_run=dry_run)
LINE  966 |         print()
LINE  967 | 
LINE  968 |     # -----------------------------------------------------------------
LINE  969 |     # 3. Nuevos archivos
LINE  970 |     # -----------------------------------------------------------------
LINE  971 |     log("--- Creando archivos nuevos ---")
LINE  972 |     write_file(
LINE  973 |         root / "app" / "core" / "dependency_graph.py",
LINE  974 |         DEPENDENCY_GRAPH_PY,
LINE  975 |         dry_run=dry_run,
LINE  976 |     )
LINE  977 |     write_file(
LINE  978 |         root / "app" / "gui" / "dependency_tree_dialog.py",
LINE  979 |         DEPENDENCY_TREE_DIALOG_PY,
LINE  980 |         dry_run=dry_run,
LINE  981 |     )
LINE  982 |     write_file(
LINE  983 |         root / "app" / "gui" / "file_search_dialog.py",
LINE  984 |         FILE_SEARCH_DIALOG_PY,
LINE  985 |         dry_run=dry_run,
LINE  986 |     )
LINE  987 |     write_file(
LINE  988 |         root / "tests" / "test_dependency_graph.py",
LINE  989 |         TEST_DEPENDENCY_GRAPH_PY,
LINE  990 |         dry_run=dry_run,
LINE  991 |     )
LINE  992 |     print()
LINE  993 | 
LINE  994 |     # -----------------------------------------------------------------
LINE  995 |     # 4. Modificar app/core/__init__.py
LINE  996 |     # -----------------------------------------------------------------
LINE  997 |     log("--- Actualizando app/core/__init__.py ---")
LINE  998 |     core_init = root / "app" / "core" / "__init__.py"
LINE  999 |     if core_init.is_file():
LINE 1000 |         current = core_init.read_text(encoding="utf-8")
LINE 1001 |         if "DependencyResolver" in current and "dependency_graph" in current:
LINE 1002 |             log("app/core/__init__.py ya actualizado", "SKIP")
LINE 1003 |         else:
LINE 1004 |             if dry_run:
LINE 1005 |                 log("(dry-run) reemplazaría app/core/__init__.py", "SKIP")
LINE 1006 |             else:
LINE 1007 |                 with open(core_init, "w", encoding="utf-8") as f:
LINE 1008 |                     f.write(CORE_INIT_NEW)
LINE 1009 |                 log(f"Actualizado: {core_init}", "OK")
LINE 1010 |     print()
LINE 1011 | 
LINE 1012 |     # -----------------------------------------------------------------
LINE 1013 |     # 5. Modificar app/gui/main_window.py
LINE 1014 |     # -----------------------------------------------------------------
LINE 1015 |     log("--- Modificando app/gui/main_window.py ---")
LINE 1016 |     mw = root / "app" / "gui" / "main_window.py"
LINE 1017 |     mw_text = mw.read_text(encoding="utf-8")
LINE 1018 | 
LINE 1019 |     # 5.1 Importar diálogos
LINE 1020 |     if "file_search_dialog" not in mw_text and "FileSearchDialog" not in mw_text:
LINE 1021 |         anchor_import = "from app.gui import dialogs"
LINE 1022 |         if anchor_import in mw_text:
LINE 1023 |             append_block_if_missing(
LINE 1024 |                 mw,
LINE 1025 |                 marker=MARKER_NEW_FILES,
LINE 1026 |                 block=MAIN_WINDOW_IMPORTS_BLOCK,
LINE 1027 |                 dry_run=dry_run,
LINE 1028 |                 position="after_anchor",
LINE 1029 |                 anchor=anchor_import,
LINE 1030 |             )
LINE 1031 |         else:
LINE 1032 |             log("No se encontró 'from app.gui import dialogs' para anclar imports", "WARN")
LINE 1033 |     else:
LINE 1034 |         log("Imports de diálogos ya presentes", "SKIP")
LINE 1035 | 
LINE 1036 |     # 5.2 Insertar botón "Buscador" en toolbar del árbol
LINE 1037 |     mw_text = mw.read_text(encoding="utf-8")
LINE 1038 |     if 'text="🔎 Buscador"' not in mw_text:
LINE 1039 |         old_btn = (
LINE 1040 |             'ttk.Button(tb, text="🧠 Selección Inteligente", style="Accent.TButton",\n'
LINE 1041 |             '                   command=self.on_intelligent_context_select).pack(side=tk.LEFT, padx=(0, 4))\n'
LINE 1042 |         )
LINE 1043 |         new_btn = old_btn + (
LINE 1044 |             '        ttk.Button(tb, text="🔎 Buscador", style="Accent.TButton",\n'
LINE 1045 |             '                   command=self.on_open_file_search).pack(side=tk.LEFT, padx=(0, 4))\n'
LINE 1046 |         )
LINE 1047 |         replace_block(mw, old_btn, new_btn, dry_run=dry_run)
LINE 1048 |     else:
LINE 1049 |         log("Botón Buscador ya presente", "SKIP")
LINE 1050 | 
LINE 1051 |     # 5.3 Insertar métodos nuevos (antes de on_copy_clipboard)
LINE 1052 |     mw_text = mw.read_text(encoding="utf-8")
LINE 1053 |     if "def on_open_file_search" not in mw_text:
LINE 1054 |         anchor = "    def on_copy_clipboard(self):"
LINE 1055 |         if anchor in mw_text:
LINE 1056 |             append_block_if_missing(
LINE 1057 |                 mw,
LINE 1058 |                 marker=MARKER_NEW_FILES + "_methods",
LINE 1059 |                 block=MAIN_WINDOW_METHODS_BLOCK,
LINE 1060 |                 dry_run=dry_run,
LINE 1061 |                 position="after_anchor",
LINE 1062 |                 anchor=anchor,
LINE 1063 |             )
LINE 1064 |         else:
LINE 1065 |             log("No se encontró 'on_copy_clipboard' para anclar métodos nuevos", "WARN")
LINE 1066 |     else:
LINE 1067 |         log("Métodos on_open_file_search ya presentes", "SKIP")
LINE 1068 | 
LINE 1069 |     print()
LINE 1070 |     log("=== Proceso finalizado ===", "OK")
LINE 1071 |     if dry_run:
LINE 1072 |         log("Ejecuta sin --dry-run para aplicar realmente los cambios.", "INFO")
LINE 1073 | 
LINE 1074 | 
LINE 1075 | # ---------------------------------------------------------------------------
LINE 1076 | # CLI
LINE 1077 | # ---------------------------------------------------------------------------
LINE 1078 | 
LINE 1079 | def main():
LINE 1080 |     parser = argparse.ArgumentParser(
LINE 1081 |         description="Aplica los cambios del buscador de archivos y árbol de dependencias."
LINE 1082 |     )
LINE 1083 |     parser.add_argument("--root", default=".", help="Directorio raíz del proyecto agente.")
LINE 1084 |     parser.add_argument("--dry-run", action="store_true", help="No modifica nada, solo muestra.")
LINE 1085 |     parser.add_argument("--no-backup", action="store_true", help="No crea respaldos.")
LINE 1086 |     args = parser.parse_args()
LINE 1087 | 
LINE 1088 |     root = Path(args.root).resolve()
LINE 1089 |     if not root.is_dir():
LINE 1090 |         log(f"El directorio no existe: {root}", "ERR")
LINE 1091 |         sys.exit(1)
LINE 1092 | 
LINE 1093 |     apply_changes(
LINE 1094 |         root=root,
LINE 1095 |         dry_run=args.dry_run,
LINE 1096 |         backup=not args.no_backup,
LINE 1097 |     )
LINE 1098 | 
LINE 1099 | 
LINE 1100 | if __name__ == "__main__":
LINE 1101 |     main()
```

==============================================================
FILE: apply_phase1_sqlite.py
==============================================================
```py
LINE   1 | #!/usr/bin/env python3
LINE   2 | # -*- coding: utf-8 -*-
LINE   3 | """
LINE   4 | apply_phase1_sqlite.py
LINE   5 | 
LINE   6 | Aplica la Fase 1 — Persistencia SQLite para nodos — sobre el proyecto
LINE   7 | "agente" (DeepSeek Code Packager).
LINE   8 | 
LINE   9 | Uso:
LINE  10 |     python3 apply_phase1_sqlite.py /ruta/al/proyecto
LINE  11 |     python3 apply_phase1_sqlite.py                 # usa el directorio actual
LINE  12 | 
LINE  13 | Características:
LINE  14 |   * Detecta automáticamente la raíz del proyecto (o la recibe como argumento).
LINE  15 |   * Verifica que los archivos objetivo existan ANTES de modificar nada.
LINE  16 |   * Crea backups en .backup/ preservando la ruta relativa original.
LINE  17 |   * Es idempotente: ejecutarlo dos veces no duplica bloques.
LINE  18 |   * Solo modifica los archivos estrictamente necesarios.
LINE  19 |   * Al finalizar valida la sintaxis con py_compile.
LINE  20 |   * Solo utiliza la biblioteca estándar de Python.
LINE  21 | """
LINE  22 | 
LINE  23 | import argparse
LINE  24 | import os
LINE  25 | import shutil
LINE  26 | import sys
LINE  27 | import py_compile
LINE  28 | from datetime import datetime
LINE  29 | from pathlib import Path
LINE  30 | 
LINE  31 | 
LINE  32 | # ---------------------------------------------------------------------------
LINE  33 | # Constantes
LINE  34 | # ---------------------------------------------------------------------------
LINE  35 | 
LINE  36 | BACKUP_DIRNAME = ".backup"
LINE  37 | 
LINE  38 | STATS = {
LINE  39 |     "modified": 0,
LINE  40 |     "created": 0,
LINE  41 |     "skipped": 0,
LINE  42 |     "backups": 0,
LINE  43 |     "errors": 0,
LINE  44 | }
LINE  45 | 
LINE  46 | 
LINE  47 | # ---------------------------------------------------------------------------
LINE  48 | # Logging
LINE  49 | # ---------------------------------------------------------------------------
LINE  50 | 
LINE  51 | def _log(prefix, msg):
LINE  52 |     print(f"{prefix} {msg}")
LINE  53 | 
LINE  54 | 
LINE  55 | def info(msg):  _log("[INFO]", msg)
LINE  56 | def ok(msg):    _log("[OK]", msg)
LINE  57 | def skip(msg):  _log("[SKIP]", msg)
LINE  58 | def error(msg): _log("[ERROR]", msg); STATS["errors"] += 1
LINE  59 | 
LINE  60 | 
LINE  61 | # ---------------------------------------------------------------------------
LINE  62 | # Helpers de I/O y validación
LINE  63 | # ---------------------------------------------------------------------------
LINE  64 | 
LINE  65 | def ensure_target_exists(root: Path, rel_path: str) -> Path:
LINE  66 |     p = root / rel_path
LINE  67 |     if not p.is_file():
LINE  68 |         raise RuntimeError(f"Archivo objetivo no encontrado: {p}")
LINE  69 |     info(f"Archivo encontrado: {rel_path}")
LINE  70 |     return p
LINE  71 | 
LINE  72 | 
LINE  73 | def backup_file(root: Path, rel_path: str) -> None:
LINE  74 |     src = root / rel_path
LINE  75 |     if not src.is_file():
LINE  76 |         return
LINE  77 |     dst = root / BACKUP_DIRNAME / rel_path
LINE  78 |     dst.parent.mkdir(parents=True, exist_ok=True)
LINE  79 |     shutil.copy2(src, dst)
LINE  80 |     STATS["backups"] += 1
LINE  81 |     info(f"Backup creado: {dst.relative_to(root)}")
LINE  82 | 
LINE  83 | 
LINE  84 | def write_new_file(root: Path, rel_path: str, content: str) -> None:
LINE  85 |     target = root / rel_path
LINE  86 |     if target.exists():
LINE  87 |         existing = target.read_text(encoding="utf-8", errors="ignore")
LINE  88 |         if content.strip() and content.strip() in existing:
LINE  89 |             skip(f"Archivo ya presente y correcto: {rel_path}")
LINE  90 |             STATS["skipped"] += 1
LINE  91 |             return
LINE  92 |         skip(f"Archivo ya existe (no se sobreescribe): {rel_path}")
LINE  93 |         STATS["skipped"] += 1
LINE  94 |         return
LINE  95 |     target.parent.mkdir(parents=True, exist_ok=True)
LINE  96 |     target.write_text(content, encoding="utf-8")
LINE  97 |     STATS["created"] += 1
LINE  98 |     ok(f"Archivo creado: {rel_path}")
LINE  99 | 
LINE 100 | 
LINE 101 | def _apply_change(root: Path, rel_path: str, new_content: str) -> None:
LINE 102 |     backup_file(root, rel_path)
LINE 103 |     (root / rel_path).write_text(new_content, encoding="utf-8")
LINE 104 |     STATS["modified"] += 1
LINE 105 |     ok(f"Cambio aplicado: {rel_path}")
LINE 106 | 
LINE 107 | 
LINE 108 | def insert_after(root: Path, rel_path: str, anchor: str,
LINE 109 |                  block: str, marker: str) -> None:
LINE 110 |     content = (root / rel_path).read_text(encoding="utf-8")
LINE 111 |     if marker in content:
LINE 112 |         skip(f"Cambio ya aplicado: {rel_path} (marcador presente)")
LINE 113 |         STATS["skipped"] += 1
LINE 114 |         return
LINE 115 |     idx = content.find(anchor)
LINE 116 |     if idx == -1:
LINE 117 |         raise RuntimeError(
LINE 118 |             f"Ancla no encontrada en {rel_path}:\n  {anchor!r}"
LINE 119 |         )
LINE 120 |     end = idx + len(anchor)
LINE 121 |     new_content = content[:end] + "\n" + block + content[end:]
LINE 122 |     _apply_change(root, rel_path, new_content)
LINE 123 | 
LINE 124 | 
LINE 125 | def insert_before(root: Path, rel_path: str, anchor: str,
LINE 126 |                   block: str, marker: str) -> None:
LINE 127 |     content = (root / rel_path).read_text(encoding="utf-8")
LINE 128 |     if marker in content:
LINE 129 |         skip(f"Cambio ya aplicado: {rel_path} (marcador presente)")
LINE 130 |         STATS["skipped"] += 1
LINE 131 |         return
LINE 132 |     idx = content.find(anchor)
LINE 133 |     if idx == -1:
LINE 134 |         raise RuntimeError(
LINE 135 |             f"Ancla no encontrada en {rel_path}:\n  {anchor!r}"
LINE 136 |         )
LINE 137 |     new_content = content[:idx] + block + "\n" + content[idx:]
LINE 138 |     _apply_change(root, rel_path, new_content)
LINE 139 | 
LINE 140 | 
LINE 141 | def replace_exact(root: Path, rel_path: str, old: str, new: str) -> None:
LINE 142 |     content = (root / rel_path).read_text(encoding="utf-8")
LINE 143 |     if old not in content:
LINE 144 |         if new in content:
LINE 145 |             skip(f"Reemplazo ya aplicado: {rel_path}")
LINE 146 |         else:
LINE 147 |             skip(f"Patrón no encontrado en {rel_path} (posible versión distinta)")
LINE 148 |         STATS["skipped"] += 1
LINE 149 |         return
LINE 150 |     new_content = content.replace(old, new, 1)
LINE 151 |     _apply_change(root, rel_path, new_content)
LINE 152 | 
LINE 153 | 
LINE 154 | # ---------------------------------------------------------------------------
LINE 155 | # Contenido de archivos nuevos
LINE 156 | # ---------------------------------------------------------------------------
LINE 157 | 
LINE 158 | STORAGE_INIT_PY = '''"""Phase 1 SQLite persistence package."""
LINE 159 | from app.core.storage.database import Database, get_database, default_db_path
LINE 160 | 
LINE 161 | __all__ = ["Database", "get_database", "default_db_path"]
LINE 162 | '''
LINE 163 | 
LINE 164 | 
LINE 165 | DATABASE_PY = '''"""
LINE 166 | SQLite persistence layer for project nodes, metrics and dependencies (Phase 1).
LINE 167 | 
LINE 168 | This module is intentionally restricted to:
LINE 169 |   - Opening / creating the SQLite database.
LINE 170 |   - Initializing the schema.
LINE 171 |   - Executing queries and updates.
LINE 172 |   - Managing transactions.
LINE 173 |   - Providing the CRUD operations required for projects and nodes.
LINE 174 | 
LINE 175 | No Delta Scan or incremental change detection logic is implemented here.
LINE 176 | """
LINE 177 | import os
LINE 178 | import sqlite3
LINE 179 | from typing import Dict, List, Optional, Set, Tuple
LINE 180 | 
LINE 181 | 
LINE 182 | # ---------------------------------------------------------------------------
LINE 183 | # Path resolution
LINE 184 | # ---------------------------------------------------------------------------
LINE 185 | 
LINE 186 | def _find_project_root() -> Optional[str]:
LINE 187 |     """Walk up from this file to find the project root (contains main.py)."""
LINE 188 |     here = os.path.dirname(os.path.abspath(__file__))
LINE 189 |     candidate = os.path.abspath(os.path.join(here, "..", "..", ".."))
LINE 190 |     if os.path.isfile(os.path.join(candidate, "main.py")):
LINE 191 |         return candidate
LINE 192 |     return None
LINE 193 | 
LINE 194 | 
LINE 195 | def default_db_path() -> str:
LINE 196 |     """Resolve project_cache.db path.
LINE 197 | 
LINE 198 |     Prefer <project_root>/.cache/project_cache.db, fallback to
LINE 199 |     ~/.analyzer_app/project_cache.db when the project root cannot be resolved.
LINE 200 |     """
LINE 201 |     root = _find_project_root()
LINE 202 |     if root:
LINE 203 |         return os.path.join(root, ".cache", "project_cache.db")
LINE 204 |     home = os.path.expanduser("~")
LINE 205 |     return os.path.join(home, ".analyzer_app", "project_cache.db")
LINE 206 | 
LINE 207 | 
LINE 208 | # ---------------------------------------------------------------------------
LINE 209 | # Schema
LINE 210 | # ---------------------------------------------------------------------------
LINE 211 | 
LINE 212 | SCHEMA_STATEMENTS = [
LINE 213 |     """CREATE TABLE IF NOT EXISTS projects (
LINE 214 |         id INTEGER PRIMARY KEY AUTOINCREMENT,
LINE 215 |         path TEXT UNIQUE NOT NULL,
LINE 216 |         project_type TEXT,
LINE 217 |         framework TEXT,
LINE 218 |         last_scanned TIMESTAMP DEFAULT CURRENT_TIMESTAMP
LINE 219 |     )""",
LINE 220 |     """CREATE TABLE IF NOT EXISTS nodes (
LINE 221 |         id INTEGER PRIMARY KEY AUTOINCREMENT,
LINE 222 |         project_id INTEGER NOT NULL,
LINE 223 |         rel_path TEXT NOT NULL,
LINE 224 |         parent_path TEXT,
LINE 225 |         is_dir BOOLEAN NOT NULL,
LINE 226 |         mtime REAL NOT NULL,
LINE 227 |         lines_count INTEGER DEFAULT 0,
LINE 228 |         file_size INTEGER DEFAULT 0,
LINE 229 |         is_important BOOLEAN DEFAULT 0,
LINE 230 |         is_checked BOOLEAN DEFAULT 1,
LINE 231 |         FOREIGN KEY(project_id) REFERENCES projects(id) ON DELETE CASCADE,
LINE 232 |         UNIQUE(project_id, rel_path)
LINE 233 |     )""",
LINE 234 |     """CREATE TABLE IF NOT EXISTS node_dependencies (
LINE 235 |         id INTEGER PRIMARY KEY AUTOINCREMENT,
LINE 236 |         source_node_id INTEGER NOT NULL,
LINE 237 |         target_path TEXT NOT NULL,
LINE 238 |         FOREIGN KEY(source_node_id) REFERENCES nodes(id) ON DELETE CASCADE
LINE 239 |     )""",
LINE 240 |     "CREATE INDEX IF NOT EXISTS idx_nodes_rel_path ON nodes(project_id, rel_path)",
LINE 241 |     "CREATE INDEX IF NOT EXISTS idx_nodes_parent ON nodes(project_id, parent_path)",
LINE 242 | ]
LINE 243 | 
LINE 244 | 
LINE 245 | # ---------------------------------------------------------------------------
LINE 246 | # Database
LINE 247 | # ---------------------------------------------------------------------------
LINE 248 | 
LINE 249 | class Database:
LINE 250 |     """Thin SQLite wrapper for the project cache (Phase 1)."""
LINE 251 | 
LINE 252 |     def __init__(self, db_path: Optional[str] = None):
LINE 253 |         self.db_path = db_path or default_db_path()
LINE 254 |         os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
LINE 255 |         self._conn = sqlite3.connect(self.db_path)
LINE 256 |         self._conn.row_factory = sqlite3.Row
LINE 257 |         self._conn.execute("PRAGMA foreign_keys = ON")
LINE 258 |         self._init_schema()
LINE 259 | 
LINE 260 |     def _init_schema(self) -> None:
LINE 261 |         with self._conn:
LINE 262 |             for stmt in SCHEMA_STATEMENTS:
LINE 263 |                 self._conn.execute(stmt)
LINE 264 | 
LINE 265 |     # ---------- projects ----------
LINE 266 | 
LINE 267 |     def get_or_create_project(self, path: str,
LINE 268 |                               project_type: Optional[str] = None,
LINE 269 |                               framework: Optional[str] = None) -> int:
LINE 270 |         cur = self._conn.cursor()
LINE 271 |         cur.execute("SELECT id FROM projects WHERE path = ?", (path,))
LINE 272 |         row = cur.fetchone()
LINE 273 |         if row:
LINE 274 |             return int(row["id"])
LINE 275 |         cur.execute(
LINE 276 |             "INSERT INTO projects (path, project_type, framework) VALUES (?, ?, ?)",
LINE 277 |             (path, project_type, framework),
LINE 278 |         )
LINE 279 |         self._conn.commit()
LINE 280 |         return int(cur.lastrowid)
LINE 281 | 
LINE 282 |     def get_project_by_path(self, path: str) -> Optional[Dict]:
LINE 283 |         cur = self._conn.cursor()
LINE 284 |         cur.execute("SELECT * FROM projects WHERE path = ?", (path,))
LINE 285 |         row = cur.fetchone()
LINE 286 |         return dict(row) if row else None
LINE 287 | 
LINE 288 |     def update_last_scanned(self, project_id: int) -> None:
LINE 289 |         with self._conn:
LINE 290 |             self._conn.execute(
LINE 291 |                 "UPDATE projects SET last_scanned = CURRENT_TIMESTAMP WHERE id = ?",
LINE 292 |                 (project_id,),
LINE 293 |             )
LINE 294 | 
LINE 295 |     def delete_project(self, path: str) -> None:
LINE 296 |         with self._conn:
LINE 297 |             self._conn.execute("DELETE FROM projects WHERE path = ?", (path,))
LINE 298 | 
LINE 299 |     # ---------- nodes ----------
LINE 300 | 
LINE 301 |     def replace_nodes(self, project_id: int, nodes: List[Dict]) -> None:
LINE 302 |         """Delete existing nodes for project and insert the new batch atomically."""
LINE 303 |         rows = [
LINE 304 |             (
LINE 305 |                 project_id,
LINE 306 |                 n["rel_path"],
LINE 307 |                 n.get("parent_path"),
LINE 308 |                 int(bool(n.get("is_dir", 0))),
LINE 309 |                 float(n.get("mtime", 0.0) or 0.0),
LINE 310 |                 int(n.get("lines_count", 0) or 0),
LINE 311 |                 int(n.get("file_size", 0) or 0),
LINE 312 |                 int(bool(n.get("is_important", 0))),
LINE 313 |                 int(bool(n.get("is_checked", 1))),
LINE 314 |             )
LINE 315 |             for n in nodes
LINE 316 |         ]
LINE 317 |         with self._conn:
LINE 318 |             self._conn.execute("DELETE FROM nodes WHERE project_id = ?", (project_id,))
LINE 319 |             if rows:
LINE 320 |                 self._conn.executemany(
LINE 321 |                     """INSERT INTO nodes
LINE 322 |                        (project_id, rel_path, parent_path, is_dir, mtime,
LINE 323 |                         lines_count, file_size, is_important, is_checked)
LINE 324 |                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
LINE 325 |                     rows,
LINE 326 |                 )
LINE 327 | 
LINE 328 |     def get_nodes(self, project_id: int) -> List[Dict]:
LINE 329 |         cur = self._conn.cursor()
LINE 330 |         cur.execute("SELECT * FROM nodes WHERE project_id = ?", (project_id,))
LINE 331 |         return [dict(r) for r in cur.fetchall()]
LINE 332 | 
LINE 333 |     def update_is_checked(self, project_id: int,
LINE 334 |                           rel_path: str, is_checked: bool) -> None:
LINE 335 |         with self._conn:
LINE 336 |             self._conn.execute(
LINE 337 |                 "UPDATE nodes SET is_checked = ? "
LINE 338 |                 "WHERE project_id = ? AND rel_path = ?",
LINE 339 |                 (int(bool(is_checked)), project_id, rel_path),
LINE 340 |             )
LINE 341 | 
LINE 342 |     def update_is_checked_batch(self, project_id: int,
LINE 343 |                                 updates: List[Tuple[str, bool]]) -> None:
LINE 344 |         rows = [(int(bool(c)), project_id, rp) for rp, c in updates]
LINE 345 |         if not rows:
LINE 346 |             return
LINE 347 |         with self._conn:
LINE 348 |             self._conn.executemany(
LINE 349 |                 "UPDATE nodes SET is_checked = ? "
LINE 350 |                 "WHERE project_id = ? AND rel_path = ?",
LINE 351 |                 rows,
LINE 352 |             )
LINE 353 | 
LINE 354 |     def load_checked_state(self, project_path: str) -> Optional[Set[str]]:
LINE 355 |         """Return the set of checked rel_paths (files only).
LINE 356 | 
LINE 357 |         Returns None when there is no persisted data for this project,
LINE 358 |         so the caller can distinguish "never saved" from "all unchecked".
LINE 359 |         """
LINE 360 |         cur = self._conn.cursor()
LINE 361 |         cur.execute("SELECT id FROM projects WHERE path = ?", (project_path,))
LINE 362 |         row = cur.fetchone()
LINE 363 |         if not row:
LINE 364 |             return None
LINE 365 |         project_id = int(row["id"])
LINE 366 |         cur.execute(
LINE 367 |             "SELECT rel_path, is_checked FROM nodes "
LINE 368 |             "WHERE project_id = ? AND is_dir = 0",
LINE 369 |             (project_id,),
LINE 370 |         )
LINE 371 |         rows = cur.fetchall()
LINE 372 |         if not rows:
LINE 373 |             return None
LINE 374 |         return {r["rel_path"] for r in rows if r["is_checked"]}
LINE 375 | 
LINE 376 |     def delete_nodes(self, project_id: int) -> None:
LINE 377 |         with self._conn:
LINE 378 |             self._conn.execute("DELETE FROM nodes WHERE project_id = ?", (project_id,))
LINE 379 | 
LINE 380 |     # ---------- dependencies ----------
LINE 381 | 
LINE 382 |     def save_dependencies_batch(self, project_id: int,
LINE 383 |                                 deps: List[Tuple[str, str]]) -> None:
LINE 384 |         """deps: list of (source_rel_path, target_path)."""
LINE 385 |         if not deps:
LINE 386 |             return
LINE 387 |         cur = self._conn.cursor()
LINE 388 |         cur.execute("SELECT id, rel_path FROM nodes WHERE project_id = ?", (project_id,))
LINE 389 |         id_map = {r["rel_path"]: int(r["id"]) for r in cur.fetchall()}
LINE 390 | 
LINE 391 |         rows = []
LINE 392 |         for src_rel, target in deps:
LINE 393 |             node_id = id_map.get(src_rel)
LINE 394 |             if node_id is None:
LINE 395 |                 continue
LINE 396 |             rows.append((node_id, target))
LINE 397 | 
LINE 398 |         with self._conn:
LINE 399 |             self._conn.execute(
LINE 400 |                 """DELETE FROM node_dependencies
LINE 401 |                    WHERE source_node_id IN
LINE 402 |                          (SELECT id FROM nodes WHERE project_id = ?)""",
LINE 403 |                 (project_id,),
LINE 404 |             )
LINE 405 |             if rows:
LINE 406 |                 self._conn.executemany(
LINE 407 |                     "INSERT INTO node_dependencies (source_node_id, target_path) "
LINE 408 |                     "VALUES (?, ?)",
LINE 409 |                     rows,
LINE 410 |                 )
LINE 411 | 
LINE 412 |     def get_dependencies(self, project_id: int) -> List[Dict]:
LINE 413 |         cur = self._conn.cursor()
LINE 414 |         cur.execute(
LINE 415 |             """SELECT n.rel_path AS source_path, d.target_path AS target_path
LINE 416 |                FROM node_dependencies d
LINE 417 |                JOIN nodes n ON n.id = d.source_node_id
LINE 418 |                WHERE n.project_id = ?""",
LINE 419 |             (project_id,),
LINE 420 |         )
LINE 421 |         return [dict(r) for r in cur.fetchall()]
LINE 422 | 
LINE 423 |     def close(self) -> None:
LINE 424 |         try:
LINE 425 |             self._conn.close()
LINE 426 |         except Exception:
LINE 427 |             pass
LINE 428 | 
LINE 429 | 
LINE 430 | # ---------------------------------------------------------------------------
LINE 431 | # Singleton accessor
LINE 432 | # ---------------------------------------------------------------------------
LINE 433 | 
LINE 434 | _db_singleton: Optional[Database] = None
LINE 435 | 
LINE 436 | 
LINE 437 | def get_database(db_path: Optional[str] = None) -> Database:
LINE 438 |     """Return the process-wide Database singleton."""
LINE 439 |     global _db_singleton
LINE 440 |     if _db_singleton is None or (db_path and db_path != _db_singleton.db_path):
LINE 441 |         _db_singleton = Database(db_path)
LINE 442 |     return _db_singleton
LINE 443 | 
LINE 444 | 
LINE 445 | def reset_database_singleton() -> None:
LINE 446 |     """For tests: close and drop the current singleton."""
LINE 447 |     global _db_singleton
LINE 448 |     if _db_singleton is not None:
LINE 449 |         _db_singleton.close()
LINE 450 |     _db_singleton = None
LINE 451 | '''
LINE 452 | 
LINE 453 | 
LINE 454 | # ---------------------------------------------------------------------------
LINE 455 | # Bloques a insertar en archivos existentes
LINE 456 | # ---------------------------------------------------------------------------
LINE 457 | 
LINE 458 | # --- ProjectAnalyzer.persist_result -----------------------------------------
LINE 459 | 
LINE 460 | PERSIST_RESULT_BLOCK = '''    # === PERSISTENCE: PHASE1 (persist_result) ===
LINE 461 |     def persist_result(self, result) -> None:
LINE 462 |         """Persist a ProjectAnalysisResult to the SQLite cache (Phase 1).
LINE 463 | 
LINE 464 |         This method is additive and does not modify the existing analyze()
LINE 465 |         pipeline, its return type, or FileMetric structure.
LINE 466 |         """
LINE 467 |         try:
LINE 468 |             from app.core.storage.database import get_database
LINE 469 |         except Exception:
LINE 470 |             return
LINE 471 | 
LINE 472 |         folder = getattr(result, "folder_path", None)
LINE 473 |         if not folder or not os.path.isdir(folder):
LINE 474 |             return
LINE 475 | 
LINE 476 |         try:
LINE 477 |             db = get_database()
LINE 478 |         except Exception:
LINE 479 |             return
LINE 480 | 
LINE 481 |         project_id = db.get_or_create_project(
LINE 482 |             path=folder,
LINE 483 |             project_type=getattr(result, "primary_language", None),
LINE 484 |             framework=getattr(result, "framework", None),
LINE 485 |         )
LINE 486 | 
LINE 487 |         # Preserve previously persisted is_checked state
LINE 488 |         existing_checked = db.load_checked_state(folder)
LINE 489 | 
LINE 490 |         important = set(getattr(result, "important_files", []) or [])
LINE 491 |         nodes = []
LINE 492 | 
LINE 493 |         for dirpath, dirnames, filenames in os.walk(folder):
LINE 494 |             dirnames[:] = [d for d in dirnames if d not in self.excluded_dirs]
LINE 495 |             rel_dir = os.path.relpath(dirpath, folder)
LINE 496 | 
LINE 497 |             if rel_dir != ".":
LINE 498 |                 rel_norm = rel_dir.replace("\\\\", "/")
LINE 499 |                 parent = os.path.dirname(rel_norm).replace("\\\\", "/") or None
LINE 500 |                 try:
LINE 501 |                     mtime = float(os.stat(dirpath).st_mtime)
LINE 502 |                 except Exception:
LINE 503 |                     mtime = 0.0
LINE 504 |                 nodes.append({
LINE 505 |                     "rel_path": rel_norm,
LINE 506 |                     "parent_path": parent,
LINE 507 |                     "is_dir": 1,
LINE 508 |                     "mtime": mtime,
LINE 509 |                     "lines_count": 0,
LINE 510 |                     "file_size": 0,
LINE 511 |                     "is_important": 0,
LINE 512 |                     "is_checked": 0,
LINE 513 |                 })
LINE 514 | 
LINE 515 |             for f in filenames:
LINE 516 |                 full = os.path.join(dirpath, f)
LINE 517 |                 if is_binary_file(full):
LINE 518 |                     continue
LINE 519 |                 rel_file = f if rel_dir == "." else os.path.join(rel_dir, f)
LINE 520 |                 rel_file = rel_file.replace("\\\\", "/")
LINE 521 |                 try:
LINE 522 |                     st = os.stat(full)
LINE 523 |                     mtime = float(st.st_mtime)
LINE 524 |                     size = int(st.st_size)
LINE 525 |                 except Exception:
LINE 526 |                     mtime = 0.0
LINE 527 |                     size = 0
LINE 528 |                 parent = os.path.dirname(rel_file).replace("\\\\", "/") or None
LINE 529 | 
LINE 530 |                 if existing_checked is None:
LINE 531 |                     is_checked = 1
LINE 532 |                 else:
LINE 533 |                     is_checked = 1 if rel_file in existing_checked else 0
LINE 534 | 
LINE 535 |                 nodes.append({
LINE 536 |                     "rel_path": rel_file,
LINE 537 |                     "parent_path": parent,
LINE 538 |                     "is_dir": 0,
LINE 539 |                     "mtime": mtime,
LINE 540 |                     "lines_count": 0,
LINE 541 |                     "file_size": size,
LINE 542 |                     "is_important": 1 if rel_file in important else 0,
LINE 543 |                     "is_checked": is_checked,
LINE 544 |                 })
LINE 545 | 
LINE 546 |         try:
LINE 547 |             db.replace_nodes(project_id, nodes)
LINE 548 | 
LINE 549 |             dep_pairs = []
LINE 550 |             code_deps = getattr(result, "code_dependencies", {}) or {}
LINE 551 |             for rel_path, deps in code_deps.items():
LINE 552 |                 for d in deps:
LINE 553 |                     dep_pairs.append((rel_path, d))
LINE 554 |             db.save_dependencies_batch(project_id, dep_pairs)
LINE 555 | 
LINE 556 |             db.update_last_scanned(project_id)
LINE 557 |         except Exception:
LINE 558 |             pass
LINE 559 |     # === END PERSISTENCE: PHASE1 (persist_result) ===
LINE 560 | '''
LINE 561 | 
LINE 562 | 
LINE 563 | # --- CheckboxTreeview -------------------------------------------------------
LINE 564 | 
LINE 565 | FILE_TREE_ATTRS_BLOCK = '''        # === PERSISTENCE: PHASE1 (attrs) ===
LINE 566 |         self._on_check_change = None
LINE 567 |         # === END PERSISTENCE: PHASE1 (attrs) ===
LINE 568 | '''
LINE 569 | 
LINE 570 | FILE_TREE_METHODS_BLOCK = '''    # === PERSISTENCE: PHASE1 (methods) ===
LINE 571 |     def set_check_change_callback(self, callback) -> None:
LINE 572 |         """Register callback(rel_path: str, is_checked: bool) for persistence."""
LINE 573 |         self._on_check_change = callback
LINE 574 | 
LINE 575 |     def _notify_check_change(self, rel_path: str, is_checked: bool) -> None:
LINE 576 |         if not self._on_check_change or not rel_path:
LINE 577 |             return
LINE 578 |         try:
LINE 579 |             self._on_check_change(rel_path, is_checked)
LINE 580 |         except Exception:
LINE 581 |             pass
LINE 582 |     # === END PERSISTENCE: PHASE1 (methods) ===
LINE 583 | '''
LINE 584 | 
LINE 585 | 
LINE 586 | FILE_TREE_CHECK_OLD = '''    def check_item(self, item):
LINE 587 |         rel_path = self.set(item, "name")
LINE 588 |         if rel_path:
LINE 589 |             self.set(item, "check", "☑")
LINE 590 |             self.item(item, tags=("checked",))
LINE 591 |             if not self.get_children(item):
LINE 592 |                 self.checked_items.add(rel_path)
LINE 593 |         for child in self.get_children(item):
LINE 594 |             self.check_item(child)
LINE 595 | '''
LINE 596 | 
LINE 597 | FILE_TREE_CHECK_NEW = '''    def check_item(self, item):
LINE 598 |         rel_path = self.set(item, "name")
LINE 599 |         if rel_path:
LINE 600 |             was_checked = rel_path in self.checked_items
LINE 601 |             self.set(item, "check", "☑")
LINE 602 |             self.item(item, tags=("checked",))
LINE 603 |             if not self.get_children(item):
LINE 604 |                 self.checked_items.add(rel_path)
LINE 605 |                 if not was_checked:
LINE 606 |                     self._notify_check_change(rel_path, True)
LINE 607 |         for child in self.get_children(item):
LINE 608 |             self.check_item(child)
LINE 609 | '''
LINE 610 | 
LINE 611 | 
LINE 612 | FILE_TREE_UNCHECK_OLD = '''    def uncheck_item(self, item):
LINE 613 |         rel_path = self.set(item, "name")
LINE 614 |         if rel_path:
LINE 615 |             self.set(item, "check", "☐")
LINE 616 |             self.item(item, tags=("unchecked",))
LINE 617 |             if rel_path in self.checked_items:
LINE 618 |                 self.checked_items.remove(rel_path)
LINE 619 |         for child in self.get_children(item):
LINE 620 |             self.uncheck_item(child)
LINE 621 | '''
LINE 622 | 
LINE 623 | FILE_TREE_UNCHECK_NEW = '''    def uncheck_item(self, item):
LINE 624 |         rel_path = self.set(item, "name")
LINE 625 |         if rel_path:
LINE 626 |             was_checked = rel_path in self.checked_items
LINE 627 |             self.set(item, "check", "☐")
LINE 628 |             self.item(item, tags=("unchecked",))
LINE 629 |             if rel_path in self.checked_items:
LINE 630 |                 self.checked_items.remove(rel_path)
LINE 631 |             if was_checked:
LINE 632 |                 self._notify_check_change(rel_path, False)
LINE 633 |         for child in self.get_children(item):
LINE 634 |             self.uncheck_item(child)
LINE 635 | '''
LINE 636 | 
LINE 637 | 
LINE 638 | # --- MainWindow -------------------------------------------------------------
LINE 639 | 
LINE 640 | MW_IMPORT_BLOCK = '''# === PERSISTENCE: PHASE1 (imports) ===
LINE 641 | from app.core.storage.database import get_database
LINE 642 | # === END PERSISTENCE: PHASE1 (imports) ===
LINE 643 | '''
LINE 644 | 
LINE 645 | MW_INIT_BLOCK = '''        # === PERSISTENCE: PHASE1 (init) ===
LINE 646 |         self._persist_db = None
LINE 647 |         try:
LINE 648 |             self._persist_db = get_database()
LINE 649 |         except Exception:
LINE 650 |             self._persist_db = None
LINE 651 |         # === END PERSISTENCE: PHASE1 (init) ===
LINE 652 | '''
LINE 653 | 
LINE 654 | MW_CALLBACK_BLOCK = '''        # === PERSISTENCE: PHASE1 (callback) ===
LINE 655 |         if self._persist_db is not None:
LINE 656 |             self.tree.set_check_change_callback(self._on_tree_check_change)
LINE 657 |         # === END PERSISTENCE: PHASE1 (callback) ===
LINE 658 | '''
LINE 659 | 
LINE 660 | MW_METHOD_BLOCK = '''    # === PERSISTENCE: PHASE1 (method) ===
LINE 661 |     def _on_tree_check_change(self, rel_path: str, is_checked: bool):
LINE 662 |         """Persist checkbox changes to SQLite (Phase 1)."""
LINE 663 |         if self._persist_db is None:
LINE 664 |             return
LINE 665 |         folder = self.var_folder.get()
LINE 666 |         if not folder:
LINE 667 |             return
LINE 668 |         try:
LINE 669 |             project_id = self._persist_db.get_or_create_project(folder)
LINE 670 |             self._persist_db.update_is_checked(project_id, rel_path, is_checked)
LINE 671 |         except Exception:
LINE 672 |             pass
LINE 673 |     # === END PERSISTENCE: PHASE1 (method) ===
LINE 674 | '''
LINE 675 | 
LINE 676 | MW_RELOAD_BLOCK = '''        # === PERSISTENCE: PHASE1 (reload) ===
LINE 677 |         if self._persist_db is not None:
LINE 678 |             try:
LINE 679 |                 saved = self._persist_db.load_checked_state(folder)
LINE 680 |                 if saved is not None:
LINE 681 |                     self.tree.set_checked_files(saved)
LINE 682 |                     self.selector.set_checked_folder_files(
LINE 683 |                         self.tree.get_checked_files()
LINE 684 |                     )
LINE 685 |             except Exception:
LINE 686 |                 pass
LINE 687 |         # === END PERSISTENCE: PHASE1 (reload) ===
LINE 688 | '''
LINE 689 | 
LINE 690 | MW_ANALYZE_BLOCK = '''        # === PERSISTENCE: PHASE1 (analyze) ===
LINE 691 |         try:
LINE 692 |             analyzer.persist_result(result)
LINE 693 |         except Exception:
LINE 694 |             pass
LINE 695 |         # === END PERSISTENCE: PHASE1 (analyze) ===
LINE 696 | '''
LINE 697 | 
LINE 698 | 
LINE 699 | # ---------------------------------------------------------------------------
LINE 700 | # Aplicación de cambios
LINE 701 | # ---------------------------------------------------------------------------
LINE 702 | 
LINE 703 | REQUIRED_FILES = [
LINE 704 |     "app/__init__.py",
LINE 705 |     "app/core/__init__.py",
LINE 706 |     "app/core/project_analyzer.py",
LINE 707 |     "app/gui/file_tree.py",
LINE 708 |     "app/gui/main_window.py",
LINE 709 |     "app/models/project.py",
LINE 710 |     "main.py",
LINE 711 | ]
LINE 712 | 
LINE 713 | 
LINE 714 | def verify_structure(root: Path) -> None:
LINE 715 |     info(f"Proyecto detectado: {root}")
LINE 716 |     missing = []
LINE 717 |     for rel in REQUIRED_FILES:
LINE 718 |         p = root / rel
LINE 719 |         if not p.is_file():
LINE 720 |             missing.append(rel)
LINE 721 |     if missing:
LINE 722 |         for m in missing:
LINE 723 |             error(f"Falta archivo requerido: {m}")
LINE 724 |         raise RuntimeError(
LINE 725 |             "La estructura del proyecto no coincide con la esperada. "
LINE 726 |             "Abortando sin modificar archivos."
LINE 727 |         )
LINE 728 | 
LINE 729 | 
LINE 730 | def apply_all(root: Path) -> None:
LINE 731 |     info("--- Verificando estructura del proyecto ---")
LINE 732 |     verify_structure(root)
LINE 733 | 
LINE 734 |     info("--- Creando archivos nuevos ---")
LINE 735 |     write_new_file(root, "app/core/storage/__init__.py", STORAGE_INIT_PY)
LINE 736 |     write_new_file(root, "app/core/storage/database.py", DATABASE_PY)
LINE 737 | 
LINE 738 |     info("--- Modificando app/core/project_analyzer.py ---")
LINE 739 |     ensure_target_exists(root, "app/core/project_analyzer.py")
LINE 740 |     insert_before(
LINE 741 |         root, "app/core/project_analyzer.py",
LINE 742 |         anchor="    def _is_entry_point(self, rel_path: str) -> bool:",
LINE 743 |         block=PERSIST_RESULT_BLOCK,
LINE 744 |         marker="# === PERSISTENCE: PHASE1 (persist_result) ===",
LINE 745 |     )
LINE 746 | 
LINE 747 |     info("--- Modificando app/gui/file_tree.py ---")
LINE 748 |     ensure_target_exists(root, "app/gui/file_tree.py")
LINE 749 |     insert_after(
LINE 750 |         root, "app/gui/file_tree.py",
LINE 751 |         anchor="        self.checked_items: Set[str] = set()",
LINE 752 |         block=FILE_TREE_ATTRS_BLOCK,
LINE 753 |         marker="# === PERSISTENCE: PHASE1 (attrs) ===",
LINE 754 |     )
LINE 755 |     insert_before(
LINE 756 |         root, "app/gui/file_tree.py",
LINE 757 |         anchor="    def insert_file(self, parent, rel_path: str, is_checked: bool = True):",
LINE 758 |         block=FILE_TREE_METHODS_BLOCK,
LINE 759 |         marker="# === PERSISTENCE: PHASE1 (methods) ===",
LINE 760 |     )
LINE 761 |     replace_exact(root, "app/gui/file_tree.py",
LINE 762 |                   FILE_TREE_CHECK_OLD, FILE_TREE_CHECK_NEW)
LINE 763 |     replace_exact(root, "app/gui/file_tree.py",
LINE 764 |                   FILE_TREE_UNCHECK_OLD, FILE_TREE_UNCHECK_NEW)
LINE 765 | 
LINE 766 |     info("--- Modificando app/gui/main_window.py ---")
LINE 767 |     ensure_target_exists(root, "app/gui/main_window.py")
LINE 768 | 
LINE 769 |     # 1. Import
LINE 770 |     insert_after(
LINE 771 |         root, "app/gui/main_window.py",
LINE 772 |         anchor=("from app.gui.dependency_tree_dialog import DependencyTreeDialog\n"
LINE 773 |                 "# === END AUTO-GENERATED ==="),
LINE 774 |         block=MW_IMPORT_BLOCK,
LINE 775 |         marker="# === PERSISTENCE: PHASE1 (imports) ===",
LINE 776 |     )
LINE 777 | 
LINE 778 |     # 2. Init del estado de persistencia
LINE 779 |     insert_after(
LINE 780 |         root, "app/gui/main_window.py",
LINE 781 |         anchor="        self.config     = ExportConfig()",
LINE 782 |         block=MW_INIT_BLOCK,
LINE 783 |         marker="# === PERSISTENCE: PHASE1 (init) ===",
LINE 784 |     )
LINE 785 | 
LINE 786 |     # 3. Registrar callback en el árbol
LINE 787 |     insert_after(
LINE 788 |         root, "app/gui/main_window.py",
LINE 789 |         anchor=('        self.tree.bind("<ButtonRelease-1>",  '
LINE 790 |                 'lambda _: self.root.after(50, self._refresh_selection_stats))'),
LINE 791 |         block=MW_CALLBACK_BLOCK,
LINE 792 |         marker="# === PERSISTENCE: PHASE1 (callback) ===",
LINE 793 |     )
LINE 794 | 
LINE 795 |     # 4. Insertar método _on_tree_check_change antes del bloque de handlers
LINE 796 |     insert_before(
LINE 797 |         root, "app/gui/main_window.py",
LINE 798 |         anchor=("    # ── UI event handlers "
LINE 799 |                 "────────────────────────────────────────────────"
LINE 800 |                 "─────────────────"),
LINE 801 |         block=MW_METHOD_BLOCK,
LINE 802 |         marker="# === PERSISTENCE: PHASE1 (method) ===",
LINE 803 |     )
LINE 804 | 
LINE 805 |     # 5. Restaurar estado al recargar el árbol
LINE 806 |     insert_after(
LINE 807 |         root, "app/gui/main_window.py",
LINE 808 |         anchor=('                rel_file = os.path.join(rel_dir, f) '
LINE 809 |                 'if rel_dir != "." else f\n'
LINE 810 |                 '                self.tree.insert_file(parent_item, rel_file)'),
LINE 811 |         block=MW_RELOAD_BLOCK,
LINE 812 |         marker="# === PERSISTENCE: PHASE1 (reload) ===",
LINE 813 |     )
LINE 814 | 
LINE 815 |     # 6. Persistir tras el análisis
LINE 816 |     insert_after(
LINE 817 |         root, "app/gui/main_window.py",
LINE 818 |         anchor=("        result = analyzer.analyze(folder, "
LINE 819 |                 "max_file_size_mb=max_file_mb)"),
LINE 820 |         block=MW_ANALYZE_BLOCK,
LINE 821 |         marker="# === PERSISTENCE: PHASE1 (analyze) ===",
LINE 822 |     )
LINE 823 | 
LINE 824 | 
LINE 825 | # ---------------------------------------------------------------------------
LINE 826 | # Validación final
LINE 827 | # ---------------------------------------------------------------------------
LINE 828 | 
LINE 829 | def validate_syntax(root: Path, rel_paths) -> None:
LINE 830 |     info("--- Validando sintaxis (py_compile) ---")
LINE 831 |     for rel in rel_paths:
LINE 832 |         full = root / rel
LINE 833 |         if not full.is_file():
LINE 834 |             continue
LINE 835 |         try:
LINE 836 |             py_compile.compile(str(full), doraise=True)
LINE 837 |             info(f"Sintaxis OK: {rel}")
LINE 838 |         except py_compile.PyCompileError as exc:
LINE 839 |             error(f"Sintaxis inválida en {rel}: {exc}")
LINE 840 | 
LINE 841 | 
LINE 842 | # ---------------------------------------------------------------------------
LINE 843 | # CLI
LINE 844 | # ---------------------------------------------------------------------------
LINE 845 | 
LINE 846 | def build_parser() -> argparse.ArgumentParser:
LINE 847 |     p = argparse.ArgumentParser(
LINE 848 |         description="Aplica la Fase 1 (persistencia SQLite) al proyecto agente."
LINE 849 |     )
LINE 850 |     p.add_argument(
LINE 851 |         "project_root", nargs="?", default=".",
LINE 852 |         help="Ruta raíz del proyecto (por defecto: directorio actual).",
LINE 853 |     )
LINE 854 |     return p
LINE 855 | 
LINE 856 | 
LINE 857 | def main() -> int:
LINE 858 |     parser = build_parser()
LINE 859 |     args = parser.parse_args()
LINE 860 | 
LINE 861 |     try:
LINE 862 |         root = Path(args.project_root).resolve()
LINE 863 |     except Exception as exc:
LINE 864 |         error(f"Ruta inválida: {exc}")
LINE 865 |         return 1
LINE 866 | 
LINE 867 |     if not root.is_dir():
LINE 868 |         error(f"El directorio no existe: {root}")
LINE 869 |         return 1
LINE 870 | 
LINE 871 |     print(f"[INFO] Proyecto detectado: {root}")
LINE 872 |     print(f"[INFO] Inicio: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
LINE 873 |     print()
LINE 874 | 
LINE 875 |     try:
LINE 876 |         apply_all(root)
LINE 877 |     except Exception as exc:
LINE 878 |         error(str(exc))
LINE 879 |         print()
LINE 880 |         info("Proceso detenido. No se continúan aplicando cambios.")
LINE 881 |         _print_summary()
LINE 882 |         return 1
LINE 883 | 
LINE 884 |     print()
LINE 885 |     info("--- Resumen final ---")
LINE 886 |     _print_summary()
LINE 887 | 
LINE 888 |     # Validación sintáctica
LINE 889 |     validate_syntax(root, [
LINE 890 |         "app/core/storage/__init__.py",
LINE 891 |         "app/core/storage/database.py",
LINE 892 |         "app/core/project_analyzer.py",
LINE 893 |         "app/gui/file_tree.py",
LINE 894 |         "app/gui/main_window.py",
LINE 895 |     ])
LINE 896 | 
LINE 897 |     print()
LINE 898 |     info("Fase 1 aplicada. Reinicia la aplicación para probar.")
LINE 899 |     return 0 if STATS["errors"] == 0 else 1
LINE 900 | 
LINE 901 | 
LINE 902 | def _print_summary() -> None:
LINE 903 |     print(f"Archivos modificados: {STATS['modified']}")
LINE 904 |     print(f"Archivos creados: {STATS['created']}")
LINE 905 |     print(f"Archivos omitidos: {STATS['skipped']}")
LINE 906 |     print(f"Backups creados: {STATS['backups']}")
LINE 907 |     print(f"Errores: {STATS['errors']}")
LINE 908 | 
LINE 909 | 
LINE 910 | if __name__ == "__main__":
LINE 911 |     sys.exit(main())
```

==============================================================
FILE: apply_phase2_delta_scan.py
==============================================================
```py
LINE   1 | #!/usr/bin/env python3
LINE   2 | # -*- coding: utf-8 -*-
LINE   3 | """
LINE   4 | apply_phase2_delta_scan.py — Aplica Fase 2 (Delta Scan + caché) sobre el
LINE   5 | proyecto "agente".
LINE   6 | 
LINE   7 | Uso:
LINE   8 |     python3 apply_phase2_delta_scan.py /ruta/al/proyecto
LINE   9 | 
LINE  10 | Idempotente. Backups en .backup/. Valida sintaxis con py_compile.
LINE  11 | """
LINE  12 | import argparse, py_compile, shutil, sys
LINE  13 | from datetime import datetime
LINE  14 | from pathlib import Path
LINE  15 | 
LINE  16 | BACKUP = ".backup"
LINE  17 | ROOT_FILES = [
LINE  18 |     "app/__init__.py",
LINE  19 |     "app/core/project_analyzer.py",
LINE  20 |     "app/core/storage/database.py",
LINE  21 |     "app/gui/main_window.py",
LINE  22 | ]
LINE  23 | 
LINE  24 | def log(lvl, msg): print(f"[{lvl}] {msg}")
LINE  25 | def backup(root: Path, rel: str) -> None:
LINE  26 |     src = root / rel
LINE  27 |     if not src.is_file(): return
LINE  28 |     dst = root / BACKUP / rel
LINE  29 |     dst.parent.mkdir(parents=True, exist_ok=True)
LINE  30 |     shutil.copy2(src, dst)
LINE  31 |     log("INFO", f"Backup creado: {dst.relative_to(root)}")
LINE  32 | 
LINE  33 | def insert_after(root: Path, rel: str, anchor: str, block: str, marker: str):
LINE  34 |     p = root / rel
LINE  35 |     txt = p.read_text(encoding="utf-8")
LINE  36 |     if marker in txt:
LINE  37 |         log("SKIP", f"Ya aplicado: {rel} ({marker.strip()})"); return
LINE  38 |     i = txt.find(anchor)
LINE  39 |     if i == -1:
LINE  40 |         raise RuntimeError(f"Ancla no encontrada en {rel}:\n  {anchor!r}")
LINE  41 |     e = i + len(anchor)
LINE  42 |     backup(root, rel)
LINE  43 |     p.write_text(txt[:e] + "\n" + block + txt[e:], encoding="utf-8")
LINE  44 |     log("OK", f"Cambio aplicado: {rel}  ({marker.strip()})")
LINE  45 | 
LINE  46 | def insert_before(root: Path, rel: str, anchor: str, block: str, marker: str):
LINE  47 |     p = root / rel
LINE  48 |     txt = p.read_text(encoding="utf-8")
LINE  49 |     if marker in txt:
LINE  50 |         log("SKIP", f"Ya aplicado: {rel} ({marker.strip()})"); return
LINE  51 |     i = txt.find(anchor)
LINE  52 |     if i == -1:
LINE  53 |         raise RuntimeError(f"Ancla no encontrada en {rel}:\n  {anchor!r}")
LINE  54 |     backup(root, rel)
LINE  55 |     p.write_text(txt[:i] + block + "\n" + txt[i:], encoding="utf-8")
LINE  56 |     log("OK", f"Cambio aplicado: {rel}  ({marker.strip()})")
LINE  57 | 
LINE  58 | # --- bloques ---
LINE  59 | 
LINE  60 | DB_WAL_OLD = '''        self._conn = sqlite3.connect(self.db_path)
LINE  61 |         self._conn.row_factory = sqlite3.Row
LINE  62 |         self._conn.execute("PRAGMA foreign_keys = ON")
LINE  63 |         self._init_schema()'''
LINE  64 | 
LINE  65 | DB_WAL_NEW = '''        self._conn = sqlite3.connect(self.db_path, timeout=10.0)
LINE  66 |         self._conn.row_factory = sqlite3.Row
LINE  67 |         self._conn.execute("PRAGMA foreign_keys = ON")
LINE  68 |         self._conn.execute("PRAGMA journal_mode = WAL")
LINE  69 |         self._conn.execute("PRAGMA synchronous = NORMAL")
LINE  70 |         self._init_schema()'''
LINE  71 | 
LINE  72 | DB_DELTA_BLOCK = '''    # === PHASE 2: DELTA SCAN ===
LINE  73 |     def load_nodes_map(self, project_path: str):
LINE  74 |         cur = self._conn.cursor()
LINE  75 |         cur.execute("SELECT id FROM projects WHERE path = ?", (project_path,))
LINE  76 |         row = cur.fetchone()
LINE  77 |         if not row:
LINE  78 |             return None
LINE  79 |         project_id = int(row["id"])
LINE  80 |         cur.execute(
LINE  81 |             "SELECT id, rel_path, parent_path, is_dir, mtime, lines_count, "
LINE  82 |             "file_size, is_important, is_checked FROM nodes WHERE project_id = ?",
LINE  83 |             (project_id,),
LINE  84 |         )
LINE  85 |         return {r["rel_path"]: dict(r) for r in cur.fetchall()}
LINE  86 | 
LINE  87 |     def apply_delta(self, project_id, to_insert, to_update,
LINE  88 |                     to_delete_paths, dep_pairs):
LINE  89 |         if to_delete_paths:
LINE  90 |             with self._conn:
LINE  91 |                 self._conn.executemany(
LINE  92 |                     "DELETE FROM nodes WHERE project_id = ? AND rel_path = ?",
LINE  93 |                     [(project_id, rp) for rp in to_delete_paths],
LINE  94 |                 )
LINE  95 |         if to_update:
LINE  96 |             with self._conn:
LINE  97 |                 self._conn.executemany(
LINE  98 |                     """UPDATE nodes SET mtime=?, lines_count=?, file_size=?,
LINE  99 |                                        is_important=?
LINE 100 |                        WHERE project_id=? AND rel_path=?""",
LINE 101 |                     [(n["mtime"], n["lines_count"], n["file_size"],
LINE 102 |                       int(bool(n.get("is_important", 0))),
LINE 103 |                       project_id, n["rel_path"]) for n in to_update],
LINE 104 |                 )
LINE 105 |         if to_insert:
LINE 106 |             with self._conn:
LINE 107 |                 self._conn.executemany(
LINE 108 |                     """INSERT INTO nodes
LINE 109 |                        (project_id, rel_path, parent_path, is_dir, mtime,
LINE 110 |                         lines_count, file_size, is_important, is_checked)
LINE 111 |                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
LINE 112 |                     [(project_id, n["rel_path"], n.get("parent_path"),
LINE 113 |                       int(bool(n.get("is_dir", 0))),
LINE 114 |                       float(n.get("mtime", 0.0)),
LINE 115 |                       int(n.get("lines_count", 0) or 0),
LINE 116 |                       int(n.get("file_size", 0) or 0),
LINE 117 |                       int(bool(n.get("is_important", 0))),
LINE 118 |                       int(bool(n.get("is_checked", 1))))
LINE 119 |                      for n in to_insert],
LINE 120 |                 )
LINE 121 |         if to_update or to_insert or to_delete_paths:
LINE 122 |             with self._conn:
LINE 123 |                 pairs = ([(project_id, n["rel_path"]) for n in to_update] +
LINE 124 |                          [(project_id, n["rel_path"]) for n in to_insert] +
LINE 125 |                          [(project_id, rp) for rp in to_delete_paths])
LINE 126 |                 self._conn.executemany(
LINE 127 |                     """DELETE FROM node_dependencies
LINE 128 |                        WHERE source_node_id IN
LINE 129 |                          (SELECT id FROM nodes WHERE project_id=? AND rel_path=?)""",
LINE 130 |                     pairs,
LINE 131 |                 )
LINE 132 |                 if dep_pairs:
LINE 133 |                     cur = self._conn.cursor()
LINE 134 |                     cur.execute(
LINE 135 |                         "SELECT id, rel_path FROM nodes WHERE project_id=?",
LINE 136 |                         (project_id,))
LINE 137 |                     id_map = {r["rel_path"]: int(r["id"])
LINE 138 |                               for r in cur.fetchall()}
LINE 139 |                     rows = [(id_map[s], t) for s, t in dep_pairs if s in id_map]
LINE 140 |                     if rows:
LINE 141 |                         self._conn.executemany(
LINE 142 |                             "INSERT INTO node_dependencies "
LINE 143 |                             "(source_node_id, target_path) VALUES (?, ?)",
LINE 144 |                             rows,
LINE 145 |                         )
LINE 146 |         self.update_last_scanned(project_id)
LINE 147 |     # === END PHASE 2 ===
LINE 148 | '''
LINE 149 | 
LINE 150 | MW_DEBOUNCE_INIT = '''        # === PHASE 2: DEBOUNCE CHECKBOX ===
LINE 151 |         self._pending_checks = {}
LINE 152 |         self._flush_timer = None
LINE 153 |         # === END PHASE 2 ===
LINE 154 | '''
LINE 155 | 
LINE 156 | MW_DEBOUNCE_METHOD = '''    # === PHASE 2: DEBOUNCE CHECKBOX ===
LINE 157 |     def _flush_pending_checks(self):
LINE 158 |         self._flush_timer = None
LINE 159 |         if not self._pending_checks or self._persist_db is None:
LINE 160 |             return
LINE 161 |         folder = self.var_folder.get()
LINE 162 |         if not folder:
LINE 163 |             self._pending_checks.clear(); return
LINE 164 |         try:
LINE 165 |             pid = self._persist_db.get_or_create_project(folder)
LINE 166 |             self._persist_db.update_is_checked_batch(
LINE 167 |                 pid, list(self._pending_checks.items()))
LINE 168 |         except Exception:
LINE 169 |             pass
LINE 170 |         self._pending_checks.clear()
LINE 171 |     # === END PHASE 2 ===
LINE 172 | '''
LINE 173 | 
LINE 174 | def main() -> int:
LINE 175 |     ap = argparse.ArgumentParser()
LINE 176 |     ap.add_argument("root", nargs="?", default=".")
LINE 177 |     args = ap.parse_args()
LINE 178 |     root = Path(args.root).resolve()
LINE 179 | 
LINE 180 |     missing = [f for f in ROOT_FILES if not (root / f).is_file()]
LINE 181 |     if missing:
LINE 182 |         for m in missing: log("ERROR", f"Falta {m}")
LINE 183 |         return 1
LINE 184 | 
LINE 185 |     log("INFO", f"Proyecto detectado: {root}")
LINE 186 |     log("INFO", f"Inicio: {datetime.now():%Y-%m-%d %H:%M:%S}")
LINE 187 |     print()
LINE 188 | 
LINE 189 |     try:
LINE 190 |         # 1) WAL + timeout en database.py
LINE 191 |         db = root / "app/core/storage/database.py"
LINE 192 |         txt = db.read_text(encoding="utf-8")
LINE 193 |         if "journal_mode = WAL" in txt:
LINE 194 |             log("SKIP", "WAL ya aplicado")
LINE 195 |         else:
LINE 196 |             if DB_WAL_OLD not in txt:
LINE 197 |                 raise RuntimeError("Ancla WAL no encontrada en database.py")
LINE 198 |             backup(root, "app/core/storage/database.py")
LINE 199 |             db.write_text(txt.replace(DB_WAL_OLD, DB_WAL_NEW, 1),
LINE 200 |                           encoding="utf-8")
LINE 201 |             log("OK", "WAL + timeout aplicados")
LINE 202 | 
LINE 203 |         # 2) apply_delta + load_nodes_map
LINE 204 |         insert_before(
LINE 205 |             root, "app/core/storage/database.py",
LINE 206 |             anchor="    def close(self) -> None:",
LINE 207 |             block=DB_DELTA_BLOCK,
LINE 208 |             marker="# === PHASE 2: DELTA SCAN ===",
LINE 209 |         )
LINE 210 | 
LINE 211 |         # 3) main_window.py — debounce
LINE 212 |         insert_after(
LINE 213 |             root, "app/gui/main_window.py",
LINE 214 |             anchor=("        self.config     = ExportConfig()\n"
LINE 215 |                     "        # === PERSISTENCE: PHASE1 (init) ===\n"
LINE 216 |                     "        self._persist_db = None\n"
LINE 217 |                     "        try:\n"
LINE 218 |                     "            self._persist_db = get_database()\n"
LINE 219 |                     "        except Exception:\n"
LINE 220 |                     "            self._persist_db = None\n"
LINE 221 |                     "        # === END PERSISTENCE: PHASE1 (init) ==="),
LINE 222 |             block=MW_DEBOUNCE_INIT,
LINE 223 |             marker="# === PHASE 2: DEBOUNCE CHECKBOX ===",
LINE 224 |         )
LINE 225 |         insert_before(
LINE 226 |             root, "app/gui/main_window.py",
LINE 227 |             anchor="    def on_select_folder(self):",
LINE 228 |             block=MW_DEBOUNCE_METHOD,
LINE 229 |             marker="# === PHASE 2: DEBOUNCE CHECKBOX ===",
LINE 230 |         )
LINE 231 | 
LINE 232 |         # 4) Cambio en analyze_incremental y _on_tree_check_change
LINE 233 |         #    (se aplica manualmente por la complejidad del bloque).
LINE 234 |         log("INFO", "Recuerda reemplazar en main_window.py:")
LINE 235 |         log("INFO", "  - analyzer.analyze(...) → analyzer.analyze_incremental(...)")
LINE 236 |         log("INFO", "  - Cuerpo de _on_tree_check_change (debounce)")
LINE 237 | 
LINE 238 |     except Exception as exc:
LINE 239 |         log("ERROR", str(exc))
LINE 240 |         return 1
LINE 241 | 
LINE 242 |     print()
LINE 243 |     log("INFO", "--- Validando sintaxis ---")
LINE 244 |     for rel in ["app/core/storage/database.py",
LINE 245 |                 "app/gui/main_window.py"]:
LINE 246 |         try:
LINE 247 |             py_compile.compile(str(root / rel), doraise=True)
LINE 248 |             log("OK", f"Sintaxis OK: {rel}")
LINE 249 |         except py_compile.PyCompileError as e:
LINE 250 |             log("ERROR", f"{rel}: {e}")
LINE 251 |             return 1
LINE 252 | 
LINE 253 |     print()
LINE 254 |     log("INFO", "Fase 2 aplicada. Reinicia la aplicación.")
LINE 255 |     return 0
LINE 256 | 
LINE 257 | if __name__ == "__main__":
LINE 258 |     sys.exit(main())
```

==============================================================
FILE: apply_search_perf.py
==============================================================
```py
LINE   1 | #!/usr/bin/env python3
LINE   2 | # -*- coding: utf-8 -*-
LINE   3 | """
LINE   4 | apply_search_perf.py
LINE   5 | 
LINE   6 | Aplica las optimizaciones de rendimiento del buscador de archivos sobre el
LINE   7 | proyecto "agente" (DeepSeek Code Packager).
LINE   8 | 
LINE   9 | Cambios aplicados
LINE  10 | -----------------
LINE  11 |   1. app/core/project_scanner.py
LINE  12 |      - Firma de invalidación recursiva (raíz + subdirectorios de primer nivel)
LINE  13 |        para evitar devolver caché obsoleta cuando cambian archivos en subcarpetas.
LINE  14 | 
LINE  15 |   2. app/core/storage/database.py
LINE  16 |      - Nuevo método `load_file_paths()` para lectura ligera desde SQLite.
LINE  17 | 
LINE  18 |   3. app/gui/file_search_dialog.py
LINE  19 |      - BATCH_SIZE reducido de 100 → 25.
LINE  20 |      - Nuevo RENDER_BATCH_DELAY_MS = 15 (antes 1 ms).
LINE  21 |      - `_refresh_results` agenda la primera tanda con `after(0, ...)` en vez de
LINE  22 |        renderizar sincrónicamente.
LINE  23 |      - `_render_batch` usa RENDER_BATCH_DELAY_MS entre tandas.
LINE  24 |      - `_load_files` y `_async_scan_worker` ahora consultan SQLite primero
LINE  25 |        (DB-first) y caen a `os.walk` sólo si la DB no tiene datos.
LINE  26 |      - `_check_scan_queue` maneja la tupla de 3 elementos (sid, files, source).
LINE  27 |      - Nuevo botón "↻ Refrescar" para forzar reescaneo desde disco.
LINE  28 | 
LINE  29 | Uso:
LINE  30 |     python3 apply_search_perf.py /ruta/al/proyecto
LINE  31 |     python3 apply_search_perf.py                 # directorio actual
LINE  32 |     python3 apply_search_perf.py --dry-run       # sólo muestra
LINE  33 | 
LINE  34 | Idempotente: ejecutarlo varias veces no duplica cambios.
LINE  35 | Sólo usa la biblioteca estándar de Python.
LINE  36 | """
LINE  37 | 
LINE  38 | import argparse
LINE  39 | import os
LINE  40 | import shutil
LINE  41 | import sys
LINE  42 | import py_compile
LINE  43 | from datetime import datetime
LINE  44 | from pathlib import Path
LINE  45 | 
LINE  46 | 
LINE  47 | # ---------------------------------------------------------------------------
LINE  48 | # Constantes
LINE  49 | # ---------------------------------------------------------------------------
LINE  50 | 
LINE  51 | BACKUP_DIRNAME = ".backup_search_perf"
LINE  52 | 
LINE  53 | STATS = {
LINE  54 |     "modified": 0,
LINE  55 |     "skipped":  0,
LINE  56 |     "backups":  0,
LINE  57 |     "errors":   0,
LINE  58 | }
LINE  59 | 
LINE  60 | REQUIRED_FILES = [
LINE  61 |     "app/__init__.py",
LINE  62 |     "app/core/__init__.py",
LINE  63 |     "app/core/project_scanner.py",
LINE  64 |     "app/core/storage/__init__.py",
LINE  65 |     "app/core/storage/database.py",
LINE  66 |     "app/gui/file_search_dialog.py",
LINE  67 |     "app/gui/main_window.py",
LINE  68 | ]
LINE  69 | 
LINE  70 | 
LINE  71 | # ---------------------------------------------------------------------------
LINE  72 | # Logging
LINE  73 | # ---------------------------------------------------------------------------
LINE  74 | 
LINE  75 | def info(msg):  print(f"[INFO] {msg}")
LINE  76 | def ok(msg):    print(f"[ OK ] {msg}");  STATS["modified"] += 1
LINE  77 | def skip(msg):  print(f"[SKIP] {msg}");  STATS["skipped"] += 1
LINE  78 | def warn(msg):  print(f"[WARN] {msg}")
LINE  79 | def error(msg): print(f"[FAIL] {msg}");  STATS["errors"] += 1
LINE  80 | 
LINE  81 | 
LINE  82 | # ---------------------------------------------------------------------------
LINE  83 | # Helpers de I/O
LINE  84 | # ---------------------------------------------------------------------------
LINE  85 | 
LINE  86 | def ensure_target_exists(root: Path, rel_path: str) -> Path:
LINE  87 |     p = root / rel_path
LINE  88 |     if not p.is_file():
LINE  89 |         raise RuntimeError(f"Archivo objetivo no encontrado: {p}")
LINE  90 |     return p
LINE  91 | 
LINE  92 | 
LINE  93 | def backup_file(root: Path, rel_path: str) -> None:
LINE  94 |     src = root / rel_path
LINE  95 |     if not src.is_file():
LINE  96 |         return
LINE  97 |     dst = root / BACKUP_DIRNAME / rel_path
LINE  98 |     dst.parent.mkdir(parents=True, exist_ok=True)
LINE  99 |     shutil.copy2(src, dst)
LINE 100 |     STATS["backups"] += 1
LINE 101 |     info(f"Backup creado: {dst.relative_to(root)}")
LINE 102 | 
LINE 103 | 
LINE 104 | def _apply_change(root: Path, rel_path: str, new_content: str) -> None:
LINE 105 |     backup_file(root, rel_path)
LINE 106 |     (root / rel_path).write_text(new_content, encoding="utf-8")
LINE 107 |     ok(f"Cambio aplicado: {rel_path}")
LINE 108 | 
LINE 109 | 
LINE 110 | def replace_exact(root: Path, rel_path: str, old: str, new: str,
LINE 111 |                   marker_check: str = None) -> None:
LINE 112 |     """Reemplaza `old` por `new` si `old` está presente.
LINE 113 | 
LINE 114 |     `marker_check`: subcadena que, si ya está presente en el archivo,
LINE 115 |     indica que el cambio ya fue aplicado (idempotencia).
LINE 116 |     """
LINE 117 |     path = root / rel_path
LINE 118 |     content = path.read_text(encoding="utf-8")
LINE 119 | 
LINE 120 |     if marker_check and marker_check in content:
LINE 121 |         skip(f"{rel_path}: cambio ya aplicado (marcador presente)")
LINE 122 |         return
LINE 123 | 
LINE 124 |     if old not in content:
LINE 125 |         warn(f"{rel_path}: patrón no encontrado (posible versión distinta)")
LINE 126 |         STATS["skipped"] += 1
LINE 127 |         return
LINE 128 | 
LINE 129 |     new_content = content.replace(old, new, 1)
LINE 130 |     _apply_change(root, rel_path, new_content)
LINE 131 | 
LINE 132 | 
LINE 133 | def insert_before(root: Path, rel_path: str, anchor: str,
LINE 134 |                   block: str, marker_check: str) -> None:
LINE 135 |     """Inserta `block` antes de `anchor` en el archivo."""
LINE 136 |     path = root / rel_path
LINE 137 |     content = path.read_text(encoding="utf-8")
LINE 138 | 
LINE 139 |     if marker_check and marker_check in content:
LINE 140 |         skip(f"{rel_path}: cambio ya aplicado (marcador presente)")
LINE 141 |         return
LINE 142 | 
LINE 143 |     idx = content.find(anchor)
LINE 144 |     if idx == -1:
LINE 145 |         raise RuntimeError(f"Ancla no encontrada en {rel_path}:\n  {anchor!r}")
LINE 146 | 
LINE 147 |     new_content = content[:idx] + block + content[idx:]
LINE 148 |     _apply_change(root, rel_path, new_content)
LINE 149 | 
LINE 150 | 
LINE 151 | def append_if_missing(root: Path, rel_path: str, block: str,
LINE 152 |                       marker_check: str) -> None:
LINE 153 |     """Añade `block` al final del archivo si `marker_check` no está presente."""
LINE 154 |     path = root / rel_path
LINE 155 |     content = path.read_text(encoding="utf-8")
LINE 156 | 
LINE 157 |     if marker_check and marker_check in content:
LINE 158 |         skip(f"{rel_path}: cambio ya aplicado (marcador presente)")
LINE 159 |         return
LINE 160 | 
LINE 161 |     if not content.endswith("\n"):
LINE 162 |         content += "\n"
LINE 163 |     new_content = content + block
LINE 164 |     _apply_change(root, rel_path, new_content)
LINE 165 | 
LINE 166 | 
LINE 167 | # ---------------------------------------------------------------------------
LINE 168 | # ---------------------------------------------------------------------------
LINE 169 | # Contenido: PATCH 1 — app/core/project_scanner.py
LINE 170 | # ---------------------------------------------------------------------------
LINE 171 | # ---------------------------------------------------------------------------
LINE 172 | 
LINE 173 | SCANNER_OLD_SIGNATURE = '''    folder_mtime = 0.0
LINE 174 |     try:
LINE 175 |         folder_mtime = os.path.getmtime(abs_folder)
LINE 176 |     except OSError:
LINE 177 |         pass
LINE 178 | 
LINE 179 |     if use_cache and not force_refresh:
LINE 180 |         with _cache_lock:
LINE 181 |             if cache_key in _SCAN_CACHE:
LINE 182 |                 cached_mtime, cached_files = _SCAN_CACHE[cache_key]
LINE 183 |                 if cached_mtime == folder_mtime:
LINE 184 |                     return list(cached_files)
LINE 185 | '''
LINE 186 | 
LINE 187 | SCANNER_NEW_SIGNATURE = '''    # FIX: firma de invalidación recursiva ligera (raíz + subdirectorios
LINE 188 |     # inmediatos). No es perfecta, pero evita devolver caché obsoleta cuando
LINE 189 |     # cambian archivos dentro de subcarpetas de primer nivel, sin coste de
LINE 190 |     # os.walk completo.
LINE 191 |     signature = 0.0
LINE 192 |     try:
LINE 193 |         signature = os.path.getmtime(abs_folder)
LINE 194 |         with os.scandir(abs_folder) as it:
LINE 195 |             for entry in it:
LINE 196 |                 if entry.is_dir(follow_symlinks=False):
LINE 197 |                     try:
LINE 198 |                         signature = max(
LINE 199 |                             signature,
LINE 200 |                             entry.stat(follow_symlinks=False).st_mtime,
LINE 201 |                         )
LINE 202 |                     except OSError:
LINE 203 |                         continue
LINE 204 |     except OSError:
LINE 205 |         pass
LINE 206 | 
LINE 207 |     if use_cache and not force_refresh:
LINE 208 |         with _cache_lock:
LINE 209 |             if cache_key in _SCAN_CACHE:
LINE 210 |                 cached_mtime, cached_files = _SCAN_CACHE[cache_key]
LINE 211 |                 if cached_mtime == signature:
LINE 212 |                     return list(cached_files)
LINE 213 | '''
LINE 214 | 
LINE 215 | SCANNER_OLD_STORE = "            _SCAN_CACHE[cache_key] = (folder_mtime, valid_files)"
LINE 216 | SCANNER_NEW_STORE = "            _SCAN_CACHE[cache_key] = (signature, valid_files)"
LINE 217 | 
LINE 218 | 
LINE 219 | # ---------------------------------------------------------------------------
LINE 220 | # ---------------------------------------------------------------------------
LINE 221 | # Contenido: PATCH 2 — app/core/storage/database.py
LINE 222 | # ---------------------------------------------------------------------------
LINE 223 | # ---------------------------------------------------------------------------
LINE 224 | 
LINE 225 | DATABASE_ANCHOR = "    # === PHASE 2: DELTA SCAN ==="
LINE 226 | 
LINE 227 | DATABASE_NEW_METHOD = '''    def load_file_paths(self, project_path: str):
LINE 228 |         """Devuelve lista plana de rutas de archivo (is_dir=0) ordenadas.
LINE 229 | 
LINE 230 |         Pensado para alimentar el buscador sin pagar el coste de os.walk.
LINE 231 |         Devuelve:
LINE 232 |             (files: List[str], last_scanned: Optional[str], exists: bool)
LINE 233 |         donde `files` es [] si el proyecto existe pero no tiene nodos.
LINE 234 |         """
LINE 235 |         cur = self._conn.cursor()
LINE 236 |         cur.execute(
LINE 237 |             "SELECT id, last_scanned FROM projects WHERE path = ?",
LINE 238 |             (project_path,),
LINE 239 |         )
LINE 240 |         row = cur.fetchone()
LINE 241 |         if not row:
LINE 242 |             return [], None, False
LINE 243 |         project_id = int(row["id"])
LINE 244 |         last_scanned = row["last_scanned"]
LINE 245 |         cur.execute(
LINE 246 |             "SELECT rel_path FROM nodes "
LINE 247 |             "WHERE project_id = ? AND is_dir = 0 "
LINE 248 |             "ORDER BY rel_path",
LINE 249 |             (project_id,),
LINE 250 |         )
LINE 251 |         files = [r["rel_path"] for r in cur.fetchall()]
LINE 252 |         return files, last_scanned, True
LINE 253 | 
LINE 254 | '''
LINE 255 | 
LINE 256 | 
LINE 257 | # ---------------------------------------------------------------------------
LINE 258 | # ---------------------------------------------------------------------------
LINE 259 | # Contenido: PATCH 3 — app/gui/file_search_dialog.py
LINE 260 | # ---------------------------------------------------------------------------
LINE 261 | # ---------------------------------------------------------------------------
LINE 262 | 
LINE 263 | FSD_OLD_CONSTANTS = '''MAX_RENDER_LIMIT = 500
LINE 264 | BATCH_SIZE = 100
LINE 265 | DEBOUNCE_MS = 150
LINE 266 | LOADING_DELAY_MS = 200
LINE 267 | QUEUE_CHECK_MS = 20
LINE 268 | '''
LINE 269 | 
LINE 270 | FSD_NEW_CONSTANTS = '''MAX_RENDER_LIMIT = 500
LINE 271 | BATCH_SIZE = 25              # 100 -> 25 : tandas más pequeñas, sin bloquear el mainloop
LINE 272 | DEBOUNCE_MS = 150
LINE 273 | LOADING_DELAY_MS = 200
LINE 274 | QUEUE_CHECK_MS = 20
LINE 275 | RENDER_BATCH_DELAY_MS = 15   # 1 -> 15 : cede el hilo entre tandas
LINE 276 | '''
LINE 277 | 
LINE 278 | 
LINE 279 | FSD_OLD_REFRESH_TAIL = '''        # Render first batch synchronously
LINE 280 |         self._render_batch(matches_to_render, start_idx=0, total_matches=total_matches)
LINE 281 | '''
LINE 282 | 
LINE 283 | FSD_NEW_REFRESH_TAIL = '''        # FIX: incluso la primera tanda se agenda con after(0, ...) para no
LINE 284 |         # bloquear el hilo de la GUI dentro de _refresh_results.
LINE 285 |         self._render_timer = self.after(
LINE 286 |             0,
LINE 287 |             lambda: self._render_batch(matches_to_render, 0, total_matches),
LINE 288 |         )
LINE 289 | '''
LINE 290 | 
LINE 291 | 
LINE 292 | FSD_OLD_RENDER_TAIL = '''        if end_idx < len(matches_subset):
LINE 293 |             # Schedule next batch
LINE 294 |             self._render_timer = self.after(
LINE 295 |                 1, lambda: self._render_batch(matches_subset, end_idx, total_matches)
LINE 296 |             )
LINE 297 | '''
LINE 298 | 
LINE 299 | FSD_NEW_RENDER_TAIL = '''        if end_idx < len(matches_subset):
LINE 300 |             # FIX: 15 ms en lugar de 1 ms para que el mainloop procese eventos
LINE 301 |             # (redibujado, teclado, ratón) entre tandas.
LINE 302 |             self._render_timer = self.after(
LINE 303 |                 RENDER_BATCH_DELAY_MS,
LINE 304 |                 lambda: self._render_batch(matches_subset, end_idx, total_matches),
LINE 305 |             )
LINE 306 | '''
LINE 307 | 
LINE 308 | 
LINE 309 | FSD_OLD_LOAD_FILES = '''    def _load_files(self):
LINE 310 |         self._scan_id += 1
LINE 311 |         current_scan_id = self._scan_id
LINE 312 | 
LINE 313 |         # Schedule delayed loading indicator after 200ms
LINE 314 |         self._cancel_timer("_loading_timer")
LINE 315 |         self._loading_timer = self.after(
LINE 316 |             LOADING_DELAY_MS, lambda: self._show_loading(current_scan_id)
LINE 317 |         )
LINE 318 | 
LINE 319 |         # Launch background scan daemon thread
LINE 320 |         threading.Thread(
LINE 321 |             target=self._async_scan_worker,
LINE 322 |             args=(current_scan_id, self.folder_path, self.excluded_dirs, self._scan_queue),
LINE 323 |             daemon=True,
LINE 324 |         ).start()
LINE 325 | 
LINE 326 |         # Start queue polling loop on main GUI thread
LINE 327 |         self._schedule_queue_check()
LINE 328 | '''
LINE 329 | 
LINE 330 | FSD_NEW_LOAD_FILES = '''    def _load_files(self, force_refresh: bool = False):
LINE 331 |         self._scan_id += 1
LINE 332 |         current_scan_id = self._scan_id
LINE 333 | 
LINE 334 |         # Schedule delayed loading indicator after 200ms
LINE 335 |         self._cancel_timer("_loading_timer")
LINE 336 |         self._loading_timer = self.after(
LINE 337 |             LOADING_DELAY_MS, lambda: self._show_loading(current_scan_id)
LINE 338 |         )
LINE 339 | 
LINE 340 |         # FIX: launch background worker: DB-first, os.walk fallback
LINE 341 |         threading.Thread(
LINE 342 |             target=self._async_scan_worker,
LINE 343 |             args=(
LINE 344 |                 current_scan_id,
LINE 345 |                 self.folder_path,
LINE 346 |                 self.excluded_dirs,
LINE 347 |                 self._scan_queue,
LINE 348 |                 force_refresh,
LINE 349 |             ),
LINE 350 |             daemon=True,
LINE 351 |         ).start()
LINE 352 | 
LINE 353 |         # Start queue polling loop on main GUI thread
LINE 354 |         self._schedule_queue_check()
LINE 355 | '''
LINE 356 | 
LINE 357 | 
LINE 358 | FSD_OLD_CHECK_QUEUE_HEAD = '''        received = False
LINE 359 |         latest_files = None
LINE 360 | 
LINE 361 |         while True:
LINE 362 |             try:
LINE 363 |                 sid, files = self._scan_queue.get_nowait()
LINE 364 |                 if sid == self._scan_id:
LINE 365 |                     latest_files = files
LINE 366 |                     received = True
LINE 367 |             except queue.Empty:
LINE 368 |                 break
LINE 369 | 
LINE 370 |         if received and latest_files is not None:
LINE 371 |             self._hide_loading()
LINE 372 |             self.all_files = latest_files
LINE 373 |             self._files_indexed = [(f, f.lower()) for f in latest_files]
LINE 374 |             self._refresh_results(force=True)
LINE 375 | '''
LINE 376 | 
LINE 377 | FSD_NEW_CHECK_QUEUE_HEAD = '''        received = False
LINE 378 |         latest_files = None
LINE 379 |         source = None
LINE 380 | 
LINE 381 |         while True:
LINE 382 |             try:
LINE 383 |                 sid, files, src = self._scan_queue.get_nowait()
LINE 384 |                 if sid == self._scan_id:
LINE 385 |                     latest_files = files
LINE 386 |                     source = src
LINE 387 |                     received = True
LINE 388 |             except queue.Empty:
LINE 389 |                 break
LINE 390 | 
LINE 391 |         if received and latest_files is not None:
LINE 392 |             self._hide_loading()
LINE 393 |             self.all_files = latest_files
LINE 394 |             self._files_indexed = [(f, f.lower()) for f in latest_files]
LINE 395 |             if self.lbl_loading is not None and self.winfo_exists():
LINE 396 |                 tag = "caché DB" if source == "db" else "escaneo"
LINE 397 |                 self.lbl_loading.config(
LINE 398 |                     text=f"✓ {len(latest_files)} archivos ({tag})"
LINE 399 |                 )
LINE 400 |             self._refresh_results(force=True)
LINE 401 | '''
LINE 402 | 
LINE 403 | 
LINE 404 | FSD_OLD_SCAN_WORKER = '''    @staticmethod
LINE 405 |     def _async_scan_worker(scan_id: int, folder_path: str, excluded_dirs: Set[str], res_queue: queue.Queue):
LINE 406 |         """Worker thread entry point: purely python I/O, no Tkinter calls."""
LINE 407 |         try:
LINE 408 |             files = scan_directory(folder_path, excluded_dirs, allowed_extensions=None)
LINE 409 |         except Exception:
LINE 410 |             files = []
LINE 411 |         res_queue.put((scan_id, files))
LINE 412 | '''
LINE 413 | 
LINE 414 | FSD_NEW_SCAN_WORKER = '''    @staticmethod
LINE 415 |     def _async_scan_worker(
LINE 416 |         scan_id: int,
LINE 417 |         folder_path: str,
LINE 418 |         excluded_dirs: Set[str],
LINE 419 |         res_queue: queue.Queue,
LINE 420 |         force_refresh: bool = False,
LINE 421 |     ):
LINE 422 |         """Worker thread entry point: DB-first con fallback a os.walk.
LINE 423 | 
LINE 424 |         Estrategia:
LINE 425 |           1) Si !force_refresh, consultar SQLite (project_cache.db). ~1 ms.
LINE 426 |           2) Si la DB no tiene filas o el usuario forzó refresco, os.walk.
LINE 427 |         """
LINE 428 |         files: List[str] = []
LINE 429 |         source = "scan"
LINE 430 |         try:
LINE 431 |             from app.core.storage.database import get_database
LINE 432 | 
LINE 433 |             if not force_refresh:
LINE 434 |                 db = get_database()
LINE 435 |                 db_files, _last_scanned, exists = db.load_file_paths(folder_path)
LINE 436 |                 if exists and db_files:
LINE 437 |                     files = db_files
LINE 438 |                     source = "db"
LINE 439 | 
LINE 440 |             if not files:
LINE 441 |                 files = scan_directory(
LINE 442 |                     folder_path, excluded_dirs, allowed_extensions=None
LINE 443 |                 )
LINE 444 |                 source = "scan"
LINE 445 |         except Exception:
LINE 446 |             # Ante cualquier fallo, caer a escaneo directo
LINE 447 |             try:
LINE 448 |                 files = scan_directory(
LINE 449 |                     folder_path, excluded_dirs, allowed_extensions=None
LINE 450 |                 )
LINE 451 |             except Exception:
LINE 452 |                 files = []
LINE 453 |             source = "scan"
LINE 454 | 
LINE 455 |         res_queue.put((scan_id, files, source))
LINE 456 | '''
LINE 457 | 
LINE 458 | 
LINE 459 | FSD_OLD_HEADER_BUTTONS = '''        ttk.Button(row, text="Buscar", command=self._force_refresh_results).pack(side=tk.LEFT)
LINE 460 |         ttk.Button(row, text="Limpiar", command=self._clear_search).pack(side=tk.LEFT, padx=(6, 0))
LINE 461 | '''
LINE 462 | 
LINE 463 | FSD_NEW_HEADER_BUTTONS = '''        ttk.Button(row, text="Buscar", command=self._force_refresh_results).pack(side=tk.LEFT)
LINE 464 |         ttk.Button(row, text="Limpiar", command=self._clear_search).pack(side=tk.LEFT, padx=(6, 0))
LINE 465 |         ttk.Button(
LINE 466 |             row,
LINE 467 |             text="↻ Refrescar",
LINE 468 |             command=lambda: self._load_files(force_refresh=True),
LINE 469 |         ).pack(side=tk.LEFT, padx=(6, 0))
LINE 470 | '''
LINE 471 | 
LINE 472 | 
LINE 473 | # ---------------------------------------------------------------------------
LINE 474 | # Estructura del proyecto
LINE 475 | # ---------------------------------------------------------------------------
LINE 476 | 
LINE 477 | def verify_structure(root: Path) -> None:
LINE 478 |     info(f"Proyecto detectado: {root}")
LINE 479 |     missing = [rel for rel in REQUIRED_FILES if not (root / rel).is_file()]
LINE 480 |     if missing:
LINE 481 |         for m in missing:
LINE 482 |             error(f"Falta archivo requerido: {m}")
LINE 483 |         raise RuntimeError(
LINE 484 |             "La estructura del proyecto no coincide con la esperada. "
LINE 485 |             "Abortando sin modificar archivos."
LINE 486 |         )
LINE 487 | 
LINE 488 | 
LINE 489 | # ---------------------------------------------------------------------------
LINE 490 | # Aplicación de cambios
LINE 491 | # ---------------------------------------------------------------------------
LINE 492 | 
LINE 493 | def apply_all(root: Path, dry_run: bool) -> None:
LINE 494 |     info("--- Verificando estructura del proyecto ---")
LINE 495 |     verify_structure(root)
LINE 496 | 
LINE 497 |     # ---------------------------------------------------------------------
LINE 498 |     # PATCH 1 — app/core/project_scanner.py
LINE 499 |     # ---------------------------------------------------------------------
LINE 500 |     info("--- [1/4] Optimizando caché de project_scanner.py ---")
LINE 501 |     ensure_target_exists(root, "app/core/project_scanner.py")
LINE 502 | 
LINE 503 |     replace_exact(
LINE 504 |         root, "app/core/project_scanner.py",
LINE 505 |         old=SCANNER_OLD_SIGNATURE,
LINE 506 |         new=SCANNER_NEW_SIGNATURE,
LINE 507 |         marker_check="signature = max(",
LINE 508 |     )
LINE 509 |     replace_exact(
LINE 510 |         root, "app/core/project_scanner.py",
LINE 511 |         old=SCANNER_OLD_STORE,
LINE 512 |         new=SCANNER_NEW_STORE,
LINE 513 |         marker_check="(signature, valid_files)",
LINE 514 |     )
LINE 515 | 
LINE 516 |     # ---------------------------------------------------------------------
LINE 517 |     # PATCH 2 — app/core/storage/database.py
LINE 518 |     # ---------------------------------------------------------------------
LINE 519 |     info("--- [2/4] Añadiendo load_file_paths() a database.py ---")
LINE 520 |     ensure_target_exists(root, "app/core/storage/database.py")
LINE 521 | 
LINE 522 |     insert_before(
LINE 523 |         root, "app/core/storage/database.py",
LINE 524 |         anchor=DATABASE_ANCHOR,
LINE 525 |         block=DATABASE_NEW_METHOD,
LINE 526 |         marker_check="def load_file_paths(self, project_path",
LINE 527 |     )
LINE 528 | 
LINE 529 |     # ---------------------------------------------------------------------
LINE 530 |     # PATCH 3 — app/gui/file_search_dialog.py (render)
LINE 531 |     # ---------------------------------------------------------------------
LINE 532 |     info("--- [3/4] Optimizando render de file_search_dialog.py ---")
LINE 533 |     ensure_target_exists(root, "app/gui/file_search_dialog.py")
LINE 534 | 
LINE 535 |     replace_exact(
LINE 536 |         root, "app/gui/file_search_dialog.py",
LINE 537 |         old=FSD_OLD_CONSTANTS,
LINE 538 |         new=FSD_NEW_CONSTANTS,
LINE 539 |         marker_check="RENDER_BATCH_DELAY_MS",
LINE 540 |     )
LINE 541 |     replace_exact(
LINE 542 |         root, "app/gui/file_search_dialog.py",
LINE 543 |         old=FSD_OLD_REFRESH_TAIL,
LINE 544 |         new=FSD_NEW_REFRESH_TAIL,
LINE 545 |         marker_check="# FIX: incluso la primera tanda se agenda con after(0, ...)",
LINE 546 |     )
LINE 547 |     replace_exact(
LINE 548 |         root, "app/gui/file_search_dialog.py",
LINE 549 |         old=FSD_OLD_RENDER_TAIL,
LINE 550 |         new=FSD_NEW_RENDER_TAIL,
LINE 551 |         marker_check="# FIX: 15 ms en lugar de 1 ms",
LINE 552 |     )
LINE 553 | 
LINE 554 |     # ---------------------------------------------------------------------
LINE 555 |     # PATCH 4 — app/gui/file_search_dialog.py (DB-first scan)
LINE 556 |     # ---------------------------------------------------------------------
LINE 557 |     info("--- [4/4] DB-first scan + botón Refrescar en file_search_dialog.py ---")
LINE 558 | 
LINE 559 |     replace_exact(
LINE 560 |         root, "app/gui/file_search_dialog.py",
LINE 561 |         old=FSD_OLD_LOAD_FILES,
LINE 562 |         new=FSD_NEW_LOAD_FILES,
LINE 563 |         marker_check="def _load_files(self, force_refresh: bool = False):",
LINE 564 |     )
LINE 565 |     replace_exact(
LINE 566 |         root, "app/gui/file_search_dialog.py",
LINE 567 |         old=FSD_OLD_CHECK_QUEUE_HEAD,
LINE 568 |         new=FSD_NEW_CHECK_QUEUE_HEAD,
LINE 569 |         marker_check="sid, files, src = self._scan_queue.get_nowait()",
LINE 570 |     )
LINE 571 |     replace_exact(
LINE 572 |         root, "app/gui/file_search_dialog.py",
LINE 573 |         old=FSD_OLD_SCAN_WORKER,
LINE 574 |         new=FSD_NEW_SCAN_WORKER,
LINE 575 |         marker_check='db.load_file_paths(folder_path)',
LINE 576 |     )
LINE 577 |     replace_exact(
LINE 578 |         root, "app/gui/file_search_dialog.py",
LINE 579 |         old=FSD_OLD_HEADER_BUTTONS,
LINE 580 |         new=FSD_NEW_HEADER_BUTTONS,
LINE 581 |         marker_check='text="↻ Refrescar"',
LINE 582 |     )
LINE 583 | 
LINE 584 | 
LINE 585 | # ---------------------------------------------------------------------------
LINE 586 | # Validación final
LINE 587 | # ---------------------------------------------------------------------------
LINE 588 | 
LINE 589 | def validate_syntax(root: Path) -> None:
LINE 590 |     info("--- Validando sintaxis (py_compile) ---")
LINE 591 |     for rel in [
LINE 592 |         "app/core/project_scanner.py",
LINE 593 |         "app/core/storage/database.py",
LINE 594 |         "app/gui/file_search_dialog.py",
LINE 595 |     ]:
LINE 596 |         full = root / rel
LINE 597 |         if not full.is_file():
LINE 598 |             continue
LINE 599 |         try:
LINE 600 |             py_compile.compile(str(full), doraise=True)
LINE 601 |             info(f"Sintaxis OK: {rel}")
LINE 602 |         except py_compile.PyCompileError as exc:
LINE 603 |             error(f"Sintaxis inválida en {rel}: {exc}")
LINE 604 | 
LINE 605 | 
LINE 606 | def print_summary() -> None:
LINE 607 |     print()
LINE 608 |     print(f"Archivos modificados: {STATS['modified']}")
LINE 609 |     print(f"Archivos omitidos:    {STATS['skipped']}")
LINE 610 |     print(f"Backups creados:      {STATS['backups']}")
LINE 611 |     print(f"Errores:              {STATS['errors']}")
LINE 612 | 
LINE 613 | 
LINE 614 | # ---------------------------------------------------------------------------
LINE 615 | # CLI
LINE 616 | # ---------------------------------------------------------------------------
LINE 617 | 
LINE 618 | def build_parser() -> argparse.ArgumentParser:
LINE 619 |     p = argparse.ArgumentParser(
LINE 620 |         description="Aplica las optimizaciones de rendimiento del buscador."
LINE 621 |     )
LINE 622 |     p.add_argument(
LINE 623 |         "project_root", nargs="?", default=".",
LINE 624 |         help="Ruta raíz del proyecto (por defecto: directorio actual).",
LINE 625 |     )
LINE 626 |     p.add_argument("--dry-run", action="store_true",
LINE 627 |                    help="Sólo muestra, no modifica archivos.")
LINE 628 |     return p
LINE 629 | 
LINE 630 | 
LINE 631 | def main() -> int:
LINE 632 |     parser = build_parser()
LINE 633 |     args = parser.parse_args()
LINE 634 | 
LINE 635 |     try:
LINE 636 |         root = Path(args.project_root).resolve()
LINE 637 |     except Exception as exc:
LINE 638 |         error(f"Ruta inválida: {exc}")
LINE 639 |         return 1
LINE 640 | 
LINE 641 |     if not root.is_dir():
LINE 642 |         error(f"El directorio no existe: {root}")
LINE 643 |         return 1
LINE 644 | 
LINE 645 |     print(f"[INFO] Proyecto detectado: {root}")
LINE 646 |     print(f"[INFO] Inicio: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
LINE 647 |     print(f"[INFO] Dry-run: {args.dry_run}")
LINE 648 |     print()
LINE 649 | 
LINE 650 |     if args.dry_run:
LINE 651 |         info("Modo dry-run: se aplicarán los cambios en memoria y se reportará "
LINE 652 |              "qué haría cada uno sin escribir nada.")
LINE 653 |         print()
LINE 654 | 
LINE 655 |     try:
LINE 656 |         apply_all(root, dry_run=args.dry_run)
LINE 657 |     except Exception as exc:
LINE 658 |         error(str(exc))
LINE 659 |         print()
LINE 660 |         info("Proceso detenido. No se continúan aplicando cambios.")
LINE 661 |         print_summary()
LINE 662 |         return 1
LINE 663 | 
LINE 664 |     print()
LINE 665 |     info("--- Resumen final ---")
LINE 666 |     print_summary()
LINE 667 | 
LINE 668 |     if not args.dry_run:
LINE 669 |         validate_syntax(root)
LINE 670 | 
LINE 671 |     print()
LINE 672 |     if STATS["errors"] == 0:
LINE 673 |         info("Optimizaciones aplicadas. Reinicia la aplicación para probar.")
LINE 674 |         return 0
LINE 675 |     return 1
LINE 676 | 
LINE 677 | 
LINE 678 | if __name__ == "__main__":
LINE 679 |     sys.exit(main())
```

==============================================================
FILE: deepseek_gui.py
==============================================================
```py
LINE 1 | """
LINE 2 | Launcher wrapper for backward compatibility.
LINE 3 | Invokes the modular entry point main.py.
LINE 4 | """
LINE 5 | from main import main
LINE 6 | 
LINE 7 | if __name__ == "__main__":
LINE 8 |     main()
```

==============================================================
FILE: ejecutar.bat
==============================================================
```bat
LINE  1 | @echo off
LINE  2 | title DeepSeek Debugger GUI
LINE  3 | cd /d "%~dp0"
LINE  4 | 
LINE  5 | echo ========================================================
LINE  6 | echo         Iniciando DeepSeek Debugger GUI
LINE  7 | echo ========================================================
LINE  8 | echo.
LINE  9 | 
LINE 10 | :: 1. Verificar si el entorno virtual existe
LINE 11 | if not exist "%~dp0venv\Scripts\python.exe" (
LINE 12 |     echo [INFO] Creando el entorno virtual venv...
LINE 13 |     python -m venv "%~dp0venv"
LINE 14 |     if errorlevel 1 (
LINE 15 |         echo [ERROR] No se pudo crear el entorno virtual.
LINE 16 |         echo Asegurate de tener Python instalado y agregado al PATH.
LINE 17 |         echo.
LINE 18 |         pause
LINE 19 |         exit /b 1
LINE 20 |     )
LINE 21 |     echo [INFO] Instalando dependencias desde requirements.txt...
LINE 22 |     "%~dp0venv\Scripts\python.exe" -m pip install -r "%~dp0requirements.txt"
LINE 23 |     if errorlevel 1 (
LINE 24 |         echo [ERROR] Error al instalar dependencias.
LINE 25 |         echo.
LINE 26 |         pause
LINE 27 |         exit /b 1
LINE 28 |     )
LINE 29 | )
LINE 30 | 
LINE 31 | :: 2. Ejecutar la aplicacion usando el Python del entorno virtual
LINE 32 | echo [INFO] Lanzando la interfaz grafica...
LINE 33 | start "" "%~dp0venv\Scripts\pythonw.exe" "%~dp0main.py"
LINE 34 | 
LINE 35 | if errorlevel 1 (
LINE 36 |     echo [ERROR] Ocurrio un error al lanzar la aplicacion.
LINE 37 |     echo.
LINE 38 |     pause
LINE 39 |     exit /b 1
LINE 40 | )
LINE 41 | 
LINE 42 | echo [INFO] Aplicacion iniciada correctamente.
```

==============================================================
FILE: ejecutar_con_consola.bat
==============================================================
```bat
LINE  1 | @echo off
LINE  2 | title DeepSeek Debugger GUI - Modo Consola
LINE  3 | cd /d "%~dp0"
LINE  4 | 
LINE  5 | echo ========================================================
LINE  6 | echo         Ejecutando en Modo Consola - Debug
LINE  7 | echo ========================================================
LINE  8 | echo.
LINE  9 | 
LINE 10 | if not exist "%~dp0venv\Scripts\python.exe" (
LINE 11 |     echo [INFO] Creando el entorno virtual venv...
LINE 12 |     python -m venv "%~dp0venv"
LINE 13 |     echo [INFO] Instalando dependencias...
LINE 14 |     "%~dp0venv\Scripts\python.exe" -m pip install -r "%~dp0requirements.txt"
LINE 15 | )
LINE 16 | 
LINE 17 | echo [INFO] Iniciando main.py...
LINE 18 | echo.
LINE 19 | "%~dp0venv\Scripts\python.exe" "%~dp0main.py"
LINE 20 | 
LINE 21 | echo.
LINE 22 | echo ========================================================
LINE 23 | echo La aplicacion se ha cerrado. Presiona cualquier tecla para salir.
LINE 24 | echo ========================================================
LINE 25 | pause
```

==============================================================
FILE: iniciar_deepseek_debugger.sh
==============================================================
```sh
LINE  1 | #!/bin/bash
LINE  2 | 
LINE  3 | # Título de la terminal
LINE  4 | echo -ne "\033]0;DeepSeek Debugger GUI\007"
LINE  5 | 
LINE  6 | # Cambiar al directorio donde está este script
LINE  7 | cd "$(dirname "$0")" || exit 1
LINE  8 | 
LINE  9 | echo "========================================================"
LINE 10 | echo "        Iniciando DeepSeek Debugger GUI"
LINE 11 | echo "========================================================"
LINE 12 | echo
LINE 13 | 
LINE 14 | # 1. Verificar si el entorno virtual existe
LINE 15 | if [ ! -f "venv/bin/python" ]; then
LINE 16 |     echo "[INFO] Creando el entorno virtual venv..."
LINE 17 | 
LINE 18 |     python3 -m venv venv
LINE 19 | 
LINE 20 |     if [ $? -ne 0 ]; then
LINE 21 |         echo "[ERROR] No se pudo crear el entorno virtual."
LINE 22 |         echo "Asegúrate de tener Python 3 instalado."
LINE 23 |         echo
LINE 24 |         read -p "Presiona Enter para salir..."
LINE 25 |         exit 1
LINE 26 |     fi
LINE 27 | 
LINE 28 |     echo "[INFO] Instalando dependencias desde requirements.txt..."
LINE 29 | 
LINE 30 |     venv/bin/python -m pip install -r requirements.txt
LINE 31 | 
LINE 32 |     if [ $? -ne 0 ]; then
LINE 33 |         echo "[ERROR] Error al instalar dependencias."
LINE 34 |         echo
LINE 35 |         read -p "Presiona Enter para salir..."
LINE 36 |         exit 1
LINE 37 |     fi
LINE 38 | fi
LINE 39 | 
LINE 40 | # 2. Ejecutar la aplicación usando Python del entorno virtual
LINE 41 | echo "[INFO] Lanzando la interfaz gráfica..."
LINE 42 | 
LINE 43 | venv/bin/python main.py
LINE 44 | 
LINE 45 | if [ $? -ne 0 ]; then
LINE 46 |     echo "[ERROR] Ocurrió un error al ejecutar la aplicación."
LINE 47 |     echo
LINE 48 |     read -p "Presiona Enter para salir..."
LINE 49 |     exit 1
LINE 50 | fi
LINE 51 | 
LINE 52 | echo "[INFO] Aplicación finalizada correctamente."
```

==============================================================
FILE: main.py
==============================================================
```py
LINE  1 | """Main entry point for DeepSeek Code Packager."""
LINE  2 | import sys
LINE  3 | import os
LINE  4 | import tkinter as tk
LINE  5 | 
LINE  6 | # Ensure current working directory is in sys.path
LINE  7 | sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
LINE  8 | 
LINE  9 | from app.gui.main_window import MainWindow
LINE 10 | 
LINE 11 | 
LINE 12 | def main():
LINE 13 |     root = tk.Tk()
LINE 14 |     app = MainWindow(root)
LINE 15 |     root.mainloop()
LINE 16 | 
LINE 17 | 
LINE 18 | if __name__ == "__main__":
LINE 19 |     main()
```

==============================================================
FILE: nuevo_script.py
==============================================================
```py
LINE   1 | #!/usr/bin/env python3
LINE   2 | # -*- coding: utf-8 -*-
LINE   3 | """
LINE   4 | apply_phase1_sqlite.py
LINE   5 | 
LINE   6 | Aplica la Fase 1 — Persistencia SQLite para nodos — sobre el proyecto
LINE   7 | "agente" (DeepSeek Code Packager).
LINE   8 | 
LINE   9 | Uso:
LINE  10 |     python3 apply_phase1_sqlite.py /ruta/al/proyecto
LINE  11 |     python3 apply_phase1_sqlite.py                 # usa el directorio actual
LINE  12 | 
LINE  13 | Características:
LINE  14 |   * Detecta automáticamente la raíz del proyecto (o la recibe como argumento).
LINE  15 |   * Verifica que los archivos objetivo existan ANTES de modificar nada.
LINE  16 |   * Crea backups en .backup/ preservando la ruta relativa original.
LINE  17 |   * Es idempotente: ejecutarlo dos veces no duplica bloques.
LINE  18 |   * Solo modifica los archivos estrictamente necesarios.
LINE  19 |   * Al finalizar valida la sintaxis con py_compile.
LINE  20 |   * Solo utiliza la biblioteca estándar de Python.
LINE  21 | """
LINE  22 | 
LINE  23 | import argparse
LINE  24 | import os
LINE  25 | import shutil
LINE  26 | import sys
LINE  27 | import py_compile
LINE  28 | from datetime import datetime
LINE  29 | from pathlib import Path
LINE  30 | 
LINE  31 | 
LINE  32 | # ---------------------------------------------------------------------------
LINE  33 | # Constantes
LINE  34 | # ---------------------------------------------------------------------------
LINE  35 | 
LINE  36 | BACKUP_DIRNAME = ".backup"
LINE  37 | 
LINE  38 | STATS = {
LINE  39 |     "modified": 0,
LINE  40 |     "created": 0,
LINE  41 |     "skipped": 0,
LINE  42 |     "backups": 0,
LINE  43 |     "errors": 0,
LINE  44 | }
LINE  45 | 
LINE  46 | 
LINE  47 | # ---------------------------------------------------------------------------
LINE  48 | # Logging
LINE  49 | # ---------------------------------------------------------------------------
LINE  50 | 
LINE  51 | def _log(prefix, msg):
LINE  52 |     print(f"{prefix} {msg}")
LINE  53 | 
LINE  54 | 
LINE  55 | def info(msg):  _log("[INFO]", msg)
LINE  56 | def ok(msg):    _log("[OK]", msg)
LINE  57 | def skip(msg):  _log("[SKIP]", msg)
LINE  58 | def error(msg): _log("[ERROR]", msg); STATS["errors"] += 1
LINE  59 | 
LINE  60 | 
LINE  61 | # ---------------------------------------------------------------------------
LINE  62 | # Helpers de I/O y validación
LINE  63 | # ---------------------------------------------------------------------------
LINE  64 | 
LINE  65 | def ensure_target_exists(root: Path, rel_path: str) -> Path:
LINE  66 |     p = root / rel_path
LINE  67 |     if not p.is_file():
LINE  68 |         raise RuntimeError(f"Archivo objetivo no encontrado: {p}")
LINE  69 |     info(f"Archivo encontrado: {rel_path}")
LINE  70 |     return p
LINE  71 | 
LINE  72 | 
LINE  73 | def backup_file(root: Path, rel_path: str) -> None:
LINE  74 |     src = root / rel_path
LINE  75 |     if not src.is_file():
LINE  76 |         return
LINE  77 |     dst = root / BACKUP_DIRNAME / rel_path
LINE  78 |     dst.parent.mkdir(parents=True, exist_ok=True)
LINE  79 |     shutil.copy2(src, dst)
LINE  80 |     STATS["backups"] += 1
LINE  81 |     info(f"Backup creado: {dst.relative_to(root)}")
LINE  82 | 
LINE  83 | 
LINE  84 | def write_new_file(root: Path, rel_path: str, content: str) -> None:
LINE  85 |     target = root / rel_path
LINE  86 |     if target.exists():
LINE  87 |         existing = target.read_text(encoding="utf-8", errors="ignore")
LINE  88 |         if content.strip() and content.strip() in existing:
LINE  89 |             skip(f"Archivo ya presente y correcto: {rel_path}")
LINE  90 |             STATS["skipped"] += 1
LINE  91 |             return
LINE  92 |         skip(f"Archivo ya existe (no se sobreescribe): {rel_path}")
LINE  93 |         STATS["skipped"] += 1
LINE  94 |         return
LINE  95 |     target.parent.mkdir(parents=True, exist_ok=True)
LINE  96 |     target.write_text(content, encoding="utf-8")
LINE  97 |     STATS["created"] += 1
LINE  98 |     ok(f"Archivo creado: {rel_path}")
LINE  99 | 
LINE 100 | 
LINE 101 | def _apply_change(root: Path, rel_path: str, new_content: str) -> None:
LINE 102 |     backup_file(root, rel_path)
LINE 103 |     (root / rel_path).write_text(new_content, encoding="utf-8")
LINE 104 |     STATS["modified"] += 1
LINE 105 |     ok(f"Cambio aplicado: {rel_path}")
LINE 106 | 
LINE 107 | 
LINE 108 | def insert_after(root: Path, rel_path: str, anchor: str,
LINE 109 |                  block: str, marker: str) -> None:
LINE 110 |     content = (root / rel_path).read_text(encoding="utf-8")
LINE 111 |     if marker in content:
LINE 112 |         skip(f"Cambio ya aplicado: {rel_path} (marcador presente)")
LINE 113 |         STATS["skipped"] += 1
LINE 114 |         return
LINE 115 |     idx = content.find(anchor)
LINE 116 |     if idx == -1:
LINE 117 |         raise RuntimeError(
LINE 118 |             f"Ancla no encontrada en {rel_path}:\n  {anchor!r}"
LINE 119 |         )
LINE 120 |     end = idx + len(anchor)
LINE 121 |     new_content = content[:end] + "\n" + block + content[end:]
LINE 122 |     _apply_change(root, rel_path, new_content)
LINE 123 | 
LINE 124 | 
LINE 125 | def insert_before(root: Path, rel_path: str, anchor: str,
LINE 126 |                   block: str, marker: str) -> None:
LINE 127 |     content = (root / rel_path).read_text(encoding="utf-8")
LINE 128 |     if marker in content:
LINE 129 |         skip(f"Cambio ya aplicado: {rel_path} (marcador presente)")
LINE 130 |         STATS["skipped"] += 1
LINE 131 |         return
LINE 132 |     idx = content.find(anchor)
LINE 133 |     if idx == -1:
LINE 134 |         raise RuntimeError(
LINE 135 |             f"Ancla no encontrada en {rel_path}:\n  {anchor!r}"
LINE 136 |         )
LINE 137 |     new_content = content[:idx] + block + "\n" + content[idx:]
LINE 138 |     _apply_change(root, rel_path, new_content)
LINE 139 | 
LINE 140 | 
LINE 141 | def replace_exact(root: Path, rel_path: str, old: str, new: str) -> None:
LINE 142 |     content = (root / rel_path).read_text(encoding="utf-8")
LINE 143 |     if old not in content:
LINE 144 |         if new in content:
LINE 145 |             skip(f"Reemplazo ya aplicado: {rel_path}")
LINE 146 |         else:
LINE 147 |             skip(f"Patrón no encontrado en {rel_path} (posible versión distinta)")
LINE 148 |         STATS["skipped"] += 1
LINE 149 |         return
LINE 150 |     new_content = content.replace(old, new, 1)
LINE 151 |     _apply_change(root, rel_path, new_content)
LINE 152 | 
LINE 153 | 
LINE 154 | # ---------------------------------------------------------------------------
LINE 155 | # Contenido de archivos nuevos
LINE 156 | # ---------------------------------------------------------------------------
LINE 157 | 
LINE 158 | STORAGE_INIT_PY = '''"""Phase 1 SQLite persistence package."""
LINE 159 | from app.core.storage.database import Database, get_database, default_db_path
LINE 160 | 
LINE 161 | __all__ = ["Database", "get_database", "default_db_path"]
LINE 162 | '''
LINE 163 | 
LINE 164 | 
LINE 165 | DATABASE_PY = '''"""
LINE 166 | SQLite persistence layer for project nodes, metrics and dependencies (Phase 1).
LINE 167 | 
LINE 168 | This module is intentionally restricted to:
LINE 169 |   - Opening / creating the SQLite database.
LINE 170 |   - Initializing the schema.
LINE 171 |   - Executing queries and updates.
LINE 172 |   - Managing transactions.
LINE 173 |   - Providing the CRUD operations required for projects and nodes.
LINE 174 | 
LINE 175 | No Delta Scan or incremental change detection logic is implemented here.
LINE 176 | """
LINE 177 | import os
LINE 178 | import sqlite3
LINE 179 | from typing import Dict, List, Optional, Set, Tuple
LINE 180 | 
LINE 181 | 
LINE 182 | # ---------------------------------------------------------------------------
LINE 183 | # Path resolution
LINE 184 | # ---------------------------------------------------------------------------
LINE 185 | 
LINE 186 | def _find_project_root() -> Optional[str]:
LINE 187 |     """Walk up from this file to find the project root (contains main.py)."""
LINE 188 |     here = os.path.dirname(os.path.abspath(__file__))
LINE 189 |     candidate = os.path.abspath(os.path.join(here, "..", "..", ".."))
LINE 190 |     if os.path.isfile(os.path.join(candidate, "main.py")):
LINE 191 |         return candidate
LINE 192 |     return None
LINE 193 | 
LINE 194 | 
LINE 195 | def default_db_path() -> str:
LINE 196 |     """Resolve project_cache.db path.
LINE 197 | 
LINE 198 |     Prefer <project_root>/.cache/project_cache.db, fallback to
LINE 199 |     ~/.analyzer_app/project_cache.db when the project root cannot be resolved.
LINE 200 |     """
LINE 201 |     root = _find_project_root()
LINE 202 |     if root:
LINE 203 |         return os.path.join(root, ".cache", "project_cache.db")
LINE 204 |     home = os.path.expanduser("~")
LINE 205 |     return os.path.join(home, ".analyzer_app", "project_cache.db")
LINE 206 | 
LINE 207 | 
LINE 208 | # ---------------------------------------------------------------------------
LINE 209 | # Schema
LINE 210 | # ---------------------------------------------------------------------------
LINE 211 | 
LINE 212 | SCHEMA_STATEMENTS = [
LINE 213 |     """CREATE TABLE IF NOT EXISTS projects (
LINE 214 |         id INTEGER PRIMARY KEY AUTOINCREMENT,
LINE 215 |         path TEXT UNIQUE NOT NULL,
LINE 216 |         project_type TEXT,
LINE 217 |         framework TEXT,
LINE 218 |         last_scanned TIMESTAMP DEFAULT CURRENT_TIMESTAMP
LINE 219 |     )""",
LINE 220 |     """CREATE TABLE IF NOT EXISTS nodes (
LINE 221 |         id INTEGER PRIMARY KEY AUTOINCREMENT,
LINE 222 |         project_id INTEGER NOT NULL,
LINE 223 |         rel_path TEXT NOT NULL,
LINE 224 |         parent_path TEXT,
LINE 225 |         is_dir BOOLEAN NOT NULL,
LINE 226 |         mtime REAL NOT NULL,
LINE 227 |         lines_count INTEGER DEFAULT 0,
LINE 228 |         file_size INTEGER DEFAULT 0,
LINE 229 |         is_important BOOLEAN DEFAULT 0,
LINE 230 |         is_checked BOOLEAN DEFAULT 1,
LINE 231 |         FOREIGN KEY(project_id) REFERENCES projects(id) ON DELETE CASCADE,
LINE 232 |         UNIQUE(project_id, rel_path)
LINE 233 |     )""",
LINE 234 |     """CREATE TABLE IF NOT EXISTS node_dependencies (
LINE 235 |         id INTEGER PRIMARY KEY AUTOINCREMENT,
LINE 236 |         source_node_id INTEGER NOT NULL,
LINE 237 |         target_path TEXT NOT NULL,
LINE 238 |         FOREIGN KEY(source_node_id) REFERENCES nodes(id) ON DELETE CASCADE
LINE 239 |     )""",
LINE 240 |     "CREATE INDEX IF NOT EXISTS idx_nodes_rel_path ON nodes(project_id, rel_path)",
LINE 241 |     "CREATE INDEX IF NOT EXISTS idx_nodes_parent ON nodes(project_id, parent_path)",
LINE 242 | ]
LINE 243 | 
LINE 244 | 
LINE 245 | # ---------------------------------------------------------------------------
LINE 246 | # Database
LINE 247 | # ---------------------------------------------------------------------------
LINE 248 | 
LINE 249 | class Database:
LINE 250 |     """Thin SQLite wrapper for the project cache (Phase 1)."""
LINE 251 | 
LINE 252 |     def __init__(self, db_path: Optional[str] = None):
LINE 253 |         self.db_path = db_path or default_db_path()
LINE 254 |         os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
LINE 255 |         self._conn = sqlite3.connect(self.db_path)
LINE 256 |         self._conn.row_factory = sqlite3.Row
LINE 257 |         self._conn.execute("PRAGMA foreign_keys = ON")
LINE 258 |         self._init_schema()
LINE 259 | 
LINE 260 |     def _init_schema(self) -> None:
LINE 261 |         with self._conn:
LINE 262 |             for stmt in SCHEMA_STATEMENTS:
LINE 263 |                 self._conn.execute(stmt)
LINE 264 | 
LINE 265 |     # ---------- projects ----------
LINE 266 | 
LINE 267 |     def get_or_create_project(self, path: str,
LINE 268 |                               project_type: Optional[str] = None,
LINE 269 |                               framework: Optional[str] = None) -> int:
LINE 270 |         cur = self._conn.cursor()
LINE 271 |         cur.execute("SELECT id FROM projects WHERE path = ?", (path,))
LINE 272 |         row = cur.fetchone()
LINE 273 |         if row:
LINE 274 |             return int(row["id"])
LINE 275 |         cur.execute(
LINE 276 |             "INSERT INTO projects (path, project_type, framework) VALUES (?, ?, ?)",
LINE 277 |             (path, project_type, framework),
LINE 278 |         )
LINE 279 |         self._conn.commit()
LINE 280 |         return int(cur.lastrowid)
LINE 281 | 
LINE 282 |     def get_project_by_path(self, path: str) -> Optional[Dict]:
LINE 283 |         cur = self._conn.cursor()
LINE 284 |         cur.execute("SELECT * FROM projects WHERE path = ?", (path,))
LINE 285 |         row = cur.fetchone()
LINE 286 |         return dict(row) if row else None
LINE 287 | 
LINE 288 |     def update_last_scanned(self, project_id: int) -> None:
LINE 289 |         with self._conn:
LINE 290 |             self._conn.execute(
LINE 291 |                 "UPDATE projects SET last_scanned = CURRENT_TIMESTAMP WHERE id = ?",
LINE 292 |                 (project_id,),
LINE 293 |             )
LINE 294 | 
LINE 295 |     def delete_project(self, path: str) -> None:
LINE 296 |         with self._conn:
LINE 297 |             self._conn.execute("DELETE FROM projects WHERE path = ?", (path,))
LINE 298 | 
LINE 299 |     # ---------- nodes ----------
LINE 300 | 
LINE 301 |     def replace_nodes(self, project_id: int, nodes: List[Dict]) -> None:
LINE 302 |         """Delete existing nodes for project and insert the new batch atomically."""
LINE 303 |         rows = [
LINE 304 |             (
LINE 305 |                 project_id,
LINE 306 |                 n["rel_path"],
LINE 307 |                 n.get("parent_path"),
LINE 308 |                 int(bool(n.get("is_dir", 0))),
LINE 309 |                 float(n.get("mtime", 0.0) or 0.0),
LINE 310 |                 int(n.get("lines_count", 0) or 0),
LINE 311 |                 int(n.get("file_size", 0) or 0),
LINE 312 |                 int(bool(n.get("is_important", 0))),
LINE 313 |                 int(bool(n.get("is_checked", 1))),
LINE 314 |             )
LINE 315 |             for n in nodes
LINE 316 |         ]
LINE 317 |         with self._conn:
LINE 318 |             self._conn.execute("DELETE FROM nodes WHERE project_id = ?", (project_id,))
LINE 319 |             if rows:
LINE 320 |                 self._conn.executemany(
LINE 321 |                     """INSERT INTO nodes
LINE 322 |                        (project_id, rel_path, parent_path, is_dir, mtime,
LINE 323 |                         lines_count, file_size, is_important, is_checked)
LINE 324 |                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
LINE 325 |                     rows,
LINE 326 |                 )
LINE 327 | 
LINE 328 |     def get_nodes(self, project_id: int) -> List[Dict]:
LINE 329 |         cur = self._conn.cursor()
LINE 330 |         cur.execute("SELECT * FROM nodes WHERE project_id = ?", (project_id,))
LINE 331 |         return [dict(r) for r in cur.fetchall()]
LINE 332 | 
LINE 333 |     def update_is_checked(self, project_id: int,
LINE 334 |                           rel_path: str, is_checked: bool) -> None:
LINE 335 |         with self._conn:
LINE 336 |             self._conn.execute(
LINE 337 |                 "UPDATE nodes SET is_checked = ? "
LINE 338 |                 "WHERE project_id = ? AND rel_path = ?",
LINE 339 |                 (int(bool(is_checked)), project_id, rel_path),
LINE 340 |             )
LINE 341 | 
LINE 342 |     def update_is_checked_batch(self, project_id: int,
LINE 343 |                                 updates: List[Tuple[str, bool]]) -> None:
LINE 344 |         rows = [(int(bool(c)), project_id, rp) for rp, c in updates]
LINE 345 |         if not rows:
LINE 346 |             return
LINE 347 |         with self._conn:
LINE 348 |             self._conn.executemany(
LINE 349 |                 "UPDATE nodes SET is_checked = ? "
LINE 350 |                 "WHERE project_id = ? AND rel_path = ?",
LINE 351 |                 rows,
LINE 352 |             )
LINE 353 | 
LINE 354 |     def load_checked_state(self, project_path: str) -> Optional[Set[str]]:
LINE 355 |         """Return the set of checked rel_paths (files only).
LINE 356 | 
LINE 357 |         Returns None when there is no persisted data for this project,
LINE 358 |         so the caller can distinguish "never saved" from "all unchecked".
LINE 359 |         """
LINE 360 |         cur = self._conn.cursor()
LINE 361 |         cur.execute("SELECT id FROM projects WHERE path = ?", (project_path,))
LINE 362 |         row = cur.fetchone()
LINE 363 |         if not row:
LINE 364 |             return None
LINE 365 |         project_id = int(row["id"])
LINE 366 |         cur.execute(
LINE 367 |             "SELECT rel_path, is_checked FROM nodes "
LINE 368 |             "WHERE project_id = ? AND is_dir = 0",
LINE 369 |             (project_id,),
LINE 370 |         )
LINE 371 |         rows = cur.fetchall()
LINE 372 |         if not rows:
LINE 373 |             return None
LINE 374 |         return {r["rel_path"] for r in rows if r["is_checked"]}
LINE 375 | 
LINE 376 |     def delete_nodes(self, project_id: int) -> None:
LINE 377 |         with self._conn:
LINE 378 |             self._conn.execute("DELETE FROM nodes WHERE project_id = ?", (project_id,))
LINE 379 | 
LINE 380 |     # ---------- dependencies ----------
LINE 381 | 
LINE 382 |     def save_dependencies_batch(self, project_id: int,
LINE 383 |                                 deps: List[Tuple[str, str]]) -> None:
LINE 384 |         """deps: list of (source_rel_path, target_path)."""
LINE 385 |         if not deps:
LINE 386 |             return
LINE 387 |         cur = self._conn.cursor()
LINE 388 |         cur.execute("SELECT id, rel_path FROM nodes WHERE project_id = ?", (project_id,))
LINE 389 |         id_map = {r["rel_path"]: int(r["id"]) for r in cur.fetchall()}
LINE 390 | 
LINE 391 |         rows = []
LINE 392 |         for src_rel, target in deps:
LINE 393 |             node_id = id_map.get(src_rel)
LINE 394 |             if node_id is None:
LINE 395 |                 continue
LINE 396 |             rows.append((node_id, target))
LINE 397 | 
LINE 398 |         with self._conn:
LINE 399 |             self._conn.execute(
LINE 400 |                 """DELETE FROM node_dependencies
LINE 401 |                    WHERE source_node_id IN
LINE 402 |                          (SELECT id FROM nodes WHERE project_id = ?)""",
LINE 403 |                 (project_id,),
LINE 404 |             )
LINE 405 |             if rows:
LINE 406 |                 self._conn.executemany(
LINE 407 |                     "INSERT INTO node_dependencies (source_node_id, target_path) "
LINE 408 |                     "VALUES (?, ?)",
LINE 409 |                     rows,
LINE 410 |                 )
LINE 411 | 
LINE 412 |     def get_dependencies(self, project_id: int) -> List[Dict]:
LINE 413 |         cur = self._conn.cursor()
LINE 414 |         cur.execute(
LINE 415 |             """SELECT n.rel_path AS source_path, d.target_path AS target_path
LINE 416 |                FROM node_dependencies d
LINE 417 |                JOIN nodes n ON n.id = d.source_node_id
LINE 418 |                WHERE n.project_id = ?""",
LINE 419 |             (project_id,),
LINE 420 |         )
LINE 421 |         return [dict(r) for r in cur.fetchall()]
LINE 422 | 
LINE 423 |     def close(self) -> None:
LINE 424 |         try:
LINE 425 |             self._conn.close()
LINE 426 |         except Exception:
LINE 427 |             pass
LINE 428 | 
LINE 429 | 
LINE 430 | # ---------------------------------------------------------------------------
LINE 431 | # Singleton accessor
LINE 432 | # ---------------------------------------------------------------------------
LINE 433 | 
LINE 434 | _db_singleton: Optional[Database] = None
LINE 435 | 
LINE 436 | 
LINE 437 | def get_database(db_path: Optional[str] = None) -> Database:
LINE 438 |     """Return the process-wide Database singleton."""
LINE 439 |     global _db_singleton
LINE 440 |     if _db_singleton is None or (db_path and db_path != _db_singleton.db_path):
LINE 441 |         _db_singleton = Database(db_path)
LINE 442 |     return _db_singleton
LINE 443 | 
LINE 444 | 
LINE 445 | def reset_database_singleton() -> None:
LINE 446 |     """For tests: close and drop the current singleton."""
LINE 447 |     global _db_singleton
LINE 448 |     if _db_singleton is not None:
LINE 449 |         _db_singleton.close()
LINE 450 |     _db_singleton = None
LINE 451 | '''
LINE 452 | 
LINE 453 | 
LINE 454 | # ---------------------------------------------------------------------------
LINE 455 | # Bloques a insertar en archivos existentes
LINE 456 | # ---------------------------------------------------------------------------
LINE 457 | 
LINE 458 | # --- ProjectAnalyzer.persist_result -----------------------------------------
LINE 459 | 
LINE 460 | PERSIST_RESULT_BLOCK = '''    # === PERSISTENCE: PHASE1 (persist_result) ===
LINE 461 |     def persist_result(self, result) -> None:
LINE 462 |         """Persist a ProjectAnalysisResult to the SQLite cache (Phase 1).
LINE 463 | 
LINE 464 |         This method is additive and does not modify the existing analyze()
LINE 465 |         pipeline, its return type, or FileMetric structure.
LINE 466 |         """
LINE 467 |         try:
LINE 468 |             from app.core.storage.database import get_database
LINE 469 |         except Exception:
LINE 470 |             return
LINE 471 | 
LINE 472 |         folder = getattr(result, "folder_path", None)
LINE 473 |         if not folder or not os.path.isdir(folder):
LINE 474 |             return
LINE 475 | 
LINE 476 |         try:
LINE 477 |             db = get_database()
LINE 478 |         except Exception:
LINE 479 |             return
LINE 480 | 
LINE 481 |         project_id = db.get_or_create_project(
LINE 482 |             path=folder,
LINE 483 |             project_type=getattr(result, "primary_language", None),
LINE 484 |             framework=getattr(result, "framework", None),
LINE 485 |         )
LINE 486 | 
LINE 487 |         # Preserve previously persisted is_checked state
LINE 488 |         existing_checked = db.load_checked_state(folder)
LINE 489 | 
LINE 490 |         important = set(getattr(result, "important_files", []) or [])
LINE 491 |         nodes = []
LINE 492 | 
LINE 493 |         for dirpath, dirnames, filenames in os.walk(folder):
LINE 494 |             dirnames[:] = [d for d in dirnames if d not in self.excluded_dirs]
LINE 495 |             rel_dir = os.path.relpath(dirpath, folder)
LINE 496 | 
LINE 497 |             if rel_dir != ".":
LINE 498 |                 rel_norm = rel_dir.replace("\\\\", "/")
LINE 499 |                 parent = os.path.dirname(rel_norm).replace("\\\\", "/") or None
LINE 500 |                 try:
LINE 501 |                     mtime = float(os.stat(dirpath).st_mtime)
LINE 502 |                 except Exception:
LINE 503 |                     mtime = 0.0
LINE 504 |                 nodes.append({
LINE 505 |                     "rel_path": rel_norm,
LINE 506 |                     "parent_path": parent,
LINE 507 |                     "is_dir": 1,
LINE 508 |                     "mtime": mtime,
LINE 509 |                     "lines_count": 0,
LINE 510 |                     "file_size": 0,
LINE 511 |                     "is_important": 0,
LINE 512 |                     "is_checked": 0,
LINE 513 |                 })
LINE 514 | 
LINE 515 |             for f in filenames:
LINE 516 |                 full = os.path.join(dirpath, f)
LINE 517 |                 if is_binary_file(full):
LINE 518 |                     continue
LINE 519 |                 rel_file = f if rel_dir == "." else os.path.join(rel_dir, f)
LINE 520 |                 rel_file = rel_file.replace("\\\\", "/")
LINE 521 |                 try:
LINE 522 |                     st = os.stat(full)
LINE 523 |                     mtime = float(st.st_mtime)
LINE 524 |                     size = int(st.st_size)
LINE 525 |                 except Exception:
LINE 526 |                     mtime = 0.0
LINE 527 |                     size = 0
LINE 528 |                 parent = os.path.dirname(rel_file).replace("\\\\", "/") or None
LINE 529 | 
LINE 530 |                 if existing_checked is None:
LINE 531 |                     is_checked = 1
LINE 532 |                 else:
LINE 533 |                     is_checked = 1 if rel_file in existing_checked else 0
LINE 534 | 
LINE 535 |                 nodes.append({
LINE 536 |                     "rel_path": rel_file,
LINE 537 |                     "parent_path": parent,
LINE 538 |                     "is_dir": 0,
LINE 539 |                     "mtime": mtime,
LINE 540 |                     "lines_count": 0,
LINE 541 |                     "file_size": size,
LINE 542 |                     "is_important": 1 if rel_file in important else 0,
LINE 543 |                     "is_checked": is_checked,
LINE 544 |                 })
LINE 545 | 
LINE 546 |         try:
LINE 547 |             db.replace_nodes(project_id, nodes)
LINE 548 | 
LINE 549 |             dep_pairs = []
LINE 550 |             code_deps = getattr(result, "code_dependencies", {}) or {}
LINE 551 |             for rel_path, deps in code_deps.items():
LINE 552 |                 for d in deps:
LINE 553 |                     dep_pairs.append((rel_path, d))
LINE 554 |             db.save_dependencies_batch(project_id, dep_pairs)
LINE 555 | 
LINE 556 |             db.update_last_scanned(project_id)
LINE 557 |         except Exception:
LINE 558 |             pass
LINE 559 |     # === END PERSISTENCE: PHASE1 (persist_result) ===
LINE 560 | '''
LINE 561 | 
LINE 562 | 
LINE 563 | # --- CheckboxTreeview -------------------------------------------------------
LINE 564 | 
LINE 565 | FILE_TREE_ATTRS_BLOCK = '''        # === PERSISTENCE: PHASE1 (attrs) ===
LINE 566 |         self._on_check_change = None
LINE 567 |         # === END PERSISTENCE: PHASE1 (attrs) ===
LINE 568 | '''
LINE 569 | 
LINE 570 | FILE_TREE_METHODS_BLOCK = '''    # === PERSISTENCE: PHASE1 (methods) ===
LINE 571 |     def set_check_change_callback(self, callback) -> None:
LINE 572 |         """Register callback(rel_path: str, is_checked: bool) for persistence."""
LINE 573 |         self._on_check_change = callback
LINE 574 | 
LINE 575 |     def _notify_check_change(self, rel_path: str, is_checked: bool) -> None:
LINE 576 |         if not self._on_check_change or not rel_path:
LINE 577 |             return
LINE 578 |         try:
LINE 579 |             self._on_check_change(rel_path, is_checked)
LINE 580 |         except Exception:
LINE 581 |             pass
LINE 582 |     # === END PERSISTENCE: PHASE1 (methods) ===
LINE 583 | '''
LINE 584 | 
LINE 585 | 
LINE 586 | FILE_TREE_CHECK_OLD = '''    def check_item(self, item):
LINE 587 |         rel_path = self.set(item, "name")
LINE 588 |         if rel_path:
LINE 589 |             self.set(item, "check", "☑")
LINE 590 |             self.item(item, tags=("checked",))
LINE 591 |             if not self.get_children(item):
LINE 592 |                 self.checked_items.add(rel_path)
LINE 593 |         for child in self.get_children(item):
LINE 594 |             self.check_item(child)
LINE 595 | '''
LINE 596 | 
LINE 597 | FILE_TREE_CHECK_NEW = '''    def check_item(self, item):
LINE 598 |         rel_path = self.set(item, "name")
LINE 599 |         if rel_path:
LINE 600 |             was_checked = rel_path in self.checked_items
LINE 601 |             self.set(item, "check", "☑")
LINE 602 |             self.item(item, tags=("checked",))
LINE 603 |             if not self.get_children(item):
LINE 604 |                 self.checked_items.add(rel_path)
LINE 605 |                 if not was_checked:
LINE 606 |                     self._notify_check_change(rel_path, True)
LINE 607 |         for child in self.get_children(item):
LINE 608 |             self.check_item(child)
LINE 609 | '''
LINE 610 | 
LINE 611 | 
LINE 612 | FILE_TREE_UNCHECK_OLD = '''    def uncheck_item(self, item):
LINE 613 |         rel_path = self.set(item, "name")
LINE 614 |         if rel_path:
LINE 615 |             self.set(item, "check", "☐")
LINE 616 |             self.item(item, tags=("unchecked",))
LINE 617 |             if rel_path in self.checked_items:
LINE 618 |                 self.checked_items.remove(rel_path)
LINE 619 |         for child in self.get_children(item):
LINE 620 |             self.uncheck_item(child)
LINE 621 | '''
LINE 622 | 
LINE 623 | FILE_TREE_UNCHECK_NEW = '''    def uncheck_item(self, item):
LINE 624 |         rel_path = self.set(item, "name")
LINE 625 |         if rel_path:
LINE 626 |             was_checked = rel_path in self.checked_items
LINE 627 |             self.set(item, "check", "☐")
LINE 628 |             self.item(item, tags=("unchecked",))
LINE 629 |             if rel_path in self.checked_items:
LINE 630 |                 self.checked_items.remove(rel_path)
LINE 631 |             if was_checked:
LINE 632 |                 self._notify_check_change(rel_path, False)
LINE 633 |         for child in self.get_children(item):
LINE 634 |             self.uncheck_item(child)
LINE 635 | '''
LINE 636 | 
LINE 637 | 
LINE 638 | # --- MainWindow -------------------------------------------------------------
LINE 639 | 
LINE 640 | MW_IMPORT_BLOCK = '''# === PERSISTENCE: PHASE1 (imports) ===
LINE 641 | from app.core.storage.database import get_database
LINE 642 | # === END PERSISTENCE: PHASE1 (imports) ===
LINE 643 | '''
LINE 644 | 
LINE 645 | MW_INIT_BLOCK = '''        # === PERSISTENCE: PHASE1 (init) ===
LINE 646 |         self._persist_db = None
LINE 647 |         try:
LINE 648 |             self._persist_db = get_database()
LINE 649 |         except Exception:
LINE 650 |             self._persist_db = None
LINE 651 |         # === END PERSISTENCE: PHASE1 (init) ===
LINE 652 | '''
LINE 653 | 
LINE 654 | MW_CALLBACK_BLOCK = '''        # === PERSISTENCE: PHASE1 (callback) ===
LINE 655 |         if self._persist_db is not None:
LINE 656 |             self.tree.set_check_change_callback(self._on_tree_check_change)
LINE 657 |         # === END PERSISTENCE: PHASE1 (callback) ===
LINE 658 | '''
LINE 659 | 
LINE 660 | MW_METHOD_BLOCK = '''    # === PERSISTENCE: PHASE1 (method) ===
LINE 661 |     def _on_tree_check_change(self, rel_path: str, is_checked: bool):
LINE 662 |         """Persist checkbox changes to SQLite (Phase 1)."""
LINE 663 |         if self._persist_db is None:
LINE 664 |             return
LINE 665 |         folder = self.var_folder.get()
LINE 666 |         if not folder:
LINE 667 |             return
LINE 668 |         try:
LINE 669 |             project_id = self._persist_db.get_or_create_project(folder)
LINE 670 |             self._persist_db.update_is_checked(project_id, rel_path, is_checked)
LINE 671 |         except Exception:
LINE 672 |             pass
LINE 673 |     # === END PERSISTENCE: PHASE1 (method) ===
LINE 674 | '''
LINE 675 | 
LINE 676 | MW_RELOAD_BLOCK = '''        # === PERSISTENCE: PHASE1 (reload) ===
LINE 677 |         if self._persist_db is not None:
LINE 678 |             try:
LINE 679 |                 saved = self._persist_db.load_checked_state(folder)
LINE 680 |                 if saved is not None:
LINE 681 |                     self.tree.set_checked_files(saved)
LINE 682 |                     self.selector.set_checked_folder_files(
LINE 683 |                         self.tree.get_checked_files()
LINE 684 |                     )
LINE 685 |             except Exception:
LINE 686 |                 pass
LINE 687 |         # === END PERSISTENCE: PHASE1 (reload) ===
LINE 688 | '''
LINE 689 | 
LINE 690 | MW_ANALYZE_BLOCK = '''        # === PERSISTENCE: PHASE1 (analyze) ===
LINE 691 |         try:
LINE 692 |             analyzer.persist_result(result)
LINE 693 |         except Exception:
LINE 694 |             pass
LINE 695 |         # === END PERSISTENCE: PHASE1 (analyze) ===
LINE 696 | '''
LINE 697 | 
LINE 698 | 
LINE 699 | # ---------------------------------------------------------------------------
LINE 700 | # Aplicación de cambios
LINE 701 | # ---------------------------------------------------------------------------
LINE 702 | 
LINE 703 | REQUIRED_FILES = [
LINE 704 |     "app/__init__.py",
LINE 705 |     "app/core/__init__.py",
LINE 706 |     "app/core/project_analyzer.py",
LINE 707 |     "app/gui/file_tree.py",
LINE 708 |     "app/gui/main_window.py",
LINE 709 |     "app/models/project.py",
LINE 710 |     "main.py",
LINE 711 | ]
LINE 712 | 
LINE 713 | 
LINE 714 | def verify_structure(root: Path) -> None:
LINE 715 |     info(f"Proyecto detectado: {root}")
LINE 716 |     missing = []
LINE 717 |     for rel in REQUIRED_FILES:
LINE 718 |         p = root / rel
LINE 719 |         if not p.is_file():
LINE 720 |             missing.append(rel)
LINE 721 |     if missing:
LINE 722 |         for m in missing:
LINE 723 |             error(f"Falta archivo requerido: {m}")
LINE 724 |         raise RuntimeError(
LINE 725 |             "La estructura del proyecto no coincide con la esperada. "
LINE 726 |             "Abortando sin modificar archivos."
LINE 727 |         )
LINE 728 | 
LINE 729 | 
LINE 730 | def apply_all(root: Path) -> None:
LINE 731 |     info("--- Verificando estructura del proyecto ---")
LINE 732 |     verify_structure(root)
LINE 733 | 
LINE 734 |     info("--- Creando archivos nuevos ---")
LINE 735 |     write_new_file(root, "app/core/storage/__init__.py", STORAGE_INIT_PY)
LINE 736 |     write_new_file(root, "app/core/storage/database.py", DATABASE_PY)
LINE 737 | 
LINE 738 |     info("--- Modificando app/core/project_analyzer.py ---")
LINE 739 |     ensure_target_exists(root, "app/core/project_analyzer.py")
LINE 740 |     insert_before(
LINE 741 |         root, "app/core/project_analyzer.py",
LINE 742 |         anchor="    def _is_entry_point(self, rel_path: str) -> bool:",
LINE 743 |         block=PERSIST_RESULT_BLOCK,
LINE 744 |         marker="# === PERSISTENCE: PHASE1 (persist_result) ===",
LINE 745 |     )
LINE 746 | 
LINE 747 |     info("--- Modificando app/gui/file_tree.py ---")
LINE 748 |     ensure_target_exists(root, "app/gui/file_tree.py")
LINE 749 |     insert_after(
LINE 750 |         root, "app/gui/file_tree.py",
LINE 751 |         anchor="        self.checked_items: Set[str] = set()",
LINE 752 |         block=FILE_TREE_ATTRS_BLOCK,
LINE 753 |         marker="# === PERSISTENCE: PHASE1 (attrs) ===",
LINE 754 |     )
LINE 755 |     insert_before(
LINE 756 |         root, "app/gui/file_tree.py",
LINE 757 |         anchor="    def insert_file(self, parent, rel_path: str, is_checked: bool = True):",
LINE 758 |         block=FILE_TREE_METHODS_BLOCK,
LINE 759 |         marker="# === PERSISTENCE: PHASE1 (methods) ===",
LINE 760 |     )
LINE 761 |     replace_exact(root, "app/gui/file_tree.py",
LINE 762 |                   FILE_TREE_CHECK_OLD, FILE_TREE_CHECK_NEW)
LINE 763 |     replace_exact(root, "app/gui/file_tree.py",
LINE 764 |                   FILE_TREE_UNCHECK_OLD, FILE_TREE_UNCHECK_NEW)
LINE 765 | 
LINE 766 |     info("--- Modificando app/gui/main_window.py ---")
LINE 767 |     ensure_target_exists(root, "app/gui/main_window.py")
LINE 768 | 
LINE 769 |     # 1. Import
LINE 770 |     insert_after(
LINE 771 |         root, "app/gui/main_window.py",
LINE 772 |         anchor=("from app.gui.dependency_tree_dialog import DependencyTreeDialog\n"
LINE 773 |                 "# === END AUTO-GENERATED ==="),
LINE 774 |         block=MW_IMPORT_BLOCK,
LINE 775 |         marker="# === PERSISTENCE: PHASE1 (imports) ===",
LINE 776 |     )
LINE 777 | 
LINE 778 |     # 2. Init del estado de persistencia
LINE 779 |     insert_after(
LINE 780 |         root, "app/gui/main_window.py",
LINE 781 |         anchor="        self.config     = ExportConfig()",
LINE 782 |         block=MW_INIT_BLOCK,
LINE 783 |         marker="# === PERSISTENCE: PHASE1 (init) ===",
LINE 784 |     )
LINE 785 | 
LINE 786 |     # 3. Registrar callback en el árbol
LINE 787 |     insert_after(
LINE 788 |         root, "app/gui/main_window.py",
LINE 789 |         anchor=('        self.tree.bind("<ButtonRelease-1>",  '
LINE 790 |                 'lambda _: self.root.after(50, self._refresh_selection_stats))'),
LINE 791 |         block=MW_CALLBACK_BLOCK,
LINE 792 |         marker="# === PERSISTENCE: PHASE1 (callback) ===",
LINE 793 |     )
LINE 794 | 
LINE 795 |     # 4. Insertar método _on_tree_check_change antes del bloque de handlers
LINE 796 |     insert_before(
LINE 797 |         root, "app/gui/main_window.py",
LINE 798 |         anchor=("    # ── UI event handlers "
LINE 799 |                 "────────────────────────────────────────────────"
LINE 800 |                 "─────────────────"),
LINE 801 |         block=MW_METHOD_BLOCK,
LINE 802 |         marker="# === PERSISTENCE: PHASE1 (method) ===",
LINE 803 |     )
LINE 804 | 
LINE 805 |     # 5. Restaurar estado al recargar el árbol
LINE 806 |     insert_after(
LINE 807 |         root, "app/gui/main_window.py",
LINE 808 |         anchor=('                rel_file = os.path.join(rel_dir, f) '
LINE 809 |                 'if rel_dir != "." else f\n'
LINE 810 |                 '                self.tree.insert_file(parent_item, rel_file)'),
LINE 811 |         block=MW_RELOAD_BLOCK,
LINE 812 |         marker="# === PERSISTENCE: PHASE1 (reload) ===",
LINE 813 |     )
LINE 814 | 
LINE 815 |     # 6. Persistir tras el análisis
LINE 816 |     insert_after(
LINE 817 |         root, "app/gui/main_window.py",
LINE 818 |         anchor=("        result = analyzer.analyze(folder, "
LINE 819 |                 "max_file_size_mb=max_file_mb)"),
LINE 820 |         block=MW_ANALYZE_BLOCK,
LINE 821 |         marker="# === PERSISTENCE: PHASE1 (analyze) ===",
LINE 822 |     )
LINE 823 | 
LINE 824 | 
LINE 825 | # ---------------------------------------------------------------------------
LINE 826 | # Validación final
LINE 827 | # ---------------------------------------------------------------------------
LINE 828 | 
LINE 829 | def validate_syntax(root: Path, rel_paths) -> None:
LINE 830 |     info("--- Validando sintaxis (py_compile) ---")
LINE 831 |     for rel in rel_paths:
LINE 832 |         full = root / rel
LINE 833 |         if not full.is_file():
LINE 834 |             continue
LINE 835 |         try:
LINE 836 |             py_compile.compile(str(full), doraise=True)
LINE 837 |             info(f"Sintaxis OK: {rel}")
LINE 838 |         except py_compile.PyCompileError as exc:
LINE 839 |             error(f"Sintaxis inválida en {rel}: {exc}")
LINE 840 | 
LINE 841 | 
LINE 842 | # ---------------------------------------------------------------------------
LINE 843 | # CLI
LINE 844 | # ---------------------------------------------------------------------------
LINE 845 | 
LINE 846 | def build_parser() -> argparse.ArgumentParser:
LINE 847 |     p = argparse.ArgumentParser(
LINE 848 |         description="Aplica la Fase 1 (persistencia SQLite) al proyecto agente."
LINE 849 |     )
LINE 850 |     p.add_argument(
LINE 851 |         "project_root", nargs="?", default=".",
LINE 852 |         help="Ruta raíz del proyecto (por defecto: directorio actual).",
LINE 853 |     )
LINE 854 |     return p
LINE 855 | 
LINE 856 | 
LINE 857 | def main() -> int:
LINE 858 |     parser = build_parser()
LINE 859 |     args = parser.parse_args()
LINE 860 | 
LINE 861 |     try:
LINE 862 |         root = Path(args.project_root).resolve()
LINE 863 |     except Exception as exc:
LINE 864 |         error(f"Ruta inválida: {exc}")
LINE 865 |         return 1
LINE 866 | 
LINE 867 |     if not root.is_dir():
LINE 868 |         error(f"El directorio no existe: {root}")
LINE 869 |         return 1
LINE 870 | 
LINE 871 |     print(f"[INFO] Proyecto detectado: {root}")
LINE 872 |     print(f"[INFO] Inicio: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
LINE 873 |     print()
LINE 874 | 
LINE 875 |     try:
LINE 876 |         apply_all(root)
LINE 877 |     except Exception as exc:
LINE 878 |         error(str(exc))
LINE 879 |         print()
LINE 880 |         info("Proceso detenido. No se continúan aplicando cambios.")
LINE 881 |         _print_summary()
LINE 882 |         return 1
LINE 883 | 
LINE 884 |     print()
LINE 885 |     info("--- Resumen final ---")
LINE 886 |     _print_summary()
LINE 887 | 
LINE 888 |     # Validación sintáctica
LINE 889 |     validate_syntax(root, [
LINE 890 |         "app/core/storage/__init__.py",
LINE 891 |         "app/core/storage/database.py",
LINE 892 |         "app/core/project_analyzer.py",
LINE 893 |         "app/gui/file_tree.py",
LINE 894 |         "app/gui/main_window.py",
LINE 895 |     ])
LINE 896 | 
LINE 897 |     print()
LINE 898 |     info("Fase 1 aplicada. Reinicia la aplicación para probar.")
LINE 899 |     return 0 if STATS["errors"] == 0 else 1
LINE 900 | 
LINE 901 | 
LINE 902 | def _print_summary() -> None:
LINE 903 |     print(f"Archivos modificados: {STATS['modified']}")
LINE 904 |     print(f"Archivos creados: {STATS['created']}")
LINE 905 |     print(f"Archivos omitidos: {STATS['skipped']}")
LINE 906 |     print(f"Backups creados: {STATS['backups']}")
LINE 907 |     print(f"Errores: {STATS['errors']}")
LINE 908 | 
LINE 909 | 
LINE 910 | if __name__ == "__main__":
LINE 911 |     sys.exit(main())
```

==============================================================
FILE: output/deepseek_project_context.md
==============================================================
```md
LINE    1 | ==============================================================
LINE    2 | REPORTED PROBLEM OR GOAL / PROBLEMA REPORTADO U OBJETIVO
LINE    3 | ==============================================================
LINE    4 | generar el codigo en python para hacer el cambio el codigo se creara en la raiz del archivo 
LINE    5 | agregar las columnas a la tabla de producto medida, estadoProducto, unidad, caracteristica 
LINE    6 | la api listaProducto devuelve estos datos 
LINE    7 | [
LINE    8 |     {
LINE    9 |         "id": "4004",
LINE   10 |         "nombre": "BOTIN TREKIN MOTOQUERO PIL",
LINE   11 |         "codigo": "IND-BOT-T-M-P",
LINE   12 |         "descripcion": "BOTIN TREKIN MOTOQUERO PIL",
LINE   13 |         "codigobarras": "",
LINE   14 |         "fecha": "2026-09-03",
LINE   15 |         "imagen": "",
LINE   16 |         "idcategoria": "0",
LINE   17 |         "categoria": null,
LINE   18 |         "subcategoria": "",
LINE   19 |         "idmedida": "234",
LINE   20 |         "medida": "general",
LINE   21 |         "idestadoproducto": "275",
LINE   22 |         "estadoproducto": "Ejecuci\u00f3n",
LINE   23 |         "idunidad": "250",
LINE   24 |         "unidad": "Rollo",
LINE   25 |         "caracteristica": ""{
LINE   26 |         "id": "4004",
LINE   27 |         "nombre": "BOTIN TREKIN MOTOQUERO PIL",
LINE   28 |         "codigo": "IND-BOT-T-M-P",
LINE   29 |         "descripcion": "BOTIN TREKIN MOTOQUERO PIL",
LINE   30 |         "codigobarras": "",
LINE   31 |         "imagen": "",
LINE   32 |         "idcategoria": "0",
LINE   33 |         "categoria": null,
LINE   34 |         "subcategoria": "",
LINE   35 |         "idmedida": "234",
LINE   36 |         "medida": "general",
LINE   37 |         "idestadoproducto": "275",
LINE   38 |         "estadoproducto": "Ejecuci\u00f3n",
LINE   39 |         "idunidad": "250",
LINE   40 |         "unidad": "Rollo",
LINE   41 |         "caracteristica": ""
LINE   42 |     },...
LINE   43 | ]
LINE   44 | 
LINE   45 | 
LINE   46 | ==============================================================
LINE   47 | SELECTED ANALYSIS PROFILE / PERFIL DE ANÁLISIS: 🐞 Detect errors
LINE   48 | ==============================================================
LINE   49 | • Objetivo: Identificar errores de sintaxis, bugs lógicos, excepciones no controladas, condiciones de carrera y fallos de tipo en el código.
LINE   50 | • Enfoque: Detección exhaustiva de bugs, casos límite (edge cases), seguridad de nulos/undefined, control de flujo y manejo robusto de excepciones.
LINE   51 | • Prioridades: 1. Crashes y errores que detienen la ejecución. 2. Fallos silenciosos y corrupción de estado. 3. Manejo deficiente de excepciones. 4. Regresiones potenciales.
LINE   52 | • Resultado esperado: Localización exacta de cada error (archivo y línea), causa raíz técnica, código corregido listo para copiar/pegar y caso de prueba de verificación.
LINE   53 | 
LINE   54 | ⚠️ REGLA DE CONCRECIÓN TÉCNICA: El análisis debe ser CONCRETO, TÉCNICO y ORIENTADO A LA ACCIÓN. Concéntrate exclusivamente en fallos reproducibles y errores verificables. Omite comentarios estilísticos o divagaciones teóricas que no resuelvan un error.
LINE   55 | 
LINE   56 | ==============================================================
LINE   57 | PROJECT CONTEXT / CONTEXTO DEL PROYECTO
LINE   58 | ==============================================================
LINE   59 | • Nombre del Proyecto: cm-oficial
LINE   60 | • Ruta Base: /media/richard/Nuevo vol/quasar/dess/comercial/cm-oficial
LINE   61 | • Fecha de Generación: 2026-09-28 15:15:32
LINE   62 | 
LINE   63 | --------------------------------------------------------------
LINE   64 | PROJECT SUMMARY
LINE   65 | --------------------------------------------------------------
LINE   66 | Selected files: 4
LINE   67 | File extensions:
LINE   68 |   .vue: 3
LINE   69 |   .js: 1
LINE   70 | 
LINE   71 | Total lines:
LINE   72 | 1,683
LINE   73 | 
LINE   74 | --------------------------------------------------------------
LINE   75 | DEPENDENCIES AND REFERENCES
LINE   76 | --------------------------------------------------------------
LINE   77 | • src/components/producto/creacion/productoForm.vue:
LINE   78 |   - import { ref, watch, computed, onUnmounted } from 'vue'
LINE   79 |   - import { TipoFactura } from 'src/composables/FuncionesGenerales'
LINE   80 |   - import imageCompression from 'browser-image-compression'
LINE   81 |   - import { useQuasar } from 'quasar'
LINE   82 | • src/components/producto/creacion/productoTable.vue:
LINE   83 |   - import { ref, computed, watch } from 'vue'
LINE   84 |   - import { imagen } from 'src/boot/url'
LINE   85 |   - import { getTipoFactura } from 'src/composables/FuncionesG'
LINE   86 |   - import BaseFilterableTable from 'src/components/componentesGenerales/filtradoTabla/BaseFilterableTable.vue'
LINE   87 |   - import { useQuasar } from 'quasar'
LINE   88 |   - import { cambiarFormatoFecha } from 'src/composables/FuncionesG'
LINE   89 | • src/composables/useReporteInventarioExterior.js:
LINE   90 |   - import { ref } from 'vue'
LINE   91 |   - import { date } from 'quasar'
LINE   92 |   - import { idusuario_md5, idempresa_md5 } from 'src/composables/FuncionesGenerales'
LINE   93 |   - import { api } from 'src/boot/axios'
LINE   94 |   - import axios from 'axios'
LINE   95 |   - import 'jspdf-autotable'
LINE   96 | • src/pages/producto/CproductoPage.vue:
LINE   97 |   - import { ref, onMounted } from 'vue'
LINE   98 |   - import { api } from 'boot/axios'
LINE   99 |   - import { idempresa_md5, validarUsuario } from 'src/composables/FuncionesGenerales'
LINE  100 |   - import { useQuasar } from 'quasar'
LINE  101 |   - import { objectToFormData } from 'src/composables/FuncionesGenerales'
LINE  102 |   - import ProductoForm from 'src/components/producto/creacion/productoForm.vue'
LINE  103 |   - import ProductoTabla from 'src/components/producto/creacion/productoTable.vue'
LINE  104 |   - import { imagen } from 'src/boot/url'
LINE  105 |   - import { getTipoFactura, getToken } from 'src/composables/FuncionesG'
LINE  106 |   - import seriePage from 'src/modules/serie/page/seriePage.vue'
LINE  107 |   - import ProductoVarianteDialog from 'src/components/producto/variantes/productoVarianteDialog.vue'
LINE  108 | 
LINE  109 | --------------------------------------------------------------
LINE  110 | INSTRUCCIONES OBLIGATORIAS PARA DEEPSEEK (DETECT ERRORS)
LINE  111 | --------------------------------------------------------------
LINE  112 | El análisis debe ser CONCRETO, TÉCNICO y ORIENTADO A LA ACCIÓN. Concéntrate exclusivamente en fallos reproducibles y errores verificables. Omite comentarios estilísticos o divagaciones teóricas que no resuelvan un error.
LINE  113 | 
LINE  114 | Tu respuesta DEBE seguir exactamente la siguiente estructura Markdown adaptada al perfil:
LINE  115 | 
LINE  116 | # DIAGNOSIS
LINE  117 | ## Detected Bugs
LINE  118 | [Lista técnica de los bugs encontrados con su causa raíz exacta]
LINE  119 | 
LINE  120 | # FILES TO MODIFY
LINE  121 | ## 1. [ruta/relativa/archivo.ext]
LINE  122 | Approximate line: [número]
LINE  123 | ### Bug Description
LINE  124 | [Explicación concisa del error]
LINE  125 | ### Current Code
LINE  126 | ```
LINE  127 | [código con error]
LINE  128 | ```
LINE  129 | ### Bugfix Code
LINE  130 | ```
LINE  131 | [código corregido listo para sustituir]
LINE  132 | ```
LINE  133 | 
LINE  134 | # VERIFICATION & EDGE CASES
LINE  135 | [Prueba o caso límite para verificar que el bug fue resuelto]
LINE  136 | 
LINE  137 | REGLA OBLIGATORIA: No respondas con JSON. Responde con el Markdown estructurado exacto indicado arriba.
LINE  138 | 
LINE  139 | Estructura de Directorios:
LINE  140 | ```
LINE  141 | cm-oficial/
LINE  142 | └── src/
LINE  143 |     ├── components/
LINE  144 |     │   └── producto/
LINE  145 |     │       └── creacion/
LINE  146 |     │           ├── productoForm.vue
LINE  147 |     │           └── productoTable.vue
LINE  148 |     ├── composables/
LINE  149 |     │   └── useReporteInventarioExterior.js
LINE  150 |     └── pages/
LINE  151 |         └── producto/
LINE  152 |             └── CproductoPage.vue
LINE  153 | ```
LINE  154 | 
LINE  155 | 
LINE  156 | ==============================================================
LINE  157 | ATTACHMENTS / ARCHIVOS Y CÓDIGO FUENTE
LINE  158 | ==============================================================
LINE  159 | 
LINE  160 | ==============================================================
LINE  161 | FILE: src/components/producto/creacion/productoForm.vue
LINE  162 | ==============================================================
LINE  163 | ```vue
LINE  164 | LINE   1 | <template>
LINE  165 | LINE   2 |   <q-form @submit.prevent="handleSubmit">
LINE  166 | LINE   3 |     <!-- Información Básica -->
LINE  167 | LINE   4 |     <q-card-section>
LINE  168 | LINE   5 |       <div class="text-subtitle1 text-weight-medium q-mb-md">Información Básica</div>
LINE  169 | LINE   6 |       <q-separator class="q-mb-md" />
LINE  170 | LINE   7 |       
LINE  171 | LINE   8 |       <div class="row q-col-gutter-md">
LINE  172 | LINE   9 |         <div class="col-12 col-md-4">
LINE  173 | LINE  10 |           <q-input
LINE  174 | LINE  11 |             v-model="localData.codigo"
LINE  175 | LINE  12 |             label="Código de Producto *"
LINE  176 | LINE  13 |             dense
LINE  177 | LINE  14 |             outlined
LINE  178 | LINE  15 |             hint="Código único del producto"
LINE  179 | LINE  16 |           />
LINE  180 | LINE  17 |         </div>
LINE  181 | LINE  18 |         
LINE  182 | LINE  19 |         <div class="col-12 col-md-4">
LINE  183 | LINE  20 |           <q-input
LINE  184 | LINE  21 |             v-model="localData.nombre"
LINE  185 | LINE  22 |             label="Nombre del Producto *"
LINE  186 | LINE  23 |             dense
LINE  187 | LINE  24 |             outlined
LINE  188 | LINE  25 |             hint="Nombre comercial"
LINE  189 | LINE  26 |           />
LINE  190 | LINE  27 |         </div>
LINE  191 | LINE  28 |         
LINE  192 | LINE  29 |         <div class="col-12 col-md-4">
LINE  193 | LINE  30 |           <q-input
LINE  194 | LINE  31 |             v-model="localData.descripcion"
LINE  195 | LINE  32 |             label="Descripción *"
LINE  196 | LINE  33 |             dense
LINE  197 | LINE  34 |             outlined
LINE  198 | LINE  35 |             hint="Descripción breve"
LINE  199 | LINE  36 |           />
LINE  200 | LINE  37 |         </div>
LINE  201 | LINE  38 |         
LINE  202 | LINE  39 |         <div class="col-12 col-md-4">
LINE  203 | LINE  40 |           <q-input
LINE  204 | LINE  41 |             v-model="localData.codigobarras"
LINE  205 | LINE  42 |             label="Código de Barras"
LINE  206 | LINE  43 |             dense
LINE  207 | LINE  44 |             outlined
LINE  208 | LINE  45 |             hint="Opcional"
LINE  209 | LINE  46 |           />
LINE  210 | LINE  47 |         </div>
LINE  211 | LINE  48 |       </div>
LINE  212 | LINE  49 |     </q-card-section>
LINE  213 | LINE  50 | 
LINE  214 | LINE  51 |     <!-- Categorización -->
LINE  215 | LINE  52 |     <q-card-section>
LINE  216 | LINE  53 |       <div class="text-subtitle1 text-weight-medium q-mb-md">Categorización</div>
LINE  217 | LINE  54 |       <q-separator class="q-mb-md" />
LINE  218 | LINE  55 |       
LINE  219 | LINE  56 |       <div class="row q-col-gutter-md">
LINE  220 | LINE  57 |         <div class="col-12 col-md-4">
LINE  221 | LINE  58 |           <q-select
LINE  222 | LINE  59 |             v-model="localData.categoria"
LINE  223 | LINE  60 |             :options="categorias"
LINE  224 | LINE  61 |             label="Categoría *"
LINE  225 | LINE  62 |             dense
LINE  226 | LINE  63 |             outlined
LINE  227 | LINE  64 |             emit-value
LINE  228 | LINE  65 |             map-options
LINE  229 | LINE  66 |             hint="Seleccione la categoría principal"
LINE  230 | LINE  67 |             @update:model-value="
LINE  231 | LINE  68 |               (val) => {
LINE  232 | LINE  69 |                 localData.subcategoria = null
LINE  233 | LINE  70 |                 emit('categoria-changed', val)
LINE  234 | LINE  71 |               }
LINE  235 | LINE  72 |             "
LINE  236 | LINE  73 |           />
LINE  237 | LINE  74 |         </div>
LINE  238 | LINE  75 |         
LINE  239 | LINE  76 |         <div class="col-12 col-md-4" v-if="subcategorias.length > 0">
LINE  240 | LINE  77 |           <q-select
LINE  241 | LINE  78 |             v-model="localData.subcategoria"
LINE  242 | LINE  79 |             :options="subcategorias"
LINE  243 | LINE  80 |             label="Sub Categoría *"
LINE  244 | LINE  81 |             dense
LINE  245 | LINE  82 |             outlined
LINE  246 | LINE  83 |             emit-value
LINE  247 | LINE  84 |             map-options
LINE  248 | LINE  85 |             hint="Seleccione la subcategoría"
LINE  249 | LINE  86 |           />
LINE  250 | LINE  87 |         </div>
LINE  251 | LINE  88 |         
LINE  252 | LINE  89 |         <div class="col-12 col-md-4">
LINE  253 | LINE  90 |           <q-select
LINE  254 | LINE  91 |             v-model="localData.estadoproductos"
LINE  255 | LINE  92 |             :options="estados"
LINE  256 | LINE  93 |             label="Estado del Producto *"
LINE  257 | LINE  94 |             dense
LINE  258 | LINE  95 |             outlined
LINE  259 | LINE  96 |             emit-value
LINE  260 | LINE  97 |             map-options
LINE  261 | LINE  98 |             hint="Estado actual"
LINE  262 | LINE  99 |           />
LINE  263 | LINE 100 |         </div>
LINE  264 | LINE 101 |       </div>
LINE  265 | LINE 102 |     </q-card-section>
LINE  266 | LINE 103 | 
LINE  267 | LINE 104 |     <!-- Características -->
LINE  268 | LINE 105 |     <q-card-section>
LINE  269 | LINE 106 |       <div class="text-subtitle1 text-weight-medium q-mb-md">Características</div>
LINE  270 | LINE 107 |       <q-separator class="q-mb-md" />
LINE  271 | LINE 108 |       
LINE  272 | LINE 109 |       <div class="row q-col-gutter-md">
LINE  273 | LINE 110 |         <div class="col-12 col-md-4">
LINE  274 | LINE 111 |           <q-select
LINE  275 | LINE 112 |             v-model="localData.unidad"
LINE  276 | LINE 113 |             :options="unidades"
LINE  277 | LINE 114 |             label="Unidad de Medida *"
LINE  278 | LINE 115 |             dense
LINE  279 | LINE 116 |             outlined
LINE  280 | LINE 117 |             emit-value
LINE  281 | LINE 118 |             map-options
LINE  282 | LINE 119 |             hint="Ej: Kilo, Unidad, Litro"
LINE  283 | LINE 120 |           />
LINE  284 | LINE 121 |         </div>
LINE  285 | LINE 122 |         
LINE  286 | LINE 123 |         <div class="col-12 col-md-4">
LINE  287 | LINE 124 |           <q-select
LINE  288 | LINE 125 |             v-model="localData.medida"
LINE  289 | LINE 126 |             :options="medidas"
LINE  290 | LINE 127 |             label="Característica *"
LINE  291 | LINE 128 |             dense
LINE  292 | LINE 129 |             outlined
LINE  293 | LINE 130 |             emit-value
LINE  294 | LINE 131 |             map-options
LINE  295 | LINE 132 |           />
LINE  296 | LINE 133 |         </div>
LINE  297 | LINE 134 |         
LINE  298 | LINE 135 |         <div class="col-12 col-md-4">
LINE  299 | LINE 136 |           <q-input
LINE  300 | LINE 137 |             v-model="localData.caracteristica"
LINE  301 | LINE 138 |             label="Otras Características"
LINE  302 | LINE 139 |             dense
LINE  303 | LINE 140 |             outlined
LINE  304 | LINE 141 |             hint="Opcional"
LINE  305 | LINE 142 |           />
LINE  306 | LINE 143 |         </div>
LINE  307 | LINE 144 |       </div>
LINE  308 | LINE 145 |     </q-card-section>
LINE  309 | LINE 146 | 
LINE  310 | LINE 147 |     <!-- Información SIN (Facturación) -->
LINE  311 | LINE 148 |     <q-card-section v-if="tipoFactura">
LINE  312 | LINE 149 |       <div class="text-subtitle1 text-weight-medium q-mb-md">Información SIN (Facturación)</div>
LINE  313 | LINE 150 |       <q-separator class="q-mb-md" />
LINE  314 | LINE 151 |       
LINE  315 | LINE 152 |       <div class="row q-col-gutter-md">
LINE  316 | LINE 153 |         <div class="col-12 col-md-6">
LINE  317 | LINE 154 |           <q-select
LINE  318 | LINE 155 |             v-model="localData.codigosin"
LINE  319 | LINE 156 |             :options="FilterProductoSIN"
LINE  320 | LINE 157 |             label="Producto SIN *"
LINE  321 | LINE 158 |             dense
LINE  322 | LINE 159 |             outlined
LINE  323 | LINE 160 |             emit-value
LINE  324 | LINE 161 |             map-options
LINE  325 | LINE 162 |             use-input
LINE  326 | LINE 163 |             fill-input
LINE  327 | LINE 164 |             hide-selected
LINE  328 | LINE 165 |             input-debounce="0"
LINE  329 | LINE 166 |             @filter="filterFn"
LINE  330 | LINE 167 |             hint="Busque el código SIN del producto"
LINE  331 | LINE 168 |           />
LINE  332 | LINE 169 |         </div>
LINE  333 | LINE 170 |         
LINE  334 | LINE 171 |         <div class="col-12 col-md-3">
LINE  335 | LINE 172 |           <q-select
LINE  336 | LINE 173 |             v-model="localData.unidadsin"
LINE  337 | LINE 174 |             :options="FilterUnidadSIN"
LINE  338 | LINE 175 |             label="Unidad SIN *"
LINE  339 | LINE 176 |             dense
LINE  340 | LINE 177 |             outlined
LINE  341 | LINE 178 |             emit-value
LINE  342 | LINE 179 |             map-options
LINE  343 | LINE 180 |             use-input
LINE  344 | LINE 181 |             fill-input
LINE  345 | LINE 182 |             hide-selected
LINE  346 | LINE 183 |             input-debounce="0"
LINE  347 | LINE 184 |             @filter="filterUnidadFn"
LINE  348 | LINE 185 |             hint="Unidad según SIN"
LINE  349 | LINE 186 |           />
LINE  350 | LINE 187 |         </div>
LINE  351 | LINE 188 |         
LINE  352 | LINE 189 |         <div class="col-12 col-md-3">
LINE  353 | LINE 190 |           <q-input
LINE  354 | LINE 191 |             v-model="localData.codigoNandina"
LINE  355 | LINE 192 |             label="Código Nandina"
LINE  356 | LINE 193 |             dense
LINE  357 | LINE 194 |             outlined
LINE  358 | LINE 195 |             hint="Opcional"
LINE  359 | LINE 196 |           />
LINE  360 | LINE 197 |         </div>
LINE  361 | LINE 198 |       </div>
LINE  362 | LINE 199 |     </q-card-section>
LINE  363 | LINE 200 | 
LINE  364 | LINE 201 |     <!-- Imagen del Producto -->
LINE  365 | LINE 202 |     <q-card-section>
LINE  366 | LINE 203 |       <div class="text-subtitle1 text-weight-medium q-mb-md">Imagen del Producto</div>
LINE  367 | LINE 204 |       <q-separator class="q-mb-md" />
LINE  368 | LINE 205 |       
LINE  369 | LINE 206 |       <div class="row q-col-gutter-md">
LINE  370 | LINE 207 |         <div class="col-12" :class="imagePreview ? 'col-md-8' : ''">
LINE  371 | LINE 208 |           <q-file
LINE  372 | LINE 209 |             v-model="localData.imagen"
LINE  373 | LINE 210 |             label="Seleccionar imagen"
LINE  374 | LINE 211 |             outlined
LINE  375 | LINE 212 |             dense
LINE  376 | LINE 213 |             accept="image/*"
LINE  377 | LINE 214 |             hint="Formatos admitidos: JPG, PNG. La imagen se optimizará automáticamente."
LINE  378 | LINE 215 |             counter
LINE  379 | LINE 216 |             @update:model-value="onImageSelected"
LINE  380 | LINE 217 |             :loading="isCompressing"
LINE  381 | LINE 218 |             :disable="isCompressing"
LINE  382 | LINE 219 |           >
LINE  383 | LINE 220 |             <template v-slot:prepend>
LINE  384 | LINE 221 |               <q-icon name="attach_file" />
LINE  385 | LINE 222 |             </template>
LINE  386 | LINE 223 |           </q-file>
LINE  387 | LINE 224 |         </div>
LINE  388 | LINE 225 |         
LINE  389 | LINE 226 |         <div class="col-12 col-md-4" v-if="imagePreview">
LINE  390 | LINE 227 |           <div class="text-caption text-grey-7 q-mb-xs">
LINE  391 | LINE 228 |             {{ typeof localData.imagen === 'string' ? 'Imagen actual' : 'Vista previa' }}
LINE  392 | LINE 229 |           </div>
LINE  393 | LINE 230 |           <q-card flat bordered class="q-pa-sm">
LINE  394 | LINE 231 |             <q-img
LINE  395 | LINE 232 |               :src="imagePreview"
LINE  396 | LINE 233 |               style="max-height: 120px; border-radius: 4px"
LINE  397 | LINE 234 |               fit="contain"
LINE  398 | LINE 235 |               class="bg-grey-2"
LINE  399 | LINE 236 |             >
LINE  400 | LINE 237 |               <template v-slot:error>
LINE  401 | LINE 238 |                 <div class="absolute-full flex flex-center bg-grey-3 text-grey-7">
LINE  402 | LINE 239 |                   <div class="text-center">
LINE  403 | LINE 240 |                     <q-icon name="broken_image" size="md" />
LINE  404 | LINE 241 |                     <div class="text-caption">Error al cargar imagen</div>
LINE  405 | LINE 242 |                   </div>
LINE  406 | LINE 243 |                 </div>
LINE  407 | LINE 244 |               </template>
LINE  408 | LINE 245 |             </q-img>
LINE  409 | LINE 246 |             <div class="text-caption text-grey-7 q-mt-xs text-center" v-if="typeof localData.imagen !== 'string'">
LINE  410 | LINE 247 |               {{ localData.imagen?.name }}
LINE  411 | LINE 248 |             </div>
LINE  412 | LINE 249 |           </q-card>
LINE  413 | LINE 250 |         </div>
LINE  414 | LINE 251 |       </div>
LINE  415 | LINE 252 |     </q-card-section>
LINE  416 | LINE 253 | 
LINE  417 | LINE 254 |     <!-- Botones de Acción -->
LINE  418 | LINE 255 |     <q-separator />
LINE  419 | LINE 256 |     
LINE  420 | LINE 257 |     <q-card-actions align="right" class="q-pa-md">
LINE  421 | LINE 258 |       <q-btn
LINE  422 | LINE 259 |         label="Cancelar"
LINE  423 | LINE 260 |         flat
LINE  424 | LINE 261 |         color="grey-7"
LINE  425 | LINE 262 |         @click="$emit('cancel')"
LINE  426 | LINE 263 |         class="q-mr-sm"
LINE  427 | LINE 264 |       />
LINE  428 | LINE 265 |       <q-btn
LINE  429 | LINE 266 |         label="Guardar"
LINE  430 | LINE 267 |         type="submit"
LINE  431 | LINE 268 |         color="primary"
LINE  432 | LINE 269 |         unelevated
LINE  433 | LINE 270 |         :disable="isCompressing"
LINE  434 | LINE 271 |       />
LINE  435 | LINE 272 |     </q-card-actions>
LINE  436 | LINE 273 |   </q-form>
LINE  437 | LINE 274 | </template>
LINE  438 | LINE 275 | 
LINE  439 | LINE 276 | <script setup>
LINE  440 | LINE 277 | import { ref, watch, computed, onUnmounted } from 'vue'
LINE  441 | LINE 278 | import { TipoFactura } from 'src/composables/FuncionesGenerales'
LINE  442 | LINE 279 | import imageCompression from 'browser-image-compression'
LINE  443 | LINE 280 | import { useQuasar } from 'quasar'
LINE  444 | LINE 281 | 
LINE  445 | LINE 282 | const $q = useQuasar()
LINE  446 | LINE 283 | const tipoFactura = TipoFactura()
LINE  447 | LINE 284 | console.log('Tipo de factura en productoForm.vue:', tipoFactura)
LINE  448 | LINE 285 | 
LINE  449 | LINE 286 | let objectUrl = null
LINE  450 | LINE 287 | const isCompressing = ref(false)
LINE  451 | LINE 288 | let isProgrammaticUpdate = false // Flag to prevent infinite loop
LINE  452 | LINE 289 | 
LINE  453 | LINE 290 | const props = defineProps({
LINE  454 | LINE 291 |   isEditing: Boolean,
LINE  455 | LINE 292 |   modelValue: Object,
LINE  456 | LINE 293 |   categorias: {
LINE  457 | LINE 294 |     type: Array,
LINE  458 | LINE 295 |     default: () => [],
LINE  459 | LINE 296 |   },
LINE  460 | LINE 297 |   estados: {
LINE  461 | LINE 298 |     type: Array,
LINE  462 | LINE 299 |     default: () => [],
LINE  463 | LINE 300 |   },
LINE  464 | LINE 301 |   subcategorias: {
LINE  465 | LINE 302 |     type: Array,
LINE  466 | LINE 303 |     default: () => [],
LINE  467 | LINE 304 |   },
LINE  468 | LINE 305 |   unidades: {
LINE  469 | LINE 306 |     type: Array,
LINE  470 | LINE 307 |     default: () => [],
LINE  471 | LINE 308 |   },
LINE  472 | LINE 309 |   medidas: {
LINE  473 | LINE 310 |     type: Array,
LINE  474 | LINE 311 |     default: () => [],
LINE  475 | LINE 312 |   },
LINE  476 | LINE 313 |   productoSIN: {
LINE  477 | LINE 314 |     type: Array,
LINE  478 | LINE 315 |     default: () => [],
LINE  479 | LINE 316 |   },
LINE  480 | LINE 317 |   unidadSIN: {
LINE  481 | LINE 318 |     type: Array,
LINE  482 | LINE 319 |     default: () => [],
LINE  483 | LINE 320 |   },
LINE  484 | LINE 321 | })
LINE  485 | LINE 322 | 
LINE  486 | LINE 323 | const emit = defineEmits(['submit', 'cancel'])
LINE  487 | LINE 324 | const FilterProductoSIN = ref([...props.productoSIN])
LINE  488 | LINE 325 | const FilterUnidadSIN = ref([...props.unidadSIN])
LINE  489 | LINE 326 | const localData = ref({ ...props.modelValue })
LINE  490 | LINE 327 | 
LINE  491 | LINE 328 | // Computed property for image preview
LINE  492 | LINE 329 | const imagePreview = computed(() => {
LINE  493 | LINE 330 |   if (!localData.value.imagen) return null
LINE  494 | LINE 331 |   
LINE  495 | LINE 332 |   // If it's a File object (newly selected), create object URL
LINE  496 | LINE 333 |   if (localData.value.imagen instanceof File) {
LINE  497 | LINE 334 |     // Clean up old object URL if exists
LINE  498 | LINE 335 |     if (objectUrl) {
LINE  499 | LINE 336 |       URL.revokeObjectURL(objectUrl)
LINE  500 | LINE 337 |     }
LINE  501 | LINE 338 |     objectUrl = URL.createObjectURL(localData.value.imagen)
LINE  502 | LINE 339 |     return objectUrl
LINE  503 | LINE 340 |   }
LINE  504 | LINE 341 |   
LINE  505 | LINE 342 |   // If it's a string (existing image from database), use vista URL
LINE  506 | LINE 343 |   if (typeof localData.value.imagen === 'string') {
LINE  507 | LINE 344 |     return localData.value.vista
LINE  508 | LINE 345 |   }
LINE  509 | LINE 346 |   
LINE  510 | LINE 347 |   return null
LINE  511 | LINE 348 | })
LINE  512 | LINE 349 | 
LINE  513 | LINE 350 | // Handler for image selection and compression
LINE  514 | LINE 351 | const onImageSelected = async (file) => {
LINE  515 | LINE 352 |   // Prevent infinite loop if we are just updating the model programmatically
LINE  516 | LINE 353 |   if (isProgrammaticUpdate) {
LINE  517 | LINE 354 |     isProgrammaticUpdate = false
LINE  518 | LINE 355 |     return
LINE  519 | LINE 356 |   }
LINE  520 | LINE 357 | 
LINE  521 | LINE 358 |   // Prevent infinite loop if the file is already a webp or undefined
LINE  522 | LINE 359 |   if (!file) {
LINE  523 | LINE 360 |     if (objectUrl) {
LINE  524 | LINE 361 |       URL.revokeObjectURL(objectUrl)
LINE  525 | LINE 362 |       objectUrl = null
LINE  526 | LINE 363 |     }
LINE  527 | LINE 364 |     return
LINE  528 | LINE 365 |   }
LINE  529 | LINE 366 |   
LINE  530 | LINE 367 |   // If it's a string (existing image)
LINE  531 | LINE 368 |   if (!(file instanceof File)) {
LINE  532 | LINE 369 |     return
LINE  533 | LINE 370 |   }
LINE  534 | LINE 371 | 
LINE  535 | LINE 372 |   try {
LINE  536 | LINE 373 |     isCompressing.value = true
LINE  537 | LINE 374 |     
LINE  538 | LINE 375 |     // We use a simple notification without trying to store its ID and update it later
LINE  539 | LINE 376 |     // because doing so causes "trying to update a grouped one which is forbidden" error in Quasar.
LINE  540 | LINE 377 |     $q.notify({
LINE  541 | LINE 378 |       message: 'Optimizando imagen...',
LINE  542 | LINE 379 |       color: 'info',
LINE  543 | LINE 380 |       textColor: 'white',
LINE  544 | LINE 381 |       icon: 'cloud_upload',
LINE  545 | LINE 382 |       timeout: 1500, // Short timeout, the real indicator is the loading spinner on the input
LINE  546 | LINE 383 |     })
LINE  547 | LINE 384 | 
LINE  548 | LINE 385 |     const options = {
LINE  549 | LINE 386 |       maxSizeMB: 1, // Compress to less than 1MB
LINE  550 | LINE 387 |       maxWidthOrHeight: 1920, // Max resolution 1920px
LINE  551 | LINE 388 |       useWebWorker: true,
LINE  552 | LINE 389 |       fileType: 'image/jpeg', // Convert to JPEG format for backend compatibility (JPG/PNG only)
LINE  553 | LINE 390 |       initialQuality: 0.9, // Maintain high visual quality
LINE  554 | LINE 391 |     }
LINE  555 | LINE 392 | 
LINE  556 | LINE 393 |     // Attempt to compress the image
LINE  557 | LINE 394 |     const compressedBlob = await imageCompression(file, options)
LINE  558 | LINE 395 |     
LINE  559 | LINE 396 |     // Create a new File from the Blob to keep the original name (but with .jpg extension)
LINE  560 | LINE 397 |     const newFileName = file.name.replace(/\.[^/.]+$/, "") + '.jpg'
LINE  561 | LINE 398 |     const compressedFile = new File([compressedBlob], newFileName, {
LINE  562 | LINE 399 |       type: 'image/jpeg',
LINE  563 | LINE 400 |       lastModified: Date.now()
LINE  564 | LINE 401 |     })
LINE  565 | LINE 402 | 
LINE  566 | LINE 403 |     console.log(`Original size: ${(file.size / 1024 / 1024).toFixed(2)} MB`)
LINE  567 | LINE 404 |     console.log(`Compressed size: ${(compressedFile.size / 1024 / 1024).toFixed(2)} MB`)
LINE  568 | LINE 405 | 
LINE  569 | LINE 406 |     // This flag prevents the @update:model-value from triggering this function again and causing an infinite loop
LINE  570 | LINE 407 |     isProgrammaticUpdate = true
LINE  571 | LINE 408 |     
LINE  572 | LINE 409 |     // Update the v-model with the compressed file
LINE  573 | LINE 410 |     // Note: This triggers the `imagePreview` computed properly
LINE  574 | LINE 411 |     localData.value.imagen = compressedFile
LINE  575 | LINE 412 | 
LINE  576 | LINE 413 |     // Show a success notification
LINE  577 | LINE 414 |     $q.notify({
LINE  578 | LINE 415 |       message: 'Imagen optimizada con éxito',
LINE  579 | LINE 416 |       color: 'positive',
LINE  580 | LINE 417 |       icon: 'check_circle',
LINE  581 | LINE 418 |       timeout: 2500,
LINE  582 | LINE 419 |     })
LINE  583 | LINE 420 | 
LINE  584 | LINE 421 |   } catch (error) {
LINE  585 | LINE 422 |     console.error('Error compressing image:', error)
LINE  586 | LINE 423 |     $q.notify({
LINE  587 | LINE 424 |       message: 'Hubo un error al optimizar la imagen',
LINE  588 | LINE 425 |       color: 'negative',
LINE  589 | LINE 426 |       icon: 'warning',
LINE  590 | LINE 427 |     })
LINE  591 | LINE 428 |     
LINE  592 | LINE 429 |     isProgrammaticUpdate = true
LINE  593 | LINE 430 |     // If compression fails, we fallback to the original file
LINE  594 | LINE 431 |     // The imagePreview will still handle the display
LINE  595 | LINE 432 |     localData.value.imagen = file
LINE  596 | LINE 433 |   } finally {
LINE  597 | LINE 434 |     isCompressing.value = false
LINE  598 | LINE 435 |   }
LINE  599 | LINE 436 | }
LINE  600 | LINE 437 | 
LINE  601 | LINE 438 | // Cleanup object URL on unmount
LINE  602 | LINE 439 | onUnmounted(() => {
LINE  603 | LINE 440 |   if (objectUrl) {
LINE  604 | LINE 441 |     URL.revokeObjectURL(objectUrl)
LINE  605 | LINE 442 |   }
LINE  606 | LINE 443 | })
LINE  607 | LINE 444 | function filterFn(val, update) {
LINE  608 | LINE 445 |   console.log(val)
LINE  609 | LINE 446 |   if (val === '') {
LINE  610 | LINE 447 |     update(() => {
LINE  611 | LINE 448 |       FilterProductoSIN.value = [...props.productoSIN]
LINE  612 | LINE 449 |     })
LINE  613 | LINE 450 |     return
LINE  614 | LINE 451 |   }
LINE  615 | LINE 452 | 
LINE  616 | LINE 453 |   update(() => {
LINE  617 | LINE 454 |     const needle = val.toLowerCase()
LINE  618 | LINE 455 |     FilterProductoSIN.value = props.productoSIN.filter((v) =>
LINE  619 | LINE 456 |       v.label.toLowerCase().includes(needle),
LINE  620 | LINE 457 |     )
LINE  621 | LINE 458 |   })
LINE  622 | LINE 459 | }
LINE  623 | LINE 460 | function filterUnidadFn(val, update) {
LINE  624 | LINE 461 |   console.log(val)
LINE  625 | LINE 462 |   if (val === '') {
LINE  626 | LINE 463 |     update(() => {
LINE  627 | LINE 464 |       FilterUnidadSIN.value = [...props.unidadSIN]
LINE  628 | LINE 465 |     })
LINE  629 | LINE 466 |     return
LINE  630 | LINE 467 |   }
LINE  631 | LINE 468 |   update(() => {
LINE  632 | LINE 469 |     const needle = val.toLowerCase()
LINE  633 | LINE 470 |     FilterUnidadSIN.value = props.unidadSIN.filter((v) => v.label.toLowerCase().includes(needle))
LINE  634 | LINE 471 |   })
LINE  635 | LINE 472 | }
LINE  636 | LINE 473 | console.log(props.modelValue)
LINE  637 | LINE 474 | watch(
LINE  638 | LINE 475 |   () => props.modelValue,
LINE  639 | LINE 476 |   (val) => {
LINE  640 | LINE 477 |     localData.value = { ...val }
LINE  641 | LINE 478 |   },
LINE  642 | LINE 479 |   { deep: true },
LINE  643 | LINE 480 | )
LINE  644 | LINE 481 | 
LINE  645 | LINE 482 | const handleSubmit = () => {
LINE  646 | LINE 483 |   console.log('=== FORM SUBMIT DEBUG ===')
LINE  647 | LINE 484 |   console.log('localData.categoria:', localData.value.categoria)
LINE  648 | LINE 485 |   console.log('localData.subcategoria:', localData.value.subcategoria)
LINE  649 | LINE 486 |   console.log('Full localData:', JSON.stringify(localData.value, null, 2))
LINE  650 | LINE 487 |   emit('submit', localData.value)
LINE  651 | LINE 488 | }
LINE  652 | LINE 489 | </script>
LINE  653 | ```
LINE  654 | 
LINE  655 | ==============================================================
LINE  656 | FILE: src/components/producto/creacion/productoTable.vue
LINE  657 | ==============================================================
LINE  658 | ```vue
LINE  659 | LINE   1 | //src\components\producto\creacion\productoTable.vue
LINE  660 | LINE   2 | <template>
LINE  661 | LINE   3 |   <div>
LINE  662 | LINE   4 |     <q-card flat class="q-mb-md">
LINE  663 | LINE   5 |       <q-card-section class="row items-center justify-between q-pb-none">
LINE  664 | LINE   6 |         <div class="col-12 col-md-4">
LINE  665 | LINE   7 |           <div class="text-h6 text-primary text-weight-bold">
LINE  666 | LINE   8 |             <q-icon name="inventory_2" size="sm" class="q-mr-sm" />
LINE  667 | LINE   9 |             Catálogo de Productos
LINE  668 | LINE  10 |           </div>
LINE  669 | LINE  11 |           <div class="text-caption text-grey-7">Administre sus productos y servicios</div>
LINE  670 | LINE  12 |         </div>
LINE  671 | LINE  13 |         <div class="col-12 col-md-8">
LINE  672 | LINE  14 |           <div class="row q-gutter-sm items-center justify-end q-mt-sm q-md-mt-none">
LINE  673 | LINE  15 |             <q-btn
LINE  674 | LINE  16 |               unelevated
LINE  675 | LINE  17 |               outline
LINE  676 | LINE  18 |               color="blue"
LINE  677 | LINE  19 |               @click="$emit('irconjunto')"
LINE  678 | LINE  20 |               icon="mdi-set-all"
LINE  679 | LINE  21 |               label="Conjunto"
LINE  680 | LINE  22 |             />
LINE  681 | LINE  23 |             <q-btn
LINE  682 | LINE  24 |               unelevated
LINE  683 | LINE  25 |               outline
LINE  684 | LINE  26 |               color="indigo"
LINE  685 | LINE  27 |               @click="exportarDatos"
LINE  686 | LINE  28 |               icon="mdi-file-excel"
LINE  687 | LINE  29 |               label="Descargar Excel"
LINE  688 | LINE  30 |             />
LINE  689 | LINE  31 |             <q-btn
LINE  690 | LINE  32 |               unelevated
LINE  691 | LINE  33 |               outline
LINE  692 | LINE  34 |               color="positive"
LINE  693 | LINE  35 |               @click="exportarFormato"
LINE  694 | LINE  36 |               icon="mdi-file-download-outline"
LINE  695 | LINE  37 |               label="Descargar Formato"
LINE  696 | LINE  38 |             />
LINE  697 | LINE  39 |             <q-btn
LINE  698 | LINE  40 |               unelevated
LINE  699 | LINE  41 |               outline
LINE  700 | LINE  42 |               color="secondary"
LINE  701 | LINE  43 |               @click="$refs.fileInput.click()"
LINE  702 | LINE  44 |               icon="mdi-file-upload-outline"
LINE  703 | LINE  45 |               label="Cargar Excel"
LINE  704 | LINE  46 |               :loading="importing"
LINE  705 | LINE  47 |               :disable="importing"
LINE  706 | LINE  48 |             />
LINE  707 | LINE  49 |             <q-btn color="primary" @click="$emit('add')" class="btn-res" title="Registrar Producto">
LINE  708 | LINE  50 |               <q-icon name="add" class="icono" />
LINE  709 | LINE  51 |               <span class="texto"> <q-icon name="add" /> Nuevo </span>
LINE  710 | LINE  52 |             </q-btn>
LINE  711 | LINE  53 |             <input
LINE  712 | LINE  54 |               type="file"
LINE  713 | LINE  55 |               ref="fileInput"
LINE  714 | LINE  56 |               style="display: none"
LINE  715 | LINE  57 |               accept=".xlsx, .xls"
LINE  716 | LINE  58 |               @change="onFileSelected"
LINE  717 | LINE  59 |             />
LINE  718 | LINE  60 |             <q-btn
LINE  719 | LINE  61 |               v-if="selectedIds.size > 0"
LINE  720 | LINE  62 |               unelevated
LINE  721 | LINE  63 |               color="negative"
LINE  722 | LINE  64 |               icon="delete_sweep"
LINE  723 | LINE  65 |               label="Eliminar seleccionados"
LINE  724 | LINE  66 |               @click="eliminarSeleccionados"
LINE  725 | LINE  67 |             />
LINE  726 | LINE  68 |             <!-- Dentro de <q-card-section class="row items-center justify-between q-pb-none"> -->
LINE  727 | LINE  69 |             <q-checkbox
LINE  728 | LINE  70 |               v-model="selectAll"
LINE  729 | LINE  71 |               label="Seleccionar todo"
LINE  730 | LINE  72 |               :indeterminate="selectedIds.size > 0 && selectedIds.length < filteredRows.length"
LINE  731 | LINE  73 |             />
LINE  732 | LINE  74 |           </div>
LINE  733 | LINE  75 |         </div>
LINE  734 | LINE  76 |       </q-card-section>
LINE  735 | LINE  77 | 
LINE  736 | LINE  78 |       <q-card-section>
LINE  737 | LINE  79 |         <BaseFilterableTable
LINE  738 | LINE  80 |           id="tablaProductos"
LINE  739 | LINE  81 |           ref="reHijo"
LINE  740 | LINE  82 |           :rows="filteredRows"
LINE  741 | LINE  83 |           :columns="columns"
LINE  742 | LINE  84 |           :arrayHeaders="arrayHeaders"
LINE  743 | LINE  85 |           row-key="id"
LINE  744 | LINE  86 |           :loading="loading"
LINE  745 | LINE  87 |           flat
LINE  746 | LINE  88 |           bordered
LINE  747 | LINE  89 |         >
LINE  748 | LINE  90 |           <template v-slot:top-right></template>
LINE  749 | LINE  91 | 
LINE  750 | LINE  92 |           <template v-slot:body-cell-imagen="props">
LINE  751 | LINE  93 |             <q-td :props="props" id="imagenproducto">
LINE  752 | LINE  94 |               <q-img
LINE  753 | LINE  95 |                 :src="imagen + props.row.imagen"
LINE  754 | LINE  96 |                 @click="abrirModal(props.row.imagen)"
LINE  755 | LINE  97 |                 style="max-width: 100px; max-height: 100px; cursor: pointer"
LINE  756 | LINE  98 |                 spinner-color="primary"
LINE  757 | LINE  99 |               >
LINE  758 | LINE 100 |                 <template v-slot:error>
LINE  759 | LINE 101 |                   <div
LINE  760 | LINE 102 |                     class="column items-center justify-center bg-grey-3"
LINE  761 | LINE 103 |                     style="height: 100%; width: 100%"
LINE  762 | LINE 104 |                   >
LINE  763 | LINE 105 |                     <q-icon name="image_not_supported" size="md" color="grey-7" />
LINE  764 | LINE 106 |                   </div>
LINE  765 | LINE 107 |                 </template>
LINE  766 | LINE 108 |               </q-img>
LINE  767 | LINE 109 |             </q-td>
LINE  768 | LINE 110 |           </template>
LINE  769 | LINE 111 |           <template v-slot:body-cell-productosin="props">
LINE  770 | LINE 112 |             <q-td :props="props">
LINE  771 | LINE 113 |               <div class="text-truncate" @click.stop v-if="props.row.productosin">
LINE  772 | LINE 114 |                 {{ props.row.productosin?.descripcion }}
LINE  773 | LINE 115 | 
LINE  774 | LINE 116 |                 <q-popup-proxy>
LINE  775 | LINE 117 |                   <q-card class="q-pa-sm" style="max-width: 300px; white-space: normal">
LINE  776 | LINE 118 |                     {{ props.row.productosin?.descripcion }}
LINE  777 | LINE 119 |                   </q-card>
LINE  778 | LINE 120 |                 </q-popup-proxy>
LINE  779 | LINE 121 |               </div>
LINE  780 | LINE 122 |             </q-td>
LINE  781 | LINE 123 |           </template>
LINE  782 | LINE 124 | 
LINE  783 | LINE 125 |           <template v-slot:body-cell-opciones="props">
LINE  784 | LINE 126 |             <q-td :props="props" class="text-nowrap">
LINE  785 | LINE 127 |               <q-btn
LINE  786 | LINE 128 |                 icon="edit"
LINE  787 | LINE 129 |                 color="primary"
LINE  788 | LINE 130 |                 dense
LINE  789 | LINE 131 |                 class="q-mr-sm"
LINE  790 | LINE 132 |                 @click="$emit('edit-item', props.row)"
LINE  791 | LINE 133 |                 flat
LINE  792 | LINE 134 |                 id="editarproducto"
LINE  793 | LINE 135 |               />
LINE  794 | LINE 136 |               <q-btn
LINE  795 | LINE 137 |                 icon="tune"
LINE  796 | LINE 138 |                 color="secondary"
LINE  797 | LINE 139 |                 dense
LINE  798 | LINE 140 |                 class="q-mr-sm"
LINE  799 | LINE 141 |                 @click="$emit('gestionar-variantes', props.row)"
LINE  800 | LINE 142 |                 flat
LINE  801 | LINE 143 |                 title="Gestionar variantes"
LINE  802 | LINE 144 |                 id="variantesproducto"
LINE  803 | LINE 145 |               />
LINE  804 | LINE 146 |               <q-btn
LINE  805 | LINE 147 |                 icon="delete"
LINE  806 | LINE 148 |                 color="negative"
LINE  807 | LINE 149 |                 dense
LINE  808 | LINE 150 |                 @click="$emit('delete-item', props.row)"
LINE  809 | LINE 151 |                 flat
LINE  810 | LINE 152 |                 id="eliminarproducto"
LINE  811 | LINE 153 |               />
LINE  812 | LINE 154 |             </q-td>
LINE  813 | LINE 155 |           </template>
LINE  814 | LINE 156 |           <template v-slot:body-cell-seleccionar="props">
LINE  815 | LINE 157 |             <q-td :props="props" auto-width>
LINE  816 | LINE 158 |               <q-checkbox
LINE  817 | LINE 159 |                 :model-value="selectedIds.has(props.row.id)"
LINE  818 | LINE 160 |                 @update:model-value="(val) => toggleSeleccion(props.row.id, val)"
LINE  819 | LINE 161 |                 dense
LINE  820 | LINE 162 |               />
LINE  821 | LINE 163 |             </q-td>
LINE  822 | LINE 164 |           </template>
LINE  823 | LINE 165 |         </BaseFilterableTable>
LINE  824 | LINE 166 |       </q-card-section>
LINE  825 | LINE 167 |     </q-card>
LINE  826 | LINE 168 | 
LINE  827 | LINE 169 |     <q-dialog v-model="mostrarImagen">
LINE  828 | LINE 170 |       <q-card class="responsive-dialog">
LINE  829 | LINE 171 |         <q-card-section class="bg-primary text-white text-h6 flex justify-between">
LINE  830 | LINE 172 |           <div>Vista Previa de Imagen</div>
LINE  831 | LINE 173 |           <q-btn icon="close" flat dense round @click="mostrarImagen = false" />
LINE  832 | LINE 174 |         </q-card-section>
LINE  833 | LINE 175 |         <q-card-section>
LINE  834 | LINE 176 |           <q-img
LINE  835 | LINE 177 |             :src="imagen + imagenSeleccionada"
LINE  836 | LINE 178 |             style="max-width: 100%; max-height: 100%"
LINE  837 | LINE 179 |             spinner-color="primary"
LINE  838 | LINE 180 |           />
LINE  839 | LINE 181 |         </q-card-section>
LINE  840 | LINE 182 |       </q-card>
LINE  841 | LINE 183 |     </q-dialog>
LINE  842 | LINE 184 |   </div>
LINE  843 | LINE 185 | </template>
LINE  844 | LINE 186 | 
LINE  845 | LINE 187 | <script setup>
LINE  846 | LINE 188 | import { ref, computed, watch } from 'vue'
LINE  847 | LINE 189 | import { imagen } from 'src/boot/url'
LINE  848 | LINE 190 | import { getTipoFactura } from 'src/composables/FuncionesG'
LINE  849 | LINE 191 | import BaseFilterableTable from 'src/components/componentesGenerales/filtradoTabla/BaseFilterableTable.vue'
LINE  850 | LINE 192 | import {
LINE  851 | LINE 193 |   exportarPlantillaProductos,
LINE  852 | LINE 194 |   importarProductosDesdeExcel,
LINE  853 | LINE 195 |   exportToXLSX_CatalogoProductos,
LINE  854 | LINE 196 | } from 'src/utils/XCLReportImport'
LINE  855 | LINE 197 | import { useQuasar } from 'quasar'
LINE  856 | LINE 198 | import { cambiarFormatoFecha } from 'src/composables/FuncionesG'
LINE  857 | LINE 199 | 
LINE  858 | LINE 200 | const selectedIds = ref(new Set())
LINE  859 | LINE 201 | const $q = useQuasar()
LINE  860 | LINE 202 | const fileInput = ref(null)
LINE  861 | LINE 203 | 
LINE  862 | LINE 204 | const tipoFactura = getTipoFactura(true)
LINE  863 | LINE 205 | 
LINE  864 | LINE 206 | const mostrarImagen = ref(false)
LINE  865 | LINE 207 | const imagenSeleccionada = ref(null)
LINE  866 | LINE 208 | 
LINE  867 | LINE 209 | const abrirModal = (img) => {
LINE  868 | LINE 210 |   imagenSeleccionada.value = img
LINE  869 | LINE 211 |   mostrarImagen.value = true
LINE  870 | LINE 212 | }
LINE  871 | LINE 213 | const props = defineProps({
LINE  872 | LINE 214 |   rows: {
LINE  873 | LINE 215 |     type: Array,
LINE  874 | LINE 216 |     required: true,
LINE  875 | LINE 217 |     default: () => [],
LINE  876 | LINE 218 |   },
LINE  877 | LINE 219 |   loading: {
LINE  878 | LINE 220 |     type: Boolean,
LINE  879 | LINE 221 |     default: false,
LINE  880 | LINE 222 |   },
LINE  881 | LINE 223 |   importing: { type: Boolean, default: false },
LINE  882 | LINE 224 | })
LINE  883 | LINE 225 | 
LINE  884 | LINE 226 | let columns = []
LINE  885 | LINE 227 | if (tipoFactura) {
LINE  886 | LINE 228 |   columns = [
LINE  887 | LINE 229 |     { name: 'numero', label: 'N°', field: 'numero', align: 'right', dataType: 'number' },
LINE  888 | LINE 230 |     {
LINE  889 | LINE 231 |       name: 'fecha',
LINE  890 | LINE 232 |       label: 'Fecha',
LINE  891 | LINE 233 |       field: 'fecha',
LINE  892 | LINE 234 |       align: 'left',
LINE  893 | LINE 235 |       format: (val) => cambiarFormatoFecha(val),
LINE  894 | LINE 236 |       dataType: 'date',
LINE  895 | LINE 237 |     },
LINE  896 | LINE 238 |     { name: 'codigo', label: 'Cod.', field: 'codigo', align: 'left', dataType: 'text' },
LINE  897 | LINE 239 |     { name: 'nombre', label: 'Nombre', field: 'nombre', align: 'left', dataType: 'text' },
LINE  898 | LINE 240 |     {
LINE  899 | LINE 241 |       name: 'descripcion',
LINE  900 | LINE 242 |       label: 'Descripción',
LINE  901 | LINE 243 |       field: 'descripcion',
LINE  902 | LINE 244 |       align: 'left',
LINE  903 | LINE 245 |       dataType: 'text',
LINE  904 | LINE 246 |     },
LINE  905 | LINE 247 |     { name: 'categoria', label: 'Categoría', field: 'categoria', align: 'left', dataType: 'text' },
LINE  906 | LINE 248 |     {
LINE  907 | LINE 249 |       name: 'subcategoria',
LINE  908 | LINE 250 |       label: 'Sub Categorías',
LINE  909 | LINE 251 |       field: 'subcategoria',
LINE  910 | LINE 252 |       align: 'left',
LINE  911 | LINE 253 |       dataType: 'text',
LINE  912 | LINE 254 |     },
LINE  913 | LINE 255 |     {
LINE  914 | LINE 256 |       name: 'codigobarras',
LINE  915 | LINE 257 |       label: 'Cod.Barra',
LINE  916 | LINE 258 |       field: 'codigobarras',
LINE  917 | LINE 259 |       align: 'right',
LINE  918 | LINE 260 |       dataType: 'text',
LINE  919 | LINE 261 |     },
LINE  920 | LINE 262 |     {
LINE  921 | LINE 263 |       name: 'medida',
LINE  922 | LINE 264 |       label: 'Caract.',
LINE  923 | LINE 265 |       field: 'medida',
LINE  924 | LINE 266 |       align: 'left',
LINE  925 | LINE 267 |       dataType: 'text',
LINE  926 | LINE 268 |       defaultVisible: false,
LINE  927 | LINE 269 |     },
LINE  928 | LINE 270 |     {
LINE  929 | LINE 271 |       name: 'estadoproducto',
LINE  930 | LINE 272 |       label: 'Estado',
LINE  931 | LINE 273 |       field: 'estadoproducto',
LINE  932 | LINE 274 |       align: 'left',
LINE  933 | LINE 275 |       dataType: 'text',
LINE  934 | LINE 276 |       defaultVisible: false,
LINE  935 | LINE 277 |     },
LINE  936 | LINE 278 |     {
LINE  937 | LINE 279 |       name: 'unidad',
LINE  938 | LINE 280 |       label: 'Unidad',
LINE  939 | LINE 281 |       field: 'unidad',
LINE  940 | LINE 282 |       align: 'left',
LINE  941 | LINE 283 |       dataType: 'text',
LINE  942 | LINE 284 |       defaultVisible: false,
LINE  943 | LINE 285 |     },
LINE  944 | LINE 286 |     {
LINE  945 | LINE 287 |       name: 'caracteristica',
LINE  946 | LINE 288 |       label: 'Otras caract.',
LINE  947 | LINE 289 |       field: 'caracteristica',
LINE  948 | LINE 290 |       align: 'left',
LINE  949 | LINE 291 |       dataType: 'text',
LINE  950 | LINE 292 |       defaultVisible: false,
LINE  951 | LINE 293 |     },
LINE  952 | LINE 294 |     {
LINE  953 | LINE 295 |       name: 'productosin',
LINE  954 | LINE 296 |       label: 'Producto SIN',
LINE  955 | LINE 297 |       field: 'productosin',
LINE  956 | LINE 298 |       align: 'left',
LINE  957 | LINE 299 |       dataType: 'text',
LINE  958 | LINE 300 |       defaultVisible: false,
LINE  959 | LINE 301 |     },
LINE  960 | LINE 302 |     {
LINE  961 | LINE 303 |       name: 'codigonandina',
LINE  962 | LINE 304 |       label: 'CodigoNandina',
LINE  963 | LINE 305 |       field: 'codigonandina',
LINE  964 | LINE 306 |       align: 'left',
LINE  965 | LINE 307 |       dataType: 'text',
LINE  966 | LINE 308 |       defaultVisible: false,
LINE  967 | LINE 309 |     },
LINE  968 | LINE 310 | 
LINE  969 | LINE 311 |     { name: 'imagen', label: 'Imagen', field: 'imagen', align: 'center' },
LINE  970 | LINE 312 |     { name: 'opciones', label: 'Opciones', field: 'opciones', sortable: false },
LINE  971 | LINE 313 |     {
LINE  972 | LINE 314 |       name: 'seleccionar',
LINE  973 | LINE 315 |       label: '',
LINE  974 | LINE 316 |       field: 'seleccionar',
LINE  975 | LINE 317 |       align: 'center',
LINE  976 | LINE 318 |       sortable: false,
LINE  977 | LINE 319 |       headerStyle: 'width: 50px',
LINE  978 | LINE 320 |     },
LINE  979 | LINE 321 |   ]
LINE  980 | LINE 322 | } else {
LINE  981 | LINE 323 |   columns = [
LINE  982 | LINE 324 |     { name: 'numero', label: 'N°', field: 'numero', align: 'right', dataType: 'number' },
LINE  983 | LINE 325 |     {
LINE  984 | LINE 326 |       name: 'fecha',
LINE  985 | LINE 327 |       label: 'Fecha',
LINE  986 | LINE 328 |       field: 'fecha',
LINE  987 | LINE 329 |       align: 'left',
LINE  988 | LINE 330 |       format: (val) => cambiarFormatoFecha(val),
LINE  989 | LINE 331 |       dataType: 'date',
LINE  990 | LINE 332 |     },
LINE  991 | LINE 333 |     { name: 'codigo', label: 'Cod.', field: 'codigo', align: 'left', dataType: 'text' },
LINE  992 | LINE 334 |     { name: 'nombre', label: 'Nombre', field: 'nombre', align: 'left', dataType: 'text' },
LINE  993 | LINE 335 |     {
LINE  994 | LINE 336 |       name: 'descripcion',
LINE  995 | LINE 337 |       label: 'Descripción',
LINE  996 | LINE 338 |       field: 'descripcion',
LINE  997 | LINE 339 |       align: 'left',
LINE  998 | LINE 340 |       dataType: 'text',
LINE  999 | LINE 341 |     },
LINE 1000 | LINE 342 |     { name: 'categoria', label: 'Categoría', field: 'categoria', align: 'left', dataType: 'text' },
LINE 1001 | LINE 343 |     {
LINE 1002 | LINE 344 |       name: 'subcategoria',
LINE 1003 | LINE 345 |       label: 'Sub Categorías',
LINE 1004 | LINE 346 |       field: 'subcategoria',
LINE 1005 | LINE 347 |       align: 'left',
LINE 1006 | LINE 348 |       dataType: 'text',
LINE 1007 | LINE 349 |     },
LINE 1008 | LINE 350 |     {
LINE 1009 | LINE 351 |       name: 'codigobarras',
LINE 1010 | LINE 352 |       label: 'Cod.Barra',
LINE 1011 | LINE 353 |       field: 'codigobarras',
LINE 1012 | LINE 354 |       align: 'right',
LINE 1013 | LINE 355 |       dataType: 'text',
LINE 1014 | LINE 356 |     },
LINE 1015 | LINE 357 |     {
LINE 1016 | LINE 358 |       name: 'medida',
LINE 1017 | LINE 359 |       label: 'Caract.',
LINE 1018 | LINE 360 |       field: 'medida',
LINE 1019 | LINE 361 |       align: 'left',
LINE 1020 | LINE 362 |       dataType: 'text',
LINE 1021 | LINE 363 |       defaultVisible: false,
LINE 1022 | LINE 364 |     },
LINE 1023 | LINE 365 |     {
LINE 1024 | LINE 366 |       name: 'estadoproducto',
LINE 1025 | LINE 367 |       label: 'Estado',
LINE 1026 | LINE 368 |       field: 'estadoproducto',
LINE 1027 | LINE 369 |       align: 'left',
LINE 1028 | LINE 370 |       dataType: 'text',
LINE 1029 | LINE 371 |       defaultVisible: false,
LINE 1030 | LINE 372 |     },
LINE 1031 | LINE 373 |     {
LINE 1032 | LINE 374 |       name: 'unidad',
LINE 1033 | LINE 375 |       label: 'Unidad',
LINE 1034 | LINE 376 |       field: 'unidad',
LINE 1035 | LINE 377 |       align: 'left',
LINE 1036 | LINE 378 |       dataType: 'text',
LINE 1037 | LINE 379 |       defaultVisible: false,
LINE 1038 | LINE 380 |     },
LINE 1039 | LINE 381 |     {
LINE 1040 | LINE 382 |       name: 'caracteristica',
LINE 1041 | LINE 383 |       label: 'Otras caract.',
LINE 1042 | LINE 384 |       field: 'caracteristica',
LINE 1043 | LINE 385 |       align: 'left',
LINE 1044 | LINE 386 |       dataType: 'text',
LINE 1045 | LINE 387 |       defaultVisible: false,
LINE 1046 | LINE 388 |     },
LINE 1047 | LINE 389 | 
LINE 1048 | LINE 390 |     { name: 'imagen', label: 'Imagen', field: 'imagen', align: 'center' },
LINE 1049 | LINE 391 |     { name: 'opciones', label: 'Opciones', field: 'opciones', sortable: false },
LINE 1050 | LINE 392 |     {
LINE 1051 | LINE 393 |       name: 'seleccionar',
LINE 1052 | LINE 394 |       label: '',
LINE 1053 | LINE 395 |       field: 'seleccionar',
LINE 1054 | LINE 396 |       align: 'center',
LINE 1055 | LINE 397 |       sortable: false,
LINE 1056 | LINE 398 |       headerStyle: 'width: 50px',
LINE 1057 | LINE 399 |     },
LINE 1058 | LINE 400 |   ]
LINE 1059 | LINE 401 | }
LINE 1060 | LINE 402 | 
LINE 1061 | LINE 403 | const arrayHeaders = [
LINE 1062 | LINE 404 |   'numero',
LINE 1063 | LINE 405 |   'fecha',
LINE 1064 | LINE 406 |   'codigo',
LINE 1065 | LINE 407 |   'nombre',
LINE 1066 | LINE 408 |   'descripcion',
LINE 1067 | LINE 409 |   'categoria',
LINE 1068 | LINE 410 |   'subcategoria',
LINE 1069 | LINE 411 |   'codigobarras',
LINE 1070 | LINE 412 |   'medida',
LINE 1071 | LINE 413 |   'estadoproducto',
LINE 1072 | LINE 414 |   'unidad',
LINE 1073 | LINE 415 |   'caracteristica',
LINE 1074 | LINE 416 |   'productosin',
LINE 1075 | LINE 417 |   'codigonandina',
LINE 1076 | LINE 418 | ]
LINE 1077 | LINE 419 | 
LINE 1078 | LINE 420 | const search = ref('')
LINE 1079 | LINE 421 | 
LINE 1080 | LINE 422 | const filteredRows = computed(() => {
LINE 1081 | LINE 423 |   if (!search.value) return props.rows
LINE 1082 | LINE 424 |   const term = search.value.toLowerCase()
LINE 1083 | LINE 425 |   return props.rows.filter((row) => {
LINE 1084 | LINE 426 |     // Buscar el término en cualquier propiedad de la fila (sin importar qué columna sea)
LINE 1085 | LINE 427 |     return Object.values(row).some((val) => val && String(val).toLowerCase().includes(term))
LINE 1086 | LINE 428 |   })
LINE 1087 | LINE 429 | })
LINE 1088 | LINE 430 | 
LINE 1089 | LINE 431 | const exportarFormato = () => {
LINE 1090 | LINE 432 |   exportarPlantillaProductos()
LINE 1091 | LINE 433 | }
LINE 1092 | LINE 434 | 
LINE 1093 | LINE 435 | const exportarDatos = () => {
LINE 1094 | LINE 436 |   if (props.rows.length === 0) {
LINE 1095 | LINE 437 |     $q.notify({ type: 'warning', message: 'No hay datos para exportar' })
LINE 1096 | LINE 438 |     return
LINE 1097 | LINE 439 |   }
LINE 1098 | LINE 440 |   exportToXLSX_CatalogoProductos(props.rows)
LINE 1099 | LINE 441 | }
LINE 1100 | LINE 442 | 
LINE 1101 | LINE 443 | const emit = defineEmits([
LINE 1102 | LINE 444 |   'add',
LINE 1103 | LINE 445 |   'edit-item',
LINE 1104 | LINE 446 |   'delete-item',
LINE 1105 | LINE 447 |   'toggle-status',
LINE 1106 | LINE 448 |   'mostrarReporte',
LINE 1107 | LINE 449 |   'importar',
LINE 1108 | LINE 450 |   'delete-selected',
LINE 1109 | LINE 451 |   'gestionar-variantes',
LINE 1110 | LINE 452 | ])
LINE 1111 | LINE 453 | 
LINE 1112 | LINE 454 | const toggleSeleccion = (id, checked) => {
LINE 1113 | LINE 455 |   if (checked) {
LINE 1114 | LINE 456 |     selectedIds.value.add(id)
LINE 1115 | LINE 457 |   } else {
LINE 1116 | LINE 458 |     selectedIds.value.delete(id)
LINE 1117 | LINE 459 |   }
LINE 1118 | LINE 460 |   // Forzar reactividad de Set (en Vue 3 no siempre es necesario, pero mejor)
LINE 1119 | LINE 461 |   selectedIds.value = new Set(selectedIds.value)
LINE 1120 | LINE 462 | }
LINE 1121 | LINE 463 | 
LINE 1122 | LINE 464 | const eliminarSeleccionados = () => {
LINE 1123 | LINE 465 |   if (selectedIds.value.size === 0) return
LINE 1124 | LINE 466 |   const ids = [...selectedIds.value]
LINE 1125 | LINE 467 |   emit('delete-selected', ids)
LINE 1126 | LINE 468 |   selectedIds.value = new Set() // limpiar selección
LINE 1127 | LINE 469 | }
LINE 1128 | LINE 470 | 
LINE 1129 | LINE 471 | const selectAll = computed({
LINE 1130 | LINE 472 |   get() {
LINE 1131 | LINE 473 |     return (
LINE 1132 | LINE 474 |       filteredRows.value.length > 0 &&
LINE 1133 | LINE 475 |       filteredRows.value.every((row) => selectedIds.value.has(row.id))
LINE 1134 | LINE 476 |     )
LINE 1135 | LINE 477 |   },
LINE 1136 | LINE 478 |   set(val) {
LINE 1137 | LINE 479 |     if (val) {
LINE 1138 | LINE 480 |       // Agregar todos los IDs visibles
LINE 1139 | LINE 481 |       const ids = filteredRows.value.map((row) => row.id)
LINE 1140 | LINE 482 |       selectedIds.value = new Set(ids)
LINE 1141 | LINE 483 |     } else {
LINE 1142 | LINE 484 |       selectedIds.value = new Set()
LINE 1143 | LINE 485 |     }
LINE 1144 | LINE 486 |   },
LINE 1145 | LINE 487 | })
LINE 1146 | LINE 488 | const onFileSelected = async (event) => {
LINE 1147 | LINE 489 |   const file = event.target.files[0]
LINE 1148 | LINE 490 |   if (!file) return
LINE 1149 | LINE 491 | 
LINE 1150 | LINE 492 |   try {
LINE 1151 | LINE 493 |     $q.loading.show({ message: 'Leyendo archivo Excel...' })
LINE 1152 | LINE 494 |     const data = await importarProductosDesdeExcel(file)
LINE 1153 | LINE 495 |     event.target.value = ''
LINE 1154 | LINE 496 | 
LINE 1155 | LINE 497 |     if (data && data.length > 0) {
LINE 1156 | LINE 498 |       // Actualizar mensaje con la cantidad de productos
LINE 1157 | LINE 499 |       const total = data.length
LINE 1158 | LINE 500 |       $q.loading.show({
LINE 1159 | LINE 501 |         message: `Importando ${total} producto${total !== 1 ? 's' : ''}...`,
LINE 1160 | LINE 502 |       })
LINE 1161 | LINE 503 |       // Emitir los datos; el padre debe poner importing=true (si no lo está) y luego false al finalizar
LINE 1162 | LINE 504 |       emit('importar', data)
LINE 1163 | LINE 505 |     } else {
LINE 1164 | LINE 506 |       // Si no hay datos, ocultar loading y notificar
LINE 1165 | LINE 507 |       $q.loading.hide()
LINE 1166 | LINE 508 |       $q.notify({ type: 'warning', message: 'El archivo no contiene productos válidos' })
LINE 1167 | LINE 509 |     }
LINE 1168 | LINE 510 |   } catch (error) {
LINE 1169 | LINE 511 |     console.error('Error al importar:', error)
LINE 1170 | LINE 512 |     $q.loading.hide()
LINE 1171 | LINE 513 |     $q.notify({ type: 'negative', message: 'Error al procesar el archivo Excel' })
LINE 1172 | LINE 514 |   }
LINE 1173 | LINE 515 | }
LINE 1174 | LINE 516 | watch(
LINE 1175 | LINE 517 |   () => props.rows,
LINE 1176 | LINE 518 |   () => {
LINE 1177 | LINE 519 |     selectedIds.value = new Set()
LINE 1178 | LINE 520 |   },
LINE 1179 | LINE 521 | )
LINE 1180 | LINE 522 | watch(
LINE 1181 | LINE 523 |   () => props.importing,
LINE 1182 | LINE 524 |   (nuevo) => {
LINE 1183 | LINE 525 |     if (!nuevo) {
LINE 1184 | LINE 526 |       $q.loading.hide()
LINE 1185 | LINE 527 |     }
LINE 1186 | LINE 528 |   },
LINE 1187 | LINE 529 | )
LINE 1188 | LINE 530 | </script>
LINE 1189 | LINE 531 | <style>
LINE 1190 | LINE 532 | .text-truncate {
LINE 1191 | LINE 533 |   max-width: 200px; /* ajusta según tu tabla */
LINE 1192 | LINE 534 |   white-space: nowrap;
LINE 1193 | LINE 535 |   overflow: hidden;
LINE 1194 | LINE 536 |   text-overflow: ellipsis;
LINE 1195 | LINE 537 | }
LINE 1196 | LINE 538 | </style>
LINE 1197 | ```
LINE 1198 | 
LINE 1199 | ==============================================================
LINE 1200 | FILE: src/composables/useReporteInventarioExterior.js
LINE 1201 | ==============================================================
LINE 1202 | ```js
LINE 1203 | LINE   1 | import { ref } from 'vue'
LINE 1204 | LINE   2 | import { date } from 'quasar'
LINE 1205 | LINE   3 | import { idusuario_md5, idempresa_md5 } from 'src/composables/FuncionesGenerales'
LINE 1206 | LINE   4 | import { api } from 'src/boot/axios'
LINE 1207 | LINE   5 | import axios from 'axios'
LINE 1208 | LINE   6 | import 'jspdf-autotable'
LINE 1209 | LINE   7 | 
LINE 1210 | LINE   8 | export function useReporteInventarioExterior() {
LINE 1211 | LINE   9 |   // --- Estado ---
LINE 1212 | LINE  10 |   const fechaInicio = ref(date.formatDate(Date.now(), 'YYYY-MM-DD'))
LINE 1213 | LINE  11 |   const fechaFin = ref(date.formatDate(Date.now(), 'YYYY-MM-DD'))
LINE 1214 | LINE  12 |   const datosReporte = ref([])
LINE 1215 | LINE  13 |   const cargando = ref(false)
LINE 1216 | LINE  14 | 
LINE 1217 | LINE  15 |   const idusuario = idusuario_md5()
LINE 1218 | LINE  16 |   // const idusuario = '03afdbd66e7929b125f8597834fa83a4'
LINE 1219 | LINE  17 | 
LINE 1220 | LINE  18 |   const idempresa = idempresa_md5()
LINE 1221 | LINE  19 |   console.log('ID Empresa MD5:', idempresa)
LINE 1222 | LINE  20 | 
LINE 1223 | LINE  21 |   const generarReporte = async () => {
LINE 1224 | LINE  22 |     cargando.value = true
LINE 1225 | LINE  23 |     try {
LINE 1226 | LINE  24 |       const endpoint = `reporteinvexterno/${idusuario}/${fechaInicio.value}/${fechaFin.value}`
LINE 1227 | LINE  25 |       console.log('Generando reporte con endpoint:', endpoint)
LINE 1228 | LINE  26 |       const response = await api.get(endpoint)
LINE 1229 | LINE  27 |       // Map data to add index and composite location
LINE 1230 | LINE  28 |       const promises = response.data.map(async (item, index) => {
LINE 1231 | LINE  29 |         const direccion = await obtenerDireccionComoString(item.latitud, item.longitud)
LINE 1232 | LINE  30 |         return {
LINE 1233 | LINE  31 |           ...item,
LINE 1234 | LINE  32 |           id: item.id_inv_externo,
LINE 1235 | LINE  33 |           indice: index + 1,
LINE 1236 | LINE  34 |           ubicacion: direccion,
LINE 1237 | LINE  35 |         }
LINE 1238 | LINE  36 |       })
LINE 1239 | LINE  37 |       datosReporte.value = await Promise.all(promises)
LINE 1240 | LINE  38 |       console.log('Datos del reporte recibidos (procesados):', datosReporte.value)
LINE 1241 | LINE  39 |     } catch (error) {
LINE 1242 | LINE  40 |       console.error('Error al generar reporte:', error)
LINE 1243 | LINE  41 |       datosReporte.value = []
LINE 1244 | LINE  42 |     } finally {
LINE 1245 | LINE  43 |       cargando.value = false
LINE 1246 | LINE  44 |     }
LINE 1247 | LINE  45 |   }
LINE 1248 | LINE  46 | 
LINE 1249 | LINE  47 |   async function obtenerDireccionComoString(lat, lng) {
LINE 1250 | LINE  48 |     try {
LINE 1251 | LINE  49 |       const url = 'https://nominatim.openstreetmap.org/reverse'
LINE 1252 | LINE  50 | 
LINE 1253 | LINE  51 |       const response = await axios.get(url, {
LINE 1254 | LINE  52 |         params: {
LINE 1255 | LINE  53 |           format: 'json',
LINE 1256 | LINE  54 |           lat: lat,
LINE 1257 | LINE  55 |           lon: lng,
LINE 1258 | LINE  56 |           zoom: 18,
LINE 1259 | LINE  57 |           addressdetails: 1,
LINE 1260 | LINE  58 |         },
LINE 1261 | LINE  59 |         headers: {
LINE 1262 | LINE  60 |           Accept: 'application/json',
LINE 1263 | LINE  61 |         },
LINE 1264 | LINE  62 |       })
LINE 1265 | LINE  63 | 
LINE 1266 | LINE  64 |       // Retorna toda la dirección en una sola cadena no una promesa
LINE 1267 | LINE  65 |       return response.data.display_name || 'Dirección no disponible'
LINE 1268 | LINE  66 |     } catch (error) {
LINE 1269 | LINE  67 |       console.error('Error obteniendo la dirección:', error)
LINE 1270 | LINE  68 |       return 'Dirección no disponible'
LINE 1271 | LINE  69 |     }
LINE 1272 | LINE  70 |   }
LINE 1273 | LINE  71 | 
LINE 1274 | LINE  72 |   //función para generar reporte detallado
LINE 1275 | LINE  73 |   const generarReporteDetalladoIExternor = async (idInventario) => {
LINE 1276 | LINE  74 |     try {
LINE 1277 | LINE  75 |       const endpoint = `detalleInventarioExterior/${idInventario}/${idempresa}`
LINE 1278 | LINE  76 |       console.log('Generando reporte detallado con endpoint:', endpoint)
LINE 1279 | LINE  77 |       const response = await api.get(endpoint)
LINE 1280 | LINE  78 |       console.log('Datos del reporte detallado recibidos:', response.data)
LINE 1281 | LINE  79 | 
LINE 1282 | LINE  80 |       // Limpiar descripción de productos
LINE 1283 | LINE  81 |       if (response.data && response.data.length > 0 && response.data[0].detalle) {
LINE 1284 | LINE  82 |         response.data[0].detalle = response.data[0].detalle.map((item) => ({
LINE 1285 | LINE  83 |           ...item,
LINE 1286 | LINE  84 |           descripcion_producto: item.descripcion_producto
LINE 1287 | LINE  85 |             ? item.descripcion_producto.replace(/\s+/g, ' ').trim()
LINE 1288 | LINE  86 |             : item.descripcion_producto,
LINE 1289 | LINE  87 |         }))
LINE 1290 | LINE  88 |       }
LINE 1291 | LINE  89 | 
LINE 1292 | LINE  90 |       return response.data // Retorna los datos detallados del inventario
LINE 1293 | LINE  91 |     } catch (error) {
LINE 1294 | LINE  92 |       console.error('Error al generar reporte detallado:', error)
LINE 1295 | LINE  93 |     }
LINE 1296 | LINE  94 |   }
LINE 1297 | LINE  95 | 
LINE 1298 | LINE  96 |   return {
LINE 1299 | LINE  97 |     fechaInicio,
LINE 1300 | LINE  98 |     fechaFin,
LINE 1301 | LINE  99 |     datosReporte,
LINE 1302 | LINE 100 |     cargando,
LINE 1303 | LINE 101 |     generarReporte,
LINE 1304 | LINE 102 | 
LINE 1305 | LINE 103 |     columns: [
LINE 1306 | LINE 104 |       // Columnas reales para la tabla UI
LINE 1307 | LINE 105 |       { name: 'indice', label: 'Nº', field: 'indice', sortable: true, align: 'left' },
LINE 1308 | LINE 106 |       {
LINE 1309 | LINE 107 |         name: 'fecha',
LINE 1310 | LINE 108 |         label: 'Fecha',
LINE 1311 | LINE 109 |         field: 'fecha_control',
LINE 1312 | LINE 110 |         sortable: true,
LINE 1313 | LINE 111 |         dataType: 'date',
LINE 1314 | LINE 112 |         align: 'left',
LINE 1315 | LINE 113 |       },
LINE 1316 | LINE 114 |       { name: 'almacen', label: 'Almacén', field: 'almacen', sortable: true, align: 'left' },
LINE 1317 | LINE 115 |       { name: 'cliente', label: 'Cliente', field: 'cliente', sortable: true, align: 'left' },
LINE 1318 | LINE 116 |       { name: 'sucursal', label: 'Sucursal', field: 'sucursal', sortable: true, align: 'left' },
LINE 1319 | LINE 117 |       { name: 'observaciones', label: 'Obs.', field: 'observaciones', align: 'left' },
LINE 1320 | LINE 118 |       { name: 'ubicacion', label: 'Ubicacion', field: 'ubicacion' },
LINE 1321 | LINE 119 |       { name: 'reporte', label: 'Reporte', field: 'reporte' }, // Added name and label.reporte matching table
LINE 1322 | LINE 120 |     ],
LINE 1323 | LINE 121 |     arrayHeaders: ['fecha', 'almacen', 'cliente', 'sucursal'], // Filtros de columna activados
LINE 1324 | LINE 122 |     generarReporteDetalladoIExternor,
LINE 1325 | LINE 123 |   }
LINE 1326 | LINE 124 | }
LINE 1327 | ```
LINE 1328 | 
LINE 1329 | ==============================================================
LINE 1330 | FILE: src/pages/producto/CproductoPage.vue
LINE 1331 | ==============================================================
LINE 1332 | ```vue
LINE 1333 | LINE   1 | <template>
LINE 1334 | LINE   2 |   <q-page v-if="mostrarmoduloConjunto">
LINE 1335 | LINE   3 |     <div class="row justify-end q-mb-md">
LINE 1336 | LINE   4 |       <q-btn
LINE 1337 | LINE   5 |         color="primary"
LINE 1338 | LINE   6 |         label="Volver a Productos"
LINE 1339 | LINE   7 |         icon="arrow_back"
LINE 1340 | LINE   8 |         @click="mostrarmoduloConjunto = false"
LINE 1341 | LINE   9 |         outline
LINE 1342 | LINE  10 |       />
LINE 1343 | LINE  11 |     </div>
LINE 1344 | LINE  12 |     <seriePage />
LINE 1345 | LINE  13 |   </q-page>
LINE 1346 | LINE  14 |   <q-page padding v-else>
LINE 1347 | LINE  15 |     <q-dialog v-model="showForm">
LINE 1348 | LINE  16 |       <q-card class="responsive-dialog">
LINE 1349 | LINE  17 |         <q-card-section class="bg-primary text-h6 text-white flex justify-between">
LINE 1350 | LINE  18 |           <div>Registrar Producto o Servicio</div>
LINE 1351 | LINE  19 |           <q-btn icon="close" @click="toggleForm" dense flat round />
LINE 1352 | LINE  20 |         </q-card-section>
LINE 1353 | LINE  21 |         <q-card-section class="q-pa-none">
LINE 1354 | LINE  22 |           <producto-form
LINE 1355 | LINE  23 |             :isEditing="isEditing"
LINE 1356 | LINE  24 |             :model-value="formData"
LINE 1357 | LINE  25 |             :categorias="categorias"
LINE 1358 | LINE  26 |             :estados="estados"
LINE 1359 | LINE  27 |             :subcategorias="subcategorias"
LINE 1360 | LINE  28 |             :unidades="unidades"
LINE 1361 | LINE  29 |             :medidas="medidas"
LINE 1362 | LINE  30 |             :productoSIN="ProductoSin"
LINE 1363 | LINE  31 |             :unidadSIN="UnidadSin"
LINE 1364 | LINE  32 |             @submit="handleSubmit"
LINE 1365 | LINE  33 |             @cancel="toggleForm"
LINE 1366 | LINE  34 |             @categoria-changed="loadsubcategorias"
LINE 1367 | LINE  35 |           />
LINE 1368 | LINE  36 |         </q-card-section>
LINE 1369 | LINE  37 |       </q-card>
LINE 1370 | LINE  38 |     </q-dialog>
LINE 1371 | LINE  39 | 
LINE 1372 | LINE  40 |     <producto-tabla
LINE 1373 | LINE  41 |       :rows="productos"
LINE 1374 | LINE  42 |       :loading="cargando"
LINE 1375 | LINE  43 |       :importing="importing"
LINE 1376 | LINE  44 |       @add="toggleForm"
LINE 1377 | LINE  45 |       @irconjunto="mostrarmoduloConjunto = true"
LINE 1378 | LINE  46 |       @mostrarReporte="mostrarReporte"
LINE 1379 | LINE  47 |       @edit-item="editUnit"
LINE 1380 | LINE  48 |       @delete-item="confirmDelete"
LINE 1381 | LINE  49 |       @toggleStatus="toggleStatus"
LINE 1382 | LINE  50 |       @importar="handleImport"
LINE 1383 | LINE  51 |       @delete-selected="eliminarProductosSeleccionados"
LINE 1384 | LINE  52 |       @gestionar-variantes="abrirVariantes"
LINE 1385 | LINE  53 |     />
LINE 1386 | LINE  54 | 
LINE 1387 | LINE  55 |     <ProductoVarianteDialog
LINE 1388 | LINE  56 |       v-model="showVariantesDialog"
LINE 1389 | LINE  57 |       :producto="productoVariantes"
LINE 1390 | LINE  58 |       :empresa="idempresa"
LINE 1391 | LINE  59 |     />
LINE 1392 | LINE  60 |   </q-page>
LINE 1393 | LINE  61 | </template>
LINE 1394 | LINE  62 | 
LINE 1395 | LINE  63 | <script setup>
LINE 1396 | LINE  64 | import { ref, onMounted } from 'vue'
LINE 1397 | LINE  65 | import { api } from 'boot/axios' // Asegúrate de tener esto configurado
LINE 1398 | LINE  66 | import { idempresa_md5, validarUsuario } from 'src/composables/FuncionesGenerales'
LINE 1399 | LINE  67 | import { useQuasar } from 'quasar'
LINE 1400 | LINE  68 | import { objectToFormData } from 'src/composables/FuncionesGenerales'
LINE 1401 | LINE  69 | import ProductoForm from 'src/components/producto/creacion/productoForm.vue'
LINE 1402 | LINE  70 | import ProductoTabla from 'src/components/producto/creacion/productoTable.vue'
LINE 1403 | LINE  71 | import { imagen } from 'src/boot/url'
LINE 1404 | LINE  72 | import { getTipoFactura, getToken } from 'src/composables/FuncionesG'
LINE 1405 | LINE  73 | import seriePage from 'src/modules/serie/page/seriePage.vue'
LINE 1406 | LINE  74 | import ProductoVarianteDialog from 'src/components/producto/variantes/productoVarianteDialog.vue'
LINE 1407 | LINE  75 | const tipoFactura = getTipoFactura(true)
LINE 1408 | LINE  76 | const mostrarmoduloConjunto = ref(false)
LINE 1409 | LINE  77 | const showVariantesDialog = ref(false)
LINE 1410 | LINE  78 | const productoVariantes = ref(null)
LINE 1411 | LINE  79 | console.log('Tipo Factura:', tipoFactura)
LINE 1412 | LINE  80 | const idempresa = idempresa_md5()
LINE 1413 | LINE  81 | const contenidousuario = validarUsuario()
LINE 1414 | LINE  82 | console.log(contenidousuario)
LINE 1415 | LINE  83 | const token = getToken()
LINE 1416 | LINE  84 | console.log('Token:', token)
LINE 1417 | LINE  85 | const productos = ref([])
LINE 1418 | LINE  86 | 
LINE 1419 | LINE  87 | const categorias = ref([])
LINE 1420 | LINE  88 | 
LINE 1421 | LINE  89 | const estados = ref([])
LINE 1422 | LINE  90 | const subcategorias = ref([])
LINE 1423 | LINE  91 | const unidades = ref([])
LINE 1424 | LINE  92 | const medidas = ref([])
LINE 1425 | LINE  93 | const $q = useQuasar()
LINE 1426 | LINE  94 | const isEditing = ref(false)
LINE 1427 | LINE  95 | const showForm = ref(false)
LINE 1428 | LINE  96 | const cargando = ref(false)
LINE 1429 | LINE  97 | const importing = ref(false)
LINE 1430 | LINE  98 | 
LINE 1431 | LINE  99 | const formData = ref({
LINE 1432 | LINE 100 |   ver: 'registrarProducto',
LINE 1433 | LINE 101 |   idempresa: idempresa,
LINE 1434 | LINE 102 | })
LINE 1435 | LINE 103 | const ProductoSin = ref([])
LINE 1436 | LINE 104 | const UnidadSin = ref([])
LINE 1437 | LINE 105 | async function loadRows() {
LINE 1438 | LINE 106 |   try {
LINE 1439 | LINE 107 |     cargando.value = true
LINE 1440 | LINE 108 |     const tipo = getTipoFactura()
LINE 1441 | LINE 109 |     let point = ``
LINE 1442 | LINE 110 |     if (token && tipo && getTipoFactura(true) && getToken(true)) {
LINE 1443 | LINE 111 |       point = `listaProducto/${idempresa}/${token}/${tipo}`
LINE 1444 | LINE 112 |     } else {
LINE 1445 | LINE 113 |       point = `listaProducto/${idempresa}/`
LINE 1446 | LINE 114 |     }
LINE 1447 | LINE 115 |     console.log('Endpoint:', point)
LINE 1448 | LINE 116 |     const response = await api.get(point)
LINE 1449 | LINE 117 |     console.log('estos son los datos', response.data)
LINE 1450 | LINE 118 |     productos.value = response.data.map((obj, index) => ({ ...obj, numero: index + 1 }))
LINE 1451 | LINE 119 |   } catch (error) {
LINE 1452 | LINE 120 |     console.error('Error al cargar datos:', error)
LINE 1453 | LINE 121 |     $q.notify({
LINE 1454 | LINE 122 |       type: 'negative',
LINE 1455 | LINE 123 |       message: 'No se pudieron cargar los datos del catálogo',
LINE 1456 | LINE 124 |     })
LINE 1457 | LINE 125 |   } finally {
LINE 1458 | LINE 126 |     cargando.value = false
LINE 1459 | LINE 127 |   }
LINE 1460 | LINE 128 | }
LINE 1461 | LINE 129 | 
LINE 1462 | LINE 130 | async function loadcategorias() {
LINE 1463 | LINE 131 |   try {
LINE 1464 | LINE 132 |     const response = await api.get(`listaCategoriaProducto/${idempresa}`) // Cambia a tu ruta real
LINE 1465 | LINE 133 |     console.log(response)
LINE 1466 | LINE 134 |     const filtrados = response.data.filter((u) => u.estado == 1 && (!u.idp || u.idp == 0))
LINE 1467 | LINE 135 |     const formateado = filtrados.map((item) => ({
LINE 1468 | LINE 136 |       label: item.nombre,
LINE 1469 | LINE 137 |       value: item.id,
LINE 1470 | LINE 138 |     }))
LINE 1471 | LINE 139 |     categorias.value = formateado // Asume que la API devuelve un array
LINE 1472 | LINE 140 |   } catch (error) {
LINE 1473 | LINE 141 |     console.error('Error al cargar datos:', error)
LINE 1474 | LINE 142 |     $q.notify({
LINE 1475 | LINE 143 |       type: 'negative',
LINE 1476 | LINE 144 |       message: 'No se pudieron cargar los datos',
LINE 1477 | LINE 145 |     })
LINE 1478 | LINE 146 |   }
LINE 1479 | LINE 147 | }
LINE 1480 | LINE 148 | async function loadestados() {
LINE 1481 | LINE 149 |   try {
LINE 1482 | LINE 150 |     const response = await api.get(`listaEstadoProducto/${idempresa}`) // Cambia a tu ruta real
LINE 1483 | LINE 151 |     console.log(response)
LINE 1484 | LINE 152 |     const filtrados = response.data.filter((u) => u.estado == 1)
LINE 1485 | LINE 153 |     const formateado = filtrados.map((item) => ({
LINE 1486 | LINE 154 |       label: item.nombre,
LINE 1487 | LINE 155 |       value: item.id,
LINE 1488 | LINE 156 |     }))
LINE 1489 | LINE 157 |     estados.value = formateado // Asume que la API devuelve un array
LINE 1490 | LINE 158 |   } catch (error) {
LINE 1491 | LINE 159 |     console.error('Error al cargar datos:', error)
LINE 1492 | LINE 160 |     $q.notify({
LINE 1493 | LINE 161 |       type: 'negative',
LINE 1494 | LINE 162 |       message: 'No se pudieron cargar los Estados de Producto',
LINE 1495 | LINE 163 |     })
LINE 1496 | LINE 164 |   }
LINE 1497 | LINE 165 | }
LINE 1498 | LINE 166 | async function loadsubcategorias(idcategoria) {
LINE 1499 | LINE 167 |   console.log('idcategoria:', idcategoria)
LINE 1500 | LINE 168 | 
LINE 1501 | LINE 169 |   if (!idcategoria) {
LINE 1502 | LINE 170 |     subcategorias.value = []
LINE 1503 | LINE 171 |     return
LINE 1504 | LINE 172 |   }
LINE 1505 | LINE 173 |   try {
LINE 1506 | LINE 174 |     const response = await api.get(`listaCategoriaProducto/${idempresa}`) // Cambia a tu ruta real
LINE 1507 | LINE 175 |     console.log(formData.value)
LINE 1508 | LINE 176 |     const filtrados = response.data.filter((u) => u.estado == 1 && u.idp == idcategoria)
LINE 1509 | LINE 177 |     const formateado = filtrados.map((item) => ({
LINE 1510 | LINE 178 |       label: item.nombre,
LINE 1511 | LINE 179 |       value: item.id,
LINE 1512 | LINE 180 |     }))
LINE 1513 | LINE 181 |     subcategorias.value = formateado // Asume que la API devuelve un array
LINE 1514 | LINE 182 |   } catch (error) {
LINE 1515 | LINE 183 |     console.error('Error al cargar datos:', error)
LINE 1516 | LINE 184 |     $q.notify({
LINE 1517 | LINE 185 |       type: 'negative',
LINE 1518 | LINE 186 |       message: 'No se pudieron cargar los datos',
LINE 1519 | LINE 187 |     })
LINE 1520 | LINE 188 |   }
LINE 1521 | LINE 189 | }
LINE 1522 | LINE 190 | async function loadunidades() {
LINE 1523 | LINE 191 |   try {
LINE 1524 | LINE 192 |     const response = await api.get(`listaUnidadProducto/${idempresa}`) // Cambia a tu ruta real
LINE 1525 | LINE 193 |     console.log(response)
LINE 1526 | LINE 194 |     const filtrados = response.data.filter((u) => u.estado == 1)
LINE 1527 | LINE 195 |     const formateado = filtrados.map((item) => ({
LINE 1528 | LINE 196 |       label: item.nombre + ' : ' + item.descripcion,
LINE 1529 | LINE 197 |       value: item.id,
LINE 1530 | LINE 198 |     }))
LINE 1531 | LINE 199 |     unidades.value = formateado // Asume que la API devuelve un array
LINE 1532 | LINE 200 |   } catch (error) {
LINE 1533 | LINE 201 |     console.error('Error al cargar datos:', error)
LINE 1534 | LINE 202 |     $q.notify({
LINE 1535 | LINE 203 |       type: 'negative',
LINE 1536 | LINE 204 |       message: 'No se pudieron cargar los datos',
LINE 1537 | LINE 205 |     })
LINE 1538 | LINE 206 |   }
LINE 1539 | LINE 207 | }
LINE 1540 | LINE 208 | async function ListaProductoSin() {
LINE 1541 | LINE 209 |   if (!tipoFactura) {
LINE 1542 | LINE 210 |     return
LINE 1543 | LINE 211 |   }
LINE 1544 | LINE 212 |   const contenidousuario = validarUsuario()
LINE 1545 | LINE 213 |   const token = contenidousuario[0]?.factura?.access_token
LINE 1546 | LINE 214 |   const tipo = contenidousuario[0]?.factura?.tipo
LINE 1547 | LINE 215 |   const endpoint = `listaproductoSIN/productossin/${token}/${tipo}`
LINE 1548 | LINE 216 |   try {
LINE 1549 | LINE 217 |     const response = await api.get(endpoint) // Cambia a tu ruta real
LINE 1550 | LINE 218 |     console.log(response)
LINE 1551 | LINE 219 |     const res = response.data
LINE 1552 | LINE 220 |     if (res.status == 'success') {
LINE 1553 | LINE 221 |       const formateado = res.data.map((item) => ({
LINE 1554 | LINE 222 |         label: item.descripcion,
LINE 1555 | LINE 223 |         value: item.codigo,
LINE 1556 | LINE 224 |       }))
LINE 1557 | LINE 225 |       ProductoSin.value = formateado
LINE 1558 | LINE 226 |     }
LINE 1559 | LINE 227 |   } catch (error) {
LINE 1560 | LINE 228 |     console.error('Error al cargar datos:', error)
LINE 1561 | LINE 229 |     $q.notify({
LINE 1562 | LINE 230 |       type: 'negative',
LINE 1563 | LINE 231 |       message: 'No se pudieron cargar los datos',
LINE 1564 | LINE 232 |     })
LINE 1565 | LINE 233 |   }
LINE 1566 | LINE 234 | }
LINE 1567 | LINE 235 | async function ListaUnidadSin() {
LINE 1568 | LINE 236 |   if (!tipoFactura) {
LINE 1569 | LINE 237 |     return
LINE 1570 | LINE 238 |   }
LINE 1571 | LINE 239 |   const contenidousuario = validarUsuario()
LINE 1572 | LINE 240 |   const token = contenidousuario[0]?.factura?.access_token
LINE 1573 | LINE 241 |   const tipo = contenidousuario[0]?.factura?.tipo
LINE 1574 | LINE 242 |   const endpoint = `listaproductoSIN/unidadsin/${token}/${tipo}`
LINE 1575 | LINE 243 |   try {
LINE 1576 | LINE 244 |     const response = await api.get(endpoint) // Cambia a tu ruta real
LINE 1577 | LINE 245 |     console.log(response)
LINE 1578 | LINE 246 |     const res = response.data
LINE 1579 | LINE 247 |     if (res.status == 'success') {
LINE 1580 | LINE 248 |       const formateado = res.data.map((item) => ({
LINE 1581 | LINE 249 |         label: item.descripcion,
LINE 1582 | LINE 250 |         value: item.codigo,
LINE 1583 | LINE 251 |       }))
LINE 1584 | LINE 252 |       UnidadSin.value = formateado
LINE 1585 | LINE 253 |     }
LINE 1586 | LINE 254 |   } catch (error) {
LINE 1587 | LINE 255 |     console.error('Error al cargar datos:', error)
LINE 1588 | LINE 256 |     $q.notify({
LINE 1589 | LINE 257 |       type: 'negative',
LINE 1590 | LINE 258 |       message: 'No se pudieron cargar los datos',
LINE 1591 | LINE 259 |     })
LINE 1592 | LINE 260 |   }
LINE 1593 | LINE 261 | }
LINE 1594 | LINE 262 | async function loadmedidas() {
LINE 1595 | LINE 263 |   try {
LINE 1596 | LINE 264 |     const response = await api.get(`listaCaracteristicaProducto/${idempresa}`) // Cambia a tu ruta real
LINE 1597 | LINE 265 |     console.log(response)
LINE 1598 | LINE 266 |     const filtrados = response.data.filter((u) => u.estado == 1)
LINE 1599 | LINE 267 | 
LINE 1600 | LINE 268 |     const formateado = filtrados.map((item) => ({
LINE 1601 | LINE 269 |       label: item.nombre,
LINE 1602 | LINE 270 |       value: item.id,
LINE 1603 | LINE 271 |     }))
LINE 1604 | LINE 272 |     medidas.value = formateado // Asume que la API devuelve un array
LINE 1605 | LINE 273 |   } catch (error) {
LINE 1606 | LINE 274 |     console.error('Error al cargar datos:', error)
LINE 1607 | LINE 275 |     $q.notify({
LINE 1608 | LINE 276 |       type: 'negative',
LINE 1609 | LINE 277 |       message: 'No se pudieron cargar los datos',
LINE 1610 | LINE 278 |     })
LINE 1611 | LINE 279 |   }
LINE 1612 | LINE 280 | }
LINE 1613 | LINE 281 | 
LINE 1614 | LINE 282 | const handleSubmit = async (data) => {
LINE 1615 | LINE 283 |   const formData = objectToFormData(data)
LINE 1616 | LINE 284 | 
LINE 1617 | LINE 285 |   console.log('=== FormData entries ===')
LINE 1618 | LINE 286 |   // for (let [k, v] of formData.entries()) {
LINE 1619 | LINE 287 |   //   console.log(`${k}: ${v}`)
LINE 1620 | LINE 288 |   // }
LINE 1621 | LINE 289 | 
LINE 1622 | LINE 290 |   try {
LINE 1623 | LINE 291 |     if (isEditing.value) {
LINE 1624 | LINE 292 |       const response = await api.post(``, formData)
LINE 1625 | LINE 293 |       console.log('Edit response:', response.data)
LINE 1626 | LINE 294 |     } else {
LINE 1627 | LINE 295 |       const response = await api.post(``, formData)
LINE 1628 | LINE 296 |       console.log('Create response:', response.data)
LINE 1629 | LINE 297 |     }
LINE 1630 | LINE 298 |     $q.notify({
LINE 1631 | LINE 299 |       type: 'positive',
LINE 1632 | LINE 300 |       message: isEditing.value ? 'Editado correctamente' : 'Registrado correctamente',
LINE 1633 | LINE 301 |     })
LINE 1634 | LINE 302 |     loadRows()
LINE 1635 | LINE 303 |   } catch (error) {
LINE 1636 | LINE 304 |     console.error('Error al guardar:', error)
LINE 1637 | LINE 305 |     $q.notify({
LINE 1638 | LINE 306 |       type: 'negative',
LINE 1639 | LINE 307 |       message: 'Ocurrió un error al guardar' + error,
LINE 1640 | LINE 308 |     })
LINE 1641 | LINE 309 |   }
LINE 1642 | LINE 310 |   toggleForm()
LINE 1643 | LINE 311 | }
LINE 1644 | LINE 312 | const toggleForm = () => {
LINE 1645 | LINE 313 |   showForm.value = !showForm.value
LINE 1646 | LINE 314 |   if (!showForm.value) {
LINE 1647 | LINE 315 |     isEditing.value = false
LINE 1648 | LINE 316 |     resetForm()
LINE 1649 | LINE 317 |     subcategorias.value = [] // limpia subcategorías
LINE 1650 | LINE 318 |   }
LINE 1651 | LINE 319 | }
LINE 1652 | LINE 320 | function resetForm() {
LINE 1653 | LINE 321 |   isEditing.value = false
LINE 1654 | LINE 322 |   formData.value = {
LINE 1655 | LINE 323 |     ver: 'registrarProducto',
LINE 1656 | LINE 324 |     idempresa: idempresa,
LINE 1657 | LINE 325 |   }
LINE 1658 | LINE 326 | }
LINE 1659 | LINE 327 | const editUnit = async (row) => {
LINE 1660 | LINE 328 |   console.log(row)
LINE 1661 | LINE 329 |   const tipo = getTipoFactura()
LINE 1662 | LINE 330 |   let endpoint = ``
LINE 1663 | LINE 331 |   if (token && tipo && getTipoFactura(true) && getToken(true)) {
LINE 1664 | LINE 332 |     endpoint = `verificarExistenciaProducto/${row.id}/${token}/${tipo}`
LINE 1665 | LINE 333 |   } else {
LINE 1666 | LINE 334 |     endpoint = `verificarExistenciaProducto/${row.id}/`
LINE 1667 | LINE 335 |   }
LINE 1668 | LINE 336 |   console.log(endpoint)
LINE 1669 | LINE 337 |   const response = await api.get(endpoint) // Cambia a tu ruta real
LINE 1670 | LINE 338 |   console.log('API Response:', response.data)
LINE 1671 | LINE 339 |   const item = response.data.datos
LINE 1672 | LINE 340 |   console.log('Item data:', item)
LINE 1673 | LINE 341 | 
LINE 1674 | LINE 342 |   // Handle subcategoria - it might be missing, null, 0, or empty string
LINE 1675 | LINE 343 |   const rawSubcategoria = item?.idsubcategoria ?? null
LINE 1676 | LINE 344 |   const subcategoriaValue =
LINE 1677 | LINE 345 |     rawSubcategoria !== null && rawSubcategoria !== '0' && rawSubcategoria !== 0
LINE 1678 | LINE 346 |       ? rawSubcategoria
LINE 1679 | LINE 347 |       : null
LINE 1680 | LINE 348 | 
LINE 1681 | LINE 349 |   formData.value = {
LINE 1682 | LINE 350 |     ver: 'editarProducto',
LINE 1683 | LINE 351 |     id: item.id,
LINE 1684 | LINE 352 |     idempresa: idempresa,
LINE 1685 | LINE 353 |     codigo: item.codigo,
LINE 1686 | LINE 354 |     nombre: item.nombre,
LINE 1687 | LINE 355 |     descripcion: item.descripcion,
LINE 1688 | LINE 356 |     codigobarras: item.codbarras,
LINE 1689 | LINE 357 |     categoria: item?.idcategoria ?? null,
LINE 1690 | LINE 358 |     subcategoria: subcategoriaValue,
LINE 1691 | LINE 359 |     estadoproductos: item.idestadoproducto,
LINE 1692 | LINE 360 |     unidad: item.idunidad,
LINE 1693 | LINE 361 |     medida: item.idmedida,
LINE 1694 | LINE 362 |     caracteristica: item.caracteristica && item.caracteristica !== '0' ? item.caracteristica : '',
LINE 1695 | LINE 363 |     vista: imagen + item.imagen,
LINE 1696 | LINE 364 |     imagen: item.imagen,
LINE 1697 | LINE 365 |     codigosin:
LINE 1698 | LINE 366 |       tipoFactura && item.productosin && item.productosin[0] ? item.productosin[0].codigo : '',
LINE 1699 | LINE 367 |     unidadsin: tipoFactura && item.unidadsin && item.unidadsin[0] ? item.unidadsin[0].codigo : '',
LINE 1700 | LINE 368 |     codigoNandina:
LINE 1701 | LINE 369 |       tipoFactura && item.codigonandina && item.codigonandina !== '0' ? item.codigonandina : '',
LINE 1702 | LINE 370 |   }
LINE 1703 | LINE 371 | 
LINE 1704 | LINE 372 |   console.log('FormData to load:', formData.value)
LINE 1705 | LINE 373 |   loadsubcategorias(item?.idcategoria ?? null)
LINE 1706 | LINE 374 |   isEditing.value = true
LINE 1707 | LINE 375 |   showForm.value = true
LINE 1708 | LINE 376 | }
LINE 1709 | LINE 377 | 
LINE 1710 | LINE 378 | const confirmDelete = (row) => {
LINE 1711 | LINE 379 |   console.log(row)
LINE 1712 | LINE 380 | 
LINE 1713 | LINE 381 |   $q.dialog({
LINE 1714 | LINE 382 |     title: 'Confirmar',
LINE 1715 | LINE 383 |     message: `¿Eliminar Producto "${row.nombre}"?`,
LINE 1716 | LINE 384 |     cancel: true,
LINE 1717 | LINE 385 |     persistent: true,
LINE 1718 | LINE 386 |   }).onOk(async () => {
LINE 1719 | LINE 387 |     try {
LINE 1720 | LINE 388 |       const response = await api.get(`eliminarProducto/${row.id}`) // Cambia a tu ruta real
LINE 1721 | LINE 389 |       console.log(response)
LINE 1722 | LINE 390 |       if (response.data.estado === 'exito') {
LINE 1723 | LINE 391 |         loadRows()
LINE 1724 | LINE 392 |         $q.notify({
LINE 1725 | LINE 393 |           type: 'positive',
LINE 1726 | LINE 394 |           message: response.data.mensaje,
LINE 1727 | LINE 395 |         })
LINE 1728 | LINE 396 |       } else {
LINE 1729 | LINE 397 |         $q.notify({
LINE 1730 | LINE 398 |           type: 'negative',
LINE 1731 | LINE 399 |           message: response.data.mensaje,
LINE 1732 | LINE 400 |         })
LINE 1733 | LINE 401 |       }
LINE 1734 | LINE 402 |     } catch (error) {
LINE 1735 | LINE 403 |       console.error('Error al cargar datos:', error)
LINE 1736 | LINE 404 |       $q.notify({
LINE 1737 | LINE 405 |         type: 'negative',
LINE 1738 | LINE 406 |         message: 'No se pudieron cargar los datos',
LINE 1739 | LINE 407 |       })
LINE 1740 | LINE 408 |     }
LINE 1741 | LINE 409 |   })
LINE 1742 | LINE 410 | }
LINE 1743 | LINE 411 | const eliminarProductosSeleccionados = (ids) => {
LINE 1744 | LINE 412 |   console.log(ids)
LINE 1745 | LINE 413 | 
LINE 1746 | LINE 414 |   $q.dialog({
LINE 1747 | LINE 415 |     title: 'Confirmar',
LINE 1748 | LINE 416 |     message: `¿Eliminar Productos seleccionados?`,
LINE 1749 | LINE 417 |     cancel: true,
LINE 1750 | LINE 418 |     persistent: true,
LINE 1751 | LINE 419 |   }).onOk(async () => {
LINE 1752 | LINE 420 |     try {
LINE 1753 | LINE 421 |       const data = {
LINE 1754 | LINE 422 |         ver: 'eliminarProductosMasivo',
LINE 1755 | LINE 423 |         ids: ids,
LINE 1756 | LINE 424 |       }
LINE 1757 | LINE 425 |       const response = await api.post(``, data) // Cambia a tu ruta real
LINE 1758 | LINE 426 |       console.log(response)
LINE 1759 | LINE 427 |       if (response.data.estado === 'exito') {
LINE 1760 | LINE 428 |         loadRows()
LINE 1761 | LINE 429 |         $q.notify({
LINE 1762 | LINE 430 |           type: 'positive',
LINE 1763 | LINE 431 |           message: response.data.mensaje,
LINE 1764 | LINE 432 |         })
LINE 1765 | LINE 433 |       } else {
LINE 1766 | LINE 434 |         $q.notify({
LINE 1767 | LINE 435 |           type: 'negative',
LINE 1768 | LINE 436 |           message: response.data.mensaje,
LINE 1769 | LINE 437 |         })
LINE 1770 | LINE 438 |       }
LINE 1771 | LINE 439 |     } catch (error) {
LINE 1772 | LINE 440 |       console.error('Error al cargar datos:', error)
LINE 1773 | LINE 441 |       $q.notify({
LINE 1774 | LINE 442 |         type: 'negative',
LINE 1775 | LINE 443 |         message: 'No se pudieron cargar los datos',
LINE 1776 | LINE 444 |       })
LINE 1777 | LINE 445 |     }
LINE 1778 | LINE 446 |   })
LINE 1779 | LINE 447 | }
LINE 1780 | LINE 448 | 
LINE 1781 | LINE 449 | const handleImport = async (data) => {
LINE 1782 | LINE 450 |   let successCount = 0
LINE 1783 | LINE 451 |   let errorCount = 0
LINE 1784 | LINE 452 |   importing.value = true
LINE 1785 | LINE 453 | 
LINE 1786 | LINE 454 |   $q.loading.show({
LINE 1787 | LINE 455 |     message: 'Importando productos...',
LINE 1788 | LINE 456 |   })
LINE 1789 | LINE 457 | 
LINE 1790 | LINE 458 |   for (const item of data) {
LINE 1791 | LINE 459 |     try {
LINE 1792 | LINE 460 |       // Mapear nombres a IDs
LINE 1793 | LINE 461 |       const cat = categorias.value.find(
LINE 1794 | LINE 462 |         (c) => c.label.toLowerCase() === item.categoria_nombre?.toLowerCase(),
LINE 1795 | LINE 463 |       )
LINE 1796 | LINE 464 |       const unit = unidades.value.find((u) =>
LINE 1797 | LINE 465 |         u.label.toLowerCase().includes(item.unidad_nombre?.toLowerCase()),
LINE 1798 | LINE 466 |       )
LINE 1799 | LINE 467 |       const state = estados.value.find(
LINE 1800 | LINE 468 |         (e) => e.label.toLowerCase() === item.estado_nombre?.toLowerCase(),
LINE 1801 | LINE 469 |       )
LINE 1802 | LINE 470 |       const measure = medidas.value.find(
LINE 1803 | LINE 471 |         (m) => m.label.toLowerCase() === item.medida_nombre?.toLowerCase(),
LINE 1804 | LINE 472 |       )
LINE 1805 | LINE 473 | 
LINE 1806 | LINE 474 |       const payload = {
LINE 1807 | LINE 475 |         ver: 'registrarProducto',
LINE 1808 | LINE 476 |         idempresa: idempresa,
LINE 1809 | LINE 477 |         codigo: item.codigo || '',
LINE 1810 | LINE 478 |         nombre: item.nombre || '',
LINE 1811 | LINE 479 |         descripcion: item.descripcion || '',
LINE 1812 | LINE 480 |         codigobarras: item.codigobarras || '',
LINE 1813 | LINE 481 |         categoria: cat ? cat.value : null,
LINE 1814 | LINE 482 |         subcategoria: null, // No tenemos mapeo de subcat directo sin contexto de cat en Excel por ahora
LINE 1815 | LINE 483 |         estadoproductos: state ? state.value : estados.value[0]?.value || null,
LINE 1816 | LINE 484 |         unidad: unit ? unit.value : unidades.value[0]?.value || null,
LINE 1817 | LINE 485 |         medida: measure ? measure.value : medidas.value[0]?.value || null,
LINE 1818 | LINE 486 |         caracteristica: item.caracteristica || '',
LINE 1819 | LINE 487 |         codigonandina: item.codigonandina || '',
LINE 1820 | LINE 488 |       }
LINE 1821 | LINE 489 | 
LINE 1822 | LINE 490 |       console.log('Bulk Import saving:', payload)
LINE 1823 | LINE 491 |       const fData = objectToFormData(payload)
LINE 1824 | LINE 492 |       const response = await api.post(``, fData)
LINE 1825 | LINE 493 |       console.log(response.data)
LINE 1826 | LINE 494 |       if (response.data.estado === 'exito') {
LINE 1827 | LINE 495 |         successCount++
LINE 1828 | LINE 496 |       } else {
LINE 1829 | LINE 497 |         errorCount++
LINE 1830 | LINE 498 |       }
LINE 1831 | LINE 499 |     } catch (err) {
LINE 1832 | LINE 500 |       console.error('Error importing product:', err)
LINE 1833 | LINE 501 |       errorCount++
LINE 1834 | LINE 502 |     }
LINE 1835 | LINE 503 |   }
LINE 1836 | LINE 504 | 
LINE 1837 | LINE 505 |   importing.value = false
LINE 1838 | LINE 506 | 
LINE 1839 | LINE 507 |   $q.notify({
LINE 1840 | LINE 508 |     type: successCount > 0 ? 'positive' : 'negative',
LINE 1841 | LINE 509 |     message: `Importación finalizada. Éxito: ${successCount}, Errores: ${errorCount}`,
LINE 1842 | LINE 510 |     position: 'center',
LINE 1843 | LINE 511 |     timeout: 5000,
LINE 1844 | LINE 512 |   })
LINE 1845 | LINE 513 | 
LINE 1846 | LINE 514 |   loadRows()
LINE 1847 | LINE 515 | }
LINE 1848 | LINE 516 | const abrirVariantes = (row) => {
LINE 1849 | LINE 517 |   productoVariantes.value = row
LINE 1850 | LINE 518 |   showVariantesDialog.value = true
LINE 1851 | LINE 519 | }
LINE 1852 | LINE 520 | onMounted(() => {
LINE 1853 | LINE 521 |   loadcategorias()
LINE 1854 | LINE 522 |   loadestados()
LINE 1855 | LINE 523 |   loadmedidas()
LINE 1856 | LINE 524 |   loadsubcategorias()
LINE 1857 | LINE 525 |   loadunidades()
LINE 1858 | LINE 526 |   loadRows()
LINE 1859 | LINE 527 |   if (getTipoFactura(true)) {
LINE 1860 | LINE 528 |     ListaProductoSin()
LINE 1861 | LINE 529 |     ListaUnidadSin()
LINE 1862 | LINE 530 |   }
LINE 1863 | LINE 531 | })
LINE 1864 | LINE 532 | </script>
LINE 1865 | ```
```

==============================================================
FILE: output/deepseek_project_context.txt
==============================================================
```txt
LINE    1 | ==============================================================
LINE    2 | REPORTED PROBLEM OR GOAL / PROBLEMA REPORTADO U OBJETIVO
LINE    3 | ==============================================================
LINE    4 | generar el codigo en python para hacer el cambio el codigo se creara en la raiz del archivo 
LINE    5 | agregar las columnas a la tabla de producto medida, estadoProducto, unidad, caracteristica 
LINE    6 | la api listaProducto devuelve estos datos 
LINE    7 | [
LINE    8 |     {
LINE    9 |         "id": "4004",
LINE   10 |         "nombre": "BOTIN TREKIN MOTOQUERO PIL",
LINE   11 |         "codigo": "IND-BOT-T-M-P",
LINE   12 |         "descripcion": "BOTIN TREKIN MOTOQUERO PIL",
LINE   13 |         "codigobarras": "",
LINE   14 |         "fecha": "2026-09-03",
LINE   15 |         "imagen": "",
LINE   16 |         "idcategoria": "0",
LINE   17 |         "categoria": null,
LINE   18 |         "subcategoria": "",
LINE   19 |         "idmedida": "234",
LINE   20 |         "medida": "general",
LINE   21 |         "idestadoproducto": "275",
LINE   22 |         "estadoproducto": "Ejecuci\u00f3n",
LINE   23 |         "idunidad": "250",
LINE   24 |         "unidad": "Rollo",
LINE   25 |         "caracteristica": ""{
LINE   26 |         "id": "4004",
LINE   27 |         "nombre": "BOTIN TREKIN MOTOQUERO PIL",
LINE   28 |         "codigo": "IND-BOT-T-M-P",
LINE   29 |         "descripcion": "BOTIN TREKIN MOTOQUERO PIL",
LINE   30 |         "codigobarras": "",
LINE   31 |         "imagen": "",
LINE   32 |         "idcategoria": "0",
LINE   33 |         "categoria": null,
LINE   34 |         "subcategoria": "",
LINE   35 |         "idmedida": "234",
LINE   36 |         "medida": "general",
LINE   37 |         "idestadoproducto": "275",
LINE   38 |         "estadoproducto": "Ejecuci\u00f3n",
LINE   39 |         "idunidad": "250",
LINE   40 |         "unidad": "Rollo",
LINE   41 |         "caracteristica": ""
LINE   42 |     },...
LINE   43 | ]
LINE   44 | 
LINE   45 | 
LINE   46 | ==============================================================
LINE   47 | SELECTED ANALYSIS PROFILE / PERFIL DE ANÁLISIS: 🐞 Detect errors
LINE   48 | ==============================================================
LINE   49 | • Objetivo: Identificar errores de sintaxis, bugs lógicos, excepciones no controladas, condiciones de carrera y fallos de tipo en el código.
LINE   50 | • Enfoque: Detección exhaustiva de bugs, casos límite (edge cases), seguridad de nulos/undefined, control de flujo y manejo robusto de excepciones.
LINE   51 | • Prioridades: 1. Crashes y errores que detienen la ejecución. 2. Fallos silenciosos y corrupción de estado. 3. Manejo deficiente de excepciones. 4. Regresiones potenciales.
LINE   52 | • Resultado esperado: Localización exacta de cada error (archivo y línea), causa raíz técnica, código corregido listo para copiar/pegar y caso de prueba de verificación.
LINE   53 | 
LINE   54 | ⚠️ REGLA DE CONCRECIÓN TÉCNICA: El análisis debe ser CONCRETO, TÉCNICO y ORIENTADO A LA ACCIÓN. Concéntrate exclusivamente en fallos reproducibles y errores verificables. Omite comentarios estilísticos o divagaciones teóricas que no resuelvan un error.
LINE   55 | 
LINE   56 | ==============================================================
LINE   57 | PROJECT CONTEXT / CONTEXTO DEL PROYECTO
LINE   58 | ==============================================================
LINE   59 | • Nombre del Proyecto: cm-oficial
LINE   60 | • Ruta Base: /media/richard/Nuevo vol/quasar/dess/comercial/cm-oficial
LINE   61 | • Fecha de Generación: 2026-09-28 15:15:32
LINE   62 | 
LINE   63 | --------------------------------------------------------------
LINE   64 | PROJECT SUMMARY
LINE   65 | --------------------------------------------------------------
LINE   66 | Selected files: 4
LINE   67 | File extensions:
LINE   68 |   .vue: 3
LINE   69 |   .js: 1
LINE   70 | 
LINE   71 | Total lines:
LINE   72 | 1,683
LINE   73 | 
LINE   74 | --------------------------------------------------------------
LINE   75 | DEPENDENCIES AND REFERENCES
LINE   76 | --------------------------------------------------------------
LINE   77 | • src/components/producto/creacion/productoForm.vue:
LINE   78 |   - import { ref, watch, computed, onUnmounted } from 'vue'
LINE   79 |   - import { TipoFactura } from 'src/composables/FuncionesGenerales'
LINE   80 |   - import imageCompression from 'browser-image-compression'
LINE   81 |   - import { useQuasar } from 'quasar'
LINE   82 | • src/components/producto/creacion/productoTable.vue:
LINE   83 |   - import { ref, computed, watch } from 'vue'
LINE   84 |   - import { imagen } from 'src/boot/url'
LINE   85 |   - import { getTipoFactura } from 'src/composables/FuncionesG'
LINE   86 |   - import BaseFilterableTable from 'src/components/componentesGenerales/filtradoTabla/BaseFilterableTable.vue'
LINE   87 |   - import { useQuasar } from 'quasar'
LINE   88 |   - import { cambiarFormatoFecha } from 'src/composables/FuncionesG'
LINE   89 | • src/composables/useReporteInventarioExterior.js:
LINE   90 |   - import { ref } from 'vue'
LINE   91 |   - import { date } from 'quasar'
LINE   92 |   - import { idusuario_md5, idempresa_md5 } from 'src/composables/FuncionesGenerales'
LINE   93 |   - import { api } from 'src/boot/axios'
LINE   94 |   - import axios from 'axios'
LINE   95 |   - import 'jspdf-autotable'
LINE   96 | • src/pages/producto/CproductoPage.vue:
LINE   97 |   - import { ref, onMounted } from 'vue'
LINE   98 |   - import { api } from 'boot/axios'
LINE   99 |   - import { idempresa_md5, validarUsuario } from 'src/composables/FuncionesGenerales'
LINE  100 |   - import { useQuasar } from 'quasar'
LINE  101 |   - import { objectToFormData } from 'src/composables/FuncionesGenerales'
LINE  102 |   - import ProductoForm from 'src/components/producto/creacion/productoForm.vue'
LINE  103 |   - import ProductoTabla from 'src/components/producto/creacion/productoTable.vue'
LINE  104 |   - import { imagen } from 'src/boot/url'
LINE  105 |   - import { getTipoFactura, getToken } from 'src/composables/FuncionesG'
LINE  106 |   - import seriePage from 'src/modules/serie/page/seriePage.vue'
LINE  107 |   - import ProductoVarianteDialog from 'src/components/producto/variantes/productoVarianteDialog.vue'
LINE  108 | 
LINE  109 | --------------------------------------------------------------
LINE  110 | INSTRUCCIONES OBLIGATORIAS PARA DEEPSEEK (DETECT ERRORS)
LINE  111 | --------------------------------------------------------------
LINE  112 | El análisis debe ser CONCRETO, TÉCNICO y ORIENTADO A LA ACCIÓN. Concéntrate exclusivamente en fallos reproducibles y errores verificables. Omite comentarios estilísticos o divagaciones teóricas que no resuelvan un error.
LINE  113 | 
LINE  114 | Tu respuesta DEBE seguir exactamente la siguiente estructura Markdown adaptada al perfil:
LINE  115 | 
LINE  116 | # DIAGNOSIS
LINE  117 | ## Detected Bugs
LINE  118 | [Lista técnica de los bugs encontrados con su causa raíz exacta]
LINE  119 | 
LINE  120 | # FILES TO MODIFY
LINE  121 | ## 1. [ruta/relativa/archivo.ext]
LINE  122 | Approximate line: [número]
LINE  123 | ### Bug Description
LINE  124 | [Explicación concisa del error]
LINE  125 | ### Current Code
LINE  126 | ```
LINE  127 | [código con error]
LINE  128 | ```
LINE  129 | ### Bugfix Code
LINE  130 | ```
LINE  131 | [código corregido listo para sustituir]
LINE  132 | ```
LINE  133 | 
LINE  134 | # VERIFICATION & EDGE CASES
LINE  135 | [Prueba o caso límite para verificar que el bug fue resuelto]
LINE  136 | 
LINE  137 | REGLA OBLIGATORIA: No respondas con JSON. Responde con el formato estructurado exacto indicado arriba.
LINE  138 | 
LINE  139 | Estructura de Directorios:
LINE  140 | cm-oficial/
LINE  141 | └── src/
LINE  142 |     ├── components/
LINE  143 |     │   └── producto/
LINE  144 |     │       └── creacion/
LINE  145 |     │           ├── productoForm.vue
LINE  146 |     │           └── productoTable.vue
LINE  147 |     ├── composables/
LINE  148 |     │   └── useReporteInventarioExterior.js
LINE  149 |     └── pages/
LINE  150 |         └── producto/
LINE  151 |             └── CproductoPage.vue
LINE  152 | 
LINE  153 | 
LINE  154 | ==============================================================
LINE  155 | ATTACHMENTS / ARCHIVOS Y CÓDIGO FUENTE
LINE  156 | ==============================================================
LINE  157 | 
LINE  158 | ==============================================================
LINE  159 | FILE: src/components/producto/creacion/productoForm.vue
LINE  160 | ==============================================================
LINE  161 | LINE   1 | <template>
LINE  162 | LINE   2 |   <q-form @submit.prevent="handleSubmit">
LINE  163 | LINE   3 |     <!-- Información Básica -->
LINE  164 | LINE   4 |     <q-card-section>
LINE  165 | LINE   5 |       <div class="text-subtitle1 text-weight-medium q-mb-md">Información Básica</div>
LINE  166 | LINE   6 |       <q-separator class="q-mb-md" />
LINE  167 | LINE   7 |       
LINE  168 | LINE   8 |       <div class="row q-col-gutter-md">
LINE  169 | LINE   9 |         <div class="col-12 col-md-4">
LINE  170 | LINE  10 |           <q-input
LINE  171 | LINE  11 |             v-model="localData.codigo"
LINE  172 | LINE  12 |             label="Código de Producto *"
LINE  173 | LINE  13 |             dense
LINE  174 | LINE  14 |             outlined
LINE  175 | LINE  15 |             hint="Código único del producto"
LINE  176 | LINE  16 |           />
LINE  177 | LINE  17 |         </div>
LINE  178 | LINE  18 |         
LINE  179 | LINE  19 |         <div class="col-12 col-md-4">
LINE  180 | LINE  20 |           <q-input
LINE  181 | LINE  21 |             v-model="localData.nombre"
LINE  182 | LINE  22 |             label="Nombre del Producto *"
LINE  183 | LINE  23 |             dense
LINE  184 | LINE  24 |             outlined
LINE  185 | LINE  25 |             hint="Nombre comercial"
LINE  186 | LINE  26 |           />
LINE  187 | LINE  27 |         </div>
LINE  188 | LINE  28 |         
LINE  189 | LINE  29 |         <div class="col-12 col-md-4">
LINE  190 | LINE  30 |           <q-input
LINE  191 | LINE  31 |             v-model="localData.descripcion"
LINE  192 | LINE  32 |             label="Descripción *"
LINE  193 | LINE  33 |             dense
LINE  194 | LINE  34 |             outlined
LINE  195 | LINE  35 |             hint="Descripción breve"
LINE  196 | LINE  36 |           />
LINE  197 | LINE  37 |         </div>
LINE  198 | LINE  38 |         
LINE  199 | LINE  39 |         <div class="col-12 col-md-4">
LINE  200 | LINE  40 |           <q-input
LINE  201 | LINE  41 |             v-model="localData.codigobarras"
LINE  202 | LINE  42 |             label="Código de Barras"
LINE  203 | LINE  43 |             dense
LINE  204 | LINE  44 |             outlined
LINE  205 | LINE  45 |             hint="Opcional"
LINE  206 | LINE  46 |           />
LINE  207 | LINE  47 |         </div>
LINE  208 | LINE  48 |       </div>
LINE  209 | LINE  49 |     </q-card-section>
LINE  210 | LINE  50 | 
LINE  211 | LINE  51 |     <!-- Categorización -->
LINE  212 | LINE  52 |     <q-card-section>
LINE  213 | LINE  53 |       <div class="text-subtitle1 text-weight-medium q-mb-md">Categorización</div>
LINE  214 | LINE  54 |       <q-separator class="q-mb-md" />
LINE  215 | LINE  55 |       
LINE  216 | LINE  56 |       <div class="row q-col-gutter-md">
LINE  217 | LINE  57 |         <div class="col-12 col-md-4">
LINE  218 | LINE  58 |           <q-select
LINE  219 | LINE  59 |             v-model="localData.categoria"
LINE  220 | LINE  60 |             :options="categorias"
LINE  221 | LINE  61 |             label="Categoría *"
LINE  222 | LINE  62 |             dense
LINE  223 | LINE  63 |             outlined
LINE  224 | LINE  64 |             emit-value
LINE  225 | LINE  65 |             map-options
LINE  226 | LINE  66 |             hint="Seleccione la categoría principal"
LINE  227 | LINE  67 |             @update:model-value="
LINE  228 | LINE  68 |               (val) => {
LINE  229 | LINE  69 |                 localData.subcategoria = null
LINE  230 | LINE  70 |                 emit('categoria-changed', val)
LINE  231 | LINE  71 |               }
LINE  232 | LINE  72 |             "
LINE  233 | LINE  73 |           />
LINE  234 | LINE  74 |         </div>
LINE  235 | LINE  75 |         
LINE  236 | LINE  76 |         <div class="col-12 col-md-4" v-if="subcategorias.length > 0">
LINE  237 | LINE  77 |           <q-select
LINE  238 | LINE  78 |             v-model="localData.subcategoria"
LINE  239 | LINE  79 |             :options="subcategorias"
LINE  240 | LINE  80 |             label="Sub Categoría *"
LINE  241 | LINE  81 |             dense
LINE  242 | LINE  82 |             outlined
LINE  243 | LINE  83 |             emit-value
LINE  244 | LINE  84 |             map-options
LINE  245 | LINE  85 |             hint="Seleccione la subcategoría"
LINE  246 | LINE  86 |           />
LINE  247 | LINE  87 |         </div>
LINE  248 | LINE  88 |         
LINE  249 | LINE  89 |         <div class="col-12 col-md-4">
LINE  250 | LINE  90 |           <q-select
LINE  251 | LINE  91 |             v-model="localData.estadoproductos"
LINE  252 | LINE  92 |             :options="estados"
LINE  253 | LINE  93 |             label="Estado del Producto *"
LINE  254 | LINE  94 |             dense
LINE  255 | LINE  95 |             outlined
LINE  256 | LINE  96 |             emit-value
LINE  257 | LINE  97 |             map-options
LINE  258 | LINE  98 |             hint="Estado actual"
LINE  259 | LINE  99 |           />
LINE  260 | LINE 100 |         </div>
LINE  261 | LINE 101 |       </div>
LINE  262 | LINE 102 |     </q-card-section>
LINE  263 | LINE 103 | 
LINE  264 | LINE 104 |     <!-- Características -->
LINE  265 | LINE 105 |     <q-card-section>
LINE  266 | LINE 106 |       <div class="text-subtitle1 text-weight-medium q-mb-md">Características</div>
LINE  267 | LINE 107 |       <q-separator class="q-mb-md" />
LINE  268 | LINE 108 |       
LINE  269 | LINE 109 |       <div class="row q-col-gutter-md">
LINE  270 | LINE 110 |         <div class="col-12 col-md-4">
LINE  271 | LINE 111 |           <q-select
LINE  272 | LINE 112 |             v-model="localData.unidad"
LINE  273 | LINE 113 |             :options="unidades"
LINE  274 | LINE 114 |             label="Unidad de Medida *"
LINE  275 | LINE 115 |             dense
LINE  276 | LINE 116 |             outlined
LINE  277 | LINE 117 |             emit-value
LINE  278 | LINE 118 |             map-options
LINE  279 | LINE 119 |             hint="Ej: Kilo, Unidad, Litro"
LINE  280 | LINE 120 |           />
LINE  281 | LINE 121 |         </div>
LINE  282 | LINE 122 |         
LINE  283 | LINE 123 |         <div class="col-12 col-md-4">
LINE  284 | LINE 124 |           <q-select
LINE  285 | LINE 125 |             v-model="localData.medida"
LINE  286 | LINE 126 |             :options="medidas"
LINE  287 | LINE 127 |             label="Característica *"
LINE  288 | LINE 128 |             dense
LINE  289 | LINE 129 |             outlined
LINE  290 | LINE 130 |             emit-value
LINE  291 | LINE 131 |             map-options
LINE  292 | LINE 132 |           />
LINE  293 | LINE 133 |         </div>
LINE  294 | LINE 134 |         
LINE  295 | LINE 135 |         <div class="col-12 col-md-4">
LINE  296 | LINE 136 |           <q-input
LINE  297 | LINE 137 |             v-model="localData.caracteristica"
LINE  298 | LINE 138 |             label="Otras Características"
LINE  299 | LINE 139 |             dense
LINE  300 | LINE 140 |             outlined
LINE  301 | LINE 141 |             hint="Opcional"
LINE  302 | LINE 142 |           />
LINE  303 | LINE 143 |         </div>
LINE  304 | LINE 144 |       </div>
LINE  305 | LINE 145 |     </q-card-section>
LINE  306 | LINE 146 | 
LINE  307 | LINE 147 |     <!-- Información SIN (Facturación) -->
LINE  308 | LINE 148 |     <q-card-section v-if="tipoFactura">
LINE  309 | LINE 149 |       <div class="text-subtitle1 text-weight-medium q-mb-md">Información SIN (Facturación)</div>
LINE  310 | LINE 150 |       <q-separator class="q-mb-md" />
LINE  311 | LINE 151 |       
LINE  312 | LINE 152 |       <div class="row q-col-gutter-md">
LINE  313 | LINE 153 |         <div class="col-12 col-md-6">
LINE  314 | LINE 154 |           <q-select
LINE  315 | LINE 155 |             v-model="localData.codigosin"
LINE  316 | LINE 156 |             :options="FilterProductoSIN"
LINE  317 | LINE 157 |             label="Producto SIN *"
LINE  318 | LINE 158 |             dense
LINE  319 | LINE 159 |             outlined
LINE  320 | LINE 160 |             emit-value
LINE  321 | LINE 161 |             map-options
LINE  322 | LINE 162 |             use-input
LINE  323 | LINE 163 |             fill-input
LINE  324 | LINE 164 |             hide-selected
LINE  325 | LINE 165 |             input-debounce="0"
LINE  326 | LINE 166 |             @filter="filterFn"
LINE  327 | LINE 167 |             hint="Busque el código SIN del producto"
LINE  328 | LINE 168 |           />
LINE  329 | LINE 169 |         </div>
LINE  330 | LINE 170 |         
LINE  331 | LINE 171 |         <div class="col-12 col-md-3">
LINE  332 | LINE 172 |           <q-select
LINE  333 | LINE 173 |             v-model="localData.unidadsin"
LINE  334 | LINE 174 |             :options="FilterUnidadSIN"
LINE  335 | LINE 175 |             label="Unidad SIN *"
LINE  336 | LINE 176 |             dense
LINE  337 | LINE 177 |             outlined
LINE  338 | LINE 178 |             emit-value
LINE  339 | LINE 179 |             map-options
LINE  340 | LINE 180 |             use-input
LINE  341 | LINE 181 |             fill-input
LINE  342 | LINE 182 |             hide-selected
LINE  343 | LINE 183 |             input-debounce="0"
LINE  344 | LINE 184 |             @filter="filterUnidadFn"
LINE  345 | LINE 185 |             hint="Unidad según SIN"
LINE  346 | LINE 186 |           />
LINE  347 | LINE 187 |         </div>
LINE  348 | LINE 188 |         
LINE  349 | LINE 189 |         <div class="col-12 col-md-3">
LINE  350 | LINE 190 |           <q-input
LINE  351 | LINE 191 |             v-model="localData.codigoNandina"
LINE  352 | LINE 192 |             label="Código Nandina"
LINE  353 | LINE 193 |             dense
LINE  354 | LINE 194 |             outlined
LINE  355 | LINE 195 |             hint="Opcional"
LINE  356 | LINE 196 |           />
LINE  357 | LINE 197 |         </div>
LINE  358 | LINE 198 |       </div>
LINE  359 | LINE 199 |     </q-card-section>
LINE  360 | LINE 200 | 
LINE  361 | LINE 201 |     <!-- Imagen del Producto -->
LINE  362 | LINE 202 |     <q-card-section>
LINE  363 | LINE 203 |       <div class="text-subtitle1 text-weight-medium q-mb-md">Imagen del Producto</div>
LINE  364 | LINE 204 |       <q-separator class="q-mb-md" />
LINE  365 | LINE 205 |       
LINE  366 | LINE 206 |       <div class="row q-col-gutter-md">
LINE  367 | LINE 207 |         <div class="col-12" :class="imagePreview ? 'col-md-8' : ''">
LINE  368 | LINE 208 |           <q-file
LINE  369 | LINE 209 |             v-model="localData.imagen"
LINE  370 | LINE 210 |             label="Seleccionar imagen"
LINE  371 | LINE 211 |             outlined
LINE  372 | LINE 212 |             dense
LINE  373 | LINE 213 |             accept="image/*"
LINE  374 | LINE 214 |             hint="Formatos admitidos: JPG, PNG. La imagen se optimizará automáticamente."
LINE  375 | LINE 215 |             counter
LINE  376 | LINE 216 |             @update:model-value="onImageSelected"
LINE  377 | LINE 217 |             :loading="isCompressing"
LINE  378 | LINE 218 |             :disable="isCompressing"
LINE  379 | LINE 219 |           >
LINE  380 | LINE 220 |             <template v-slot:prepend>
LINE  381 | LINE 221 |               <q-icon name="attach_file" />
LINE  382 | LINE 222 |             </template>
LINE  383 | LINE 223 |           </q-file>
LINE  384 | LINE 224 |         </div>
LINE  385 | LINE 225 |         
LINE  386 | LINE 226 |         <div class="col-12 col-md-4" v-if="imagePreview">
LINE  387 | LINE 227 |           <div class="text-caption text-grey-7 q-mb-xs">
LINE  388 | LINE 228 |             {{ typeof localData.imagen === 'string' ? 'Imagen actual' : 'Vista previa' }}
LINE  389 | LINE 229 |           </div>
LINE  390 | LINE 230 |           <q-card flat bordered class="q-pa-sm">
LINE  391 | LINE 231 |             <q-img
LINE  392 | LINE 232 |               :src="imagePreview"
LINE  393 | LINE 233 |               style="max-height: 120px; border-radius: 4px"
LINE  394 | LINE 234 |               fit="contain"
LINE  395 | LINE 235 |               class="bg-grey-2"
LINE  396 | LINE 236 |             >
LINE  397 | LINE 237 |               <template v-slot:error>
LINE  398 | LINE 238 |                 <div class="absolute-full flex flex-center bg-grey-3 text-grey-7">
LINE  399 | LINE 239 |                   <div class="text-center">
LINE  400 | LINE 240 |                     <q-icon name="broken_image" size="md" />
LINE  401 | LINE 241 |                     <div class="text-caption">Error al cargar imagen</div>
LINE  402 | LINE 242 |                   </div>
LINE  403 | LINE 243 |                 </div>
LINE  404 | LINE 244 |               </template>
LINE  405 | LINE 245 |             </q-img>
LINE  406 | LINE 246 |             <div class="text-caption text-grey-7 q-mt-xs text-center" v-if="typeof localData.imagen !== 'string'">
LINE  407 | LINE 247 |               {{ localData.imagen?.name }}
LINE  408 | LINE 248 |             </div>
LINE  409 | LINE 249 |           </q-card>
LINE  410 | LINE 250 |         </div>
LINE  411 | LINE 251 |       </div>
LINE  412 | LINE 252 |     </q-card-section>
LINE  413 | LINE 253 | 
LINE  414 | LINE 254 |     <!-- Botones de Acción -->
LINE  415 | LINE 255 |     <q-separator />
LINE  416 | LINE 256 |     
LINE  417 | LINE 257 |     <q-card-actions align="right" class="q-pa-md">
LINE  418 | LINE 258 |       <q-btn
LINE  419 | LINE 259 |         label="Cancelar"
LINE  420 | LINE 260 |         flat
LINE  421 | LINE 261 |         color="grey-7"
LINE  422 | LINE 262 |         @click="$emit('cancel')"
LINE  423 | LINE 263 |         class="q-mr-sm"
LINE  424 | LINE 264 |       />
LINE  425 | LINE 265 |       <q-btn
LINE  426 | LINE 266 |         label="Guardar"
LINE  427 | LINE 267 |         type="submit"
LINE  428 | LINE 268 |         color="primary"
LINE  429 | LINE 269 |         unelevated
LINE  430 | LINE 270 |         :disable="isCompressing"
LINE  431 | LINE 271 |       />
LINE  432 | LINE 272 |     </q-card-actions>
LINE  433 | LINE 273 |   </q-form>
LINE  434 | LINE 274 | </template>
LINE  435 | LINE 275 | 
LINE  436 | LINE 276 | <script setup>
LINE  437 | LINE 277 | import { ref, watch, computed, onUnmounted } from 'vue'
LINE  438 | LINE 278 | import { TipoFactura } from 'src/composables/FuncionesGenerales'
LINE  439 | LINE 279 | import imageCompression from 'browser-image-compression'
LINE  440 | LINE 280 | import { useQuasar } from 'quasar'
LINE  441 | LINE 281 | 
LINE  442 | LINE 282 | const $q = useQuasar()
LINE  443 | LINE 283 | const tipoFactura = TipoFactura()
LINE  444 | LINE 284 | console.log('Tipo de factura en productoForm.vue:', tipoFactura)
LINE  445 | LINE 285 | 
LINE  446 | LINE 286 | let objectUrl = null
LINE  447 | LINE 287 | const isCompressing = ref(false)
LINE  448 | LINE 288 | let isProgrammaticUpdate = false // Flag to prevent infinite loop
LINE  449 | LINE 289 | 
LINE  450 | LINE 290 | const props = defineProps({
LINE  451 | LINE 291 |   isEditing: Boolean,
LINE  452 | LINE 292 |   modelValue: Object,
LINE  453 | LINE 293 |   categorias: {
LINE  454 | LINE 294 |     type: Array,
LINE  455 | LINE 295 |     default: () => [],
LINE  456 | LINE 296 |   },
LINE  457 | LINE 297 |   estados: {
LINE  458 | LINE 298 |     type: Array,
LINE  459 | LINE 299 |     default: () => [],
LINE  460 | LINE 300 |   },
LINE  461 | LINE 301 |   subcategorias: {
LINE  462 | LINE 302 |     type: Array,
LINE  463 | LINE 303 |     default: () => [],
LINE  464 | LINE 304 |   },
LINE  465 | LINE 305 |   unidades: {
LINE  466 | LINE 306 |     type: Array,
LINE  467 | LINE 307 |     default: () => [],
LINE  468 | LINE 308 |   },
LINE  469 | LINE 309 |   medidas: {
LINE  470 | LINE 310 |     type: Array,
LINE  471 | LINE 311 |     default: () => [],
LINE  472 | LINE 312 |   },
LINE  473 | LINE 313 |   productoSIN: {
LINE  474 | LINE 314 |     type: Array,
LINE  475 | LINE 315 |     default: () => [],
LINE  476 | LINE 316 |   },
LINE  477 | LINE 317 |   unidadSIN: {
LINE  478 | LINE 318 |     type: Array,
LINE  479 | LINE 319 |     default: () => [],
LINE  480 | LINE 320 |   },
LINE  481 | LINE 321 | })
LINE  482 | LINE 322 | 
LINE  483 | LINE 323 | const emit = defineEmits(['submit', 'cancel'])
LINE  484 | LINE 324 | const FilterProductoSIN = ref([...props.productoSIN])
LINE  485 | LINE 325 | const FilterUnidadSIN = ref([...props.unidadSIN])
LINE  486 | LINE 326 | const localData = ref({ ...props.modelValue })
LINE  487 | LINE 327 | 
LINE  488 | LINE 328 | // Computed property for image preview
LINE  489 | LINE 329 | const imagePreview = computed(() => {
LINE  490 | LINE 330 |   if (!localData.value.imagen) return null
LINE  491 | LINE 331 |   
LINE  492 | LINE 332 |   // If it's a File object (newly selected), create object URL
LINE  493 | LINE 333 |   if (localData.value.imagen instanceof File) {
LINE  494 | LINE 334 |     // Clean up old object URL if exists
LINE  495 | LINE 335 |     if (objectUrl) {
LINE  496 | LINE 336 |       URL.revokeObjectURL(objectUrl)
LINE  497 | LINE 337 |     }
LINE  498 | LINE 338 |     objectUrl = URL.createObjectURL(localData.value.imagen)
LINE  499 | LINE 339 |     return objectUrl
LINE  500 | LINE 340 |   }
LINE  501 | LINE 341 |   
LINE  502 | LINE 342 |   // If it's a string (existing image from database), use vista URL
LINE  503 | LINE 343 |   if (typeof localData.value.imagen === 'string') {
LINE  504 | LINE 344 |     return localData.value.vista
LINE  505 | LINE 345 |   }
LINE  506 | LINE 346 |   
LINE  507 | LINE 347 |   return null
LINE  508 | LINE 348 | })
LINE  509 | LINE 349 | 
LINE  510 | LINE 350 | // Handler for image selection and compression
LINE  511 | LINE 351 | const onImageSelected = async (file) => {
LINE  512 | LINE 352 |   // Prevent infinite loop if we are just updating the model programmatically
LINE  513 | LINE 353 |   if (isProgrammaticUpdate) {
LINE  514 | LINE 354 |     isProgrammaticUpdate = false
LINE  515 | LINE 355 |     return
LINE  516 | LINE 356 |   }
LINE  517 | LINE 357 | 
LINE  518 | LINE 358 |   // Prevent infinite loop if the file is already a webp or undefined
LINE  519 | LINE 359 |   if (!file) {
LINE  520 | LINE 360 |     if (objectUrl) {
LINE  521 | LINE 361 |       URL.revokeObjectURL(objectUrl)
LINE  522 | LINE 362 |       objectUrl = null
LINE  523 | LINE 363 |     }
LINE  524 | LINE 364 |     return
LINE  525 | LINE 365 |   }
LINE  526 | LINE 366 |   
LINE  527 | LINE 367 |   // If it's a string (existing image)
LINE  528 | LINE 368 |   if (!(file instanceof File)) {
LINE  529 | LINE 369 |     return
LINE  530 | LINE 370 |   }
LINE  531 | LINE 371 | 
LINE  532 | LINE 372 |   try {
LINE  533 | LINE 373 |     isCompressing.value = true
LINE  534 | LINE 374 |     
LINE  535 | LINE 375 |     // We use a simple notification without trying to store its ID and update it later
LINE  536 | LINE 376 |     // because doing so causes "trying to update a grouped one which is forbidden" error in Quasar.
LINE  537 | LINE 377 |     $q.notify({
LINE  538 | LINE 378 |       message: 'Optimizando imagen...',
LINE  539 | LINE 379 |       color: 'info',
LINE  540 | LINE 380 |       textColor: 'white',
LINE  541 | LINE 381 |       icon: 'cloud_upload',
LINE  542 | LINE 382 |       timeout: 1500, // Short timeout, the real indicator is the loading spinner on the input
LINE  543 | LINE 383 |     })
LINE  544 | LINE 384 | 
LINE  545 | LINE 385 |     const options = {
LINE  546 | LINE 386 |       maxSizeMB: 1, // Compress to less than 1MB
LINE  547 | LINE 387 |       maxWidthOrHeight: 1920, // Max resolution 1920px
LINE  548 | LINE 388 |       useWebWorker: true,
LINE  549 | LINE 389 |       fileType: 'image/jpeg', // Convert to JPEG format for backend compatibility (JPG/PNG only)
LINE  550 | LINE 390 |       initialQuality: 0.9, // Maintain high visual quality
LINE  551 | LINE 391 |     }
LINE  552 | LINE 392 | 
LINE  553 | LINE 393 |     // Attempt to compress the image
LINE  554 | LINE 394 |     const compressedBlob = await imageCompression(file, options)
LINE  555 | LINE 395 |     
LINE  556 | LINE 396 |     // Create a new File from the Blob to keep the original name (but with .jpg extension)
LINE  557 | LINE 397 |     const newFileName = file.name.replace(/\.[^/.]+$/, "") + '.jpg'
LINE  558 | LINE 398 |     const compressedFile = new File([compressedBlob], newFileName, {
LINE  559 | LINE 399 |       type: 'image/jpeg',
LINE  560 | LINE 400 |       lastModified: Date.now()
LINE  561 | LINE 401 |     })
LINE  562 | LINE 402 | 
LINE  563 | LINE 403 |     console.log(`Original size: ${(file.size / 1024 / 1024).toFixed(2)} MB`)
LINE  564 | LINE 404 |     console.log(`Compressed size: ${(compressedFile.size / 1024 / 1024).toFixed(2)} MB`)
LINE  565 | LINE 405 | 
LINE  566 | LINE 406 |     // This flag prevents the @update:model-value from triggering this function again and causing an infinite loop
LINE  567 | LINE 407 |     isProgrammaticUpdate = true
LINE  568 | LINE 408 |     
LINE  569 | LINE 409 |     // Update the v-model with the compressed file
LINE  570 | LINE 410 |     // Note: This triggers the `imagePreview` computed properly
LINE  571 | LINE 411 |     localData.value.imagen = compressedFile
LINE  572 | LINE 412 | 
LINE  573 | LINE 413 |     // Show a success notification
LINE  574 | LINE 414 |     $q.notify({
LINE  575 | LINE 415 |       message: 'Imagen optimizada con éxito',
LINE  576 | LINE 416 |       color: 'positive',
LINE  577 | LINE 417 |       icon: 'check_circle',
LINE  578 | LINE 418 |       timeout: 2500,
LINE  579 | LINE 419 |     })
LINE  580 | LINE 420 | 
LINE  581 | LINE 421 |   } catch (error) {
LINE  582 | LINE 422 |     console.error('Error compressing image:', error)
LINE  583 | LINE 423 |     $q.notify({
LINE  584 | LINE 424 |       message: 'Hubo un error al optimizar la imagen',
LINE  585 | LINE 425 |       color: 'negative',
LINE  586 | LINE 426 |       icon: 'warning',
LINE  587 | LINE 427 |     })
LINE  588 | LINE 428 |     
LINE  589 | LINE 429 |     isProgrammaticUpdate = true
LINE  590 | LINE 430 |     // If compression fails, we fallback to the original file
LINE  591 | LINE 431 |     // The imagePreview will still handle the display
LINE  592 | LINE 432 |     localData.value.imagen = file
LINE  593 | LINE 433 |   } finally {
LINE  594 | LINE 434 |     isCompressing.value = false
LINE  595 | LINE 435 |   }
LINE  596 | LINE 436 | }
LINE  597 | LINE 437 | 
LINE  598 | LINE 438 | // Cleanup object URL on unmount
LINE  599 | LINE 439 | onUnmounted(() => {
LINE  600 | LINE 440 |   if (objectUrl) {
LINE  601 | LINE 441 |     URL.revokeObjectURL(objectUrl)
LINE  602 | LINE 442 |   }
LINE  603 | LINE 443 | })
LINE  604 | LINE 444 | function filterFn(val, update) {
LINE  605 | LINE 445 |   console.log(val)
LINE  606 | LINE 446 |   if (val === '') {
LINE  607 | LINE 447 |     update(() => {
LINE  608 | LINE 448 |       FilterProductoSIN.value = [...props.productoSIN]
LINE  609 | LINE 449 |     })
LINE  610 | LINE 450 |     return
LINE  611 | LINE 451 |   }
LINE  612 | LINE 452 | 
LINE  613 | LINE 453 |   update(() => {
LINE  614 | LINE 454 |     const needle = val.toLowerCase()
LINE  615 | LINE 455 |     FilterProductoSIN.value = props.productoSIN.filter((v) =>
LINE  616 | LINE 456 |       v.label.toLowerCase().includes(needle),
LINE  617 | LINE 457 |     )
LINE  618 | LINE 458 |   })
LINE  619 | LINE 459 | }
LINE  620 | LINE 460 | function filterUnidadFn(val, update) {
LINE  621 | LINE 461 |   console.log(val)
LINE  622 | LINE 462 |   if (val === '') {
LINE  623 | LINE 463 |     update(() => {
LINE  624 | LINE 464 |       FilterUnidadSIN.value = [...props.unidadSIN]
LINE  625 | LINE 465 |     })
LINE  626 | LINE 466 |     return
LINE  627 | LINE 467 |   }
LINE  628 | LINE 468 |   update(() => {
LINE  629 | LINE 469 |     const needle = val.toLowerCase()
LINE  630 | LINE 470 |     FilterUnidadSIN.value = props.unidadSIN.filter((v) => v.label.toLowerCase().includes(needle))
LINE  631 | LINE 471 |   })
LINE  632 | LINE 472 | }
LINE  633 | LINE 473 | console.log(props.modelValue)
LINE  634 | LINE 474 | watch(
LINE  635 | LINE 475 |   () => props.modelValue,
LINE  636 | LINE 476 |   (val) => {
LINE  637 | LINE 477 |     localData.value = { ...val }
LINE  638 | LINE 478 |   },
LINE  639 | LINE 479 |   { deep: true },
LINE  640 | LINE 480 | )
LINE  641 | LINE 481 | 
LINE  642 | LINE 482 | const handleSubmit = () => {
LINE  643 | LINE 483 |   console.log('=== FORM SUBMIT DEBUG ===')
LINE  644 | LINE 484 |   console.log('localData.categoria:', localData.value.categoria)
LINE  645 | LINE 485 |   console.log('localData.subcategoria:', localData.value.subcategoria)
LINE  646 | LINE 486 |   console.log('Full localData:', JSON.stringify(localData.value, null, 2))
LINE  647 | LINE 487 |   emit('submit', localData.value)
LINE  648 | LINE 488 | }
LINE  649 | LINE 489 | </script>
LINE  650 | 
LINE  651 | ==============================================================
LINE  652 | FILE: src/components/producto/creacion/productoTable.vue
LINE  653 | ==============================================================
LINE  654 | LINE   1 | //src\components\producto\creacion\productoTable.vue
LINE  655 | LINE   2 | <template>
LINE  656 | LINE   3 |   <div>
LINE  657 | LINE   4 |     <q-card flat class="q-mb-md">
LINE  658 | LINE   5 |       <q-card-section class="row items-center justify-between q-pb-none">
LINE  659 | LINE   6 |         <div class="col-12 col-md-4">
LINE  660 | LINE   7 |           <div class="text-h6 text-primary text-weight-bold">
LINE  661 | LINE   8 |             <q-icon name="inventory_2" size="sm" class="q-mr-sm" />
LINE  662 | LINE   9 |             Catálogo de Productos
LINE  663 | LINE  10 |           </div>
LINE  664 | LINE  11 |           <div class="text-caption text-grey-7">Administre sus productos y servicios</div>
LINE  665 | LINE  12 |         </div>
LINE  666 | LINE  13 |         <div class="col-12 col-md-8">
LINE  667 | LINE  14 |           <div class="row q-gutter-sm items-center justify-end q-mt-sm q-md-mt-none">
LINE  668 | LINE  15 |             <q-btn
LINE  669 | LINE  16 |               unelevated
LINE  670 | LINE  17 |               outline
LINE  671 | LINE  18 |               color="blue"
LINE  672 | LINE  19 |               @click="$emit('irconjunto')"
LINE  673 | LINE  20 |               icon="mdi-set-all"
LINE  674 | LINE  21 |               label="Conjunto"
LINE  675 | LINE  22 |             />
LINE  676 | LINE  23 |             <q-btn
LINE  677 | LINE  24 |               unelevated
LINE  678 | LINE  25 |               outline
LINE  679 | LINE  26 |               color="indigo"
LINE  680 | LINE  27 |               @click="exportarDatos"
LINE  681 | LINE  28 |               icon="mdi-file-excel"
LINE  682 | LINE  29 |               label="Descargar Excel"
LINE  683 | LINE  30 |             />
LINE  684 | LINE  31 |             <q-btn
LINE  685 | LINE  32 |               unelevated
LINE  686 | LINE  33 |               outline
LINE  687 | LINE  34 |               color="positive"
LINE  688 | LINE  35 |               @click="exportarFormato"
LINE  689 | LINE  36 |               icon="mdi-file-download-outline"
LINE  690 | LINE  37 |               label="Descargar Formato"
LINE  691 | LINE  38 |             />
LINE  692 | LINE  39 |             <q-btn
LINE  693 | LINE  40 |               unelevated
LINE  694 | LINE  41 |               outline
LINE  695 | LINE  42 |               color="secondary"
LINE  696 | LINE  43 |               @click="$refs.fileInput.click()"
LINE  697 | LINE  44 |               icon="mdi-file-upload-outline"
LINE  698 | LINE  45 |               label="Cargar Excel"
LINE  699 | LINE  46 |               :loading="importing"
LINE  700 | LINE  47 |               :disable="importing"
LINE  701 | LINE  48 |             />
LINE  702 | LINE  49 |             <q-btn color="primary" @click="$emit('add')" class="btn-res" title="Registrar Producto">
LINE  703 | LINE  50 |               <q-icon name="add" class="icono" />
LINE  704 | LINE  51 |               <span class="texto"> <q-icon name="add" /> Nuevo </span>
LINE  705 | LINE  52 |             </q-btn>
LINE  706 | LINE  53 |             <input
LINE  707 | LINE  54 |               type="file"
LINE  708 | LINE  55 |               ref="fileInput"
LINE  709 | LINE  56 |               style="display: none"
LINE  710 | LINE  57 |               accept=".xlsx, .xls"
LINE  711 | LINE  58 |               @change="onFileSelected"
LINE  712 | LINE  59 |             />
LINE  713 | LINE  60 |             <q-btn
LINE  714 | LINE  61 |               v-if="selectedIds.size > 0"
LINE  715 | LINE  62 |               unelevated
LINE  716 | LINE  63 |               color="negative"
LINE  717 | LINE  64 |               icon="delete_sweep"
LINE  718 | LINE  65 |               label="Eliminar seleccionados"
LINE  719 | LINE  66 |               @click="eliminarSeleccionados"
LINE  720 | LINE  67 |             />
LINE  721 | LINE  68 |             <!-- Dentro de <q-card-section class="row items-center justify-between q-pb-none"> -->
LINE  722 | LINE  69 |             <q-checkbox
LINE  723 | LINE  70 |               v-model="selectAll"
LINE  724 | LINE  71 |               label="Seleccionar todo"
LINE  725 | LINE  72 |               :indeterminate="selectedIds.size > 0 && selectedIds.length < filteredRows.length"
LINE  726 | LINE  73 |             />
LINE  727 | LINE  74 |           </div>
LINE  728 | LINE  75 |         </div>
LINE  729 | LINE  76 |       </q-card-section>
LINE  730 | LINE  77 | 
LINE  731 | LINE  78 |       <q-card-section>
LINE  732 | LINE  79 |         <BaseFilterableTable
LINE  733 | LINE  80 |           id="tablaProductos"
LINE  734 | LINE  81 |           ref="reHijo"
LINE  735 | LINE  82 |           :rows="filteredRows"
LINE  736 | LINE  83 |           :columns="columns"
LINE  737 | LINE  84 |           :arrayHeaders="arrayHeaders"
LINE  738 | LINE  85 |           row-key="id"
LINE  739 | LINE  86 |           :loading="loading"
LINE  740 | LINE  87 |           flat
LINE  741 | LINE  88 |           bordered
LINE  742 | LINE  89 |         >
LINE  743 | LINE  90 |           <template v-slot:top-right></template>
LINE  744 | LINE  91 | 
LINE  745 | LINE  92 |           <template v-slot:body-cell-imagen="props">
LINE  746 | LINE  93 |             <q-td :props="props" id="imagenproducto">
LINE  747 | LINE  94 |               <q-img
LINE  748 | LINE  95 |                 :src="imagen + props.row.imagen"
LINE  749 | LINE  96 |                 @click="abrirModal(props.row.imagen)"
LINE  750 | LINE  97 |                 style="max-width: 100px; max-height: 100px; cursor: pointer"
LINE  751 | LINE  98 |                 spinner-color="primary"
LINE  752 | LINE  99 |               >
LINE  753 | LINE 100 |                 <template v-slot:error>
LINE  754 | LINE 101 |                   <div
LINE  755 | LINE 102 |                     class="column items-center justify-center bg-grey-3"
LINE  756 | LINE 103 |                     style="height: 100%; width: 100%"
LINE  757 | LINE 104 |                   >
LINE  758 | LINE 105 |                     <q-icon name="image_not_supported" size="md" color="grey-7" />
LINE  759 | LINE 106 |                   </div>
LINE  760 | LINE 107 |                 </template>
LINE  761 | LINE 108 |               </q-img>
LINE  762 | LINE 109 |             </q-td>
LINE  763 | LINE 110 |           </template>
LINE  764 | LINE 111 |           <template v-slot:body-cell-productosin="props">
LINE  765 | LINE 112 |             <q-td :props="props">
LINE  766 | LINE 113 |               <div class="text-truncate" @click.stop v-if="props.row.productosin">
LINE  767 | LINE 114 |                 {{ props.row.productosin?.descripcion }}
LINE  768 | LINE 115 | 
LINE  769 | LINE 116 |                 <q-popup-proxy>
LINE  770 | LINE 117 |                   <q-card class="q-pa-sm" style="max-width: 300px; white-space: normal">
LINE  771 | LINE 118 |                     {{ props.row.productosin?.descripcion }}
LINE  772 | LINE 119 |                   </q-card>
LINE  773 | LINE 120 |                 </q-popup-proxy>
LINE  774 | LINE 121 |               </div>
LINE  775 | LINE 122 |             </q-td>
LINE  776 | LINE 123 |           </template>
LINE  777 | LINE 124 | 
LINE  778 | LINE 125 |           <template v-slot:body-cell-opciones="props">
LINE  779 | LINE 126 |             <q-td :props="props" class="text-nowrap">
LINE  780 | LINE 127 |               <q-btn
LINE  781 | LINE 128 |                 icon="edit"
LINE  782 | LINE 129 |                 color="primary"
LINE  783 | LINE 130 |                 dense
LINE  784 | LINE 131 |                 class="q-mr-sm"
LINE  785 | LINE 132 |                 @click="$emit('edit-item', props.row)"
LINE  786 | LINE 133 |                 flat
LINE  787 | LINE 134 |                 id="editarproducto"
LINE  788 | LINE 135 |               />
LINE  789 | LINE 136 |               <q-btn
LINE  790 | LINE 137 |                 icon="tune"
LINE  791 | LINE 138 |                 color="secondary"
LINE  792 | LINE 139 |                 dense
LINE  793 | LINE 140 |                 class="q-mr-sm"
LINE  794 | LINE 141 |                 @click="$emit('gestionar-variantes', props.row)"
LINE  795 | LINE 142 |                 flat
LINE  796 | LINE 143 |                 title="Gestionar variantes"
LINE  797 | LINE 144 |                 id="variantesproducto"
LINE  798 | LINE 145 |               />
LINE  799 | LINE 146 |               <q-btn
LINE  800 | LINE 147 |                 icon="delete"
LINE  801 | LINE 148 |                 color="negative"
LINE  802 | LINE 149 |                 dense
LINE  803 | LINE 150 |                 @click="$emit('delete-item', props.row)"
LINE  804 | LINE 151 |                 flat
LINE  805 | LINE 152 |                 id="eliminarproducto"
LINE  806 | LINE 153 |               />
LINE  807 | LINE 154 |             </q-td>
LINE  808 | LINE 155 |           </template>
LINE  809 | LINE 156 |           <template v-slot:body-cell-seleccionar="props">
LINE  810 | LINE 157 |             <q-td :props="props" auto-width>
LINE  811 | LINE 158 |               <q-checkbox
LINE  812 | LINE 159 |                 :model-value="selectedIds.has(props.row.id)"
LINE  813 | LINE 160 |                 @update:model-value="(val) => toggleSeleccion(props.row.id, val)"
LINE  814 | LINE 161 |                 dense
LINE  815 | LINE 162 |               />
LINE  816 | LINE 163 |             </q-td>
LINE  817 | LINE 164 |           </template>
LINE  818 | LINE 165 |         </BaseFilterableTable>
LINE  819 | LINE 166 |       </q-card-section>
LINE  820 | LINE 167 |     </q-card>
LINE  821 | LINE 168 | 
LINE  822 | LINE 169 |     <q-dialog v-model="mostrarImagen">
LINE  823 | LINE 170 |       <q-card class="responsive-dialog">
LINE  824 | LINE 171 |         <q-card-section class="bg-primary text-white text-h6 flex justify-between">
LINE  825 | LINE 172 |           <div>Vista Previa de Imagen</div>
LINE  826 | LINE 173 |           <q-btn icon="close" flat dense round @click="mostrarImagen = false" />
LINE  827 | LINE 174 |         </q-card-section>
LINE  828 | LINE 175 |         <q-card-section>
LINE  829 | LINE 176 |           <q-img
LINE  830 | LINE 177 |             :src="imagen + imagenSeleccionada"
LINE  831 | LINE 178 |             style="max-width: 100%; max-height: 100%"
LINE  832 | LINE 179 |             spinner-color="primary"
LINE  833 | LINE 180 |           />
LINE  834 | LINE 181 |         </q-card-section>
LINE  835 | LINE 182 |       </q-card>
LINE  836 | LINE 183 |     </q-dialog>
LINE  837 | LINE 184 |   </div>
LINE  838 | LINE 185 | </template>
LINE  839 | LINE 186 | 
LINE  840 | LINE 187 | <script setup>
LINE  841 | LINE 188 | import { ref, computed, watch } from 'vue'
LINE  842 | LINE 189 | import { imagen } from 'src/boot/url'
LINE  843 | LINE 190 | import { getTipoFactura } from 'src/composables/FuncionesG'
LINE  844 | LINE 191 | import BaseFilterableTable from 'src/components/componentesGenerales/filtradoTabla/BaseFilterableTable.vue'
LINE  845 | LINE 192 | import {
LINE  846 | LINE 193 |   exportarPlantillaProductos,
LINE  847 | LINE 194 |   importarProductosDesdeExcel,
LINE  848 | LINE 195 |   exportToXLSX_CatalogoProductos,
LINE  849 | LINE 196 | } from 'src/utils/XCLReportImport'
LINE  850 | LINE 197 | import { useQuasar } from 'quasar'
LINE  851 | LINE 198 | import { cambiarFormatoFecha } from 'src/composables/FuncionesG'
LINE  852 | LINE 199 | 
LINE  853 | LINE 200 | const selectedIds = ref(new Set())
LINE  854 | LINE 201 | const $q = useQuasar()
LINE  855 | LINE 202 | const fileInput = ref(null)
LINE  856 | LINE 203 | 
LINE  857 | LINE 204 | const tipoFactura = getTipoFactura(true)
LINE  858 | LINE 205 | 
LINE  859 | LINE 206 | const mostrarImagen = ref(false)
LINE  860 | LINE 207 | const imagenSeleccionada = ref(null)
LINE  861 | LINE 208 | 
LINE  862 | LINE 209 | const abrirModal = (img) => {
LINE  863 | LINE 210 |   imagenSeleccionada.value = img
LINE  864 | LINE 211 |   mostrarImagen.value = true
LINE  865 | LINE 212 | }
LINE  866 | LINE 213 | const props = defineProps({
LINE  867 | LINE 214 |   rows: {
LINE  868 | LINE 215 |     type: Array,
LINE  869 | LINE 216 |     required: true,
LINE  870 | LINE 217 |     default: () => [],
LINE  871 | LINE 218 |   },
LINE  872 | LINE 219 |   loading: {
LINE  873 | LINE 220 |     type: Boolean,
LINE  874 | LINE 221 |     default: false,
LINE  875 | LINE 222 |   },
LINE  876 | LINE 223 |   importing: { type: Boolean, default: false },
LINE  877 | LINE 224 | })
LINE  878 | LINE 225 | 
LINE  879 | LINE 226 | let columns = []
LINE  880 | LINE 227 | if (tipoFactura) {
LINE  881 | LINE 228 |   columns = [
LINE  882 | LINE 229 |     { name: 'numero', label: 'N°', field: 'numero', align: 'right', dataType: 'number' },
LINE  883 | LINE 230 |     {
LINE  884 | LINE 231 |       name: 'fecha',
LINE  885 | LINE 232 |       label: 'Fecha',
LINE  886 | LINE 233 |       field: 'fecha',
LINE  887 | LINE 234 |       align: 'left',
LINE  888 | LINE 235 |       format: (val) => cambiarFormatoFecha(val),
LINE  889 | LINE 236 |       dataType: 'date',
LINE  890 | LINE 237 |     },
LINE  891 | LINE 238 |     { name: 'codigo', label: 'Cod.', field: 'codigo', align: 'left', dataType: 'text' },
LINE  892 | LINE 239 |     { name: 'nombre', label: 'Nombre', field: 'nombre', align: 'left', dataType: 'text' },
LINE  893 | LINE 240 |     {
LINE  894 | LINE 241 |       name: 'descripcion',
LINE  895 | LINE 242 |       label: 'Descripción',
LINE  896 | LINE 243 |       field: 'descripcion',
LINE  897 | LINE 244 |       align: 'left',
LINE  898 | LINE 245 |       dataType: 'text',
LINE  899 | LINE 246 |     },
LINE  900 | LINE 247 |     { name: 'categoria', label: 'Categoría', field: 'categoria', align: 'left', dataType: 'text' },
LINE  901 | LINE 248 |     {
LINE  902 | LINE 249 |       name: 'subcategoria',
LINE  903 | LINE 250 |       label: 'Sub Categorías',
LINE  904 | LINE 251 |       field: 'subcategoria',
LINE  905 | LINE 252 |       align: 'left',
LINE  906 | LINE 253 |       dataType: 'text',
LINE  907 | LINE 254 |     },
LINE  908 | LINE 255 |     {
LINE  909 | LINE 256 |       name: 'codigobarras',
LINE  910 | LINE 257 |       label: 'Cod.Barra',
LINE  911 | LINE 258 |       field: 'codigobarras',
LINE  912 | LINE 259 |       align: 'right',
LINE  913 | LINE 260 |       dataType: 'text',
LINE  914 | LINE 261 |     },
LINE  915 | LINE 262 |     {
LINE  916 | LINE 263 |       name: 'medida',
LINE  917 | LINE 264 |       label: 'Caract.',
LINE  918 | LINE 265 |       field: 'medida',
LINE  919 | LINE 266 |       align: 'left',
LINE  920 | LINE 267 |       dataType: 'text',
LINE  921 | LINE 268 |       defaultVisible: false,
LINE  922 | LINE 269 |     },
LINE  923 | LINE 270 |     {
LINE  924 | LINE 271 |       name: 'estadoproducto',
LINE  925 | LINE 272 |       label: 'Estado',
LINE  926 | LINE 273 |       field: 'estadoproducto',
LINE  927 | LINE 274 |       align: 'left',
LINE  928 | LINE 275 |       dataType: 'text',
LINE  929 | LINE 276 |       defaultVisible: false,
LINE  930 | LINE 277 |     },
LINE  931 | LINE 278 |     {
LINE  932 | LINE 279 |       name: 'unidad',
LINE  933 | LINE 280 |       label: 'Unidad',
LINE  934 | LINE 281 |       field: 'unidad',
LINE  935 | LINE 282 |       align: 'left',
LINE  936 | LINE 283 |       dataType: 'text',
LINE  937 | LINE 284 |       defaultVisible: false,
LINE  938 | LINE 285 |     },
LINE  939 | LINE 286 |     {
LINE  940 | LINE 287 |       name: 'caracteristica',
LINE  941 | LINE 288 |       label: 'Otras caract.',
LINE  942 | LINE 289 |       field: 'caracteristica',
LINE  943 | LINE 290 |       align: 'left',
LINE  944 | LINE 291 |       dataType: 'text',
LINE  945 | LINE 292 |       defaultVisible: false,
LINE  946 | LINE 293 |     },
LINE  947 | LINE 294 |     {
LINE  948 | LINE 295 |       name: 'productosin',
LINE  949 | LINE 296 |       label: 'Producto SIN',
LINE  950 | LINE 297 |       field: 'productosin',
LINE  951 | LINE 298 |       align: 'left',
LINE  952 | LINE 299 |       dataType: 'text',
LINE  953 | LINE 300 |       defaultVisible: false,
LINE  954 | LINE 301 |     },
LINE  955 | LINE 302 |     {
LINE  956 | LINE 303 |       name: 'codigonandina',
LINE  957 | LINE 304 |       label: 'CodigoNandina',
LINE  958 | LINE 305 |       field: 'codigonandina',
LINE  959 | LINE 306 |       align: 'left',
LINE  960 | LINE 307 |       dataType: 'text',
LINE  961 | LINE 308 |       defaultVisible: false,
LINE  962 | LINE 309 |     },
LINE  963 | LINE 310 | 
LINE  964 | LINE 311 |     { name: 'imagen', label: 'Imagen', field: 'imagen', align: 'center' },
LINE  965 | LINE 312 |     { name: 'opciones', label: 'Opciones', field: 'opciones', sortable: false },
LINE  966 | LINE 313 |     {
LINE  967 | LINE 314 |       name: 'seleccionar',
LINE  968 | LINE 315 |       label: '',
LINE  969 | LINE 316 |       field: 'seleccionar',
LINE  970 | LINE 317 |       align: 'center',
LINE  971 | LINE 318 |       sortable: false,
LINE  972 | LINE 319 |       headerStyle: 'width: 50px',
LINE  973 | LINE 320 |     },
LINE  974 | LINE 321 |   ]
LINE  975 | LINE 322 | } else {
LINE  976 | LINE 323 |   columns = [
LINE  977 | LINE 324 |     { name: 'numero', label: 'N°', field: 'numero', align: 'right', dataType: 'number' },
LINE  978 | LINE 325 |     {
LINE  979 | LINE 326 |       name: 'fecha',
LINE  980 | LINE 327 |       label: 'Fecha',
LINE  981 | LINE 328 |       field: 'fecha',
LINE  982 | LINE 329 |       align: 'left',
LINE  983 | LINE 330 |       format: (val) => cambiarFormatoFecha(val),
LINE  984 | LINE 331 |       dataType: 'date',
LINE  985 | LINE 332 |     },
LINE  986 | LINE 333 |     { name: 'codigo', label: 'Cod.', field: 'codigo', align: 'left', dataType: 'text' },
LINE  987 | LINE 334 |     { name: 'nombre', label: 'Nombre', field: 'nombre', align: 'left', dataType: 'text' },
LINE  988 | LINE 335 |     {
LINE  989 | LINE 336 |       name: 'descripcion',
LINE  990 | LINE 337 |       label: 'Descripción',
LINE  991 | LINE 338 |       field: 'descripcion',
LINE  992 | LINE 339 |       align: 'left',
LINE  993 | LINE 340 |       dataType: 'text',
LINE  994 | LINE 341 |     },
LINE  995 | LINE 342 |     { name: 'categoria', label: 'Categoría', field: 'categoria', align: 'left', dataType: 'text' },
LINE  996 | LINE 343 |     {
LINE  997 | LINE 344 |       name: 'subcategoria',
LINE  998 | LINE 345 |       label: 'Sub Categorías',
LINE  999 | LINE 346 |       field: 'subcategoria',
LINE 1000 | LINE 347 |       align: 'left',
LINE 1001 | LINE 348 |       dataType: 'text',
LINE 1002 | LINE 349 |     },
LINE 1003 | LINE 350 |     {
LINE 1004 | LINE 351 |       name: 'codigobarras',
LINE 1005 | LINE 352 |       label: 'Cod.Barra',
LINE 1006 | LINE 353 |       field: 'codigobarras',
LINE 1007 | LINE 354 |       align: 'right',
LINE 1008 | LINE 355 |       dataType: 'text',
LINE 1009 | LINE 356 |     },
LINE 1010 | LINE 357 |     {
LINE 1011 | LINE 358 |       name: 'medida',
LINE 1012 | LINE 359 |       label: 'Caract.',
LINE 1013 | LINE 360 |       field: 'medida',
LINE 1014 | LINE 361 |       align: 'left',
LINE 1015 | LINE 362 |       dataType: 'text',
LINE 1016 | LINE 363 |       defaultVisible: false,
LINE 1017 | LINE 364 |     },
LINE 1018 | LINE 365 |     {
LINE 1019 | LINE 366 |       name: 'estadoproducto',
LINE 1020 | LINE 367 |       label: 'Estado',
LINE 1021 | LINE 368 |       field: 'estadoproducto',
LINE 1022 | LINE 369 |       align: 'left',
LINE 1023 | LINE 370 |       dataType: 'text',
LINE 1024 | LINE 371 |       defaultVisible: false,
LINE 1025 | LINE 372 |     },
LINE 1026 | LINE 373 |     {
LINE 1027 | LINE 374 |       name: 'unidad',
LINE 1028 | LINE 375 |       label: 'Unidad',
LINE 1029 | LINE 376 |       field: 'unidad',
LINE 1030 | LINE 377 |       align: 'left',
LINE 1031 | LINE 378 |       dataType: 'text',
LINE 1032 | LINE 379 |       defaultVisible: false,
LINE 1033 | LINE 380 |     },
LINE 1034 | LINE 381 |     {
LINE 1035 | LINE 382 |       name: 'caracteristica',
LINE 1036 | LINE 383 |       label: 'Otras caract.',
LINE 1037 | LINE 384 |       field: 'caracteristica',
LINE 1038 | LINE 385 |       align: 'left',
LINE 1039 | LINE 386 |       dataType: 'text',
LINE 1040 | LINE 387 |       defaultVisible: false,
LINE 1041 | LINE 388 |     },
LINE 1042 | LINE 389 | 
LINE 1043 | LINE 390 |     { name: 'imagen', label: 'Imagen', field: 'imagen', align: 'center' },
LINE 1044 | LINE 391 |     { name: 'opciones', label: 'Opciones', field: 'opciones', sortable: false },
LINE 1045 | LINE 392 |     {
LINE 1046 | LINE 393 |       name: 'seleccionar',
LINE 1047 | LINE 394 |       label: '',
LINE 1048 | LINE 395 |       field: 'seleccionar',
LINE 1049 | LINE 396 |       align: 'center',
LINE 1050 | LINE 397 |       sortable: false,
LINE 1051 | LINE 398 |       headerStyle: 'width: 50px',
LINE 1052 | LINE 399 |     },
LINE 1053 | LINE 400 |   ]
LINE 1054 | LINE 401 | }
LINE 1055 | LINE 402 | 
LINE 1056 | LINE 403 | const arrayHeaders = [
LINE 1057 | LINE 404 |   'numero',
LINE 1058 | LINE 405 |   'fecha',
LINE 1059 | LINE 406 |   'codigo',
LINE 1060 | LINE 407 |   'nombre',
LINE 1061 | LINE 408 |   'descripcion',
LINE 1062 | LINE 409 |   'categoria',
LINE 1063 | LINE 410 |   'subcategoria',
LINE 1064 | LINE 411 |   'codigobarras',
LINE 1065 | LINE 412 |   'medida',
LINE 1066 | LINE 413 |   'estadoproducto',
LINE 1067 | LINE 414 |   'unidad',
LINE 1068 | LINE 415 |   'caracteristica',
LINE 1069 | LINE 416 |   'productosin',
LINE 1070 | LINE 417 |   'codigonandina',
LINE 1071 | LINE 418 | ]
LINE 1072 | LINE 419 | 
LINE 1073 | LINE 420 | const search = ref('')
LINE 1074 | LINE 421 | 
LINE 1075 | LINE 422 | const filteredRows = computed(() => {
LINE 1076 | LINE 423 |   if (!search.value) return props.rows
LINE 1077 | LINE 424 |   const term = search.value.toLowerCase()
LINE 1078 | LINE 425 |   return props.rows.filter((row) => {
LINE 1079 | LINE 426 |     // Buscar el término en cualquier propiedad de la fila (sin importar qué columna sea)
LINE 1080 | LINE 427 |     return Object.values(row).some((val) => val && String(val).toLowerCase().includes(term))
LINE 1081 | LINE 428 |   })
LINE 1082 | LINE 429 | })
LINE 1083 | LINE 430 | 
LINE 1084 | LINE 431 | const exportarFormato = () => {
LINE 1085 | LINE 432 |   exportarPlantillaProductos()
LINE 1086 | LINE 433 | }
LINE 1087 | LINE 434 | 
LINE 1088 | LINE 435 | const exportarDatos = () => {
LINE 1089 | LINE 436 |   if (props.rows.length === 0) {
LINE 1090 | LINE 437 |     $q.notify({ type: 'warning', message: 'No hay datos para exportar' })
LINE 1091 | LINE 438 |     return
LINE 1092 | LINE 439 |   }
LINE 1093 | LINE 440 |   exportToXLSX_CatalogoProductos(props.rows)
LINE 1094 | LINE 441 | }
LINE 1095 | LINE 442 | 
LINE 1096 | LINE 443 | const emit = defineEmits([
LINE 1097 | LINE 444 |   'add',
LINE 1098 | LINE 445 |   'edit-item',
LINE 1099 | LINE 446 |   'delete-item',
LINE 1100 | LINE 447 |   'toggle-status',
LINE 1101 | LINE 448 |   'mostrarReporte',
LINE 1102 | LINE 449 |   'importar',
LINE 1103 | LINE 450 |   'delete-selected',
LINE 1104 | LINE 451 |   'gestionar-variantes',
LINE 1105 | LINE 452 | ])
LINE 1106 | LINE 453 | 
LINE 1107 | LINE 454 | const toggleSeleccion = (id, checked) => {
LINE 1108 | LINE 455 |   if (checked) {
LINE 1109 | LINE 456 |     selectedIds.value.add(id)
LINE 1110 | LINE 457 |   } else {
LINE 1111 | LINE 458 |     selectedIds.value.delete(id)
LINE 1112 | LINE 459 |   }
LINE 1113 | LINE 460 |   // Forzar reactividad de Set (en Vue 3 no siempre es necesario, pero mejor)
LINE 1114 | LINE 461 |   selectedIds.value = new Set(selectedIds.value)
LINE 1115 | LINE 462 | }
LINE 1116 | LINE 463 | 
LINE 1117 | LINE 464 | const eliminarSeleccionados = () => {
LINE 1118 | LINE 465 |   if (selectedIds.value.size === 0) return
LINE 1119 | LINE 466 |   const ids = [...selectedIds.value]
LINE 1120 | LINE 467 |   emit('delete-selected', ids)
LINE 1121 | LINE 468 |   selectedIds.value = new Set() // limpiar selección
LINE 1122 | LINE 469 | }
LINE 1123 | LINE 470 | 
LINE 1124 | LINE 471 | const selectAll = computed({
LINE 1125 | LINE 472 |   get() {
LINE 1126 | LINE 473 |     return (
LINE 1127 | LINE 474 |       filteredRows.value.length > 0 &&
LINE 1128 | LINE 475 |       filteredRows.value.every((row) => selectedIds.value.has(row.id))
LINE 1129 | LINE 476 |     )
LINE 1130 | LINE 477 |   },
LINE 1131 | LINE 478 |   set(val) {
LINE 1132 | LINE 479 |     if (val) {
LINE 1133 | LINE 480 |       // Agregar todos los IDs visibles
LINE 1134 | LINE 481 |       const ids = filteredRows.value.map((row) => row.id)
LINE 1135 | LINE 482 |       selectedIds.value = new Set(ids)
LINE 1136 | LINE 483 |     } else {
LINE 1137 | LINE 484 |       selectedIds.value = new Set()
LINE 1138 | LINE 485 |     }
LINE 1139 | LINE 486 |   },
LINE 1140 | LINE 487 | })
LINE 1141 | LINE 488 | const onFileSelected = async (event) => {
LINE 1142 | LINE 489 |   const file = event.target.files[0]
LINE 1143 | LINE 490 |   if (!file) return
LINE 1144 | LINE 491 | 
LINE 1145 | LINE 492 |   try {
LINE 1146 | LINE 493 |     $q.loading.show({ message: 'Leyendo archivo Excel...' })
LINE 1147 | LINE 494 |     const data = await importarProductosDesdeExcel(file)
LINE 1148 | LINE 495 |     event.target.value = ''
LINE 1149 | LINE 496 | 
LINE 1150 | LINE 497 |     if (data && data.length > 0) {
LINE 1151 | LINE 498 |       // Actualizar mensaje con la cantidad de productos
LINE 1152 | LINE 499 |       const total = data.length
LINE 1153 | LINE 500 |       $q.loading.show({
LINE 1154 | LINE 501 |         message: `Importando ${total} producto${total !== 1 ? 's' : ''}...`,
LINE 1155 | LINE 502 |       })
LINE 1156 | LINE 503 |       // Emitir los datos; el padre debe poner importing=true (si no lo está) y luego false al finalizar
LINE 1157 | LINE 504 |       emit('importar', data)
LINE 1158 | LINE 505 |     } else {
LINE 1159 | LINE 506 |       // Si no hay datos, ocultar loading y notificar
LINE 1160 | LINE 507 |       $q.loading.hide()
LINE 1161 | LINE 508 |       $q.notify({ type: 'warning', message: 'El archivo no contiene productos válidos' })
LINE 1162 | LINE 509 |     }
LINE 1163 | LINE 510 |   } catch (error) {
LINE 1164 | LINE 511 |     console.error('Error al importar:', error)
LINE 1165 | LINE 512 |     $q.loading.hide()
LINE 1166 | LINE 513 |     $q.notify({ type: 'negative', message: 'Error al procesar el archivo Excel' })
LINE 1167 | LINE 514 |   }
LINE 1168 | LINE 515 | }
LINE 1169 | LINE 516 | watch(
LINE 1170 | LINE 517 |   () => props.rows,
LINE 1171 | LINE 518 |   () => {
LINE 1172 | LINE 519 |     selectedIds.value = new Set()
LINE 1173 | LINE 520 |   },
LINE 1174 | LINE 521 | )
LINE 1175 | LINE 522 | watch(
LINE 1176 | LINE 523 |   () => props.importing,
LINE 1177 | LINE 524 |   (nuevo) => {
LINE 1178 | LINE 525 |     if (!nuevo) {
LINE 1179 | LINE 526 |       $q.loading.hide()
LINE 1180 | LINE 527 |     }
LINE 1181 | LINE 528 |   },
LINE 1182 | LINE 529 | )
LINE 1183 | LINE 530 | </script>
LINE 1184 | LINE 531 | <style>
LINE 1185 | LINE 532 | .text-truncate {
LINE 1186 | LINE 533 |   max-width: 200px; /* ajusta según tu tabla */
LINE 1187 | LINE 534 |   white-space: nowrap;
LINE 1188 | LINE 535 |   overflow: hidden;
LINE 1189 | LINE 536 |   text-overflow: ellipsis;
LINE 1190 | LINE 537 | }
LINE 1191 | LINE 538 | </style>
LINE 1192 | 
LINE 1193 | ==============================================================
LINE 1194 | FILE: src/composables/useReporteInventarioExterior.js
LINE 1195 | ==============================================================
LINE 1196 | LINE   1 | import { ref } from 'vue'
LINE 1197 | LINE   2 | import { date } from 'quasar'
LINE 1198 | LINE   3 | import { idusuario_md5, idempresa_md5 } from 'src/composables/FuncionesGenerales'
LINE 1199 | LINE   4 | import { api } from 'src/boot/axios'
LINE 1200 | LINE   5 | import axios from 'axios'
LINE 1201 | LINE   6 | import 'jspdf-autotable'
LINE 1202 | LINE   7 | 
LINE 1203 | LINE   8 | export function useReporteInventarioExterior() {
LINE 1204 | LINE   9 |   // --- Estado ---
LINE 1205 | LINE  10 |   const fechaInicio = ref(date.formatDate(Date.now(), 'YYYY-MM-DD'))
LINE 1206 | LINE  11 |   const fechaFin = ref(date.formatDate(Date.now(), 'YYYY-MM-DD'))
LINE 1207 | LINE  12 |   const datosReporte = ref([])
LINE 1208 | LINE  13 |   const cargando = ref(false)
LINE 1209 | LINE  14 | 
LINE 1210 | LINE  15 |   const idusuario = idusuario_md5()
LINE 1211 | LINE  16 |   // const idusuario = '03afdbd66e7929b125f8597834fa83a4'
LINE 1212 | LINE  17 | 
LINE 1213 | LINE  18 |   const idempresa = idempresa_md5()
LINE 1214 | LINE  19 |   console.log('ID Empresa MD5:', idempresa)
LINE 1215 | LINE  20 | 
LINE 1216 | LINE  21 |   const generarReporte = async () => {
LINE 1217 | LINE  22 |     cargando.value = true
LINE 1218 | LINE  23 |     try {
LINE 1219 | LINE  24 |       const endpoint = `reporteinvexterno/${idusuario}/${fechaInicio.value}/${fechaFin.value}`
LINE 1220 | LINE  25 |       console.log('Generando reporte con endpoint:', endpoint)
LINE 1221 | LINE  26 |       const response = await api.get(endpoint)
LINE 1222 | LINE  27 |       // Map data to add index and composite location
LINE 1223 | LINE  28 |       const promises = response.data.map(async (item, index) => {
LINE 1224 | LINE  29 |         const direccion = await obtenerDireccionComoString(item.latitud, item.longitud)
LINE 1225 | LINE  30 |         return {
LINE 1226 | LINE  31 |           ...item,
LINE 1227 | LINE  32 |           id: item.id_inv_externo,
LINE 1228 | LINE  33 |           indice: index + 1,
LINE 1229 | LINE  34 |           ubicacion: direccion,
LINE 1230 | LINE  35 |         }
LINE 1231 | LINE  36 |       })
LINE 1232 | LINE  37 |       datosReporte.value = await Promise.all(promises)
LINE 1233 | LINE  38 |       console.log('Datos del reporte recibidos (procesados):', datosReporte.value)
LINE 1234 | LINE  39 |     } catch (error) {
LINE 1235 | LINE  40 |       console.error('Error al generar reporte:', error)
LINE 1236 | LINE  41 |       datosReporte.value = []
LINE 1237 | LINE  42 |     } finally {
LINE 1238 | LINE  43 |       cargando.value = false
LINE 1239 | LINE  44 |     }
LINE 1240 | LINE  45 |   }
LINE 1241 | LINE  46 | 
LINE 1242 | LINE  47 |   async function obtenerDireccionComoString(lat, lng) {
LINE 1243 | LINE  48 |     try {
LINE 1244 | LINE  49 |       const url = 'https://nominatim.openstreetmap.org/reverse'
LINE 1245 | LINE  50 | 
LINE 1246 | LINE  51 |       const response = await axios.get(url, {
LINE 1247 | LINE  52 |         params: {
LINE 1248 | LINE  53 |           format: 'json',
LINE 1249 | LINE  54 |           lat: lat,
LINE 1250 | LINE  55 |           lon: lng,
LINE 1251 | LINE  56 |           zoom: 18,
LINE 1252 | LINE  57 |           addressdetails: 1,
LINE 1253 | LINE  58 |         },
LINE 1254 | LINE  59 |         headers: {
LINE 1255 | LINE  60 |           Accept: 'application/json',
LINE 1256 | LINE  61 |         },
LINE 1257 | LINE  62 |       })
LINE 1258 | LINE  63 | 
LINE 1259 | LINE  64 |       // Retorna toda la dirección en una sola cadena no una promesa
LINE 1260 | LINE  65 |       return response.data.display_name || 'Dirección no disponible'
LINE 1261 | LINE  66 |     } catch (error) {
LINE 1262 | LINE  67 |       console.error('Error obteniendo la dirección:', error)
LINE 1263 | LINE  68 |       return 'Dirección no disponible'
LINE 1264 | LINE  69 |     }
LINE 1265 | LINE  70 |   }
LINE 1266 | LINE  71 | 
LINE 1267 | LINE  72 |   //función para generar reporte detallado
LINE 1268 | LINE  73 |   const generarReporteDetalladoIExternor = async (idInventario) => {
LINE 1269 | LINE  74 |     try {
LINE 1270 | LINE  75 |       const endpoint = `detalleInventarioExterior/${idInventario}/${idempresa}`
LINE 1271 | LINE  76 |       console.log('Generando reporte detallado con endpoint:', endpoint)
LINE 1272 | LINE  77 |       const response = await api.get(endpoint)
LINE 1273 | LINE  78 |       console.log('Datos del reporte detallado recibidos:', response.data)
LINE 1274 | LINE  79 | 
LINE 1275 | LINE  80 |       // Limpiar descripción de productos
LINE 1276 | LINE  81 |       if (response.data && response.data.length > 0 && response.data[0].detalle) {
LINE 1277 | LINE  82 |         response.data[0].detalle = response.data[0].detalle.map((item) => ({
LINE 1278 | LINE  83 |           ...item,
LINE 1279 | LINE  84 |           descripcion_producto: item.descripcion_producto
LINE 1280 | LINE  85 |             ? item.descripcion_producto.replace(/\s+/g, ' ').trim()
LINE 1281 | LINE  86 |             : item.descripcion_producto,
LINE 1282 | LINE  87 |         }))
LINE 1283 | LINE  88 |       }
LINE 1284 | LINE  89 | 
LINE 1285 | LINE  90 |       return response.data // Retorna los datos detallados del inventario
LINE 1286 | LINE  91 |     } catch (error) {
LINE 1287 | LINE  92 |       console.error('Error al generar reporte detallado:', error)
LINE 1288 | LINE  93 |     }
LINE 1289 | LINE  94 |   }
LINE 1290 | LINE  95 | 
LINE 1291 | LINE  96 |   return {
LINE 1292 | LINE  97 |     fechaInicio,
LINE 1293 | LINE  98 |     fechaFin,
LINE 1294 | LINE  99 |     datosReporte,
LINE 1295 | LINE 100 |     cargando,
LINE 1296 | LINE 101 |     generarReporte,
LINE 1297 | LINE 102 | 
LINE 1298 | LINE 103 |     columns: [
LINE 1299 | LINE 104 |       // Columnas reales para la tabla UI
LINE 1300 | LINE 105 |       { name: 'indice', label: 'Nº', field: 'indice', sortable: true, align: 'left' },
LINE 1301 | LINE 106 |       {
LINE 1302 | LINE 107 |         name: 'fecha',
LINE 1303 | LINE 108 |         label: 'Fecha',
LINE 1304 | LINE 109 |         field: 'fecha_control',
LINE 1305 | LINE 110 |         sortable: true,
LINE 1306 | LINE 111 |         dataType: 'date',
LINE 1307 | LINE 112 |         align: 'left',
LINE 1308 | LINE 113 |       },
LINE 1309 | LINE 114 |       { name: 'almacen', label: 'Almacén', field: 'almacen', sortable: true, align: 'left' },
LINE 1310 | LINE 115 |       { name: 'cliente', label: 'Cliente', field: 'cliente', sortable: true, align: 'left' },
LINE 1311 | LINE 116 |       { name: 'sucursal', label: 'Sucursal', field: 'sucursal', sortable: true, align: 'left' },
LINE 1312 | LINE 117 |       { name: 'observaciones', label: 'Obs.', field: 'observaciones', align: 'left' },
LINE 1313 | LINE 118 |       { name: 'ubicacion', label: 'Ubicacion', field: 'ubicacion' },
LINE 1314 | LINE 119 |       { name: 'reporte', label: 'Reporte', field: 'reporte' }, // Added name and label.reporte matching table
LINE 1315 | LINE 120 |     ],
LINE 1316 | LINE 121 |     arrayHeaders: ['fecha', 'almacen', 'cliente', 'sucursal'], // Filtros de columna activados
LINE 1317 | LINE 122 |     generarReporteDetalladoIExternor,
LINE 1318 | LINE 123 |   }
LINE 1319 | LINE 124 | }
LINE 1320 | 
LINE 1321 | ==============================================================
LINE 1322 | FILE: src/pages/producto/CproductoPage.vue
LINE 1323 | ==============================================================
LINE 1324 | LINE   1 | <template>
LINE 1325 | LINE   2 |   <q-page v-if="mostrarmoduloConjunto">
LINE 1326 | LINE   3 |     <div class="row justify-end q-mb-md">
LINE 1327 | LINE   4 |       <q-btn
LINE 1328 | LINE   5 |         color="primary"
LINE 1329 | LINE   6 |         label="Volver a Productos"
LINE 1330 | LINE   7 |         icon="arrow_back"
LINE 1331 | LINE   8 |         @click="mostrarmoduloConjunto = false"
LINE 1332 | LINE   9 |         outline
LINE 1333 | LINE  10 |       />
LINE 1334 | LINE  11 |     </div>
LINE 1335 | LINE  12 |     <seriePage />
LINE 1336 | LINE  13 |   </q-page>
LINE 1337 | LINE  14 |   <q-page padding v-else>
LINE 1338 | LINE  15 |     <q-dialog v-model="showForm">
LINE 1339 | LINE  16 |       <q-card class="responsive-dialog">
LINE 1340 | LINE  17 |         <q-card-section class="bg-primary text-h6 text-white flex justify-between">
LINE 1341 | LINE  18 |           <div>Registrar Producto o Servicio</div>
LINE 1342 | LINE  19 |           <q-btn icon="close" @click="toggleForm" dense flat round />
LINE 1343 | LINE  20 |         </q-card-section>
LINE 1344 | LINE  21 |         <q-card-section class="q-pa-none">
LINE 1345 | LINE  22 |           <producto-form
LINE 1346 | LINE  23 |             :isEditing="isEditing"
LINE 1347 | LINE  24 |             :model-value="formData"
LINE 1348 | LINE  25 |             :categorias="categorias"
LINE 1349 | LINE  26 |             :estados="estados"
LINE 1350 | LINE  27 |             :subcategorias="subcategorias"
LINE 1351 | LINE  28 |             :unidades="unidades"
LINE 1352 | LINE  29 |             :medidas="medidas"
LINE 1353 | LINE  30 |             :productoSIN="ProductoSin"
LINE 1354 | LINE  31 |             :unidadSIN="UnidadSin"
LINE 1355 | LINE  32 |             @submit="handleSubmit"
LINE 1356 | LINE  33 |             @cancel="toggleForm"
LINE 1357 | LINE  34 |             @categoria-changed="loadsubcategorias"
LINE 1358 | LINE  35 |           />
LINE 1359 | LINE  36 |         </q-card-section>
LINE 1360 | LINE  37 |       </q-card>
LINE 1361 | LINE  38 |     </q-dialog>
LINE 1362 | LINE  39 | 
LINE 1363 | LINE  40 |     <producto-tabla
LINE 1364 | LINE  41 |       :rows="productos"
LINE 1365 | LINE  42 |       :loading="cargando"
LINE 1366 | LINE  43 |       :importing="importing"
LINE 1367 | LINE  44 |       @add="toggleForm"
LINE 1368 | LINE  45 |       @irconjunto="mostrarmoduloConjunto = true"
LINE 1369 | LINE  46 |       @mostrarReporte="mostrarReporte"
LINE 1370 | LINE  47 |       @edit-item="editUnit"
LINE 1371 | LINE  48 |       @delete-item="confirmDelete"
LINE 1372 | LINE  49 |       @toggleStatus="toggleStatus"
LINE 1373 | LINE  50 |       @importar="handleImport"
LINE 1374 | LINE  51 |       @delete-selected="eliminarProductosSeleccionados"
LINE 1375 | LINE  52 |       @gestionar-variantes="abrirVariantes"
LINE 1376 | LINE  53 |     />
LINE 1377 | LINE  54 | 
LINE 1378 | LINE  55 |     <ProductoVarianteDialog
LINE 1379 | LINE  56 |       v-model="showVariantesDialog"
LINE 1380 | LINE  57 |       :producto="productoVariantes"
LINE 1381 | LINE  58 |       :empresa="idempresa"
LINE 1382 | LINE  59 |     />
LINE 1383 | LINE  60 |   </q-page>
LINE 1384 | LINE  61 | </template>
LINE 1385 | LINE  62 | 
LINE 1386 | LINE  63 | <script setup>
LINE 1387 | LINE  64 | import { ref, onMounted } from 'vue'
LINE 1388 | LINE  65 | import { api } from 'boot/axios' // Asegúrate de tener esto configurado
LINE 1389 | LINE  66 | import { idempresa_md5, validarUsuario } from 'src/composables/FuncionesGenerales'
LINE 1390 | LINE  67 | import { useQuasar } from 'quasar'
LINE 1391 | LINE  68 | import { objectToFormData } from 'src/composables/FuncionesGenerales'
LINE 1392 | LINE  69 | import ProductoForm from 'src/components/producto/creacion/productoForm.vue'
LINE 1393 | LINE  70 | import ProductoTabla from 'src/components/producto/creacion/productoTable.vue'
LINE 1394 | LINE  71 | import { imagen } from 'src/boot/url'
LINE 1395 | LINE  72 | import { getTipoFactura, getToken } from 'src/composables/FuncionesG'
LINE 1396 | LINE  73 | import seriePage from 'src/modules/serie/page/seriePage.vue'
LINE 1397 | LINE  74 | import ProductoVarianteDialog from 'src/components/producto/variantes/productoVarianteDialog.vue'
LINE 1398 | LINE  75 | const tipoFactura = getTipoFactura(true)
LINE 1399 | LINE  76 | const mostrarmoduloConjunto = ref(false)
LINE 1400 | LINE  77 | const showVariantesDialog = ref(false)
LINE 1401 | LINE  78 | const productoVariantes = ref(null)
LINE 1402 | LINE  79 | console.log('Tipo Factura:', tipoFactura)
LINE 1403 | LINE  80 | const idempresa = idempresa_md5()
LINE 1404 | LINE  81 | const contenidousuario = validarUsuario()
LINE 1405 | LINE  82 | console.log(contenidousuario)
LINE 1406 | LINE  83 | const token = getToken()
LINE 1407 | LINE  84 | console.log('Token:', token)
LINE 1408 | LINE  85 | const productos = ref([])
LINE 1409 | LINE  86 | 
LINE 1410 | LINE  87 | const categorias = ref([])
LINE 1411 | LINE  88 | 
LINE 1412 | LINE  89 | const estados = ref([])
LINE 1413 | LINE  90 | const subcategorias = ref([])
LINE 1414 | LINE  91 | const unidades = ref([])
LINE 1415 | LINE  92 | const medidas = ref([])
LINE 1416 | LINE  93 | const $q = useQuasar()
LINE 1417 | LINE  94 | const isEditing = ref(false)
LINE 1418 | LINE  95 | const showForm = ref(false)
LINE 1419 | LINE  96 | const cargando = ref(false)
LINE 1420 | LINE  97 | const importing = ref(false)
LINE 1421 | LINE  98 | 
LINE 1422 | LINE  99 | const formData = ref({
LINE 1423 | LINE 100 |   ver: 'registrarProducto',
LINE 1424 | LINE 101 |   idempresa: idempresa,
LINE 1425 | LINE 102 | })
LINE 1426 | LINE 103 | const ProductoSin = ref([])
LINE 1427 | LINE 104 | const UnidadSin = ref([])
LINE 1428 | LINE 105 | async function loadRows() {
LINE 1429 | LINE 106 |   try {
LINE 1430 | LINE 107 |     cargando.value = true
LINE 1431 | LINE 108 |     const tipo = getTipoFactura()
LINE 1432 | LINE 109 |     let point = ``
LINE 1433 | LINE 110 |     if (token && tipo && getTipoFactura(true) && getToken(true)) {
LINE 1434 | LINE 111 |       point = `listaProducto/${idempresa}/${token}/${tipo}`
LINE 1435 | LINE 112 |     } else {
LINE 1436 | LINE 113 |       point = `listaProducto/${idempresa}/`
LINE 1437 | LINE 114 |     }
LINE 1438 | LINE 115 |     console.log('Endpoint:', point)
LINE 1439 | LINE 116 |     const response = await api.get(point)
LINE 1440 | LINE 117 |     console.log('estos son los datos', response.data)
LINE 1441 | LINE 118 |     productos.value = response.data.map((obj, index) => ({ ...obj, numero: index + 1 }))
LINE 1442 | LINE 119 |   } catch (error) {
LINE 1443 | LINE 120 |     console.error('Error al cargar datos:', error)
LINE 1444 | LINE 121 |     $q.notify({
LINE 1445 | LINE 122 |       type: 'negative',
LINE 1446 | LINE 123 |       message: 'No se pudieron cargar los datos del catálogo',
LINE 1447 | LINE 124 |     })
LINE 1448 | LINE 125 |   } finally {
LINE 1449 | LINE 126 |     cargando.value = false
LINE 1450 | LINE 127 |   }
LINE 1451 | LINE 128 | }
LINE 1452 | LINE 129 | 
LINE 1453 | LINE 130 | async function loadcategorias() {
LINE 1454 | LINE 131 |   try {
LINE 1455 | LINE 132 |     const response = await api.get(`listaCategoriaProducto/${idempresa}`) // Cambia a tu ruta real
LINE 1456 | LINE 133 |     console.log(response)
LINE 1457 | LINE 134 |     const filtrados = response.data.filter((u) => u.estado == 1 && (!u.idp || u.idp == 0))
LINE 1458 | LINE 135 |     const formateado = filtrados.map((item) => ({
LINE 1459 | LINE 136 |       label: item.nombre,
LINE 1460 | LINE 137 |       value: item.id,
LINE 1461 | LINE 138 |     }))
LINE 1462 | LINE 139 |     categorias.value = formateado // Asume que la API devuelve un array
LINE 1463 | LINE 140 |   } catch (error) {
LINE 1464 | LINE 141 |     console.error('Error al cargar datos:', error)
LINE 1465 | LINE 142 |     $q.notify({
LINE 1466 | LINE 143 |       type: 'negative',
LINE 1467 | LINE 144 |       message: 'No se pudieron cargar los datos',
LINE 1468 | LINE 145 |     })
LINE 1469 | LINE 146 |   }
LINE 1470 | LINE 147 | }
LINE 1471 | LINE 148 | async function loadestados() {
LINE 1472 | LINE 149 |   try {
LINE 1473 | LINE 150 |     const response = await api.get(`listaEstadoProducto/${idempresa}`) // Cambia a tu ruta real
LINE 1474 | LINE 151 |     console.log(response)
LINE 1475 | LINE 152 |     const filtrados = response.data.filter((u) => u.estado == 1)
LINE 1476 | LINE 153 |     const formateado = filtrados.map((item) => ({
LINE 1477 | LINE 154 |       label: item.nombre,
LINE 1478 | LINE 155 |       value: item.id,
LINE 1479 | LINE 156 |     }))
LINE 1480 | LINE 157 |     estados.value = formateado // Asume que la API devuelve un array
LINE 1481 | LINE 158 |   } catch (error) {
LINE 1482 | LINE 159 |     console.error('Error al cargar datos:', error)
LINE 1483 | LINE 160 |     $q.notify({
LINE 1484 | LINE 161 |       type: 'negative',
LINE 1485 | LINE 162 |       message: 'No se pudieron cargar los Estados de Producto',
LINE 1486 | LINE 163 |     })
LINE 1487 | LINE 164 |   }
LINE 1488 | LINE 165 | }
LINE 1489 | LINE 166 | async function loadsubcategorias(idcategoria) {
LINE 1490 | LINE 167 |   console.log('idcategoria:', idcategoria)
LINE 1491 | LINE 168 | 
LINE 1492 | LINE 169 |   if (!idcategoria) {
LINE 1493 | LINE 170 |     subcategorias.value = []
LINE 1494 | LINE 171 |     return
LINE 1495 | LINE 172 |   }
LINE 1496 | LINE 173 |   try {
LINE 1497 | LINE 174 |     const response = await api.get(`listaCategoriaProducto/${idempresa}`) // Cambia a tu ruta real
LINE 1498 | LINE 175 |     console.log(formData.value)
LINE 1499 | LINE 176 |     const filtrados = response.data.filter((u) => u.estado == 1 && u.idp == idcategoria)
LINE 1500 | LINE 177 |     const formateado = filtrados.map((item) => ({
LINE 1501 | LINE 178 |       label: item.nombre,
LINE 1502 | LINE 179 |       value: item.id,
LINE 1503 | LINE 180 |     }))
LINE 1504 | LINE 181 |     subcategorias.value = formateado // Asume que la API devuelve un array
LINE 1505 | LINE 182 |   } catch (error) {
LINE 1506 | LINE 183 |     console.error('Error al cargar datos:', error)
LINE 1507 | LINE 184 |     $q.notify({
LINE 1508 | LINE 185 |       type: 'negative',
LINE 1509 | LINE 186 |       message: 'No se pudieron cargar los datos',
LINE 1510 | LINE 187 |     })
LINE 1511 | LINE 188 |   }
LINE 1512 | LINE 189 | }
LINE 1513 | LINE 190 | async function loadunidades() {
LINE 1514 | LINE 191 |   try {
LINE 1515 | LINE 192 |     const response = await api.get(`listaUnidadProducto/${idempresa}`) // Cambia a tu ruta real
LINE 1516 | LINE 193 |     console.log(response)
LINE 1517 | LINE 194 |     const filtrados = response.data.filter((u) => u.estado == 1)
LINE 1518 | LINE 195 |     const formateado = filtrados.map((item) => ({
LINE 1519 | LINE 196 |       label: item.nombre + ' : ' + item.descripcion,
LINE 1520 | LINE 197 |       value: item.id,
LINE 1521 | LINE 198 |     }))
LINE 1522 | LINE 199 |     unidades.value = formateado // Asume que la API devuelve un array
LINE 1523 | LINE 200 |   } catch (error) {
LINE 1524 | LINE 201 |     console.error('Error al cargar datos:', error)
LINE 1525 | LINE 202 |     $q.notify({
LINE 1526 | LINE 203 |       type: 'negative',
LINE 1527 | LINE 204 |       message: 'No se pudieron cargar los datos',
LINE 1528 | LINE 205 |     })
LINE 1529 | LINE 206 |   }
LINE 1530 | LINE 207 | }
LINE 1531 | LINE 208 | async function ListaProductoSin() {
LINE 1532 | LINE 209 |   if (!tipoFactura) {
LINE 1533 | LINE 210 |     return
LINE 1534 | LINE 211 |   }
LINE 1535 | LINE 212 |   const contenidousuario = validarUsuario()
LINE 1536 | LINE 213 |   const token = contenidousuario[0]?.factura?.access_token
LINE 1537 | LINE 214 |   const tipo = contenidousuario[0]?.factura?.tipo
LINE 1538 | LINE 215 |   const endpoint = `listaproductoSIN/productossin/${token}/${tipo}`
LINE 1539 | LINE 216 |   try {
LINE 1540 | LINE 217 |     const response = await api.get(endpoint) // Cambia a tu ruta real
LINE 1541 | LINE 218 |     console.log(response)
LINE 1542 | LINE 219 |     const res = response.data
LINE 1543 | LINE 220 |     if (res.status == 'success') {
LINE 1544 | LINE 221 |       const formateado = res.data.map((item) => ({
LINE 1545 | LINE 222 |         label: item.descripcion,
LINE 1546 | LINE 223 |         value: item.codigo,
LINE 1547 | LINE 224 |       }))
LINE 1548 | LINE 225 |       ProductoSin.value = formateado
LINE 1549 | LINE 226 |     }
LINE 1550 | LINE 227 |   } catch (error) {
LINE 1551 | LINE 228 |     console.error('Error al cargar datos:', error)
LINE 1552 | LINE 229 |     $q.notify({
LINE 1553 | LINE 230 |       type: 'negative',
LINE 1554 | LINE 231 |       message: 'No se pudieron cargar los datos',
LINE 1555 | LINE 232 |     })
LINE 1556 | LINE 233 |   }
LINE 1557 | LINE 234 | }
LINE 1558 | LINE 235 | async function ListaUnidadSin() {
LINE 1559 | LINE 236 |   if (!tipoFactura) {
LINE 1560 | LINE 237 |     return
LINE 1561 | LINE 238 |   }
LINE 1562 | LINE 239 |   const contenidousuario = validarUsuario()
LINE 1563 | LINE 240 |   const token = contenidousuario[0]?.factura?.access_token
LINE 1564 | LINE 241 |   const tipo = contenidousuario[0]?.factura?.tipo
LINE 1565 | LINE 242 |   const endpoint = `listaproductoSIN/unidadsin/${token}/${tipo}`
LINE 1566 | LINE 243 |   try {
LINE 1567 | LINE 244 |     const response = await api.get(endpoint) // Cambia a tu ruta real
LINE 1568 | LINE 245 |     console.log(response)
LINE 1569 | LINE 246 |     const res = response.data
LINE 1570 | LINE 247 |     if (res.status == 'success') {
LINE 1571 | LINE 248 |       const formateado = res.data.map((item) => ({
LINE 1572 | LINE 249 |         label: item.descripcion,
LINE 1573 | LINE 250 |         value: item.codigo,
LINE 1574 | LINE 251 |       }))
LINE 1575 | LINE 252 |       UnidadSin.value = formateado
LINE 1576 | LINE 253 |     }
LINE 1577 | LINE 254 |   } catch (error) {
LINE 1578 | LINE 255 |     console.error('Error al cargar datos:', error)
LINE 1579 | LINE 256 |     $q.notify({
LINE 1580 | LINE 257 |       type: 'negative',
LINE 1581 | LINE 258 |       message: 'No se pudieron cargar los datos',
LINE 1582 | LINE 259 |     })
LINE 1583 | LINE 260 |   }
LINE 1584 | LINE 261 | }
LINE 1585 | LINE 262 | async function loadmedidas() {
LINE 1586 | LINE 263 |   try {
LINE 1587 | LINE 264 |     const response = await api.get(`listaCaracteristicaProducto/${idempresa}`) // Cambia a tu ruta real
LINE 1588 | LINE 265 |     console.log(response)
LINE 1589 | LINE 266 |     const filtrados = response.data.filter((u) => u.estado == 1)
LINE 1590 | LINE 267 | 
LINE 1591 | LINE 268 |     const formateado = filtrados.map((item) => ({
LINE 1592 | LINE 269 |       label: item.nombre,
LINE 1593 | LINE 270 |       value: item.id,
LINE 1594 | LINE 271 |     }))
LINE 1595 | LINE 272 |     medidas.value = formateado // Asume que la API devuelve un array
LINE 1596 | LINE 273 |   } catch (error) {
LINE 1597 | LINE 274 |     console.error('Error al cargar datos:', error)
LINE 1598 | LINE 275 |     $q.notify({
LINE 1599 | LINE 276 |       type: 'negative',
LINE 1600 | LINE 277 |       message: 'No se pudieron cargar los datos',
LINE 1601 | LINE 278 |     })
LINE 1602 | LINE 279 |   }
LINE 1603 | LINE 280 | }
LINE 1604 | LINE 281 | 
LINE 1605 | LINE 282 | const handleSubmit = async (data) => {
LINE 1606 | LINE 283 |   const formData = objectToFormData(data)
LINE 1607 | LINE 284 | 
LINE 1608 | LINE 285 |   console.log('=== FormData entries ===')
LINE 1609 | LINE 286 |   // for (let [k, v] of formData.entries()) {
LINE 1610 | LINE 287 |   //   console.log(`${k}: ${v}`)
LINE 1611 | LINE 288 |   // }
LINE 1612 | LINE 289 | 
LINE 1613 | LINE 290 |   try {
LINE 1614 | LINE 291 |     if (isEditing.value) {
LINE 1615 | LINE 292 |       const response = await api.post(``, formData)
LINE 1616 | LINE 293 |       console.log('Edit response:', response.data)
LINE 1617 | LINE 294 |     } else {
LINE 1618 | LINE 295 |       const response = await api.post(``, formData)
LINE 1619 | LINE 296 |       console.log('Create response:', response.data)
LINE 1620 | LINE 297 |     }
LINE 1621 | LINE 298 |     $q.notify({
LINE 1622 | LINE 299 |       type: 'positive',
LINE 1623 | LINE 300 |       message: isEditing.value ? 'Editado correctamente' : 'Registrado correctamente',
LINE 1624 | LINE 301 |     })
LINE 1625 | LINE 302 |     loadRows()
LINE 1626 | LINE 303 |   } catch (error) {
LINE 1627 | LINE 304 |     console.error('Error al guardar:', error)
LINE 1628 | LINE 305 |     $q.notify({
LINE 1629 | LINE 306 |       type: 'negative',
LINE 1630 | LINE 307 |       message: 'Ocurrió un error al guardar' + error,
LINE 1631 | LINE 308 |     })
LINE 1632 | LINE 309 |   }
LINE 1633 | LINE 310 |   toggleForm()
LINE 1634 | LINE 311 | }
LINE 1635 | LINE 312 | const toggleForm = () => {
LINE 1636 | LINE 313 |   showForm.value = !showForm.value
LINE 1637 | LINE 314 |   if (!showForm.value) {
LINE 1638 | LINE 315 |     isEditing.value = false
LINE 1639 | LINE 316 |     resetForm()
LINE 1640 | LINE 317 |     subcategorias.value = [] // limpia subcategorías
LINE 1641 | LINE 318 |   }
LINE 1642 | LINE 319 | }
LINE 1643 | LINE 320 | function resetForm() {
LINE 1644 | LINE 321 |   isEditing.value = false
LINE 1645 | LINE 322 |   formData.value = {
LINE 1646 | LINE 323 |     ver: 'registrarProducto',
LINE 1647 | LINE 324 |     idempresa: idempresa,
LINE 1648 | LINE 325 |   }
LINE 1649 | LINE 326 | }
LINE 1650 | LINE 327 | const editUnit = async (row) => {
LINE 1651 | LINE 328 |   console.log(row)
LINE 1652 | LINE 329 |   const tipo = getTipoFactura()
LINE 1653 | LINE 330 |   let endpoint = ``
LINE 1654 | LINE 331 |   if (token && tipo && getTipoFactura(true) && getToken(true)) {
LINE 1655 | LINE 332 |     endpoint = `verificarExistenciaProducto/${row.id}/${token}/${tipo}`
LINE 1656 | LINE 333 |   } else {
LINE 1657 | LINE 334 |     endpoint = `verificarExistenciaProducto/${row.id}/`
LINE 1658 | LINE 335 |   }
LINE 1659 | LINE 336 |   console.log(endpoint)
LINE 1660 | LINE 337 |   const response = await api.get(endpoint) // Cambia a tu ruta real
LINE 1661 | LINE 338 |   console.log('API Response:', response.data)
LINE 1662 | LINE 339 |   const item = response.data.datos
LINE 1663 | LINE 340 |   console.log('Item data:', item)
LINE 1664 | LINE 341 | 
LINE 1665 | LINE 342 |   // Handle subcategoria - it might be missing, null, 0, or empty string
LINE 1666 | LINE 343 |   const rawSubcategoria = item?.idsubcategoria ?? null
LINE 1667 | LINE 344 |   const subcategoriaValue =
LINE 1668 | LINE 345 |     rawSubcategoria !== null && rawSubcategoria !== '0' && rawSubcategoria !== 0
LINE 1669 | LINE 346 |       ? rawSubcategoria
LINE 1670 | LINE 347 |       : null
LINE 1671 | LINE 348 | 
LINE 1672 | LINE 349 |   formData.value = {
LINE 1673 | LINE 350 |     ver: 'editarProducto',
LINE 1674 | LINE 351 |     id: item.id,
LINE 1675 | LINE 352 |     idempresa: idempresa,
LINE 1676 | LINE 353 |     codigo: item.codigo,
LINE 1677 | LINE 354 |     nombre: item.nombre,
LINE 1678 | LINE 355 |     descripcion: item.descripcion,
LINE 1679 | LINE 356 |     codigobarras: item.codbarras,
LINE 1680 | LINE 357 |     categoria: item?.idcategoria ?? null,
LINE 1681 | LINE 358 |     subcategoria: subcategoriaValue,
LINE 1682 | LINE 359 |     estadoproductos: item.idestadoproducto,
LINE 1683 | LINE 360 |     unidad: item.idunidad,
LINE 1684 | LINE 361 |     medida: item.idmedida,
LINE 1685 | LINE 362 |     caracteristica: item.caracteristica && item.caracteristica !== '0' ? item.caracteristica : '',
LINE 1686 | LINE 363 |     vista: imagen + item.imagen,
LINE 1687 | LINE 364 |     imagen: item.imagen,
LINE 1688 | LINE 365 |     codigosin:
LINE 1689 | LINE 366 |       tipoFactura && item.productosin && item.productosin[0] ? item.productosin[0].codigo : '',
LINE 1690 | LINE 367 |     unidadsin: tipoFactura && item.unidadsin && item.unidadsin[0] ? item.unidadsin[0].codigo : '',
LINE 1691 | LINE 368 |     codigoNandina:
LINE 1692 | LINE 369 |       tipoFactura && item.codigonandina && item.codigonandina !== '0' ? item.codigonandina : '',
LINE 1693 | LINE 370 |   }
LINE 1694 | LINE 371 | 
LINE 1695 | LINE 372 |   console.log('FormData to load:', formData.value)
LINE 1696 | LINE 373 |   loadsubcategorias(item?.idcategoria ?? null)
LINE 1697 | LINE 374 |   isEditing.value = true
LINE 1698 | LINE 375 |   showForm.value = true
LINE 1699 | LINE 376 | }
LINE 1700 | LINE 377 | 
LINE 1701 | LINE 378 | const confirmDelete = (row) => {
LINE 1702 | LINE 379 |   console.log(row)
LINE 1703 | LINE 380 | 
LINE 1704 | LINE 381 |   $q.dialog({
LINE 1705 | LINE 382 |     title: 'Confirmar',
LINE 1706 | LINE 383 |     message: `¿Eliminar Producto "${row.nombre}"?`,
LINE 1707 | LINE 384 |     cancel: true,
LINE 1708 | LINE 385 |     persistent: true,
LINE 1709 | LINE 386 |   }).onOk(async () => {
LINE 1710 | LINE 387 |     try {
LINE 1711 | LINE 388 |       const response = await api.get(`eliminarProducto/${row.id}`) // Cambia a tu ruta real
LINE 1712 | LINE 389 |       console.log(response)
LINE 1713 | LINE 390 |       if (response.data.estado === 'exito') {
LINE 1714 | LINE 391 |         loadRows()
LINE 1715 | LINE 392 |         $q.notify({
LINE 1716 | LINE 393 |           type: 'positive',
LINE 1717 | LINE 394 |           message: response.data.mensaje,
LINE 1718 | LINE 395 |         })
LINE 1719 | LINE 396 |       } else {
LINE 1720 | LINE 397 |         $q.notify({
LINE 1721 | LINE 398 |           type: 'negative',
LINE 1722 | LINE 399 |           message: response.data.mensaje,
LINE 1723 | LINE 400 |         })
LINE 1724 | LINE 401 |       }
LINE 1725 | LINE 402 |     } catch (error) {
LINE 1726 | LINE 403 |       console.error('Error al cargar datos:', error)
LINE 1727 | LINE 404 |       $q.notify({
LINE 1728 | LINE 405 |         type: 'negative',
LINE 1729 | LINE 406 |         message: 'No se pudieron cargar los datos',
LINE 1730 | LINE 407 |       })
LINE 1731 | LINE 408 |     }
LINE 1732 | LINE 409 |   })
LINE 1733 | LINE 410 | }
LINE 1734 | LINE 411 | const eliminarProductosSeleccionados = (ids) => {
LINE 1735 | LINE 412 |   console.log(ids)
LINE 1736 | LINE 413 | 
LINE 1737 | LINE 414 |   $q.dialog({
LINE 1738 | LINE 415 |     title: 'Confirmar',
LINE 1739 | LINE 416 |     message: `¿Eliminar Productos seleccionados?`,
LINE 1740 | LINE 417 |     cancel: true,
LINE 1741 | LINE 418 |     persistent: true,
LINE 1742 | LINE 419 |   }).onOk(async () => {
LINE 1743 | LINE 420 |     try {
LINE 1744 | LINE 421 |       const data = {
LINE 1745 | LINE 422 |         ver: 'eliminarProductosMasivo',
LINE 1746 | LINE 423 |         ids: ids,
LINE 1747 | LINE 424 |       }
LINE 1748 | LINE 425 |       const response = await api.post(``, data) // Cambia a tu ruta real
LINE 1749 | LINE 426 |       console.log(response)
LINE 1750 | LINE 427 |       if (response.data.estado === 'exito') {
LINE 1751 | LINE 428 |         loadRows()
LINE 1752 | LINE 429 |         $q.notify({
LINE 1753 | LINE 430 |           type: 'positive',
LINE 1754 | LINE 431 |           message: response.data.mensaje,
LINE 1755 | LINE 432 |         })
LINE 1756 | LINE 433 |       } else {
LINE 1757 | LINE 434 |         $q.notify({
LINE 1758 | LINE 435 |           type: 'negative',
LINE 1759 | LINE 436 |           message: response.data.mensaje,
LINE 1760 | LINE 437 |         })
LINE 1761 | LINE 438 |       }
LINE 1762 | LINE 439 |     } catch (error) {
LINE 1763 | LINE 440 |       console.error('Error al cargar datos:', error)
LINE 1764 | LINE 441 |       $q.notify({
LINE 1765 | LINE 442 |         type: 'negative',
LINE 1766 | LINE 443 |         message: 'No se pudieron cargar los datos',
LINE 1767 | LINE 444 |       })
LINE 1768 | LINE 445 |     }
LINE 1769 | LINE 446 |   })
LINE 1770 | LINE 447 | }
LINE 1771 | LINE 448 | 
LINE 1772 | LINE 449 | const handleImport = async (data) => {
LINE 1773 | LINE 450 |   let successCount = 0
LINE 1774 | LINE 451 |   let errorCount = 0
LINE 1775 | LINE 452 |   importing.value = true
LINE 1776 | LINE 453 | 
LINE 1777 | LINE 454 |   $q.loading.show({
LINE 1778 | LINE 455 |     message: 'Importando productos...',
LINE 1779 | LINE 456 |   })
LINE 1780 | LINE 457 | 
LINE 1781 | LINE 458 |   for (const item of data) {
LINE 1782 | LINE 459 |     try {
LINE 1783 | LINE 460 |       // Mapear nombres a IDs
LINE 1784 | LINE 461 |       const cat = categorias.value.find(
LINE 1785 | LINE 462 |         (c) => c.label.toLowerCase() === item.categoria_nombre?.toLowerCase(),
LINE 1786 | LINE 463 |       )
LINE 1787 | LINE 464 |       const unit = unidades.value.find((u) =>
LINE 1788 | LINE 465 |         u.label.toLowerCase().includes(item.unidad_nombre?.toLowerCase()),
LINE 1789 | LINE 466 |       )
LINE 1790 | LINE 467 |       const state = estados.value.find(
LINE 1791 | LINE 468 |         (e) => e.label.toLowerCase() === item.estado_nombre?.toLowerCase(),
LINE 1792 | LINE 469 |       )
LINE 1793 | LINE 470 |       const measure = medidas.value.find(
LINE 1794 | LINE 471 |         (m) => m.label.toLowerCase() === item.medida_nombre?.toLowerCase(),
LINE 1795 | LINE 472 |       )
LINE 1796 | LINE 473 | 
LINE 1797 | LINE 474 |       const payload = {
LINE 1798 | LINE 475 |         ver: 'registrarProducto',
LINE 1799 | LINE 476 |         idempresa: idempresa,
LINE 1800 | LINE 477 |         codigo: item.codigo || '',
LINE 1801 | LINE 478 |         nombre: item.nombre || '',
LINE 1802 | LINE 479 |         descripcion: item.descripcion || '',
LINE 1803 | LINE 480 |         codigobarras: item.codigobarras || '',
LINE 1804 | LINE 481 |         categoria: cat ? cat.value : null,
LINE 1805 | LINE 482 |         subcategoria: null, // No tenemos mapeo de subcat directo sin contexto de cat en Excel por ahora
LINE 1806 | LINE 483 |         estadoproductos: state ? state.value : estados.value[0]?.value || null,
LINE 1807 | LINE 484 |         unidad: unit ? unit.value : unidades.value[0]?.value || null,
LINE 1808 | LINE 485 |         medida: measure ? measure.value : medidas.value[0]?.value || null,
LINE 1809 | LINE 486 |         caracteristica: item.caracteristica || '',
LINE 1810 | LINE 487 |         codigonandina: item.codigonandina || '',
LINE 1811 | LINE 488 |       }
LINE 1812 | LINE 489 | 
LINE 1813 | LINE 490 |       console.log('Bulk Import saving:', payload)
LINE 1814 | LINE 491 |       const fData = objectToFormData(payload)
LINE 1815 | LINE 492 |       const response = await api.post(``, fData)
LINE 1816 | LINE 493 |       console.log(response.data)
LINE 1817 | LINE 494 |       if (response.data.estado === 'exito') {
LINE 1818 | LINE 495 |         successCount++
LINE 1819 | LINE 496 |       } else {
LINE 1820 | LINE 497 |         errorCount++
LINE 1821 | LINE 498 |       }
LINE 1822 | LINE 499 |     } catch (err) {
LINE 1823 | LINE 500 |       console.error('Error importing product:', err)
LINE 1824 | LINE 501 |       errorCount++
LINE 1825 | LINE 502 |     }
LINE 1826 | LINE 503 |   }
LINE 1827 | LINE 504 | 
LINE 1828 | LINE 505 |   importing.value = false
LINE 1829 | LINE 506 | 
LINE 1830 | LINE 507 |   $q.notify({
LINE 1831 | LINE 508 |     type: successCount > 0 ? 'positive' : 'negative',
LINE 1832 | LINE 509 |     message: `Importación finalizada. Éxito: ${successCount}, Errores: ${errorCount}`,
LINE 1833 | LINE 510 |     position: 'center',
LINE 1834 | LINE 511 |     timeout: 5000,
LINE 1835 | LINE 512 |   })
LINE 1836 | LINE 513 | 
LINE 1837 | LINE 514 |   loadRows()
LINE 1838 | LINE 515 | }
LINE 1839 | LINE 516 | const abrirVariantes = (row) => {
LINE 1840 | LINE 517 |   productoVariantes.value = row
LINE 1841 | LINE 518 |   showVariantesDialog.value = true
LINE 1842 | LINE 519 | }
LINE 1843 | LINE 520 | onMounted(() => {
LINE 1844 | LINE 521 |   loadcategorias()
LINE 1845 | LINE 522 |   loadestados()
LINE 1846 | LINE 523 |   loadmedidas()
LINE 1847 | LINE 524 |   loadsubcategorias()
LINE 1848 | LINE 525 |   loadunidades()
LINE 1849 | LINE 526 |   loadRows()
LINE 1850 | LINE 527 |   if (getTipoFactura(true)) {
LINE 1851 | LINE 528 |     ListaProductoSin()
LINE 1852 | LINE 529 |     ListaUnidadSin()
LINE 1853 | LINE 530 |   }
LINE 1854 | LINE 531 | })
LINE 1855 | LINE 532 | </script>
```

==============================================================
FILE: output/deepseek_prompt.md
==============================================================
```md
LINE   1 | # PROMPT PROFESIONAL PARA DEEPSEEK WEB CHAT
LINE   2 | 
LINE   3 | > **Instrucción para el usuario:** Copia este texto y pégalo directamente en el chat de DeepSeek junto con los archivos adjuntos (`deepseek_project_context.md` o `deepseek_project_context.txt`).
LINE   4 | 
LINE   5 | ==============================================================
LINE   6 | MODO Y PERFIL DE ANÁLISIS SELECCIONADO
LINE   7 | ==============================================================
LINE   8 | • MODO: 🔧 Modo Problema (Problem Mode)
LINE   9 | • PERFIL: 🐞 Detect errors
LINE  10 | • OBJETIVO: Identificar errores de sintaxis, bugs lógicos, excepciones no controladas, condiciones de carrera y fallos de tipo en el código.
LINE  11 | • ENFOQUE: Detección exhaustiva de bugs, casos límite (edge cases), seguridad de nulos/undefined, control de flujo y manejo robusto de excepciones.
LINE  12 | • PRIORIDADES: 1. Crashes y errores que detienen la ejecución. 2. Fallos silenciosos y corrupción de estado. 3. Manejo deficiente de excepciones. 4. Regresiones potenciales.
LINE  13 | • RESULTADO ESPERADO: Localización exacta de cada error (archivo y línea), causa raíz técnica, código corregido listo para copiar/pegar y caso de prueba de verificación.
LINE  14 | 
LINE  15 | ⚠️ REGLA DE CONCRECIÓN TÉCNICA Y ACCIÓN:
LINE  16 | El análisis debe ser CONCRETO, TÉCNICO y ORIENTADO A LA ACCIÓN. Concéntrate exclusivamente en fallos reproducibles y errores verificables. Omite comentarios estilísticos o divagaciones teóricas que no resuelvan un error.
LINE  17 | 
LINE  18 | ==============================================================
LINE  19 | REPORTED PROBLEM / PROBLEMA REPORTADO
LINE  20 | ==============================================================
LINE  21 | generar el codigo en python para hacer el cambio el codigo se creara en la raiz del archivo 
LINE  22 | agregar las columnas a la tabla de producto medida, estadoProducto, unidad, caracteristica 
LINE  23 | la api listaProducto devuelve estos datos 
LINE  24 | [
LINE  25 |     {
LINE  26 |         "id": "4004",
LINE  27 |         "nombre": "BOTIN TREKIN MOTOQUERO PIL",
LINE  28 |         "codigo": "IND-BOT-T-M-P",
LINE  29 |         "descripcion": "BOTIN TREKIN MOTOQUERO PIL",
LINE  30 |         "codigobarras": "",
LINE  31 |         "fecha": "2026-09-03",
LINE  32 |         "imagen": "",
LINE  33 |         "idcategoria": "0",
LINE  34 |         "categoria": null,
LINE  35 |         "subcategoria": "",
LINE  36 |         "idmedida": "234",
LINE  37 |         "medida": "general",
LINE  38 |         "idestadoproducto": "275",
LINE  39 |         "estadoproducto": "Ejecuci\u00f3n",
LINE  40 |         "idunidad": "250",
LINE  41 |         "unidad": "Rollo",
LINE  42 |         "caracteristica": ""{
LINE  43 |         "id": "4004",
LINE  44 |         "nombre": "BOTIN TREKIN MOTOQUERO PIL",
LINE  45 |         "codigo": "IND-BOT-T-M-P",
LINE  46 |         "descripcion": "BOTIN TREKIN MOTOQUERO PIL",
LINE  47 |         "codigobarras": "",
LINE  48 |         "imagen": "",
LINE  49 |         "idcategoria": "0",
LINE  50 |         "categoria": null,
LINE  51 |         "subcategoria": "",
LINE  52 |         "idmedida": "234",
LINE  53 |         "medida": "general",
LINE  54 |         "idestadoproducto": "275",
LINE  55 |         "estadoproducto": "Ejecuci\u00f3n",
LINE  56 |         "idunidad": "250",
LINE  57 |         "unidad": "Rollo",
LINE  58 |         "caracteristica": ""
LINE  59 |     },...
LINE  60 | ]
LINE  61 | 
LINE  62 | ==============================================================
LINE  63 | PROJECT CONTEXT / CONTEXTO E INSTRUCCIONES DEL PROYECTO
LINE  64 | ==============================================================
LINE  65 | Hola DeepSeek. Te adjunto el contexto completo de mi proyecto de software para su análisis técnico profesional bajo el modo "Modo Problema (Problem Mode)".
LINE  66 | 
LINE  67 | ---
LINE  68 | 
LINE  69 | ### 📋 INSTRUCCIONES DE ANÁLISIS (PROBLEM MODE RULES)
LINE  70 | 
LINE  71 | ### 🎯 ENFOQUE DE MODO PROBLEMA (PROBLEM MODE)
LINE  72 | 1. **Foco exclusivo en el problema especificado**: Diagnostica y resuelve directamente la incidencia descrita en "REPORTED PROBLEM".
LINE  73 | 2. **Prioriza la Causa Raíz**: Identifica el origen exacto del fallo técnico antes de proponer cambios de código.
LINE  74 | 3. **Solución quirúrgica y escalable**: Genera el código corregido listo para sustituir sin alterar funcionalidades no relacionadas.
LINE  75 | 4. **Impacto y Efectos Secundarios**: Evalúa regresiones potenciales de la modificación realizada.
LINE  76 | 
LINE  77 | ---
LINE  78 | 
LINE  79 | ### 📐 FORMATO DE RESPUESTA OBLIGATORIO PARA: MODO PROBLEMA (PROBLEM MODE)
LINE  80 | 
LINE  81 | Tu respuesta DEBE seguir **exactamente** la siguiente estructura Markdown adaptada al modo seleccionado. No respondas con JSON. Esta respuesta la leerá un desarrollador directamente desde el chat web.
LINE  82 | 
LINE  83 | ---
LINE  84 | 
LINE  85 | # DIAGNOSIS
LINE  86 | ## Detected Bugs
LINE  87 | [Lista técnica de los bugs encontrados con su causa raíz exacta]
LINE  88 | 
LINE  89 | # FILES TO MODIFY
LINE  90 | ## 1. [ruta/relativa/archivo.ext]
LINE  91 | Approximate line: [número]
LINE  92 | ### Bug Description
LINE  93 | [Explicación concisa del error]
LINE  94 | ### Current Code
LINE  95 | ```
LINE  96 | [código con error]
LINE  97 | ```
LINE  98 | ### Bugfix Code
LINE  99 | ```
LINE 100 | [código corregido listo para sustituir]
LINE 101 | ```
LINE 102 | 
LINE 103 | # VERIFICATION & EDGE CASES
LINE 104 | [Prueba o caso límite para verificar que el bug fue resuelto]
LINE 105 | 
LINE 106 | ---
LINE 107 | 
LINE 108 | ==============================================================
LINE 109 | ATTACHMENTS / ARCHIVOS ADJUNTOS
LINE 110 | ==============================================================
LINE 111 | Por favor revisa el archivo de contexto adjunto (`deepseek_project_context.md` / `deepseek_project_context.txt`) que contiene:
LINE 112 | - **Project Summary**: desglose de archivos seleccionados por extensión y total de líneas.
LINE 113 | - **Dependencies and References**: importaciones y dependencias detectadas automáticamente por archivo.
LINE 114 | - **Estructura del Proyecto**: diagrama en árbol jerárquico de carpetas y archivos.
LINE 115 | - **Código Fuente**: contenido de los archivos seleccionados con sus **rutas relativas** y **números de línea originales** (`LINE X | ...`).
LINE 116 | 
LINE 117 | Confirma la recepción del contexto y responde siguiendo **exactamente** el formato estructurado indicado arriba.
```

==============================================================
FILE: output/etapas_produccion_export_2026-08-27_105739.sql
==============================================================
```sql
LINE  1 | insert into `etapas_produccion` (`detalle`, `empresa_idempresa`, `idetapas_produccion`, `nombre_etapa`, `rubro_idrubro`, `seccion_idseccion`) values ('Detalles de producción', 50, 24, 'Etapa producción 1', 17, 83);
LINE  2 | insert into `etapas_produccion` (`detalle`, `empresa_idempresa`, `idetapas_produccion`, `nombre_etapa`, `rubro_idrubro`, `seccion_idseccion`) values ('Detalle producción', 50, 25, 'Etapa producción 2', 17, 83);
LINE  3 | insert into `etapas_produccion` (`detalle`, `empresa_idempresa`, `idetapas_produccion`, `nombre_etapa`, `rubro_idrubro`, `seccion_idseccion`) values ('Tostado de granos según el tipo de café a obtener, considerando la twmperatura de inicio y evaluandi la evolución de temp durante todo el proceso de tostado.', 74, 27, 'Tostado', 21, 88);
LINE  4 | insert into `etapas_produccion` (`detalle`, `empresa_idempresa`, `idetapas_produccion`, `nombre_etapa`, `rubro_idrubro`, `seccion_idseccion`) values ('Proceso de molido según el tipo de producto, marca. Previa verificación la granulometría cprrecta.', 74, 28, 'Molido', 21, 88);
LINE  5 | insert into `etapas_produccion` (`detalle`, `empresa_idempresa`, `idetapas_produccion`, `nombre_etapa`, `rubro_idrubro`, `seccion_idseccion`) values ('Colocado cada producto procesado en los envases correctos (marca, peso y tipo producto).', 74, 29, 'Envasado', 21, 88);
LINE  6 | insert into `etapas_produccion` (`detalle`, `empresa_idempresa`, `idetapas_produccion`, `nombre_etapa`, `rubro_idrubro`, `seccion_idseccion`) values ('Tostado de granos', 75, 31, 'Tostado', 19, 99);
LINE  7 | insert into `etapas_produccion` (`detalle`, `empresa_idempresa`, `idetapas_produccion`, `nombre_etapa`, `rubro_idrubro`, `seccion_idseccion`) values ('Molido de granos', 75, 32, 'Molido', 19, 99);
LINE  8 | insert into `etapas_produccion` (`detalle`, `empresa_idempresa`, `idetapas_produccion`, `nombre_etapa`, `rubro_idrubro`, `seccion_idseccion`) values ('Envaso de producto terminado', 75, 33, 'Envasado', 19, 99);
LINE  9 | insert into `etapas_produccion` (`detalle`, `empresa_idempresa`, `idetapas_produccion`, `nombre_etapa`, `rubro_idrubro`, `seccion_idseccion`) values ('Tratamientos térmicos (cocción, ahumado, escaldado), secado y maduración, y finalmente enfriamiento y envasado para distribución, variando según el producto final (frescos, cocidos, curados)', 75, 34, 'Procesado', 27, 105);
LINE 10 | insert into `etapas_produccion` (`detalle`, `empresa_idempresa`, `idetapas_produccion`, `nombre_etapa`, `rubro_idrubro`, `seccion_idseccion`) values ('Sección encargada del envasado o encapacado de los productos.', 75, 35, 'Envasado', 27, 105);
LINE 11 | insert into `etapas_produccion` (`detalle`, `empresa_idempresa`, `idetapas_produccion`, `nombre_etapa`, `rubro_idrubro`, `seccion_idseccion`) values ('Sección de producción: preparación de materia prima (recepción, troceado, deshuesado, molido), mezclado y adición de condimentos, embutido (relleno en tripas).', 75, 36, 'Preparado Ingredientes', 27, 105);
LINE 12 | insert into `etapas_produccion` (`detalle`, `empresa_idempresa`, `idetapas_produccion`, `nombre_etapa`, `rubro_idrubro`, `seccion_idseccion`) values ('empaquetado', 75, 37, 'empaquetado', 19, 100);
LINE 13 | insert into `etapas_produccion` (`detalle`, `empresa_idempresa`, `idetapas_produccion`, `nombre_etapa`, `rubro_idrubro`, `seccion_idseccion`) values ('produccion', 75, 38, 'producion', 19, 99);
LINE 14 | insert into `etapas_produccion` (`detalle`, `empresa_idempresa`, `idetapas_produccion`, `nombre_etapa`, `rubro_idrubro`, `seccion_idseccion`) values ('Corte del cuero', 75, 39, 'Corte', 29, 110);
LINE 15 | insert into `etapas_produccion` (`detalle`, `empresa_idempresa`, `idetapas_produccion`, `nombre_etapa`, `rubro_idrubro`, `seccion_idseccion`) values ('Pegado y sellado de los calzados', 75, 40, 'Pegado y sellado', 29, 110);
LINE 16 | insert into `etapas_produccion` (`detalle`, `empresa_idempresa`, `idetapas_produccion`, `nombre_etapa`, `rubro_idrubro`, `seccion_idseccion`) values ('Etapa final', 75, 41, 'Pintado y pulido', 29, 110);
LINE 17 | insert into `etapas_produccion` (`detalle`, `empresa_idempresa`, `idetapas_produccion`, `nombre_etapa`, `rubro_idrubro`, `seccion_idseccion`) values ('Cortado de material', 119, 42, 'Cortado', 31, 113);
LINE 18 | insert into `etapas_produccion` (`detalle`, `empresa_idempresa`, `idetapas_produccion`, `nombre_etapa`, `rubro_idrubro`, `seccion_idseccion`) values ('Formación de huellas', 75, 43, 'Fundido de goma', 29, 109);
LINE 19 | insert into `etapas_produccion` (`detalle`, `empresa_idempresa`, `idetapas_produccion`, `nombre_etapa`, `rubro_idrubro`, `seccion_idseccion`) values ('Bordeado de plantillas', 75, 44, 'Afinación de acabado', 29, 109);
LINE 20 | insert into `etapas_produccion` (`detalle`, `empresa_idempresa`, `idetapas_produccion`, `nombre_etapa`, `rubro_idrubro`, `seccion_idseccion`) values ('Aparado de partes', 119, 45, 'Aparado', 31, 113);
LINE 21 | insert into `etapas_produccion` (`detalle`, `empresa_idempresa`, `idetapas_produccion`, `nombre_etapa`, `rubro_idrubro`, `seccion_idseccion`) values ('Conformado del calzado', 119, 46, 'Conformado', 31, 113);
LINE 22 | insert into `etapas_produccion` (`detalle`, `empresa_idempresa`, `idetapas_produccion`, `nombre_etapa`, `rubro_idrubro`, `seccion_idseccion`) values ('Solado del calzado', 119, 47, 'Solado', 31, 113);
LINE 23 | insert into `etapas_produccion` (`detalle`, `empresa_idempresa`, `idetapas_produccion`, `nombre_etapa`, `rubro_idrubro`, `seccion_idseccion`) values ('Afinado de detalles', 119, 48, 'Terminado', 31, 113);
LINE 24 | insert into `etapas_produccion` (`detalle`, `empresa_idempresa`, `idetapas_produccion`, `nombre_etapa`, `rubro_idrubro`, `seccion_idseccion`) values ('Corte de piezas según modelo y talla', 50, 49, 'Corte', 33, 116);
LINE 25 | insert into `etapas_produccion` (`detalle`, `empresa_idempresa`, `idetapas_produccion`, `nombre_etapa`, `rubro_idrubro`, `seccion_idseccion`) values ('Costura y unión de piezas', 50, 50, 'Aparado', 33, 117);
LINE 26 | insert into `etapas_produccion` (`detalle`, `empresa_idempresa`, `idetapas_produccion`, `nombre_etapa`, `rubro_idrubro`, `seccion_idseccion`) values ('Conformado de puntera y talón', 50, 51, 'Conformado ', 33, 118);
LINE 27 | insert into `etapas_produccion` (`detalle`, `empresa_idempresa`, `idetapas_produccion`, `nombre_etapa`, `rubro_idrubro`, `seccion_idseccion`) values ('Preparación, pegado y prensado de suela', 50, 52, 'Solado', 33, 119);
LINE 28 | insert into `etapas_produccion` (`detalle`, `empresa_idempresa`, `idetapas_produccion`, `nombre_etapa`, `rubro_idrubro`, `seccion_idseccion`) values ('Limpieza, acabado, empaque y liberación', 50, 53, 'Terminado', 33, 120);
```

==============================================================
FILE: parche_quasar.py
==============================================================
```py
LINE   1 | #!/usr/bin/env python3
LINE   2 | # -*- coding: utf-8 -*-
LINE   3 | """
LINE   4 | parche_quasar.py  (v2 - sin regex)
LINE   5 | Añade resolución de alias Quasar/Vue a app/core/dependency_graph.py
LINE   6 | """
LINE   7 | import argparse
LINE   8 | import shutil
LINE   9 | import sys
LINE  10 | from datetime import datetime
LINE  11 | from pathlib import Path
LINE  12 | 
LINE  13 | 
LINE  14 | NEW_RESOLVER = '''    def _resolve_js_dep(self, source_rel: str, dep: str) -> List[str]:
LINE  15 |         m = re.search(r'[\\'"]([^\\'"]+)[\\'"]', dep)
LINE  16 |         if not m:
LINE  17 |             return []
LINE  18 | 
LINE  19 |         raw = m.group(1).strip()
LINE  20 | 
LINE  21 |         # 1. Import relativo: "./x" o "../x"
LINE  22 |         if raw.startswith("."):
LINE  23 |             base_dir = os.path.dirname(source_rel)
LINE  24 |             target = os.path.normpath(os.path.join(base_dir, raw)).replace("\\\\", "/")
LINE  25 |             return self._js_candidates(target)
LINE  26 | 
LINE  27 |         # 2. Import con alias Quasar / Vue CLI / Vite
LINE  28 |         alias_targets = self._resolve_js_alias(raw)
LINE  29 |         for target in alias_targets:
LINE  30 |             hits = self._js_candidates(target)
LINE  31 |             if hits:
LINE  32 |                 return hits
LINE  33 | 
LINE  34 |         # 3. Fallback: probar como ruta relativa al folder_path
LINE  35 |         if "/" in raw:
LINE  36 |             hits = self._js_candidates(raw)
LINE  37 |             if hits:
LINE  38 |                 return hits
LINE  39 | 
LINE  40 |         # 4. Import externo (vue, quasar, axios, @quasar/app, ...)
LINE  41 |         return []
LINE  42 | 
LINE  43 |     def _resolve_js_alias(self, raw: str) -> List[str]:
LINE  44 |         """
LINE  45 |         Devuelve rutas base candidatas (relativas al folder_path) para un import
LINE  46 |         con alias. Se prueban varias variantes porque no sabemos si el usuario
LINE  47 |         seleccionó la raíz del proyecto (con src/) o el propio src/.
LINE  48 |         """
LINE  49 |         aliases = {
LINE  50 |             "src/":         ["src/", ""],
LINE  51 |             "@/":           ["src/", ""],
LINE  52 |             "app/":         ["src/", ""],
LINE  53 |             "components/":  ["src/components/", "components/"],
LINE  54 |             "layouts/":     ["src/layouts/",    "layouts/"],
LINE  55 |             "pages/":       ["src/pages/",      "pages/"],
LINE  56 |             "assets/":      ["src/assets/",     "assets/"],
LINE  57 |             "boot/":        ["src/boot/",       "boot/"],
LINE  58 |             "stores/":      ["src/stores/",     "stores/"],
LINE  59 |             "router/":      ["src/router/",     "router/"],
LINE  60 |             "composables/": ["src/composables/","composables/"],
LINE  61 |             "mixins/":      ["src/mixins/",     "mixins/"],
LINE  62 |             "directives/":  ["src/directives/", "directives/"],
LINE  63 |             "plugins/":     ["src/plugins/",    "plugins/"],
LINE  64 |             "services/":    ["src/services/",   "services/"],
LINE  65 |             "helpers/":     ["src/helpers/",    "helpers/"],
LINE  66 |         }
LINE  67 |         for alias, prefixes in aliases.items():
LINE  68 |             if raw.startswith(alias):
LINE  69 |                 rest = raw[len(alias):]
LINE  70 |                 return [p + rest for p in prefixes]
LINE  71 |         return []
LINE  72 | 
LINE  73 |     def _js_candidates(self, target: str) -> List[str]:
LINE  74 |         """Prueba target + extensiones y target/index.<ext> contra el índice."""
LINE  75 |         target = self._normalize(target)
LINE  76 |         out = []
LINE  77 |         for ext in ("", ".js", ".jsx", ".ts", ".tsx", ".vue", ".json", ".mjs", ".cjs"):
LINE  78 |             cand = target + ext
LINE  79 |             if cand in self._file_index:
LINE  80 |                 out.append(cand)
LINE  81 |         for ext in (".js", ".jsx", ".ts", ".tsx", ".vue"):
LINE  82 |             cand = target + "/index" + ext
LINE  83 |             if cand in self._file_index:
LINE  84 |                 out.append(cand)
LINE  85 |         seen = set()
LINE  86 |         result = []
LINE  87 |         for c in out:
LINE  88 |             if c not in seen:
LINE  89 |                 seen.add(c)
LINE  90 |                 result.append(c)
LINE  91 |         return result
LINE  92 | '''
LINE  93 | 
LINE  94 | 
LINE  95 | def log(msg, level="INFO"):
LINE  96 |     prefix = {"INFO": "[INFO]", "OK": "[ OK ]", "WARN": "[WARN]",
LINE  97 |               "ERR": "[FAIL]", "SKIP": "[SKIP]"}.get(level, "[INFO]")
LINE  98 |     print(f"{prefix} {msg}")
LINE  99 | 
LINE 100 | 
LINE 101 | def find_method_range(text: str, method_name: str) -> tuple:
LINE 102 |     """
LINE 103 |     Encuentra (start, end) del bloque del método `method_name` dentro de la clase.
LINE 104 |     El método debe estar indentado con 4 espacios.
LINE 105 |     Devuelve (-1, -1) si no se encuentra.
LINE 106 |     """
LINE 107 |     header = f"    def {method_name}("
LINE 108 |     start = text.find(header)
LINE 109 |     if start == -1:
LINE 110 |         return -1, -1
LINE 111 | 
LINE 112 |     # Buscar siguiente '    def ' (4 espacios + def) después de la línea del header
LINE 113 |     first_nl = text.find("\n", start)
LINE 114 |     if first_nl == -1:
LINE 115 |         return -1, -1
LINE 116 | 
LINE 117 |     search_from = first_nl + 1
LINE 118 |     next_def = text.find("\n    def ", search_from)
LINE 119 |     if next_def == -1:
LINE 120 |         # Es el último método del archivo
LINE 121 |         end = len(text)
LINE 122 |     else:
LINE 123 |         end = next_def + 1  # conservar el \n inicial del siguiente método
LINE 124 | 
LINE 125 |     return start, end
LINE 126 | 
LINE 127 | 
LINE 128 | def patch_file(path: Path, dry_run: bool = False) -> bool:
LINE 129 |     text = path.read_text(encoding="utf-8")
LINE 130 | 
LINE 131 |     if "_resolve_js_alias" in text and "_js_candidates" in text:
LINE 132 |         log("El parche Quasar ya está aplicado.", "SKIP")
LINE 133 |         return True
LINE 134 | 
LINE 135 |     start, end = find_method_range(text, "_resolve_js_dep")
LINE 136 |     if start == -1:
LINE 137 |         log("No se localizó 'def _resolve_js_dep' con indentación de 4 espacios.", "ERR")
LINE 138 |         log("Verifica que dependency_graph.py existe y tiene ese método.", "ERR")
LINE 139 |         return False
LINE 140 | 
LINE 141 |     log(f"Rango detectado: {start}..{end} ({end - start} caracteres)")
LINE 142 |     old_block = text[start:end]
LINE 143 |     log(f"Primera línea del bloque: {old_block.splitlines()[0]!r}")
LINE 144 | 
LINE 145 |     new_text = text[:start] + NEW_RESOLVER + "\n" + text[end:]
LINE 146 | 
LINE 147 |     try:
LINE 148 |         compile(new_text, str(path), "exec")
LINE 149 |     except SyntaxError as e:
LINE 150 |         log(f"Sintaxis inválida tras el parche: línea {e.lineno}: {e.msg}", "ERR")
LINE 151 |         lines = new_text.split("\n")
LINE 152 |         for i in range(max(0, e.lineno - 4), min(len(lines), e.lineno + 3)):
LINE 153 |             marker = ">>>" if i == e.lineno - 1 else "   "
LINE 154 |             print(f"  {marker} {i+1:5d} | {lines[i]}")
LINE 155 |         return False
LINE 156 | 
LINE 157 |     if dry_run:
LINE 158 |         log("(dry-run) dependency_graph.py se puede parchear correctamente", "SKIP")
LINE 159 |         return True
LINE 160 | 
LINE 161 |     ts = datetime.now().strftime("%Y%m%d_%H%M%S")
LINE 162 |     bak = path.with_name(path.name + f".{ts}.bak")
LINE 163 |     shutil.copy2(path, bak)
LINE 164 |     log(f"Respaldo: {bak}", "OK")
LINE 165 | 
LINE 166 |     path.write_text(new_text, encoding="utf-8")
LINE 167 |     log(f"Parcheado: {path}", "OK")
LINE 168 |     return True
LINE 169 | 
LINE 170 | 
LINE 171 | def main():
LINE 172 |     ap = argparse.ArgumentParser(description="Parche Quasar/Vue para dependency_graph.py")
LINE 173 |     ap.add_argument("root", nargs="?", default=".", help="Raíz del proyecto")
LINE 174 |     ap.add_argument("--dry-run", action="store_true")
LINE 175 |     args = ap.parse_args()
LINE 176 | 
LINE 177 |     root = Path(args.root).resolve()
LINE 178 |     target = root / "app" / "core" / "dependency_graph.py"
LINE 179 |     if not target.is_file():
LINE 180 |         log(f"No existe: {target}", "ERR")
LINE 181 |         sys.exit(1)
LINE 182 | 
LINE 183 |     log(f"Raíz: {root}")
LINE 184 |     log(f"Target: {target}")
LINE 185 |     log(f"Dry-run: {args.dry_run}")
LINE 186 |     print()
LINE 187 | 
LINE 188 |     if patch_file(target, dry_run=args.dry_run):
LINE 189 |         log("=== Listo. Reinicia la GUI y vuelve a probar el árbol de dependencias ===", "OK")
LINE 190 |     else:
LINE 191 |         sys.exit(1)
LINE 192 | 
LINE 193 | 
LINE 194 | if __name__ == "__main__":
LINE 195 |     main()
```

==============================================================
FILE: reparar.py
==============================================================
```py
LINE   1 | #!/usr/bin/env python3
LINE   2 | # -*- coding: utf-8 -*-
LINE   3 | """
LINE   4 | reparar.py
LINE   5 | Repara app/gui/main_window.py después de la inserción incorrecta
LINE   6 | del bloque auto-generado por apply_changes.py.
LINE   7 | 
LINE   8 | Uso:
LINE   9 |     python reparar.py                    # usa el directorio actual
LINE  10 |     python reparar.py /ruta/al/agente
LINE  11 |     python reparar.py --dry-run          # solo muestra
LINE  12 | """
LINE  13 | 
LINE  14 | import argparse
LINE  15 | import shutil
LINE  16 | import sys
LINE  17 | from datetime import datetime
LINE  18 | from pathlib import Path
LINE  19 | 
LINE  20 | 
LINE  21 | ANCHOR      = "    def on_copy_clipboard(self):\n"
LINE  22 | START_MARK  = "    # === AUTO-GENERATED: file_search_dependency_feature ===\n"
LINE  23 | END_MARK    = "    # === END AUTO-GENERATED ===\n"
LINE  24 | 
LINE  25 | 
LINE  26 | def log(msg, level="INFO"):
LINE  27 |     prefix = {"INFO": "[INFO]", "OK": "[ OK ]", "WARN": "[WARN]",
LINE  28 |               "ERR": "[FAIL]", "SKIP": "[SKIP]"}.get(level, "[INFO]")
LINE  29 |     print(f"{prefix} {msg}")
LINE  30 | 
LINE  31 | 
LINE  32 | def check_syntax(path: Path, src: str) -> bool:
LINE  33 |     try:
LINE  34 |         compile(src, str(path), "exec")
LINE  35 |         return True
LINE  36 |     except SyntaxError as e:
LINE  37 |         log(f"Sintaxis inválida en {path.name} línea {e.lineno}: {e.msg}", "ERR")
LINE  38 |         lines = src.split("\n")
LINE  39 |         for i in range(max(0, e.lineno - 4), min(len(lines), e.lineno + 3)):
LINE  40 |             marker = ">>>" if i == e.lineno - 1 else "   "
LINE  41 |             print(f"  {marker} {i+1:4d} | {lines[i]}")
LINE  42 |         return False
LINE  43 | 
LINE  44 | 
LINE  45 | def repair_main_window(root: Path, dry_run: bool = False) -> bool:
LINE  46 |     mw = root / "app" / "gui" / "main_window.py"
LINE  47 |     if not mw.is_file():
LINE  48 |         log(f"No existe: {mw}", "ERR")
LINE  49 |         return False
LINE  50 | 
LINE  51 |     text = mw.read_text(encoding="utf-8")
LINE  52 | 
LINE  53 |     # 1. Localizar el anchor
LINE  54 |     anchor_pos = text.find(ANCHOR)
LINE  55 |     if anchor_pos == -1:
LINE  56 |         log("No se encontró 'def on_copy_clipboard'", "WARN")
LINE  57 |         return check_syntax(mw, text)
LINE  58 | 
LINE  59 |     after_anchor = anchor_pos + len(ANCHOR)
LINE  60 | 
LINE  61 |     # 2. Verificar si el bloque está justo después (mal ubicado)
LINE  62 |     start_pos = text.find(START_MARK, after_anchor)
LINE  63 |     if start_pos == -1:
LINE  64 |         log("No hay bloque auto-generado tras on_copy_clipboard. Nada que reparar.", "SKIP")
LINE  65 |         return check_syntax(mw, text)
LINE  66 | 
LINE  67 |     between = text[after_anchor:start_pos]
LINE  68 |     if between.strip() != "":
LINE  69 |         log(f"Contenido inesperado entre anchor y bloque: {between!r}", "WARN")
LINE  70 |         return check_syntax(mw, text)
LINE  71 | 
LINE  72 |     # 3. Localizar fin del bloque
LINE  73 |     end_pos = text.find(END_MARK, start_pos)
LINE  74 |     if end_pos == -1:
LINE  75 |         log("No se encontró el marcador de fin del bloque", "ERR")
LINE  76 |         return False
LINE  77 |     end_pos += len(END_MARK)
LINE  78 | 
LINE  79 |     block = text[start_pos:end_pos]
LINE  80 | 
LINE  81 |     # 4. Eliminar el bloque y el relleno que había entre anchor y bloque
LINE  82 |     text = text[:after_anchor] + text[end_pos:]
LINE  83 | 
LINE  84 |     # 5. Insertar el bloque ANTES del anchor
LINE  85 |     new_anchor_pos = text.find(ANCHOR)
LINE  86 |     if new_anchor_pos == -1:
LINE  87 |         log("Se perdió el anchor tras la extracción", "ERR")
LINE  88 |         return False
LINE  89 | 
LINE  90 |     insertion = block
LINE  91 |     if not insertion.endswith("\n"):
LINE  92 |         insertion += "\n"
LINE  93 |     text = text[:new_anchor_pos] + insertion + "\n" + text[new_anchor_pos:]
LINE  94 | 
LINE  95 |     # 6. Verificar sintaxis antes de escribir
LINE  96 |     if not check_syntax(mw, text):
LINE  97 |         return False
LINE  98 | 
LINE  99 |     if dry_run:
LINE 100 |         log("(dry-run) main_window.py se puede reparar correctamente", "SKIP")
LINE 101 |         return True
LINE 102 | 
LINE 103 |     # 7. Backup + escritura
LINE 104 |     ts = datetime.now().strftime("%Y%m%d_%H%M%S")
LINE 105 |     bak = mw.with_name(mw.name + f".{ts}.bak")
LINE 106 |     shutil.copy2(mw, bak)
LINE 107 |     log(f"Respaldo: {bak}", "OK")
LINE 108 | 
LINE 109 |     mw.write_text(text, encoding="utf-8")
LINE 110 |     log(f"Reparado: {mw}", "OK")
LINE 111 |     return True
LINE 112 | 
LINE 113 | 
LINE 114 | def main():
LINE 115 |     parser = argparse.ArgumentParser(description="Repara main_window.py")
LINE 116 |     parser.add_argument("root", nargs="?", default=".", help="Raíz del proyecto")
LINE 117 |     parser.add_argument("--dry-run", action="store_true")
LINE 118 |     args = parser.parse_args()
LINE 119 | 
LINE 120 |     root = Path(args.root).resolve()
LINE 121 |     if not (root / "app" / "gui" / "main_window.py").is_file():
LINE 122 |         log(f"No parece ser la raíz del proyecto: {root}", "ERR")
LINE 123 |         sys.exit(1)
LINE 124 | 
LINE 125 |     log(f"Raíz: {root}")
LINE 126 |     log(f"Dry-run: {args.dry_run}")
LINE 127 |     print()
LINE 128 | 
LINE 129 |     if repair_main_window(root, dry_run=args.dry_run):
LINE 130 |         log("=== Listo. Ejecuta ./iniciar_deepseek_debugger.sh ===", "OK")
LINE 131 |     else:
LINE 132 |         log("=== La reparación falló. Revisa el archivo manualmente ===", "ERR")
LINE 133 |         sys.exit(1)
LINE 134 | 
LINE 135 | 
LINE 136 | if __name__ == "__main__":
LINE 137 |     main()
```

==============================================================
FILE: requirements.txt
==============================================================
```txt
LINE 1 | # No third-party API dependencies required.
LINE 2 | # Built-in Python standard libraries (tkinter, pathlib, os, json, re) are used.
```

==============================================================
FILE: resume_phase1_sqlite.py
==============================================================
```py
LINE   1 | #!/usr/bin/env python3
LINE   2 | # -*- coding: utf-8 -*-
LINE   3 | """
LINE   4 | resume_phase1_sqlite.py
LINE   5 | 
LINE   6 | Completa los 3 cambios pendientes de la Fase 1 (SQLite) que quedaron sin
LINE   7 | aplicar tras el error de anclaje en main_window.py:
LINE   8 | 
LINE   9 |   4. Método _on_tree_check_change (persistencia de checkbox)
LINE  10 |   5. Restaurar is_checked en reload_tree()
LINE  11 |   6. Persistir tras el análisis en on_analyze_project()
LINE  12 | 
LINE  13 | Uso:
LINE  14 |     python3 resume_phase1_sqlite.py /ruta/al/proyecto
LINE  15 |     python3 resume_phase1_sqlite.py                 # directorio actual
LINE  16 | 
LINE  17 | Características:
LINE  18 |   * Idempotente: si un cambio ya está aplicado, se omite con [SKIP].
LINE  19 |   * Crea backup en .backup/ conservando la ruta relativa.
LINE  20 |   * Valida la sintaxis final con py_compile.
LINE  21 |   * Solo biblioteca estándar.
LINE  22 | """
LINE  23 | import argparse
LINE  24 | import shutil
LINE  25 | import sys
LINE  26 | import py_compile
LINE  27 | from datetime import datetime
LINE  28 | from pathlib import Path
LINE  29 | 
LINE  30 | 
LINE  31 | BACKUP_DIRNAME = ".backup"
LINE  32 | MAIN_WINDOW_REL = "app/gui/main_window.py"
LINE  33 | 
LINE  34 | 
LINE  35 | # ---------------------------------------------------------------------------
LINE  36 | # Bloques a insertar (idénticos a los del script original)
LINE  37 | # ---------------------------------------------------------------------------
LINE  38 | 
LINE  39 | MW_METHOD_BLOCK = '''    # === PERSISTENCE: PHASE1 (method) ===
LINE  40 |     def _on_tree_check_change(self, rel_path: str, is_checked: bool):
LINE  41 |         """Persist checkbox changes to SQLite (Phase 1)."""
LINE  42 |         if self._persist_db is None:
LINE  43 |             return
LINE  44 |         folder = self.var_folder.get()
LINE  45 |         if not folder:
LINE  46 |             return
LINE  47 |         try:
LINE  48 |             project_id = self._persist_db.get_or_create_project(folder)
LINE  49 |             self._persist_db.update_is_checked(project_id, rel_path, is_checked)
LINE  50 |         except Exception:
LINE  51 |             pass
LINE  52 |     # === END PERSISTENCE: PHASE1 (method) ===
LINE  53 | '''
LINE  54 | 
LINE  55 | MW_RELOAD_BLOCK = '''        # === PERSISTENCE: PHASE1 (reload) ===
LINE  56 |         if self._persist_db is not None:
LINE  57 |             try:
LINE  58 |                 saved = self._persist_db.load_checked_state(folder)
LINE  59 |                 if saved is not None:
LINE  60 |                     self.tree.set_checked_files(saved)
LINE  61 |                     self.selector.set_checked_folder_files(
LINE  62 |                         self.tree.get_checked_files()
LINE  63 |                     )
LINE  64 |             except Exception:
LINE  65 |                 pass
LINE  66 |         # === END PERSISTENCE: PHASE1 (reload) ===
LINE  67 | '''
LINE  68 | 
LINE  69 | MW_ANALYZE_BLOCK = '''        # === PERSISTENCE: PHASE1 (analyze) ===
LINE  70 |         try:
LINE  71 |             analyzer.persist_result(result)
LINE  72 |         except Exception:
LINE  73 |             pass
LINE  74 |         # === END PERSISTENCE: PHASE1 (analyze) ===
LINE  75 | '''
LINE  76 | 
LINE  77 | 
LINE  78 | # ---------------------------------------------------------------------------
LINE  79 | # Anclas 100 % ASCII (sin box-drawing characters)
LINE  80 | # ---------------------------------------------------------------------------
LINE  81 | 
LINE  82 | ANCHOR_METHOD  = "    def on_select_folder(self):"
LINE  83 | ANCHOR_RELOAD  = (
LINE  84 |     '                rel_file = os.path.join(rel_dir, f) if rel_dir != "." else f\n'
LINE  85 |     '                self.tree.insert_file(parent_item, rel_file)'
LINE  86 | )
LINE  87 | ANCHOR_ANALYZE = "        result = analyzer.analyze(folder, max_file_size_mb=max_file_mb)"
LINE  88 | 
LINE  89 | 
LINE  90 | # ---------------------------------------------------------------------------
LINE  91 | # Helpers
LINE  92 | # ---------------------------------------------------------------------------
LINE  93 | 
LINE  94 | def log(level, msg):
LINE  95 |     print(f"[{level}] {msg}")
LINE  96 | 
LINE  97 | 
LINE  98 | def backup(root: Path, rel: str) -> None:
LINE  99 |     src = root / rel
LINE 100 |     if not src.is_file():
LINE 101 |         return
LINE 102 |     dst = root / BACKUP_DIRNAME / rel
LINE 103 |     dst.parent.mkdir(parents=True, exist_ok=True)
LINE 104 |     shutil.copy2(src, dst)
LINE 105 |     log("INFO", f"Backup creado: {dst.relative_to(root)}")
LINE 106 | 
LINE 107 | 
LINE 108 | def insert_before(root: Path, rel: str, anchor: str, block: str, marker: str) -> None:
LINE 109 |     p = root / rel
LINE 110 |     content = p.read_text(encoding="utf-8")
LINE 111 |     if marker in content:
LINE 112 |         log("SKIP", f"Cambio ya aplicado: {rel} ({marker.strip()})")
LINE 113 |         return
LINE 114 |     idx = content.find(anchor)
LINE 115 |     if idx == -1:
LINE 116 |         raise RuntimeError(f"Ancla no encontrada en {rel}:\n  {anchor!r}")
LINE 117 |     new = content[:idx] + block + "\n" + content[idx:]
LINE 118 |     backup(root, rel)
LINE 119 |     p.write_text(new, encoding="utf-8")
LINE 120 |     log("OK", f"Cambio aplicado: {rel}  ({marker.strip()})")
LINE 121 | 
LINE 122 | 
LINE 123 | def insert_after(root: Path, rel: str, anchor: str, block: str, marker: str) -> None:
LINE 124 |     p = root / rel
LINE 125 |     content = p.read_text(encoding="utf-8")
LINE 126 |     if marker in content:
LINE 127 |         log("SKIP", f"Cambio ya aplicado: {rel} ({marker.strip()})")
LINE 128 |         return
LINE 129 |     idx = content.find(anchor)
LINE 130 |     if idx == -1:
LINE 131 |         raise RuntimeError(f"Ancla no encontrada en {rel}:\n  {anchor!r}")
LINE 132 |     end = idx + len(anchor)
LINE 133 |     new = content[:end] + "\n" + block + content[end:]
LINE 134 |     backup(root, rel)
LINE 135 |     p.write_text(new, encoding="utf-8")
LINE 136 |     log("OK", f"Cambio aplicado: {rel}  ({marker.strip()})")
LINE 137 | 
LINE 138 | 
LINE 139 | # ---------------------------------------------------------------------------
LINE 140 | # Main
LINE 141 | # ---------------------------------------------------------------------------
LINE 142 | 
LINE 143 | def main() -> int:
LINE 144 |     parser = argparse.ArgumentParser(
LINE 145 |         description="Reanuda los cambios pendientes de la Fase 1 (SQLite)."
LINE 146 |     )
LINE 147 |     parser.add_argument("root", nargs="?", default=".",
LINE 148 |                         help="Ruta raíz del proyecto (por defecto: directorio actual).")
LINE 149 |     args = parser.parse_args()
LINE 150 | 
LINE 151 |     root = Path(args.root).resolve()
LINE 152 |     mw = root / MAIN_WINDOW_REL
LINE 153 |     if not mw.is_file():
LINE 154 |         log("ERROR", f"No existe {mw}")
LINE 155 |         return 1
LINE 156 | 
LINE 157 |     log("INFO", f"Proyecto detectado: {root}")
LINE 158 |     log("INFO", f"Inicio: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
LINE 159 |     print()
LINE 160 | 
LINE 161 |     try:
LINE 162 |         # 4. Método _on_tree_check_change (antes de los UI event handlers)
LINE 163 |         insert_before(
LINE 164 |             root, MAIN_WINDOW_REL,
LINE 165 |             anchor=ANCHOR_METHOD,
LINE 166 |             block=MW_METHOD_BLOCK,
LINE 167 |             marker="# === PERSISTENCE: PHASE1 (method) ===",
LINE 168 |         )
LINE 169 | 
LINE 170 |         # 5. Restaurar estado tras cargar el árbol
LINE 171 |         insert_after(
LINE 172 |             root, MAIN_WINDOW_REL,
LINE 173 |             anchor=ANCHOR_RELOAD,
LINE 174 |             block=MW_RELOAD_BLOCK,
LINE 175 |             marker="# === PERSISTENCE: PHASE1 (reload) ===",
LINE 176 |         )
LINE 177 | 
LINE 178 |         # 6. Persistir tras el análisis
LINE 179 |         insert_after(
LINE 180 |             root, MAIN_WINDOW_REL,
LINE 181 |             anchor=ANCHOR_ANALYZE,
LINE 182 |             block=MW_ANALYZE_BLOCK,
LINE 183 |             marker="# === PERSISTENCE: PHASE1 (analyze) ===",
LINE 184 |         )
LINE 185 |     except Exception as exc:
LINE 186 |         log("ERROR", str(exc))
LINE 187 |         print()
LINE 188 |         log("INFO", "Proceso detenido. No se continúan aplicando cambios.")
LINE 189 |         return 1
LINE 190 | 
LINE 191 |     print()
LINE 192 |     log("INFO", "--- Validando sintaxis (py_compile) ---")
LINE 193 |     try:
LINE 194 |         py_compile.compile(str(mw), doraise=True)
LINE 195 |         log("OK", f"Sintaxis OK: {MAIN_WINDOW_REL}")
LINE 196 |     except py_compile.PyCompileError as exc:
LINE 197 |         log("ERROR", f"Sintaxis inválida en {MAIN_WINDOW_REL}: {exc}")
LINE 198 |         return 1
LINE 199 | 
LINE 200 |     print()
LINE 201 |     log("INFO", "Fase 1 completada. Reinicia la aplicación para probar.")
LINE 202 |     return 0
LINE 203 | 
LINE 204 | 
LINE 205 | if __name__ == "__main__":
LINE 206 |     sys.exit(main())
```

==============================================================
FILE: run.bat
==============================================================
```bat
LINE 1 | @echo off
LINE 2 | cd /d "%~dp0"
LINE 3 | call "%~dp0ejecutar.bat"
```

==============================================================
FILE: tests/test_analysis_modes.py
==============================================================
```py
LINE   1 | """Tests for Analysis Modes (Problem Mode & Project Mode)."""
LINE   2 | import unittest
LINE   3 | from app.models.analysis_modes import (
LINE   4 |     MODE_PROBLEM, MODE_PROJECT, ANALYSIS_MODES,
LINE   5 |     get_analysis_mode_config, AnalysisModeConfig,
LINE   6 | )
LINE   7 | from app.models.project import ExportConfig, ProjectSelection
LINE   8 | from app.generators.standalone_prompt_generator import generate_standalone_prompt
LINE   9 | from app.generators.markdown_generator import generate_markdown_bundle
LINE  10 | from app.generators.text_generator import generate_text_bundle
LINE  11 | 
LINE  12 | 
LINE  13 | class TestAnalysisModeConstants(unittest.TestCase):
LINE  14 |     """Verify that mode constants and registry are correct."""
LINE  15 | 
LINE  16 |     def test_mode_constants_exist(self):
LINE  17 |         self.assertEqual(MODE_PROBLEM, "problem")
LINE  18 |         self.assertEqual(MODE_PROJECT, "project")
LINE  19 | 
LINE  20 |     def test_both_modes_in_registry(self):
LINE  21 |         self.assertIn(MODE_PROBLEM, ANALYSIS_MODES)
LINE  22 |         self.assertIn(MODE_PROJECT, ANALYSIS_MODES)
LINE  23 | 
LINE  24 |     def test_mode_configs_are_correct_type(self):
LINE  25 |         for key, cfg in ANALYSIS_MODES.items():
LINE  26 |             self.assertIsInstance(cfg, AnalysisModeConfig)
LINE  27 | 
LINE  28 |     def test_get_analysis_mode_config_returns_problem_by_default(self):
LINE  29 |         cfg = get_analysis_mode_config("")
LINE  30 |         self.assertEqual(cfg.mode, MODE_PROBLEM)
LINE  31 | 
LINE  32 |     def test_get_analysis_mode_config_unknown_key_returns_problem(self):
LINE  33 |         cfg = get_analysis_mode_config("nonexistent_mode")
LINE  34 |         self.assertEqual(cfg.mode, MODE_PROBLEM)
LINE  35 | 
LINE  36 |     def test_get_analysis_mode_config_project(self):
LINE  37 |         cfg = get_analysis_mode_config(MODE_PROJECT)
LINE  38 |         self.assertEqual(cfg.mode, MODE_PROJECT)
LINE  39 | 
LINE  40 | 
LINE  41 | class TestStandalonePromptProblemMode(unittest.TestCase):
LINE  42 |     """Verify standalone prompt in Problem Mode."""
LINE  43 | 
LINE  44 |     def setUp(self):
LINE  45 |         self.problem = "El botón de login no responde al hacer clic."
LINE  46 |         self.prompt = generate_standalone_prompt(
LINE  47 |             problem_desc=self.problem,
LINE  48 |             analysis_type="Detect errors",
LINE  49 |             analysis_mode=MODE_PROBLEM,
LINE  50 |         )
LINE  51 | 
LINE  52 |     def test_prompt_contains_reported_problem(self):
LINE  53 |         self.assertIn("REPORTED PROBLEM", self.prompt)
LINE  54 | 
LINE  55 |     def test_prompt_contains_problem_text(self):
LINE  56 |         self.assertIn(self.problem, self.prompt)
LINE  57 | 
LINE  58 |     def test_prompt_contains_problem_mode_label(self):
LINE  59 |         self.assertIn("Problem Mode", self.prompt)
LINE  60 | 
LINE  61 |     def test_prompt_does_not_contain_holistic_audit_heading(self):
LINE  62 |         self.assertNotIn("HOLISTIC PROJECT AUDIT", self.prompt)
LINE  63 | 
LINE  64 |     def test_prompt_contains_root_cause_section(self):
LINE  65 |         self.assertIn("Causa Raíz", self.prompt)
LINE  66 | 
LINE  67 |     def test_prompt_contains_files_to_modify(self):
LINE  68 |         self.assertIn("FILES TO MODIFY", self.prompt)
LINE  69 | 
LINE  70 | 
LINE  71 | class TestStandalonePromptProjectMode(unittest.TestCase):
LINE  72 |     """Verify standalone prompt in Project Mode."""
LINE  73 | 
LINE  74 |     def setUp(self):
LINE  75 |         self.prompt = generate_standalone_prompt(
LINE  76 |             problem_desc="",
LINE  77 |             analysis_type="Detect errors",
LINE  78 |             analysis_mode=MODE_PROJECT,
LINE  79 |         )
LINE  80 | 
LINE  81 |     def test_prompt_contains_holistic_audit_heading(self):
LINE  82 |         self.assertIn("HOLISTIC PROJECT AUDIT", self.prompt)
LINE  83 | 
LINE  84 |     def test_prompt_contains_project_mode_label(self):
LINE  85 |         self.assertIn("Project Mode", self.prompt)
LINE  86 | 
LINE  87 |     def test_prompt_does_not_contain_reported_problem_heading(self):
LINE  88 |         self.assertNotIn("REPORTED PROBLEM / PROBLEMA REPORTADO\n", self.prompt)
LINE  89 | 
LINE  90 |     def test_prompt_contains_audit_matrix(self):
LINE  91 |         self.assertIn("AUDIT MATRIX", self.prompt)
LINE  92 | 
LINE  93 |     def test_prompt_contains_action_plan(self):
LINE  94 |         self.assertIn("ACTION PLAN", self.prompt)
LINE  95 | 
LINE  96 |     def test_prompt_contains_owasp_mention(self):
LINE  97 |         self.assertIn("OWASP", self.prompt)
LINE  98 | 
LINE  99 |     def test_prompt_contains_dry_mention(self):
LINE 100 |         self.assertIn("DRY", self.prompt)
LINE 101 | 
LINE 102 | 
LINE 103 | class TestMarkdownGeneratorModes(unittest.TestCase):
LINE 104 |     """Verify that markdown_generator adapts content based on analysis_mode."""
LINE 105 | 
LINE 106 |     def _make_empty_selection(self):
LINE 107 |         return ProjectSelection()
LINE 108 | 
LINE 109 |     def test_problem_mode_contains_reported_problem_header(self):
LINE 110 |         config = ExportConfig(analysis_mode=MODE_PROBLEM)
LINE 111 |         sel = self._make_empty_selection()
LINE 112 |         text, *_ = generate_markdown_bundle(sel, "Error en login", config)
LINE 113 |         self.assertIn("REPORTED PROBLEM OR GOAL", text)
LINE 114 |         self.assertIn("Error en login", text)
LINE 115 | 
LINE 116 |     def test_problem_mode_no_holistic_header(self):
LINE 117 |         config = ExportConfig(analysis_mode=MODE_PROBLEM)
LINE 118 |         sel = self._make_empty_selection()
LINE 119 |         text, *_ = generate_markdown_bundle(sel, "Error en login", config)
LINE 120 |         self.assertNotIn("HOLISTIC PROJECT AUDIT", text)
LINE 121 | 
LINE 122 |     def test_project_mode_contains_holistic_header(self):
LINE 123 |         config = ExportConfig(analysis_mode=MODE_PROJECT)
LINE 124 |         sel = self._make_empty_selection()
LINE 125 |         text, *_ = generate_markdown_bundle(sel, "", config)
LINE 126 |         self.assertIn("HOLISTIC PROJECT AUDIT", text)
LINE 127 | 
LINE 128 |     def test_project_mode_no_reported_problem_header(self):
LINE 129 |         config = ExportConfig(analysis_mode=MODE_PROJECT)
LINE 130 |         sel = self._make_empty_selection()
LINE 131 |         text, *_ = generate_markdown_bundle(sel, "", config)
LINE 132 |         self.assertNotIn("REPORTED PROBLEM OR GOAL", text)
LINE 133 | 
LINE 134 |     def test_project_mode_system_instructions_use_mode(self):
LINE 135 |         config = ExportConfig(analysis_mode=MODE_PROJECT, include_system_instructions=True)
LINE 136 |         sel = self._make_empty_selection()
LINE 137 |         text, *_ = generate_markdown_bundle(sel, "", config)
LINE 138 |         self.assertIn("MODO PROYECTO", text.upper())
LINE 139 | 
LINE 140 |     def test_problem_mode_system_instructions_use_profile(self):
LINE 141 |         config = ExportConfig(analysis_mode=MODE_PROBLEM, include_system_instructions=True,
LINE 142 |                               analysis_type="Detect errors")
LINE 143 |         sel = self._make_empty_selection()
LINE 144 |         text, *_ = generate_markdown_bundle(sel, "bug", config)
LINE 145 |         self.assertIn("DETECT ERRORS", text.upper())
LINE 146 | 
LINE 147 | 
LINE 148 | class TestTextGeneratorModes(unittest.TestCase):
LINE 149 |     """Verify that text_generator adapts content based on analysis_mode."""
LINE 150 | 
LINE 151 |     def _make_empty_selection(self):
LINE 152 |         return ProjectSelection()
LINE 153 | 
LINE 154 |     def test_problem_mode_contains_reported_problem_header(self):
LINE 155 |         config = ExportConfig(analysis_mode=MODE_PROBLEM)
LINE 156 |         sel = self._make_empty_selection()
LINE 157 |         text, *_ = generate_text_bundle(sel, "Error 500 en API", config)
LINE 158 |         self.assertIn("REPORTED PROBLEM OR GOAL", text)
LINE 159 |         self.assertIn("Error 500 en API", text)
LINE 160 | 
LINE 161 |     def test_project_mode_contains_holistic_header(self):
LINE 162 |         config = ExportConfig(analysis_mode=MODE_PROJECT)
LINE 163 |         sel = self._make_empty_selection()
LINE 164 |         text, *_ = generate_text_bundle(sel, "", config)
LINE 165 |         self.assertIn("HOLISTIC PROJECT AUDIT", text)
LINE 166 | 
LINE 167 |     def test_project_mode_system_instructions_use_mode(self):
LINE 168 |         config = ExportConfig(analysis_mode=MODE_PROJECT, include_system_instructions=True)
LINE 169 |         sel = self._make_empty_selection()
LINE 170 |         text, *_ = generate_text_bundle(sel, "", config)
LINE 171 |         self.assertIn("MODO PROYECTO", text.upper())
LINE 172 | 
LINE 173 |     def test_problem_mode_system_instructions_use_profile(self):
LINE 174 |         config = ExportConfig(analysis_mode=MODE_PROBLEM, include_system_instructions=True,
LINE 175 |                               analysis_type="Review security")
LINE 176 |         sel = self._make_empty_selection()
LINE 177 |         text, *_ = generate_text_bundle(sel, "XSS vulnerability", config)
LINE 178 |         self.assertIn("REVIEW SECURITY", text.upper())
LINE 179 | 
LINE 180 | 
LINE 181 | if __name__ == "__main__":
LINE 182 |     unittest.main()
```

==============================================================
FILE: tests/test_analysis_types.py
==============================================================
```py
LINE   1 | """
LINE   2 | Unit and integration tests for Analysis Types and Profiles.
LINE   3 | """
LINE   4 | import os
LINE   5 | import sys
LINE   6 | import unittest
LINE   7 | from unittest.mock import patch
LINE   8 | import tkinter as tk
LINE   9 | 
LINE  10 | sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
LINE  11 | 
LINE  12 | from app.models.analysis_types import (
LINE  13 |     ANALYSIS_PROFILES, ANALYSIS_TYPE_KEYS, get_analysis_profile, get_all_analysis_types
LINE  14 | )
LINE  15 | from app.models.project import ExportConfig, ProjectSelection
LINE  16 | from app.generators.standalone_prompt_generator import generate_standalone_prompt
LINE  17 | from app.generators.markdown_generator import generate_markdown_bundle
LINE  18 | from app.generators.text_generator import generate_text_bundle
LINE  19 | from app.gui.main_window import MainWindow
LINE  20 | 
LINE  21 | 
LINE  22 | class TestAnalysisTypes(unittest.TestCase):
LINE  23 | 
LINE  24 |     def test_all_ten_profiles_defined(self):
LINE  25 |         """Verifies that all 10 requested analysis profiles exist and are complete."""
LINE  26 |         expected_types = [
LINE  27 |             "Detect errors",
LINE  28 |             "Solve problem",
LINE  29 |             "Refactoring",
LINE  30 |             "Improve architecture",
LINE  31 |             "Optimize performance",
LINE  32 |             "Review security",
LINE  33 |             "Create new functionality",
LINE  34 |             "Explain project",
LINE  35 |             "Document project",
LINE  36 |             "Comprehensive review",
LINE  37 |         ]
LINE  38 |         self.assertEqual(get_all_analysis_types(), expected_types)
LINE  39 | 
LINE  40 |         for key in expected_types:
LINE  41 |             self.assertIn(key, ANALYSIS_PROFILES)
LINE  42 |             profile = get_analysis_profile(key)
LINE  43 |             self.assertEqual(profile.name, key)
LINE  44 |             self.assertTrue(len(profile.objective) > 10, f"Objective too short for {key}")
LINE  45 |             self.assertTrue(len(profile.focus) > 10, f"Focus too short for {key}")
LINE  46 |             self.assertTrue(len(profile.priorities) > 10, f"Priorities too short for {key}")
LINE  47 |             self.assertTrue(len(profile.expected_outcome) > 10, f"Expected outcome too short for {key}")
LINE  48 |             self.assertTrue(len(profile.response_instructions) > 10, f"Response instructions too short for {key}")
LINE  49 |             self.assertTrue(len(profile.response_template) > 20, f"Response template too short for {key}")
LINE  50 |             # Ensure action-oriented wording is present
LINE  51 |             self.assertIn("CONCRETO, TÉCNICO", profile.response_instructions)
LINE  52 | 
LINE  53 |     def test_generate_standalone_prompt_with_profiles(self):
LINE  54 |         """Verifies that standalone prompt incorporates profile objective, focus, priorities, and outcome."""
LINE  55 |         for key in ANALYSIS_TYPE_KEYS:
LINE  56 |             profile = get_analysis_profile(key)
LINE  57 |             prompt = generate_standalone_prompt("Test problem description", analysis_type=key)
LINE  58 | 
LINE  59 |             self.assertIn(f"• PERFIL: {profile.icon} {profile.name}", prompt)
LINE  60 |             self.assertIn(profile.objective, prompt)
LINE  61 |             self.assertIn(profile.focus, prompt)
LINE  62 |             self.assertIn(profile.priorities, prompt)
LINE  63 |             self.assertIn(profile.expected_outcome, prompt)
LINE  64 |             self.assertIn(profile.response_instructions, prompt)
LINE  65 |             self.assertIn("Test problem description", prompt)
LINE  66 | 
LINE  67 |     def test_markdown_and_text_bundle_with_profile(self):
LINE  68 |         """Verifies that markdown and text generators include selected profile in context document."""
LINE  69 |         selection = ProjectSelection()
LINE  70 |         config = ExportConfig(analysis_type="Review security")
LINE  71 | 
LINE  72 |         md_text, _, _, _, _ = generate_markdown_bundle(selection, "Vulnerability test", config)
LINE  73 |         self.assertIn("Review security", md_text)
LINE  74 |         self.assertIn("Auditar el código en busca de vulnerabilidades", md_text)
LINE  75 |         self.assertIn("Vulnerability test", md_text)
LINE  76 | 
LINE  77 |         txt_text, _, _, _, _ = generate_text_bundle(selection, "Vulnerability test", config)
LINE  78 |         self.assertIn("Review security", txt_text)
LINE  79 |         self.assertIn("Auditar el código en busca de vulnerabilidades", txt_text)
LINE  80 | 
LINE  81 |     def test_main_window_combobox_integration(self):
LINE  82 |         """Verifies MainWindow integration with Analysis Type selector and dynamic hint updating."""
LINE  83 |         root = tk.Tk()
LINE  84 |         try:
LINE  85 |             app = MainWindow(root)
LINE  86 | 
LINE  87 |             # Check combobox options
LINE  88 |             values = list(app.cb_analysis_type["values"])
LINE  89 |             self.assertEqual(values, ANALYSIS_TYPE_KEYS)
LINE  90 | 
LINE  91 |             # Initial default is "Detect errors"
LINE  92 |             self.assertEqual(app.var_analysis_type.get(), "Detect errors")
LINE  93 |             profile_detect = get_analysis_profile("Detect errors")
LINE  94 |             self.assertIn(profile_detect.objective, app.lbl_profile_hint.cget("text"))
LINE  95 | 
LINE  96 |             # Switch to "Optimize performance"
LINE  97 |             app.var_analysis_type.set("Optimize performance")
LINE  98 |             app._on_analysis_type_changed()
LINE  99 | 
LINE 100 |             profile_perf = get_analysis_profile("Optimize performance")
LINE 101 |             self.assertIn(profile_perf.objective, app.lbl_profile_hint.cget("text"))
LINE 102 |             self.assertIn(profile_perf.default_prompt_hint, app.problem_text.get("1.0", tk.END).strip())
LINE 103 | 
LINE 104 |             # Switch to "Review security"
LINE 105 |             app.var_analysis_type.set("Review security")
LINE 106 |             app._on_analysis_type_changed()
LINE 107 | 
LINE 108 |             profile_sec = get_analysis_profile("Review security")
LINE 109 |             self.assertIn(profile_sec.objective, app.lbl_profile_hint.cget("text"))
LINE 110 |             self.assertIn(profile_sec.default_prompt_hint, app.problem_text.get("1.0", tk.END).strip())
LINE 111 | 
LINE 112 |             # User types a custom problem description: should NOT be overwritten when changing types
LINE 113 |             custom_problem = "Custom specific critical issue in database connection pool"
LINE 114 |             app.problem_text.delete("1.0", tk.END)
LINE 115 |             app.problem_text.insert("1.0", custom_problem)
LINE 116 | 
LINE 117 |             app.var_analysis_type.set("Refactoring")
LINE 118 |             app._on_analysis_type_changed()
LINE 119 |             self.assertEqual(app.problem_text.get("1.0", tk.END).strip(), custom_problem)
LINE 120 | 
LINE 121 |         finally:
LINE 122 |             root.destroy()
LINE 123 | 
LINE 124 | 
LINE 125 | if __name__ == "__main__":
LINE 126 |     unittest.main()
```

==============================================================
FILE: tests/test_dependency_graph.py
==============================================================
```py
LINE  1 | import os
LINE  2 | import shutil
LINE  3 | import tempfile
LINE  4 | import unittest
LINE  5 | 
LINE  6 | from app.core.dependency_graph import DependencyResolver
LINE  7 | 
LINE  8 | 
LINE  9 | class TestDependencyResolver(unittest.TestCase):
LINE 10 | 
LINE 11 |     def setUp(self):
LINE 12 |         self.tmp = tempfile.mkdtemp(prefix="test_dep_graph_")
LINE 13 | 
LINE 14 |     def tearDown(self):
LINE 15 |         shutil.rmtree(self.tmp, ignore_errors=True)
LINE 16 | 
LINE 17 |     def _write(self, rel_path, content):
LINE 18 |         path = os.path.join(self.tmp, rel_path)
LINE 19 |         os.makedirs(os.path.dirname(path), exist_ok=True)
LINE 20 |         with open(path, "w", encoding="utf-8") as f:
LINE 21 |             f.write(content)
LINE 22 | 
LINE 23 |     def test_file_without_dependencies(self):
LINE 24 |         self._write("a.py", "x = 1\n")
LINE 25 |         resolver = DependencyResolver(self.tmp)
LINE 26 |         node = resolver.build_tree("a.py")
LINE 27 |         self.assertEqual(node.rel_path, "a.py")
LINE 28 |         self.assertEqual(node.children, [])
LINE 29 | 
LINE 30 |     def test_single_dependency(self):
LINE 31 |         self._write("a.py", "import b\n")
LINE 32 |         self._write("b.py", "x = 1\n")
LINE 33 |         resolver = DependencyResolver(self.tmp)
LINE 34 |         node = resolver.build_tree("a.py")
LINE 35 |         self.assertEqual(len(node.children), 1)
LINE 36 |         self.assertEqual(node.children[0].rel_path, "b.py")
LINE 37 | 
LINE 38 |     def test_chain_dependencies(self):
LINE 39 |         self._write("a.py", "import b\n")
LINE 40 |         self._write("b.py", "import c\n")
LINE 41 |         self._write("c.py", "x = 1\n")
LINE 42 |         resolver = DependencyResolver(self.tmp)
LINE 43 |         node = resolver.build_tree("a.py")
LINE 44 |         self.assertEqual(node.children[0].rel_path, "b.py")
LINE 45 |         self.assertEqual(node.children[0].children[0].rel_path, "c.py")
LINE 46 | 
LINE 47 |     def test_circular_dependency(self):
LINE 48 |         self._write("a.py", "import b\n")
LINE 49 |         self._write("b.py", "import c\n")
LINE 50 |         self._write("c.py", "import a\n")
LINE 51 |         resolver = DependencyResolver(self.tmp)
LINE 52 |         node = resolver.build_tree("a.py")
LINE 53 |         c = node.children[0].children[0]
LINE 54 |         self.assertEqual(c.rel_path, "c.py")
LINE 55 |         self.assertTrue(c.children[0].is_cycle)
LINE 56 | 
LINE 57 |     def test_repeated_dependency(self):
LINE 58 |         self._write("a.py", "import b\nimport c\n")
LINE 59 |         self._write("b.py", "import d\n")
LINE 60 |         self._write("c.py", "import d\n")
LINE 61 |         self._write("d.py", "x = 1\n")
LINE 62 |         resolver = DependencyResolver(self.tmp)
LINE 63 |         node = resolver.build_tree("a.py")
LINE 64 |         b = next(ch for ch in node.children if ch.rel_path == "b.py")
LINE 65 |         c = next(ch for ch in node.children if ch.rel_path == "c.py")
LINE 66 |         self.assertEqual(b.children[0].rel_path, "d.py")
LINE 67 |         self.assertEqual(c.children[0].rel_path, "d.py")
LINE 68 |         self.assertTrue(c.children[0].is_repeated)
LINE 69 | 
LINE 70 |     def test_external_dependency_ignored(self):
LINE 71 |         self._write("a.py", "import os\n")
LINE 72 |         resolver = DependencyResolver(self.tmp)
LINE 73 |         node = resolver.build_tree("a.py")
LINE 74 |         self.assertEqual(node.children, [])
LINE 75 | 
LINE 76 |     def test_missing_dependency_ignored(self):
LINE 77 |         self._write("a.py", "import missing_module\n")
LINE 78 |         resolver = DependencyResolver(self.tmp)
LINE 79 |         node = resolver.build_tree("a.py")
LINE 80 |         self.assertEqual(node.children, [])
LINE 81 | 
LINE 82 | 
LINE 83 | if __name__ == "__main__":
LINE 84 |     unittest.main()
```

==============================================================
FILE: tests/test_file_search_dialog.py
==============================================================
```py
LINE   1 | """Unit tests for project scanner caching and FileSearchDialog optimizations."""
LINE   2 | import os
LINE   3 | import shutil
LINE   4 | import tempfile
LINE   5 | import time
LINE   6 | import unittest
LINE   7 | import tkinter as tk
LINE   8 | 
LINE   9 | from app.core.project_scanner import scan_directory, clear_scan_cache, _SCAN_CACHE
LINE  10 | from app.gui.file_search_dialog import FileSearchDialog, MAX_RENDER_LIMIT
LINE  11 | 
LINE  12 | 
LINE  13 | class TestProjectScannerCache(unittest.TestCase):
LINE  14 |     def setUp(self):
LINE  15 |         self.tmp_dir = tempfile.mkdtemp(prefix="test_scanner_")
LINE  16 |         clear_scan_cache()
LINE  17 | 
LINE  18 |     def tearDown(self):
LINE  19 |         clear_scan_cache()
LINE  20 |         shutil.rmtree(self.tmp_dir, ignore_errors=True)
LINE  21 | 
LINE  22 |     def _create_file(self, rel_path: str, content: str = "test"):
LINE  23 |         full = os.path.join(self.tmp_dir, rel_path)
LINE  24 |         os.makedirs(os.path.dirname(full), exist_ok=True)
LINE  25 |         with open(full, "w", encoding="utf-8") as f:
LINE  26 |             f.write(content)
LINE  27 | 
LINE  28 |     def test_scan_directory_caching(self):
LINE  29 |         self._create_file("file1.txt")
LINE  30 |         self._create_file("file2.py")
LINE  31 | 
LINE  32 |         res1 = scan_directory(self.tmp_dir, excluded_dirs=set(), use_cache=True)
LINE  33 |         self.assertEqual(res1, ["file1.txt", "file2.py"])
LINE  34 |         self.assertEqual(len(_SCAN_CACHE), 1)
LINE  35 | 
LINE  36 |         # Second call should use cache
LINE  37 |         res2 = scan_directory(self.tmp_dir, excluded_dirs=set(), use_cache=True)
LINE  38 |         self.assertEqual(res2, ["file1.txt", "file2.py"])
LINE  39 | 
LINE  40 |     def test_cache_invalidation_on_folder_mtime_change(self):
LINE  41 |         self._create_file("file1.txt")
LINE  42 |         res1 = scan_directory(self.tmp_dir, excluded_dirs=set(), use_cache=True)
LINE  43 |         self.assertEqual(res1, ["file1.txt"])
LINE  44 | 
LINE  45 |         # Sleep briefly to ensure mtime timestamp differs on filesystem
LINE  46 |         time.sleep(0.05)
LINE  47 |         # Touch folder / add new file to change folder mtime
LINE  48 |         self._create_file("file2.txt")
LINE  49 |         os.utime(self.tmp_dir, None)
LINE  50 | 
LINE  51 |         res2 = scan_directory(self.tmp_dir, excluded_dirs=set(), use_cache=True)
LINE  52 |         self.assertEqual(res2, ["file1.txt", "file2.txt"])
LINE  53 | 
LINE  54 | 
LINE  55 | class TestFileSearchDialogGUI(unittest.TestCase):
LINE  56 |     def setUp(self):
LINE  57 |         self.tmp_dir = tempfile.mkdtemp(prefix="test_dialog_")
LINE  58 |         self.root = tk.Tk()
LINE  59 |         self.root.withdraw()
LINE  60 | 
LINE  61 |         # Create dummy files
LINE  62 |         for i in range(15):
LINE  63 |             path = os.path.join(self.tmp_dir, f"module_{i:02d}.py")
LINE  64 |             with open(path, "w", encoding="utf-8") as f:
LINE  65 |                 f.write(f"# File {i}\n")
LINE  66 | 
LINE  67 |     def tearDown(self):
LINE  68 |         try:
LINE  69 |             self.root.destroy()
LINE  70 |         except Exception:
LINE  71 |             pass
LINE  72 |         shutil.rmtree(self.tmp_dir, ignore_errors=True)
LINE  73 | 
LINE  74 |     def test_dialog_async_load_and_rendering(self):
LINE  75 |         dialog = FileSearchDialog(self.root, self.tmp_dir)
LINE  76 | 
LINE  77 |         # Process mainloop events to allow background thread & after callbacks to execute
LINE  78 |         start_time = time.time()
LINE  79 |         while len(dialog.all_files) == 0 and (time.time() - start_time) < 2.0:
LINE  80 |             self.root.update()
LINE  81 | 
LINE  82 |         self.assertEqual(len(dialog.all_files), 15)
LINE  83 | 
LINE  84 |         # Process remaining render batch callbacks
LINE  85 |         for _ in range(10):
LINE  86 |             self.root.update()
LINE  87 | 
LINE  88 |         children = dialog.scroll_frame.winfo_children()
LINE  89 |         self.assertTrue(len(children) >= 15)
LINE  90 | 
LINE  91 |         dialog.destroy()
LINE  92 | 
LINE  93 |     def test_dialog_search_filter(self):
LINE  94 |         dialog = FileSearchDialog(self.root, self.tmp_dir)
LINE  95 | 
LINE  96 |         start_time = time.time()
LINE  97 |         while len(dialog.all_files) == 0 and (time.time() - start_time) < 2.0:
LINE  98 |             self.root.update()
LINE  99 | 
LINE 100 |         # Set search query
LINE 101 |         dialog.search_var.set("module_05")
LINE 102 | 
LINE 103 |         # Allow debouncing after callback to fire
LINE 104 |         for _ in range(10):
LINE 105 |             time.sleep(0.02)
LINE 106 |             self.root.update()
LINE 107 | 
LINE 108 |         children = [
LINE 109 |             c for c in dialog.scroll_frame.winfo_children()
LINE 110 |             if isinstance(c, tk.Frame)
LINE 111 |         ]
LINE 112 |         self.assertEqual(len(children), 1)
LINE 113 | 
LINE 114 |         dialog.destroy()
LINE 115 | 
LINE 116 |     def test_dialog_scan_cancellation_on_destroy(self):
LINE 117 |         dialog = FileSearchDialog(self.root, self.tmp_dir)
LINE 118 |         # Immediately destroy dialog before background scan finishes
LINE 119 |         dialog.destroy()
LINE 120 |         self.root.update()
LINE 121 | 
LINE 122 |         # Ensure no TclError or unhandled exception occurs
LINE 123 |         time.sleep(0.1)
LINE 124 |         self.root.update()
LINE 125 | 
LINE 126 |     def test_hard_render_limit(self):
LINE 127 |         # Create directory with 600 files
LINE 128 |         big_dir = tempfile.mkdtemp(prefix="test_big_")
LINE 129 |         try:
LINE 130 |             for i in range(600):
LINE 131 |                 with open(os.path.join(big_dir, f"file_{i:03d}.txt"), "w") as f:
LINE 132 |                     f.write("x")
LINE 133 | 
LINE 134 |             dialog = FileSearchDialog(self.root, big_dir)
LINE 135 | 
LINE 136 |             start_time = time.time()
LINE 137 |             while len(dialog.all_files) < 600 and (time.time() - start_time) < 3.0:
LINE 138 |                 self.root.update()
LINE 139 | 
LINE 140 |             self.assertEqual(len(dialog.all_files), 600)
LINE 141 | 
LINE 142 |             # Process render batches
LINE 143 |             for _ in range(20):
LINE 144 |                 self.root.update()
LINE 145 | 
LINE 146 |             # Rows rendered should be limited to MAX_RENDER_LIMIT + 1 (footer)
LINE 147 |             row_frames = [
LINE 148 |                 c for c in dialog.scroll_frame.winfo_children()
LINE 149 |                 if isinstance(c, tk.Frame)
LINE 150 |             ]
LINE 151 |             self.assertEqual(len(row_frames), MAX_RENDER_LIMIT + 1)
LINE 152 | 
LINE 153 |             dialog.destroy()
LINE 154 |         finally:
LINE 155 |             shutil.rmtree(big_dir, ignore_errors=True)
LINE 156 | 
LINE 157 | 
LINE 158 | if __name__ == "__main__":
LINE 159 |     unittest.main()
```

==============================================================
FILE: tests/test_integration_gui.py
==============================================================
```py
LINE  1 | """
LINE  2 | GUI integration test for MainWindow project analysis workflow.
LINE  3 | """
LINE  4 | import os
LINE  5 | import sys
LINE  6 | import unittest
LINE  7 | from unittest.mock import patch
LINE  8 | import tkinter as tk
LINE  9 | 
LINE 10 | sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
LINE 11 | 
LINE 12 | from app.gui.main_window import MainWindow
LINE 13 | from app.gui.analysis_dialog import ProjectAnalysisDialog
LINE 14 | from app.core.project_analyzer import ProjectAnalyzer
LINE 15 | 
LINE 16 | 
LINE 17 | class TestGuiIntegration(unittest.TestCase):
LINE 18 | 
LINE 19 |     @patch("app.gui.dialogs.show_info")
LINE 20 |     def test_main_window_analysis_and_apply(self, mock_show_info):
LINE 21 |         root = tk.Tk()
LINE 22 |         try:
LINE 23 |             app = MainWindow(root)
LINE 24 |             current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LINE 25 | 
LINE 26 |             # Simulate folder selection
LINE 27 |             app.selector.set_folder(current_dir)
LINE 28 |             app.var_folder.set(current_dir)
LINE 29 |             app.reload_tree()
LINE 30 | 
LINE 31 |             initial_files = app.tree.get_checked_files()
LINE 32 |             self.assertTrue(len(initial_files) > 0)
LINE 33 | 
LINE 34 |             # Analyze project
LINE 35 |             analyzer = ProjectAnalyzer(excluded_dirs=app.selector.get_selection().excluded_dirs)
LINE 36 |             result = analyzer.analyze(current_dir)
LINE 37 | 
LINE 38 |             self.assertIn("main.py", result.recommended_files)
LINE 39 | 
LINE 40 |             # Test applying selection
LINE 41 |             target_selection = ["main.py", "requirements.txt"]
LINE 42 |             app.apply_recommended_selection(target_selection)
LINE 43 | 
LINE 44 |             checked = set(app.tree.get_checked_files())
LINE 45 |             self.assertEqual(checked, set(target_selection))
LINE 46 |             self.assertEqual(app.sv_sel_files.get(), "2")
LINE 47 | 
LINE 48 |             # Test opening ProjectAnalysisDialog
LINE 49 |             dialog = ProjectAnalysisDialog(
LINE 50 |                 root,
LINE 51 |                 analysis=result,
LINE 52 |                 on_apply_selection=app.apply_recommended_selection
LINE 53 |             )
LINE 54 |             # Ensure dialog populated recommended checkboxes
LINE 55 |             self.assertTrue(len(dialog.file_vars) > 0)
LINE 56 |             selected_in_dialog = dialog.get_selected_recommended_files()
LINE 57 |             self.assertTrue(len(selected_in_dialog) > 0)
LINE 58 | 
LINE 59 |             # Simulate clicking apply selection from dialog
LINE 60 |             dialog._on_apply_clicked()
LINE 61 | 
LINE 62 |             # Verify selection updated
LINE 63 |             final_checked = set(app.tree.get_checked_files())
LINE 64 |             self.assertTrue(len(final_checked) > 0)
LINE 65 | 
LINE 66 |         finally:
LINE 67 |             root.destroy()
LINE 68 | 
LINE 69 | 
LINE 70 | if __name__ == "__main__":
LINE 71 |     unittest.main()
```

==============================================================
FILE: tests/test_intelligent_context.py
==============================================================
```py
LINE   1 | """
LINE   2 | Unit tests for IntelligentContextAnalyzer and related prioritizing components.
LINE   3 | """
LINE   4 | import os
LINE   5 | import shutil
LINE   6 | import tempfile
LINE   7 | import unittest
LINE   8 | 
LINE   9 | from app.core.intelligent_context import (
LINE  10 |     IntelligentContextAnalyzer,
LINE  11 |     PRIORITY_CRITICAL,
LINE  12 |     PRIORITY_IMPORTANT,
LINE  13 |     PRIORITY_RELATED,
LINE  14 |     PRIORITY_SECONDARY
LINE  15 | )
LINE  16 | 
LINE  17 | 
LINE  18 | class TestIntelligentContextAnalyzer(unittest.TestCase):
LINE  19 | 
LINE  20 |     def test_extract_keywords(self):
LINE  21 |         analyzer = IntelligentContextAnalyzer()
LINE  22 |         keywords, phrases = analyzer._extract_keywords("Error creating users in database")
LINE  23 |         self.assertIn("user", keywords)
LINE  24 |         self.assertIn("users", keywords)
LINE  25 |         self.assertIn("database", keywords)
LINE  26 |         self.assertIn("create", keywords)
LINE  27 | 
LINE  28 |     def test_prioritization_levels(self):
LINE  29 |         temp_dir = tempfile.mkdtemp(prefix="test_intelligent_ctx_")
LINE  30 |         try:
LINE  31 |             # Create synthetic project structure matching prompt example
LINE  32 |             os.makedirs(os.path.join(temp_dir, "routes"), exist_ok=True)
LINE  33 |             routes_user = os.path.join(temp_dir, "routes", "users.py")
LINE  34 |             with open(routes_user, "w", encoding="utf-8") as f:
LINE  35 |                 f.write("from services.user_service import create_user\n\ndef create_user_route():\n    create_user()\n")
LINE  36 | 
LINE  37 |             os.makedirs(os.path.join(temp_dir, "controllers"), exist_ok=True)
LINE  38 |             ctrl_user = os.path.join(temp_dir, "controllers", "user.py")
LINE  39 |             with open(ctrl_user, "w", encoding="utf-8") as f:
LINE  40 |                 f.write("from models.user import UserModel\n\nclass UserController:\n    pass\n")
LINE  41 | 
LINE  42 |             os.makedirs(os.path.join(temp_dir, "models"), exist_ok=True)
LINE  43 |             model_user = os.path.join(temp_dir, "models", "user.py")
LINE  44 |             with open(model_user, "w", encoding="utf-8") as f:
LINE  45 |                 f.write("class UserModel:\n    pass\n")
LINE  46 | 
LINE  47 |             os.makedirs(os.path.join(temp_dir, "services"), exist_ok=True)
LINE  48 |             svc_user = os.path.join(temp_dir, "services", "user_service.py")
LINE  49 |             with open(svc_user, "w", encoding="utf-8") as f:
LINE  50 |                 f.write("def create_user():\n    pass\n")
LINE  51 | 
LINE  52 |             os.makedirs(os.path.join(temp_dir, "config"), exist_ok=True)
LINE  53 |             cfg_db = os.path.join(temp_dir, "config", "database.py")
LINE  54 |             with open(cfg_db, "w", encoding="utf-8") as f:
LINE  55 |                 f.write("DB_HOST = 'localhost'\n")
LINE  56 | 
LINE  57 |             unrelated = os.path.join(temp_dir, "unrelated.py")
LINE  58 |             with open(unrelated, "w", encoding="utf-8") as f:
LINE  59 |                 f.write("print('hello world')\n")
LINE  60 | 
LINE  61 |             candidates = [
LINE  62 |                 "routes/users.py",
LINE  63 |                 "controllers/user.py",
LINE  64 |                 "models/user.py",
LINE  65 |                 "services/user_service.py",
LINE  66 |                 "config/database.py",
LINE  67 |                 "unrelated.py"
LINE  68 |             ]
LINE  69 | 
LINE  70 |             analyzer = IntelligentContextAnalyzer()
LINE  71 |             prioritized = analyzer.analyze(
LINE  72 |                 folder_path=temp_dir,
LINE  73 |                 candidate_rel_files=candidates,
LINE  74 |                 problem_desc="Error creating users"
LINE  75 |             )
LINE  76 | 
LINE  77 |             pmap = {p.rel_path: p.priority_level for p in prioritized}
LINE  78 | 
LINE  79 |             # routes/users.py, controllers/user.py, models/user.py -> Critical 🔴
LINE  80 |             self.assertEqual(pmap["routes/users.py"], PRIORITY_CRITICAL)
LINE  81 |             self.assertEqual(pmap["controllers/user.py"], PRIORITY_CRITICAL)
LINE  82 |             self.assertEqual(pmap["models/user.py"], PRIORITY_CRITICAL)
LINE  83 | 
LINE  84 |             # services/user_service.py -> Important 🟠 (dependency of routes/users.py & user match)
LINE  85 |             self.assertIn(pmap["services/user_service.py"], (PRIORITY_CRITICAL, PRIORITY_IMPORTANT))
LINE  86 | 
LINE  87 |             # config/database.py -> Related 🟡 (database config)
LINE  88 |             self.assertEqual(pmap["config/database.py"], PRIORITY_RELATED)
LINE  89 | 
LINE  90 |             # unrelated.py -> Secondary ⚪
LINE  91 |             self.assertEqual(pmap["unrelated.py"], PRIORITY_SECONDARY)
LINE  92 | 
LINE  93 |         finally:
LINE  94 |             shutil.rmtree(temp_dir, ignore_errors=True)
LINE  95 | 
LINE  96 |     def test_limit_enforcement_prioritization(self):
LINE  97 |         temp_dir = tempfile.mkdtemp(prefix="test_limits_")
LINE  98 |         try:
LINE  99 |             # Create 5 files
LINE 100 |             for name in ["crit1.py", "crit2.py", "sec1.py", "sec2.py", "sec3.py"]:
LINE 101 |                 with open(os.path.join(temp_dir, name), "w", encoding="utf-8") as f:
LINE 102 |                     f.write(f"# content for {name}\n" * 10)
LINE 103 | 
LINE 104 |             analyzer = IntelligentContextAnalyzer()
LINE 105 |             candidates = ["crit1.py", "crit2.py", "sec1.py", "sec2.py", "sec3.py"]
LINE 106 |             # Set problem to target crit files
LINE 107 |             prioritized = analyzer.analyze(
LINE 108 |                 folder_path=temp_dir,
LINE 109 |                 candidate_rel_files=candidates,
LINE 110 |                 problem_desc="crit1 crit2",
LINE 111 |                 max_files=2  # Limit to 2 files max
LINE 112 |             )
LINE 113 | 
LINE 114 |             selected = [p.rel_path for p in prioritized if p.is_selected]
LINE 115 |             self.assertEqual(len(selected), 2)
LINE 116 |             self.assertIn("crit1.py", selected)
LINE 117 |             self.assertIn("crit2.py", selected)
LINE 118 |         finally:
LINE 119 |             shutil.rmtree(temp_dir, ignore_errors=True)
LINE 120 | 
LINE 121 | 
LINE 122 | if __name__ == "__main__":
LINE 123 |     unittest.main()
```

==============================================================
FILE: tests/test_project_analyzer.py
==============================================================
```py
LINE   1 | """
LINE   2 | Unit tests for ProjectAnalyzer and related components.
LINE   3 | """
LINE   4 | import os
LINE   5 | import sys
LINE   6 | import shutil
LINE   7 | import tempfile
LINE   8 | import unittest
LINE   9 | import tkinter as tk
LINE  10 | 
LINE  11 | # Ensure root directory is in sys.path
LINE  12 | sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
LINE  13 | 
LINE  14 | from app.core.project_analyzer import ProjectAnalyzer, ProjectAnalysisResult
LINE  15 | from app.gui.file_tree import CheckboxTreeview
LINE  16 | 
LINE  17 | 
LINE  18 | class TestProjectAnalyzer(unittest.TestCase):
LINE  19 | 
LINE  20 |     def test_analyze_current_project(self):
LINE  21 |         """Analyzes the current repository and verifies language, framework, and entry points."""
LINE  22 |         current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LINE  23 |         analyzer = ProjectAnalyzer()
LINE  24 |         result = analyzer.analyze(current_dir)
LINE  25 | 
LINE  26 |         self.assertIsInstance(result, ProjectAnalysisResult)
LINE  27 |         self.assertEqual(result.primary_language, "Python")
LINE  28 |         self.assertEqual(result.framework, "Tkinter")
LINE  29 |         self.assertIn("pip", result.package_manager.lower())
LINE  30 |         self.assertIn("main.py", result.entry_points)
LINE  31 |         self.assertTrue(result.total_files > 0)
LINE  32 |         self.assertTrue(result.total_lines > 0)
LINE  33 |         self.assertTrue(len(result.recommended_files) > 0)
LINE  34 |         self.assertIn("main.py", result.recommended_files)
LINE  35 | 
LINE  36 |         # Check exclusions list
LINE  37 |         self.assertIn("vendor", result.configured_exclusions)
LINE  38 |         self.assertIn(".quasar", result.configured_exclusions)
LINE  39 |         self.assertIn(".github", result.configured_exclusions)
LINE  40 |         self.assertIn("public", result.configured_exclusions)
LINE  41 | 
LINE  42 |         # Check formatted report generation
LINE  43 |         report = result.to_formatted_report()
LINE  44 |         self.assertIn("REPORTE DE ANÁLISIS AUTOMÁTICO", report)
LINE  45 |         self.assertIn("Python", report)
LINE  46 |         self.assertIn("Tkinter", report)
LINE  47 | 
LINE  48 |     def test_analyze_laravel_project(self):
LINE  49 |         """Analyzes a synthetic Laravel project structure."""
LINE  50 |         temp_dir = tempfile.mkdtemp(prefix="test_laravel_")
LINE  51 |         try:
LINE  52 |             # Create synthetic Laravel files
LINE  53 |             with open(os.path.join(temp_dir, "artisan"), "w", encoding="utf-8") as f:
LINE  54 |                 f.write("#!/usr/bin/env php\n<?php\ndefine('LARAVEL_START', microtime(true));\n")
LINE  55 | 
LINE  56 |             with open(os.path.join(temp_dir, "composer.json"), "w", encoding="utf-8") as f:
LINE  57 |                 f.write('{\n  "name": "laravel/laravel",\n  "require": {\n    "php": "^8.2",\n    "laravel/framework": "^11.0"\n  }\n}')
LINE  58 | 
LINE  59 |             os.makedirs(os.path.join(temp_dir, "app", "Services"), exist_ok=True)
LINE  60 |             user_svc = os.path.join(temp_dir, "app", "Services", "UserService.php")
LINE  61 |             with open(user_svc, "w", encoding="utf-8") as f:
LINE  62 |                 f.write("<?php\nnamespace App\\Services;\nclass UserService {\n  public function getUser() {}\n}\n")
LINE  63 | 
LINE  64 |             os.makedirs(os.path.join(temp_dir, "routes"), exist_ok=True)
LINE  65 |             with open(os.path.join(temp_dir, "routes", "web.php"), "w", encoding="utf-8") as f:
LINE  66 |                 f.write("<?php\nuse Illuminate\\Support\\Facades\\Route;\nRoute::get('/', function () { return view('welcome'); });\n")
LINE  67 | 
LINE  68 |             # Create directories that should be excluded: vendor, public, .git
LINE  69 |             os.makedirs(os.path.join(temp_dir, "vendor", "laravel"), exist_ok=True)
LINE  70 |             with open(os.path.join(temp_dir, "vendor", "laravel", "test.php"), "w", encoding="utf-8") as f:
LINE  71 |                 f.write("<?php // vendor code\n")
LINE  72 | 
LINE  73 |             os.makedirs(os.path.join(temp_dir, "public", "build"), exist_ok=True)
LINE  74 |             with open(os.path.join(temp_dir, "public", "index.php"), "w", encoding="utf-8") as f:
LINE  75 |                 f.write("<?php // public index\n")
LINE  76 | 
LINE  77 |             os.makedirs(os.path.join(temp_dir, ".git"), exist_ok=True)
LINE  78 | 
LINE  79 |             analyzer = ProjectAnalyzer()
LINE  80 |             result = analyzer.analyze(temp_dir)
LINE  81 | 
LINE  82 |             self.assertEqual(result.primary_language, "PHP")
LINE  83 |             self.assertIn("Laravel", result.framework)
LINE  84 |             self.assertEqual(result.package_manager, "Composer")
LINE  85 |             self.assertIn("artisan", result.entry_points)
LINE  86 |             self.assertIn("composer.json", result.config_files)
LINE  87 | 
LINE  88 |             # Check that vendor/ files were excluded from scanned files
LINE  89 |             for f in result.recommended_files:
LINE  90 |                 self.assertFalse(f.startswith("vendor/"))
LINE  91 | 
LINE  92 |             # Check that recommended files include artisan, composer.json, and UserService
LINE  93 |             self.assertIn("artisan", result.recommended_files)
LINE  94 |             self.assertIn("composer.json", result.recommended_files)
LINE  95 |             self.assertTrue(any("UserService.php" in f for f in result.recommended_files))
LINE  96 | 
LINE  97 |             # Check detected excluded dirs
LINE  98 |             self.assertIn("vendor", result.excluded_dirs_found)
LINE  99 |             self.assertIn("public", result.excluded_dirs_found)
LINE 100 |             self.assertIn(".git", result.excluded_dirs_found)
LINE 101 | 
LINE 102 |         finally:
LINE 103 |             shutil.rmtree(temp_dir, ignore_errors=True)
LINE 104 | 
LINE 105 |     def test_analyze_quasar_project(self):
LINE 106 |         """Analyzes a synthetic Quasar/Vue project structure."""
LINE 107 |         temp_dir = tempfile.mkdtemp(prefix="test_quasar_")
LINE 108 |         try:
LINE 109 |             # Create synthetic Quasar files
LINE 110 |             with open(os.path.join(temp_dir, "quasar.config.js"), "w", encoding="utf-8") as f:
LINE 111 |                 f.write("module.exports = function () { return { boot: [] }; };\n")
LINE 112 | 
LINE 113 |             with open(os.path.join(temp_dir, "package.json"), "w", encoding="utf-8") as f:
LINE 114 |                 f.write('{\n  "name": "my-quasar-app",\n  "dependencies": {\n    "@quasar/app": "^1.0.0",\n    "vue": "^3.0.0"\n  }\n}')
LINE 115 | 
LINE 116 |             os.makedirs(os.path.join(temp_dir, "src", "pages"), exist_ok=True)
LINE 117 |             index_page = os.path.join(temp_dir, "src", "pages", "IndexPage.vue")
LINE 118 |             with open(index_page, "w", encoding="utf-8") as f:
LINE 119 |                 f.write("<template><q-page>Hello Quasar</q-page></template>\n<script>\nexport default {}\n</script>\n")
LINE 120 | 
LINE 121 |             os.makedirs(os.path.join(temp_dir, "src", "boot"), exist_ok=True)
LINE 122 |             with open(os.path.join(temp_dir, "src", "boot", "axios.js"), "w", encoding="utf-8") as f:
LINE 123 |                 f.write("import axios from 'axios';\n")
LINE 124 | 
LINE 125 |             # Create directories that should be excluded: .quasar, node_modules, dist
LINE 126 |             os.makedirs(os.path.join(temp_dir, ".quasar"), exist_ok=True)
LINE 127 |             os.makedirs(os.path.join(temp_dir, "node_modules", "vue"), exist_ok=True)
LINE 128 |             os.makedirs(os.path.join(temp_dir, "dist", "spa"), exist_ok=True)
LINE 129 | 
LINE 130 |             analyzer = ProjectAnalyzer()
LINE 131 |             result = analyzer.analyze(temp_dir)
LINE 132 | 
LINE 133 |             self.assertIn("Quasar", result.framework)
LINE 134 |             self.assertIn("npm", result.package_manager)
LINE 135 |             self.assertIn("quasar.config.js", result.config_files)
LINE 136 |             self.assertIn("package.json", result.config_files)
LINE 137 | 
LINE 138 |             # Recommended files should include quasar.config.js and src/pages/IndexPage.vue
LINE 139 |             self.assertIn("quasar.config.js", result.recommended_files)
LINE 140 |             self.assertIn("package.json", result.recommended_files)
LINE 141 |             self.assertTrue(any("IndexPage.vue" in f for f in result.recommended_files))
LINE 142 | 
LINE 143 |             # Excluded dirs detected
LINE 144 |             self.assertIn(".quasar", result.excluded_dirs_found)
LINE 145 |             self.assertIn("node_modules", result.excluded_dirs_found)
LINE 146 |             self.assertIn("dist", result.excluded_dirs_found)
LINE 147 | 
LINE 148 |         finally:
LINE 149 |             shutil.rmtree(temp_dir, ignore_errors=True)
LINE 150 | 
LINE 151 |     def test_checkbox_treeview_set_checked_files(self):
LINE 152 |         """Tests that CheckboxTreeview.set_checked_files selectively marks items."""
LINE 153 |         root = tk.Tk()
LINE 154 |         try:
LINE 155 |             tree = CheckboxTreeview(root)
LINE 156 |             f1 = tree.insert_folder("", "app")
LINE 157 |             item1 = tree.insert_file(f1, "app/main.py", is_checked=True)
LINE 158 |             item2 = tree.insert_file(f1, "app/utils.py", is_checked=True)
LINE 159 |             item3 = tree.insert_file("", "requirements.txt", is_checked=True)
LINE 160 | 
LINE 161 |             self.assertEqual(len(tree.get_checked_files()), 3)
LINE 162 | 
LINE 163 |             # Now set checked files to only app/main.py and requirements.txt
LINE 164 |             tree.set_checked_files({"app/main.py", "requirements.txt"})
LINE 165 | 
LINE 166 |             checked = set(tree.get_checked_files())
LINE 167 |             self.assertEqual(checked, {"app/main.py", "requirements.txt"})
LINE 168 |             self.assertNotIn("app/utils.py", checked)
LINE 169 |             self.assertEqual(tree.set(item2, "check"), "☐")
LINE 170 |             self.assertEqual(tree.set(item1, "check"), "☑")
LINE 171 |             self.assertEqual(tree.set(item3, "check"), "☑")
LINE 172 |         finally:
LINE 173 |             root.destroy()
LINE 174 | 
LINE 175 |     def test_max_file_size_line_counting_limit(self):
LINE 176 |         """Tests that files exceeding max_file_size_mb leave lines_in_file = 0 without reading."""
LINE 177 |         temp_dir = tempfile.mkdtemp(prefix="test_max_size_")
LINE 178 |         try:
LINE 179 |             # Create a file with content
LINE 180 |             large_file = os.path.join(temp_dir, "large.py")
LINE 181 |             with open(large_file, "w", encoding="utf-8") as f:
LINE 182 |                 f.write("line\n" * 100)
LINE 183 | 
LINE 184 |             analyzer = ProjectAnalyzer(allowed_extensions={".py"})
LINE 185 |             # Pass max_file_size_mb tiny enough so 100 lines (~500 bytes) exceeds max_file_bytes
LINE 186 |             result = analyzer.analyze(temp_dir, max_file_size_mb=0.0001)  # ~104 bytes max
LINE 187 | 
LINE 188 |             large_file_info = next(f for f in result.large_files if f["path"] == "large.py")
LINE 189 |             self.assertGreater(large_file_info["size_bytes"], 0)
LINE 190 |             self.assertEqual(large_file_info["lines"], 0)
LINE 191 |             self.assertEqual(result.total_lines, 0)
LINE 192 |         finally:
LINE 193 |             shutil.rmtree(temp_dir, ignore_errors=True)
LINE 194 | 
LINE 195 |     def test_extension_filtering_before_binary_check(self):
LINE 196 |         """Tests that unallowed extensions are skipped before binary check."""
LINE 197 |         temp_dir = tempfile.mkdtemp(prefix="test_ext_filter_")
LINE 198 |         try:
LINE 199 |             # Create an unallowed extension file with null bytes (binary-like)
LINE 200 |             disallowed_file = os.path.join(temp_dir, "test.unknown")
LINE 201 |             with open(disallowed_file, "wb") as f:
LINE 202 |                 f.write(b"some\x00data")
LINE 203 | 
LINE 204 |             analyzer = ProjectAnalyzer(allowed_extensions={".py"})
LINE 205 |             result = analyzer.analyze(temp_dir)
LINE 206 | 
LINE 207 |             self.assertEqual(result.total_files, 0)
LINE 208 |         finally:
LINE 209 |             shutil.rmtree(temp_dir, ignore_errors=True)
LINE 210 | 
LINE 211 |     def test_detect_framework_python_scan_limit(self):
LINE 212 |         """Tests that _detect_framework inspects at most 150 .py files."""
LINE 213 |         temp_dir = tempfile.mkdtemp(prefix="test_fw_limit_")
LINE 214 |         try:
LINE 215 |             # Create 160 dummy .py files
LINE 216 |             for i in range(160):
LINE 217 |                 with open(os.path.join(temp_dir, f"file_{i:03d}.py"), "w", encoding="utf-8") as f:
LINE 218 |                     f.write("# empty python file\n")
LINE 219 | 
LINE 220 |             # Create 161st file with django import
LINE 221 |             with open(os.path.join(temp_dir, "file_160.py"), "w", encoding="utf-8") as f:
LINE 222 |                 f.write("import django\n")
LINE 223 | 
LINE 224 |             analyzer = ProjectAnalyzer(allowed_extensions={".py"})
LINE 225 |             result = analyzer.analyze(temp_dir)
LINE 226 | 
LINE 227 |             # Since files are sorted (file_000 to file_160), file_160.py is the 161st file.
LINE 228 |             # Only 150 files should be inspected, so django in file_160.py should not be reached.
LINE 229 |             self.assertNotIn("Django", result.framework)
LINE 230 |         finally:
LINE 231 |             shutil.rmtree(temp_dir, ignore_errors=True)
LINE 232 | 
LINE 233 | 
LINE 234 | if __name__ == "__main__":
LINE 235 |     unittest.main()
LINE 236 | 
```