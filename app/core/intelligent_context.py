"""
Intelligent Context Analyzer engine.
Analyzes problem descriptions, matches filenames and content symbols,
inspects dependency graphs, assigns priority levels (Critical, Important, Related, Secondary),
and enforces size/file count constraints prioritizing high-relevance code files.
"""
import os
import re
from dataclasses import dataclass
from typing import List, Dict, Set, Tuple, Optional

from app.core.dependency_detector import DependencyDetector
from app.utils.file_utils import get_file_size, is_binary_file, safe_read_file


PRIORITY_CRITICAL = 1
PRIORITY_IMPORTANT = 2
PRIORITY_RELATED = 3
PRIORITY_SECONDARY = 4

PRIORITY_META = {
    PRIORITY_CRITICAL: {"icon": "🔴", "label": "Crítico", "desc": "Archivo directamente involucrado en el problema"},
    PRIORITY_IMPORTANT: {"icon": "🟠", "label": "Importante", "desc": "Dependencia directa o flujo afectado"},
    PRIORITY_RELATED: {"icon": "🟡", "label": "Relacionado", "desc": "Dependencia indirecta o configuración relevante"},
    PRIORITY_SECONDARY: {"icon": "⚪", "label": "Secundario", "desc": "Archivo de contexto general o débilmente relacionado"},
}

STOP_WORDS = {
    "error", "failed", "failure", "issue", "bug", "problem", "cannot", "cant",
    "unable", "to", "in", "the", "a", "an", "of", "and", "or", "for", "with",
    "de", "del", "la", "el", "en", "con", "un", "una", "al", "para", "por", "que",
    "no", "se", "es", "al", "los", "las", "su", "sus", "como"
}


@dataclass
class PrioritizedFile:
    rel_path: str
    abs_path: str
    priority_level: int  # 1: Critical, 2: Important, 3: Related, 4: Secondary
    score: float
    reason: str
    size_bytes: int
    is_selected: bool = True

    @property
    def priority_icon(self) -> str:
        return PRIORITY_META.get(self.priority_level, {}).get("icon", "⚪")

    @property
    def priority_label(self) -> str:
        return PRIORITY_META.get(self.priority_level, {}).get("label", "Secundario")


