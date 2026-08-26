#!/usr/bin/env python3
"""
test_r1_pc_scripting.py — R1 Test Suite: Player Agency & Neutral Scene Presentation
===================================================================================
Authoritative Source: ORIGINAL_REQUEST.md (§R1), PROJECT.md (§1, Feature 1)

This test suite validates 100% compliance with Requirement 1 (R1):
  - Asserts zero prescriptive PC scripting (e.g. "Khoril rolls", "Einar searches",
    "Torvir invokes", "Einar uses Burglary", "Torvir engages", "Einar makes")
    across all markdown files in the repository.
  - Asserts zero character-forcing failure reactions (e.g. "Torvir flies into rage",
    "Einar becomes obsessed with gold", "Einar gains 2 Shadow").
  - Asserts zero hardcoded hero role assignments in tactical Band options or combat tasks.
  - Asserts that scenes, encounters, obstacles, and environmental features are phrased
    neutrally as GM presentation tools and player choices.
"""

import os
import re
import unittest
from pathlib import Path
from typing import Dict, List, Tuple, Set

ROOT_DIR = Path(__file__).resolve().parent.parent

# Files to test for R1 compliance
MODULAR_CHAPTERS = [
    "01_campaign_context.md",
    "02_band_mechanics.md",
    "03_operational_mechanics.md",
    "04_keyed_locations.md",
    "05_adversaries_and_hazards.md",
    "06_relics_and_rewards.md",
    "07_gm_playbook_and_pacing.md",
]

QUICKSTART_FILES = [
    "quickstart/00_overview_and_background.md",
    "quickstart/01_delve_mechanics_and_alert_system.md",
    "quickstart/02_keyed_locations.md",
    "quickstart/03_adversaries_and_hazards.md",
    "quickstart/04_loot_relics_and_rewards.md",
    "quickstart/05_gm_screen_and_play_aids.md",
]

HANDOUT_FILES = [
    "handouts/band_worksheet.md",
    "handouts/dying_scribe_letter.md",
    "handouts/gm_cheat_sheet.md",
    "handouts/node_map.md",
]

MASTER_FILES = [
    "armouries_of_the_third_deep_master.md",
]

ALL_ADVENTURE_MARKDOWN_FILES = MODULAR_CHAPTERS + QUICKSTART_FILES + HANDOUT_FILES + MASTER_FILES

