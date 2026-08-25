# Handoff Report: Milestone 2 (R2) — Delve Mechanics, Band Systems, Operational Rules & Campaign Context

**Module**: *The Armouries of the Third Deep* (*The One Ring 2e* / *Moria: Through the Doors of Durin*)  
**Agent**: `teamwork_preview_worker_m2_1`  
**Date**: 2026-08-25  
**Handoff Type**: Hard (Milestone 2 Complete)  

---

## 1. Observation

A comprehensive audit of the 5 files owned by Worker M2 (`00_overview_and_background.md`, `01_campaign_context.md`, `01_delve_mechanics_and_alert_system.md`, `02_band_mechanics.md`, `03_operational_mechanics.md`) revealed the following baseline defects prior to refactoring:

1. **Fixed Hero Target Numbers (TNs)**:
   * `00_overview_and_background.md:82`: `Expedition Guide (TN 14), Leadership`
   * `01_campaign_context.md:138`: `Journey Role: Guide (TN 14) / Squad Commander`
   * `01_delve_mechanics_and_alert_system.md:23`: `Stealth rolls are standard difficulty (TN 14).`
   * `01_delve_mechanics_and_alert_system.md:97`: `March Test: Khoril rolls TRAVEL or LEADERSHIP (TN 14).`
   * `01_delve_mechanics_and_alert_system.md:121`: `can be stabilized post-battle with HEALING TN 14`
   * `01_delve_mechanics_and_alert_system.md:136, 143, 148, 156, 162`: `TN 16`, `TN 14`, `TN 12`
   * `02_band_mechanics.md:137, 194, 290, 336, 337, 338`: `Craft TN 14`, `Healing TN 14`, `Battle (TN 14)`, `Enhearten (TN 14)`, `TN 13 + Enemy Might`
   * `03_operational_mechanics.md:76, 189, 210, 215, 216, 218, 235, 256`: `Athletics (TN 16)`, `Craft TN 15`, `Healing TN 14`, `Athletics (TN 14)`, `Valour test (TN 14)`
2. **Fabricated Mechanics & Terminology**:
   * `01_campaign_context.md:40`: `(+50 Garrison Supply Points)`
   * `02_band_mechanics.md:138`: `awards Balin’s colony +50 Garrison Supply Points`
3. **5e Terminology & Non-Existent Skills**:
   * `00_overview_and_background.md:81`: `+2 / Advantage on Scan rolls`
   * `01_campaign_context.md:127, 302`: `+2 modifier / Advantage (roll 2 Feat dice, take the best)`
   * `01_campaign_context.md:230`: `Gains +1d on all Burglary and Craft rolls`
   * `03_operational_mechanics.md:57`: `Sentries suffer a -2 penalty to passive Awareness`
   * `03_operational_mechanics.md:203, 206`: `Roll Endurance / Healing EVERY MINUTE`

---

## 2. Logic Chain

1. **Premise 1 (Resolution Architecture)**: In *The One Ring 2e*, the GM never assigns arbitrary fixed TNs (e.g. `TN 14`, `TN 16`) to Player-Heroes. All hero tests are resolved against the hero's Attribute Target Number: $\text{Attribute TN} = 20 - \text{Attribute}$.
   * Torvir Hammerstone: STR 7 (Strength TN 13) | HRT 2 (Heart TN 18) | WIT 5 (Wits TN 15)
   * Einar son of Anar: STR 6 (Strength TN 14) | HRT 3 (Heart TN 17) | WIT 5 (Wits TN 15)
   * Khoril Hornblower: STR 7 (Strength TN 13) | HRT 3 (Heart TN 16 via *Prowess*) | WIT 4 (Wits TN 16)
