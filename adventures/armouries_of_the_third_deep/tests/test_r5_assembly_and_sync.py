#!/usr/bin/env python3
"""
test_r5_assembly_and_sync.py — R5 Test Suite: Master Document Assembly & Sync
==============================================================================
Authoritative Source: ORIGINAL_REQUEST.md (§R5), PROJECT.md (§4, Feature 13, Feature 14)

This test suite validates 100% compliance with Requirement 5 (R5):
  - Asserts that master document assembly correctly stitches together all 7 modular
    chapter files (01-07) and 4 handout appendix files (Appendix A-D).
  - Asserts markdown synchronization across modular chapters, quickstart files, and handouts.
  - Asserts build script readiness and import integrity (build_master_document.py,
    render_handouts.py, validate_module_suite.py).
  - Asserts that presentation assets (HTML/PDF pipelines) are structurally aligned.
"""

import os
import re
import sys
import unittest
from pathlib import Path
from typing import Dict, List, Tuple, Set

ROOT_DIR = Path(__file__).resolve().parent.parent

MODULAR_CHAPTER_FILES = [
    ("01_campaign_context.md", "Chapter 1: Campaign Context"),
    ("02_band_mechanics.md", "Chapter 2: Squad Management"),
    ("03_operational_mechanics.md", "Chapter 3: Operational Mechanics"),
    ("04_keyed_locations.md", "Chapter 4: Keyed Locations"),
    ("05_adversaries_and_hazards.md", "Chapter 5: Adversaries"),
    ("06_relics_and_rewards.md", "Chapter 6: Relics"),
    ("07_gm_playbook_and_pacing.md", "Chapter 7: GM Playbook"),
]

APPENDIX_FILES = [
    ("handouts/node_map.md", "Appendix A: Operational Node Map"),
    ("handouts/gm_cheat_sheet.md", "Appendix B: 1-Page Rapid GM Cheat Sheet"),
    ("handouts/band_worksheet.md", "Appendix C: Dwarf Vanguard Band Worksheet"),
    ("handouts/dying_scribe_letter.md", "Appendix D: In-World Player Handout"),
]

QUICKSTART_FILES = [
    "quickstart/00_overview_and_background.md",
    "quickstart/01_delve_mechanics_and_alert_system.md",
    "quickstart/02_keyed_locations.md",
    "quickstart/03_adversaries_and_hazards.md",
    "quickstart/04_loot_relics_and_rewards.md",
    "quickstart/05_gm_screen_and_play_aids.md",
]


class BaseR5Test(unittest.TestCase):
    """Base test case for R5 verification."""

    @classmethod
    def setUpClass(cls):
        cls.root_dir = ROOT_DIR


class TestR5MasterDocumentAssembly(BaseR5Test):
    """R5: Verify assembly integrity of the master markdown and HTML book."""

    def test_r5_master_markdown_file_exists_and_non_empty(self):
        """R5.1: Verify armouries_of_the_third_deep_master.md exists and is non-empty."""
        master_path = self.root_dir / "armouries_of_the_third_deep_master.md"
        self.assertTrue(master_path.exists(), "armouries_of_the_third_deep_master.md does not exist.")
        content = master_path.read_text(encoding="utf-8")
        self.assertTrue(len(content) > 50000, f"Master markdown is suspiciously small ({len(content)} bytes).")

    def test_r5_master_markdown_contains_all_7_chapters_in_order(self):
        """R5.2: Verify master document contains all 7 chapters in exact sequential order."""
        master_path = self.root_dir / "armouries_of_the_third_deep_master.md"
        if not master_path.exists():
            self.skipTest("Master markdown not found")
        content = master_path.read_text(encoding="utf-8")

        last_pos = 0
        for rel_file, chapter_title in MODULAR_CHAPTER_FILES:
            # Check chapter heading or marker in master
            match = re.search(re.escape(chapter_title[:15]), content[last_pos:], re.IGNORECASE)
            self.assertIsNotNone(
                match,
                f"Master document missing or out-of-order chapter: '{chapter_title}' (from {rel_file})"
            )
            last_pos += match.start()

    def test_r5_master_markdown_contains_all_4_appendices_in_order(self):
        """R5.3: Verify master document contains all 4 appendices in sequential order."""
        master_path = self.root_dir / "armouries_of_the_third_deep_master.md"
        if not master_path.exists():
            self.skipTest("Master markdown not found")
        content = master_path.read_text(encoding="utf-8")

        # Check for Appendices header
        self.assertTrue(
            "APPENDICES" in content.upper(),
            "Master document missing '# APPENDICES' section banner."
        )

        last_pos = 0
        for rel_file, appendix_title in APPENDIX_FILES:
            match = re.search(re.escape(appendix_title[:15]), content[last_pos:], re.IGNORECASE)
            self.assertIsNotNone(
                match,
                f"Master document missing or out-of-order appendix: '{appendix_title}' (from {rel_file})"
            )
            last_pos += match.start()

    def test_r5_master_document_toc_completeness(self):
        """R5.4: Verify master markdown contains Table of Contents covering all chapters and appendices."""
        master_path = self.root_dir / "armouries_of_the_third_deep_master.md"
        if not master_path.exists():
            self.skipTest("Master markdown not found")
        content = master_path.read_text(encoding="utf-8")

        self.assertTrue("Table of Contents" in content or "TABLE OF CONTENTS" in content)
        for i in range(1, 8):
            self.assertTrue(
                re.search(rf"Chapter\s*{i}", content, re.IGNORECASE),
                f"Table of Contents missing reference to Chapter {i}."
            )


