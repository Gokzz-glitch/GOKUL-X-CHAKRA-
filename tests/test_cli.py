from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
PYTHON = sys.executable


class MemoryCliTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.root = Path(self.temp_dir.name)
        self.db = self.root / "memory.sqlite3"
        self.env = os.environ.copy()
        self.env["PYTHONPATH"] = str(PROJECT / "src")

    def run_cli(self, *args):
        return subprocess.run(
            [PYTHON, "-m", "chakra_memory", "--db", str(self.db), *args],
            cwd=PROJECT,
            env=self.env,
            text=True,
            capture_output=True,
        )

    def test_memory_lifecycle_and_markdown_export(self):
        initialized = self.run_cli("init")
        self.assertEqual(initialized.returncode, 0, initialized.stderr)
        self.assertTrue(self.db.exists())

        added = self.run_cli(
            "add",
            "--kind", "fact",
            "--title", "Startup focus",
            "--content", "CHAKRA is developing AI for colonoscopy polyp detection.",
            "--source", "Founder interview",
            "--tag", "healthcare",
        )
        self.assertEqual(added.returncode, 0, added.stderr)
        memory_id = added.stdout.strip()
        self.assertTrue(memory_id)

        found = self.run_cli("search", "colonoscopy")
        self.assertEqual(found.returncode, 0, found.stderr)
        self.assertIn(memory_id, found.stdout)

        shown = self.run_cli("show", memory_id)
        self.assertEqual(shown.returncode, 0, shown.stderr)
        self.assertIn("Founder interview", shown.stdout)
        self.assertIn("polyp detection", shown.stdout)

        export_path = self.root / "exports" / "memory.md"
        exported = self.run_cli("export", "--output", str(export_path))
        self.assertEqual(exported.returncode, 0, exported.stderr)
        self.assertIn("Startup focus", export_path.read_text(encoding="utf-8"))

        archived = self.run_cli("archive", memory_id)
        self.assertEqual(archived.returncode, 0, archived.stderr)
        active = self.run_cli("list")
        self.assertEqual(active.returncode, 0, active.stderr)
        self.assertNotIn(memory_id, active.stdout)
        archived_list = self.run_cli("list", "--archived")
        self.assertEqual(archived_list.returncode, 0, archived_list.stderr)
        self.assertIn(memory_id, archived_list.stdout)


if __name__ == "__main__":
    unittest.main()
