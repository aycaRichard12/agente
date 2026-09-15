"""Tests for Analysis Modes (Problem Mode & Project Mode)."""
import unittest
from app.models.analysis_modes import (
    MODE_PROBLEM, MODE_PROJECT, ANALYSIS_MODES,
    get_analysis_mode_config, AnalysisModeConfig,
)
from app.models.project import ExportConfig, ProjectSelection
from app.generators.standalone_prompt_generator import generate_standalone_prompt
from app.generators.markdown_generator import generate_markdown_bundle
from app.generators.text_generator import generate_text_bundle


class TestAnalysisModeConstants(unittest.TestCase):
    """Verify that mode constants and registry are correct."""

    def test_mode_constants_exist(self):
        self.assertEqual(MODE_PROBLEM, "problem")
        self.assertEqual(MODE_PROJECT, "project")

    def test_both_modes_in_registry(self):
        self.assertIn(MODE_PROBLEM, ANALYSIS_MODES)
        self.assertIn(MODE_PROJECT, ANALYSIS_MODES)

    def test_mode_configs_are_correct_type(self):
        for key, cfg in ANALYSIS_MODES.items():
            self.assertIsInstance(cfg, AnalysisModeConfig)

    def test_get_analysis_mode_config_returns_problem_by_default(self):
        cfg = get_analysis_mode_config("")
        self.assertEqual(cfg.mode, MODE_PROBLEM)

    def test_get_analysis_mode_config_unknown_key_returns_problem(self):
        cfg = get_analysis_mode_config("nonexistent_mode")
        self.assertEqual(cfg.mode, MODE_PROBLEM)

    def test_get_analysis_mode_config_project(self):
        cfg = get_analysis_mode_config(MODE_PROJECT)
        self.assertEqual(cfg.mode, MODE_PROJECT)


class TestStandalonePromptProblemMode(unittest.TestCase):
    """Verify standalone prompt in Problem Mode."""

    def setUp(self):
        self.problem = "El botón de login no responde al hacer clic."
        self.prompt = generate_standalone_prompt(
            problem_desc=self.problem,
            analysis_type="Detect errors",
            analysis_mode=MODE_PROBLEM,
        )

    def test_prompt_contains_reported_problem(self):
        self.assertIn("REPORTED PROBLEM", self.prompt)

    def test_prompt_contains_problem_text(self):
        self.assertIn(self.problem, self.prompt)

    def test_prompt_contains_problem_mode_label(self):
        self.assertIn("Problem Mode", self.prompt)

    def test_prompt_does_not_contain_holistic_audit_heading(self):
        self.assertNotIn("HOLISTIC PROJECT AUDIT", self.prompt)

    def test_prompt_contains_root_cause_section(self):
        self.assertIn("Causa Raíz", self.prompt)

    def test_prompt_contains_files_to_modify(self):
        self.assertIn("FILES TO MODIFY", self.prompt)


class TestStandalonePromptProjectMode(unittest.TestCase):
    """Verify standalone prompt in Project Mode."""

    def setUp(self):
        self.prompt = generate_standalone_prompt(
            problem_desc="",
            analysis_type="Detect errors",
            analysis_mode=MODE_PROJECT,
        )

    def test_prompt_contains_holistic_audit_heading(self):
        self.assertIn("HOLISTIC PROJECT AUDIT", self.prompt)

    def test_prompt_contains_project_mode_label(self):
        self.assertIn("Project Mode", self.prompt)

    def test_prompt_does_not_contain_reported_problem_heading(self):
        self.assertNotIn("REPORTED PROBLEM / PROBLEMA REPORTADO\n", self.prompt)

    def test_prompt_contains_audit_matrix(self):
        self.assertIn("AUDIT MATRIX", self.prompt)

    def test_prompt_contains_action_plan(self):
        self.assertIn("ACTION PLAN", self.prompt)

    def test_prompt_contains_owasp_mention(self):
        self.assertIn("OWASP", self.prompt)

    def test_prompt_contains_dry_mention(self):
        self.assertIn("DRY", self.prompt)


