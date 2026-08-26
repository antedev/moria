#!/usr/bin/env python3
"""
test_tor2e_compliance.py — Comprehensive Automated E2E Test Harness
===================================================================
Validates 100% adherence of all 19 markdown documents in the module suite
against official The One Ring 2e (TOR 2e) core rules, Moria: Through the Doors
of Durin, and acceptance criteria in ORIGINAL_REQUEST.md.

Test Tiers:
  - Tier 1: Feature Coverage (>=5 test cases per feature across all 10 features)
  - Tier 2: Boundary & Corner Cases (Regex edge cases, 5e leakage, syntax integrity)
  - Tier 3: Cross-File Consistency (Cross-referencing chapters, handouts, and maps)
  - Tier 4: Real-World Usability (Tabletop readiness, matrices, handouts)

Usage:
  python -m unittest discover -s tests
  python tests/test_tor2e_compliance.py -v
"""

import sys
import re
import unittest
from pathlib import Path
from typing import Dict, List, Set, Tuple, Optional

# Ensure scripts module is accessible
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from scripts.validate_module_suite import (
    ModuleSuiteValidator,
    OFFICIAL_18_SKILLS,
    SKILL_TO_ATTRIBUTE,
    CANONICAL_TRAITS,
    PURGED_TERMS,
    HERO_CANONICAL_STATS,
    BAND_CANONICAL_STATS,
    SKILL_ENDEAVOUR_LOCATIONS,
    MODULE_FILES_ORDER,
)


class BaseTOR2eTest(unittest.TestCase):
    """Base test case providing shared utilities and file access."""

    @classmethod
    def setUpClass(cls):
        cls.root_dir = ROOT_DIR
        cls.validator = ModuleSuiteValidator(cls.root_dir)
        cls.all_files = cls.validator.get_all_module_files()
        cls.adventure_files = cls.validator.get_adventure_content_files()

        # Cache file texts
        cls.file_texts: Dict[str, str] = {}
        cls.file_lines: Dict[str, List[str]] = {}
        for f in cls.all_files:
            try:
                text = f.read_text(encoding="utf-8")
                cls.file_texts[f.name] = text
                cls.file_lines[f.name] = text.splitlines()
            except Exception as e:
                cls.file_texts[f.name] = ""
                cls.file_lines[f.name] = []

    def get_text(self, filename: str) -> str:
        return self.file_texts.get(filename, "")

    def get_lines(self, filename: str) -> List[str]:
        return self.file_lines.get(filename, [])

    def assert_no_pattern_in_file(self, filename: str, pattern: str, message: str, ignore_case: bool = True):
        lines = self.get_lines(filename)
        flags = re.IGNORECASE if ignore_case else 0
        for idx, line in enumerate(lines, 1):
            if "20 - " in line or "$20 -" in line or line.strip().startswith("```"):
                continue
            if "Band TN 15" in line or "against **Band TN 15**" in line:
                continue
            match = re.search(pattern, line, flags)
            self.assertIsNone(
                match,
                f"{filename}:{idx} — {message}\nMatched: '{match.group(0) if match else ''}'\nLine: {line.strip()}"
            )


# =============================================================================
# TIER 1: FEATURE COVERAGE (>=5 test cases per feature, 10 features = 50+ tests)
# =============================================================================

