#!/usr/bin/env python3
"""Unified Test Execution Harness and TOR 2e Simulation Engine.

Adventure Module: The Armouries of the Third Deep (The One Ring 2e)
Location: c:/Users/ante/Documents/Moria/tests/test_runner.py

This module provides:
1. Pure Python TOR 2e mechanical simulation models (Heroes, Band, Adversaries, Alerts, Relics, Locations).
2. Module file parser and static validator for adventure markdown publications.
3. Unified CLI test execution harness for running Tier 1-4 tests with structured diagnostics and clean exit codes.
"""

import os
import sys
import re
import argparse
import unittest
import time
from typing import Dict, List, Optional, Tuple, Set, Any


# ==============================================================================
# SECTION 1: TOR 2e MECHANICAL SIMULATION ENGINE & DATA CONTRACTS
# ==============================================================================

class Hero:
    """Player-Hero profile conforming to The One Ring 2e."""
    def __init__(
        self,
        name: str,
        culture: str,
        calling: str,
        shadow_path: str,
        strength: int,
        heart: int,
        wits: int,
        endurance: int,
        hope: int,
        parry: int,
        armour_dice: int,
        load: int = 0,
        fatigue: int = 0,
        shadow: int = 0,
        distinctive_features: Optional[List[str]] = None,
        virtues_rewards: Optional[List[str]] = None,
        gear: Optional[List[str]] = None
    ):
        self.name = name
        self.culture = culture
        self.calling = calling
        self.shadow_path = shadow_path
        self.strength = strength
        self.heart = heart
        self.wits = wits
        
        # TOR 2e Target Numbers = 20 - Attribute
        self.strength_tn = 20 - strength
        self.heart_tn = 20 - heart
        self.wits_tn = 20 - wits
        
        self.max_endurance = endurance
        self.current_endurance = endurance
        self.max_hope = hope
        self.current_hope = hope
        self.parry = parry
        self.armour_dice = armour_dice
        self.load = load
        self.fatigue = fatigue
        self.shadow = shadow
        self.distinctive_features = distinctive_features or []
        self.virtues_rewards = virtues_rewards or []
        self.gear = gear or []
        self.is_weary = False
        self.is_miserable = False
        self.wounds = 0

    @property
    def weary_threshold(self) -> int:
        return self.load + self.fatigue

    def update_conditions(self):
        self.is_weary = self.current_endurance <= self.weary_threshold
        self.is_miserable = self.current_hope <= self.shadow

    def take_damage(self, amount: int):
        self.current_endurance = max(0, self.current_endurance - amount)
        self.update_conditions()

    def heal(self, amount: int):
        self.current_endurance = min(self.max_endurance, self.current_endurance + amount)
        self.update_conditions()

    def spend_hope(self, amount: int = 1) -> bool:
        if self.is_miserable or self.current_hope < amount:
            return False
        self.current_hope -= amount
        self.update_conditions()
        return True

    def gain_shadow(self, amount: int):
        self.shadow += amount
        self.update_conditions()


class Companion:
    """Individual Dwarf Companion in Balin's Expedition Band."""
    def __init__(
        self,
        name: str,
        max_endurance: int,
        gift: str,
        quirk: str,
        tactical_role: str,
        current_endurance: Optional[int] = None,
        injury_tier: str = "Uninjured",  # Uninjured, Fleeting, Moderate, Severe, Grievous, Lingering
        is_hardened: bool = False
    ):
        self.name = name
        self.max_endurance = max_endurance
        self.current_endurance = current_endurance if current_endurance is not None else max_endurance
        self.gift = gift
        self.quirk = quirk
        self.tactical_role = tactical_role
        self.injury_tier = injury_tier
        self.is_hardened = is_hardened

    @property
    def is_incapacitated(self) -> bool:
        return self.current_endurance <= 0 or self.injury_tier in ("Grievous", "Lingering")

    def suffer_injury(self, tier: str):
        self.injury_tier = tier
        if tier == "Grievous":
            self.current_endurance = 0


