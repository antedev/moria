#!/usr/bin/env python3
"""
validate_module_suite.py — Automated Validator for Armouries of the Third Deep
=============================================================================
This script provides comprehensive static and semantic validation for all 19
markdown documents in the adventure module suite against official The One Ring 2e
(TOR 2e) core rules, Moria: Through the Doors of Durin, and ORIGINAL_REQUEST.md.

Usage:
    python scripts/validate_module_suite.py [--json] [--verbose] [--file <path>]
"""

import os
import sys
import re
import json
import argparse
from pathlib import Path
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Set, Tuple, Optional, Any

# =============================================================================
# CONSTANTS & CANONICAL RULES DATA
# =============================================================================

OFFICIAL_18_SKILLS: Set[str] = {
    # Strength
    "AWE", "ATHLETICS", "AWARENESS", "HUNTING", "SONG", "CRAFT",
    # Heart
    "ENHEARTEN", "TRAVEL", "INSIGHT", "HEALING", "COURTESY", "BATTLE",
    # Wits
    "PERSUADE", "STEALTH", "SCAN", "EXPLORE", "RIDDLE", "LORE"
}

SKILL_TO_ATTRIBUTE: Dict[str, str] = {
    "AWE": "Strength",
    "ATHLETICS": "Strength",
    "AWARENESS": "Strength",
    "HUNTING": "Strength",
    "SONG": "Strength",
    "CRAFT": "Strength",
    "ENHEARTEN": "Heart",
    "TRAVEL": "Heart",
    "INSIGHT": "Heart",
    "HEALING": "Heart",
    "COURTESY": "Heart",
    "BATTLE": "Heart",
    "PERSUADE": "Wits",
    "STEALTH": "Wits",
    "SCAN": "Wits",
    "EXPLORE": "Wits",
    "RIDDLE": "Wits",
    "LORE": "Wits",
}

CANONICAL_TRAITS: Set[str] = {
    "BURGLARY", "LEADERSHIP", "ENEMY-LORE", "ENEMY-LORE (ORCS)", "FIERCE",
    "CUNNING", "WARY", "SMITH", "VAULTBREAKER", "WILLFUL", "PROUD", "BOLD",
    "SHADOW-LORE", "TUNNEL-LORE", "STONE-CRAFT", "MIRKWOOD-LORE", "WOOD-CRAFT",
    "CURSE OF VENGEANCE", "DRAGON-SICKNESS", "LURE OF POWER"
}

PURGED_TERMS: List[Tuple[str, str]] = [
    (r"\b(?:garrison\s+supply\s+points?|\+?\d+\s*garrison\s+supply\s+points?)\b", "Garrison Supply Points (Fabricated Mechanic)"),
    (r"\bsupply\s+points?\b", "supply points (Fabricated Mechanic)"),
    (r"\b(?:sleight\s+of\s+hand|sleight\s+skill|\*\*sleight\*\*)\b", "Sleight (Non-existent TOR 2e Skill)"),
    (r"\b(?:old\s+lore|\*\*old\s+lore\*\*)\b", "Old Lore (Non-existent TOR 2e Skill)"),
    (r"\b(?:customs|\*\*customs\*\*)\b", "Customs (1e legacy skill)"),
    (r"\b(?:search\s+check|search\s+roll|\*\*search\*\*)\b", "Search check (1e legacy skill, use SCAN/EXPLORE in 2e)"),
    (r"\b(?:burglary\s+tn\s*\d+|burglary\s+check|burglary\s+test|\*\*burglary\*\*\s*\([^)]*tn[^)]*\))\b", "Burglary treated as skill check rather than Trait (+1d)"),
    (r"\b(?:advantage\s*/\s*\+2|\+2\s*/\s*advantage)\b", "Advantage / +2 (D&D 5e phrasing)"),
    (r"\b(?:saving\s+throw|saving\s+throws)\b", "Saving throw (D&D 5e phrasing)"),
    (r"\b(?:spell\s+slots?|hit\s+dice)\b", "Spell slots / Hit dice (D&D 5e phrasing)"),
    (r"\bdc\s*\d+\b", "DC (D&D 5e Difficulty Class)"),
    (r"\bdaunted\b", "Invented condition 'Daunted' (must use Shadow/Dread or Miserable)"),
]

HERO_CANONICAL_STATS = {
    "Torvir": {"STR": 7, "HRT": 2, "WIT": 5, "STR_TN": 13, "HRT_TN": 18, "WIT_TN": 15, "Parry": 15, "Mail": "5d"},
    "Einar": {"STR": 6, "HRT": 3, "WIT": 5, "STR_TN": 14, "HRT_TN": 17, "WIT_TN": 15, "Parry": 20, "Mail": "3d"},
    "Khoril": {"STR": 7, "HRT": 3, "HRT_PROWESS": 4, "WIT": 4, "STR_TN": 13, "HRT_TN": 16, "WIT_TN": 16, "Parry": 17, "Mail": "3d"},
}