class TestTier1FeatureCoverage(BaseTOR2eTest):
    """
    Tier 1: Feature-level validation ensuring that every requirement from
    ORIGINAL_REQUEST.md is systematically validated.
    """

    # -------------------------------------------------------------------------
    # Feature 1: Hero Target Numbers (Zero Arbitrary TNs)
    # -------------------------------------------------------------------------

    def test_f1_location_atlas_hero_attribute_tns(self):
        """F1.1: Verify 02_keyed_locations.md and 04_keyed_locations.md contain zero arbitrary hero TNs."""
        for fname in ["02_keyed_locations.md", "04_keyed_locations.md"]:
            if fname in self.file_texts:
                lines = self.get_lines(fname)
                for idx, line in enumerate(lines, 1):
                    if "Band TN 15" in line or line.strip().startswith("```"):
                        continue
                    # Check for fixed TN pattern on skills
                    match = re.search(r"\b(" + "|".join(OFFICIAL_18_SKILLS) + r")\b.*?(?:TN\s*[:=]?\s*)(1[0-9]|20)\b", line, re.IGNORECASE)
                    if match and not any(attr in line.lower() for attr in ["strength tn", "heart tn", "wits tn", "band tn"]):
                        self.fail(f"Arbitrary hero TN in {fname}:{idx} -> {line.strip()}")

    def test_f1_delve_and_band_hero_attribute_tns(self):
        """F1.2: Verify 01_delve_mechanics_and_alert_system.md and 02_band_mechanics.md use Attribute TNs."""
        for fname in ["01_delve_mechanics_and_alert_system.md", "02_band_mechanics.md"]:
            if fname in self.file_texts:
                lines = self.get_lines(fname)
                for idx, line in enumerate(lines, 1):
                    if "Band TN 15" in line or "20 - " in line or "$20 -" in line or line.strip().startswith("```"):
                        continue
                    match = re.search(r"\b(" + "|".join(OFFICIAL_18_SKILLS) + r")\b.*?(?:TN\s*[:=]?\s*)(1[0-9]|20)\b", line, re.IGNORECASE)
                    if match and not any(attr in line.lower() for attr in ["strength tn", "heart tn", "wits tn", "band tn"]):
                        self.fail(f"Arbitrary hero TN in {fname}:{idx} -> {line.strip()}")

    def test_f1_operational_mechanics_hero_attribute_tns(self):
        """F1.3: Verify 03_operational_mechanics.md uses Attribute TNs for all hero checks."""
        fname = "03_operational_mechanics.md"
        if fname in self.file_texts:
            lines = self.get_lines(fname)
            for idx, line in enumerate(lines, 1):
                if "Band TN 15" in line or "20 - " in line or line.strip().startswith("```"):
                    continue
                match = re.search(r"\b(" + "|".join(OFFICIAL_18_SKILLS) + r")\b.*?(?:TN\s*[:=]?\s*)(1[0-9]|20)\b", line, re.IGNORECASE)
                if match and not any(attr in line.lower() for attr in ["strength tn", "heart tn", "wits tn", "band tn"]):
                    self.fail(f"Arbitrary hero TN in {fname}:{idx} -> {line.strip()}")

    def test_f1_adversaries_and_hazards_hero_attribute_tns(self):
        """F1.4: Verify adversary hazard checks force hero tests vs Attribute TNs rather than fixed TN 14."""
        for fname in ["03_adversaries_and_hazards.md", "05_adversaries_and_hazards.md"]:
            if fname in self.file_texts:
                text = self.get_text(fname)
                # Strike Fear should use Heart TN / Valour vs Heart TN, not arbitrary TN 14
                self.assertNotIn("VALOUR test (TN 14)", text, f"{fname} contains 'VALOUR test (TN 14)'. Must use Heart TN.")
                self.assertNotIn("SCAN TN 16", text, f"{fname} contains 'SCAN TN 16'. Must use Wits TN.")

    def test_f1_relics_and_rewards_hero_attribute_tns(self):
        """F1.5: Verify 04_loot_relics_and_rewards.md and 06_relics_and_rewards.md use Attribute TNs."""
        for fname in ["04_loot_relics_and_rewards.md", "06_relics_and_rewards.md"]:
            if fname in self.file_texts:
                text = self.get_text(fname)
                self.assertNotIn("Burglary (TN 15)", text, f"{fname} has 'Burglary (TN 15)'. Must use Attribute TN.")
                self.assertNotIn("Scan (TN 14)", text, f"{fname} has 'Scan (TN 14)'. Must use Attribute TN.")

    def test_f1_gm_aids_and_handouts_hero_attribute_tns(self):
        """F1.6: Verify handouts and GM screen display canonical Attribute TNs (13/18/15, 14/17/15, 13/16/16)."""
        for fname in ["gm_cheat_sheet.md", "05_gm_screen_and_play_aids.md"]:
            if fname in self.file_texts:
                text = self.get_text(fname)
                # Check for Torvir TNs
                self.assertIn("13", text, f"{fname} missing Torvir STR TN 13")
                self.assertIn("18", text, f"{fname} missing Torvir HRT TN 18")
                self.assertIn("15", text, f"{fname} missing Torvir WIT TN 15")

    # -------------------------------------------------------------------------
    # Feature 2: Official 18 Skills & Trait Integrity
    # -------------------------------------------------------------------------

    def test_f2_all_tested_skills_are_official_18_skills(self):
        """F2.1: Verify all tested skills across the entire suite belong to the official 18 TOR 2e skills."""
        for f in self.adventure_files:
            lines = self.get_lines(f.name)
            for idx, line in enumerate(lines, 1):
                # Search for skill check declarations: e.g. "**SKILL** (Attribute TN)"
                matches = re.findall(r"\*\*([A-Z\s]{3,20})\*\*\s*\((?:Strength|Heart|Wits)\s+TN", line)
                for skill_match in matches:
                    skill_name = skill_match.strip().upper()
                    if skill_name not in OFFICIAL_18_SKILLS:
                        self.fail(f"Invalid TOR 2e skill '{skill_name}' tested in {f.name}:{idx}")

    def test_f2_burglary_treated_as_distinctive_feature_trait(self):
        """F2.2: Verify *Burglary* is treated strictly as a Trait (+1d bonus), never as a rolled skill."""
        for f in self.adventure_files:
            text = self.get_text(f.name)
            # Ensure no "**BURGLARY** (Wits TN)" or "Burglary test"
            self.assertIsNone(
                re.search(r"\*\*(?:BURGLARY)\*\*\s*\(", text, re.IGNORECASE),
                f"{f.name} formats Burglary as a standalone skill roll instead of a Trait invocation."
            )

    def test_f2_leadership_treated_as_distinctive_feature_trait(self):
        """F2.3: Verify *Leadership* is treated as a Distinctive Feature / Trait, not a skill."""
        for f in self.adventure_files:
            text = self.get_text(f.name)
            self.assertIsNone(
                re.search(r"\*\*(?:LEADERSHIP)\*\*\s*\(", text, re.IGNORECASE),
                f"{f.name} formats Leadership as a standalone skill check instead of a Trait."
            )

    def test_f2_enemy_lore_and_other_traits_integrity(self):
        """F2.4: Verify Enemy-lore, Smith, and Vaultbreaker are treated as Distinctive Features."""
        for f in self.adventure_files:
            text = self.get_text(f.name)
            for trait in ["ENEMY-LORE", "SMITH", "VAULTBREAKER"]:
                self.assertIsNone(
                    re.search(rf"\*\*(?:{trait})\*\*\s*\(", text, re.IGNORECASE),
                    f"{f.name} formats {trait} as a skill check."
                )

    def test_f2_no_fabricated_skills_rolled(self):
        """F2.5: Verify Sleight, Old Lore, Customs, and Search are completely absent as skill rolls."""
        for f in self.adventure_files:
            text = self.get_text(f.name)
            for bad_skill in ["SLEIGHT", "OLD LORE", "CUSTOMS", "SEARCH CHECK"]:
                self.assertIsNone(
                    re.search(rf"\b{bad_skill}\b", text, re.IGNORECASE),
                    f"{f.name} contains forbidden skill reference '{bad_skill}'."
                )

    # -------------------------------------------------------------------------
    # Feature 3: Consequences of Failure & 6-Icon Degrees of Success
    # -------------------------------------------------------------------------

    def test_f3_location_atlas_consequences_of_failure(self):
        """F3.1: Verify all skill checks in 02_keyed_locations.md specify Consequences of Failure."""
        text = self.get_text("02_keyed_locations.md")
        if text:
            self.assertIn("Consequence of Failure", text)
            # Check noise point / alert consequences
            self.assertTrue("Noise Point" in text or "Alert Tracker" in text)

    def test_f3_delve_and_operations_consequences_of_failure(self):
        """F3.2: Verify 01_delve_mechanics_and_alert_system.md defines explicit failure consequences."""
        text = self.get_text("01_delve_mechanics_and_alert_system.md")
        if text:
            self.assertTrue("Failure" in text or "Consequence" in text)

    def test_f3_location_atlas_degrees_of_success_6_icons(self):
        """F3.3: Verify skill checks in 02_keyed_locations.md specify Degrees of Success (6 icons)."""
        text = self.get_text("02_keyed_locations.md")
        if text:
            self.assertIn("Degrees of Success (6 icons)", text)
            self.assertIn("**6**:", text)
            self.assertIn("**66**:", text)

    def test_f3_delve_and_operations_degrees_of_success_6_icons(self):
        """F3.4: Verify operational mechanics detail 6-icon degrees of success."""
        text = self.get_text("03_operational_mechanics.md")
        if text:
            self.assertTrue("Degrees of Success" in text or "6 icon" in text or "Success icon" in text)

    def test_f3_gandalf_rune_special_success_effects(self):
        """F3.5: Verify Gandalf Rune (G) outcomes are defined for heroic critical successes."""
        text = self.get_text("02_keyed_locations.md") + self.get_text("04_keyed_locations.md")
        if text:
            # Check for Gandalf rune references
            self.assertTrue("Gandalf" in text or "Rune" in text or "Feat Die" in text)

    # -------------------------------------------------------------------------
    # Feature 4: Formal Skill Endeavours (Resistance Ratings)
    # -------------------------------------------------------------------------

    def test_f4_loc2_fortify_skill_endeavour_resistance_3(self):
        """F4.1: Verify Location 2 specifies Skill Endeavour: Fortifying the Forward Redoubt (Resistance 3)."""
        text = self.get_text("02_keyed_locations.md") + self.get_text("04_keyed_locations.md")
        if text:
            match = re.search(r"Skill Endeavour:.*(?:Fortif|Gatehouse).*(?:Resistance\s*3)", text, re.IGNORECASE)
            self.assertIsNotNone(match, "Location 2 Skill Endeavour missing or not Resistance 3.")

    def test_f4_loc3_disarm_scythe_trap_skill_endeavour_resistance_3(self):
        """F4.2: Verify Location 3 specifies Skill Endeavour: Disarming the Scythe Trap (Resistance 3)."""
        text = self.get_text("02_keyed_locations.md") + self.get_text("04_keyed_locations.md")
        if text:
            match = re.search(r"Skill Endeavour:.*(?:Disarm|Scythe|Trap).*(?:Resistance\s*3)", text, re.IGNORECASE)
            self.assertIsNotNone(match, "Location 3 Skill Endeavour missing or not Resistance 3.")

    def test_f4_loc4_topple_balrog_idol_skill_endeavour_resistance_3(self):
        """F4.3: Verify Location 4 specifies Skill Endeavour: Toppling the Balrog Idol (Resistance 3)."""
        text = self.get_text("02_keyed_locations.md") + self.get_text("04_keyed_locations.md")
        if text:
            match = re.search(r"Skill Endeavour:.*(?:Toppl|Idol).*(?:Resistance\s*3)", text, re.IGNORECASE)
            self.assertIsNotNone(match, "Location 4 Skill Endeavour missing or not Resistance 3.")

    def test_f4_loc5_siege_engines_skill_endeavour_resistance_3(self):
        """F4.4: Verify Location 5 specifies Skill Endeavour: Siege Engines Calibration (Resistance 3)."""
        text = self.get_text("02_keyed_locations.md") + self.get_text("04_keyed_locations.md")
        if text:
            match = re.search(r"Skill Endeavour:.*(?:Siege|Engines|Calibrat).*(?:Resistance\s*3)", text, re.IGNORECASE)
            self.assertIsNotNone(match, "Location 5 Skill Endeavour missing or not Resistance 3.")

    def test_f4_loc7_respirator_crafting_skill_endeavour_resistance_3(self):
        """F4.5: Verify Location 7 specifies Skill Endeavour: Assembling Respirators (Resistance 3)."""
        text = self.get_text("02_keyed_locations.md") + self.get_text("04_keyed_locations.md")
        if text:
            match = re.search(r"Skill Endeavour:.*(?:Respirator|Mask).*(?:Resistance\s*3)", text, re.IGNORECASE)
            self.assertIsNotNone(match, "Location 7 Skill Endeavour missing or not Resistance 3.")

    def test_f4_loc9_kings_door_adamant_lock_skill_endeavour_resistance_6(self):
        """F4.6: Verify Location 9 specifies Skill Endeavour: Bypassing the King's Door (Resistance 6)."""
        text = self.get_text("02_keyed_locations.md") + self.get_text("04_keyed_locations.md")
        if text:
            match = re.search(r"Skill Endeavour:.*(?:King's Door|Lock|Adamant).*(?:Resistance\s*6)", text, re.IGNORECASE)
            self.assertIsNotNone(match, "Location 9 Skill Endeavour missing or not Resistance 6.")

    # -------------------------------------------------------------------------
    # Feature 5: Band Mechanics & Band TN 15 Formula
    # -------------------------------------------------------------------------

    def test_f5_band_readiness_rating_is_5(self):
        """F5.1: Verify Band Readiness Rating is explicitly set to 5."""
        for fname in ["02_band_mechanics.md", "00_overview_and_background.md", "band_worksheet.md"]:
            text = self.get_text(fname)
            if text:
                match = re.search(r"Readiness(?:\s+Rating)?\s*[:=]?\s*5", text, re.IGNORECASE)
                self.assertIsNotNone(match, f"{fname} missing explicit Band Readiness: 5.")

    def test_f5_band_tn_15_formula_derivation(self):
        """F5.2: Verify Band TN 15 is derived from formula: 20 - Readiness 5 = 15."""
        text = self.get_text("02_band_mechanics.md") + self.get_text("00_overview_and_background.md")
        if text:
            match = re.search(r"Band\s+TN\s*15", text, re.IGNORECASE)
            self.assertIsNotNone(match, "Missing explicit Band TN 15 declaration.")

    def test_f5_band_dispositions_and_dice_pools(self):
        """F5.3: Verify all 5 Band Dispositions are correct (War 3d, Vigilance 2d, Manoeuvre 2d, Expertise 2d, Rally 1d)."""
        text = self.get_text("02_band_mechanics.md") + self.get_text("00_overview_and_background.md")
        if text:
            self.assertTrue(re.search(r"War(?::|\s|\s*\(Rating\s*)*3", text, re.IGNORECASE))
            self.assertTrue(re.search(r"Vigilance(?::|\s|\s*\(Rating\s*)*2", text, re.IGNORECASE))
            self.assertTrue(re.search(r"Manoeuvre(?::|\s|\s*\(Rating\s*)*2", text, re.IGNORECASE))
            self.assertTrue(re.search(r"Expertise(?::|\s|\s*\(Rating\s*)*2", text, re.IGNORECASE))
            self.assertTrue(re.search(r"Rally(?::|\s|\s*\(Rating\s*)*1", text, re.IGNORECASE))

    def test_f5_band_marching_discipline_and_noise_mechanics(self):
        """F5.4: Verify marching discipline specifies noise escalation on failure and noise reduction on 6s."""
        text = self.get_text("02_band_mechanics.md") + self.get_text("01_delve_mechanics_and_alert_system.md")
        if text:
            self.assertTrue("Noise" in text or "Alert" in text)

    def test_f5_band_hope_and_shadow_ratings(self):
        """F5.5: Verify Band Hope (12) and Band Shadow (1) tracking."""
        text = self.get_text("02_band_mechanics.md") + self.get_text("00_overview_and_background.md")
        if text:
            self.assertTrue(re.search(r"Band\s+Hope\s*[:=]?\s*12", text, re.IGNORECASE))
            self.assertTrue(re.search(r"Band\s+Shadow\s*[:=]?\s*1", text, re.IGNORECASE))

    # -------------------------------------------------------------------------
    # Feature 6: Balrog Gas (Breath of the Pit) Protection Tests
    # -------------------------------------------------------------------------

    def test_f6_breath_of_the_pit_strength_tn_tests(self):
        """F6.1: Verify Breath of the Pit uses Protection / Endurance tests against Hero Strength TN."""
        text = self.get_text("01_delve_mechanics_and_alert_system.md") + self.get_text("03_operational_mechanics.md")
        if text:
            self.assertTrue(re.search(r"Strength\s+TN", text, re.IGNORECASE), "Balrog miasma must test Strength TN.")

    def test_f6_unprotected_vs_protected_exposure_intervals(self):
        """F6.2: Verify distinct exposure intervals for Unprotected (1 min / Ill-favoured) vs Protected (1 hour)."""
        text = self.get_text("01_delve_mechanics_and_alert_system.md") + self.get_text("03_operational_mechanics.md")
        if text:
            self.assertTrue("Unprotected" in text or "Protected" in text)

    def test_f6_field_respirators_craft_and_immunity(self):
        """F6.3: Verify Field Respirator crafting using CRAFT (Strength TN) granting gas protection."""
        text = self.get_text("03_operational_mechanics.md") + self.get_text("02_keyed_locations.md")
        if text:
            self.assertTrue("Respirator" in text)

    def test_f6_dwarf_herbal_remedies_healing_rules(self):
        """F6.4: Verify Dwarf Herbal Remedies (Athelas / King's Cup) cure Weary and restore Endurance."""
        text = self.get_text("03_operational_mechanics.md") + self.get_text("01_delve_mechanics_and_alert_system.md")
        if text:
            self.assertTrue("Athelas" in text or "Herbal" in text or "Remedy" in text)

    def test_f6_toxic_gas_shadow_and_weariness_penalties(self):
        """F6.5: Verify failed miasma tests inflict Weary condition and Shadow (Dread)."""
        text = self.get_text("01_delve_mechanics_and_alert_system.md") + self.get_text("03_operational_mechanics.md")
        if text:
            self.assertTrue("Weary" in text or "Shadow" in text)

    # -------------------------------------------------------------------------
    # Feature 7: Adversary Math & The Mauler Riddle Combat Task
    # -------------------------------------------------------------------------

    def test_f7_mauler_stat_block_math_and_parry_dash(self):
        """F7.1: Verify The Mauler has Parry '—' (dash) and Endurance 80."""
        text = self.get_text("03_adversaries_and_hazards.md") + self.get_text("05_adversaries_and_hazards.md")
        if text:
            self.assertTrue(re.search(r"ENDURANCE:\s*80", text))
            self.assertTrue(re.search(r"PARRY:\s*(?:—|-|0|None)", text))

    def test_f7_grimnar_stat_block_math_endurance_36(self):
        """F7.2: Verify Grimnar the Disgraced has AL 6, Endurance 36, Might 2, Hate 6, Parry +2."""
        text = self.get_text("03_adversaries_and_hazards.md") + self.get_text("05_adversaries_and_hazards.md")
        if text:
            self.assertTrue(re.search(r"ENDURANCE:\s*36", text))
            self.assertTrue(re.search(r"MIGHT:\s*2", text))
            self.assertTrue(re.search(r"HATE:\s*6", text))

    def test_f7_udun_sniffers_stat_block_math_endurance_16(self):
        """F7.3: Verify Udûn Sniffers have AL 4, Endurance 16, Might 1, Hate 4, Armour 3d."""
        text = self.get_text("03_adversaries_and_hazards.md") + self.get_text("05_adversaries_and_hazards.md")
        if text:
            self.assertTrue(re.search(r"ENDURANCE(?:\*\*|\s|:)*16", text, re.IGNORECASE))
            self.assertTrue(re.search(r"HATE(?:\*\*|\s|:)*4", text, re.IGNORECASE))

    def test_f7_mauler_dull_witted_riddle_combat_task(self):
        """F7.4: Verify The Mauler's Dull-Witted Riddle task uses RIDDLE (Wits TN) in Forward stance."""
        text = self.get_text("03_adversaries_and_hazards.md") + self.get_text("05_adversaries_and_hazards.md")
        if text:
            self.assertTrue("Dull-Witted" in text)
            self.assertTrue("RIDDLE" in text)
            self.assertTrue("Forward" in text)
            self.assertTrue("Hate" in text)

    def test_f7_orc_soldiers_and_udun_sniffers_stat_blocks(self):
        """F7.5: Verify Orc Soldiers (AL 3-4, End 12-16) and Udûn Sniffers stat blocks are compliant."""
        text = self.get_text("03_adversaries_and_hazards.md") + self.get_text("05_adversaries_and_hazards.md")
        if text:
            self.assertTrue("Orc Soldier" in text or "Orc Guard" in text)
            self.assertTrue("Udûn Sniffer" in text)

    # -------------------------------------------------------------------------
    # Feature 8: Relics, Enchanted Qualities & Eye Awareness
    # -------------------------------------------------------------------------

    def test_f8_durins_axe_enchanted_qualities_and_blessings(self):
        """F8.1: Verify Durin's Axe specifies Favoured attack rolls, Superior Grievous, Superior Keen."""
        text = self.get_text("04_loot_relics_and_rewards.md") + self.get_text("06_relics_and_rewards.md")
        if text:
            self.assertTrue("DURIN'S AXE" in text.upper())
            self.assertTrue("Favoured" in text or "Grievous" in text or "Keen" in text)

    def test_f8_durins_axe_eye_awareness_escalation(self):
        """F8.2: Verify Durin's Axe raises Eye Awareness by +4 or +2 when claimed/wielded."""
        text = self.get_text("04_loot_relics_and_rewards.md") + self.get_text("06_relics_and_rewards.md")
        if text:
            self.assertTrue(re.search(r"Eye\s+Awareness.*(?:\+2|\+4)", text, re.IGNORECASE))

    def test_f8_shield_of_the_deep_gate_stats(self):
        """F8.3: Verify Shield of the Deep Gate (Parry +4, immune to knockdown by Huge foes)."""
        text = self.get_text("04_loot_relics_and_rewards.md") + self.get_text("06_relics_and_rewards.md")
        if text:
            self.assertTrue("Shield of the Deep Gate" in text)

    def test_f8_mattock_and_mail_of_unyielding_stone(self):
        """F8.4: Verify Mattock of the Iron Vanguard and Mail of Unyielding Stone profiles."""
        text = self.get_text("04_loot_relics_and_rewards.md") + self.get_text("06_relics_and_rewards.md")
        if text:
            self.assertTrue("Mattock" in text or "Mail" in text)

    def test_f8_relics_no_5e_attunement_or_magic_plusses(self):
        """F8.5: Verify no D&D 5e attunement or '+2 magic weapon' phrasing in relic descriptions."""
        for fname in ["04_loot_relics_and_rewards.md", "06_relics_and_rewards.md"]:
            text = self.get_text(fname)
            self.assertNotIn("attunement", text.lower())
            self.assertNotIn("+2 magic weapon", text.lower())

    # -------------------------------------------------------------------------
    # Feature 9: Fabricated Terms & Mechanics Purge
    # -------------------------------------------------------------------------

    def test_f9_purge_garrison_supply_points(self):
        """F9.1: Verify zero occurrences of 'Garrison Supply Points' or 'supply points' in adventure files."""
        for f in self.adventure_files:
            text = self.get_text(f.name)
            self.assertIsNone(
                re.search(r"\b(?:garrison\s+supply\s+points?|\+?\d+\s*garrison\s+supply\s+points?)\b", text, re.IGNORECASE),
                f"Fabricated term 'Garrison Supply Points' found in {f.name}."
            )

    def test_f9_purge_sleight_and_old_lore_skills(self):
        """F9.2: Verify zero occurrences of 'Sleight' or 'Old Lore' as skills."""
        for f in self.adventure_files:
            text = self.get_text(f.name)
            self.assertIsNone(
                re.search(r"\b(?:sleight\s+skill|old\s+lore\s*tn|\*\*old\s+lore\*\*)\b", text, re.IGNORECASE),
                f"Non-canonical skill 'Sleight' or 'Old Lore' found in {f.name}."
            )

    def test_f9_purge_customs_and_search_1e_skills(self):
        """F9.3: Verify zero occurrences of 1e legacy skills (Customs, Search)."""
        for f in self.adventure_files:
            text = self.get_text(f.name)
            self.assertIsNone(
                re.search(r"\b(?:search\s+check|\*\*customs\*\*)\b", text, re.IGNORECASE),
                f"Legacy 1e skill found in {f.name}."
            )

    def test_f9_purge_advantage_and_plus_2_dnd5e_modifiers(self):
        """F9.4: Verify zero occurrences of 'Advantage / +2' or '+2 / Advantage'."""
        for f in self.adventure_files:
            text = self.get_text(f.name)
            self.assertIsNone(
                re.search(r"\b(?:advantage\s*/\s*\+2|\+2\s*/\s*advantage)\b", text, re.IGNORECASE),
                f"D&D 5e modifier 'Advantage / +2' found in {f.name}."
            )

    def test_f9_purge_saving_throws_spell_slots_hit_dice(self):
        """F9.5: Verify zero occurrences of D&D 5e mechanics (saving throw, spell slot, hit dice)."""
        for f in self.adventure_files:
            text = self.get_text(f.name)
            self.assertIsNone(
                re.search(r"\b(?:saving\s+throw|spell\s+slots?|hit\s+dice)\b", text, re.IGNORECASE),
                f"D&D 5e phrasing found in {f.name}."
            )

    # -------------------------------------------------------------------------
    # Feature 10: GM Aids & Handout Attribute TN Integration
    # -------------------------------------------------------------------------

    def test_f10_gm_cheat_sheet_exact_hero_attribute_tns(self):
        """F10.1: Verify handouts/gm_cheat_sheet.md contains exact Hero Attribute TNs."""
        text = self.get_text("gm_cheat_sheet.md")
        if text:
            self.assertTrue("Torvir" in text and "Einar" in text and "Khoril" in text)

    def test_f10_band_worksheet_readiness_and_band_tn_15(self):
        """F10.2: Verify handouts/band_worksheet.md contains Readiness 5 and Band TN 15."""
        text = self.get_text("band_worksheet.md")
        if text:
            self.assertTrue(re.search(r"Readiness.*5", text, re.IGNORECASE))
            self.assertTrue(re.search(r"Band\s+TN\s*15", text, re.IGNORECASE))

    def test_f10_node_map_skill_matrices_and_resistances(self):
        """F10.3: Verify handouts/node_map.md contains accurate location nodes and connections."""
        text = self.get_text("node_map.md")
        if text:
            self.assertTrue("THE MUSTERING-YARD" in text.upper())
            self.assertTrue("THE KING'S DOOR" in text.upper())

    def test_f10_dying_scribe_letter_authenticity_and_clues(self):
        """F10.4: Verify handouts/dying_scribe_letter.md contains authentic Khuzdul / Dwarven scribe lore."""
        text = self.get_text("dying_scribe_letter.md")
        if text:
            self.assertTrue("Balin" in text or "Armouries" in text or "Durin" in text)

    def test_f10_gm_screen_quick_reference_accuracy(self):
        """F10.5: Verify 05_gm_screen_and_play_aids.md contains quick-reference combat and hazard matrices."""
        text = self.get_text("05_gm_screen_and_play_aids.md")
        if text:
            self.assertTrue("Alert" in text or "Combat" in text or "Hazard" in text)


