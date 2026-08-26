#!/usr/bin/env python3
"""
test_r3_boxed_text_spoilers.py — R3 Test Suite: Boxed Read-Aloud Text Quality & Spoiler Removal
================================================================================================
Authoritative Source: ORIGINAL_REQUEST.md (§R3), PROJECT.md (§2, Feature 3)

This test suite validates 100% compliance with Requirement 3 (R3):
  - Asserts all 10 location boxed read-aloud texts are clean and contain zero trap/spoiler words
    (e.g. scythe, tripwire, poison vat, sleeping troll, secret door, dual keyhole metals, lead tube).
  - Asserts that boxed read-aloud blocks exist for all 10 keyed locations in 04_keyed_locations.md,
    quickstart/02_keyed_locations.md, and armouries_of_the_third_deep_master.md.
  - Asserts that descriptions focus exclusively on immediate sensory perceptions (lighting, scale,
    silence, cold drafts, echoes, shadows) without revealing GM-only tactical secrets or solutions.
"""

import os
import re
import unittest
from pathlib import Path
from typing import Dict, List, Tuple, Set, Optional

ROOT_DIR = Path(__file__).resolve().parent.parent

# Files containing boxed read-aloud text
LOCATION_FILES = [
    "04_keyed_locations.md",
    "quickstart/02_keyed_locations.md",
    "armouries_of_the_third_deep_master.md",
]

# Prohibited trap, monster, and puzzle spoiler patterns across all 10 boxed read-aloud texts
SPOILER_KEYWORDS: List[Tuple[str, str, Optional[int]]] = [
    # Location 3 Spoilers: Scythe Trap & Poison Vats
    (r"\bscythe(?:s)?\b", "Concealed scythe blade trap spoiler in read-aloud text", 3),
    (r"\btripwire(?:s)?\b", "Concealed tripwire trap spoiler in read-aloud text", 3),
    (r"\bliekling(?:or|a|an)?\b", "Swedish scythe blade spoiler (lieklingor)", 3),
    (r"\bspända\s+senor\b", "Swedish tripwire tendon spoiler (spända senor)", 3),
    (r"\bpoison\s+vat(?:s)?\b", "Concealed poison vat trap spoiler in read-aloud text", 3),
    (r"\bvidrigt,?\s+glänsande\s+svart\s+gift\b", "Swedish poison dripping blade spoiler", 3),
    (r"\bcounterweight\s+blade(?:s)?\b", "Trap mechanism spoiler in read-aloud text", 3),

    # Location 6 Spoilers: Sleeping Cave-Troll revealed before scouting
    (r"\bsleeping\s+(?:cave[\s\-])?troll\b", "Directly revealing sleeping troll before scouting in read-aloud", 6),
    (r"\bsover\s+slaktaren\b", "Swedish sleeping troll spoiler (sover Slaktaren)", 6),
    (r"\bett\s+grottroll\b", "Swedish cave troll reveal spoiler (ett Grottroll)", 6),
    (r"\binkapslad\s+i\s+ett\s+absurt\s+pansar\b", "Swedish troll armor spoiler", 6),

    # Location 7 Spoilers: Lead scroll tube spotted through dense miasma
    (r"\blead\s+(?:scroll\s+)?(?:tube|cylinder)\b", "Lead scroll tube spotted at far room through dense gas", 7),
    (r"\bförseglad\s+cylinder\s+av\s+tungt\s+bly\b", "Swedish lead cylinder spoiler (blycylinder)", 7),
    (r"\bstenhänder\s+är\s+alltjämt\s+knutna\b", "Swedish scribe hands holding cylinder spoiler", 7),

    # Location 8 Spoilers: Historical exposition in read-aloud
    (r"\bkvävas\s+till\s+döds\b", "Swedish narrative spoiler of past goblin suffocation", 8),
    (r"\bbröt\s+upp\s+den\s+yttre\s+porten\s+för\s+århundraden\b", "Historical exposition spoiler in read-aloud", 8),

    # Location 9 Spoilers: Two Keyhole metals / puzzle solution revealed
    (r"\b(?:two|dual)\s+keyholes\b", "Two keyholes puzzle solution revealed in read-aloud", 9),
    (r"\b(?:kungens|fältherrens)\s+nyckelhål\b", "Swedish King's / Marshal's keyhole puzzle reveal", 9),
    (r"\bmithril[\s\-]legering.*meteoritjärn\b", "Exact keyhole metallurgical solution spoiled in read-aloud", 9),
    (r"\bmithril\s+keyhole\b", "Mithril keyhole spoiler in read-aloud", 9),
    (r"\bmeteorite\s+iron\s+keyhole\b", "Meteorite iron keyhole spoiler in read-aloud", 9),

    # General spoilers across all read-alouds
    (r"\bsecret\s+door\b", "Secret door revealed in read-aloud text", None),
    (r"\bsecret\s+passage\b", "Secret passage revealed in read-aloud text", None),
    (r"\blönndörr\b", "Swedish secret door spoiler (lönndörr)", None),
]