class Band:
    """Moria Band System for 6-8 Veteran Companions (TOR 2e Moria p. 189-195)."""
    def __init__(
        self,
        readiness: int = 5,
        war: int = 3,
        vigilance: int = 2,
        manoeuvre: int = 2,
        expertise: int = 2,
        rally: int = 1,
        shared_hope: int = 12,
        shared_shadow: int = 1,
        companions: Optional[List[Companion]] = None,
        burden: str = "Medium"  # Light, Medium, Heavy, Overburdened
    ):
        self.readiness = readiness
        self.war = war
        self.vigilance = vigilance
        self.manoeuvre = manoeuvre
        self.expertise = expertise
        self.rally = rally
        self.shared_hope = shared_hope
        self.shared_shadow = shared_shadow
        self.burden = burden
        self.companions: List[Companion] = companions or []

    @property
    def readiness_tn(self) -> int:
        return 20 - self.readiness

    @property
    def active_count(self) -> int:
        return sum(1 for c in self.companions if not c.is_incapacitated)

    @property
    def total_count(self) -> int:
        return len(self.companions)

    @property
    def is_weary(self) -> bool:
        if not self.companions:
            return False
        incapacitated = sum(1 for c in self.companions if c.is_incapacitated)
        return (incapacitated / len(self.companions)) >= 0.5

    def spend_band_hope(self, amount: int = 1) -> bool:
        if self.shared_hope < amount:
            return False
        self.shared_hope -= amount
        return True

    def add_band_shadow(self, amount: int):
        self.shared_shadow += amount

    def resolve_casualty(self, companion_name: str, injury: str):
        for c in self.companions:
            if c.name.lower() == companion_name.lower():
                c.suffer_injury(injury)
                if injury in ("Severe", "Grievous"):
                    self.add_band_shadow(1)
                elif injury == "Slain":
                    self.add_band_shadow(2)
                    c.current_endurance = 0
                    c.injury_tier = "Lingering"
                break


class AlertTracker:
    """4-Stage Alert Tracker & Sound Economy (ORIGINAL_REQUEST R4, Moria p. 39)."""
    def __init__(self, hunt_threshold: int = 14):
        self.alert_level = 0  # 0: Quiet Shadows, 1: Unease & Scent, 2: Hunted & Barricaded, 3: Drums in the Deep
        self.eye_awareness = 0
        self.noise_points = 0
        self.hunt_threshold = hunt_threshold
        self.revelations_triggered = 0
        self.countdown_to_shaft_seal: Optional[int] = None

    def add_noise(self, points: int) -> int:
        """Add noise points and advance Alert Level / Eye Awareness."""
        self.noise_points += points
        
        # Noise progression to Alert levels:
        # 0-3 pts -> Alert 0
        # 4-7 pts -> Alert 1
        # 8-11 pts -> Alert 2
        # 12+ pts -> Alert 3
        if self.noise_points >= 12:
            self.set_alert_level(3)
        elif self.noise_points >= 8:
            self.set_alert_level(max(self.alert_level, 2))
        elif self.noise_points >= 4:
            self.set_alert_level(max(self.alert_level, 1))

        # Acoustic conversion to Eye Awareness (Lesser +1, Loud +2, Powerful +3, Extreme +4)
        if points >= 5:
            self.add_eye_awareness(3)
        elif points >= 3:
            self.add_eye_awareness(2)
        elif points >= 1:
            self.add_eye_awareness(1)

        return self.alert_level

    def add_eye_awareness(self, amount: int) -> bool:
        """Add Eye Awareness and check for Revelation Episode."""
        self.eye_awareness += amount
        if self.eye_awareness >= self.hunt_threshold:
            self.trigger_revelation()
            return True
        return False

    def set_alert_level(self, level: int):
        self.alert_level = max(0, min(3, level))
        if self.alert_level == 3 and self.countdown_to_shaft_seal is None:
            self.countdown_to_shaft_seal = 6  # 6 rounds / exploration turns to evacuate

    def trigger_revelation(self):
        self.revelations_triggered += 1
        self.eye_awareness = 0  # Resets to 0 after Revelation episode per TOR 2e canon
        self.set_alert_level(3)

    @property
    def level_name(self) -> str:
        names = {
            0: "Alert 0: Quiet Shadows",
            1: "Alert 1: Unease & Scent",
            2: "Alert 2: Hunted & Barricaded",
            3: "Alert 3: Drums in the Deep"
        }
        return names.get(self.alert_level, "Unknown")