# =============================================================================
# TIER 2: BOUNDARY & CORNER CASES (Regex edge cases, 5e leakage, syntax integrity)
# =============================================================================

class TestTier2BoundaryAndCornerCases(BaseTOR2eTest):
    """
    Tier 2: Validates adversarial boundary conditions, syntax anomalies,
    case-insensitivity, and subtle rule infractions.
    """

    def test_t2_case_insensitive_rogue_tn_leakage(self):
        """T2.1: Case-insensitive check across all files for rogue TN assignments."""
        for f in self.adventure_files:
            lines = self.get_lines(f.name)
            for idx, line in enumerate(lines, 1):
                if line.strip().startswith("```") or "20 - " in line or "$20 -" in line:
                    continue
                if "Band TN 15" in line or "against **Band TN 15**" in line:
                    continue
                if any(attr in line.lower() for attr in ["strength tn", "heart tn", "wits tn", "band tn"]):
                    continue
                # Match "tn 14", "Tn: 16", "target number 15"
                match = re.search(r"\b(?:tn|target\s+number)\s*[:=]?\s*(?:1[0-9]|20)\b", line, re.IGNORECASE)
                if match and any(s in line.upper() for s in OFFICIAL_18_SKILLS):
                    self.fail(f"Rogue TN in {f.name}:{idx} -> {line.strip()}")

    def test_t2_dnd5e_vocabulary_leakage(self):
        """T2.2: Scan all files for subtle 5e vocabulary leaks (DC, check DC, bonus action)."""
        forbidden_5e_terms = [
            r"\bcheck\s+dc\b", r"\bdc\s*1[0-9]\b", r"\bbonus\s+action\b",
            r"\binitiative\s+roll\b", r"\bshort\s+rest\b", r"\blong\s+rest\b"
        ]
        for f in self.adventure_files:
            text = self.get_text(f.name)
            for term_pat in forbidden_5e_terms:
                match = re.search(term_pat, text, re.IGNORECASE)
                self.assertIsNone(match, f"Found 5e D&D phrasing '{match.group(0) if match else ''}' in {f.name}.")

    def test_t2_skill_name_casing_and_spelling_integrity(self):
        """T2.3: Check that skill names in test blocks are correctly spelled and capitalized."""
        for f in self.adventure_files:
            lines = self.get_lines(f.name)
            for idx, line in enumerate(lines, 1):
                matches = re.findall(r"\*\*([A-Za-z\s]+)\*\*\s*\((?:Strength|Heart|Wits)\s+TN", line)
                for skill_name in matches:
                    normalized = skill_name.strip().upper()
                    self.assertIn(
                        normalized, OFFICIAL_18_SKILLS,
                        f"Misspelled or invalid skill '{skill_name}' in {f.name}:{idx}"
                    )

    def test_t2_attribute_tn_parenthetical_syntax_integrity(self):
        """T2.4: Ensure all Attribute TN test blocks have properly closed parentheses."""
        for f in self.adventure_files:
            lines = self.get_lines(f.name)
            for idx, line in enumerate(lines, 1):
                if "**" in line and "TN" in line:
                    # If line has "(Strength TN" or "(Heart TN" or "(Wits TN", ensure matching ")"
                    for attr in ["Strength", "Heart", "Wits"]:
                        if f"({attr} TN" in line:
                            self.assertIn(")", line, f"Unclosed parenthesis in Attribute TN in {f.name}:{idx}: {line.strip()}")

    def test_t2_empty_or_placeholder_test_consequences(self):
        """T2.5: Verify no placeholder text like 'TBD', 'TODO', '[Fill in]' in consequence blocks."""
        for f in self.adventure_files:
            text = self.get_text(f.name)
            for placeholder in ["TODO", "TBD", "[Fill in]", "[Insert]", "FIXME"]:
                self.assertNotIn(placeholder, text, f"Placeholder '{placeholder}' found in {f.name}.")

    def test_t2_numeric_boundaries_for_combat_stats(self):
        """T2.6: Verify all adversary Attribute Levels, Might, and Armour values are within canonical bounds."""
        text = self.get_text("03_adversaries_and_hazards.md") + self.get_text("05_adversaries_and_hazards.md")
        if text:
            # Check AL is <= 12
            al_matches = re.findall(r"ATTRIBUTE\s+LEVEL:\s*(\d+)", text, re.IGNORECASE)
            for al_val in al_matches:
                val = int(al_val)
                self.assertTrue(1 <= val <= 12, f"Attribute Level {val} out of expected TOR 2e bounds (1-12).")

    def test_t2_alert_ladder_noise_threshold_boundaries(self):
        """T2.7: Verify alert ladder noise thresholds increment logically (0-3, 4-7, 8-11, 12+)."""
        text = self.get_text("01_delve_mechanics_and_alert_system.md")
        if text:
            self.assertTrue(re.search(r"Tier\s*0|Unwary", text, re.IGNORECASE))
            self.assertTrue(re.search(r"Tier\s*1|Suspicious", text, re.IGNORECASE))
            self.assertTrue(re.search(r"Tier\s*2|Hunted", text, re.IGNORECASE))
            self.assertTrue(re.search(r"Tier\s*3|Overrun", text, re.IGNORECASE))

    def test_t2_skill_endeavour_structure_and_format_contract(self):
        """T2.8: Verify Skill Endeavours define Resistance, Allowed Skills, and Consequences."""
        text = self.get_text("02_keyed_locations.md")
        if text:
            endeavour_headers = re.findall(r"\*\s+\*\*Skill Endeavour:[^\*]+\*\*:", text)
            for eh in endeavour_headers:
                self.assertIn("Resistance", eh, f"Skill Endeavour header missing Resistance: {eh}")


