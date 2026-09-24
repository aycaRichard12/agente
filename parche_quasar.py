#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
parche_quasar.py  (v2 - sin regex)
Añade resolución de alias Quasar/Vue a app/core/dependency_graph.py
"""
import argparse
import shutil
import sys
from datetime import datetime
from pathlib import Path


NEW_RESOLVER = '''    def _resolve_js_dep(self, source_rel: str, dep: str) -> List[str]:
        m = re.search(r'[\\'"]([^\\'"]+)[\\'"]', dep)
        if not m:
            return []

        raw = m.group(1).strip()

        # 1. Import relativo: "./x" o "../x"
        if raw.startswith("."):
            base_dir = os.path.dirname(source_rel)
            target = os.path.normpath(os.path.join(base_dir, raw)).replace("\\\\", "/")
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
'''


def log(msg, level="INFO"):
    prefix = {"INFO": "[INFO]", "OK": "[ OK ]", "WARN": "[WARN]",
              "ERR": "[FAIL]", "SKIP": "[SKIP]"}.get(level, "[INFO]")
    print(f"{prefix} {msg}")


def find_method_range(text: str, method_name: str) -> tuple:
    """
    Encuentra (start, end) del bloque del método `method_name` dentro de la clase.
    El método debe estar indentado con 4 espacios.
    Devuelve (-1, -1) si no se encuentra.
    """
    header = f"    def {method_name}("
    start = text.find(header)
    if start == -1:
        return -1, -1

    # Buscar siguiente '    def ' (4 espacios + def) después de la línea del header
    first_nl = text.find("\n", start)
    if first_nl == -1:
        return -1, -1

    search_from = first_nl + 1
    next_def = text.find("\n    def ", search_from)
    if next_def == -1:
        # Es el último método del archivo
        end = len(text)
    else:
        end = next_def + 1  # conservar el \n inicial del siguiente método

    return start, end


def patch_file(path: Path, dry_run: bool = False) -> bool:
    text = path.read_text(encoding="utf-8")

    if "_resolve_js_alias" in text and "_js_candidates" in text:
        log("El parche Quasar ya está aplicado.", "SKIP")
        return True

    start, end = find_method_range(text, "_resolve_js_dep")
    if start == -1:
        log("No se localizó 'def _resolve_js_dep' con indentación de 4 espacios.", "ERR")
        log("Verifica que dependency_graph.py existe y tiene ese método.", "ERR")
        return False

    log(f"Rango detectado: {start}..{end} ({end - start} caracteres)")
    old_block = text[start:end]
    log(f"Primera línea del bloque: {old_block.splitlines()[0]!r}")

    new_text = text[:start] + NEW_RESOLVER + "\n" + text[end:]

    try:
        compile(new_text, str(path), "exec")
    except SyntaxError as e:
        log(f"Sintaxis inválida tras el parche: línea {e.lineno}: {e.msg}", "ERR")
        lines = new_text.split("\n")
        for i in range(max(0, e.lineno - 4), min(len(lines), e.lineno + 3)):
            marker = ">>>" if i == e.lineno - 1 else "   "
            print(f"  {marker} {i+1:5d} | {lines[i]}")
        return False

    if dry_run:
        log("(dry-run) dependency_graph.py se puede parchear correctamente", "SKIP")
        return True

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    bak = path.with_name(path.name + f".{ts}.bak")
    shutil.copy2(path, bak)
    log(f"Respaldo: {bak}", "OK")

    path.write_text(new_text, encoding="utf-8")
    log(f"Parcheado: {path}", "OK")
    return True


def main():
    ap = argparse.ArgumentParser(description="Parche Quasar/Vue para dependency_graph.py")
    ap.add_argument("root", nargs="?", default=".", help="Raíz del proyecto")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    target = root / "app" / "core" / "dependency_graph.py"
    if not target.is_file():
        log(f"No existe: {target}", "ERR")
        sys.exit(1)

    log(f"Raíz: {root}")
    log(f"Target: {target}")
    log(f"Dry-run: {args.dry_run}")
    print()

    if patch_file(target, dry_run=args.dry_run):
        log("=== Listo. Reinicia la GUI y vuelve a probar el árbol de dependencias ===", "OK")
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()