class IntelligentContextAnalyzer:
    """Analyzes problem description & project files to prioritize relevant context."""

    def __init__(self):
        self.detector = DependencyDetector()

    def analyze(
        self,
        folder_path: str,
        candidate_rel_files: List[str],
        problem_desc: str,
        max_file_size_mb: float = 2.0,
        max_total_size_mb: float = 50.0,
        max_files: int = 100,
    ) -> List[PrioritizedFile]:
        """
        Main entry point for intelligent context analysis.
        Returns list of PrioritizedFile sorted by priority (1 to 4) then score.
        """
        if not candidate_rel_files:
            return []

        # Step 1: Tokenize & extract keywords from problem description
        keywords, key_phrases = self._extract_keywords(problem_desc)

        # Map rel_path -> full abs_path & read content snippets for code files
        file_map: Dict[str, str] = {}
        content_map: Dict[str, str] = {}
        size_map: Dict[str, int] = {}

        max_read_bytes = int(max_file_size_mb * 1024 * 1024)

        for rel_f in candidate_rel_files:
            abs_f = rel_f if os.path.isabs(rel_f) else os.path.join(folder_path, rel_f) if folder_path else rel_f
            file_map[rel_f] = abs_f
            if os.path.isfile(abs_f) and not is_binary_file(abs_f):
                sz = get_file_size(abs_f)
                size_map[rel_f] = sz
                # Safe read snippet up to 64KB for symbol analysis
                content_map[rel_f] = safe_read_file(abs_f, max_bytes=min(sz, 65536))
            else:
                size_map[rel_f] = 0
                content_map[rel_f] = ""

        # Step 2: Calculate initial keyword & filename relevance scores
        scores: Dict[str, float] = {}
        reasons: Dict[str, List[str]] = {}
        direct_matches: Set[str] = set()

        for rel_f, content in content_map.items():
            score, matched_reasons, is_direct = self._score_file(rel_f, content, keywords, key_phrases)
            scores[rel_f] = score
            reasons[rel_f] = matched_reasons
            if is_direct:
                direct_matches.add(rel_f)

        # Step 3: Dependency Graph Analysis (imports & references)
        # Build dependency adjacency lists (file -> imported modules/files)
        deps_map: Dict[str, List[str]] = {}
        for rel_f, content in content_map.items():
            if content:
                deps_map[rel_f] = self.detector.detect_file_dependencies(rel_f, content)
            else:
                deps_map[rel_f] = []

        # Find direct dependencies & reverse references of Critical (direct match) files
        critical_files: Set[str] = set(direct_matches)

        # If no keywords matched directly, pick top-scoring files as critical if score > 0
        if not critical_files and scores:
            top_scored = [f for f, s in sorted(scores.items(), key=lambda x: x[1], reverse=True) if s > 0]
            if top_scored:
                critical_files.update(top_scored[:3])

        important_files: Set[str] = set()
        related_files: Set[str] = set()

        # Step 4: Propagate priorities via dependency graph
        # Direct dependencies or importers of Critical files become Important
        for rel_f in candidate_rel_files:
            if rel_f in critical_files:
                continue

            # Check if rel_f imports any critical file or is imported by any critical file
            is_important = False
            for crit_f in critical_files:
                crit_stem = os.path.splitext(os.path.basename(crit_f))[0].lower()
                f_stem = os.path.splitext(os.path.basename(rel_f))[0].lower()

                # Does rel_f reference crit_f?
                for dep in deps_map.get(rel_f, []):
                    if crit_stem in dep.lower() or crit_f.lower() in dep.lower():
                        is_important = True
                        reasons[rel_f].append(f"Importa el archivo crítico {crit_f}")
                        break

                # Does crit_f reference rel_f?
                if not is_important:
                    for dep in deps_map.get(crit_f, []):
                        if f_stem in dep.lower() or rel_f.lower() in dep.lower():
                            is_important = True
                            reasons[rel_f].append(f"Utilizado por el archivo crítico {crit_f}")
                            break

                if is_important:
                    break

            if is_important:
                important_files.add(rel_f)

        # Database/Config files or indirect dependencies become Related
        config_patterns = re.compile(r'(?:config|database|db|setting|env|router|index|main|app|server)', re.IGNORECASE)
        for rel_f in candidate_rel_files:
            if rel_f in critical_files or rel_f in important_files:
                continue

            base_name = os.path.basename(rel_f)
            if config_patterns.search(base_name):
                related_files.add(rel_f)
                reasons[rel_f].append("Archivo de configuración / entrada global")
            elif scores.get(rel_f, 0) > 0:
                related_files.add(rel_f)
                reasons[rel_f].append("Coincidencia parcial de términos")

        # Step 5: Assign priority levels
        result_files: List[PrioritizedFile] = []

        for rel_f in candidate_rel_files:
            if rel_f in critical_files:
                level = PRIORITY_CRITICAL
                reason_str = "; ".join(reasons.get(rel_f, [])) or "Coincidencia directa con el problema"
            elif rel_f in important_files:
                level = PRIORITY_IMPORTANT
                reason_str = "; ".join(reasons.get(rel_f, [])) or "Dependencia directa de un archivo crítico"
            elif rel_f in related_files:
                level = PRIORITY_RELATED
                reason_str = "; ".join(reasons.get(rel_f, [])) or "Configuración o coincidencia indirecta"
            else:
                level = PRIORITY_SECONDARY
                reason_str = "Archivo secundario del proyecto"

            result_files.append(PrioritizedFile(
                rel_path=rel_f,
                abs_path=file_map[rel_f],
                priority_level=level,
                score=scores.get(rel_f, 0.0),
                reason=reason_str,
                size_bytes=size_map.get(rel_f, 0),
                is_selected=True
            ))

        # Step 6: Sort by priority (1 to 4) then score desc
        result_files.sort(key=lambda x: (x.priority_level, -x.score, x.rel_path))

        # Step 7: Apply context limits (auto-uncheck files that exceed max limits)
        self.apply_limits(
            result_files,
            max_files=max_files,
            max_file_size_mb=max_file_size_mb,
            max_total_size_mb=max_total_size_mb
        )

        return result_files

    def apply_limits(
        self,
        files: List[PrioritizedFile],
        max_files: int,
        max_file_size_mb: float,
        max_total_size_mb: float,
    ) -> None:
        """
        Enforces MAX_FILES, MAX_FILE_SIZE, and MAX_TOTAL_SIZE limits.
        Higher-priority files are checked first; exceeding files have is_selected = False.
        """
        cumulative_bytes = 0
        selected_count = 0
        max_file_bytes = int(max_file_size_mb * 1024 * 1024)
        max_total_bytes = int(max_total_size_mb * 1024 * 1024)

        for pf in files:
            # Skip if oversize single file
            if pf.size_bytes > max_file_bytes:
                pf.is_selected = False
                pf.reason += f" [Omitido: excede {max_file_size_mb:g}MB por archivo]"
                continue

            # Skip if max_files limit reached
            if selected_count >= max_files:
                pf.is_selected = False
                pf.reason += f" [Omitido: excede límite de {max_files} archivos]"
                continue

            # Skip if max_total_bytes reached
            if cumulative_bytes + pf.size_bytes > max_total_bytes:
                pf.is_selected = False
                pf.reason += f" [Omitido: excede límite de tamaño acumulado ({max_total_size_mb:g}MB)]"
                continue

            # Include file
            pf.is_selected = True
            selected_count += 1
            cumulative_bytes += pf.size_bytes

    def _extract_keywords(self, problem_desc: str) -> Tuple[Set[str], List[str]]:
        """Extracts individual tokens and key multi-word phrases from problem description."""
        if not problem_desc:
            return set(), []

        cleaned = problem_desc.lower()
        # Find snake_case or camelCase or slash paths or dot notations
        tokens = re.findall(r'[a-z0-9_\-\.\/]+', cleaned)

        keywords: Set[str] = set()
        key_phrases: List[str] = []

        for t in tokens:
            # Split slash paths or dot notation
            sub_parts = re.split(r'[\/\.]', t)
            for part in sub_parts:
                part_clean = part.strip("_ -")
                if len(part_clean) > 2 and part_clean not in STOP_WORDS:
                    keywords.add(part_clean)
                    # Add singular/plural variants
                    if part_clean.endswith("s") and len(part_clean) > 3:
                        keywords.add(part_clean[:-1])
                    elif not part_clean.endswith("s"):
                        keywords.add(part_clean + "s")
                    
                    # Add verb stem variants (-ing, -ed, -tion)
                    if part_clean.endswith("ing") and len(part_clean) > 5:
                        keywords.add(part_clean[:-3])
                        keywords.add(part_clean[:-3] + "e")
                    elif part_clean.endswith("ed") and len(part_clean) > 4:
                        keywords.add(part_clean[:-2])
                        keywords.add(part_clean[:-1])
                    elif part_clean.endswith("tion") and len(part_clean) > 6:
                        keywords.add(part_clean[:-4] + "te")

        # Multi-word phrase extraction (e.g. "creating users" -> "create user", "users")
        words = [w for w in re.findall(r'[a-z0-9]+', cleaned) if len(w) > 2 and w not in STOP_WORDS]
        for i in range(len(words) - 1):
            key_phrases.append(f"{words[i]} {words[i+1]}")

        return keywords, key_phrases

    def _score_file(
        self,
        rel_path: str,
        content: str,
        keywords: Set[str],
        key_phrases: List[str]
    ) -> Tuple[float, List[str], bool]:
        """Calculates relevance score and determines if file is a direct match."""
        score = 0.0
        reasons: List[str] = []
        is_direct = False

        norm_rel = rel_path.lower().replace("\\", "/")
        file_stem = os.path.splitext(os.path.basename(norm_rel))[0]
        path_parts = norm_rel.split("/")

        # 1. Filename & Path Matching
        for kw in keywords:
            if kw in file_stem:
                score += 15.0
                reasons.append(f"Nombre de archivo contiene '{kw}'")
                is_direct = True
            elif any(kw in part for part in path_parts):
                score += 8.0
                reasons.append(f"Ruta de archivo contiene '{kw}'")
                is_direct = True

        # 2. Content Symbol & Keyword Matching
        if content:
            lower_content = content.lower()
            for kw in keywords:
                occurrences = lower_content.count(kw)
                if occurrences > 0:
                    score += min(occurrences * 1.5, 10.0)
                    # Check if keyword is part of class or function definition
                    if re.search(r'(?:class|def|function|interface|type|struct)\s+\w*' + re.escape(kw), lower_content):
                        score += 12.0
                        is_direct = True
                        reasons.append(f"Define símbolo/clase/función '{kw}'")
                    elif not any(kw in r for r in reasons):
                        reasons.append(f"Contenido menciona '{kw}' ({occurrences} veces)")

            for phrase in key_phrases:
                if phrase in lower_content:
                    score += 5.0

        return score, reasons, is_direct