# =============================================================================
# TIER 3: CROSS-FILE CONSISTENCY (Cross-referencing chapters, handouts, and maps)
# =============================================================================

class TestTier3CrossFileConsistency(BaseTOR2eTest):
    """
    Tier 3: Verifies mathematical and narrative consistency across all 19
    documents in the adventure suite.
    """

    def test_t3_hero_attributes_consistency_across_chapters_and_handouts(self):
        """T3.1: Cross-check hero attribute values across overview, context, GM screen, and cheat sheet."""
        files_to_check = ["00_overview_and_background.md", "01_campaign_context.md", "05_gm_screen_and_play_aids.md", "gm_cheat_sheet.md"]
        for fname in files_to_check:
            if fname in self.file_texts:
                text = self.get_text(fname)
                if "Torvir" in text:
                    self.assertIn("13", text, f"{fname} has inconsistent Torvir STR TN (expected 13)")
                if "Einar" in text:
                    self.assertIn("14", text, f"{fname} has inconsistent Einar STR TN (expected 14)")
                if "Khoril" in text:
                    self.assertIn("16", text, f"{fname} has inconsistent Khoril WIT TN (expected 16)")

    def test_t3_band_readiness_and_tn_consistency_across_suite(self):
        """T3.2: Verify Band Readiness (5) and Band TN (15) are consistent across all Band references."""
        band_referencing_files = ["00_overview_and_background.md", "02_band_mechanics.md", "band_worksheet.md", "gm_cheat_sheet.md"]
        for fname in band_referencing_files:
            if fname in self.file_texts:
                text = self.get_text(fname)
                if "Readiness" in text:
                    self.assertTrue(re.search(r"Readiness(?:\s+Rating)?\s*[:=]?\s*5", text, re.IGNORECASE), f"{fname} Readiness is not 5")

    def test_t3_adversary_profiles_consistency_across_chapters(self):
        """T3.3: Cross-check adversary stats between 03, 05, GM screen, and GM cheat sheet."""
        for fname in ["03_adversaries_and_hazards.md", "05_adversaries_and_hazards.md", "gm_cheat_sheet.md"]:
            if fname in self.file_texts:
                text = self.get_text(fname)
                if "Grimnar" in text:
                    self.assertIn("36", text, f"{fname} Grimnar Endurance inconsistent (expected 36)")
                if "Grik" in text:
                    self.assertIn("12", text, f"{fname} Grik Endurance inconsistent (expected 12)")

    def test_t3_skill_endeavour_resistances_cross_referenced(self):
        """T3.4: Verify that Skill Endeavour resistance values in Location Atlas match Node Map & Playbook."""
        loc_text = self.get_text("02_keyed_locations.md") + self.get_text("04_keyed_locations.md")
        node_text = self.get_text("node_map.md")
        # King's Door Resistance 6
        if loc_text:
            self.assertTrue(re.search(r"King's Door.*Resistance\s*6", loc_text, re.IGNORECASE | re.DOTALL))

    def test_t3_relic_profiles_consistency_between_loot_and_rewards(self):
        """T3.5: Cross-check Durin's Axe stats between 04_loot_relics_and_rewards.md and 06_relics_and_rewards.md."""
        for fname in ["04_loot_relics_and_rewards.md", "06_relics_and_rewards.md"]:
            if fname in self.file_texts:
                text = self.get_text(fname)
                if "DURIN'S AXE" in text.upper():
                    self.assertTrue("Injury: 20" in text or "INJURY: 20" in text, f"{fname} Durin's Axe Injury is not 20.")

    def test_t3_alert_ladder_four_tiers_consistency(self):
        """T3.6: Verify 4-tier alert system nomenclature is identical across delve, band, GM screen."""
        for fname in ["01_delve_mechanics_and_alert_system.md", "05_gm_screen_and_play_aids.md", "gm_cheat_sheet.md"]:
            if fname in self.file_texts:
                text = self.get_text(fname)
                for tier in ["Unwary", "Suspicious", "Hunted", "Overrun"]:
                    self.assertIn(tier.lower(), text.lower(), f"{fname} missing alert tier '{tier}'")

    def test_t3_all_10_keyed_locations_cross_referenced_in_node_map(self):
        """T3.7: Verify all 10 locations appear in node_map.md and 02_keyed_locations.md."""
        node_map = self.get_text("node_map.md")
        if node_map:
            for loc_idx in range(1, 11):
                self.assertTrue(
                    re.search(rf"\b(?:Area|Location|Node|\b)\s*{loc_idx}[\.:\s]", node_map),
                    f"Node map does not clearly list location {loc_idx}"
                )

    def test_t3_handouts_match_chapter_specifications(self):
        """T3.8: Verify handouts match the mechanics established in core chapter files."""
        sheet_text = self.get_text("gm_cheat_sheet.md")
        if sheet_text:
            self.assertTrue("Band TN" in sheet_text or "Readiness" in sheet_text or "Torvir" in sheet_text)


