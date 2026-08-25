# Changes Report: Delve Mechanics, Band Systems, Operational Rules & Campaign Context (Milestone 2 / R2)

**Agent**: `teamwork_preview_worker_m2_1`  
**Date**: 2026-08-25  
**Integrity Mode**: Full TOR 2e Alignment & Mathematical Rigor  

---

## 1. Executive Summary of Changes

Milestone 2 (R2) refactoring has been fully executed across the 5 owned files:
1. `00_overview_and_background.md`
2. `01_campaign_context.md`
3. `01_delve_mechanics_and_alert_system.md`
4. `02_band_mechanics.md`
5. `03_operational_mechanics.md`

All arbitrary hero target numbers (e.g. `TN 14`, `TN 16`, `TN 12`), fabricated point systems (`+50 Garrison Supply Points`), non-existent rolled skills (`Burglary`, `Leadership`, `Endurance`), and 5e terminology (`+2 / Advantage`, flat skill bonuses) have been completely eliminated. All mechanics have been restructured to strictly follow *The One Ring 2nd Edition* core rules and *Moria: Through the Doors of Durin*.

---

## 2. File-by-File Detailed Modification Log

### 2.1 `00_overview_and_background.md`
* **Hero Reference Table (Section 2.2)**:
  * **Torvir Hammerstone**: Updated mechanical profile with explicit Attribute TNs (STR 7 [TN 13], HRT 2 [TN 18], WIT 5 [TN 15]), Great Axe profile (*Damage 8, Injury 20, Pierce 9–10, Grievous*), and Traits (*Fierce*, *Willful*, *Enemy-lore (Orcs)* [+1d]). Clarified that *The Eye of Thrym* is inert in the Third Deep.
  * **Einar son of Anar**: Updated with Attribute TNs (STR 6 [TN 14], HRT 3 [TN 17], WIT 5 [TN 15]), *The Broken Key* mechanics (makes **SCAN** rolls **Favoured**), and Distinctive Features (*Cunning*, *Wary*, *Burglary* [+1d on locks/traps]).
  * **Khoril Hornblower**: Updated with Attribute TNs (STR 7 [TN 13], HRT 3 [TN 16 via *Prowess*], WIT 4 [TN 16]), *Battle-horn of the Realm* (+1d **BATTLE** / Band **WAR** or **RALLY**, +1 AP / +2 Eye on sounding), and Expedition Guide role (**TRAVEL** — Heart TN 16, invoking *Leadership* [+1d]).
* **Band Summary (Section 2.3)**:
  * Updated Band Readiness to explicit **Band TN 15** ($20 - \text{Readiness } 5$).
  * Formatted Dispositions: War 3 (3d6), Vigilance 2 (2d6), Manoeuvre 2 (2d6), Expertise 2 (2d6), Rally 1 (1d6).

### 2.2 `01_campaign_context.md`
* **Supply Points Purge (Section 1.2)**:
  * Replaced `(+50 Garrison Supply Points)` with equipping 40–50 frontline defenders in Balin's vanguard with gromril-mail and masterwork weapons, eliminating colony vulnerability and securing the Caves of Thrym Thistlebeard.
* **Player-Hero Quick Matrix (Section 2)**:
  * Embedded exact Attribute TNs for all three heroes: Torvir (STR 13/HRT 18/WIT 15), Einar (STR 14/HRT 17/WIT 15), Khoril (STR 13/HRT 16/WIT 16).
* **Einar Profile & Broken Key (Section 2.2)**:
  * Replaced D&D 5e `+2 modifier / Advantage (roll 2 Feat dice, take the best)` with official TOR 2e **Favoured** condition (roll 2 Feat dice, keep higher result).
  * Replaced `+2 to Scan in darkness` with `+1d on SCAN rolls in dark subterranean chambers`.
  * Clarified *Burglary* as a Distinctive Feature (Trait) invoked for +1d on **STEALTH**, **SCAN**, or **CRAFT** tests.
