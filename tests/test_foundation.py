import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class FoundationTests(unittest.TestCase):
    def test_missing_files_and_broken_link_fail(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "README.md").write_text("[broken](absent.md)")
            errors = load("validate").validate(root)
            self.assertTrue(any("Missing" in e for e in errors))
            self.assertTrue(any("Broken link" in e for e in errors))

    @unittest.skipUnless((ROOT / "projects").exists(), "Generator source lives in foundation")
    def test_generated_products_validate_and_remain_separate(self):
        initializer = load("initialize_project")
        with tempfile.TemporaryDirectory() as temp:
            for product in initializer.PRODUCTS:
                target = Path(temp) / product
                initializer.initialize(product, target)
                self.assertEqual([], load("validate").validate(target))
                self.assertEqual((ROOT / "projects" / product / "DOMAIN_RULES.md").read_text(),
                                 (target / "docs/DOMAIN_RULES.md").read_text())
                self.assertFalse((target / ".git").exists())
                self.assertFalse((target / "projects").exists())

    def test_existing_destination_is_preserved(self):
        with tempfile.TemporaryDirectory() as temp:
            sentinel = Path(temp) / "existing.txt"
            sentinel.write_text("retain")
            with self.assertRaises(FileExistsError):
                load("initialize_project").initialize("logistics-crosscheck", temp)
            self.assertEqual("retain", sentinel.read_text())

    def test_unknown_product_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "new"
            with self.assertRaises(ValueError):
                load("initialize_project").initialize("unknown", target)
            self.assertFalse(target.exists())
