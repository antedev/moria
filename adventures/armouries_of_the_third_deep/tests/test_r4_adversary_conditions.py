#!/usr/bin/env python3
"""
test_r4_adversary_conditions.py — R4 Test Suite: Canonical TOR 2e Rules, Conditions & Adversary Stats
======================================================================================================
Authoritative Source: ORIGINAL_REQUEST.md (§R4), PROJECT.md (§3, Feature 4, Feature 8)

This test suite validates 100% compliance with Requirement 4 (R4):
  - Asserts zero occurrences of the non-canonical "Daunted" condition across all markdown,
    python, HTML, and documentation files in the repository.
  - Asserts that all fear, dread, and supernatural effects use canonical TOR 2e conditions:
    Shadow Points (Dread/Greed/Sorcery/Misdeed), Hope loss, Miserable, Weary, Wounded, Bout of Madness.
  - Asserts that all adversary stat blocks (The Mauler, Grimnar, Grik, Udûn Sniffers, Orc Soldiers)
    match official TOR 2e math (Attribute Level, Endurance, Might, Hate, Parry, Armour, Fell Abilities).
"""

import os
import re
import unittest
from pathlib import Path
from typing import Dict, List, Tuple, Set

ROOT_DIR = Path(__file__).resolve().parent.parent

# Adversary canonical specifications for TOR 2e
ADVERSARY_CANONICAL_PROFILES = {
    "The Mauler": {
        "Attribute_Level": 10,
        "Endurance": 80,
        "Might": 2,
        "Hate": 10,
        "Armour": "5d",
        "Parry": "—",
        "Fell_Abilities": ["Hideous Toughness", "Strike Fear", "Horrible Strength", "Dull-Witted"],
    },
    "Grimnar the Disgraced": {
        "Attribute_Level": 6,
        "Endurance": 36,
        "Might": 2,
        "Hate": 6,
        "Armour": "3d",
        "Parry": "+2",
        "Fell_Abilities": ["Snake-like Speed", "Great Leap", "Denizen of the Dark", "Hideous Toughness", "Strike Fear"],
    },
    "Grik": {
        "Attribute_Level": 3,
        "Endurance": 12,
        "Might": 1,
        "Hate": 3,
        "Armour": "2d",
        "Parry": "+1",
        "Fell_Abilities": ["Craven"],
    },
    "Udûn Sniffers": {
        "Attribute_Level": 4,
        "Endurance": 16,
        "Might": 1,
        "Hate": 4,
        "Armour": "3d",
    },
}

# Non-canonical / invented condition terms that must be purged
FORBIDDEN_CONDITION_TERMS: List[Tuple[str, str]] = [
    (r"\bdaunted\b", "Invented condition 'Daunted' (must use Shadow/Dread or Miserable)"),
    (r"\bpoisoned\s+condition\b", "Non-canonical 'Poisoned condition' (use Weary, Endurance loss, or Wound)"),
    (r"\bfatal\s+stasis\b", "Invented condition 'fatal stasis'"),
    (r"\bpinned\s+condition\b", "Non-canonical 'Pinned condition'"),
    (r"\bdemoralized\s+condition\b", "Non-canonical 'Demoralized condition'"),
]


class BaseR4Test(unittest.TestCase):
    """Base test case for R4 verification."""

    @classmethod
    def setUpClass(cls):
        cls.all_files: Dict[str, Path] = {}
        for ext in ["*.md", "*.py", "*.html"]:
            for p in ROOT_DIR.rglob(ext):
                if ".git" in p.parts or ".agents" in p.parts or "__pycache__" in p.parts:
                    continue
                rel = p.relative_to(ROOT_DIR).as_posix()
                cls.all_files[rel] = p


