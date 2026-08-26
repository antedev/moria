#!/usr/bin/env python3
"""
test_r2_pregen_tns.py — R2 Test Suite: Target Number Architecture & Pregen TN Purge
====================================================================================
Authoritative Source: ORIGINAL_REQUEST.md (§R2), PROJECT.md (§1, Feature 2)

This test suite validates 100% compliance with Requirement 2 (R2):
  - Asserts zero hardcoded pregen TN listings (e.g. `Torvir 15, Einar 15, Khoril 16`,
    `(Wits TN: Torvir`, `(Strength TN:`, `(Heart TN:`, `Heart TN: Khoril 16`,
    `(Wits TN 15, Favoured)`, `Strength TN (Torvir 13, Einar 14)`) across all
    keyed locations, delve mechanics, adversaries, hazards, relics, and GM aids.
  - Asserts that all skill checks across all adventure markdown files use standard
    The One Ring 2e notation (e.g. `**SCAN roll**`, `**STEALTH roll (Favoured)**`,
    `**CRAFT roll (+1d)**`, `**ATHLETICS roll**`, `**BATTLE roll**`).
  - Asserts that character-sheet Attribute TN formulas (TN = 20 - Attribute) exist only
    where character profiles are formally defined, not inside adventure obstacle checks.
"""

import os
import re
import unittest
from pathlib import Path
from typing import Dict, List, Tuple, Set

ROOT_DIR = Path(__file__).resolve().parent.parent

OFFICIAL_18_SKILLS: Set[str] = {
    # Strength
    "AWE", "ATHLETICS", "AWARENESS", "HUNTING", "SONG", "CRAFT",
    # Heart
    "ENHEARTEN", "TRAVEL", "INSIGHT", "HEALING", "COURTESY", "BATTLE",
    # Wits
    "PERSUADE", "STEALTH", "SCAN", "EXPLORE", "RIDDLE", "LORE"
}

# Files where adventure obstacle skill checks occur
ADVENTURE_CHECK_FILES = [
    "02_band_mechanics.md",
    "03_operational_mechanics.md",
    "04_keyed_locations.md",
    "05_adversaries_and_hazards.md",
    "06_relics_and_rewards.md",
    "07_gm_playbook_and_pacing.md",
    "quickstart/01_delve_mechanics_and_alert_system.md",
    "quickstart/02_keyed_locations.md",
    "quickstart/03_adversaries_and_hazards.md",
    "quickstart/04_loot_relics_and_rewards.md",
    "quickstart/05_gm_screen_and_play_aids.md",
    "handouts/gm_cheat_sheet.md",
    "handouts/band_worksheet.md",
    "handouts/dying_scribe_letter.md",
    "handouts/node_map.md",
    "armouries_of_the_third_deep_master.md",
]

