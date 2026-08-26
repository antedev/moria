# Changes Ledger — Milestone M2 (Worker M2)

**Worker**: `worker_m2`  
**Date**: 2026-08-26  
**Focus**: Core Operational Mechanics, Squad Band Systems, Adversary Certification & Hazard Refactoring  

---

## 1. Summary of Modifications

Worker M2 executed a comprehensive refactoring across 7 assigned files to achieve 100% compliance with *The One Ring 2nd Edition* (*TOR 2e*) canon, restore neutral GM presentation, remove prescriptive character scripting, and purge all non-canonical conditions (specifically the "Daunted" condition).

---

## 2. File-by-File Changes Ledger

### A. `01_campaign_context.md`
- **Section 2.3 (Journey Roles)**: Removed hardcoded `Heart TN 16` from Khoril's Expedition Guide description; refactored to standard `**TRAVEL roll** (invoking Leadership for +1d)`.
- **Section 5 (Artifacts & Relics — The Three Campaign Relics)**:
  - *The Eye of Thrym*: Neutralized from `Torvir's heirloom` to `Dwarven heirloom (carried by the expedition's vanguard/champion)`.
  - *The Broken Key*: Neutralized from `Einar's heirloom` to `Dwarven heirloom (carried by the expedition's scout/infiltrator)`.
  - *The Battle-horn of the Realm*: Neutralized from `Khoril's heirloom` to `Dwarven heirloom (carried by the expedition's captain/guide)`.

### B. `02_band_mechanics.md`
- **Section 1.1 (Band Hierarchy)**: Removed prescriptive text claiming the three pre-gens specifically command the band; refactored to generic Player-Heroes commanding a seasoned vanguard.
- **Section 2.1 (Tactical Formations)**:
  - *Point Recon*: Generalized point scout and recon screen without hardcoded PC names.
  - *Forward Scout Screen*: Replaced Einar-specific scripting with neutral Favoured **SCAN rolls** and trap identification.
  - *Shield-Wall Phalanx*: Replaced Torvir-specific scripting with frontline warriors locking shields.
- **Section 2.2 (Squad Marching Discipline)**:
  - Refactored March Test from `Khoril rolls TRAVEL (Heart TN 16)...` to `The company's Guide or leader makes a **TRAVEL roll** or **ENHEARTEN roll** (invoking a Trait such as *Leadership* for **+1d**), OR the GM rolls Band **MANOEUVRE** (2d) against **Band TN 15**`.
- **Section 2.3 (Deploying Dwarf Companions)**:
  - Salvage Craft check: Removed `Strength TN: Torvir 13, Einar 14, Khoril 13`, standardized to `**CRAFT roll** (or Band EXPERTISE [2d vs Band TN 15])`.
- **Section 2.4 (Band Casualties & Medical Recovery)**:
  - First Aid Table: Removed all hardcoded Heart TNs (`Torvir 18, Einar 17, Khoril 16`), updated to standard `**HEALING roll**` or Band `**EXPERTISE** (2d vs Band TN 15)`.
- **Section 3.1 & 3.2 (Hero Leader Actions in Band Clash)**:
  - Neutralized Command, Inspire, Fight, and Duel hero actions from pre-gen names and hardcoded TNs to open Player-Hero options using canonical TOR 2e check formats (`**BATTLE roll**`, `**ENHEARTEN roll**`, `**VALOUR test**`, combat attacks).

### C. `03_operational_mechanics.md`
- **Section 1.1 (Alert Ladder & Stealth Checks)**:
  - Alert 0: Replaced `Torvir 15, Einar 15, Khoril 16` with `**STEALTH rolls** against the hero's Target Number`.
  - Alert 2: Replaced `Einar can make Scan tests...` with `Heroes can make **SCAN rolls**`.
  - Sentry Chase / Escape: Replaced `ATHLETICS test (Strength TN: Torvir 13, Einar 14, Khoril 13...)` with `**ATHLETICS roll (Ill-favoured or at -1d)**`.
- **Section 2 (Noise Economy)**:
  - Standardized all horn references from `Khoril's Battle-horn` to `The Battle-horn of the Realm`.
- **Section 3.1 (Toxic Miasma)**:
  - Exposure Matrix: Replaced `Protection test vs Strength TN` with canonical `**PROTECTION test**` (Ill-favoured / standard) and removed non-canon dying/stasis text.
  - Countermeasures: Removed hardcoded pre-gen TNs from Crafting Respirators, Field Herbal Treatments, First Aid Triage, and Unjamming Flue; standardized to `**CRAFT roll**`, `**HEALING roll**`, and `**ATHLETICS roll**`.
- **Section 3.2 (Structural Collapse)**:
  - Standardized tests to `**PROTECTION test**` and `**ATHLETICS roll**`; removed all hardcoded pregen TNs.
- **Section 3.3 (Subterranean Water Perils)**:
  - Standardized all entries to canonical `**PROTECTION test**`, `**ENHEARTEN roll**`, `**VALOUR test**`, and `**HEALING roll**`.

### D. `05_adversaries_and_hazards.md`
- **Section 1.1 (Core Combat Rules)**:
  - Removed hardcoded pregen TNs from attack resolution formulas.