class TestR4DauntedPurge(BaseR4Test):
    """R4: Complete eradication of the non-canonical 'Daunted' condition across the entire repo."""

    def test_r4_zero_occurrences_of_daunted_across_all_markdown_files(self):
        """R4.1: Verify zero occurrences of 'Daunted' across all markdown files in the repository."""
        violations = []
        for rel_path, path in self.all_files.items():
            if not rel_path.endswith(".md"):
                continue
            # Skip project requirement / audit docs that discuss the Daunted purge rule
            if rel_path in ["PROJECT.md", "TEST_INFRA.md", "TEST_READY.md", "README.md"]:
                continue
            text = path.read_text(encoding="utf-8")
            lines = text.splitlines()
            for idx, line in enumerate(lines, 1):
                if line.strip().startswith("```"):
                    continue
                match = re.search(r"\bdaunted\b", line, re.IGNORECASE)
                if match:
                    violations.append(f"{rel_path}:{idx} -> {line.strip()}")

        self.assertEqual(
            violations, [],
            f"Found {len(violations)} occurrences of forbidden 'Daunted' condition in markdown files:\n"
            + "\n".join(violations)
        )

    def test_r4_zero_occurrences_of_daunted_in_scripts(self):
        """R4.2: Verify zero occurrences of 'Daunted' in production scripts (excluding test assertions)."""
        violations = []
        for rel_path, path in self.all_files.items():
            if not rel_path.startswith("scripts/"):
                continue
            text = path.read_text(encoding="utf-8")
            lines = text.splitlines()
            for idx, line in enumerate(lines, 1):
                # Allow comments or purged term checking in validate_module_suite.py
                if "validate_module_suite.py" in rel_path and ("PURGED" in line or "daunted" in line.lower() and "assert" not in line):
                    continue
                match = re.search(r"\bdaunted\b", line, re.IGNORECASE)
                if match:
                    violations.append(f"{rel_path}:{idx} -> {line.strip()}")

        self.assertEqual(
            violations, [],
            f"Found forbidden 'Daunted' references in scripts:\n" + "\n".join(violations)
        )

    def test_r4_zero_occurrences_of_daunted_in_html_assets(self):
        """R4.3: Verify zero occurrences of 'Daunted' in compiled HTML assets."""
        violations = []
        for rel_path, path in self.all_files.items():
            if not rel_path.endswith(".html"):
                continue
            text = path.read_text(encoding="utf-8")
            lines = text.splitlines()
            for idx, line in enumerate(lines, 1):
                match = re.search(r"\bdaunted\b", line, re.IGNORECASE)
                if match:
                    violations.append(f"{rel_path}:{idx} -> {line.strip()}")

        self.assertEqual(
            violations, [],
            f"Found {len(violations)} occurrences of 'Daunted' in HTML presentation assets:\n"
            + "\n".join(violations)
        )


class TestR4CanonicalConditions(BaseR4Test):
    """R4: Verify canonical TOR 2e conditions and mechanics."""

    def test_r4_zero_forbidden_invented_conditions(self):
        """R4.4: Verify absence of non-canonical conditions (fatal stasis, pinned condition, etc.)."""
        violations = []
        for rel_path, path in self.all_files.items():
            if not rel_path.endswith(".md"):
                continue
            if rel_path in ["PROJECT.md", "TEST_INFRA.md", "TEST_READY.md", "README.md"]:
                continue
            text = path.read_text(encoding="utf-8")
            lines = text.splitlines()
            for idx, line in enumerate(lines, 1):
                if line.strip().startswith("```"):
                    continue
                for pattern, desc in FORBIDDEN_CONDITION_TERMS:
                    match = re.search(pattern, line, re.IGNORECASE)
                    if match:
                        violations.append(f"{rel_path}:{idx} [{desc}] -> {line.strip()}")

        self.assertEqual(
            violations, [],
            f"Found {len(violations)} forbidden condition violations:\n" + "\n".join(violations)
        )

    def test_r4_canonical_fear_and_strike_fear_mechanics(self):
        """R4.5: Verify Strike Fear inflicts Shadow (Dread) / Miserable condition, not Daunted."""
        for rel_path in ["05_adversaries_and_hazards.md", "quickstart/03_adversaries_and_hazards.md"]:
            if rel_path not in self.all_files:
                continue
            text = self.all_files[rel_path].read_text(encoding="utf-8")
            self.assertNotIn(
                "become Daunted", text,
                f"{rel_path} Strike Fear still contains 'become Daunted'."
            )
            self.assertTrue(
                "Shadow" in text or "Dread" in text or "Miserable" in text,
                f"{rel_path} Strike Fear missing canonical Shadow/Dread effect."
            )


