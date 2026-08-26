# E2E Test Infrastructure Specification: Armouries of the Third Deep

## Test Philosophy & Architectural Principles
- **Authoritative & Requirement-Driven**: Validates 100% adherence of all 22 markdown documents, HTML assets, and build pipelines in the repository against official *The One Ring 2e* (TOR 2e) core rules, *Moria: Through the Doors of Durin*, and `ORIGINAL_REQUEST.md`.
- **Zero-Tolerance Quality Gates**: Enforces strict prohibition of prescriptive PC scripting (R1), hardcoded pre-gen Target Numbers (R2), trap/spoiler leaks in boxed read-aloud descriptions (R3), non-canonical conditions like "Daunted" (R4), and desynchronized document assembly (R5).
- **Dual Harness Integration**: Combines Python standard `unittest` test suites in `tests/` with the standalone CLI validator `scripts/validate_module_suite.py`.

---

## Comprehensive Test Suite Architecture

| Suite / Module | Focus & Core Requirements | Primary Invariants Verified |
|:---|:---|:---|
| `tests/test_r1_pc_scripting.py` | **R1: Player Agency & Neutral Scene Presentation** | • 0 prescriptive PC skill roll dictates (e.g. `Khoril rolls`, `Einar searches`)<br>• 0 prescriptive trait invocations on named heroes (`Torvir invoking`)<br>• 0 forced player failure reactions (e.g. rage cutscenes, forced greed)<br>• 0 hardcoded participant assignments in tactical Band options or combat duels |
| `tests/test_r2_pregen_tns.py` | **R2: TN Architecture & Pregen TN Purge** | • 0 hardcoded pre-gen TN listings (e.g. `Torvir 15, Einar 15, Khoril 16`)<br>• Standard TOR 2e check format (`**SKILL roll**`, `**SKILL test**`)<br>• Zero arbitrary hero fixed TNs (e.g. `TN 14`, `TN 16`)<br>• Hero Attribute TNs ($20 - \text{Attribute}$) kept strictly on character sheets |
| `tests/test_r3_boxed_text_spoilers.py` | **R3: Boxed Read-Aloud Text Quality & Spoilers** | • 10/10 location read-aloud boxes present and evocative<br>• 0 concealed trap spoilers (scythe blades, tripwires, poison vats)<br>• 0 sleeping monster reveals (sleeping cave-troll in Location 6)<br>• 0 secret puzzle solution leaks (lead scroll tube, dual keyhole metals) |
| `tests/test_r4_adversary_conditions.py` | **R4: Canon TOR 2e Rules & Adversary Math** | • 0 occurrences of non-canonical "Daunted" condition across all files<br>• Canonical fear & dread mechanics (Shadow/Dread, Miserable, Weary, Hope loss)<br>• The Mauler (AL 10, End 80, Might 2, Hate 10, Parry `—`, Dull-Witted Riddle)<br>• Grimnar the Disgraced (AL 6, End 36, Might 2, Hate 6, Parry +2) |
| `tests/test_r5_assembly_and_sync.py` | **R5: Master Assembly & Synchronization** | • Master document (`armouries_of_the_third_deep_master.md`) assembly integrity<br>• All 7 modular chapters (`01`–`07`) + 4 handouts (App A–D) in exact order<br>• Synchronization across modular chapters, quickstart files, and handouts<br>• Build script readiness (`build_master_document.py`, `render_handouts.py`) |
| `tests/test_tor2e_compliance.py` | **TOR 2e 4-Tier Comprehensive Compliance** | • Tier 1: Systematic Feature Coverage across all 10 core system features<br>• Tier 2: Boundary & Corner Cases (case-insensitivity, 5e vocabulary leaks)<br>• Tier 3: Cross-File Consistency across 22 markdown documents<br>• Tier 4: Real-World Table Usability (matrices, handouts, GM dashboards) |
| `tests/test_math_and_balance.py` | **Mathematical Consistency & Balance Models** | • Hero Attribute TN formula derivations ($20 - \text{Attribute}$)<br>• Band Readiness formula ($20 - 5 = 15$) and Disposition dice pools<br>• Adversary Endurance formulas ($\text{AL} \times 8$ troll, $\text{AL} \times 6$ chief, $\text{AL} \times 4$ soldier)<br>• Weapon damage, load, injury ratings, and Balrog toxic gas timers |
| `tests/test_adversarial_coverage.py` | **Independent Adversarial Stress Suite** | • Multi-vector stress testing for rogue TNs, DC leaks, fake skills<br>• Verification of 6 canonical Skill Endeavours (Resistance 3, 6)<br>• Verification of Eye Awareness escalation mechanics (+4, +2) |

---

## Test Execution Commands

### 1. Execute Full Python Test Suite
```bash
python -m unittest discover -s tests -v
```

### 2. Execute Specific Requirement Suites
```bash
# R1: Player Agency & Neutral Scene Presentation
python -m unittest tests/test_r1_pc_scripting.py -v

# R2: Target Number Architecture & Pregen TN Purge
python -m unittest tests/test_r2_pregen_tns.py -v

# R3: Boxed Read-Aloud Text Quality & Spoiler Removal
python -m unittest tests/test_r3_boxed_text_spoilers.py -v

# R4: Canon TOR 2e Conditions & Adversary Stats
python -m unittest tests/test_r4_adversary_conditions.py -v

# R5: Master Document Assembly & Synchronization
python -m unittest tests/test_r5_assembly_and_sync.py -v
```

### 3. Execute Standalone CLI Suite Validator
```bash
python scripts/validate_module_suite.py -v
python scripts/validate_module_suite.py --json
```

---

## Document Inventory Under Test (22 Markdown Files)
1. `01_campaign_context.md`
2. `02_band_mechanics.md`
3. `03_operational_mechanics.md`
4. `04_keyed_locations.md`
5. `05_adversaries_and_hazards.md`
6. `06_relics_and_rewards.md`
7. `07_gm_playbook_and_pacing.md`
8. `armouries_of_the_third_deep_master.md`
9. `handouts/band_worksheet.md`
10. `handouts/dying_scribe_letter.md`
11. `handouts/gm_cheat_sheet.md`
12. `handouts/node_map.md`
13. `quickstart/00_overview_and_background.md`
14. `quickstart/01_delve_mechanics_and_alert_system.md`
15. `quickstart/02_keyed_locations.md`
16. `quickstart/03_adversaries_and_hazards.md`
17. `quickstart/04_loot_relics_and_rewards.md`
18. `quickstart/05_gm_screen_and_play_aids.md`
19. `PROJECT.md`
20. `README.md`
21. `TEST_INFRA.md`
22. `TEST_READY.md`