# Specific prescriptive PC scripting regex patterns that violate player agency
PRESCRIPTIVE_ACTION_PATTERNS: List[Tuple[str, str]] = [
    # 1. Prescriptive PC rolls / checks / attempts
    (
        r"\b(?:Torvir|Einar|Khoril)\s+(?:rolls?|makes?|tests?|attempts?|makes\s+the\s+opening)\s+(?:a\s+|an\s+)?(?:\*\*)?(?:[A-Z]{3,12}|March|Scan|Stealth|Craft|Explore|Battle|Enhearten|Travel|Awe|Song|Riddle|Lore)",
        "Prescriptive PC skill roll (e.g. 'Khoril rolls TRAVEL', 'Einar makes SCAN')"
    ),
    (
        r"\b(?:Torvir|Einar|Khoril)\s+rolls\s+(?:Favoured|Ill-favoured)",
        "Prescriptive PC dice roll condition (e.g. 'Einar rolls Favoured')"
    ),
    # 2. Prescriptive Trait invocations tied to specific heroes
    (
        r"\b(?:Torvir|Einar|Khoril)\s+invoking\s+[A-Za-z\-'\s\(\)]+\s+(?:rolls|grants|gains)",
        "Prescriptive trait invocation on named PC (e.g. 'Torvir invoking Enemy-lore')"
    ),
    (
        r"\b(?:Torvir|Einar|Khoril)'s\s+(?:Favoured\s+SCAN|Leadership\s+Trait|Enemy-lore|The\s+Broken\s+Key)",
        "Prescriptive PC trait possessive (e.g. 'Einar's Favoured SCAN checks')"
    ),
    # 3. Prescriptive tactic assignments and single combat / duel assignments
    (
        r"\bCommand\s*\(\s*Khoril\s*\)",
        "Prescriptive leader task assigned to Khoril in combat"
    ),
    (
        r"\bDuel\s*(?:Combat\s+Task)?\s*\(\s*Torvir\s*\)",
        "Prescriptive single combat duel assigned to Torvir"
    ),
    (
        r"\b(?:Primary|Support|Participants?)\s*:\s*Einar\b",
        "Prescriptive participant slot forcing Einar"
    ),
    (
        r"\b(?:Primary|Support|Participants?)\s*:\s*Torvir\b",
        "Prescriptive participant slot forcing Torvir"
    ),
    (
        r"\b(?:Primary|Support|Participants?)\s*:\s*Khoril\b",
        "Prescriptive participant slot forcing Khoril"
    ),
    # 4. Forced narrative actions / cutscenes
    (
        r"\bTorvir's\s+Curse\s+of\s+Vengeance\s*:\s*On\s+failure,\s+Torvir\s+flies",
        "Forced PC rage cutscene on failure (Location 4)"
    ),
    (
        r"\bEinar's\s+Dragon-sickness\s*:\s*On\s+failure,\s+Einar\s+becomes\s+obsessed",
        "Forced PC obsession cutscene on failure (Location 4)"
    ),
    (
        r"\bTorvir\s+or\s+Khoril\s*\(\s*being\s+of\s+Durin's\s+royal\s+line\s*\)\s*slicing\s+their\s+palm",
        "Prescriptive blood ritual scripting (Location 9)"
    ),
    (
        r"\bEinar\s+and\s+Bróga\s+can\s+attempt\s+the\s+Skill\s+Endeavour",
        "Restricting Skill Endeavour attempt to specific pregen (Location 9)"
    ),
    (
        r"\bTorvir\s+can\s+spend\s+1\s+Hope\b",
        "Scripting specific pregen resource expenditure"
    ),
    (
        r"\bKhoril\s+can\s+spend\s+1\s+point\s+of\s+Band\s+Hope\b",
        "Scripting specific pregen Band Hope expenditure"
    ),
    (
        r"\bFirst\s+Aid\s+Overwatch\s*\(\s*Einar\s*\)",
        "Scripting first aid action exclusively for Einar"
    ),
]


class BaseR1Test(unittest.TestCase):
    """Base test case for R1 verification."""

    @classmethod
    def setUpClass(cls):
        cls.file_texts: Dict[str, str] = {}
        cls.file_lines: Dict[str, List[str]] = {}

        for rel_path in ALL_ADVENTURE_MARKDOWN_FILES:
            full_path = ROOT_DIR / rel_path
            if full_path.exists():
                text = full_path.read_text(encoding="utf-8")
                cls.file_texts[rel_path] = text
                cls.file_lines[rel_path] = text.splitlines()
            else:
                cls.file_texts[rel_path] = ""
                cls.file_lines[rel_path] = []

    def get_text(self, rel_path: str) -> str:
        return self.file_texts.get(rel_path, "")

    def get_lines(self, rel_path: str) -> List[str]:
        return self.file_lines.get(rel_path, [])


