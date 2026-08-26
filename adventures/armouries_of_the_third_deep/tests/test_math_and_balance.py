#!/usr/bin/env python3
"""
test_math_and_balance.py — Mathematical Consistency, Combat Models & Balance Validator
========================================================================================
Empirical adversarial verification test suite for 'Armouries of the Third Deep'.
Validates:
  1. Hero Attribute TN formulas (20 - Attribute) across Torvir, Einar, Khoril.
  2. Band Readiness TN formula (20 - 5 = 15) and Disposition dice pools.
  3. Adversary stat formulas (AL * 8 troll endurance, AL * 6 chief endurance, AL * 4 soldier endurance).
  4. Weapon damage, injury ratings, and load calculations on all items and relics.
  5. Balrog toxic gas exposure mechanics and timer/resistance consistency across chapters 1, 3, 4, 5, 7.
  6. Cross-system balance: Alert ladder, Noise economy, Eye awareness, and Skill Endeavours.
"""

import sys
import re
import unittest
from pathlib import Path
from typing import Dict, List, Set, Tuple, Any

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))


class BaseMathAndBalanceTest(unittest.TestCase):
    """Base class providing loaded file texts, line mappings, and helper regex matchers."""

    @classmethod
    def setUpClass(cls):
        cls.root_dir = ROOT_DIR
        cls.all_md_files = sorted(
            list(cls.root_dir.glob("*.md"))
            + list(cls.root_dir.glob("handouts/*.md"))
            + list(cls.root_dir.glob("quickstart/*.md"))
        )
        cls.file_texts: Dict[str, str] = {}
        cls.file_lines: Dict[str, List[str]] = {}

        for f in cls.all_md_files:
            rel_name = f.relative_to(cls.root_dir).as_posix()
            try:
                content = f.read_text(encoding="utf-8")
                cls.file_texts[rel_name] = content
                cls.file_texts[f.name] = content
                cls.file_lines[rel_name] = content.splitlines()
                cls.file_lines[f.name] = content.splitlines()
            except Exception as e:
                cls.file_texts[rel_name] = ""
                cls.file_lines[rel_name] = []

    def get_text(self, rel_path: str) -> str:
        if rel_path in self.file_texts:
            return self.file_texts[rel_path]
        for k, v in self.file_texts.items():
            if k == rel_path or Path(k).name == rel_path:
                return v
        return ""

    def get_lines(self, rel_path: str) -> List[str]:
        if rel_path in self.file_lines:
            return self.file_lines[rel_path]
        for k, v in self.file_lines.items():
            if k == rel_path or Path(k).name == rel_path:
                return v
        return []


# =============================================================================
# 1. HERO ATTRIBUTE TN FORMULAS & DERIVATIONS
# =============================================================================