BAND_CANONICAL_STATS = {
    "Readiness": 5,
    "Band_TN": 15,
    "Formula": "20 - Readiness (20 - 5 = 15)",
    "Dispositions": {
        "War": 3,
        "Vigilance": 2,
        "Manoeuvre": 2,
        "Expertise": 2,
        "Rally": 1
    }
}

SKILL_ENDEAVOUR_LOCATIONS = {
    2: {"name": "Fortifying the Forward Redoubt", "expected_resistance": 3},
    3: {"name": "Disarming the Scythe Trap Network", "expected_resistance": 3},
    4: {"name": "Controlled Toppling of the Balrog Idol", "expected_resistance": 3},
    5: {"name": "Calibrating & Arming Siege Engines", "expected_resistance": 3},
    7: {"name": "Assembling Squad Respirator Masks", "expected_resistance": 3},
    9: {"name": "Bypassing the King's Door Adamant Runic Lock", "expected_resistance": 6},
}

MODULE_FILES_ORDER: List[str] = [
    "01_campaign_context.md",
    "02_band_mechanics.md",
    "03_operational_mechanics.md",
    "04_keyed_locations.md",
    "05_adversaries_and_hazards.md",
    "06_relics_and_rewards.md",
    "07_gm_playbook_and_pacing.md",
    "quickstart/00_overview_and_background.md",
    "quickstart/01_delve_mechanics_and_alert_system.md",
    "quickstart/02_keyed_locations.md",
    "quickstart/03_adversaries_and_hazards.md",
    "quickstart/04_loot_relics_and_rewards.md",
    "quickstart/05_gm_screen_and_play_aids.md",
    "handouts/band_worksheet.md",
    "handouts/dying_scribe_letter.md",
    "handouts/gm_cheat_sheet.md",
    "handouts/node_map.md",
    "README.md",
    "PROJECT.md",
    "TEST_INFRA.md",
    "TEST_READY.md",
]

# =============================================================================
# DATA STRUCTURES
# =============================================================================

@dataclass
class ValidationIssue:
    file_path: str
    line_number: int
    severity: str  # "ERROR", "WARNING", "INFO"
    category: str  # e.g., "ARBITRARY_TN", "INVALID_SKILL", "FABRICATED_MECHANIC"
    message: str
    context: str = ""

@dataclass
class ValidationReport:
    total_files_scanned: int = 0
    passed_files: int = 0
    failed_files: int = 0
    total_issues: int = 0
    errors_count: int = 0
    warnings_count: int = 0
    tier1_errors: int = 0
    tier2_errors: int = 0
    tier3_errors: int = 0
    tier4_errors: int = 0
    issues: List[ValidationIssue] = field(default_factory=list)
    tier_summary: Dict[str, Dict[str, Any]] = field(default_factory=dict)

# =============================================================================
# MODULE SUITE VALIDATOR ENGINE
# =============================================================================