class Adversary:
    """TOR 2e Adversary Profile and Combat Mechanics."""
    def __init__(
        self,
        name: str,
        attribute_level: int,
        endurance: int,
        might: int,
        hate: int,
        parry: int,  # 0 if '-'
        armour_dice: int,
        combat_proficiencies: Dict[str, Tuple[int, int, int, str]],  # name -> (rank, damage, injury, special)
        fell_abilities: List[str],
        distinctive_features: Optional[List[str]] = None,
        is_shadow_servant: bool = True
    ):
        self.name = name
        self.attribute_level = attribute_level
        self.max_endurance = endurance
        self.current_endurance = endurance
        self.might = might
        self.max_hate = hate
        self.current_hate = hate
        self.parry = parry
        self.armour_dice = armour_dice
        self.combat_proficiencies = combat_proficiencies
        self.fell_abilities = fell_abilities
        self.distinctive_features = distinctive_features or []
        self.is_shadow_servant = is_shadow_servant
        self.wounds = 0
        self.is_dead = False

    @property
    def is_weary(self) -> bool:
        return self.current_hate <= 0

    def spend_hate(self, amount: int = 1) -> bool:
        if self.current_hate < amount:
            return False
        self.current_hate -= amount
        return True

    def take_damage(self, amount: int):
        self.current_endurance = max(0, self.current_endurance - amount)
        if self.current_endurance == 0:
            if "Hideous Toughness" in self.fell_abilities and self.wounds == 0:
                # Triggers Piercing Blow check, resets to half endurance if alive
                self.current_endurance = self.max_endurance // 2
            else:
                self.is_dead = True

    def suffer_wound(self):
        self.wounds += 1
        if self.wounds >= self.might:
            self.is_dead = True


# ==============================================================================
# SECTION 2: ADVENTURE MODULE STATIC INSPECTOR & PARSER
# ==============================================================================

class ModuleInspector:
    """Validates markdown adventure files against TOR 2e and project specifications."""
    
    EXPECTED_FILES = [
        "README.md",
        "01_campaign_context.md",
        "02_band_mechanics.md",
        "03_operational_mechanics.md",
        "04_keyed_locations.md",
        "05_adversaries_and_hazards.md",
        "06_relics_and_rewards.md",
        "07_gm_playbook_and_pacing.md",
        "handouts/gm_cheat_sheet.md",
        "handouts/band_worksheet.md",
        "handouts/node_map.md",
        "handouts/dying_scribe_letter.md"
    ]

    EXPECTED_LOCATIONS = [
        "The Mustering-Yard",
        "The Upper Gatehouse",
        "The First Armoury",
        "The Broken Hall",
        "The Second Armoury",
        "The Hall of the Mauler",
        "The Poisoned Halls",
        "The Upper Armoury",
        "The King's Door",
        "The Lower Armoury"
    ]

    PLACEHOLDER_PATTERNS = [
        re.compile(r'\bTODO\b', re.IGNORECASE),
        re.compile(r'\bTBD\b', re.IGNORECASE),
        re.compile(r'\bFIXME\b', re.IGNORECASE),
        re.compile(r'\[placeholder\]', re.IGNORECASE),
        re.compile(r'\.\.\.\s*\(to be completed\)', re.IGNORECASE),
    ]

    def __init__(self, base_dir: str):
        self.base_dir = os.path.abspath(base_dir)

    def file_exists(self, rel_path: str) -> bool:
        full_path = os.path.join(self.base_dir, rel_path)
        return os.path.isfile(full_path)

    def read_file(self, rel_path: str) -> str:
        full_path = os.path.join(self.base_dir, rel_path)
        if not os.path.isfile(full_path):
            return ""
        with open(full_path, "r", encoding="utf-8") as f:
            return f.read()

    def check_all_files_exist(self) -> Tuple[bool, List[str]]:
        missing = [f for f in self.EXPECTED_FILES if not self.file_exists(f)]
        return len(missing) == 0, missing

    def check_placeholders(self, rel_path: str) -> List[str]:
        content = self.read_file(rel_path)
        if not content:
            return [f"File {rel_path} is missing or empty"]
        matches = []
        for i, line in enumerate(content.splitlines(), start=1):
            for pat in self.PLACEHOLDER_PATTERNS:
                if pat.search(line):
                    matches.append(f"{rel_path}:{i} matched placeholder pattern '{pat.pattern}': {line.strip()[:60]}")
        return matches

    def validate_location_structure(self, content: str) -> Dict[str, Any]:
        """Validates that keyed locations contain boxed text, GM sensory bullets, interactables, and TNs."""
        results = {}
        for loc in self.EXPECTED_LOCATIONS:
            loc_found = loc.lower() in content.lower()
            boxed_text = bool(re.search(rf'{re.escape(loc)}.*?(\n>\s+[^\n]+)', content, re.IGNORECASE | re.DOTALL))
            has_sensory = ("lighting" in content.lower() and "draft" in content.lower() and 
                           "echo" in content.lower() and "smell" in content.lower())
            has_tns = bool(re.search(r'TN\s*1[0-9]', content))
            results[loc] = {
                "found": loc_found,
                "boxed_text": boxed_text,
                "has_sensory": has_sensory,
                "has_tns": has_tns
            }
        return results

    def validate_d66_table(self, content: str) -> Tuple[bool, int, List[int]]:
        """Verifies that a D66 scavenge table has exactly 36 valid entries (11-16, 21-26, ..., 61-66)."""
        valid_rolls = [d1 * 10 + d2 for d1 in range(1, 7) for d2 in range(1, 7)]
        found_rolls = []
        for roll in valid_rolls:
            # Pattern matching roll entry like `| 11 |` or `**11**` or `11.`
            pat = rf'(?:\||\*\*|\b){roll}(?:\||\*\*|\.|\s)'
            if re.search(pat, content):
                found_rolls.append(roll)
        missing = [r for r in valid_rolls if r not in found_rolls]
        return len(missing) == 0, len(found_rolls), missing