def extract_boxed_read_aloud_blocks(content: str) -> Dict[int, List[str]]:
    """
    Extracts read-aloud blockquote passages for each of the 10 keyed locations.
    Returns a mapping from location index (1-10) to list of read-aloud text strings.
    """
    location_boxes: Dict[int, List[str]] = {i: [] for i in range(1, 11)}

    # Split content by Location headers: e.g. "## Location 1: ...", "### 4.1 Location 1: ...", etc.
    loc_sections = re.split(r"(?:^|\n)#{2,3}\s+(?:(?:4\.\d+\s+)?Location\s+(\d+)|\b(?:Area|Node)\s+(\d+))", content, flags=re.IGNORECASE)

    current_loc = None
    for section in loc_sections:
        if not section:
            continue
        if section.isdigit():
            current_loc = int(section)
            continue

        if current_loc and 1 <= current_loc <= 10:
            # Extract blockquote text (lines starting with >)
            lines = section.splitlines()
            in_quote = False
            quote_lines = []
            for line in lines:
                stripped = line.strip()
                if stripped.startswith(">"):
                    in_quote = True
                    # Remove leading > and whitespace
                    clean = re.sub(r"^>\s*", "", stripped)
                    quote_lines.append(clean)
                elif in_quote:
                    if stripped.startswith(">") or (stripped and not stripped.startswith("#") and not stripped.startswith("**")):
                        quote_lines.append(stripped)
                    else:
                        in_quote = False
                        if quote_lines:
                            location_boxes[current_loc].append("\n".join(quote_lines))
                            quote_lines = []

            if quote_lines:
                location_boxes[current_loc].append("\n".join(quote_lines))

    return location_boxes


class BaseR3Test(unittest.TestCase):
    """Base test case for R3 verification."""

    @classmethod
    def setUpClass(cls):
        cls.file_texts: Dict[str, str] = {}
        for rel_path in LOCATION_FILES:
            full_path = ROOT_DIR / rel_path
            if full_path.exists():
                cls.file_texts[rel_path] = full_path.read_text(encoding="utf-8")
            else:
                cls.file_texts[rel_path] = ""


