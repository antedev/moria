# Project: Armouries of the Third Deep — Comprehensive Revision (R1–R5)

## Architecture & System Foundation

### 1. The One Ring 2e (TOR 2e) Resolution Architecture & Agency
- **Player Agency (R1)**: The GM presents environmental features, sensory cues, and hazards neutrally. Players choose their company's response, marching roles, and skill actions. Zero prescriptive text assuming specific PC actions (no "Khoril rolls...", "Einar searches...", "Torvir invokes...").
- **Hero Skill Tests (R2)**: All tests are presented in standard TOR 2e notation (e.g. "**SCAN roll**", "**STEALTH roll**", "**EXPLORE roll**", "**CRAFT roll**"). Zero hardcoded pregen Target Numbers (e.g. `(Wits TN: Torvir 15, Einar 15, Khoril 16)`). Players roll against the Target Numbers on their own character sheets (TN = $20 - \text{Attribute}$).
- **Difficulty & Modifiers**: Handled strictly through official TOR 2e mechanisms:
  - **Favoured / Ill-favoured**: Roll two Feat dice, keep higher / lower.
  - **Bonus / Penalty Dice**: $\pm 1\text{d}$ or $\pm 2\text{d}$.
  - **Trait Invocations**: Distinctive Features (e.g. *Burglary*, *Enemy-lore (Orcs)*, *Fierce*, *Cunning*, *Wary*, *Leadership*, *Smith*, *Vaultbreaker*) grant $+1\text{d}$ when invoked on applicable skill rolls.
  - **Skill Endeavours**: Complex actions defined by **Resistance** (e.g. Resistance 3 to 6) and allowable attempts / consequences.
  - **Band Resolution**: Band TN 15 ($20 - \text{Readiness 5}$) with Disposition ratings.

### 2. Boxed Read-Aloud Text Standards (R3)
- Evocative, concise, atmospheric descriptions providing only immediate sensory impressions (sight, sound, smell, scale, temperature, lighting) upon entering a location.
- **Zero Spoilers**: Concealed tripwires, scythe traps, poison vats, ambush positions, hidden doors, sleeping trolls, and puzzle mechanisms are strictly omitted from read-aloud text and detailed only in GM reference sections.

### 3. Canonical TOR 2e Conditions & Mechanics (R4)
- Complete purge of non-canonical conditions (specifically **"Daunted"** — 0 occurrences across repository).
- Canonical consequences: **Weary**, **Miserable**, **Wounded**, **Endurance Loss**, **Shadow Points (Dread / Greed / Sorcery / Misdeed)**, **Hope Loss**, and **Bout of Madness triggers**.
- Adversary stat blocks, Fell Abilities (e.g., *Strike Fear*, *Craven*, *Horrible Strength*), and combat proficiencies strictly verified against TOR 2e rules.

### 4. Build Pipeline & Presentation Synchronization (R5)
- All modular markdown files (`01`–`07`), quickstart files (`quickstart/00`–`05`), and handouts (`handouts/*.md`) are synchronized.
- Build scripts (`scripts/build_master_document.py`, `scripts/build_handouts.py`, `scripts/render_handouts.py`) compile the updated `armouries_of_the_third_deep_master.md`, HTML, and PDF print assets with 0 errors.

---

## Feature Inventory

