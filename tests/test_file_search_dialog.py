"""Unit tests for project scanner caching and FileSearchDialog optimizations."""
import os
import shutil
import tempfile
import time
import unittest
import tkinter as tk

from app.core.project_scanner import scan_directory, clear_scan_cache, _SCAN_CACHE
from app.gui.file_search_dialog import FileSearchDialog, MAX_RENDER_LIMIT


class TestProjectScannerCache(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.mkdtemp(prefix="test_scanner_")
        clear_scan_cache()

    def tearDown(self):
        clear_scan_cache()
        shutil.rmtree(self.tmp_dir, ignore_errors=True)

    def _create_file(self, rel_path: str, content: str = "test"):
        full = os.path.join(self.tmp_dir, rel_path)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8") as f:
            f.write(content)

    def test_scan_directory_caching(self):
        self._create_file("file1.txt")
        self._create_file("file2.py")

        res1 = scan_directory(self.tmp_dir, excluded_dirs=set(), use_cache=True)
        self.assertEqual(res1, ["file1.txt", "file2.py"])
        self.assertEqual(len(_SCAN_CACHE), 1)

        # Second call should use cache
        res2 = scan_directory(self.tmp_dir, excluded_dirs=set(), use_cache=True)
        self.assertEqual(res2, ["file1.txt", "file2.py"])

    def test_cache_invalidation_on_folder_mtime_change(self):
        self._create_file("file1.txt")
        res1 = scan_directory(self.tmp_dir, excluded_dirs=set(), use_cache=True)
        self.assertEqual(res1, ["file1.txt"])

        # Sleep briefly to ensure mtime timestamp differs on filesystem
        time.sleep(0.05)
        # Touch folder / add new file to change folder mtime
        self._create_file("file2.txt")
        os.utime(self.tmp_dir, None)

        res2 = scan_directory(self.tmp_dir, excluded_dirs=set(), use_cache=True)
        self.assertEqual(res2, ["file1.txt", "file2.txt"])


class TestFileSearchDialogGUI(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.mkdtemp(prefix="test_dialog_")
        self.root = tk.Tk()
        self.root.withdraw()

        # Create dummy files
        for i in range(15):
            path = os.path.join(self.tmp_dir, f"module_{i:02d}.py")
            with open(path, "w", encoding="utf-8") as f:
                f.write(f"# File {i}\n")

    def tearDown(self):
        try:
            self.root.destroy()
        except Exception:
            pass
        shutil.rmtree(self.tmp_dir, ignore_errors=True)

    def test_dialog_async_load_and_rendering(self):
        dialog = FileSearchDialog(self.root, self.tmp_dir)

        # Process mainloop events to allow background thread & after callbacks to execute
        start_time = time.time()
        while len(dialog.all_files) == 0 and (time.time() - start_time) < 2.0:
            self.root.update()

        self.assertEqual(len(dialog.all_files), 15)

        # Process remaining render batch callbacks
        for _ in range(10):
            self.root.update()

        children = dialog.scroll_frame.winfo_children()
        self.assertTrue(len(children) >= 15)

        dialog.destroy()

    def test_dialog_search_filter(self):
        dialog = FileSearchDialog(self.root, self.tmp_dir)

        start_time = time.time()
        while len(dialog.all_files) == 0 and (time.time() - start_time) < 2.0:
            self.root.update()

        # Set search query
        dialog.search_var.set("module_05")

        # Allow debouncing after callback to fire
        for _ in range(10):
            time.sleep(0.02)
            self.root.update()

        children = [
            c for c in dialog.scroll_frame.winfo_children()
            if isinstance(c, tk.Frame)
        ]
        self.assertEqual(len(children), 1)

        dialog.destroy()

    def test_dialog_scan_cancellation_on_destroy(self):
        dialog = FileSearchDialog(self.root, self.tmp_dir)
        # Immediately destroy dialog before background scan finishes
        dialog.destroy()
        self.root.update()

        # Ensure no TclError or unhandled exception occurs
        time.sleep(0.1)
        self.root.update()

    def test_hard_render_limit(self):
        # Create directory with 600 files
        big_dir = tempfile.mkdtemp(prefix="test_big_")
        try:
            for i in range(600):
                with open(os.path.join(big_dir, f"file_{i:03d}.txt"), "w") as f:
                    f.write("x")

            dialog = FileSearchDialog(self.root, big_dir)

            start_time = time.time()
            while len(dialog.all_files) < 600 and (time.time() - start_time) < 3.0:
                self.root.update()

            self.assertEqual(len(dialog.all_files), 600)

            # Process render batches
            for _ in range(20):
                self.root.update()

            # Rows rendered should be limited to MAX_RENDER_LIMIT + 1 (footer)
            row_frames = [
                c for c in dialog.scroll_frame.winfo_children()
                if isinstance(c, tk.Frame)
            ]
            self.assertEqual(len(row_frames), MAX_RENDER_LIMIT + 1)

            dialog.destroy()
        finally:
            shutil.rmtree(big_dir, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