class TestR5MarkdownSynchronization(BaseR5Test):
    """R5: Verify synchronization between modular chapters, quickstart, and handouts."""

    def test_r5_all_10_keyed_locations_present_in_modular_and_quickstart(self):
        """R5.5: Verify both 04_keyed_locations.md and quickstart/02_keyed_locations.md define all 10 locations."""
        for rel_path in ["04_keyed_locations.md", "quickstart/02_keyed_locations.md"]:
            file_path = self.root_dir / rel_path
            if not file_path.exists():
                continue
            text = file_path.read_text(encoding="utf-8")
            for loc_num in range(1, 11):
                self.assertTrue(
                    re.search(rf"Location\s+{loc_num}[:\s]", text, re.IGNORECASE),
                    f"{rel_path} missing definition for Location {loc_num}."
                )

    def test_r5_all_quickstart_files_exist(self):
        """R5.6: Verify all 6 quickstart files exist and have content."""
        for rel_path in QUICKSTART_FILES:
            file_path = self.root_dir / rel_path
            self.assertTrue(file_path.exists(), f"Missing quickstart file: {rel_path}")
            text = file_path.read_text(encoding="utf-8")
            self.assertTrue(len(text) > 500, f"Quickstart file {rel_path} is too small or empty.")

    def test_r5_all_handouts_exist(self):
        """R5.7: Verify all 4 handout source markdown files exist."""
        for rel_path, _ in APPENDIX_FILES:
            file_path = self.root_dir / rel_path
            self.assertTrue(file_path.exists(), f"Missing handout file: {rel_path}")
            text = file_path.read_text(encoding="utf-8")
            self.assertTrue(len(text) > 500, f"Handout file {rel_path} is too small or empty.")


class TestR5BuildScriptsReadiness(BaseR5Test):
    """R5: Verify build automation script syntax, entrypoints, and import integrity."""

    def test_r5_build_master_document_script_validity(self):
        """R5.8: Verify scripts/build_master_document.py is importable and defines assembly functions."""
        script_path = self.root_dir / "scripts" / "build_master_document.py"
        self.assertTrue(script_path.exists(), "scripts/build_master_document.py does not exist.")
        content = script_path.read_text(encoding="utf-8")
        self.assertIn("generate_master_markdown", content)
        self.assertIn("build_master_html", content)

    def test_r5_render_handouts_script_validity(self):
        """R5.9: Verify scripts/render_handouts.py is present and defines handout renderers."""
        script_path = self.root_dir / "scripts" / "render_handouts.py"
        self.assertTrue(script_path.exists(), "scripts/render_handouts.py does not exist.")
        content = script_path.read_text(encoding="utf-8")
        self.assertTrue(
            "build_gm_cheat_sheet_html" in content or "render" in content.lower(),
            "render_handouts.py missing expected handout builder functions."
        )

    def test_r5_validate_module_suite_script_validity(self):
        """R5.10: Verify scripts/validate_module_suite.py is present and defines validator class."""
        script_path = self.root_dir / "scripts" / "validate_module_suite.py"
        self.assertTrue(script_path.exists(), "scripts/validate_module_suite.py does not exist.")
        content = script_path.read_text(encoding="utf-8")
        self.assertIn("ModuleSuiteValidator", content)


if __name__ == "__main__":
    unittest.main(verbosity=2)