| # | Feature / Directive | Description | Milestone | Source | Status |
|---|---------------------|-------------|-----------|--------|:------:|
| 1 | Neutral Scene Presentation (Locations) | Eliminate prescriptive PC actions in 02 & 04 keyed locations | M1 | R1, Survey 1 | DONE |
| 2 | Keyed Locations TN Streamlining | Remove all `(Attribute TN: Torvir X, ...)` from 02 & 04 locations | M1 | R2, Survey 1 | DONE |
| 3 | Read-Aloud Boxed Text Overhaul | Rewrite all 10 location read-aloud boxes (remove trap/clue spoilers) | M1 | R3, Survey 1 | DONE |
| 4 | Purge "Daunted" in Locations | Replace all 4 occurrences in 04_keyed_locations with canon conditions | M1 | R4, Survey 1 | DONE |
| 5 | Quickstart Locations Alignment | Neutralize agency, remove TNs, rewrite boxed text in quickstart/02 | M1 | R1-R4, Survey 2 | DONE |
| 6 | Delve & Band Agency & TN Cleanup | Neutralize agency and remove pregen TNs in 01 delve, 02 band, 03 operations | M2 | R1, R2, Survey 1 | DONE |
| 7 | Campaign Overview & Quickstart 00-01 | Remove prescriptive scripting in 00/01 overview and quickstart/00-01 | M2 | R1, R2, Survey 2 | DONE |
| 8 | Adversaries & Hazards Audit | Remove "Daunted" (05_adversaries line 115, quickstart/03), audit Fell Abilities | M2 | R4, Survey 1, 2 | DONE |
| 9 | Relics & Loot Agency/TN Cleanup | Neutralize agency and remove pregen TNs in 04/06 relics & loot | M3 | R1, R2, Survey 1 | DONE |
| 10 | GM Playbook & Aids Refactoring | Update 05/07 GM screen & playbook with neutral phrasing and clean tests | M3 | R1, R2, Survey 1 | DONE |
| 11 | Handouts Suite Overhaul | Update cheat sheet, band worksheet, node map, scribe letter (no TNs/scripts) | M3 | R1, R2, Survey 2 | DONE |
| 12 | Quickstart 04-05 Synchronization | Align quickstart appendices and loot with canon TOR 2e and clean tests | M3 | R1-R5, Survey 2 | DONE |
| 13 | Build Pipeline Script Updates | Update build_master_document.py, render_handouts.py, validate_module_suite.py | M4 | R5, Survey 3 | DONE |
| 14 | Master Document & Asset Compilation | Recompile master markdown, HTML, and PDF assets with 0 errors | M4 | R5, Survey 3 | DONE |
| 15 | Automated Validator & E2E Tests | Update test suite in tests/ and validate_module_suite.py for R1-R5 | E2E | Acceptance | DONE |
| 16 | Final Review & Forensic Integrity Audit | Multi-agent review, challenger stress testing, and forensic audit | Final | Acceptance | DONE |

---

## Milestones

| # | Milestone Name | Scope (Files Owned) | Dependencies | Status |
|---|----------------|---------------------|--------------|:------:|
| **M1** | Keyed Locations Atlas (Chapters 02/04 & Quickstart 02) | `02_keyed_locations.md`<br>`04_keyed_locations.md`<br>`quickstart/02_keyed_locations.md` | none | **DONE** |
| **M2** | Delve, Band, Overview, Adversaries & Hazards | `00_overview_and_background.md`<br>`01_campaign_context.md`<br>`01_delve_mechanics_and_alert_system.md`<br>`02_band_mechanics.md`<br>`03_operational_mechanics.md`<br>`03_adversaries_and_hazards.md`<br>`05_adversaries_and_hazards.md`<br>`quickstart/00_adventure_overview.md`<br>`quickstart/01_delve_and_band_mechanics.md`<br>`quickstart/03_adversaries_and_hazards.md` | none | **DONE** |
| **M3** | Relics, GM Playbook, Handouts & Quickstart Sync | `04_loot_relics_and_rewards.md`<br>`06_relics_and_rewards.md`<br>`05_gm_screen_and_play_aids.md`<br>`07_gm_playbook_and_pacing.md`<br>`quickstart/04_loot_and_rewards.md`<br>`quickstart/05_appendices.md`<br>`handouts/gm_cheat_sheet.md`<br>`handouts/band_worksheet.md`<br>`handouts/node_map.md`<br>`handouts/dying_scribe_letter.md` | M1, M2 | **DONE** |
| **M4** | Build Pipeline & Presentation Compilation | `scripts/build_master_document.py`<br>`scripts/render_handouts.py`<br>`scripts/validate_module_suite.py`<br>`armouries_of_the_third_deep_master.md`<br>`print/`<br>`handouts/html/`<br>`handouts/pdf/` | M1, M2, M3 | **DONE** |
| **E2E** | E2E Testing & Validation Track | `tests/`<br>`TEST_INFRA.md`<br>`TEST_READY.md` | none (Parallel) | **DONE** |
| **Final** | Full Suite Verification & Forensic Integrity Audit | All files across module suite | M1, M2, M3, M4, E2E | **DONE** |

---

## Final Verification Summary
- **Reviewer 1 (Chapters & Quickstarts)**: APPROVE
- **Reviewer 2 (Adversaries, Relics & Presentation Assets)**: APPROVE
- **Challenger 1 (Adversarial Stress Testing & Pattern Scans)**: APPROVE (158 tests passing, 0 errors, 0 "Daunted", 0 TN leaks)
- **Challenger 2 (Math, Mechanics & Build Execution)**: APPROVE (Adversary formulas, Band TN 15, Skill Endeavours, Build Scripts clean)
- **Forensic Auditor**: CLEAN (Zero Integrity Violations, Authentic Implementation, Genuine Build Pipeline)
- **Automated Test Results**: 158 / 158 tests passing with returncode 0 across all 8 suites in `tests/`.
