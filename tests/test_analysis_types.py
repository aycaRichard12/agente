"""
Unit and integration tests for Analysis Types and Profiles.
"""
import os
import sys
import unittest
from unittest.mock import patch
import tkinter as tk

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.models.analysis_types import (
    ANALYSIS_PROFILES, ANALYSIS_TYPE_KEYS, get_analysis_profile, get_all_analysis_types
)
from app.models.project import ExportConfig, ProjectSelection
from app.generators.standalone_prompt_generator import generate_standalone_prompt
from app.generators.markdown_generator import generate_markdown_bundle
from app.generators.text_generator import generate_text_bundle
from app.gui.main_window import MainWindow


class TestAnalysisTypes(unittest.TestCase):

    def test_all_ten_profiles_defined(self):
        """Verifies that all 10 requested analysis profiles exist and are complete."""
        expected_types = [
            "Detect errors",
            "Solve problem",
            "Refactoring",
            "Improve architecture",
            "Optimize performance",
            "Review security",
            "Create new functionality",
            "Explain project",
            "Document project",
            "Comprehensive review",
        ]
        self.assertEqual(get_all_analysis_types(), expected_types)

        for key in expected_types:
            self.assertIn(key, ANALYSIS_PROFILES)
            profile = get_analysis_profile(key)
            self.assertEqual(profile.name, key)
            self.assertTrue(len(profile.objective) > 10, f"Objective too short for {key}")
            self.assertTrue(len(profile.focus) > 10, f"Focus too short for {key}")
            self.assertTrue(len(profile.priorities) > 10, f"Priorities too short for {key}")
            self.assertTrue(len(profile.expected_outcome) > 10, f"Expected outcome too short for {key}")
            self.assertTrue(len(profile.response_instructions) > 10, f"Response instructions too short for {key}")
            self.assertTrue(len(profile.response_template) > 20, f"Response template too short for {key}")
            # Ensure action-oriented wording is present
            self.assertIn("CONCRETO, TÉCNICO", profile.response_instructions)

    def test_generate_standalone_prompt_with_profiles(self):
        """Verifies that standalone prompt incorporates profile objective, focus, priorities, and outcome."""
        for key in ANALYSIS_TYPE_KEYS:
            profile = get_analysis_profile(key)
            prompt = generate_standalone_prompt("Test problem description", analysis_type=key)

            self.assertIn(f"SELECTED ANALYSIS PROFILE: {profile.icon} {profile.name}", prompt)
            self.assertIn(profile.objective, prompt)
            self.assertIn(profile.focus, prompt)
            self.assertIn(profile.priorities, prompt)
            self.assertIn(profile.expected_outcome, prompt)
            self.assertIn(profile.response_instructions, prompt)
            self.assertIn("Test problem description", prompt)

    def test_markdown_and_text_bundle_with_profile(self):
        """Verifies that markdown and text generators include selected profile in context document."""
        selection = ProjectSelection()
        config = ExportConfig(analysis_type="Review security")

        md_text, _, _, _, _ = generate_markdown_bundle(selection, "Vulnerability test", config)
        self.assertIn("Review security", md_text)
        self.assertIn("Auditar el código en busca de vulnerabilidades", md_text)
        self.assertIn("Vulnerability test", md_text)

        txt_text, _, _, _, _ = generate_text_bundle(selection, "Vulnerability test", config)
        self.assertIn("Review security", txt_text)
        self.assertIn("Auditar el código en busca de vulnerabilidades", txt_text)

    def test_main_window_combobox_integration(self):
        """Verifies MainWindow integration with Analysis Type selector and dynamic hint updating."""
        root = tk.Tk()
        try:
            app = MainWindow(root)

            # Check combobox options
            values = list(app.cb_analysis_type["values"])
            self.assertEqual(values, ANALYSIS_TYPE_KEYS)

            # Initial default is "Detect errors"
            self.assertEqual(app.var_analysis_type.get(), "Detect errors")
            profile_detect = get_analysis_profile("Detect errors")
            self.assertIn(profile_detect.objective, app.lbl_profile_hint.cget("text"))

            # Switch to "Optimize performance"
            app.var_analysis_type.set("Optimize performance")
            app._on_analysis_type_changed()

            profile_perf = get_analysis_profile("Optimize performance")
            self.assertIn(profile_perf.objective, app.lbl_profile_hint.cget("text"))
            self.assertIn(profile_perf.default_prompt_hint, app.problem_text.get("1.0", tk.END).strip())

            # Switch to "Review security"
            app.var_analysis_type.set("Review security")
            app._on_analysis_type_changed()

            profile_sec = get_analysis_profile("Review security")
            self.assertIn(profile_sec.objective, app.lbl_profile_hint.cget("text"))
            self.assertIn(profile_sec.default_prompt_hint, app.problem_text.get("1.0", tk.END).strip())

            # User types a custom problem description: should NOT be overwritten when changing types
            custom_problem = "Custom specific critical issue in database connection pool"
            app.problem_text.delete("1.0", tk.END)
            app.problem_text.insert("1.0", custom_problem)

            app.var_analysis_type.set("Refactoring")
            app._on_analysis_type_changed()
            self.assertEqual(app.problem_text.get("1.0", tk.END).strip(), custom_problem)

        finally:
            root.destroy()


if __name__ == "__main__":
    unittest.main()
