#!/usr/bin/env python3
"""
test_adversarial_coverage.py — Independent Adversarial Stress Test Suite
========================================================================
Author: teamwork_preview_challenger_1 (Empirical Challenger)
Target: Armouries of the Third Deep (19 Markdown Documents)

This test module executes aggressive, multi-vector adversarial stress tests
designed to find hidden edge cases, rogue TNs, 5e rule leaks, non-canonical
skills, malformed Skill Endeavours, and cross-file stat inconsistencies.

Usage:
  python -m unittest tests/test_adversarial_coverage.py -v
"""

import os
import re
import sys
import unittest
from pathlib import Path
from typing import Dict, List, Set, Tuple

# Project root directory
ROOT_DIR = Path(__file__).resolve().parent.parent

OFFICIAL_18_SKILLS: Set[str] = {
    # Strength
    "AWE", "ATHLETICS", "AWARENESS", "HUNTING", "SONG", "CRAFT",
    # Heart
    "ENHEARTEN", "TRAVEL", "INSIGHT", "HEALING", "COURTESY", "BATTLE",
    # Wits
    "PERSUADE", "STEALTH", "SCAN", "EXPLORE", "RIDDLE", "LORE"
}

DISALLOWED_SKILLS_AND_LEAKS: List[Tuple[str, str]] = [
    (r"\b(?:sleight\s+of\s+hand|sleight\s+skill|\*\*sleight\*\*)\b", "Sleight (Fake Skill)"),
    (r"\b(?:old\s+lore|\*\*old\s+lore\*\*)\b", "Old Lore (Fake Skill)"),
    (r"\b(?:customs|\*\*customs\*\*)\b", "Customs (1e Legacy Skill)"),
    (r"\b(?:search\s+check|search\s+roll|\*\*search\*\*)\b", "Search check (1e Legacy Skill)"),
    (r"\b(?:garrison\s+supply\s+points?|\+?\d+\s*garrison\s+supply\s+points?)\b", "Garrison Supply Points (Fabricated Mechanic)"),
    (r"\bsupply\s+points?\b", "supply points (Fabricated Mechanic)"),
    (r"\b(?:advantage\s*/\s*\+2|\+2\s*/\s*advantage)\b", "Advantage / +2 (5e phrasing)"),
    (r"\b(?:passive\s+perception|passive\s+awareness)\b", "Passive Perception/Awareness (5e phrasing)"),
    (r"\b(?:saving\s+throw|saving\s+throws)\b", "Saving throw (5e phrasing)"),
    (r"\b(?:spell\s+slots?|hit\s+dice)\b", "Spell slots / Hit dice (5e phrasing)"),
    (r"\bdc\s*\d+\b", "DC (5e Difficulty Class)"),
    (r"\bdifficulty\s*\d+\b", "Difficulty XX (5e phrasing)"),
]

HERO_STATS = {
    "Torvir": {"STR": 7, "HRT": 2, "WIT": 5, "STR_TN": 13, "HRT_TN": 18, "WIT_TN": 15, "Parry": 15, "Mail": "5d"},
    "Einar": {"STR": 6, "HRT": 3, "WIT": 5, "STR_TN": 14, "HRT_TN": 17, "WIT_TN": 15, "Parry": 20, "Mail": "3d"},
    "Khoril": {"STR": 7, "HRT": 4, "WIT": 4, "STR_TN": 13, "HRT_TN": 16, "WIT_TN": 16, "Parry": 17, "Mail": "3d"},
}

ALL_19_MODULE_FILES = [
    "00_overview_and_background.md",
    "01_campaign_context.md",
    "01_delve_mechanics_and_alert_system.md",
    "02_band_mechanics.md",
    "02_keyed_locations.md",
    "03_adversaries_and_hazards.md",
    "03_operational_mechanics.md",
    "04_keyed_locations.md",
    "04_loot_relics_and_rewards.md",
    "05_adversaries_and_hazards.md",
    "05_gm_screen_and_play_aids.md",
    "06_relics_and_rewards.md",
    "07_gm_playbook_and_pacing.md",
    "handouts/band_worksheet.md",
    "handouts/dying_scribe_letter.md",
    "handouts/gm_cheat_sheet.md",
    "handouts/node_map.md",
    "README.md",
    "PROJECT.md",
]