class TestMarkdownGeneratorModes(unittest.TestCase):
    """Verify that markdown_generator adapts content based on analysis_mode."""

    def _make_empty_selection(self):
        return ProjectSelection()

    def test_problem_mode_contains_reported_problem_header(self):
        config = ExportConfig(analysis_mode=MODE_PROBLEM)
        sel = self._make_empty_selection()
        text, *_ = generate_markdown_bundle(sel, "Error en login", config)
        self.assertIn("REPORTED PROBLEM OR GOAL", text)
        self.assertIn("Error en login", text)

    def test_problem_mode_no_holistic_header(self):
        config = ExportConfig(analysis_mode=MODE_PROBLEM)
        sel = self._make_empty_selection()
        text, *_ = generate_markdown_bundle(sel, "Error en login", config)
        self.assertNotIn("HOLISTIC PROJECT AUDIT", text)

    def test_project_mode_contains_holistic_header(self):
        config = ExportConfig(analysis_mode=MODE_PROJECT)
        sel = self._make_empty_selection()
        text, *_ = generate_markdown_bundle(sel, "", config)
        self.assertIn("HOLISTIC PROJECT AUDIT", text)

    def test_project_mode_no_reported_problem_header(self):
        config = ExportConfig(analysis_mode=MODE_PROJECT)
        sel = self._make_empty_selection()
        text, *_ = generate_markdown_bundle(sel, "", config)
        self.assertNotIn("REPORTED PROBLEM OR GOAL", text)

    def test_project_mode_system_instructions_use_mode(self):
        config = ExportConfig(analysis_mode=MODE_PROJECT, include_system_instructions=True)
        sel = self._make_empty_selection()
        text, *_ = generate_markdown_bundle(sel, "", config)
        self.assertIn("MODO PROYECTO", text.upper())

    def test_problem_mode_system_instructions_use_profile(self):
        config = ExportConfig(analysis_mode=MODE_PROBLEM, include_system_instructions=True,
                              analysis_type="Detect errors")
        sel = self._make_empty_selection()
        text, *_ = generate_markdown_bundle(sel, "bug", config)
        self.assertIn("DETECT ERRORS", text.upper())


class TestTextGeneratorModes(unittest.TestCase):
    """Verify that text_generator adapts content based on analysis_mode."""

    def _make_empty_selection(self):
        return ProjectSelection()

    def test_problem_mode_contains_reported_problem_header(self):
        config = ExportConfig(analysis_mode=MODE_PROBLEM)
        sel = self._make_empty_selection()
        text, *_ = generate_text_bundle(sel, "Error 500 en API", config)
        self.assertIn("REPORTED PROBLEM OR GOAL", text)
        self.assertIn("Error 500 en API", text)

    def test_project_mode_contains_holistic_header(self):
        config = ExportConfig(analysis_mode=MODE_PROJECT)
        sel = self._make_empty_selection()
        text, *_ = generate_text_bundle(sel, "", config)
        self.assertIn("HOLISTIC PROJECT AUDIT", text)

    def test_project_mode_system_instructions_use_mode(self):
        config = ExportConfig(analysis_mode=MODE_PROJECT, include_system_instructions=True)
        sel = self._make_empty_selection()
        text, *_ = generate_text_bundle(sel, "", config)
        self.assertIn("MODO PROYECTO", text.upper())

    def test_problem_mode_system_instructions_use_profile(self):
        config = ExportConfig(analysis_mode=MODE_PROBLEM, include_system_instructions=True,
                              analysis_type="Review security")
        sel = self._make_empty_selection()
        text, *_ = generate_text_bundle(sel, "XSS vulnerability", config)
        self.assertIn("REVIEW SECURITY", text.upper())


if __name__ == "__main__":
    unittest.main()
