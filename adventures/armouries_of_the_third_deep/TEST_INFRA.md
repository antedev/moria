# E2E Test Infra: Armouries of the Third Deep

## Test Philosophy
- Opaque-box, requirement-driven, mathematically rigorous.
- Validates 100% adherence of all 19 module files to official *The One Ring 2e* core rules and *Moria: Through the Doors of Durin*.
- Automated static and semantic validation test harness: `tests/test_tor2e_compliance.py` / `scripts/validate_module_suite.py`.

## Feature Inventory & Test Mapping
| # | Feature / Area | Source Requirement | Tier 1 (Feature) | Tier 2 (Boundary) | Tier 3 (Cross-Feature) | Tier 4 (Workload) |
|---|----------------|-------------------|:----------------:|:-----------------:|:----------------------:|:-----------------:|
| 1 | Hero Target Numbers (Zero Arbitrary TNs) | ORIGINAL_REQUEST §1, R1–R4 | 5 tests | 5 tests | ✓ | ✓ |
| 2 | Official 18 Skills & Trait Integrity | ORIGINAL_REQUEST §2, §3 | 5 tests | 5 tests | ✓ | ✓ |
| 3 | Consequences of Failure & 6-Icon Successes | ORIGINAL_REQUEST §2, R1 | 5 tests | 5 tests | ✓ | ✓ |
| 4 | Formal Skill Endeavours (Resistance ratings) | ORIGINAL_REQUEST §1, R1 | 5 tests | 5 tests | ✓ | ✓ |
| 5 | Band Mechanics & TN 15 Formula | ORIGINAL_REQUEST §1, R2 | 5 tests | 5 tests | ✓ | ✓ |
| 6 | Balrog Gas (Breath of the Pit) Protection tests | ORIGINAL_REQUEST §1, R2 | 5 tests | 5 tests | ✓ | ✓ |
| 7 | Adversary Math & The Mauler Riddle Combat Task | ORIGINAL_REQUEST §1, R3 | 5 tests | 5 tests | ✓ | ✓ |
| 8 | Relic Enchanted Qualities & Eye Awareness | ORIGINAL_REQUEST §1, R4 | 5 tests | 5 tests | ✓ | ✓ |
| 9 | Fabricated Mechanics Purge (Garrison Supply Points) | ORIGINAL_REQUEST §3, R1–R4 | 5 tests | 5 tests | ✓ | ✓ |
| 10 | GM Aids & Handout Attribute TN Integration | ORIGINAL_REQUEST §1, R4 | 5 tests | 5 tests | ✓ | ✓ |

## Test Architecture
- **Validation Runner**: `python -m unittest discover -s tests` or `python tests/test_tor2e_compliance.py`
- **Validation Rules**:
  1. `test_no_arbitrary_hero_tns`: Scans all `.md` files for regex patterns like `TN\s*(1[0-9]|20)` on hero rolls, confirming all hero checks use Attribute TNs.
  2. `test_no_fabricated_mechanics`: Confirms zero instances of `Garrison Supply Points`, `supply points`, `Sleight`, `Old Lore`, `Burglary TN`.
  3. `test_18_official_skills`: Asserts all rolled skills are within the 18 official TOR 2e skills, and traits like *Burglary* / *Leadership* are designated as Traits.
  4. `test_adversary_math_and_stats`: Asserts The Mauler (Parry `—`, End 80, Might 2), Grimnar (End 36, Might 2, Parry +2), Grik (End 12, AL 3), and official stats.
  5. `test_skill_endeavours`: Validates that all 6 complex operations specify explicit Resistance ratings ($3, 6$).
  6. `test_handouts_and_matrices`: Asserts that `handouts/gm_cheat_sheet.md`, `handouts/band_worksheet.md`, and `handouts/node_map.md` contain accurate Hero Attribute TNs and Band TN 15.

## Coverage Thresholds
- Tier 1: ≥5 test cases per feature (50+ checks across all 19 files)
- Tier 2: Boundary & Corner cases (edge check regexes, case sensitivity, spacing, table formatting)
- Tier 3: Cross-file consistency & cross-referencing between chapters and handouts
- Tier 4: Real-world table readiness (GM cheat sheet, band worksheet, node map)