* **Khoril Profile & Battle-Horn (Section 2.3)**:
  * Replaced `Guide (TN 14)` with `Guide (TRAVEL — Heart TN 16)`.
  * Replaced `+1 to all Battle rolls` with `+1d on all BATTLE rolls made by Khoril or Band WAR / RALLY rolls`.
  * Replaced `+1 to Enhearten rolls` with `+1d on ENHEARTEN rolls`.
  * Clarified *Leadership* as a Trait invoked for +1d on **ENHEARTEN**, **TRAVEL**, or **BATTLE** tests.
* **Companion Profiles (Section 3.1)**:
  * Updated Bróga's *Vaultbreaker* to grant +1d on **CRAFT** and **STEALTH** rolls when picking locks or disarming traps, invoking the *Burglary* Trait.
* **Relic Attunement & Operational Constraints (Section 5)**:
  * Updated Relic Profile Matrix and detailed descriptions for *The Broken Key* (Favoured SCAN, +1d CRAFT via *Burglary*) and *Battle-horn of the Realm* (+1d BATTLE / Band WAR/RALLY, acoustic alert penalty).

### 2.3 `01_delve_mechanics_and_alert_system.md`
* **Alert Ladder Stealth (Section 1)**:
  * Replaced `Stealth rolls are standard difficulty (TN 14)` with `Stealth tests are resolved against Hero Wits TN (Torvir 15, Einar 15, Khoril 16)`.
* **Squad Marching Discipline (Section 3.1)**:
  * Replaced fixed TN 14 march test with: Khoril rolls **TRAVEL** (Heart TN 16) or **ENHEARTEN** (Heart TN 16), invoking *Leadership* for **+1d**, OR GM rolls Band **MANOEUVRE** (2d6) against **Band TN 15**.
  * Structured noise escalation on Failure (+1 Alert Point, +2 on Eye of Sauron) and noise reduction on Success Icons (-1 Noise Point per 6).
* **Band Deployments & Casualties (Sections 3.2 & 3.3)**:
  * Updated Upper Gatehouse Garrison benefit to grant **+1d** to extraction and withdrawal tests.
  * Updated Salvage Squad capacity to 40 suits of ancient mail and wargear.
  * Updated post-battle stabilization to **HEALING** (Heart TN: Torvir 18, Einar 17, Khoril 16) or Band **EXPERTISE** (2d vs Band TN 15).
* **Environmental Hazards (Section 4)**:
  * **Breath of the Pit**: Standardized exposure matrix with **Protection tests** against Hero **Strength TN** ($20 - \text{STR}$: Torvir 13, Einar 14, Khoril 13) every 1 minute (Ill-favoured) for Unprotected, and once per 1 hour (standard roll) for Protected. Added Masterwork Respirator 4-hour immunity. Formalized Dwarf Remedy as a Skill Endeavour (**Resistance 4**, **CRAFT** [Strength TN] or **HEALING** [Heart TN]).
  * **Slag-Worms**: Replaced fixed TN 14 with **ATHLETICS** (Strength TN: Torvir 13, Einar 14, Khoril 13) or Protection test (4d vs Strength TN).
  * **Structural Adamant Collapses**: Replaced passive TN 12 with **SCAN** (Wits TN 15, Favoured via *The Broken Key*). Bracing uses **CRAFT** (Strength TN) or Band **WAR** (3d vs Band TN 15).

### 2.4 `02_band_mechanics.md`
* **Band Dispositions & Deployments (Sections 1 & 2)**:
  * Consolidated Band TN 15 across all roles (Vigilance 2d vs Band TN 15, War 3d vs Band TN 15).
  * Replaced `Craft TN 14` with `CRAFT (Strength TN: Torvir 13, Einar 14, Khoril 13)`.
  * Replaced `+50 Garrison Supply Points` with narrative/campaign vanguard armament and royal recognition.
* **Injury & Morale Systems (Section 3)**:
  * Five Injury Tiers: Severe and Grievous injuries require First Aid (**HEALING** — Heart TN or Band **EXPERTISE** 2d vs Band TN 15).
  * Damage Threat and Fatigue testing: GM rolls Band **RALLY** (1d6) against **Band TN 15 + Threat/Fatigue Points**.
