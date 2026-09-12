"""
GUI integration test for MainWindow project analysis workflow.
"""
import os
import sys
import unittest
from unittest.mock import patch
import tkinter as tk

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.gui.main_window import MainWindow
from app.gui.analysis_dialog import ProjectAnalysisDialog
from app.core.project_analyzer import ProjectAnalyzer


class TestGuiIntegration(unittest.TestCase):

    @patch("app.gui.dialogs.show_info")
    def test_main_window_analysis_and_apply(self, mock_show_info):
        root = tk.Tk()
        try:
            app = MainWindow(root)
            current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

            # Simulate folder selection
            app.selector.set_folder(current_dir)
            app.var_folder.set(current_dir)
            app.reload_tree()

            initial_files = app.tree.get_checked_files()
            self.assertTrue(len(initial_files) > 0)

            # Analyze project
            analyzer = ProjectAnalyzer(excluded_dirs=app.selector.get_selection().excluded_dirs)
            result = analyzer.analyze(current_dir)

            self.assertIn("main.py", result.recommended_files)

            # Test applying selection
            target_selection = ["main.py", "requirements.txt"]
            app.apply_recommended_selection(target_selection)

            checked = set(app.tree.get_checked_files())
            self.assertEqual(checked, set(target_selection))
            self.assertEqual(app.sv_sel_files.get(), "2")

            # Test opening ProjectAnalysisDialog
            dialog = ProjectAnalysisDialog(
                root,
                analysis=result,
                on_apply_selection=app.apply_recommended_selection
            )
            # Ensure dialog populated recommended checkboxes
            self.assertTrue(len(dialog.file_vars) > 0)
            selected_in_dialog = dialog.get_selected_recommended_files()
            self.assertTrue(len(selected_in_dialog) > 0)

            # Simulate clicking apply selection from dialog
            dialog._on_apply_clicked()

            # Verify selection updated
            final_checked = set(app.tree.get_checked_files())
            self.assertTrue(len(final_checked) > 0)

        finally:
            root.destroy()


if __name__ == "__main__":
    unittest.main()