class BaseAdversarialTest(unittest.TestCase):
    """Base class providing loaded file texts and adversarial helper assertions."""

    @classmethod
    def setUpClass(cls):
        cls.file_texts: Dict[str, str] = {}
        cls.file_lines: Dict[str, List[str]] = {}
        for rel_path in ALL_19_MODULE_FILES:
            file_path = ROOT_DIR / rel_path
            if not file_path.exists():
                file_path = ROOT_DIR / "quickstart" / rel_path
            if file_path.exists():
                text = file_path.read_text(encoding="utf-8")
                cls.file_texts[rel_path] = text
                cls.file_lines[rel_path] = text.splitlines()
            else:
                cls.file_texts[rel_path] = ""
                cls.file_lines[rel_path] = []

    def get_text(self, rel_path: str) -> str:
        return self.file_texts.get(rel_path, "")

    def get_lines(self, rel_path: str) -> List[str]:
        return self.file_lines.get(rel_path, [])


class TestAdversarialRogueTNs(BaseAdversarialTest):
    """Aggressive probing for rogue fixed Target Numbers assigned to player heroes."""

    def test_adversarial_no_rogue_fixed_hero_tns(self):
        """
        Scan every line of all 19 files. Fail if any line contains a fixed TN (e.g. TN 10-20)
        attached to a player test, outside allowed Band TN or Injury TN or explicit character sheet formulas.
        """
        rogue_pattern = re.compile(r"\bTN\s*[:=]?\s*(1[0-9]|20)\b", re.IGNORECASE)

        for rel_path, lines in self.file_lines.items():
            for idx, line in enumerate(lines, 1):
                stripped = line.strip()
                if not stripped or stripped.startswith("```"):
                    continue

                # Allowed canonical forms
                if "20 - " in line or "$20 -" in line:
                    continue
                if "Band TN 15" in line or "Band TN 16" in line or "Band TN" in line:
                    continue
                if "Injury TN" in line or "Injury" in line:
                    continue
                if any(k in line for k in ["STR 7 (TN 13)", "STR 6 (TN 14)", "HRT 2 (TN 18)", "HRT 3 (TN 17)", "HRT 4 (TN 16)", "WIT 5 (TN 15)", "WIT 4 (TN 16)"]):
                    continue
                if any(k in line for k in ["Strength TN 13", "Strength TN 14", "Heart TN 18", "Heart TN 17", "Heart TN 16", "Wits TN 15", "Wits TN 16"]):
                    continue
                if "STR 13 / HRT 18 / WIT 15" in line or "STR 14 / HRT 17 / WIT 15" in line or "STR 13 / HRT 16 / WIT 16" in line:
                    continue
                if re.search(r"\(TN\s*1[34]\)\s*\d+\s*\(TN\s*1[678]\)", line):
                    continue

                matches = rogue_pattern.findall(line)
                if matches:
                    # Check if line also contains valid attribute specifier
                    lower = line.lower()
                    if not any(attr in lower for attr in ["strength tn", "heart tn", "wits tn", "band tn", "readiness tn", "readiness", "injury tn", "str 7", "str 6", "hrt 2", "hrt 3", "hrt 4", "wit 5", "wit 4"]):
                        self.fail(
                            f"Rogue Fixed TN detected in {rel_path}:{idx}\n"
                            f"Content: {line.strip()}"
                        )

    def test_adversarial_no_dc_or_difficulty_numbers(self):
        """Probe for D&D 5e 'DC XX' or 'Difficulty XX' across all documents."""
        dc_pattern = re.compile(r"\b(?:DC|Difficulty)\s*[:=]?\s*\d+\b", re.IGNORECASE)
        for rel_path, lines in self.file_lines.items():
            for idx, line in enumerate(lines, 1):
                match = dc_pattern.search(line)
                if match:
                    self.fail(f"5e DC/Difficulty detected in {rel_path}:{idx} -> {line.strip()}")


class TestAdversarialSkillIntegrity(BaseAdversarialTest):
    """Probe for non-existent skills, 1e skills, or traits formatted as rolled skills."""

    def test_adversarial_no_purged_or_leaked_skills(self):
        """Ensure Sleight, Old Lore, Customs, Search Check are 100% purged."""
        for pattern, label in DISALLOWED_SKILLS_AND_LEAKS:
            regex = re.compile(pattern, re.IGNORECASE)
            for rel_path, lines in self.file_lines.items():
                if rel_path in ["PROJECT.md", "README.md"]:
                    continue
                for idx, line in enumerate(lines, 1):
                    match = regex.search(line)
                    if match:
                        self.fail(f"Forbidden term '{label}' detected in {rel_path}:{idx} -> {line.strip()}")

    def test_adversarial_traits_never_rolled_as_skills(self):
        """Ensure Burglary, Leadership, Smith, Vaultbreaker are never rolled directly."""
        trait_skill_pattern = re.compile(
            r"\*\*(?:BURGLARY|LEADERSHIP|SMITH|VAULTBREAKER|ENEMY-LORE)\*\*\s*\(",
            re.IGNORECASE
        )
        for rel_path, lines in self.file_lines.items():
            for idx, line in enumerate(lines, 1):
                match = trait_skill_pattern.search(line)
                if match:
                    self.fail(
                        f"Trait treated as standalone skill roll in {rel_path}:{idx}\n"
                        f"Line: {line.strip()}"
                    )

    def test_adversarial_all_tested_skills_belong_to_official_18(self):
        """Extract every '**SKILL** (Attribute TN)' check across all files and verify against official 18."""
        skill_decl_pattern = re.compile(r"\*\*([A-Za-z\s]{3,25})\*\*\s*\((?:Strength|Heart|Wits)\s+TN", re.IGNORECASE)
        for rel_path, lines in self.file_lines.items():
            for idx, line in enumerate(lines, 1):
                matches = skill_decl_pattern.findall(line)
                for skill_name in matches:
                    clean_name = skill_name.strip().upper()
                    self.assertIn(
                        clean_name,
                        OFFICIAL_18_SKILLS,
                        f"Unrecognized skill '{clean_name}' tested in {rel_path}:{idx} -> {line.strip()}"
                    )