* **Group Stealth & Marching Tests (Section 4.1)**:
  * Replaced fixed TN 14 prompts with Khoril's **TRAVEL** / **ENHEARTEN** (Heart TN 16, *Leadership* +1d) or Band **MANOEUVRE** (2d6 vs Band TN 15), with noise escalation (+1 AP, +2 on Eye) and reduction on 6s (-1 Noise Point per 6).
* **Mass Combat / Band Clashes (Section 5)**:
  * **Command (Khoril)**: Khoril rolls **BATTLE** (Strength TN 13 / Heart TN 16), invoking *Leadership* for **+1d**.
  * **Inspire (Torvir or Khoril)**: Hero rolls **ENHEARTEN** (Heart TN: Torvir 18, Khoril 16).
  * **Fight (Torvir or Einar)**: Attacks resolved using Combat Proficiency against **Strength TN** (Torvir 13, Einar 14), modified by stance and adversary Parry.
  * **Duel (Torvir)**: Single combat vs enemy Champion, nullifying Might penalty.
  * **Clash Roll**: Band **WAR** (3d6) against **Band TN 15 + Enemy Might**.

### 2.5 `03_operational_mechanics.md`
* **Alert Stage Modifiers (Section 1.1)**:
  * Alert 0: Replaced `-2 penalty to passive Awareness` with `-1d to sentry Awareness; +1d to hero STEALTH / EXPLORE`.
  * Alert 2: Replaced `Athletics (TN 16)` with `ATHLETICS (Strength TN, Ill-favoured or -1d)`.
* **The Balrog Neurotoxic Miasma (Section 3.1)**:
  * Standardized Toxic Miasma Degradation Matrix to **Protection tests** against Hero **Strength TN** ($20 - \text{STR}$) every 1 minute (Ill-favoured) for Unprotected, and once per 1 hour (standard roll) for Protected.
  * Formalized Masterwork Respirators as a Skill Endeavour: **Resistance 3**, tested with **CRAFT** (Strength TN) or Band **EXPERTISE** (2d vs Band TN 15), granting 4 hours complete immunity.
  * Field Herbal Treatments: **HEALING** (Heart TN) or **CRAFT** (Strength TN).
  * First Aid Triage: **HEALING** (Heart TN, Ill-favoured if Severe, -1d if Grievous) or Band **EXPERTISE** (2d vs Band TN 15).
  * Unjamming Flue: **CRAFT** or **ATHLETICS** (Strength TN, Ill-favoured).
* **Structural Collapse & Water Perils (Sections 3.2 & 3.3)**:
  * Collapse Protection: 4d vs Strength TN. Clearing rubble: **ATHLETICS** (Strength TN) or Band **WAR** (3d vs Band TN 15).
  * Water Perils: Replaced `Valour test (TN 14)` on bitter mineral water with a **Protection test** against **Strength TN** (or **ENHEARTEN** vs Heart TN).

---

## 3. Compliance Matrix

| Rule / Requirement | Status | Verification Result |
| :--- | :---: | :--- |
| Zero fixed Hero TNs (TN 12, TN 14, TN 16) | **PASS** | 100% of hero tests use Strength TN, Heart TN, or Wits TN. |
| Band TN 15 ($20 - \text{Readiness } 5$) | **PASS** | All Band tests use Band TN 15 + modifiers. |
| Band Marching Discipline | **PASS** | Khoril TRAVEL/ENHEARTEN (Heart TN 16, *Leadership* +1d) or Band MANOEUVRE (2d vs TN 15), noise escalation on failure, noise reduction on 6s. |
| Balrog Gas Hazard (*Breath of the Pit*) | **PASS** | Protection vs Strength TN every 1 min (Unprotected) / 1 hr (Protected), Resistance 3 Respirator Endeavour (4 hrs immunity). |
| Purge `+50 Garrison Supply Points` | **PASS** | 0 occurrences across all 5 files; replaced with narrative/campaign vanguard armament and royal recognition. |
| Trait & Skill Integrity | **PASS** | *Burglary*, *Leadership*, *Smith*, *Enemy-lore* formatted as Traits granting +1d on valid official skills. No non-canonical skills. |