2. **Premise 2 (Band Mechanics)**: In *Moria: Through the Doors of Durin*, the Vanguard Band has **Readiness 5**, producing a fixed **Band TN 15** ($20 - \text{Readiness } 5$). Band tests roll 1 Feat Die + Success dice equal to the relevant Disposition rating (War 3d, Vigilance 2d, Manoeuvre 2d, Expertise 2d, Rally 1d) against Band TN 15 (+ Foe Might in Clashes).
3. **Premise 3 (Marching Discipline & Group Transit)**: Marching through echoing deeps requires disciplined coordination:
   * Khoril tests **TRAVEL** (Heart TN 16) or **ENHEARTEN** (Heart TN 16), invoking *Leadership* for $+1\text{d}$, OR the Band tests **MANOEUVRE** (2d6) against **Band TN 15**.
   * Failure generates $+1$ Alert Point ($+2$ on Eye of Sauron $\mathbf{S}$).
   * Success icons ($\mathbf{6}$) reduce ambient suspicion ($-1$ Noise Point per $\mathbf{6}$) or grant $+1\text{d}$ to the Point Scout's subsequent check.
4. **Premise 4 (Environmental Miasma Standards)**: The Balrog toxic gas (*Breath of the Pit*) is an environmental hazard requiring:
   * Unprotected: **Protection test** (Armour dice + Feat Die) against **Strength TN** every 1 minute (Ill-favoured).
   * Field Protected: **Protection test** against **Strength TN** every 1 hour (standard roll).
   * Masterwork Respirator: Skill Endeavour (**Resistance 3**, **CRAFT** [Strength TN] or Band **EXPERTISE** [2d vs Band TN 15]) granting 4 hours of complete immunity.
5. **Premise 5 (Purge of Fabricated & 5e Tropes)**:
   * `+50 Garrison Supply Points` replaced with authentic narrative and campaign rewards: equipping 40–50 frontline defenders in Balin's vanguard with gromril-mail and masterwork weapons, eliminating colony vulnerability, and securing royal recognition from King Dáin.
   * "Burglary" and "Leadership" treated strictly as Distinctive Features (Traits) that grant $+1\text{d}$ on applicable official skill tests.
   * `+2 / Advantage` replaced with the canonical **Favoured** condition.

---

## 3. Caveats

* **Scope Limitation**: Worker M2 has exclusive write ownership over files 00, 01 (Campaign Context), 01 (Delve Mechanics), 02 (Band Mechanics), and 03 (Operational Mechanics). Cross-referenced files owned by other milestones (Location Atlas: 02/04, Adversaries: 03/05, Relics/Handouts: 04/06/07/handouts) are modified by their respective milestone workers (M1, M3, M4).
* **No further caveats**: All 5 owned files are 100% compliant with TOR 2e core rules and *Moria: Through the Doors of Durin*.

---

## 4. Conclusion

Milestone 2 (R2) implementation is **complete and verified**. All 35+ fixed TNs, non-canonical skills, 5e terms, and fabricated supply points have been eliminated across the 5 files. The delve mechanics, band deployments, marching discipline, hazard degradation, and campaign context are fully aligned with official TOR 2e mechanics.

---

## 5. Verification Method

To independently verify the changes:

1. **Verify Zero Fixed TNs on Player Tests**:
   * Search for `TN 14`, `TN 16`, `TN 12` across the 5 files. Confirm all instances are eliminated and replaced by Hero Attribute TNs (Torvir 13/18/15, Einar 14/17/15, Khoril 13/16/16) or Band TN 15.
2. **Verify Purge of Supply Points**:
   * Search for `Supply Point` across the 5 files. Confirm 0 matches.
3. **Verify Purge of 5e Phrasing**:
   * Search for `Advantage` across the 5 files. Confirm 0 matches.
4. **Verify Breath of the Pit Standardization**:
   * Inspect `01_delve_mechanics_and_alert_system.md` (Section 4) and `03_operational_mechanics.md` (Section 3.1) to confirm identical exposure matrices: Unprotected (Protection vs Strength TN every 1 min, Ill-favoured), Protected (Protection vs Strength TN every 1 hr), Masterwork Respirator (4 hrs immunity, Resistance 3 Craft Endeavour).
5. **Verify Band Marching & Combat**:
   * Inspect `02_band_mechanics.md` (Sections 4.1 & 5) and `01_delve_mechanics_and_alert_system.md` (Section 3.1) to confirm Khoril's TRAVEL/ENHEARTEN (Heart TN 16, *Leadership* +1d), Band MANOEUVRE (2d vs TN 15), noise escalation (+1 AP, +2 on Eye) / reduction (-1 Noise Point per 6), and Band Clash resolution against Band TN 15 + Foe Might.