# ==============================================================================
# SECTION 3: FACTORY HELPERS FOR CANONICAL ADVENTURE ENTITIES
# ==============================================================================

def create_canonical_heroes() -> Dict[str, Hero]:
    """Builds the 3 canonical Player-Heroes per ORIGINAL_REQUEST & PROJECT.md."""
    torvir = Hero(
        name="Torvir Hammerstone",
        culture="Dwarf of Durin's Folk",
        calling="Champion",
        shadow_path="Curse of Vengeance",
        strength=7,
        heart=2,
        wits=5,
        endurance=29,
        hope=10,
        parry=15,
        armour_dice=6,  # Mail 5d + Helm 1d
        load=24,
        fatigue=7,
        shadow=0,
        distinctive_features=["Fierce", "Willful", "Enemy-lore (Orcs)"],
        virtues_rewards=["Fierce-Minded", "Mastery (Axes)", "Grievous (Great Axe)"],
        gear=["Great Axe", "Spear", "Coat of Mail", "Helm", "The Eye of Thrym"]
    )
    
    einar = Hero(
        name="Einar son of Anar",
        culture="Dwarf of the Iron Hills",
        calling="Treasure Hunter",
        shadow_path="Dragon-sickness",
        strength=6,
        heart=3,
        wits=5,
        endurance=28,
        hope=11,
        parry=20,  # Wits 5 + Base 10 + Shield 3 + Shield Reward 1 + Durin's Way 2 = 21/20
        armour_dice=4,  # Mail 3d + Helm 1d
        load=15,
        fatigue=5,
        shadow=2,
        distinctive_features=["Cunning", "Wary", "Burglary"],
        virtues_rewards=["Durin's Way", "Keen (Sword)", "Reinforced Shield", "Mastery (Awareness, Healing)"],
        gear=["Short Sword", "Spear", "Mail-shirt", "Helm", "Reinforced Shield", "The Broken Key", "Wind-proof Lantern"]
    )
    
    khoril = Hero(
        name="Khoril Hornblower",
        culture="Dwarf of Durin's Folk",
        calling="Captain",
        shadow_path="Lure of Power",
        strength=7,
        heart=3,
        wits=4,
        endurance=29,
        hope=11,
        parry=17,
        armour_dice=4,
        load=16,
        fatigue=7,
        shadow=1,
        distinctive_features=["Wary", "Cunning", "Leadership"],
        virtues_rewards=["Prowess (Heart)", "Durin's Way", "Reinforced Shield"],
        gear=["Long-hafted Axe", "Dwarven Bow", "Mail-shirt", "Helm", "Shield", "Battle-horn of the Realm"]
    )
    
    return {"torvir": torvir, "einar": einar, "khoril": khoril}