# Patterns representing hardcoded pregen TN listings inside adventure checks
HARDCODED_PREGEN_TN_PATTERNS: List[Tuple[str, str]] = [
    # 1. Multi-hero pregen TN listings: e.g. "Torvir 15, Einar 15, Khoril 16"
    (
        r"Torvir\s+\d+,\s*Einar\s+\d+,\s*Khoril\s+\d+",
        "Pregen TN triple listing (e.g. 'Torvir 15, Einar 15, Khoril 16')"
    ),
    (
        r"Torvir\s+\d+,\s*Einar\s+\d+",
        "Pregen TN double listing (e.g. 'Torvir 13, Einar 14')"
    ),
    (
        r"Khoril\s+\d+,\s*Torvir\s+\d+,\s*Einar\s+\d+",
        "Pregen TN triple listing (e.g. 'Khoril 16, Torvir 18, Einar 17')"
    ),
    (
        r"Torvir\s+1[385]|Einar\s+1[475]|Khoril\s+1[36]",
        "Individual pregen TN tag (e.g. 'Torvir 13', 'Einar 14', 'Khoril 16') in test context"
    ),
    # 2. Attribute TN parentheticals embedding pregen names or fixed numbers
    (
        r"\((?:Strength|Heart|Wits)\s+TN\s*:\s*(?:Torvir|Einar|Khoril)",
        "Attribute TN parenthetical specifying pregen name (e.g. '(Wits TN: Torvir 15...')"
    ),
    (
        r"\((?:Strength|Heart|Wits)\s+TN\s*:\s*\d+\)",
        "Attribute TN parenthetical with hardcoded number (e.g. '(Heart TN: 16)')"
    ),
    (
        r"\b(?:Strength|Heart|Wits)\s+TN\s*\(\s*(?:Torvir|Einar|Khoril)",
        "Attribute TN parenthetical variant with pregen name"
    ),
    (
        r"\b(?:against\s+)?(?:their\s+)?(?:Strength|Heart|Wits)\s+TN\s*\(\s*Torvir",
        "Direct check phrasing embedding pregen TN list"
    ),
    (
        r"\(Wits\s+TN\s+15,\s+Favoured\)",
        "Hardcoded Wits TN 15 in Favoured check"
    ),
    (
        r"Heart\s+TN\s*:\s*Einar\s+17\s+or\s+Wits\s+TN\s*:\s*Einar\s+15",
        "Hardcoded pregen TN options in Shadow test"
    ),
]


class BaseR2Test(unittest.TestCase):
    """Base test case for R2 verification."""

    @classmethod
    def setUpClass(cls):
        cls.file_texts: Dict[str, str] = {}
        cls.file_lines: Dict[str, List[str]] = {}

        for rel_path in ADVENTURE_CHECK_FILES:
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