- **Section 2 (The Mauler Stat Block & Tactics)**:
  - *Dull-Witted*: Replaced `RIDDLE test (Wits TN: Torvir 15...)` with `**RIDDLE roll (Favoured)**`.
  - *Strike Fear*: **PURGED "Daunted" condition!** Replaced with canonical `All Player-heroes within sight must make a **VALOUR test** or gain **2 Shadow Points (Dread)**; heroes whose current Shadow equals or exceeds their Hope become **Miserable**.`
  - *Scavenged Iron Carapace*: Replaced `CRAFT or ATHLETICS test against their Strength TN` with `**CRAFT roll** or **ATHLETICS roll**`.
  - *Riddle Duel Mechanics*: Neutralized stance requirements, removed pregen names, replaced hardcoded TN with `**RIDDLE roll (Favoured)**`.
  - *Arena Tactics (Catwalks & Stalactites)*: Removed hardcoded TNs; replaced with `**ATHLETICS roll**` and `**CRAFT roll**`.
- **Section 3 (Grimnar the Disgraced)**:
  - *Hatred*: Neutralized to `against Dwarves of Durin's Folk and Dwarf Companions (+1d)`.
  - *Vengeful Strike*: Neutralized from `Torvir, Einar, or Khoril` to `a Player-Hero`.
  - *Ambush Tactics & Dialogue*: Neutralized target scripting and dialogue labels to archetypes (Champion, Scout, Commander).
  - *Retreat Protocol*: Replaced hardcoded TN with `**ATHLETICS roll**` or ranged attack.
- **Section 4.2 (Black Orc-Venom)**:
  - Replaced hardcoded Heart/Strength TNs with `**HEALING roll** or **PROTECTION test**`.
- **Section 5 (Environmental Hazards)**:
  - *Toxic Miasma*: Replaced all hardcoded TNs with standard `**PROTECTION test**` and `**HEALING roll**`.
  - *Slag-Worm Tremors & Collapse*: Standardized to `**SCAN roll**`, `**PROTECTION test**`, and `**ATHLETICS roll**`.
  - *Pitfalls & Chasm Crossing*: Standardized matrix to `**SCAN roll**`, `**CRAFT roll**`, and `**ATHLETICS roll**`.
  - *Water Peril Table*: Standardized to `**HEALING roll**` and `**VALOUR test**`.
- **Section 7 (GM Dashboard & Integration Rules)**:
  - Neutralized pregen names in Band Combat Integration Rules.

### E. `quickstart/00_overview_and_background.md`
- **Section 2.2 (Player Heroes Table)**:
  - Removed `(TRAVEL — Heart TN 16)` from Khoril's profile; updated to `Expedition Guide (invoking Leadership for +1d on TRAVEL rolls)`.
  - Neutralized narrative role descriptions to focus on functional delve roles without prescriptive restrictions.

### F. `quickstart/01_delve_mechanics_and_alert_system.md`
- **Section 1 (Alert Ladder)**: Replaced `Torvir 15, Einar 15, Khoril 16` with standard `**STEALTH rolls** against each hero's TN`.
- **Section 2 (Noise Economy)**: Neutralized horn entry to `Sounding the Battle-horn of the Realm`.
- **Section 3.1 & 3.2 (Squad Formations & Band Rules)**:
  - Replaced specific pregen names in ASCII tactical formation diagram with functional roles (Point Scout, Frontline Breacher, Company Guide).
  - Neutralized March Test to `The company's Guide or commander makes a **TRAVEL roll** or **ENHEARTEN roll**...`
  - Replaced `Demoralized` with canonical `**Miserable**`.
  - Replaced hardcoded Heart TNs with `**HEALING roll**`.
- **Section 4 (Environmental Hazards)**:
  - Standardized Breath of the Pit, Congealed Slag-Worms, and Structural Collapses to canonical TOR 2e roll notation without hardcoded TNs.

### G. `quickstart/03_adversaries_and_hazards.md`
- **Section 1 (The Mauler & Grimnar)**:
  - *Dull-Witted*: Standardized to `**RIDDLE roll (Favoured)**`.
  - *Strike Fear*: **PURGED "Daunted" condition!** Aligned with Valour test, Shadow Points (Dread), and Miserable condition.
  - *Scavenged Iron Carapace*: Standardized to `**CRAFT roll** or **ATHLETICS roll**`.
  - *Grimnar*: Neutralized Hatred and Vengeful Strike to neutral hero triggers.
- **Section 2 (Garrison Foes)**:
  - Udûn Sniffers *Black Venom*: Replaced hardcoded Heart/Strength TNs with `**HEALING roll** or **PROTECTION test**`.
- **Section 3 & 4 (Hazard Matrix & Water Perils)**:
  - Standardized all 5 hazard matrix rows and water peril table entries to standard TOR 2e notation (`**PROTECTION test**`, `**HEALING roll**`, `**ATHLETICS roll**`, `**SCAN roll**`, `**VALOUR test**`).

---

## 3. Verification & Compliance Summary

1. **R1 (Player Agency & Neutral Presentation)**: Verified — all prescriptive character action dictations removed across all 7 files.
2. **R2 (Streamline Skill Checks & Target Numbers)**: Verified — 0 hardcoded pregen Target Number listings remaining in operational, band, adversary, and quickstart files.
3. **R4 (Canon TOR 2e Rule Audit & Adversary Certification)**: Verified — 0 occurrences of "Daunted" condition; all stat blocks, fell abilities, and hazards strictly certified against TOR 2e canon.