def create_canonical_band() -> Band:
    """Builds the 7 veteran Dwarf Companions Band per Moria Band Rules."""
    companions = [
        Companion("Bláin", 18, "Goblin-Slayer", "Battle-scarred jaw", "Rearguard Cleaver", current_endurance=10, injury_tier="Moderate"),
        Companion("Fáin", 18, "Dead-Eye", "Enclosed iron helm", "Forward Sentry / Sharpshooter", current_endurance=15),
        Companion("Dúrmer", 22, "Mighty", "Iron flask drinker", "Phalanx Anchor / Breacher", current_endurance=22, is_hardened=True),
        Companion("Hjoldring", 18, "Smith", "Covered in forge soot", "Armourer & Salvage Master", current_endurance=18),
        Companion("Bróga", 12, "Vaultbreaker", "Copper & brass rings", "Sapper / Infiltrator", current_endurance=12),
        Companion("Austri", 18, "Scout", "Mutters architectural runes", "Flank Scout / Runner", current_endurance=10),
        Companion("Dolg", 18, "Shield-Bearer", "Orc weapon notch shield", "Vanguard Bulwark", current_endurance=18)
    ]
    return Band(
        readiness=5,
        war=3,
        vigilance=2,
        manoeuvre=2,
        expertise=2,
        rally=1,
        shared_hope=12,
        shared_shadow=1,
        companions=companions,
        burden="Medium"
    )


def create_canonical_adversaries() -> Dict[str, Adversary]:
    """Builds the adversary stat blocks conforming strictly to TOR 2e."""
    the_mauler = Adversary(
        name="The Mauler",
        attribute_level=10,
        endurance=80,
        might=2,
        hate=10,
        parry=0,
        armour_dice=5,
        combat_proficiencies={
            "Maul": (3, 8, 16, "Break Shield, Heavy Blow"),
            "Crush": (3, 6, 12, "Seize")
        },
        fell_abilities=[
            "Dull-Witted",
            "Hideous Toughness",
            "Strike Fear",
            "Thick Hide",
            "Scavenged Iron Carapace"
        ],
        distinctive_features=["Brutish", "Lumbering"]
    )
    
    grimnar = Adversary(
        name="Grimnar the Disgraced",
        attribute_level=6,
        endurance=32,
        might=2,
        hate=7,
        parry=3,
        armour_dice=3,
        combat_proficiencies={
            "Heavy Scimitar": (3, 5, 18, "Break Shield"),
            "Stolen Dwarven Dagger": (3, 3, 14, "Pierce"),
            "Broad-headed Spear": (2, 5, 16, "Pierce")
        },
        fell_abilities=[
            "Denizen of the Dark",
            "Hate Sunlight",
            "Hatred (Durin's Folk)",
            "Hideous Toughness",
            "Snake-like Speed",
            "Vengeful Strike"
        ],
        distinctive_features=["Fierce", "Vengeful", "Cunning"]
    )
    
    grik = Adversary(
        name="Grik the Skulker",
        attribute_level=2,
        endurance=8,
        might=1,
        hate=2,
        parry=1,
        armour_dice=1,
        combat_proficiencies={
            "Jagged Knife": (2, 2, 14, "")
        },
        fell_abilities=["Craven", "Sneak in Shadows"],
        distinctive_features=["Cunning", "Talkative", "Cowardly"]
    )
    
    udun_sniffer = Adversary(
        name="Udûn Sniffer",
        attribute_level=4,
        endurance=16,
        might=1,
        hate=4,
        parry=0,
        armour_dice=3,
        combat_proficiencies={
            "Torch-staff": (3, 4, 14, "Fiery Blow")
        },
        fell_abilities=["Denizen of the Dark", "Heartless", "Hate Sunlight"],
        distinctive_features=["Crazed", "Tough"]
    )
    
    orc_drummer = Adversary(
        name="Moria Orc Drummer",
        attribute_level=3,
        endurance=12,
        might=1,
        hate=3,
        parry=1,
        armour_dice=2,
        combat_proficiencies={
            "Orc-axe": (2, 3, 18, "Break Shield"),
            "Bow": (2, 3, 14, "Pierce")
        },
        fell_abilities=["Denizen of the Dark", "Hate Sunlight", "Drums in the Deep"],
        distinctive_features=["Deformed", "Loud"]
    )

    return {
        "the_mauler": the_mauler,
        "grimnar": grimnar,
        "grik": grik,
        "udun_sniffer": udun_sniffer,
        "orc_drummer": orc_drummer
    }