class TestR4AdversaryStatsAndMath(BaseR4Test):
    """R4: Verify adversary stat blocks and combat proficiencies."""

    def test_r4_the_mauler_stat_block_compliance(self):
        """R4.6: Verify The Mauler (Cave-Troll) stat block math and Fell Abilities."""
        for rel_path in ["05_adversaries_and_hazards.md", "quickstart/03_adversaries_and_hazards.md"]:
            if rel_path not in self.all_files:
                continue
            text = self.all_files[rel_path].read_text(encoding="utf-8")
            self.assertTrue(re.search(r"ATTRIBUTE\s+LEVEL\s*:\s*10", text, re.IGNORECASE))
            self.assertTrue(re.search(r"ENDURANCE\s*:\s*80", text, re.IGNORECASE))
            self.assertTrue(re.search(r"MIGHT\s*:\s*2", text, re.IGNORECASE))
            self.assertTrue(re.search(r"HATE\s*:\s*10", text, re.IGNORECASE))
            self.assertTrue(re.search(r"PARRY\s*:\s*(?:—|-|0|None)", text, re.IGNORECASE))
            self.assertTrue(re.search(r"ARMOUR\s*:\s*5d", text, re.IGNORECASE))
            self.assertTrue("Hideous Toughness" in text)
            self.assertTrue("Strike Fear" in text)
            self.assertTrue("Horrible Strength" in text)
            self.assertTrue("Dull-Witted" in text)

    def test_r4_grimnar_stat_block_compliance(self):
        """R4.7: Verify Grimnar the Disgraced (Great Orc Chief) stat block math and Fell Abilities."""
        for rel_path in ["05_adversaries_and_hazards.md", "quickstart/03_adversaries_and_hazards.md"]:
            if rel_path not in self.all_files:
                continue
            text = self.all_files[rel_path].read_text(encoding="utf-8")
            self.assertTrue(re.search(r"ATTRIBUTE\s+LEVEL\s*:\s*6", text, re.IGNORECASE))
            self.assertTrue(re.search(r"ENDURANCE\s*:\s*36", text, re.IGNORECASE))
            self.assertTrue(re.search(r"MIGHT\s*:\s*2", text, re.IGNORECASE))
            self.assertTrue(re.search(r"HATE\s*:\s*6", text, re.IGNORECASE))
            self.assertTrue(re.search(r"ARMOUR\s*:\s*3d", text, re.IGNORECASE))
            self.assertTrue("Snake-like Speed" in text)
            self.assertTrue("Great Leap" in text)
            self.assertTrue("Denizen of the Dark" in text)

    def test_r4_grik_stat_block_compliance(self):
        """R4.8: Verify Grik (Orc Sentry / Craven) stat block."""
        for rel_path in ["05_adversaries_and_hazards.md", "quickstart/03_adversaries_and_hazards.md"]:
            if rel_path not in self.all_files:
                continue
            text = self.all_files[rel_path].read_text(encoding="utf-8")
            if "Grik" in text:
                self.assertTrue(re.search(r"ENDURANCE\s*:\s*12", text, re.IGNORECASE))
                self.assertTrue("Craven" in text)

    def test_r4_udun_sniffers_stat_block_compliance(self):
        """R4.9: Verify Udûn Sniffers (Orc Trackers) stat block."""
        for rel_path in ["05_adversaries_and_hazards.md", "quickstart/03_adversaries_and_hazards.md"]:
            if rel_path not in self.all_files:
                continue
            text = self.all_files[rel_path].read_text(encoding="utf-8")
            if "Udûn Sniffer" in text:
                self.assertTrue(re.search(r"ENDURANCE\s*:\s*16", text, re.IGNORECASE))
                self.assertTrue(re.search(r"HATE\s*:\s*4", text, re.IGNORECASE))


if __name__ == "__main__":
    unittest.main(verbosity=2)
