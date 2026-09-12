"""
Unit tests for ProjectAnalyzer and related components.
"""
import os
import sys
import shutil
import tempfile
import unittest
import tkinter as tk

# Ensure root directory is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.core.project_analyzer import ProjectAnalyzer, ProjectAnalysisResult
from app.gui.file_tree import CheckboxTreeview


class TestProjectAnalyzer(unittest.TestCase):

    def test_analyze_current_project(self):
        """Analyzes the current repository and verifies language, framework, and entry points."""
        current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        analyzer = ProjectAnalyzer()
        result = analyzer.analyze(current_dir)

        self.assertIsInstance(result, ProjectAnalysisResult)
        self.assertEqual(result.primary_language, "Python")
        self.assertEqual(result.framework, "Tkinter")
        self.assertIn("pip", result.package_manager.lower())
        self.assertIn("main.py", result.entry_points)
        self.assertTrue(result.total_files > 0)
        self.assertTrue(result.total_lines > 0)
        self.assertTrue(len(result.recommended_files) > 0)
        self.assertIn("main.py", result.recommended_files)

        # Check exclusions list
        self.assertIn("vendor", result.configured_exclusions)
        self.assertIn(".quasar", result.configured_exclusions)
        self.assertIn(".github", result.configured_exclusions)
        self.assertIn("public", result.configured_exclusions)

        # Check formatted report generation
        report = result.to_formatted_report()
        self.assertIn("REPORTE DE ANÁLISIS AUTOMÁTICO", report)
        self.assertIn("Python", report)
        self.assertIn("Tkinter", report)

    def test_analyze_laravel_project(self):
        """Analyzes a synthetic Laravel project structure."""
        temp_dir = tempfile.mkdtemp(prefix="test_laravel_")
        try:
            # Create synthetic Laravel files
            with open(os.path.join(temp_dir, "artisan"), "w", encoding="utf-8") as f:
                f.write("#!/usr/bin/env php\n<?php\ndefine('LARAVEL_START', microtime(true));\n")

            with open(os.path.join(temp_dir, "composer.json"), "w", encoding="utf-8") as f:
                f.write('{\n  "name": "laravel/laravel",\n  "require": {\n    "php": "^8.2",\n    "laravel/framework": "^11.0"\n  }\n}')

            os.makedirs(os.path.join(temp_dir, "app", "Services"), exist_ok=True)
            user_svc = os.path.join(temp_dir, "app", "Services", "UserService.php")
            with open(user_svc, "w", encoding="utf-8") as f:
                f.write("<?php\nnamespace App\\Services;\nclass UserService {\n  public function getUser() {}\n}\n")

            os.makedirs(os.path.join(temp_dir, "routes"), exist_ok=True)
            with open(os.path.join(temp_dir, "routes", "web.php"), "w", encoding="utf-8") as f:
                f.write("<?php\nuse Illuminate\\Support\\Facades\\Route;\nRoute::get('/', function () { return view('welcome'); });\n")

            # Create directories that should be excluded: vendor, public, .git
            os.makedirs(os.path.join(temp_dir, "vendor", "laravel"), exist_ok=True)
            with open(os.path.join(temp_dir, "vendor", "laravel", "test.php"), "w", encoding="utf-8") as f:
                f.write("<?php // vendor code\n")

            os.makedirs(os.path.join(temp_dir, "public", "build"), exist_ok=True)
            with open(os.path.join(temp_dir, "public", "index.php"), "w", encoding="utf-8") as f:
                f.write("<?php // public index\n")

            os.makedirs(os.path.join(temp_dir, ".git"), exist_ok=True)

            analyzer = ProjectAnalyzer()
            result = analyzer.analyze(temp_dir)

            self.assertEqual(result.primary_language, "PHP")
            self.assertIn("Laravel", result.framework)
            self.assertEqual(result.package_manager, "Composer")
            self.assertIn("artisan", result.entry_points)
            self.assertIn("composer.json", result.config_files)

            # Check that vendor/ files were excluded from scanned files
            for f in result.recommended_files:
                self.assertFalse(f.startswith("vendor/"))

            # Check that recommended files include artisan, composer.json, and UserService
            self.assertIn("artisan", result.recommended_files)
            self.assertIn("composer.json", result.recommended_files)
            self.assertTrue(any("UserService.php" in f for f in result.recommended_files))

            # Check detected excluded dirs
            self.assertIn("vendor", result.excluded_dirs_found)
            self.assertIn("public", result.excluded_dirs_found)
            self.assertIn(".git", result.excluded_dirs_found)

        finally:
            shutil.rmtree(temp_dir, ignore_errors=True)

    def test_analyze_quasar_project(self):
        """Analyzes a synthetic Quasar/Vue project structure."""
        temp_dir = tempfile.mkdtemp(prefix="test_quasar_")
        try:
            # Create synthetic Quasar files
            with open(os.path.join(temp_dir, "quasar.config.js"), "w", encoding="utf-8") as f:
                f.write("module.exports = function () { return { boot: [] }; };\n")

            with open(os.path.join(temp_dir, "package.json"), "w", encoding="utf-8") as f:
                f.write('{\n  "name": "my-quasar-app",\n  "dependencies": {\n    "@quasar/app": "^1.0.0",\n    "vue": "^3.0.0"\n  }\n}')

            os.makedirs(os.path.join(temp_dir, "src", "pages"), exist_ok=True)
            index_page = os.path.join(temp_dir, "src", "pages", "IndexPage.vue")
            with open(index_page, "w", encoding="utf-8") as f:
                f.write("<template><q-page>Hello Quasar</q-page></template>\n<script>\nexport default {}\n</script>\n")

            os.makedirs(os.path.join(temp_dir, "src", "boot"), exist_ok=True)
            with open(os.path.join(temp_dir, "src", "boot", "axios.js"), "w", encoding="utf-8") as f:
                f.write("import axios from 'axios';\n")

            # Create directories that should be excluded: .quasar, node_modules, dist
            os.makedirs(os.path.join(temp_dir, ".quasar"), exist_ok=True)
            os.makedirs(os.path.join(temp_dir, "node_modules", "vue"), exist_ok=True)
            os.makedirs(os.path.join(temp_dir, "dist", "spa"), exist_ok=True)

            analyzer = ProjectAnalyzer()
            result = analyzer.analyze(temp_dir)

            self.assertIn("Quasar", result.framework)
            self.assertIn("npm", result.package_manager)
            self.assertIn("quasar.config.js", result.config_files)
            self.assertIn("package.json", result.config_files)

            # Recommended files should include quasar.config.js and src/pages/IndexPage.vue
            self.assertIn("quasar.config.js", result.recommended_files)
            self.assertIn("package.json", result.recommended_files)
            self.assertTrue(any("IndexPage.vue" in f for f in result.recommended_files))

            # Excluded dirs detected
            self.assertIn(".quasar", result.excluded_dirs_found)
            self.assertIn("node_modules", result.excluded_dirs_found)
            self.assertIn("dist", result.excluded_dirs_found)

        finally:
            shutil.rmtree(temp_dir, ignore_errors=True)

    def test_checkbox_treeview_set_checked_files(self):
        """Tests that CheckboxTreeview.set_checked_files selectively marks items."""
        root = tk.Tk()
        try:
            tree = CheckboxTreeview(root)
            f1 = tree.insert_folder("", "app")
            item1 = tree.insert_file(f1, "app/main.py", is_checked=True)
            item2 = tree.insert_file(f1, "app/utils.py", is_checked=True)
            item3 = tree.insert_file("", "requirements.txt", is_checked=True)

            self.assertEqual(len(tree.get_checked_files()), 3)

            # Now set checked files to only app/main.py and requirements.txt
            tree.set_checked_files({"app/main.py", "requirements.txt"})

            checked = set(tree.get_checked_files())
            self.assertEqual(checked, {"app/main.py", "requirements.txt"})
            self.assertNotIn("app/utils.py", checked)
            self.assertEqual(tree.set(item2, "check"), "☐")
            self.assertEqual(tree.set(item1, "check"), "☑")
            self.assertEqual(tree.set(item3, "check"), "☑")
        finally:
            root.destroy()


if __name__ == "__main__":
    unittest.main()
