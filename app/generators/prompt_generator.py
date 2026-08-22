"""Prompt generator orchestrator."""
from typing import Tuple
from app.models.project import ProjectSelection, ExportConfig
from app.generators.markdown_generator import generate_markdown_bundle
from app.generators.text_generator import generate_text_bundle


class PromptGenerator:
    def __init__(self, config: ExportConfig = None):
        self.config = config or ExportConfig()

    def generate(self, selection: ProjectSelection, problem_desc: str) -> Tuple[str, int, int, int, int]:
        """
        Generates document bundle.
        Returns: (full_text, included_count, excluded_count, oversized_count, total_lines)
        """
        if self.config.output_format == "text":
            return generate_text_bundle(selection, problem_desc, self.config)
        return generate_markdown_bundle(selection, problem_desc, self.config)
