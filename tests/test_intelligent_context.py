"""
Unit tests for IntelligentContextAnalyzer and related prioritizing components.
"""
import os
import shutil
import tempfile
import unittest

from app.core.intelligent_context import (
    IntelligentContextAnalyzer,
    PRIORITY_CRITICAL,
    PRIORITY_IMPORTANT,
    PRIORITY_RELATED,
    PRIORITY_SECONDARY
)


class TestIntelligentContextAnalyzer(unittest.TestCase):

    def test_extract_keywords(self):
        analyzer = IntelligentContextAnalyzer()
        keywords, phrases = analyzer._extract_keywords("Error creating users in database")
        self.assertIn("user", keywords)
        self.assertIn("users", keywords)
        self.assertIn("database", keywords)
        self.assertIn("create", keywords)

    def test_prioritization_levels(self):
        temp_dir = tempfile.mkdtemp(prefix="test_intelligent_ctx_")
        try:
            # Create synthetic project structure matching prompt example
            os.makedirs(os.path.join(temp_dir, "routes"), exist_ok=True)
            routes_user = os.path.join(temp_dir, "routes", "users.py")
            with open(routes_user, "w", encoding="utf-8") as f:
                f.write("from services.user_service import create_user\n\ndef create_user_route():\n    create_user()\n")

            os.makedirs(os.path.join(temp_dir, "controllers"), exist_ok=True)
            ctrl_user = os.path.join(temp_dir, "controllers", "user.py")
            with open(ctrl_user, "w", encoding="utf-8") as f:
                f.write("from models.user import UserModel\n\nclass UserController:\n    pass\n")

            os.makedirs(os.path.join(temp_dir, "models"), exist_ok=True)
            model_user = os.path.join(temp_dir, "models", "user.py")
            with open(model_user, "w", encoding="utf-8") as f:
                f.write("class UserModel:\n    pass\n")

            os.makedirs(os.path.join(temp_dir, "services"), exist_ok=True)
            svc_user = os.path.join(temp_dir, "services", "user_service.py")
            with open(svc_user, "w", encoding="utf-8") as f:
                f.write("def create_user():\n    pass\n")

            os.makedirs(os.path.join(temp_dir, "config"), exist_ok=True)
            cfg_db = os.path.join(temp_dir, "config", "database.py")
            with open(cfg_db, "w", encoding="utf-8") as f:
                f.write("DB_HOST = 'localhost'\n")

            unrelated = os.path.join(temp_dir, "unrelated.py")
            with open(unrelated, "w", encoding="utf-8") as f:
                f.write("print('hello world')\n")

            candidates = [
                "routes/users.py",
                "controllers/user.py",
                "models/user.py",
                "services/user_service.py",
                "config/database.py",
                "unrelated.py"
            ]

            analyzer = IntelligentContextAnalyzer()
            prioritized = analyzer.analyze(
                folder_path=temp_dir,
                candidate_rel_files=candidates,
                problem_desc="Error creating users"
            )

            pmap = {p.rel_path: p.priority_level for p in prioritized}

            # routes/users.py, controllers/user.py, models/user.py -> Critical 🔴
            self.assertEqual(pmap["routes/users.py"], PRIORITY_CRITICAL)
            self.assertEqual(pmap["controllers/user.py"], PRIORITY_CRITICAL)
            self.assertEqual(pmap["models/user.py"], PRIORITY_CRITICAL)

            # services/user_service.py -> Important 🟠 (dependency of routes/users.py & user match)
            self.assertIn(pmap["services/user_service.py"], (PRIORITY_CRITICAL, PRIORITY_IMPORTANT))

            # config/database.py -> Related 🟡 (database config)
            self.assertEqual(pmap["config/database.py"], PRIORITY_RELATED)

            # unrelated.py -> Secondary ⚪
            self.assertEqual(pmap["unrelated.py"], PRIORITY_SECONDARY)

        finally:
            shutil.rmtree(temp_dir, ignore_errors=True)

    def test_limit_enforcement_prioritization(self):
        temp_dir = tempfile.mkdtemp(prefix="test_limits_")
        try:
            # Create 5 files
            for name in ["crit1.py", "crit2.py", "sec1.py", "sec2.py", "sec3.py"]:
                with open(os.path.join(temp_dir, name), "w", encoding="utf-8") as f:
                    f.write(f"# content for {name}\n" * 10)

            analyzer = IntelligentContextAnalyzer()
            candidates = ["crit1.py", "crit2.py", "sec1.py", "sec2.py", "sec3.py"]
            # Set problem to target crit files
            prioritized = analyzer.analyze(
                folder_path=temp_dir,
                candidate_rel_files=candidates,
                problem_desc="crit1 crit2",
                max_files=2  # Limit to 2 files max
            )

            selected = [p.rel_path for p in prioritized if p.is_selected]
            self.assertEqual(len(selected), 2)
            self.assertIn("crit1.py", selected)
            self.assertIn("crit2.py", selected)
        finally:
            shutil.rmtree(temp_dir, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