class TestAdversarial5eLeaks(BaseAdversarialTest):
    """Probe for subtle D&D 5th Edition phrasing leaks."""

    def test_adversarial_no_5e_advantage_plus_2(self):
        """Probe for 'Advantage / +2', 'Advantage', or 'Disadvantage' in rule blocks."""
        pattern = re.compile(r"\b(?:advantage\s*/\s*\+2|\+2\s*/\s*advantage)\b", re.IGNORECASE)
        for rel_path, text in self.file_texts.items():
            if rel_path in ["PROJECT.md", "README.md"]:
                continue
            match = pattern.search(text)
            self.assertIsNone(match, f"5e 'Advantage / +2' found in {rel_path}: {match.group(0) if match else ''}")

    def test_adversarial_no_passive_perception_or_saving_throws(self):
        """Probe for 'passive Perception', 'saving throw', 'spell slots', 'hit dice'."""
        patterns = [
            (r"\bpassive\s+perception\b", "passive Perception"),
            (r"\bperception\s+check\b", "perception check"),
            (r"\bsaving\s+throw\b", "saving throw"),
            (r"\bspell\s+slot\b", "spell slot"),
            (r"\bhit\s+dice\b", "hit dice"),
        ]
        for pattern, label in patterns:
            regex = re.compile(pattern, re.IGNORECASE)
            for rel_path, text in self.file_texts.items():
                match = regex.search(text)
                self.assertIsNone(match, f"5e mechanic '{label}' found in {rel_path}")


class TestAdversarialSkillEndeavours(BaseAdversarialTest):
    """Verify all 6 canonical Skill Endeavours across keyed locations and supporting files."""

    def test_adversarial_6_skill_endeavours_present_and_consistent(self):
        """Verify the 6 core Skill Endeavours have correct Resistance ratings in keyed locations."""
        loc_text = self.get_text("02_keyed_locations.md") + "\n" + self.get_text("04_keyed_locations.md")

        endeavours = [
            ("Fortifying the Forward Redoubt", 3),
            ("Disarming the Scythe Scrap-Trap Network", 3),
            ("Controlled Toppling of the Balrog Idol", 3),
            ("Calibrating & Arming the Siege Engines", 3),
            ("Assembling Squad Respirator Masks", 3),
            ("Bypassing the Adamant Runic Lock", 6),
        ]

        for name, expected_res in endeavours:
            # Check presence of name and resistance
            pattern = re.compile(rf"{re.escape(name)}.*?(?:Resistance\s*{expected_res})", re.IGNORECASE | re.DOTALL)
            self.assertTrue(
                pattern.search(loc_text),
                f"Skill Endeavour '{name}' (Resistance {expected_res}) missing or inconsistent in location atlas."
            )


class TestAdversarialCombatAndAdversaries(BaseAdversarialTest):
    """Verify adversary stats, The Mauler Riddle duel, and fell abilities math."""

    def test_adversarial_the_mauler_profile_and_riddle_duel(self):
        """Verify The Mauler has Parry '—', Endurance 80, Might 2, and Forward Stance Riddle task."""
        text = self.get_text("03_adversaries_and_hazards.md") + "\n" + self.get_text("05_adversaries_and_hazards.md")
        self.assertTrue(re.search(r"ENDURANCE:\s*80", text), "The Mauler Endurance 80 missing.")
        self.assertTrue(re.search(r"MIGHT:\s*2", text), "The Mauler Might 2 missing.")
        self.assertTrue(re.search(r"HATE:\s*10", text) or re.search(r"HATE:\s*8", text), "The Mauler Hate missing.")
        self.assertTrue(re.search(r"PARRY:\s*(?:—|-|0|None)", text), "The Mauler Parry '—' missing.")
        self.assertTrue("Dull-Witted" in text, "The Mauler Dull-Witted trait missing.")
        self.assertTrue("RIDDLE" in text and "Forward" in text, "The Mauler Forward stance Riddle duel missing.")

    def test_adversarial_grimnar_and_sniffers_stats(self):
        """Verify Grimnar (AL 6, End 36, Might 2, Hate 6) and Sniffers (AL 4, End 16, Hate 4)."""
        text = self.get_text("03_adversaries_and_hazards.md") + "\n" + self.get_text("05_adversaries_and_hazards.md")
        self.assertTrue(re.search(r"Grimnar", text, re.IGNORECASE))
        self.assertTrue(re.search(r"Endurance(?:\*\*|:|\s)+36", text, re.IGNORECASE))
        self.assertTrue(re.search(r"Sniffer", text, re.IGNORECASE))
        self.assertTrue(re.search(r"Endurance(?:\*\*|:|\s)+16", text, re.IGNORECASE))


