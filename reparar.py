#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
reparar.py
Repara app/gui/main_window.py después de la inserción incorrecta
del bloque auto-generado por apply_changes.py.

Uso:
    python reparar.py                    # usa el directorio actual
    python reparar.py /ruta/al/agente
    python reparar.py --dry-run          # solo muestra
"""

import argparse
import shutil
import sys
from datetime import datetime
from pathlib import Path


ANCHOR      = "    def on_copy_clipboard(self):\n"
START_MARK  = "    # === AUTO-GENERATED: file_search_dependency_feature ===\n"
END_MARK    = "    # === END AUTO-GENERATED ===\n"


def log(msg, level="INFO"):
    prefix = {"INFO": "[INFO]", "OK": "[ OK ]", "WARN": "[WARN]",
              "ERR": "[FAIL]", "SKIP": "[SKIP]"}.get(level, "[INFO]")
    print(f"{prefix} {msg}")


def check_syntax(path: Path, src: str) -> bool:
    try:
        compile(src, str(path), "exec")
        return True
    except SyntaxError as e:
        log(f"Sintaxis inválida en {path.name} línea {e.lineno}: {e.msg}", "ERR")
        lines = src.split("\n")
        for i in range(max(0, e.lineno - 4), min(len(lines), e.lineno + 3)):
            marker = ">>>" if i == e.lineno - 1 else "   "
            print(f"  {marker} {i+1:4d} | {lines[i]}")
        return False


def repair_main_window(root: Path, dry_run: bool = False) -> bool:
    mw = root / "app" / "gui" / "main_window.py"
    if not mw.is_file():
        log(f"No existe: {mw}", "ERR")
        return False

    text = mw.read_text(encoding="utf-8")

    # 1. Localizar el anchor
    anchor_pos = text.find(ANCHOR)
    if anchor_pos == -1:
        log("No se encontró 'def on_copy_clipboard'", "WARN")
        return check_syntax(mw, text)

    after_anchor = anchor_pos + len(ANCHOR)

    # 2. Verificar si el bloque está justo después (mal ubicado)
    start_pos = text.find(START_MARK, after_anchor)
    if start_pos == -1:
        log("No hay bloque auto-generado tras on_copy_clipboard. Nada que reparar.", "SKIP")
        return check_syntax(mw, text)

    between = text[after_anchor:start_pos]
    if between.strip() != "":
        log(f"Contenido inesperado entre anchor y bloque: {between!r}", "WARN")
        return check_syntax(mw, text)

    # 3. Localizar fin del bloque
    end_pos = text.find(END_MARK, start_pos)
    if end_pos == -1:
        log("No se encontró el marcador de fin del bloque", "ERR")
        return False
    end_pos += len(END_MARK)

    block = text[start_pos:end_pos]

    # 4. Eliminar el bloque y el relleno que había entre anchor y bloque
    text = text[:after_anchor] + text[end_pos:]

    # 5. Insertar el bloque ANTES del anchor
    new_anchor_pos = text.find(ANCHOR)
    if new_anchor_pos == -1:
        log("Se perdió el anchor tras la extracción", "ERR")
        return False

    insertion = block
    if not insertion.endswith("\n"):
        insertion += "\n"
    text = text[:new_anchor_pos] + insertion + "\n" + text[new_anchor_pos:]

    # 6. Verificar sintaxis antes de escribir
    if not check_syntax(mw, text):
        return False

    if dry_run:
        log("(dry-run) main_window.py se puede reparar correctamente", "SKIP")
        return True

    # 7. Backup + escritura
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    bak = mw.with_name(mw.name + f".{ts}.bak")
    shutil.copy2(mw, bak)
    log(f"Respaldo: {bak}", "OK")

    mw.write_text(text, encoding="utf-8")
    log(f"Reparado: {mw}", "OK")
    return True


def main():
    parser = argparse.ArgumentParser(description="Repara main_window.py")
    parser.add_argument("root", nargs="?", default=".", help="Raíz del proyecto")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not (root / "app" / "gui" / "main_window.py").is_file():
        log(f"No parece ser la raíz del proyecto: {root}", "ERR")
        sys.exit(1)

    log(f"Raíz: {root}")
    log(f"Dry-run: {args.dry_run}")
    print()

    if repair_main_window(root, dry_run=args.dry_run):
        log("=== Listo. Ejecuta ./iniciar_deepseek_debugger.sh ===", "OK")
    else:
        log("=== La reparación falló. Revisa el archivo manualmente ===", "ERR")
        sys.exit(1)


if __name__ == "__main__":
    main()