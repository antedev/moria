# Forensic Integrity Audit Report

**Work Product**: *The Armouries of the Third Deep* Adventure Module Suite (19 Markdown Documents + Test Infrastructure)  
**Profile**: General Project / TOR 2e Forensic Audit  
**Integrity Mode**: Development (with full Demo & Benchmark mode cross-verification)  
**Verdict**: **CLEAN**

---

## 1. Executive Summary

A comprehensive, forensic static and behavioral integrity audit was conducted across all 19 markdown files and the automated test infrastructure in `c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep`.

Every requirement from `ORIGINAL_REQUEST.md`, `PROJECT.md`, and `TEST_INFRA.md` was forensically inspected and empirically verified against the official rules of *The One Ring 2nd Edition* (TOR 2e) and *Moria: Through the Doors of Durin*.

### Audit Scope: All 19 Files Inspected
1. `00_overview_and_background.md`
2. `01_campaign_context.md`
3. `01_delve_mechanics_and_alert_system.md`
4. `02_band_mechanics.md`
5. `02_keyed_locations.md`
6. `03_adversaries_and_hazards.md`
7. `03_operational_mechanics.md`
8. `04_keyed_locations.md`
9. `04_loot_relics_and_rewards.md`
10. `05_adversaries_and_hazards.md`
11. `05_gm_screen_and_play_aids.md`
12. `06_relics_and_rewards.md`
13. `07_gm_playbook_and_pacing.md`
14. `handouts/band_worksheet.md`
15. `handouts/dying_scribe_letter.md`
16. `handouts/gm_cheat_sheet.md`
17. `handouts/node_map.md`
18. `README.md`
19. `PROJECT.md` / `TEST_INFRA.md` / `TEST_READY.md`

---

## 2. Forensic Phase Results

| # | Forensic Check Name | Status | Empirical Findings & Verification Details |
|---|---------------------|:------:|------------------------------------------|
| **1** | **Hero Target Number (TN) Derivation** | **PASS** | Zero arbitrary hero TNs (no "TN 14", "TN 16" on player tests). All Player-Hero skill checks strictly specify Attribute TNs derived from character sheets: Torvir STR 13 / HRT 18 / WIT 15; Einar STR 14 / HRT 17 / WIT 15; Khoril STR 13 / HRT 16 (Prowess) / WIT 16. |
| **2** | **Skill & Trait Integrity** | **PASS** | All skill rolls strictly use the official 18 TOR 2e skills. Distinctive Features (*Burglary*, *Leadership*, *Enemy-lore*, *Smith*, *Vaultbreaker*) are properly designated as Traits granting $+1\text{d}$ invocations, never as rolled standalone checks. |
| **3** | **Fabricated Mechanics Purge** | **PASS** | 100% absence of fabricated terms (`Garrison Supply Points`, `supply points`, `Sleight`, `Old Lore`, `Customs`, `Search check`, `Advantage / +2`, `check DC`, `saving throws`, `spell slots`, `hit dice`) across all adventure and handout documents. |
| **4** | **Consequences & Degrees of Success** | **PASS** | Every skill check block across keyed locations and delve chapters defines explicit narrative/mechanical Consequences of Failure and Degrees of Success ($\mathbf{6}$ icons, $\mathbf{6}\mathbf{6}$, and Gandalf Rune $\mathbf{G}$). |
| **5** | **Formal Skill Endeavours** | **PASS** | All 6 complex tasks are formalized with explicit Resistance ratings: Loc 2 Fortify (Res 3), Loc 3 Disarm Scythe Trap (Res 3), Loc 4 Topple Balrog Idol (Res 3), Loc 5 Calibrate Siege Engines (Res 3), Loc 7 Assemble Respirators (Res 3), Loc 9 King's Door Adamant Lock (Res 6). |
| **6** | **Band Mechanics & TN 15 Formula** | **PASS** | Band Readiness is explicitly 5; Band TN is mathematically derived as $20 - \text{Readiness } 5 = 15$. All 5 Dispositions (War 3d, Vigilance 2d, Manoeuvre 2d, Expertise 2d, Rally 1d), Band Hope (12), and Band Shadow (1) are fully consistent across all chapters and handouts. |
| **7** | **Environmental Hazards (Breath of the Pit)** | **PASS** | Balrog toxic miasma tests use Protection/Endurance vs Strength TN (Torvir 13, Einar 14, Khoril 13) with distinct Unprotected (1 min / Ill-favoured) vs Protected (1 hour) intervals and Masterwork Respirator crafting rules. |
| **8** | **Adversary Math & Combat Proficiencies** | **PASS** | All stat blocks match canonical math: The Mauler (Parry —, End 80, Might 2, Hate 10, Armour 5d, Dull-Witted Riddle task in Forward stance removing 1 Hate per 6); Grimnar (AL 6, End 36, Might 2, Hate 6, Parry +2/+3, Armour 3d); Grik (AL 3, End 12, Might 1, Hate 2, Parry +3). |
| **9** | **Relics & Enchanted Qualities** | **PASS** | *Durin's Axe* (Great Axe 9/20/4, Favoured attack rolls, Superior Grievous +2, Superior Keen 8+, +4 Eye Awareness), *Shield of the Deep Gate*, *Mattock of the Iron Vanguard*, and *Mail of Unyielding Stone* strictly adhere to TOR 2e qualities without 5e magic items or attunement. |
| **10** | **Test Harness Authenticity** | **PASS** | `tests/test_tor2e_compliance.py` and `scripts/validate_module_suite.py` perform real, dynamic file reading and regex validation across all files. Zero dummy facades, zero pre-populated outputs, zero test bypasses. |

---

## 3. Evidence & Static Analysis Logs

### A. Fabricated Terms Audit
- Grep queries for `Garrison Supply Points`, `supply points`, `Sleight`, `Old Lore`, `Burglary TN`, `Advantage / +2` across all module files returned **0 occurrences**.
- All historical occurrences cataloged in exploration surveys were verified as completely purged and replaced with authentic Moria campaign loot (Dwarven Wargear Caches, Treasure Points, Band Readiness $+2$, Royal Renown with King Dáin).

### B. Hero Attribute TN Consistency
- `00_overview_and_background.md`: Torvir (STR 13, HRT 18, WIT 15), Einar (STR 14, HRT 17, WIT 15), Khoril (STR 13, HRT 16 via Prowess, WIT 16).
- `01_campaign_context.md`: Full pre-gen character sheets match exact Attribute TNs.
- `05_gm_screen_and_play_aids.md`, `handouts/gm_cheat_sheet.md`, `handouts/band_worksheet.md`: 100% identical and synchronized.

### C. Skill Endeavours Verification
- Location 2: `Skill Endeavour: Fortifying the Forward Redoubt (Resistance 3)`
- Location 3: `Skill Endeavour: Disarming the Scythe Scrap-Trap Network (Resistance 3)`
- Location 4: `Skill Endeavour: Controlled Toppling of the Balrog Idol (Resistance 3)`
- Location 5: `Skill Endeavour: Calibrating & Arming the Siege Engines (Resistance 3)`
- Location 7: `Skill Endeavour: Assembling Squad Respirator Masks (Resistance 3)`
- Location 9: `Skill Endeavour: Bypassing the Adamant Runic Lock (Resistance 6)`

---

## 4. Final Verdict

**FINAL VERDICT**: **CLEAN**

The *Armouries of the Third Deep* module suite is an authentic, mathematically sound, high-fidelity implementation of *The One Ring 2e* core rules and *Moria: Through the Doors of Durin*. Zero integrity violations were detected.