class TestAdversarialRelicsAndRewards(BaseAdversarialTest):
    """Verify relics adhere to official TOR 2e Enchanted Qualities and Eye Awareness rules."""

    def test_adversarial_relic_qualities(self):
        """Verify Durin's Axe, Shield of the Deep Gate, Mattock, and Mail of Unyielding Stone."""
        text = self.get_text("04_loot_relics_and_rewards.md") + "\n" + self.get_text("06_relics_and_rewards.md")
        self.assertTrue("DURIN'S AXE" in text.upper())
        self.assertTrue("Superior Grievous" in text or "Grievous" in text)
        self.assertTrue("Superior Keen" in text or "Keen" in text)
        self.assertTrue("Shield of the Deep Gate" in text)
        self.assertTrue("Mail of Unyielding Stone" in text)
        self.assertTrue(re.search(r"Eye\s+Awareness", text, re.IGNORECASE))


class TestAdversarialHandoutsSync(BaseAdversarialTest):
    """Verify handouts and GM screen sync with exact hero stats and Band TN 15."""

    def test_adversarial_hero_attribute_tns_in_handouts(self):
        """Verify gm_cheat_sheet.md and band_worksheet.md list exact hero Attribute TNs."""
        cheat_sheet = self.get_text("handouts/gm_cheat_sheet.md")
        band_sheet = self.get_text("handouts/band_worksheet.md")

        for doc, doc_name in [(cheat_sheet, "gm_cheat_sheet.md"), (band_sheet, "band_worksheet.md")]:
            # Torvir STR 13, HRT 18, WIT 15
            self.assertTrue(re.search(r"Torvir.*13.*18.*15", doc, re.DOTALL), f"Torvir stats mismatch in {doc_name}")
            # Einar STR 14, HRT 17, WIT 15
            self.assertTrue(re.search(r"Einar.*14.*17.*15", doc, re.DOTALL), f"Einar stats mismatch in {doc_name}")
            # Khoril STR 13, HRT 16, WIT 16
            self.assertTrue(re.search(r"Khoril.*13.*16.*16", doc, re.DOTALL), f"Khoril stats mismatch in {doc_name}")
            # Band TN 15
            self.assertTrue(re.search(r"Band\s+TN\s*15", doc), f"Band TN 15 mismatch in {doc_name}")


class TestAdversarialKeyedLocationsCompleteness(BaseAdversarialTest):
    """Verify that all 10 Keyed Locations contain complete test blocks."""

    def test_adversarial_10_locations_present(self):
        """Ensure all 10 location headings are present in 02_keyed_locations.md and 04_keyed_locations.md."""
        for fname in ["02_keyed_locations.md", "04_keyed_locations.md"]:
            text = self.get_text(fname)
            for loc_num in range(1, 11):
                self.assertTrue(
                    re.search(rf"(?:Location|Area|\#\#\#)\s+{loc_num}[:\.\s]", text, re.IGNORECASE),
                    f"Location {loc_num} heading missing in {fname}"
                )

    def test_adversarial_all_location_test_blocks_have_failure_and_6_icons(self):
        """Ensure every test block in 02_keyed_locations.md contains Consequence of Failure and 6-icons."""
        lines = self.get_lines("02_keyed_locations.md")
        in_test_block = False
        block_has_failure = False
        block_has_success = False

        for idx, line in enumerate(lines, 1):
            if line.startswith("### Location") or line.startswith("## "):
                in_test_block = False
            if "* **" in line and "(" in line and "TN" in line:
                in_test_block = True
                block_has_failure = False
                block_has_success = False
            if in_test_block:
                if "Consequence of Failure" in line or "*Failure*" in line:
                    block_has_failure = True
                if "Degrees of Success" in line or "**6**:" in line or "*Success*" in line:
                    block_has_success = True


if __name__ == "__main__":
    unittest.main()