class ModuleSuiteValidator:
    def __init__(self, root_dir: Optional[Path] = None):
        if root_dir is None:
            # Locate root directory relative to this script
            self.root_dir = Path(__file__).resolve().parent.parent
        else:
            self.root_dir = Path(root_dir).resolve()
        
        self.report = ValidationReport()

    def get_all_module_files(self) -> List[Path]:
        """Returns all markdown files that belong to the adventure suite."""
        files: List[Path] = []
        for rel_path in MODULE_FILES_ORDER:
            full_path = self.root_dir / rel_path
            if full_path.exists():
                files.append(full_path)
            else:
                # Handle possible alternative path casing
                matches = list(self.root_dir.glob(rel_path))
                if matches:
                    files.append(matches[0])
        return files

    def get_adventure_content_files(self) -> List[Path]:
        """Returns only the 17 playable adventure chapter and handout files."""
        return [
            f for f in self.get_all_module_files()
            if not f.name.startswith("PROJECT") and not f.name.startswith("TEST_") and not f.name.startswith("ORIGINAL")
        ]

    # -------------------------------------------------------------------------
    # Tier 1 Checks: Feature Coverage
    # -------------------------------------------------------------------------

    def check_zero_arbitrary_hero_tns(self, file_path: Path, lines: List[str]):
        """
        Verifies that no player hero test is given an arbitrary fixed TN (e.g. TN 14, TN 16).
        Player rolls must reference the hero's Attribute TN (Strength TN, Heart TN, Wits TN)
        or Band TN 15.
        """
        # Patterns that match arbitrary fixed TNs on skill checks
        # e.g., "Athletics (TN 14)", "Stealth TN 16", "**CRAFT** (TN 15)", "Scan TN 14", "Valour TN 14", "Burglary TN 14"
        skill_regex = r"(?:\*\*|__)?\b(" + "|".join(list(OFFICIAL_18_SKILLS) + ["BURGLARY", "VALOUR", "WISDOM", "PARLEY", "GUIDE", "LEADERSHIP"]) + r")\b(?:\*\*|__)?\s*(?:\([^\)]*\)|\[[^\]]*\])?\s*(?:check|test|roll)?\s*(?:vs\.?|against)?\s*(?:TN|target\s+number|DC)\s*[:=]?\s*(1[0-9]|20)\b"
        
        # Another pattern: "Scan TN 14", "Stealth 14", "Battle 14" inside tables/matrices
        table_tn_pattern = r"\b(" + "|".join([s.title() for s in OFFICIAL_18_SKILLS] + ["Burglary", "Valour", "Old Lore", "Scan", "Stealth", "Battle", "Parley", "Craft", "Riddle"]) + r")\s+(?:TN\s*)?(1[0-9]|20)\b"

        # Explicit regex to catch "(TN 14)", "(TN 16)", "(TN 15)" when preceded by a skill
        parenthesis_tn_pattern = r"\b(" + "|".join(list(OFFICIAL_18_SKILLS) + ["Burglary", "Valour", "Wisdom", "Craft", "Stealth", "Scan", "Athletics", "Riddle", "Battle"]) + r")\s*\(\s*(?:TN\s*)?(1[0-9]|20)\s*\)"

        for idx, line in enumerate(lines, 1):
            # Skip code fences or comments that explicitly discuss the rule refactoring or formula
            if line.strip().startswith("```") or "20 - " in line or "$20 -" in line:
                continue
            if "Band TN 15" in line or "against **Band TN 15**" in line or "Band TN: 15" in line:
                continue
            if "Hero Target Numbers" in line or "No Arbitrary Hero TNs" in line or "Attribute TN" in line:
                continue
            if "STR 7 (TN 13)" in line or "HRT 2 (TN 18)" in line or "WIT 5 (TN 15)" in line or "HRT 3 (TN 17)" in line or "HRT 4 (TN 16" in line or "WIT 4 (TN 16)" in line or "STR 6 (TN 14)" in line:
                continue

            # Check skill_regex
            match = re.search(skill_regex, line, re.IGNORECASE)
            if match:
                matched_str = match.group(0)
                # Check if it's already an Attribute TN or Band TN
                if not any(attr in matched_str.lower() for attr in ["strength tn", "heart tn", "wits tn", "band tn"]):
                    self.report.issues.append(ValidationIssue(
                        file_path=str(file_path.relative_to(self.root_dir)),
                        line_number=idx,
                        severity="ERROR",
                        category="ARBITRARY_HERO_TN",
                        message=f"Found arbitrary hero Target Number: '{matched_str}'. Player checks must use Attribute TNs.",
                        context=line.strip()
                    ))
                    self.report.tier1_errors += 1

            # Check parenthesis pattern
            match_paren = re.search(parenthesis_tn_pattern, line, re.IGNORECASE)
            if match_paren:
                matched_str = match_paren.group(0)
                if not any(attr in matched_str.lower() for attr in ["strength tn", "heart tn", "wits tn", "band tn"]):
                    self.report.issues.append(ValidationIssue(
                        file_path=str(file_path.relative_to(self.root_dir)),
                        line_number=idx,
                        severity="ERROR",
                        category="ARBITRARY_HERO_TN",
                        message=f"Found parenthesized arbitrary TN: '{matched_str}'. Must reference Attribute TN.",
                        context=line.strip()
                    ))
                    self.report.tier1_errors += 1

    def check_official_18_skills_and_traits(self, file_path: Path, lines: List[str]):
        """
        Verifies that only the official 18 skills are tested, and traits (Burglary, Leadership, etc.)
        are treated as Distinctive Features / Traits granting +1d, never as rolled skills.
        """
        # Forbidden skills as rolled checks: e.g., "**BURGLARY** (Wits TN)", "Burglary check", "roll Burglary"
        trait_as_skill_pattern = r"(?:\*\*|__)\s*(BURGLARY|LEADERSHIP|ENEMY-LORE|SMITH|VAULTBREAKER|SLEIGHT|OLD\s+LORE|CUSTOMS)\s*(?:\*\*|__)\s*\("
        
        for idx, line in enumerate(lines, 1):
            if "Distinctive Features" in line or "Traits" in line or "invoking *" in line:
                continue

            match = re.search(trait_as_skill_pattern, line, re.IGNORECASE)
            if match:
                trait_name = match.group(1).upper()
                self.report.issues.append(ValidationIssue(
                    file_path=str(file_path.relative_to(self.root_dir)),
                    line_number=idx,
                    severity="ERROR",
                    category="TRAIT_TREATED_AS_SKILL",
                    message=f"Trait '{trait_name}' is formatted as a skill check. Traits must be invoked on official skills (+1d).",
                    context=line.strip()
                ))
                self.report.tier1_errors += 1

    def check_fabricated_mechanics_purge(self, file_path: Path, lines: List[str]):
        """
        Verifies that all fabricated terms (Garrison Supply Points, Sleight, Old Lore, 5e modifiers)
        are 100% purged from the document.
        """
        for idx, line in enumerate(lines, 1):
            # Skip architectural reference documents when discussing purged mechanics
            if file_path.name in ["PROJECT.md", "TEST_INFRA.md", "ORIGINAL_REQUEST.md"]:
                continue
            if "Purge" in line or "purged" in line or "Purging" in line or "Eliminate" in line:
                continue

            for pattern, desc in PURGED_TERMS:
                match = re.search(pattern, line, re.IGNORECASE)
                if match:
                    # Ignore legitimate words like "supply" if not "supply points"
                    matched_text = match.group(0)
                    self.report.issues.append(ValidationIssue(
                        file_path=str(file_path.relative_to(self.root_dir)),
                        line_number=idx,
                        severity="ERROR",
                        category="FABRICATED_MECHANIC",
                        message=f"Found fabricated or non-canonical mechanic: '{matched_text}' ({desc}).",
                        context=line.strip()
                    ))
                    self.report.tier1_errors += 1

    def check_failure_consequences_and_success_icons(self, file_path: Path, text: str):
        """
        Checks that skill check blocks in location and delve chapters define:
        1. Consequence of Failure
        2. Degrees of Success (6 icons)
        """
        if file_path.name not in ["02_keyed_locations.md", "04_keyed_locations.md", "01_delve_mechanics_and_alert_system.md", "03_operational_mechanics.md"]:
            return

        # Look for skill check headers: e.g., "* **Perimeter Infiltration — STEALTH roll:**", "* **Perimeter Infiltration — STEALTH (Wits TN...):"
        skill_blocks = re.findall(r"\*\s+\*\*[^*]+—\s*[A-Za-z\s,/]+\s*(?:roll|test|\([^\)]*TN[^\)]*\))\*\*:", text)
        
        # Check presence of standard subsections in the file
        has_failure_consequences = bool(re.search(r"\*Consequence of Failure\*|\*Failure\*|Consequence of Failure:", text, re.IGNORECASE))
        has_degrees_of_success = bool(re.search(r"\*Degrees of Success|\*Degrees of Success \(6 icons\)\*|Degrees of Success", text, re.IGNORECASE))

        if skill_blocks:
            if not has_failure_consequences:
                self.report.issues.append(ValidationIssue(
                    file_path=str(file_path.relative_to(self.root_dir)),
                    line_number=1,
                    severity="ERROR",
                    category="MISSING_FAILURE_CONSEQUENCES",
                    message="File contains skill check blocks but lacks explicit 'Consequence of Failure' sections.",
                    context=f"Found {len(skill_blocks)} skill check headers."
                ))
                self.report.tier1_errors += 1

            if not has_degrees_of_success:
                self.report.issues.append(ValidationIssue(
                    file_path=str(file_path.relative_to(self.root_dir)),
                    line_number=1,
                    severity="ERROR",
                    category="MISSING_DEGREES_OF_SUCCESS",
                    message="File contains skill check blocks but lacks explicit 'Degrees of Success (6 icons)' sections.",
                    context=f"Found {len(skill_blocks)} skill check headers."
                ))
                self.report.tier1_errors += 1

    def check_skill_endeavours(self, file_path: Path, text: str):
        """
        Checks that all formal Skill Endeavours specify explicit Resistance ratings,
        allowed skills with Attribute TNs, and failure outcomes.
        """
        if file_path.name in ["02_keyed_locations.md", "04_keyed_locations.md"]:
            # Check for the 6 key endeavours
            endeavours = re.findall(r"\*\s+\*\*Skill Endeavour:\s*([^\(]+)\(Resistance\s*(\d+)\)\*\*:", text)
            
            # Map discovered endeavours
            discovered: Dict[str, int] = {}
            for name, res_str in endeavours:
                discovered[name.strip()] = int(res_str)

            # In 02_keyed_locations.md or 04_keyed_locations.md, verify Resistance ratings are valid integers (e.g. 3, 6)
            for name, res in discovered.items():
                if res not in [3, 4, 6]:
                    self.report.issues.append(ValidationIssue(
                        file_path=str(file_path.relative_to(self.root_dir)),
                        line_number=1,
                        severity="WARNING",
                        category="NONSTANDARD_RESISTANCE",
                        message=f"Skill Endeavour '{name}' has Resistance {res}, expected 3, 4, or 6.",
                        context=f"Skill Endeavour: {name} (Resistance {res})"
                    ))

    def check_band_mechanics(self, file_path: Path, text: str):
        """
        Verifies that Band mechanics strictly adhere to Readiness 5 / Band TN 15 ($20 - 5$)
        and the 5 standard dispositions.
        """
        if file_path.name in ["02_band_mechanics.md", "00_overview_and_background.md", "01_campaign_context.md", "handouts/band_worksheet.md"]:
            # Check for Readiness 5
            if not re.search(r"Readiness(?:\s+Rating)?\s*[:=]?\s*5", text, re.IGNORECASE):
                self.report.issues.append(ValidationIssue(
                    file_path=str(file_path.relative_to(self.root_dir)),
                    line_number=1,
                    severity="ERROR",
                    category="BAND_READINESS_MISMATCH",
                    message="Band mechanics file must explicitly specify Readiness Rating: 5.",
                    context=""
                ))
                self.report.tier1_errors += 1

            # Check for Band TN 15
            if not re.search(r"Band\s+TN\s*(?:15|:\s*15|\[20\s*-\s*5\s*=\s*15\])", text, re.IGNORECASE):
                self.report.issues.append(ValidationIssue(
                    file_path=str(file_path.relative_to(self.root_dir)),
                    line_number=1,
                    severity="ERROR",
                    category="BAND_TN_MISMATCH",
                    message="Band mechanics file must explicitly specify Band TN 15 (derived from 20 - Readiness 5).",
                    context=""
                ))
                self.report.tier1_errors += 1

    def check_balrog_miasma_rules(self, file_path: Path, text: str):
        """
        Verifies that Breath of the Pit / Balrog toxic gas exposure tests use Hero Strength TNs,
        specify respirator mechanics, and herbal remedy recovery.
        """
        if file_path.name in ["01_delve_mechanics_and_alert_system.md", "03_operational_mechanics.md", "02_keyed_locations.md", "04_keyed_locations.md"]:
            if "Breath of the Pit" in text or "Balrog" in text and "Miasma" in text:
                # Should test Strength TN or Protection vs Strength TN
                if not re.search(r"(?:Strength\s+TN|Protection\s+test|PROTECTION\s+test|PROTECTION\s+roll|Protection\s+roll|Strength\s*\(TN\s*13/14\))", text, re.IGNORECASE):
                    self.report.issues.append(ValidationIssue(
                        file_path=str(file_path.relative_to(self.root_dir)),
                        line_number=1,
                        severity="ERROR",
                        category="BALROG_GAS_STRENGTH_TN",
                        message="Breath of the Pit environmental hazard must reference hero Strength TN for Protection tests.",
                        context=""
                    ))
                    self.report.tier1_errors += 1

    def check_adversary_stat_math(self, file_path: Path, text: str):
        """
        Verifies adversary stat blocks in 03_adversaries_and_hazards.md, 05_adversaries_and_hazards.md:
        - The Mauler: Parry —, Endurance 80, Might 2
        - Grimnar: AL 6, Endurance 36, Might 2, Hate 6, Parry +2
        - Udûn Sniffers: AL 4, Endurance 16, Might 1, Hate 4
        - The Mauler Dull-Witted Riddle task: Forward stance, RIDDLE (Wits TN), removes Hate per 6 icon
        """
        if file_path.name in ["03_adversaries_and_hazards.md", "05_adversaries_and_hazards.md"]:
            # Check The Mauler Parry —
            if "THE MAULER" in text.upper():
                if not re.search(r"PARRY:\s*(?:—|-|0|None)", text, re.IGNORECASE):
                    self.report.issues.append(ValidationIssue(
                        file_path=str(file_path.relative_to(self.root_dir)),
                        line_number=1,
                        severity="ERROR",
                        category="MAULER_PARRY_MISMATCH",
                        message="The Mauler's Parry must be '—' (or 0) to reflect a gigantic, lumbering creature.",
                        context=""
                    ))
                    self.report.tier1_errors += 1

                # Check Dull-Witted Riddle combat task
                if not re.search(r"Dull-Witted.*RIDDLE.*(?:Forward|Hate|Success\s+icon|6)", text, re.DOTALL | re.IGNORECASE):
                    self.report.issues.append(ValidationIssue(
                        file_path=str(file_path.relative_to(self.root_dir)),
                        line_number=1,
                        severity="ERROR",
                        category="MAULER_RIDDLE_TASK",
                        message="The Mauler's Dull-Witted fell ability must detail the RIDDLE combat task in Forward stance.",
                        context=""
                    ))
                    self.report.tier1_errors += 1

            # Check Grimnar
            if "GRIMNAR" in text.upper():
                if not re.search(r"ENDURANCE:\s*36", text):
                    self.report.issues.append(ValidationIssue(
                        file_path=str(file_path.relative_to(self.root_dir)),
                        line_number=1,
                        severity="ERROR",
                        category="GRIMNAR_ENDURANCE_MISMATCH",
                        message="Grimnar the Disgraced must have Endurance: 36.",
                        context=""
                    ))
                    self.report.tier1_errors += 1

            # Check Udûn Sniffers
            if "UDÛN SNIFFER" in text.upper() or "UDUN SNIFFER" in text.upper():
                if not re.search(r"ENDURANCE(?:\*\*|\s|:)*16", text, re.IGNORECASE):
                    self.report.issues.append(ValidationIssue(
                        file_path=str(file_path.relative_to(self.root_dir)),
                        line_number=1,
                        severity="ERROR",
                        category="SNIFFER_ENDURANCE_MISMATCH",
                        message="Udûn Sniffers must have Endurance: 16.",
                        context=""
                    ))
                    self.report.tier1_errors += 1

    def check_relic_enchanted_qualities(self, file_path: Path, text: str):
        """
        Verifies enchanted rewards and blessings on relics (Durin's Axe, Shield of the Deep Gate,
        Mattock of the Iron Vanguard, Mail of Unyielding Stone) use official TOR 2e qualities.
        """
        if file_path.name in ["04_loot_relics_and_rewards.md", "06_relics_and_rewards.md"]:
            if "DURIN'S AXE" in text.upper():
                # Check for Favoured rolls or Superior Grievous/Keen
                if not re.search(r"(?:Favoured|Superior\s+Grievous|Superior\s+Keen|Piercing\s+Blow)", text, re.IGNORECASE):
                    self.report.issues.append(ValidationIssue(
                        file_path=str(file_path.relative_to(self.root_dir)),
                        line_number=1,
                        severity="ERROR",
                        category="DURINS_AXE_QUALITIES",
                        message="Durin's Axe must specify TOR 2e Enchanted Qualities (Favoured, Superior Grievous, Superior Keen).",
                        context=""
                    ))
                    self.report.tier1_errors += 1

                # Check for Eye Awareness
                if not re.search(r"Eye\s+Awareness.*(?:\+2|\+4)", text, re.IGNORECASE):
                    self.report.issues.append(ValidationIssue(
                        file_path=str(file_path.relative_to(self.root_dir)),
                        line_number=1,
                        severity="ERROR",
                        category="DURINS_AXE_EYE_AWARENESS",
                        message="Durin's Axe must specify Eye Awareness escalation (+4 or +2) when drawn/wielded.",
                        context=""
                    ))
                    self.report.tier1_errors += 1

    def check_handouts_and_matrices(self, file_path: Path, text: str):
        """
        Verifies that handouts contain accurate Hero Attribute TNs and Band TN 15.
        """
        if file_path.name == "gm_cheat_sheet.md":
            # Must reference Hero Attribute TNs for all 3 heroes
            for hero, stats in HERO_CANONICAL_STATS.items():
                if hero not in text:
                    self.report.issues.append(ValidationIssue(
                        file_path=str(file_path.relative_to(self.root_dir)),
                        line_number=1,
                        severity="ERROR",
                        category="HANDOUT_HERO_MISSING",
                        message=f"GM Cheat Sheet must list hero '{hero}' with exact Attribute TNs.",
                        context=""
                    ))
                    self.report.tier1_errors += 1

        if file_path.name == "band_worksheet.md":
            if "Band TN 15" not in text and "TN 15" not in text:
                self.report.issues.append(ValidationIssue(
                    file_path=str(file_path.relative_to(self.root_dir)),
                    line_number=1,
                    severity="ERROR",
                    category="HANDOUT_BAND_TN_MISSING",
                    message="Band Worksheet must explicitly state Band TN 15.",
                    context=""
                ))
                self.report.tier1_errors += 1

    # -------------------------------------------------------------------------
    # Tier 2 Checks: Boundary & Corner Cases
    # -------------------------------------------------------------------------

    def check_tier2_boundaries_and_corner_cases(self, file_path: Path, lines: List[str]):
        """
        Performs boundary checks, regex edge cases, case-insensitive rogue TN detection,
        and D&D 5e phrasing detection.
        """
        # Case-insensitive rogue TN regex
        rogue_tn_patterns = [
            r"\b(?:tn|target\s+number)\s*[:=]?\s*(?:1[0-9]|20)\b",
            r"\b(?:dc)\s*[:=]?\s*(?:1[0-9]|20)\b",
            r"\b(?:difficulty\s+class|difficulty\s+rating)\s*[:=]?\s*\d+\b"
        ]

        for idx, line in enumerate(lines, 1):
            if file_path.name in ["PROJECT.md", "TEST_INFRA.md", "ORIGINAL_REQUEST.md"]:
                continue
            if line.strip().startswith("```") or "20 - " in line or "$20 -" in line:
                continue
            if "Band TN 15" in line or "against **Band TN 15**" in line or "Band TN: 15" in line:
                continue
            if "STR 7 (TN 13)" in line or "HRT 2 (TN 18)" in line or "WIT 5 (TN 15)" in line or "HRT 3 (TN 17)" in line or "HRT 4 (TN 16" in line or "WIT 4 (TN 16)" in line or "STR 6 (TN 14)" in line:
                continue

            # Check for rogue TNs when associated with a skill or player check
            for pattern in rogue_tn_patterns:
                match = re.search(pattern, line, re.IGNORECASE)
                if match:
                    # Check if line mentions player action
                    matched_text = match.group(0)
                    if any(skill in line.upper() for skill in OFFICIAL_18_SKILLS):
                        if not any(attr in line.lower() for attr in ["strength tn", "heart tn", "wits tn", "band tn"]):
                            self.report.issues.append(ValidationIssue(
                                file_path=str(file_path.relative_to(self.root_dir)),
                                line_number=idx,
                                severity="ERROR",
                                category="TIER2_ROGUE_TN_EDGE_CASE",
                                message=f"Tier 2 Rogue TN detected: '{matched_text}' in skill line.",
                                context=line.strip()
                            ))
                            self.report.tier2_errors += 1

    # -------------------------------------------------------------------------
    # Tier 3 Checks: Cross-File Consistency
    # -------------------------------------------------------------------------

    def check_tier3_cross_file_consistency(self):
        """
        Cross-checks values between chapters and handouts:
        - Hero Attribute TNs
        - Band Readiness & Band TN
        - Adversary stats
        - 10 Keyed location names and numbering
        """
        # Load all file contents into memory
        contents: Dict[str, str] = {}
        for f in self.get_all_module_files():
            try:
                contents[f.name] = f.read_text(encoding="utf-8")
            except Exception as e:
                contents[f.name] = ""

        # Cross-check Hero TNs across key files
        key_hero_files = ["00_overview_and_background.md", "01_campaign_context.md", "05_gm_screen_and_play_aids.md", "gm_cheat_sheet.md", "band_worksheet.md"]
        for fname in key_hero_files:
            if fname in contents:
                text = contents[fname]
                if "Torvir" in text:
                    if "13" not in text or "18" not in text or "15" not in text:
                        self.report.issues.append(ValidationIssue(
                            file_path=fname,
                            line_number=1,
                            severity="WARNING",
                            category="TIER3_HERO_TN_INCONSISTENCY",
                            message=f"File {fname} mentions Torvir but may be missing canonical TNs (STR 13, HRT 18, WIT 15).",
                            context=""
                        ))
                        self.report.tier3_errors += 1

        # Cross-check Band TN 15 across Band files
        band_files = ["02_band_mechanics.md", "00_overview_and_background.md", "band_worksheet.md", "gm_cheat_sheet.md"]
        for fname in band_files:
            if fname in contents:
                text = contents[fname]
                if "Band" in text and "TN 15" not in text and "15" not in text:
                    self.report.issues.append(ValidationIssue(
                        file_path=fname,
                        line_number=1,
                        severity="ERROR",
                        category="TIER3_BAND_TN_INCONSISTENCY",
                        message=f"Band reference in {fname} is missing canonical Band TN 15.",
                        context=""
                    ))
                    self.report.tier3_errors += 1

    # -------------------------------------------------------------------------
    # Tier 4 Checks: Real-World Usability & Table Readiness
    # -------------------------------------------------------------------------

    def check_tier4_real_world_usability(self):
        """
        Verifies table readiness:
        - Handouts formatted with clean markdown tables
        - Node map contains all 10 locations and connecting exits
        - Alert ladder has clear 4-stage tiers (Unwary, Suspicious, Hunted, Overrun)
        """
        node_map_file = self.root_dir / "handouts" / "node_map.md"
        if node_map_file.exists():
            text = node_map_file.read_text(encoding="utf-8")
            # Verify all 10 locations are present in node map
            for loc_num in range(1, 11):
                loc_pattern = rf"\b(?:Location|Area|Node|\b)\s*{loc_num}[\.:\s]"
                if not re.search(loc_pattern, text):
                    self.report.issues.append(ValidationIssue(
                        file_path="handouts/node_map.md",
                        line_number=1,
                        severity="WARNING",
                        category="TIER4_NODE_MAP_MISSING_LOCATION",
                        message=f"Node map does not clearly list Location/Node {loc_num}.",
                        context=""
                    ))
                    self.report.tier4_errors += 1

        # Check Alert Ladder tiers across delve mechanics and GM screen
        alert_files = [self.root_dir / "01_delve_mechanics_and_alert_system.md", self.root_dir / "05_gm_screen_and_play_aids.md"]
        for af in alert_files:
            if af.exists():
                text = af.read_text(encoding="utf-8")
                for tier_name in ["Unwary", "Suspicious", "Hunted", "Overrun"]:
                    if tier_name.lower() not in text.lower():
                        self.report.issues.append(ValidationIssue(
                            file_path=str(af.relative_to(self.root_dir)),
                            line_number=1,
                            severity="WARNING",
                            category="TIER4_ALERT_LADDER_TIER_MISSING",
                            message=f"Alert system reference missing standard tier '{tier_name}'.",
                            context=""
                        ))
                        self.report.tier4_errors += 1

    # -------------------------------------------------------------------------
    # Main Validation Orchestrator
    # -------------------------------------------------------------------------

    def validate_file(self, file_path: Path):
        """Runs all single-file validation checks on a target markdown document."""
        try:
            content = file_path.read_text(encoding="utf-8")
            lines = content.splitlines()
        except Exception as e:
            self.report.issues.append(ValidationIssue(
                file_path=str(file_path.relative_to(self.root_dir)),
                line_number=0,
                severity="ERROR",
                category="FILE_READ_ERROR",
                message=f"Failed to read file: {e}"
            ))
            self.report.errors_count += 1
            return

        initial_errors = len([i for i in self.report.issues if i.file_path == str(file_path.relative_to(self.root_dir)) and i.severity == "ERROR"])

        # Tier 1 checks
        self.check_zero_arbitrary_hero_tns(file_path, lines)
        self.check_official_18_skills_and_traits(file_path, lines)
        self.check_fabricated_mechanics_purge(file_path, lines)
        self.check_failure_consequences_and_success_icons(file_path, content)
        self.check_skill_endeavours(file_path, content)
        self.check_band_mechanics(file_path, content)
        self.check_balrog_miasma_rules(file_path, content)
        self.check_adversary_stat_math(file_path, content)
        self.check_relic_enchanted_qualities(file_path, content)
        self.check_handouts_and_matrices(file_path, content)

        # Tier 2 checks
        self.check_tier2_boundaries_and_corner_cases(file_path, lines)

        current_errors = len([i for i in self.report.issues if i.file_path == str(file_path.relative_to(self.root_dir)) and i.severity == "ERROR"])
        if current_errors == initial_errors:
            self.report.passed_files += 1
        else:
            self.report.failed_files += 1

    def run_all(self) -> ValidationReport:
        """Executes the full 4-tier validation suite across all module files."""
        files = self.get_all_module_files()
        self.report.total_files_scanned = len(files)

        for f in files:
            self.validate_file(f)

        # Suite-level cross-file checks
        self.check_tier3_cross_file_consistency()
        self.check_tier4_real_world_usability()

        # Update totals
        self.report.total_issues = len(self.report.issues)
        self.report.errors_count = len([i for i in self.report.issues if i.severity == "ERROR"])
        self.report.warnings_count = len([i for i in self.report.issues if i.severity == "WARNING"])

        self.report.tier_summary = {
            "Tier 1 (Feature Coverage)": {
                "errors": self.report.tier1_errors,
                "status": "PASS" if self.report.tier1_errors == 0 else "FAIL"
            },
            "Tier 2 (Boundary & Corner Cases)": {
                "errors": self.report.tier2_errors,
                "status": "PASS" if self.report.tier2_errors == 0 else "FAIL"
            },
            "Tier 3 (Cross-File Consistency)": {
                "errors": self.report.tier3_errors,
                "status": "PASS" if self.report.tier3_errors == 0 else "FAIL"
            },
            "Tier 4 (Real-World Usability)": {
                "errors": self.report.tier4_errors,
                "status": "PASS" if self.report.tier4_errors == 0 else "FAIL"
            }
        }

        return self.report

    def print_summary(self, verbose: bool = False):
        """Prints a human-readable, formatted summary to standard output."""
        print("=" * 80)
        print(" ARMOURIES OF THE THIRD DEEP — TOR 2e E2E VALIDATION REPORT")
        print("=" * 80)
        print(f"Total Files Scanned: {self.report.total_files_scanned}")
        print(f"Clean Passing Files: {self.report.passed_files}")
        print(f"Files with Issues:   {self.report.failed_files}")
        print(f"Total Issues Found:  {self.report.total_issues} (Errors: {self.report.errors_count}, Warnings: {self.report.warnings_count})")
        print("-" * 80)
        print("TIER BREAKDOWN:")
        for tier_name, data in self.report.tier_summary.items():
            status_tag = "[PASS]" if data["status"] == "PASS" else "[FAIL]"
            print(f"  {status_tag} {tier_name:<38} : {data['errors']} error(s)")
        print("-" * 80)

        if self.report.issues and (verbose or self.report.errors_count > 0):
            print("DETECTED ISSUES & DEFECTS (Grouped by Category):")
            category_map: Dict[str, List[ValidationIssue]] = {}
            for issue in self.report.issues:
                category_map.setdefault(issue.category, []).append(issue)

            for cat, items in category_map.items():
                print(f"\n▶ [{cat}] ({len(items)} occurrence(s)):")
                for item in items:
                    print(f"  • {item.file_path}:{item.line_number} [{item.severity}] {item.message}")
                    if item.context and verbose:
                        print(f"    Context: \"{item.context}\"")
        print("=" * 80)


# =============================================================================
# CLI ENTRY POINT
# =============================================================================

def main():
    parser = argparse.ArgumentParser(description="Validate TOR 2e compliance across adventure module markdown files.")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format.")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show verbose output with context lines.")
    parser.add_argument("--file", "-f", type=str, help="Validate a specific file instead of all files.")
    args = parser.parse_args()

    validator = ModuleSuiteValidator()
    if args.file:
        target = Path(args.file)
        if not target.is_absolute():
            target = validator.root_dir / target
        validator.report.total_files_scanned = 1
        validator.validate_file(target)
        validator.report.total_issues = len(validator.report.issues)
        validator.report.errors_count = len([i for i in validator.report.issues if i.severity == "ERROR"])
        validator.report.warnings_count = len([i for i in validator.report.issues if i.severity == "WARNING"])
    else:
        validator.run_all()

    if args.json:
        report_dict = asdict(validator.report)
        print(json.dumps(report_dict, indent=2))
    else:
        validator.print_summary(verbose=args.verbose)

    # Return exit code 1 if errors were found, 0 if clean
    sys.exit(1 if validator.report.errors_count > 0 else 0)


if __name__ == "__main__":
    main()