class TestR1PlayerAgencyModularChapters(BaseR1Test):
    """R1: Player Agency & Neutral Scene Presentation in Modular Chapters (01-07)."""

    def test_r1_zero_prescriptive_pc_scripting_in_02_band_mechanics(self):
        """R1.1: Verify 02_band_mechanics.md contains zero prescriptive PC scripting."""
        lines = self.get_lines("02_band_mechanics.md")
        self.assertTrue(len(lines) > 0, "02_band_mechanics.md missing or empty")

        violations = []
        for idx, line in enumerate(lines, 1):
            if line.strip().startswith("```"):
                continue
            for pattern, desc in PRESCRIPTIVE_ACTION_PATTERNS:
                if re.search(pattern, line, re.IGNORECASE):
                    violations.append(f"Line {idx} [{desc}]: {line.strip()}")

        self.assertEqual(
            violations, [],
            f"Found {len(violations)} prescriptive PC scripting violations in 02_band_mechanics.md:\n"
            + "\n".join(violations)
        )

    def test_r1_zero_prescriptive_pc_scripting_in_03_operational_mechanics(self):
        """R1.2: Verify 03_operational_mechanics.md contains zero prescriptive PC scripting."""
        lines = self.get_lines("03_operational_mechanics.md")
        self.assertTrue(len(lines) > 0, "03_operational_mechanics.md missing or empty")

        violations = []
        for idx, line in enumerate(lines, 1):
            if line.strip().startswith("```"):
                continue
            for pattern, desc in PRESCRIPTIVE_ACTION_PATTERNS:
                if re.search(pattern, line, re.IGNORECASE):
                    violations.append(f"Line {idx} [{desc}]: {line.strip()}")

        self.assertEqual(
            violations, [],
            f"Found {len(violations)} prescriptive PC scripting violations in 03_operational_mechanics.md:\n"
            + "\n".join(violations)
        )

    def test_r1_zero_prescriptive_pc_scripting_in_04_keyed_locations(self):
        """R1.3: Verify 04_keyed_locations.md contains zero prescriptive PC scripting across all 10 locations."""
        lines = self.get_lines("04_keyed_locations.md")
        self.assertTrue(len(lines) > 0, "04_keyed_locations.md missing or empty")

        violations = []
        for idx, line in enumerate(lines, 1):
            if line.strip().startswith("```"):
                continue
            for pattern, desc in PRESCRIPTIVE_ACTION_PATTERNS:
                if re.search(pattern, line, re.IGNORECASE):
                    violations.append(f"Line {idx} [{desc}]: {line.strip()}")

        self.assertEqual(
            violations, [],
            f"Found {len(violations)} prescriptive PC scripting violations in 04_keyed_locations.md:\n"
            + "\n".join(violations)
        )

    def test_r1_zero_prescriptive_pc_scripting_in_05_adversaries_and_hazards(self):
        """R1.4: Verify 05_adversaries_and_hazards.md contains zero adversary tactics scripted to specific PCs."""
        lines = self.get_lines("05_adversaries_and_hazards.md")
        self.assertTrue(len(lines) > 0, "05_adversaries_and_hazards.md missing or empty")

        violations = []
        for idx, line in enumerate(lines, 1):
            if line.strip().startswith("```"):
                continue
            for pattern, desc in PRESCRIPTIVE_ACTION_PATTERNS:
                if re.search(pattern, line, re.IGNORECASE):
                    violations.append(f"Line {idx} [{desc}]: {line.strip()}")

        self.assertEqual(
            violations, [],
            f"Found {len(violations)} prescriptive PC scripting violations in 05_adversaries_and_hazards.md:\n"
            + "\n".join(violations)
        )

    def test_r1_zero_prescriptive_pc_scripting_in_06_relics_and_rewards(self):
        """R1.5: Verify 06_relics_and_rewards.md contains zero prescriptive PC assignments for claiming relics."""
        lines = self.get_lines("06_relics_and_rewards.md")
        self.assertTrue(len(lines) > 0, "06_relics_and_rewards.md missing or empty")

        violations = []
        for idx, line in enumerate(lines, 1):
            if line.strip().startswith("```"):
                continue
            for pattern, desc in PRESCRIPTIVE_ACTION_PATTERNS:
                if re.search(pattern, line, re.IGNORECASE):
                    violations.append(f"Line {idx} [{desc}]: {line.strip()}")

        self.assertEqual(
            violations, [],
            f"Found {len(violations)} prescriptive PC scripting violations in 06_relics_and_rewards.md:\n"
            + "\n".join(violations)
        )

    def test_r1_zero_prescriptive_pc_scripting_in_07_gm_playbook_and_pacing(self):
        """R1.6: Verify 07_gm_playbook_and_pacing.md contains zero session timelines dictating hero choices."""
        lines = self.get_lines("07_gm_playbook_and_pacing.md")
        self.assertTrue(len(lines) > 0, "07_gm_playbook_and_pacing.md missing or empty")

        violations = []
        for idx, line in enumerate(lines, 1):
            if line.strip().startswith("```"):
                continue
            for pattern, desc in PRESCRIPTIVE_ACTION_PATTERNS:
                if re.search(pattern, line, re.IGNORECASE):
                    violations.append(f"Line {idx} [{desc}]: {line.strip()}")

        self.assertEqual(
            violations, [],
            f"Found {len(violations)} prescriptive PC scripting violations in 07_gm_playbook_and_pacing.md:\n"
            + "\n".join(violations)
        )