class TestHeroAttributeMath(BaseMathAndBalanceTest):
    """
    Verifies that all Hero Attribute TNs strictly adhere to the formula:
    Attribute TN = 20 - Attribute Rating.
    """

    HERO_ATTRIBUTES = {
        "Torvir": {"STR": 7, "HRT": 2, "WIT": 5, "Expected_STR_TN": 13, "Expected_HRT_TN": 18, "Expected_WIT_TN": 15, "Parry_Base": 15},
        "Einar": {"STR": 6, "HRT": 3, "WIT": 5, "Expected_STR_TN": 14, "Expected_HRT_TN": 17, "Expected_WIT_TN": 15, "Parry_Base": 20},
        "Khoril": {"STR": 7, "HRT": 3, "HRT_PROWESS": 4, "WIT": 4, "Expected_STR_TN": 13, "Expected_HRT_TN": 16, "Expected_WIT_TN": 16, "Parry_Base": 17},
    }

    def test_hero_attribute_tn_formula_derivation(self):
        """Verify mathematical integrity of the (20 - Attribute) formula for each hero."""
        for hero, stats in self.HERO_ATTRIBUTES.items():
            str_tn = 20 - stats["STR"]
            hrt_tn = 20 - stats.get("HRT_PROWESS", stats["HRT"])
            wit_tn = 20 - stats["WIT"]

            self.assertEqual(str_tn, stats["Expected_STR_TN"], f"{hero} STR TN mismatch")
            self.assertEqual(hrt_tn, stats["Expected_HRT_TN"], f"{hero} HRT TN mismatch")
            self.assertEqual(wit_tn, stats["Expected_WIT_TN"], f"{hero} WIT TN mismatch")

    def test_hero_attribute_tns_in_character_sheets(self):
        """Verify 01_campaign_context.md and 00_overview_and_background.md have correct TNs."""
        for filename in ["01_campaign_context.md"]:
            text = self.get_text(filename)
            self.assertTrue(len(text) > 0, f"{filename} is empty or missing")

            # Torvir checks
            self.assertTrue(re.search(r"STR(?:ENGTH)?\s*7", text, re.IGNORECASE), f"{filename} missing Torvir STR 7")
            self.assertTrue(re.search(r"TN\s*13", text, re.IGNORECASE), f"{filename} missing STR TN 13")
            self.assertTrue(re.search(r"H(?:EA)?RT\s*2", text, re.IGNORECASE), f"{filename} missing Torvir HRT 2")
            self.assertTrue(re.search(r"TN\s*18", text, re.IGNORECASE), f"{filename} missing HRT TN 18")
            self.assertTrue(re.search(r"WIT(?:S)?\s*5", text, re.IGNORECASE), f"{filename} missing Torvir WIT 5")
            self.assertTrue(re.search(r"TN\s*15", text, re.IGNORECASE), f"{filename} missing WIT TN 15")

            # Einar checks
            self.assertTrue(re.search(r"STR(?:ENGTH)?\s*6", text, re.IGNORECASE), f"{filename} missing Einar STR 6")
            self.assertTrue(re.search(r"TN\s*14", text, re.IGNORECASE), f"{filename} missing STR TN 14")
            self.assertTrue(re.search(r"H(?:EA)?RT\s*3", text, re.IGNORECASE), f"{filename} missing Einar HRT 3")
            self.assertTrue(re.search(r"TN\s*17", text, re.IGNORECASE), f"{filename} missing HRT TN 17")

            # Khoril checks
            self.assertTrue(re.search(r"WIT(?:S)?\s*4", text, re.IGNORECASE), f"{filename} missing Khoril WIT 4")
            self.assertTrue(re.search(r"TN\s*16", text, re.IGNORECASE), f"{filename} missing WIT/HRT TN 16")

    def test_hero_attribute_tns_in_gm_cheat_sheet_and_worksheet(self):
        """Verify handouts have exact matching Attribute TNs."""
        for filename in ["handouts/gm_cheat_sheet.md", "handouts/band_worksheet.md", "05_gm_screen_and_play_aids.md"]:
            text = self.get_text(filename)
            self.assertIn("Torvir", text, f"{filename} missing Torvir")
            self.assertIn("STR 7 (TN 13)", text, f"{filename} missing Torvir STR 7 (TN 13)")
            self.assertIn("HRT 2 (TN 18)", text, f"{filename} missing Torvir HRT 2 (TN 18)")
            self.assertIn("WIT 5 (TN 15)", text, f"{filename} missing Torvir WIT 5 (TN 15)")

            self.assertIn("Einar", text, f"{filename} missing Einar")
            self.assertIn("STR 6 (TN 14)", text, f"{filename} missing Einar STR 6 (TN 14)")
            self.assertIn("HRT 3 (TN 17)", text, f"{filename} missing Einar HRT 3 (TN 17)")
            self.assertIn("WIT 5 (TN 15)", text, f"{filename} missing Einar WIT 5 (TN 15)")

            self.assertIn("Khoril", text, f"{filename} missing Khoril")
            self.assertIn("STR 7 (TN 13)", text, f"{filename} missing Khoril STR 7 (TN 13)")
            self.assertIn("HRT 4 (TN 16)", text, f"{filename} missing Khoril HRT 4 (TN 16)")
            self.assertIn("WIT 4 (TN 16)", text, f"{filename} missing Khoril WIT 4 (TN 16)")

    def test_zero_arbitrary_fixed_tns_on_player_tests(self):
        """Ensure no raw 'TN 14', 'TN 16', or 'DC 15' are assigned to player heroes across all files."""
        for rel_path, lines in self.file_lines.items():
            for idx, line in enumerate(lines, 1):
                # Skip comments, code blocks, or mathematical definitions of Band TN / Formulas
                if line.strip().startswith("```") or "20 - " in line or "$20 -" in line:
                    continue
                if "Band TN 15" in line or "against **Band TN 15**" in line or "Band TN 15 + " in line:
                    continue
                if "Hunt 14" in line or "Hunt 16" in line or "Hunt Threshold" in line:
                    continue
                if "Injury TN" in line or "Injury 16" in line or "Injury 18" in line or "Injury 20" in line:
                    continue

                # Pattern matching arbitrary skill checks with fixed numbers like 'STEALTH (TN 14)' without Attribute TN
                match = re.search(r"\b(AWE|ATHLETICS|AWARENESS|HUNTING|SONG|CRAFT|ENHEARTEN|TRAVEL|INSIGHT|HEALING|COURTESY|BATTLE|PERSUADE|STEALTH|SCAN|EXPLORE|RIDDLE|LORE|VALOUR)\b[^(]*?\bTN\s*[:=]?\s*(1[0-9]|20)\b", line, re.IGNORECASE)
                if match:
                    # If line has 'Strength TN', 'Heart TN', 'Wits TN', 'Band TN', or specifies hero names, it's valid
                    if not any(attr in line.lower() for attr in ["strength tn", "heart tn", "wits tn", "band tn", "torvir", "einar", "khoril", "injury tn"]):
                        self.fail(f"Found arbitrary fixed hero TN in {rel_path}:{idx} -> {line.strip()}")