# ==============================================================================
# SECTION 4: TEST RUNNER CLI HARNESS
# ==============================================================================

class StructuredTestResult(unittest.TextTestResult):
    """Custom TestResult collecting detailed tier metrics and pass/fail diagnostics."""
    def __init__(self, stream, descriptions, verbosity):
        super().__init__(stream, descriptions, verbosity)
        self.test_records: List[Dict[str, Any]] = []

    def addSuccess(self, test):
        super().addSuccess(test)
        self.test_records.append({
            "name": str(test),
            "status": "PASS",
            "error": None
        })

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.test_records.append({
            "name": str(test),
            "status": "FAIL",
            "error": self._exc_info_to_string(err, test)
        })

    def addError(self, test, err):
        super().addError(test, err)
        self.test_records.append({
            "name": str(test),
            "status": "ERROR",
            "error": self._exc_info_to_string(err, test)
        })


def run_test_suite(tier: Optional[int] = None) -> int:
    """Executes the test suite for specified tier (1, 2, 3, 4) or all tiers."""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    tests_dir = os.path.dirname(os.path.abspath(__file__))
    
    tier_modules = {
        1: "test_tier1_features",
        2: "test_tier2_boundaries",
        3: "test_tier3_combinations",
        4: "test_tier4_workloads"
    }

    print("=" * 80)
    print("  THE ONE RING 2e — MORIA: ARMOURIES OF THE THIRD DEEP")
    print("  E2E TEST HARNESS & SYSTEM VERIFICATION")
    print("=" * 80)
    
    start_time = time.time()
    
    if tier is not None:
        if tier in tier_modules:
            mod_name = tier_modules[tier]
            print(f"[*] Running Target: Tier {tier} ({mod_name}.py)")
            mod_suite = loader.discover(tests_dir, pattern=f"{mod_name}.py")
            suite.addTests(mod_suite)
        else:
            print(f"[!] Error: Invalid tier {tier}. Valid options: 1, 2, 3, 4")
            return 1
    else:
        print("[*] Running Full E2E Test Suite (Tiers 1, 2, 3, and 4)")
        for t_idx in sorted(tier_modules.keys()):
            mod_name = tier_modules[t_idx]
            mod_suite = loader.discover(tests_dir, pattern=f"{mod_name}.py")
            suite.addTests(mod_suite)

    runner = unittest.TextTestRunner(resultclass=StructuredTestResult, verbosity=2)
    result: StructuredTestResult = runner.run(suite)
    elapsed = time.time() - start_time

    # Diagnostic Summary Table
    total_tests = result.testsRun
    failures = len(result.failures)
    errors = len(result.errors)
    passed = total_tests - (failures + errors)
    pass_rate = (passed / total_tests * 100) if total_tests > 0 else 0.0

    print("\n" + "=" * 80)
    print("                      TEST EXECUTION SUMMARY")
    print("=" * 80)
    print(f" Total Tests Run:      {total_tests}")
    print(f" Passed:               {passed}")
    print(f" Failures:             {failures}")
    print(f" Errors:               {errors}")
    print(f" Pass Rate:            {pass_rate:.1f}%")
    print(f" Total Elapsed Time:   {elapsed:.3f}s")
    print("=" * 80)

    if failures > 0 or errors > 0:
        print("\n[!] DIAGNOSTIC FAILURE DETAILS:")
        for rec in result.test_records:
            if rec["status"] in ("FAIL", "ERROR"):
                print(f"\n--- [{rec['status']}] {rec['name']} ---")
                print(rec["error"])
        return 1
    else:
        print("\n[✓] ALL TESTS PASSED SUCCESSFULLY.")
        return 0


def main():
    parser = argparse.ArgumentParser(description="Moria E2E Test Suite Runner")
    parser.add_argument("--tier", type=int, choices=[1, 2, 3, 4], help="Run tests for a specific tier only (1-4)")
    parser.add_argument("--all", action="store_true", help="Run all tiers (default)")
    args = parser.parse_args()

    target_tier = args.tier if args.tier else None
    sys.exit(run_test_suite(target_tier))


if __name__ == "__main__":
    main()