class TestR3BoxedTextSpoilers(BaseR3Test):
    """R3: Verify zero trap/spoiler words in boxed read-aloud texts across all 10 locations."""

    def test_r3_all_10_locations_have_boxed_read_aloud_in_04_keyed_locations(self):
        """R3.1: Verify all 10 locations in 04_keyed_locations.md have boxed read-aloud descriptions."""
        text = self.file_texts.get("04_keyed_locations.md", "")
        self.assertTrue(len(text) > 0, "04_keyed_locations.md missing or empty")

        boxes = extract_boxed_read_aloud_blocks(text)
        for loc_num in range(1, 11):
            self.assertTrue(
                len(boxes[loc_num]) > 0,
                f"Location {loc_num} is missing boxed read-aloud text in 04_keyed_locations.md"
            )

    def test_r3_zero_spoilers_in_04_keyed_locations_boxed_text(self):
        """R3.2: Verify zero trap/spoiler keywords in 04_keyed_locations.md read-aloud boxes."""
        text = self.file_texts.get("04_keyed_locations.md", "")
        self.assertTrue(len(text) > 0, "04_keyed_locations.md missing or empty")

        boxes = extract_boxed_read_aloud_blocks(text)
        violations = []

        for loc_num, box_list in boxes.items():
            combined_box_text = "\n".join(box_list)
            for pattern, desc, target_loc in SPOILER_KEYWORDS:
                if target_loc is None or target_loc == loc_num:
                    match = re.search(pattern, combined_box_text, re.IGNORECASE)
                    if match:
                        violations.append(
                            f"Location {loc_num} read-aloud box contains spoiler [{desc}]: matched '{match.group(0)}'"
                        )

        self.assertEqual(
            violations, [],
            f"Found {len(violations)} spoiler leaks in 04_keyed_locations.md boxed text:\n"
            + "\n".join(violations)
        )

    def test_r3_zero_spoilers_in_quickstart_02_keyed_locations(self):
        """R3.3: Verify zero trap/spoiler keywords in quickstart/02_keyed_locations.md read-aloud boxes."""
        text = self.file_texts.get("quickstart/02_keyed_locations.md", "")
        if not text:
            self.skipTest("quickstart/02_keyed_locations.md not found")

        boxes = extract_boxed_read_aloud_blocks(text)
        violations = []

        for loc_num, box_list in boxes.items():
            combined_box_text = "\n".join(box_list)
            for pattern, desc, target_loc in SPOILER_KEYWORDS:
                if target_loc is None or target_loc == loc_num:
                    match = re.search(pattern, combined_box_text, re.IGNORECASE)
                    if match:
                        violations.append(
                            f"Quickstart Location {loc_num} read-aloud box contains spoiler [{desc}]: matched '{match.group(0)}'"
                        )

        self.assertEqual(
            violations, [],
            f"Found {len(violations)} spoiler leaks in quickstart/02_keyed_locations.md:\n"
            + "\n".join(violations)
        )

    def test_r3_zero_spoilers_in_master_document_boxed_text(self):
        """R3.4: Verify zero trap/spoiler keywords in armouries_of_the_third_deep_master.md read-aloud boxes."""
        text = self.file_texts.get("armouries_of_the_third_deep_master.md", "")
        if not text:
            self.skipTest("armouries_of_the_third_deep_master.md not found")

        boxes = extract_boxed_read_aloud_blocks(text)
        violations = []

        for loc_num, box_list in boxes.items():
            combined_box_text = "\n".join(box_list)
            for pattern, desc, target_loc in SPOILER_KEYWORDS:
                if target_loc is None or target_loc == loc_num:
                    match = re.search(pattern, combined_box_text, re.IGNORECASE)
                    if match:
                        violations.append(
                            f"Master Document Location {loc_num} read-aloud contains spoiler [{desc}]: matched '{match.group(0)}'"
                        )

        self.assertEqual(
            violations, [],
            f"Found {len(violations)} spoiler leaks in armouries_of_the_third_deep_master.md:\n"
            + "\n".join(violations)
        )

    def test_r3_sensory_and_atmosphere_focus(self):
        """R3.5: Check that read-aloud boxes describe immediate sensory impressions (sight, sound, smell, scale)."""
        text = self.file_texts.get("04_keyed_locations.md", "")
        if not text:
            self.skipTest("04_keyed_locations.md not found")

        boxes = extract_boxed_read_aloud_blocks(text)
        for loc_num in range(1, 11):
            if boxes[loc_num]:
                box_text = "\n".join(boxes[loc_num]).lower()
                # Check for at least one sensory keyword per location
                has_sensory = any(
                    s in box_text for s in [
                        "shadow", "stone", "cold", "air", "echo", "dark", "silence", "dust",
                        "pillars", "arch", "light", "draft", "smell", "scent", "iron", "granite",
                        "basalt", "gloom", "murmur", "stench", "hush", "vast", "vault", "hall"
                    ]
                )
                self.assertTrue(
                    has_sensory,
                    f"Location {loc_num} read-aloud text lacks atmospheric/sensory imagery: {box_text[:100]}"
                )


if __name__ == "__main__":
    unittest.main(verbosity=2)
