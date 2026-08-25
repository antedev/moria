# Orchestrator Execution Plan: Armouries of the Third Deep Refactoring

## Objectives
Coordinate complete and rigorous refactoring of all adventure module files and handouts for "Armouries of the Third Deep" to strictly align with *The One Ring 2e* (TOR 2e) core rules and *Moria: Through the Doors of Durin*.

## Step-by-Step Execution Plan

### Step 1: Survey & Mapping (Phase 1)
- Dispatch 3 parallel Explorers:
  - **Explorer 1 (Locations & Atlas)**: Survey `02_keyed_locations.md`, `04_keyed_locations.md`, `handouts/node_map.md` to identify all fixed TNs, skill checks, complex multi-step actions (Skill Endeavours), and missing failure/success mechanics.
  - **Explorer 2 (Delve, Band & Operational Systems)**: Survey `01_delve_mechanics_and_alert_system.md`, `02_band_mechanics.md`, `03_operational_mechanics.md`, `00_overview_and_background.md`, `01_campaign_context.md` to identify non-standard mechanics, TN prompts, Band march/readiness rules, toxic gas exposure tests, and fabricated terms ("garrison supply points").
  - **Explorer 3 (Adversaries, Hazards, Relics, GM Aids & Handouts)**: Survey `03_adversaries_and_hazards.md`, `05_adversaries_and_hazards.md`, `04_loot_relics_and_rewards.md`, `06_relics_and_rewards.md`, `05_gm_screen_and_play_aids.md`, `07_gm_playbook_and_pacing.md`, `handouts/gm_cheat_sheet.md`, `handouts/band_worksheet.md`, `handouts/dying_scribe_letter.md`. Check adversary math, Riddle combat task, enchanted rewards/blessings, hero attribute TNs, and traits.

### Step 2: Synthesis & PROJECT.md / TEST_INFRA.md Construction
- Aggregate explorer survey reports into `PROJECT.md` with:
  - Feature Inventory (all requirements mapped to milestones)
  - Code Layout & File Write Ownership
  - Interface Contracts & Mechanics Standards
- Launch E2E Testing Track via `teamwork_preview_test_writer` / test orchestrator to create automated validation harness (`scripts/validate_module_suite.py` or similar) to strictly check for:
  - Zero arbitrary TNs ("TN 14", "TN 16", etc. on hero tests)
  - Valid 18 official skills and proper Distinctive Feature traits
  - Zero fabricated terms ("garrison supply points", "sleight skill")
  - Complete test block structures (Skill, Attribute Base, Modifiers, Failure Consequence, Extra Success 6s)
  - Exact hero stats (Torvir, Einar, Khoril) and Band TN 15
  - Adversary stat block math and formatting
  - Skill Endeavour Resistance format

### Step 3: Sequential / Parallel Milestone Execution
- **Milestone 1 (R1 - Location Atlas)**: Worker refactors 02 and 04 keyed locations. Reviewers (2), Challengers (2), Auditor verify.
- **Milestone 2 (R2 - Delve & Operational Mechanics)**: Worker refactors 01 delve, 02 band, 03 operational mechanics. Reviewers (2), Challengers (2), Auditor verify.
- **Milestone 3 (R3 - Adversaries & Hazards)**: Worker refactors 03 & 05 adversary stat blocks, combat proficiencies, The Mauler mechanics. Reviewers (2), Challengers (2), Auditor verify.
- **Milestone 4 (R4 - Relics, GM Aids & Handouts)**: Worker refactors 04, 05, 06, 07 and all handouts (`handouts/gm_cheat_sheet.md`, `handouts/band_worksheet.md`, etc.). Reviewers (2), Challengers (2), Auditor verify.

### Step 4: Final Verification & Adversarial Coverage Hardening
- Phase 1: Run 100% E2E automated test suite across all 19 files.
- Phase 2: Adversarial Coverage Hardening via Challengers.
- Forensic Auditor complete suite audit.

### Step 5: Final Completion Report to Sentinel
- Report outcome to Sentinel with verified evidence.