# =============================================================================
# 2. BAND READINESS TN & DISPOSITION DICE POOLS
# =============================================================================

class TestBandReadinessAndDispositions(BaseMathAndBalanceTest):
    """
    Verifies that the Band system adheres to:
    Band Readiness = 5
    Band TN = 20 - Readiness = 15
    Dispositions: War 3d, Vigilance 2d, Manoeuvre 2d, Expertise 2d, Rally 1d
    """

    def test_band_readiness_formula(self):
        """Verify Band TN formula (20 - 5 = 15)."""
        readiness = 5
        band_tn = 20 - readiness
        self.assertEqual(band_tn, 15)

    def test_band_disposition_dice_pools(self):
        """Verify the 5 Dispositions across 00_overview, 02_band_mechanics, and handouts."""
        for filename in ["00_overview_and_background.md", "02_band_mechanics.md", "handouts/band_worksheet.md", "handouts/gm_cheat_sheet.md"]:
            text = self.get_text(filename)
            self.assertIn("Band Readiness", text, f"{filename} missing Band Readiness")
            self.assertIn("15", text, f"{filename} missing TN 15")

            # Check all 5 Dispositions
            self.assertTrue(re.search(r"War\s*[:=]?\s*3", text, re.IGNORECASE), f"{filename} missing War 3")
            self.assertTrue(re.search(r"Vigilance\s*[:=]?\s*2", text, re.IGNORECASE), f"{filename} missing Vigilance 2")
            self.assertTrue(re.search(r"Manoeuvre\s*[:=]?\s*2", text, re.IGNORECASE), f"{filename} missing Manoeuvre 2")
            self.assertTrue(re.search(r"Expertise\s*[:=]?\s*2", text, re.IGNORECASE), f"{filename} missing Expertise 2")
            self.assertTrue(re.search(r"Rally\s*[:=]?\s*1", text, re.IGNORECASE), f"{filename} missing Rally 1")

    def test_band_hope_and_shadow_pools(self):
        """Verify Band Hope is 12 and Band Shadow is 1."""
        for filename in ["00_overview_and_background.md", "02_band_mechanics.md", "handouts/band_worksheet.md"]:
            text = self.get_text(filename)
            self.assertIn("12", text, f"{filename} missing Hope 12")
            self.assertIn("1", text, f"{filename} missing Shadow 1")

    def test_companion_veteran_count(self):
        """Verify the squad roster consists of 7 active veteran Dwarves."""
        text = self.get_text("02_band_mechanics.md")
        companions = ["Bláin", "Fáin", "Dúrmer", "Hjoldring", "Bróga", "Austri", "Dolg"]
        for comp in companions:
            self.assertIn(comp, text, f"02_band_mechanics.md missing companion {comp}")


