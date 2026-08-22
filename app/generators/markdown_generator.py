"""Markdown prompt bundle generator with Smart Context (File Extensions Breakdown & Dependencies)."""
import os
from collections import Counter
from datetime import datetime
from typing import Tuple, List, Dict
from app.models.project import ProjectSelection, ExportConfig
from app.core.file_reader import read_and_format_file
from app.core.project_structure import build_folder_tree_str
from app.core.dependency_detector import DependencyDetector
from app.utils.file_utils import is_binary_file, get_file_size, safe_read_file


def generate_markdown_bundle(
    selection: ProjectSelection, 
    problem_desc: str, 
    config: ExportConfig
) -> Tuple[str, int, int, int, int]:
    """
    Generates Markdown document with Smart Context:
    1. REPORTED PROBLEM
    2. PROJECT CONTEXT (Metadata, Extension Frequency Summary, Dependencies, Limits Warnings, Tree)
    3. ATTACHMENTS (Selected Files with LINE X | formatting)

    Returns: (full_text, included_count, excluded_count, oversized_count, total_lines)
    """
    folder_path = selection.folder_path
    project_name = os.path.basename(folder_path) if folder_path else "Proyecto"
    base_path = os.path.abspath(folder_path) if folder_path else "N/A"
    gen_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file_blocks = []
    omitted_warnings: List[Dict[str, str]] = []
    extension_counts: Counter = Counter()
    file_dependencies: Dict[str, List[str]] = {}

    included_count = 0
    excluded_count = 0
    oversized_count = 0
    total_lines = 0

    cumulative_bytes = 0
    max_file_bytes = int(config.max_file_size_mb * 1024 * 1024)
    max_total_bytes = int(config.max_total_size_mb * 1024 * 1024)
    detector = DependencyDetector()

    def process_file(full_path: str, display_name: str):
        nonlocal included_count, excluded_count, oversized_count, total_lines, cumulative_bytes

        ext = os.path.splitext(display_name)[1].lower() or "[sin extensión]"

        # 1. Binary check
        if is_binary_file(full_path):
            excluded_count += 1
            return

        size_bytes = get_file_size(full_path)

        # 2. Check MAX_FILES limit
        if included_count >= config.max_files:
            oversized_count += 1
            omitted_warnings.append({
                "file": display_name,
                "reason": f"Exceeds MAX_FILES limit of {config.max_files} files."
            })
            return

        # 3. Check MAX_FILE_SIZE limit
        if size_bytes > max_file_bytes:
            oversized_count += 1
            omitted_warnings.append({
                "file": display_name,
                "reason": f"Exceeds the allowed limit of {config.max_file_size_mb:g} MB."
            })
            return

        # 4. Check MAX_TOTAL_SIZE limit
        if cumulative_bytes + size_bytes > max_total_bytes:
            oversized_count += 1
            omitted_warnings.append({
                "file": display_name,
                "reason": f"Exceeds MAX_TOTAL_SIZE limit of {config.max_total_size_mb:g} MB (Cumulative size reached)."
            })
            return

        # Read content safely
        raw_text = safe_read_file(full_path, max_bytes=max_file_bytes)
        deps = detector.detect_file_dependencies(display_name, raw_text)
        if deps:
            file_dependencies[display_name] = deps

        formatted_code = read_and_format_file(
            full_path, 
            add_line_numbers=config.add_line_numbers,
            max_file_size_mb=config.max_file_size_mb
        )
        lines_in_file = formatted_code.count('\n') + (1 if formatted_code else 0)
        total_lines += lines_in_file
        cumulative_bytes += size_bytes
        extension_counts[ext] += 1

        code_ext = ext.lstrip('.')
        block = [
            "==============================================================",
            f"FILE: {display_name}",
            "==============================================================",
            f"```{code_ext}",
            formatted_code,
            "```"
        ]
        file_blocks.append("\n".join(block))
        included_count += 1

    # 1. Folder files
    if folder_path and os.path.isdir(folder_path):
        for rel_f in sorted(selection.checked_folder_files):
            full_path = os.path.join(folder_path, rel_f)
            if os.path.isfile(full_path):
                process_file(full_path, rel_f)

    # 2. Individual files
    for abs_f in selection.individual_files:
        if os.path.isfile(abs_f):
            if folder_path and abs_f.startswith(folder_path):
                display_name = os.path.relpath(abs_f, folder_path)
            else:
                display_name = os.path.basename(abs_f)
            process_file(abs_f, display_name)

    doc = []

    # 1. REPORTED PROBLEM
    doc.append("==============================================================")
    doc.append("REPORTED PROBLEM / PROBLEMA REPORTADO")
    doc.append("==============================================================")
    if problem_desc.strip():
        doc.append(problem_desc.strip())
    else:
        doc.append("[No se especificó una descripción del problema]")
    doc.append("\n")

    # 2. PROJECT CONTEXT & SMART SUMMARY
    doc.append("==============================================================")
    doc.append("PROJECT CONTEXT / CONTEXTO DEL PROYECTO")
    doc.append("==============================================================")
    doc.append(f"• Nombre del Proyecto: {project_name}")
    doc.append(f"• Ruta Base: {base_path}")
    doc.append(f"• Fecha de Generación: {gen_date}\n")

    # PROJECT SUMMARY
    doc.append("--------------------------------------------------------------")
    doc.append("PROJECT SUMMARY")
    doc.append("--------------------------------------------------------------")
    doc.append(f"Selected files: {included_count}")
    doc.append("File extensions:")
    if extension_counts:
        for ext_name, count in extension_counts.most_common():
            doc.append(f"  {ext_name}: {count}")
    else:
        doc.append("  (Ningún archivo procesado)")
    doc.append(f"\nTotal lines:\n{total_lines:,}\n")

    # DEPENDENCIES AND REFERENCES
    if file_dependencies:
        doc.append("--------------------------------------------------------------")
        doc.append("DEPENDENCIES AND REFERENCES")
        doc.append("--------------------------------------------------------------")
        for f_name, deps in file_dependencies.items():
            doc.append(f"• {f_name}:")
            for dep in deps:
                doc.append(f"  - {dep}")
        doc.append("")

    # Limits Warning Block
    if omitted_warnings:
        doc.append("--------------------------------------------------------------")
        doc.append("⚠️ ARCHIVOS OMITIDOS POR LÍMITES DE TAMAÑO / OMITTED FILES WARNINGS")
        doc.append("--------------------------------------------------------------")
        for warn in omitted_warnings:
            doc.append(f"File omitted:\n{warn['file']}\nReason:\n{warn['reason']}\n")

    # Mandatory System Response Format Instructions for DeepSeek
    if config.include_system_instructions:
        doc.append("--------------------------------------------------------------")
        doc.append("INSTRUCCIONES OBLIGATORIAS PARA DEEPSEEK / RESPONSE FORMAT RULES")
        doc.append("--------------------------------------------------------------")
        doc.append("Tu respuesta DEBE seguir exactamente la siguiente estructura Markdown:")
        doc.append("""
# DIAGNOSIS
## Problem
[Descripción técnica del problema]
## Root Cause
[Causa raíz técnica]

# FILES TO MODIFY
## 1. ruta/relativa/archivo.ext
Approximate line: [número]
### Problem
[Problema en este archivo]
### Solution
[Solución propuesta]
### Current Code
```
[código actual]
```
### Corrected Code
```
[código corregido]
```

# NEW FILES
[Nuevos archivos requeridos o: No se requieren nuevos archivos.]

# ARCHITECTURAL CHANGES
[Cambios en estructura o: No se requieren cambios arquitectónicos.]

# RISKS OR SIDE EFFECTS
[Riesgos identificados o: Sin riesgos identificados.]

# IMPLEMENTATION PLAN
1. [Primer paso]
2. [Segundo paso]
3. [Tercer paso]
""")
        doc.append("REGLA OBLIGATORIA: No respondas con JSON. Responde con el Markdown estructurado exacto indicado arriba. Especifica siempre archivo, línea aproximada, código actual y código corregido.")

    if config.include_tree and folder_path and os.path.isdir(folder_path):
        tree_str = build_folder_tree_str(folder_path, list(selection.checked_folder_files), selection.excluded_dirs)
        doc.append("\nEstructura de Directorios:")
        doc.append(f"```\n{tree_str}\n```")
    
    doc.append("\n")

    # 3. ATTACHMENTS
    doc.append("==============================================================")
    doc.append("ATTACHMENTS / ARCHIVOS Y CÓDIGO FUENTE")
    doc.append("==============================================================\n")
    doc.append("\n\n".join(file_blocks))

    full_text = "\n".join(doc)
    return full_text, included_count, excluded_count, oversized_count, total_lines