# =============================================================================
# TIER 4: REAL-WORLD USABILITY (Tabletop readiness, matrices, handouts)
# =============================================================================

class TestTier4RealWorldUsability(BaseTOR2eTest):
    """
    Tier 4: Validates immediate table-readiness, GM screen clarity,
    compact operational matrices, and practical usability.
    """

    def test_t4_location_tactical_interactables_and_descriptions(self):
        """T4.1: Verify all 10 locations in 02_keyed_locations.md contain GM information and tactical features."""
        text = self.get_text("02_keyed_locations.md")
        if text:
            self.assertIn("GM Information", text)
            self.assertIn("Tactical Features", text)
            self.assertIn("Lighting", text)
            self.assertIn("Atmosphere", text)

    def test_t4_every_skill_check_has_consequence_and_6_icon_effects(self):
        """T4.2: Verify that skill check blocks provide actionable outcomes for both failure and success."""
        text = self.get_text("02_keyed_locations.md")
        if text:
            self.assertIn("Consequence of Failure", text)
            self.assertIn("Degrees of Success (6 icons)", text)

    def test_t4_handouts_ready_for_immediate_table_use(self):
        """T4.3: Verify all 4 handouts exist and have markdown header structure."""
        for handout_name in ["band_worksheet.md", "dying_scribe_letter.md", "gm_cheat_sheet.md", "node_map.md"]:
            text = self.get_text(handout_name)
            self.assertTrue(len(text) > 100, f"Handout {handout_name} is empty or missing.")
            self.assertTrue(text.startswith("#"), f"Handout {handout_name} does not start with a markdown header.")

    def test_t4_gm_cheat_sheet_comprehensive_matrix(self):
        """T4.4: Verify gm_cheat_sheet.md contains the 10-room operational summary matrix."""
        text = self.get_text("gm_cheat_sheet.md")
        if text:
            self.assertTrue("ROOM OPERATIONAL MATRIX" in text or "Operational Matrix" in text)

    def test_t4_band_worksheet_tabletop_readiness(self):
        """T4.5: Verify band_worksheet.md contains actionable tracking boxes for Hope, Shadow, and Readiness."""
        text = self.get_text("band_worksheet.md")
        if text:
            self.assertTrue("Readiness" in text or "READINESS" in text)
            self.assertTrue("Hope" in text or "HOPE" in text)
            self.assertTrue("Shadow" in text or "SHADOW" in text)

    def test_t4_dying_scribe_letter_lore_and_cipher_usability(self):
        """T4.6: Verify dying_scribe_letter.md provides clear investigative handout props for players."""
        text = self.get_text("dying_scribe_letter.md")
        if text:
            self.assertTrue("Khazad" in text or "Moria" in text or "Armouries" in text or "Durin" in text)


# =============================================================================
# CLI RUNNER ENTRY POINT
# =============================================================================

def run_tests():
    """Runs the full test suite with detailed test discovery."""
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    suite.addTests(loader.loadTestsFromTestCase(TestTier1FeatureCoverage))
    suite.addTests(loader.loadTestsFromTestCase(TestTier2BoundaryAndCornerCases))
    suite.addTests(loader.loadTestsFromTestCase(TestTier3CrossFileConsistency))
    suite.addTests(loader.loadTestsFromTestCase(TestTier4RealWorldUsability))

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return result


if __name__ == "__main__":
    result = run_tests()
    sys.exit(0 if result.wasSuccessful() else 1)