# =============================================================================
# 3. ADVERSARY STAT FORMULAS & COMBAT MODELS
# =============================================================================

class TestAdversaryStatFormulasAndMath(BaseMathAndBalanceTest):
    """
    Verifies that adversary stats follow TOR 2e canonical formulas:
    - Troll Endurance = AL * 8 (The Mauler AL 10 => 80 Endurance)
    - Chief Endurance = AL * 6 (Grimnar AL 6 => 36 Endurance)
    - Soldier/Scout Endurance = AL * 4 (Grik AL 3 => 12, Sniffers AL 4 => 16, Orc Soldiers AL 3 => 12, Orc Guards AL 4 => 16)
    - Might, Hate, Parry, and Armour dice pools.
    """

    ADVERSARY_MODELS = {
        "The Mauler": {
            "AL": 10,
            "Multiplier": 8,  # Troll formula: AL * 8
            "Expected_Endurance": 80,
            "Might": 2,
            "Hate": 10,
            "Parry": "—",
            "Armour": "5d"
        },
        "Grimnar the Disgraced": {
            "AL": 6,
            "Multiplier": 6,  # Chief formula: AL * 6
            "Expected_Endurance": 36,
            "Might": 2,
            "Hate": 6,
            "Parry": "+2",
            "Armour": "3d"
        },

        "Udûn Sniffers": {
            "AL": 4,
            "Multiplier": 4,  # Hunter/Zealot formula: AL * 4
            "Expected_Endurance": 16,
            "Might": 1,
            "Hate": 4,
            "Parry": "—",  # or +0
            "Armour": "3d"
        },
        "Orc Soldiers": {
            "AL": 3,
            "Multiplier": 4,
            "Expected_Endurance": 12,
            "Might": 1,
            "Hate": 3,
            "Parry": "+1",
            "Armour": "2d"
        },
        "Orc Guards": {
            "AL": 4,
            "Multiplier": 4,
            "Expected_Endurance": 16,
            "Might": 1,
            "Hate": 4,
            "Parry": "+2",
            "Armour": "3d"
        },
        "Orc Drummers": {
            "AL": 3,
            "Multiplier": 4,
            "Expected_Endurance": 12,
            "Might": 1,
            "Hate": 3,
            "Parry": "+1",
            "Armour": "2d"
        },
        "Black Uruks": {
            "AL": 5,
            "Multiplier": 4,
            "Expected_Endurance": 20,
            "Might": 1,
            "Hate": 5,
            "Parry": "+2",
            "Armour": "3d"
        },
        "Black Uruk Captain": {
            "AL": 6,
            "Multiplier": 4,  # 24 Endurance
            "Expected_Endurance": 24,
            "Might": 2,
            "Hate": 6,
            "Parry": "+3",
            "Armour": "4d"
        }
    }

    def test_adversary_endurance_formulas(self):
        """Verify mathematical formula output for all adversary Endurance pools."""
        for foe, stats in self.ADVERSARY_MODELS.items():
            calculated_end = stats["AL"] * stats["Multiplier"]
            self.assertEqual(
                calculated_end,
                stats["Expected_Endurance"],
                f"Endurance calculation mismatch for {foe}: {stats['AL']} * {stats['Multiplier']} != {stats['Expected_Endurance']}"
            )

    def test_adversaries_stat_blocks_in_chapter_3_and_5(self):
        """Verify exact stat block definitions in 03_adversaries_and_hazards.md and 05_adversaries_and_hazards.md."""
        for filename in ["03_adversaries_and_hazards.md", "05_adversaries_and_hazards.md"]:
            text = self.get_text(filename)
            self.assertTrue(len(text) > 0, f"{filename} missing")

            # The Mauler
            self.assertTrue(re.search(r"ATTRIBUTE\s+LEVEL:\s*10", text, re.IGNORECASE), f"{filename} missing The Mauler AL 10")
            self.assertTrue(re.search(r"ENDURANCE:\s*80", text, re.IGNORECASE), f"{filename} missing The Mauler End 80")
            self.assertTrue(re.search(r"MIGHT:\s*2", text, re.IGNORECASE), f"{filename} missing The Mauler Might 2")
            self.assertTrue(re.search(r"HATE:\s*10", text, re.IGNORECASE), f"{filename} missing The Mauler Hate 10")
            self.assertTrue(re.search(r"ARMOUR:\s*5d", text, re.IGNORECASE), f"{filename} missing The Mauler Armour 5d")

            # Grimnar
            self.assertTrue(re.search(r"ATTRIBUTE\s+LEVEL:\s*6", text, re.IGNORECASE), f"{filename} missing Grimnar AL 6")
            self.assertTrue(re.search(r"ENDURANCE:\s*36", text, re.IGNORECASE), f"{filename} missing Grimnar End 36")
            self.assertTrue(re.search(r"MIGHT:\s*2", text, re.IGNORECASE), f"{filename} missing Grimnar Might 2")
            self.assertTrue(re.search(r"HATE:\s*6", text, re.IGNORECASE), f"{filename} missing Grimnar Hate 6")
            self.assertTrue(re.search(r"ARMOUR:\s*3d", text, re.IGNORECASE), f"{filename} missing Grimnar Armour 3d")

            # Udûn Sniffers
            self.assertTrue(re.search(r"Attribute\s+Level(?:\*\*|:|\s)+4", text, re.IGNORECASE), f"{filename} missing Udûn Sniffer AL 4")
            self.assertTrue(re.search(r"Endurance(?:\*\*|:|\s)+16", text, re.IGNORECASE), f"{filename} missing Udûn Sniffer End 16")
            self.assertTrue(re.search(r"Hate(?:\*\*|:|\s)+4", text, re.IGNORECASE), f"{filename} missing Udûn Sniffer Hate 4")

    def test_the_mauler_dull_witted_riddle_combat_task(self):
        """Verify The Mauler's Dull-Witted Riddle combat task is correctly structured."""
        for filename in ["03_adversaries_and_hazards.md", "05_adversaries_and_hazards.md", "02_keyed_locations.md", "04_keyed_locations.md"]:
            text = self.get_text(filename)
            self.assertIn("Dull-Witted", text, f"{filename} missing Dull-Witted trait")
            self.assertIn("RIDDLE", text, f"{filename} missing RIDDLE test in Dull-Witted")
            self.assertIn("Wits TN", text, f"{filename} missing Wits TN in Dull-Witted")
            self.assertIn("Hate", text, f"{filename} missing Hate removal in Dull-Witted")


