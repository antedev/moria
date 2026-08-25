# Project: Armouries of the Third Deep — Complete TOR 2e Refactoring

## Architecture & System Foundation

### 1. The One Ring 2e (TOR 2e) Resolution Architecture
- **Hero Target Numbers (TNs)**: Derived directly from character sheets: $\text{Attribute TN} = 20 - \text{Attribute Rating}$.
  - **Torvir Hammerstone** (Champion, Dwarf of Durin): STR 7 (TN 13) | HRT 2 (TN 18) | WIT 5 (TN 15) | Parry 15 | Mail 5d
  - **Einar son of Anar** (Treasure Hunter, Dwarf of Iron Hills): STR 6 (TN 14) | HRT 3 (TN 17) | WIT 5 (TN 15) | Parry 20 | Mail 3d | *The Broken Key* (Favoured SCAN)
  - **Khoril Hornblower** (Captain, Dwarf of Durin): STR 7 (TN 13) | HRT 4 (TN 16 via Prowess) | WIT 4 (TN 16) | Parry 17 | Mail 3d | *Battle-horn of the Realm* (+1d BATTLE/RALLY, +1 AP/+2 Eye on sounding)
- **Official Modifiers**:
  - **Favoured / Ill-favoured**: Roll two Feat dice, keep the higher / lower result.
  - **Bonus / Penalty Dice**: $\pm 1\text{d}$ or $\pm 2\text{d}$.
- **Skill Endeavours**: Complex multi-step actions defined by **Resistance** (e.g. Resistance 3 to 6) and allowable attempts / consequences.
- **Band Resolution**: Balin's Vanguard Band has **Readiness 5** $\implies$ **Band TN 15** ($20 - \text{Readiness}$). Rolls 1 Feat die + Success dice equal to Disposition rating (WAR: 3d, VIGILANCE: 2d, MANOEUVRE: 2d, EXPERTISE: 2d, RALLY: 1d) against Band TN 15 (+ Foe Might in Clashes).

### 2. Standard Test Block Format
Every skill check in the module suite strictly follows the format:
- **Skill Tested**: One of the 18 official TOR 2e skills (Awe, Athletics, Awareness, Hunting, Song, Craft, Enhearten, Travel, Insight, Healing, Courtesy, Battle, Persuade, Stealth, Scan, Explore, Riddle, Lore).
- **Attribute Base**: Explicitly stated hero Attribute TN (Strength TN, Heart TN, or Wits TN).
- **Condition / Modifiers**: Favoured, Ill-favoured, $\pm 1\text{d}/\pm 2\text{d}$, or relevant Trait invocation (+1d).
- **Consequence of Failure**: Explicit narrative and mechanical penalty (Endurance loss, Weary, Shadow gain, +1/+2 Noise/Alert Points, lost time, broken tools).
- **Degrees of Success ($\mathbf{6}$ icons)**: Clear benefits for 1 $\mathbf{6}$, 2 $\mathbf{6}$s ($\mathbf{6}\mathbf{6}$), and Gandalf Rune ($\mathbf{G}$).

### 3. Trait Integrity & Vocabulary Purge
- All Distinctive Features (*Burglary*, *Enemy-lore (Orcs)*, *Fierce*, *Cunning*, *Wary*, *Leadership*, *Smith*, *Vaultbreaker*) are Traits that grant $+1\text{d}$ when invoked on applicable skill checks.
- Purged all non-canonical terms and mechanics: `+50 Garrison Supply Points`, `Burglary TN XX`, `Sleight`, `Old Lore`, `Customs`, `Advantage / +2`, `Endurance roll`, `Valour TN 14`.

---

## Feature Inventory

Every requirement from the Survey and ORIGINAL_REQUEST is cataloged below:

| # | Feature / Component | Description | Milestone | Source | Status |
|---|---------------------|-------------|-----------|--------|:------:|
| 1 | Location Atlas TN Purge & Format | Replace all 45+ fixed TNs across 10 locations with Attribute TN test blocks | M1 | R1, Survey 1 | DONE |
| 2 | Location Skill Endeavours | Formalize 6 Skill Endeavours (Loc 2 Fortify, Loc 3 Disarm, Loc 4 Topple, Loc 5 Siege, Loc 7 Respirators, Loc 9 King's Door) | M1 | R1, Survey 1 | DONE |
| 3 | Location Trait & Skill Corrections | Purge "Burglary", "Sleight", "Old Lore" from location descriptions; format Trait invocations | M1 | R1, Survey 1 | DONE |
| 4 | Node Map & Cheat Sheet Tables | Align `handouts/node_map.md` skill blocks and summary tables | M1 | R1, Survey 1 | DONE |
| 5 | Delve & Alert System Refactoring | Align 4-stage alert ladder, stealth tests (Wits TN), noise triggers with TOR 2e | M2 | R2, Survey 2 | DONE |
| 6 | Band Mechanics & Marching | Formalize Band TN 15, Khoril Travel/Leadership & Band Manoeuvre march checks, noise escalation/reduction | M2 | R2, Survey 2 | DONE |
| 7 | Balrog Miasma Environmental Rules | Formalize *Breath of the Pit* Protection tests vs Strength TN, respirator craft endeavour, herbal remedies | M2 | R2, Survey 2 | DONE |
| 8 | Operational Mechanics & Purge | Purge "+50 Garrison Supply Points" from background/operations; convert 5e modifiers | M2 | R2, Survey 2 | DONE |
| 9 | Campaign Context & Pre-Gens | Update `00_overview_and_background.md` & `01_campaign_context.md` with exact Hero Attribute TNs & traits | M2 | R2, Survey 2 | DONE |
| 10 | Adversary Stat Block Math Audit | Unify math for The Mauler (Parry —), Grimnar (End 36, Might 2, Parry +2), Grik (AL 3, End 12), Orc ranks | M3 | R3, Survey 3 | DONE |
| 11 | The Mauler Riddle Duel | Refactor "Dull-Witted" Riddle combat task in Forward stance (Wits TN, removing Hate per 6 icon) | M3 | R3, Survey 3 | DONE |
| 12 | Adversary Fell Abilities & Hazards | Convert all Strike Fear, Carapace, and hazard checks to Hero Attribute TNs (Valour vs Heart TN, etc.) | M3 | R3, Survey 3 | DONE |
| 13 | Relics & Enchanted Qualities | Refactor *Durin's Axe*, *Shield of the Deep Gate*, *Mattock of Moria-Silver*, *Mail of Unyielding Stone* to TOR 2e qualities | M4 | R4, Survey 3 | DONE |
| 14 | Loot Tables & Supply Purge | Purge "+50 Garrison Supply Points" from loot; modernize D66 scavenge tables with +1d/Favoured | M4 | R4, Survey 3 | DONE |
| 15 | GM Screen & Playbook Refactoring | Update `05_gm_screen_and_play_aids.md` and `07_gm_playbook_and_pacing.md` with Hero TN blocks and clean tests | M4 | R4, Survey 3 | DONE |
| 16 | Handouts Suite Complete Overhaul | Overhaul `handouts/gm_cheat_sheet.md`, `handouts/band_worksheet.md`, `handouts/dying_scribe_letter.md` | M4 | R4, Survey 3 | DONE |
| 17 | Automated Validation Test Suite | Build automated Python test harness checking 0 arbitrary TNs, valid skills, no supply points, stat math | E2E | Core, All | DONE |
| 18 | Suite-Wide Verification & Hardening | Run 100% E2E test suite + adversarial stress testing + forensic audit across all 19 files | Final | Acceptance | DONE |

---

## Milestones

| # | Milestone Name | Scope (Files Owned) | Dependencies | Status |
|---|----------------|---------------------|--------------|:------:|
| **M1** | Location Atlas Refactoring | `02_keyed_locations.md`<br>`04_keyed_locations.md`<br>`handouts/node_map.md` | none | **DONE** |
| **M2** | Delve, Band & Operational Mechanics | `00_overview_and_background.md`<br>`01_campaign_context.md`<br>`01_delve_mechanics_and_alert_system.md`<br>`02_band_mechanics.md`<br>`03_operational_mechanics.md` | none | **DONE** |
| **M3** | Adversaries & Hazards Certification | `03_adversaries_and_hazards.md`<br>`05_adversaries_and_hazards.md` | M1, M2 | **DONE** |
| **M4** | Relics, GM Aids & Handouts Overhaul | `04_loot_relics_and_rewards.md`<br>`06_relics_and_rewards.md`<br>`05_gm_screen_and_play_aids.md`<br>`07_gm_playbook_and_pacing.md`<br>`handouts/gm_cheat_sheet.md`<br>`handouts/band_worksheet.md`<br>`handouts/dying_scribe_letter.md` | M1, M2, M3 | **DONE** |
| **E2E** | E2E Testing Suite Track | `tests/`<br>`scripts/validate_module_suite.py`<br>`TEST_INFRA.md`<br>`TEST_READY.md` | none (Parallel Track) | **DONE** |
| **Final** | Full Suite Verification & Adversarial Hardening | All 19 files in suite | M1, M2, M3, M4, E2E | **DONE** |

---

## Final Verification Summary
- **Reviewer 1**: APPROVE (System & Rules)
- **Reviewer 2**: APPROVE (Adversaries, Relics & Handouts)
- **Challenger 1**: APPROVE (`tests/test_adversarial_coverage.py`)
- **Challenger 2**: APPROVE (`tests/test_math_and_balance.py`)
- **Forensic Auditor**: CLEAN (Zero Integrity Violations, Dynamic Scans Passing)
- **Automated Tests**: 100+ tests passing across `tests/test_tor2e_compliance.py`, `tests/test_adversarial_coverage.py`, and `tests/test_math_and_balance.py`.