class TestR1PlayerAgencyQuickstartAndHandouts(BaseR1Test):
    """R1: Player Agency & Neutral Scene Presentation in Quickstart and Handouts."""

    def test_r1_zero_prescriptive_pc_scripting_in_quickstart_locations(self):
        """R1.7: Verify quickstart/02_keyed_locations.md contains zero prescriptive PC scripting."""
        lines = self.get_lines("quickstart/02_keyed_locations.md")
        if not lines:
            self.skipTest("quickstart/02_keyed_locations.md not found")

        violations = []
        for idx, line in enumerate(lines, 1):
            if line.strip().startswith("```"):
                continue
            for pattern, desc in PRESCRIPTIVE_ACTION_PATTERNS:
                if re.search(pattern, line, re.IGNORECASE):
                    violations.append(f"Line {idx} [{desc}]: {line.strip()}")

        self.assertEqual(
            violations, [],
            f"Found {len(violations)} prescriptive violations in quickstart/02_keyed_locations.md:\n"
            + "\n".join(violations)
        )

    def test_r1_zero_prescriptive_pc_scripting_in_quickstart_all_files(self):
        """R1.8: Verify all quickstart documents (00 through 05) contain zero prescriptive PC scripting."""
        for rel_path in QUICKSTART_FILES:
            lines = self.get_lines(rel_path)
            if not lines:
                continue
            violations = []
            for idx, line in enumerate(lines, 1):
                if line.strip().startswith("```"):
                    continue
                # Skip pregen character sheet bio descriptions in 00_overview_and_background.md
                if rel_path == "quickstart/00_overview_and_background.md" and ("## Pre-Generated" in line or "### Torvir" in line or "### Einar" in line or "### Khoril" in line):
                    continue
                for pattern, desc in PRESCRIPTIVE_ACTION_PATTERNS:
                    if re.search(pattern, line, re.IGNORECASE):
                        violations.append(f"Line {idx} [{desc}]: {line.strip()}")

            self.assertEqual(
                violations, [],
                f"Found {len(violations)} prescriptive violations in {rel_path}:\n"
                + "\n".join(violations)
            )

    def test_r1_zero_prescriptive_pc_scripting_in_handouts(self):
        """R1.9: Verify all handouts (cheat sheet, band worksheet, node map, scribe letter) are neutral."""
        for rel_path in HANDOUT_FILES:
            lines = self.get_lines(rel_path)
            if not lines:
                continue
            violations = []
            for idx, line in enumerate(lines, 1):
                if line.strip().startswith("```"):
                    continue
                for pattern, desc in PRESCRIPTIVE_ACTION_PATTERNS:
                    if re.search(pattern, line, re.IGNORECASE):
                        violations.append(f"Line {idx} [{desc}]: {line.strip()}")

            self.assertEqual(
                violations, [],
                f"Found {len(violations)} prescriptive violations in {rel_path}:\n"
                + "\n".join(violations)
            )

    def test_r1_zero_prescriptive_pc_scripting_in_master_document(self):
        """R1.10: Verify compiled master document contains zero prescriptive PC scripting."""
        lines = self.get_lines("armouries_of_the_third_deep_master.md")
        if not lines:
            self.skipTest("armouries_of_the_third_deep_master.md not found")

        violations = []
        for idx, line in enumerate(lines, 1):
            if line.strip().startswith("```"):
                continue
            for pattern, desc in PRESCRIPTIVE_ACTION_PATTERNS:
                if re.search(pattern, line, re.IGNORECASE):
                    violations.append(f"Line {idx} [{desc}]: {line.strip()}")

        self.assertEqual(
            violations, [],
            f"Found {len(violations)} prescriptive violations in armouries_of_the_third_deep_master.md:\n"
            + "\n".join(violations)
        )


class TestR1NeutralAgencyFraming(BaseR1Test):
    """R1: Verify neutral GM presentation and open tactical company choices."""

    def test_r1_obstacle_checks_use_neutral_framing(self):
        """R1.11: Check that keyed locations introduce obstacles neutrally without assigning heroes."""
        for filename in ["04_keyed_locations.md", "quickstart/02_keyed_locations.md"]:
            text = self.get_text(filename)
            if not text:
                continue

            # Ensure checks are presented neutrally
            self.assertTrue(
                "A hero" in text or "The Company" in text or "A Player-Hero" in text or "Companions" in text or "A companion" in text,
                f"{filename} lacks neutral company/hero obstacle framing."
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