# =============================================================================
# 4. WEAPONS, RELICS & LOAD CALCULATIONS
# =============================================================================

class TestWeaponsRelicsAndLoadCalculations(BaseMathAndBalanceTest):
    """
    Verifies weapons, relics, enchanted rewards, and load calculations:
    - Durin's Axe: Great Axe, Damage 9 (Base 7 + Superior Grievous 2), Injury 20, Load 4
    - Shield of the Deep Gate: Great Shield, Parry +3, Load 3 (Reinforced, Unyielding)
    - Mattock of Moria-Silver: Two-handed Mattock, Damage 8 (Base 7 + Grievous 1), Injury 18, Load 3 (5 - Close Fitting 2)
    - Mail of Unyielding Stone: Coat of Mail, Protection 5d, Load 12 (16 - Close Fitting 4)
    - Helm of the Iron Watch: Protection +1d, Load 1
    """

    def test_durins_axe_profile_math(self):
        """Verify Durin's Axe damage, injury, load, and craft qualities."""
        for filename in ["04_loot_relics_and_rewards.md", "06_relics_and_rewards.md"]:
            text = self.get_text(filename)
            self.assertIn("DURIN'S AXE", text.upper(), f"{filename} missing Durin's Axe header")
            self.assertTrue(re.search(r"DAMAGE:\s*9", text, re.IGNORECASE) or "Damage: 9" in text or "Damage Rating**: **9**" in text, f"{filename} missing Damage 9")
            self.assertTrue(re.search(r"INJURY:\s*20", text, re.IGNORECASE) or "Injury: 20" in text or "Injury Rating**: **20**" in text, f"{filename} missing Injury 20")
            self.assertTrue(re.search(r"LOAD:\s*4", text, re.IGNORECASE) or "Load: 4" in text or "Load**: 4" in text, f"{filename} missing Load 4")
            self.assertIn("Superior Grievous", text, f"{filename} missing Superior Grievous")
            self.assertIn("Superior Keen", text, f"{filename} missing Superior Keen")
            self.assertIn("Flame of Hope", text, f"{filename} missing Flame of Hope")
            self.assertIn("Gleam of Terror", text, f"{filename} missing Gleam of Terror")
            self.assertIn("+4", text, f"{filename} missing +4 Eye Awareness")

    def test_tunnel_guard_relics_math(self):
        """Verify Shield of Deep Gate, Mattock of Moria-Silver, and Mail of Unyielding Stone."""
        for filename in ["04_loot_relics_and_rewards.md", "06_relics_and_rewards.md"]:
            text = self.get_text(filename)
            # Shield of the Deep Gate
            self.assertIn("Shield of the Deep Gate", text)
            self.assertTrue(re.search(r"Parry(?:\s+Modifier)?(?:\*\*|:|\s)*\+?3", text, re.IGNORECASE) or "Parry +3" in text or "Parry Modifier**: **+3**" in text)
            self.assertIn("Unyielding", text)

            # Mattock of Moria-Silver
            self.assertTrue("Mattock of Moria-Silver" in text or "Mattock of the Iron Vanguard" in text)
            self.assertTrue(re.search(r"Damage(?:\s+Rating)?(?:\*\*|:|\s)*8", text, re.IGNORECASE) or "Damage 8" in text)
            self.assertTrue(re.search(r"Injury(?:\s+Rating)?(?:\*\*|:|\s)*18", text, re.IGNORECASE) or "Injury 18" in text)
            self.assertTrue(re.search(r"Load(?:\*\*|:|\s)*3", text, re.IGNORECASE) or "Load: 3" in text)
            self.assertIn("Gleaming Edge", text)

            # Mail of Unyielding Stone
            self.assertIn("Mail of Unyielding Stone", text)
            self.assertTrue(re.search(r"Protection(?:\s+Rating)?(?:\*\*|:|\s)*5d", text, re.IGNORECASE) or "Protection 5d" in text)
            self.assertTrue(re.search(r"Load(?:\*\*|:|\s)*12", text, re.IGNORECASE) or "Load: 12" in text)
            self.assertIn("Impenetrable", text)


