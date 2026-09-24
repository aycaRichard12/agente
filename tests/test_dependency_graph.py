import os
import shutil
import tempfile
import unittest

from app.core.dependency_graph import DependencyResolver


class TestDependencyResolver(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="test_dep_graph_")

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _write(self, rel_path, content):
        path = os.path.join(self.tmp, rel_path)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

    def test_file_without_dependencies(self):
        self._write("a.py", "x = 1\n")
        resolver = DependencyResolver(self.tmp)
        node = resolver.build_tree("a.py")
        self.assertEqual(node.rel_path, "a.py")
        self.assertEqual(node.children, [])

    def test_single_dependency(self):
        self._write("a.py", "import b\n")
        self._write("b.py", "x = 1\n")
        resolver = DependencyResolver(self.tmp)
        node = resolver.build_tree("a.py")
        self.assertEqual(len(node.children), 1)
        self.assertEqual(node.children[0].rel_path, "b.py")

    def test_chain_dependencies(self):
        self._write("a.py", "import b\n")
        self._write("b.py", "import c\n")
        self._write("c.py", "x = 1\n")
        resolver = DependencyResolver(self.tmp)
        node = resolver.build_tree("a.py")
        self.assertEqual(node.children[0].rel_path, "b.py")
        self.assertEqual(node.children[0].children[0].rel_path, "c.py")

    def test_circular_dependency(self):
        self._write("a.py", "import b\n")
        self._write("b.py", "import c\n")
        self._write("c.py", "import a\n")
        resolver = DependencyResolver(self.tmp)
        node = resolver.build_tree("a.py")
        c = node.children[0].children[0]
        self.assertEqual(c.rel_path, "c.py")
        self.assertTrue(c.children[0].is_cycle)

    def test_repeated_dependency(self):
        self._write("a.py", "import b\nimport c\n")
        self._write("b.py", "import d\n")
        self._write("c.py", "import d\n")
        self._write("d.py", "x = 1\n")
        resolver = DependencyResolver(self.tmp)
        node = resolver.build_tree("a.py")
        b = next(ch for ch in node.children if ch.rel_path == "b.py")
        c = next(ch for ch in node.children if ch.rel_path == "c.py")
        self.assertEqual(b.children[0].rel_path, "d.py")
        self.assertEqual(c.children[0].rel_path, "d.py")
        self.assertTrue(c.children[0].is_repeated)

    def test_external_dependency_ignored(self):
        self._write("a.py", "import os\n")
        resolver = DependencyResolver(self.tmp)
        node = resolver.build_tree("a.py")
        self.assertEqual(node.children, [])

    def test_missing_dependency_ignored(self):
        self._write("a.py", "import missing_module\n")
        resolver = DependencyResolver(self.tmp)
        node = resolver.build_tree("a.py")
        self.assertEqual(node.children, [])


if __name__ == "__main__":
    unittest.main()