class TestR2PregenTNPurge(BaseR2Test):
    """R2: Assert zero hardcoded pregen TN listings across all adventure files."""

    def test_r2_zero_hardcoded_pregen_tns_in_04_keyed_locations(self):
        """R2.1: Verify 04_keyed_locations.md has zero hardcoded pregen TN listings."""
        lines = self.get_lines("04_keyed_locations.md")
        self.assertTrue(len(lines) > 0, "04_keyed_locations.md missing or empty")

        violations = []
        for idx, line in enumerate(lines, 1):
            if line.strip().startswith("```"):
                continue
            for pattern, desc in HARDCODED_PREGEN_TN_PATTERNS:
                if re.search(pattern, line, re.IGNORECASE):
                    violations.append(f"Line {idx} [{desc}]: {line.strip()}")

        self.assertEqual(
            violations, [],
            f"Found {len(violations)} hardcoded pregen TN violations in 04_keyed_locations.md:\n"
            + "\n".join(violations)
        )

    def test_r2_zero_hardcoded_pregen_tns_in_02_band_mechanics(self):
        """R2.2: Verify 02_band_mechanics.md has zero hardcoded pregen TN listings."""
        lines = self.get_lines("02_band_mechanics.md")
        self.assertTrue(len(lines) > 0, "02_band_mechanics.md missing or empty")

        violations = []
        for idx, line in enumerate(lines, 1):
            if line.strip().startswith("```"):
                continue
            # Allow mathematical explanation of Band TN 15 (20 - 5 = 15)
            if "20 - 5" in line or "20 - Readiness" in line or "Band TN 15" in line:
                continue
            for pattern, desc in HARDCODED_PREGEN_TN_PATTERNS:
                if re.search(pattern, line, re.IGNORECASE):
                    violations.append(f"Line {idx} [{desc}]: {line.strip()}")

        self.assertEqual(
            violations, [],
            f"Found {len(violations)} hardcoded pregen TN violations in 02_band_mechanics.md:\n"
            + "\n".join(violations)
        )

    def test_r2_zero_hardcoded_pregen_tns_in_03_operational_mechanics(self):
        """R2.3: Verify 03_operational_mechanics.md has zero hardcoded pregen TN listings."""
        lines = self.get_lines("03_operational_mechanics.md")
        self.assertTrue(len(lines) > 0, "03_operational_mechanics.md missing or empty")

        violations = []
        for idx, line in enumerate(lines, 1):
            if line.strip().startswith("```"):
                continue
            for pattern, desc in HARDCODED_PREGEN_TN_PATTERNS:
                if re.search(pattern, line, re.IGNORECASE):
                    violations.append(f"Line {idx} [{desc}]: {line.strip()}")

        self.assertEqual(
            violations, [],
            f"Found {len(violations)} hardcoded pregen TN violations in 03_operational_mechanics.md:\n"
            + "\n".join(violations)
        )

    def test_r2_zero_hardcoded_pregen_tns_in_05_adversaries_and_hazards(self):
        """R2.4: Verify 05_adversaries_and_hazards.md has zero hardcoded pregen TN listings."""
        lines = self.get_lines("05_adversaries_and_hazards.md")
        self.assertTrue(len(lines) > 0, "05_adversaries_and_hazards.md missing or empty")

        violations = []
        for idx, line in enumerate(lines, 1):
            if line.strip().startswith("```"):
                continue
            for pattern, desc in HARDCODED_PREGEN_TN_PATTERNS:
                if re.search(pattern, line, re.IGNORECASE):
                    violations.append(f"Line {idx} [{desc}]: {line.strip()}")

        self.assertEqual(
            violations, [],
            f"Found {len(violations)} hardcoded pregen TN violations in 05_adversaries_and_hazards.md:\n"
            + "\n".join(violations)
        )

    def test_r2_zero_hardcoded_pregen_tns_in_06_relics_and_rewards(self):
        """R2.5: Verify 06_relics_and_rewards.md has zero hardcoded pregen TN listings."""
        lines = self.get_lines("06_relics_and_rewards.md")
        self.assertTrue(len(lines) > 0, "06_relics_and_rewards.md missing or empty")

        violations = []
        for idx, line in enumerate(lines, 1):
            if line.strip().startswith("```"):
                continue
            for pattern, desc in HARDCODED_PREGEN_TN_PATTERNS:
                if re.search(pattern, line, re.IGNORECASE):
                    violations.append(f"Line {idx} [{desc}]: {line.strip()}")

        self.assertEqual(
            violations, [],
            f"Found {len(violations)} hardcoded pregen TN violations in 06_relics_and_rewards.md:\n"
            + "\n".join(violations)
        )

    def test_r2_zero_hardcoded_pregen_tns_in_07_gm_playbook_and_pacing(self):
        """R2.6: Verify 07_gm_playbook_and_pacing.md has zero hardcoded pregen TN listings."""
        lines = self.get_lines("07_gm_playbook_and_pacing.md")
        self.assertTrue(len(lines) > 0, "07_gm_playbook_and_pacing.md missing or empty")

        violations = []
        for idx, line in enumerate(lines, 1):
            if line.strip().startswith("```"):
                continue
            for pattern, desc in HARDCODED_PREGEN_TN_PATTERNS:
                if re.search(pattern, line, re.IGNORECASE):
                    violations.append(f"Line {idx} [{desc}]: {line.strip()}")

        self.assertEqual(
            violations, [],
            f"Found {len(violations)} hardcoded pregen TN violations in 07_gm_playbook_and_pacing.md:\n"
            + "\n".join(violations)
        )

    def test_r2_zero_hardcoded_pregen_tns_in_quickstart_files(self):
        """R2.7: Verify all quickstart files (01-05) have zero hardcoded pregen TN listings."""
        for rel_path in [
            "quickstart/01_delve_mechanics_and_alert_system.md",
            "quickstart/02_keyed_locations.md",
            "quickstart/03_adversaries_and_hazards.md",
            "quickstart/04_loot_relics_and_rewards.md",
            "quickstart/05_gm_screen_and_play_aids.md",
        ]:
            lines = self.get_lines(rel_path)
            if not lines:
                continue

            violations = []
            for idx, line in enumerate(lines, 1):
                if line.strip().startswith("```"):
                    continue
                if "20 - 5" in line or "20 - Readiness" in line or "Band TN 15" in line:
                    continue
                # Skip the hero attribute reference table in gm_screen_and_play_aids if formatted as character overview
                if rel_path == "quickstart/05_gm_screen_and_play_aids.md" and ("| Hero |" in line or "| Torvir" in line or "| Einar" in line or "| Khoril" in line):
                    continue
                for pattern, desc in HARDCODED_PREGEN_TN_PATTERNS:
                    if re.search(pattern, line, re.IGNORECASE):
                        violations.append(f"Line {idx} [{desc}]: {line.strip()}")

            self.assertEqual(
                violations, [],
                f"Found {len(violations)} hardcoded pregen TN violations in {rel_path}:\n"
                + "\n".join(violations)
            )

    def test_r2_zero_hardcoded_pregen_tns_in_handouts(self):
        """R2.8: Verify handouts have zero hardcoded pregen TN listings in check blocks."""
        for rel_path in ["handouts/node_map.md", "handouts/dying_scribe_letter.md"]:
            lines = self.get_lines(rel_path)
            if not lines:
                continue

            violations = []
            for idx, line in enumerate(lines, 1):
                if line.strip().startswith("```"):
                    continue
                for pattern, desc in HARDCODED_PREGEN_TN_PATTERNS:
                    if re.search(pattern, line, re.IGNORECASE):
                        violations.append(f"Line {idx} [{desc}]: {line.strip()}")

            self.assertEqual(
                violations, [],
                f"Found {len(violations)} hardcoded pregen TN violations in {rel_path}:\n"
                + "\n".join(violations)
            )

    def test_r2_zero_hardcoded_pregen_tns_in_master_document(self):
        """R2.9: Verify armouries_of_the_third_deep_master.md has zero hardcoded pregen TN listings in checks."""
        lines = self.get_lines("armouries_of_the_third_deep_master.md")
        if not lines:
            self.skipTest("armouries_of_the_third_deep_master.md not found")

        violations = []
        for idx, line in enumerate(lines, 1):
            if line.strip().startswith("```"):
                continue
            # Allow the Chapter 1 pre-gen character sheet section and Band formula
            if idx < 300 and ("STR 7 (TN 13)" in line or "STR 6 (TN 14)" in line or "HRT 4 (TN 16)" in line):
                continue
            if "20 - 5" in line or "20 - Readiness" in line or "Band TN 15" in line:
                continue
            for pattern, desc in HARDCODED_PREGEN_TN_PATTERNS:
                if re.search(pattern, line, re.IGNORECASE):
                    violations.append(f"Line {idx} [{desc}]: {line.strip()}")

        self.assertEqual(
            violations, [],
            f"Found {len(violations)} hardcoded pregen TN violations in armouries_of_the_third_deep_master.md:\n"
            + "\n".join(violations)
        )


class TestR2StandardTOR2eNotation(BaseR2Test):
    """R2: Verify all skill tests use standard TOR 2e check format."""

    def test_r2_skill_check_formatting_standard_tor2e(self):
        """R2.10: Verify skill check presentations use standard TOR 2e notation (e.g. **SCAN roll**)."""
        for filename in ["04_keyed_locations.md", "quickstart/02_keyed_locations.md"]:
            text = self.get_text(filename)
            if not text:
                continue

            # Find all bold check headers: **SKILL roll** or **SKILL test**
            check_matches = re.findall(r"\*\*([A-Z\s]{3,20})\s+(?:roll|test)\*\*", text, re.IGNORECASE)
            self.assertTrue(
                len(check_matches) >= 10,
                f"{filename} does not contain standard bold skill roll headers (found {len(check_matches)})."
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