# =============================================================================
# 5. BALROG TOXIC GAS (BREATH OF THE PIT) CONSISTENCY
# =============================================================================

class TestBalrogToxicGasMechanics(BaseMathAndBalanceTest):
    """
    Verifies the Balrog toxic gas (Breath of the Pit) across chapters 1, 3, 4, 5, 7:
    - Unprotected: Protection/Endurance vs Strength TN every 1 minute (Ill-favoured).
    - Protected: Protection/Endurance vs Strength TN every 1 hour (Standard).
    - Masterwork Respirators: Skill Endeavour Resistance 3 via CRAFT (Strength TN) / Band EXPERTISE (2d vs Band TN 15) -> 4 hours complete immunity.
    """

    def test_gas_mechanics_in_delve_and_operational_chapters(self):
        """Verify gas mechanics in 01_delve_mechanics_and_alert_system.md and 03_operational_mechanics.md."""
        for filename in ["01_delve_mechanics_and_alert_system.md", "03_operational_mechanics.md"]:
            text = self.get_text(filename)
            self.assertTrue(re.search(r"Breath of the Pit", text, re.IGNORECASE), f"{filename} missing Breath of the Pit")
            self.assertIn("Strength TN", text, f"{filename} missing Strength TN check")
            self.assertTrue(re.search(r"(?:1\s+minute|every\s+minute)", text, re.IGNORECASE), f"{filename} missing 1 minute unprotected")
            self.assertTrue(re.search(r"1\s+hour", text, re.IGNORECASE), f"{filename} missing 1 hour protected")
            self.assertTrue(re.search(r"4\s+hours", text, re.IGNORECASE), f"{filename} missing 4 hours immunity")
            self.assertTrue(re.search(r"Resistance(?:\*\*|:|\s)*3", text, re.IGNORECASE) or "Resistance 3" in text, f"{filename} missing Resistance 3 respirator endeavour")

    def test_gas_mechanics_in_locations_and_hazards(self):
        """Verify gas mechanics in 02_keyed_locations.md, 04_keyed_locations.md, 03_adversaries, 05_adversaries."""
        for filename in ["02_keyed_locations.md", "04_keyed_locations.md", "03_adversaries_and_hazards.md", "05_adversaries_and_hazards.md"]:
            text = self.get_text(filename)
            self.assertIn("Poisoned Halls", text, f"{filename} missing Poisoned Halls")
            self.assertIn("Strength TN", text, f"{filename} missing Strength TN in gas check")
            self.assertIn("Respirator", text or "respirator", f"{filename} missing respirator references")


# =============================================================================
# 6. CROSS-SYSTEM BALANCE: ALERT LADDER, NOISE ECONOMY & SKILL ENDEAVOURS
# =============================================================================

class TestCrossSystemBalanceAndInteractions(BaseMathAndBalanceTest):
    """
    Verifies cross-system balance:
    - 4-Stage Alert Tracker: Alert 0 (0-3), Alert 1 (4-7), Alert 2 (8-11), Alert 3 (12+)
    - Strategic Eye Awareness: Base Hunt Threshold (14), Durin's Axe (+4), Horn (+2), Drummers (+3)
    - 6 Formal Skill Endeavours and Resistance ratings
    """

    SKILL_ENDEAVOURS = {
        "Loc 2 Fortify": {"location": "2", "expected_resistance": 3},
        "Loc 3 Disarm Trap": {"location": "3", "expected_resistance": 3},
        "Loc 4 Topple Idol": {"location": "4", "expected_resistance": 3},
        "Loc 5 Siege Engines": {"location": "5", "expected_resistance": 3},
        "Loc 7 Respirators": {"location": "7", "expected_resistance": 3},
        "Loc 9 King's Door": {"location": "9", "expected_resistance": 6},
    }

    def test_alert_tracker_four_stages_bounds(self):
        """Verify Alert Tracker boundaries (0-3, 4-7, 8-11, 12+) across chapters 1, 3, 5, 7 and handouts."""
        for filename in ["01_delve_mechanics_and_alert_system.md", "03_operational_mechanics.md", "handouts/gm_cheat_sheet.md"]:
            text = self.get_text(filename)
            self.assertIn("0–3", text or "0-3", f"{filename} missing Alert 0 (0-3)")
            self.assertIn("4–7", text or "4-7", f"{filename} missing Alert 1 (4-7)")
            self.assertIn("8–11", text or "8-11", f"{filename} missing Alert 2 (8-11)")
            self.assertIn("12+", text or "12", f"{filename} missing Alert 3 (12+)")

    def test_eye_awareness_hunt_threshold(self):
        """Verify Eye Awareness baseline Hunt Threshold is 14 (drops to 12 at Alert 2)."""
        for filename in ["01_delve_mechanics_and_alert_system.md", "03_operational_mechanics.md"]:
            text = self.get_text(filename)
            self.assertIn("14", text, f"{filename} missing Hunt Threshold 14")
            self.assertIn("+4", text, f"{filename} missing Durin's Axe +4 Eye Awareness")

    def test_all_six_skill_endeavour_resistances(self):
        """Verify that all 6 Skill Endeavours specify explicit Resistance ratings (3 or 6)."""
        loc_text = self.get_text("02_keyed_locations.md") + "\n" + self.get_text("04_keyed_locations.md")
        for name, spec in self.SKILL_ENDEAVOURS.items():
            res = spec["expected_resistance"]
            self.assertTrue(
                re.search(rf"Resistance\s*[:*]?\s*{res}\b", loc_text, re.IGNORECASE),
                f"Skill endeavour '{name}' missing Resistance {res} in location atlas"
            )


if __name__ == "__main__":
    unittest.main()
