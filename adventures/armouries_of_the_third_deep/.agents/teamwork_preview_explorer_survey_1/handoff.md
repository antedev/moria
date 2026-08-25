# Handoff Report: Location Atlas Survey & TOR 2e Alignment
**Agent**: `teamwork_preview_explorer_survey_1`  
**Milestone**: Milestone 1 (R1) — Location Atlas System Audit & Refactoring  
**Working Directory**: `c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep/.agents/teamwork_preview_explorer_survey_1`  
**Target Files Surveyed**:
- `c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep/02_keyed_locations.md`
- `c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep/04_keyed_locations.md`
- `c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep/handouts/node_map.md`
- Referenced: `handouts/gm_cheat_sheet.md`, `handouts/band_worksheet.md`, `00_overview_and_background.md`

---

## 1. Observation

Direct observations from inspecting the codebase:

1. **Fixed Hero Target Numbers**:
   - `02_keyed_locations.md:82`: `"Stealth Infiltration (STEALTH TN 14)"`
   - `02_keyed_locations.md:83`: `"Ambush Assault (BATTLE TN 14)"`
   - `02_keyed_locations.md:84`: `"Scan the Pavilion (SCAN TN 14 / Einar with Broken Key rolls with +2)"`
   - `02_keyed_locations.md:99`: `"Fortify the Gatehouse (CRAFT TN 14)"`
   - `02_keyed_locations.md:100`: `"Spot Overhead Slag-Worm (AWARENESS TN 14)"`
   - `02_keyed_locations.md:115`: `"Detect Traps (SCAN TN 14 / Einar with Broken Key rolls with +2)"` and `"test ATHLETICS (TN 14)"`
   - `02_keyed_locations.md:127`: `"All heroes must make a VALOUR Test (TN 14)"`
   - `02_keyed_locations.md:133`: `"Decipher the Desecrated Murals (LORE TN 14)"`
   - `02_keyed_locations.md:148`: `"Repair a Dwarf Ballista (CRAFT TN 14 / Hjoldring assists)"`
   - `02_keyed_locations.md:161`: `"walking across a floor strewn with loose iron rings and metal scrap (STEALTH TN 16)"`
   - `02_keyed_locations.md:165`: `"FORWARD STANCE / RIDDLE TN 14"`
   - `02_keyed_locations.md:166`: `"spotted via SCAN TN 12"`
   - `02_keyed_locations.md:176`: `"test once per hour (TN 14)"`
   - `02_keyed_locations.md:177`: `"VALOUR TN 12"`
   - `02_keyed_locations.md:208`: `"Extended CRAFT Endeavour: Resistance 6, TN 16"`
   - `02_keyed_locations.md:211`: `"VALOUR TN 14 test"`
   - `04_keyed_locations.md:182-202`: Multiple `TN 14` tests (Scan, Stealth, Old Lore, Persuade, Battle)
   - `04_keyed_locations.md:257-261`: `Craft (TN 14)`, `Craft (TN 16) / Battle (TN 14)`, `Explore (TN 14)`
   - `04_keyed_locations.md:334-340`: `Scan (TN 14)`, `Burglary (TN 14)`, `Healing (TN 14)`, `Craft (TN 14)`
   - `04_keyed_locations.md:403-428`: `Valour TN 14 / Awe TN 14`, `Old Lore TN 14 / Riddle TN 14`, `Athletics (TN 14)`, `Enhearten / Song (TN 14)`, `Craft TN 14`
   - `04_keyed_locations.md:485-506`: `Athletics (TN 14)`, `Craft (TN 14)`, `Battle (TN 14)`, `Burglary TN 14`
   - `04_keyed_locations.md:557-572`: `Athletics (TN 14)`, `Hunting (TN 14)`, `Riddle (TN 14)`, `Stealth (TN 16)`
   - `04_keyed_locations.md:635-650`: `Endurance / Healing (TN 14)`, `Craft (TN 15)`, `Athletics (TN 12)`, `Athletics (TN 16)`, `Scan (TN 14)`
   - `04_keyed_locations.md:716-731`: `Craft (TN 14) or Burglary (TN 14)`, `Scan TN 12`, `Explore / Battle (TN 14)`, `Burglary (TN 14)`
   - `04_keyed_locations.md:795-805`: `Burglary / Craft Endeavour (requires 3 Successes vs TN 16)`, `Awareness (TN 14)`, `Riddle / Old Lore (TN 14)`, `Burglary (TN 16)`
   - `04_keyed_locations.md:879-883`: `Awe / Song (TN 14)`, `Valour TN 14`, `Craft / Old Lore (TN 14)`
   - `handouts/node_map.md:16, 96, 98, 99, 100, 298, 301, 304, 307`: `Hunt 16`, `Explore TN 14`, `Scan TN 14`, `Athletics 14`, `Burglary 14`, `Scan TN 12`, `Customs / Persuade TN 14`
   - `handouts/gm_cheat_sheet.md:12-54`: Summary matrix contains 20+ fixed TNs.

2. **Non-Existent Skills & Trait Conflation**:
   - `02_keyed_locations.md:134`: `"STEALTH / SLEIGHT TN 14"` (Sleight is fabricated).
   - `04_keyed_locations.md:278, 336, 506, 716, 726, 795, 805`: `"Burglary TN 14"`, `"Burglary TN 16"`, `"Burglary (TN 16 / Extended Endeavour)"` (Burglary is an official Trait, not a skill).
   - `04_keyed_locations.md:186, 405, 414, 649, 804, 883`: `"Old Lore TN 14"` (Old Lore is not in TOR 2e; official skill is `Lore`).
   - `handouts/node_map.md:307`: `"Customs / Persuade TN 14"` (Customs is legacy 1e).
   - `04_keyed_locations.md:913, 915, 919`: `"Dread 14"`, `"Catwalks 14"`, `"Greed 14"` used as skill entries.

3. **Flat Modifiers**:
   - `02_keyed_locations.md:84, 115`: `"Einar with Broken Key rolls with +2"`
   - `04_keyed_locations.md:122, 183, 335, 650, 726, 795`: `"+2 modifier / Advantage"`
   - `04_keyed_locations.md:123`: `"Grants +1 to all Battle rolls"`

4. **Fabricated Mechanics**:
   - `04_keyed_locations.md:120, 688, 714, 740`: `"+50 Garrison Supply Points for Balin!"`
   - `handouts/node_map.md:350`: `"+50 Garrison Supply Points"`

5. **Missing Failure Prices & Degrees of Success**:
   - Nearly all skill check descriptions lack the explicit Consequences of Failure (Endurance loss, Weary, Shadow, Noise points) and Degree of Success ($\mathbf{6}$ and $\mathbf{6}\mathbf{6}$ icons).

---

## 2. Logic Chain

1. **Premise 1 (TOR 2e Core Rules on TNs)**: In *The One Ring 2e*, the GM never sets fixed Target Numbers for Player-Heroes. All tests are resolved against the hero's Attribute TN derived from the formula $\text{TN} = 20 - \text{Attribute}$.
2. **Inference from Observation 1**: All 45+ fixed TN instances (`TN 12`, `TN 14`, `TN 15`, `TN 16`) violate core TOR 2e mechanics and must be replaced by referencing the hero's Strength TN ($20-\text{STR}$), Heart TN ($20-\text{HRT}$), or Wits TN ($20-\text{WIT}$).
3. **Premise 2 (Official Skills vs Traits)**: TOR 2e defines exactly 18 skills (Awe, Athletics, Awareness, Hunting, Song, Craft, Enhearten, Travel, Insight, Healing, Courtesy, Battle, Persuade, Stealth, Scan, Explore, Riddle, Lore). Distinctive Features (e.g. *Burglary*, *Enemy-lore*, *Leadership*, *Wary*) are Traits that can be invoked to grant $+1\text{d}$ or automatic actions.
4. **Inference from Observation 2**:
   - `Burglary` tests must be converted to **CRAFT**, **STEALTH**, or **SCAN** tests, specifying that heroes with the *Burglary* Trait (e.g. Einar) or *Vaultbreaker* gift (Bróga) gain $+1\text{d}$.
   - `Sleight` must be converted to **STEALTH** or **CRAFT**.
   - `Old Lore` must be converted to **LORE** (Wits).
   - `Customs` must be converted to **COURTESY**, **PERSUADE**, or **RIDDLE**.
   - `Dread` / `Greed` / `Catwalks` in tables must be converted to **AWE**, **ENHEARTEN**, **VALOUR**, and **ATHLETICS**.
5. **Premise 3 (Modifiers in TOR 2e)**: TOR 2e strictly uses **Favoured / Ill-favoured** (rolling two Feat dice and keeping higher/lower) or dice pool modifiers ($\pm 1\text{d} / \pm 2\text{d}$). Flat numerical bonuses do not exist.
6. **Inference from Observation 3**: All "+2" and "+1" flat modifiers must be refactored into **Favoured** or $+1\text{d}$.
7. **Premise 4 (Skill Endeavours & Task Structure)**: Multi-step complex tasks require formal **Skill Endeavours** with explicit Resistance ratings ($3, 6$) and structured failure costs.
8. **Inference from Observations 1 & 5**: The six complex operations across Locations 2, 3, 4, 5, 7, and 9 must be converted into formal Skill Endeavours.

---

## 3. Caveats

- **Scope Boundary**: This survey strictly evaluated the Location Atlas files (`02_keyed_locations.md`, `04_keyed_locations.md`, `handouts/node_map.md`) and their corresponding matrices in `handouts/gm_cheat_sheet.md`. Detailed stat block math for adversaries (e.g. The Mauler, Grimnar) in `03_adversaries_and_hazards.md` and `05_adversaries_and_hazards.md` falls under Milestone 3 (R3) and was referenced only for environmental integration.
- **Scribe Name Consistency**: Scribe *Náli son of Náin* (`04:639`) vs *Frár* (`node_map:53`) must be reconciled with `handouts/dying_scribe_letter.md` during implementation.
- No other caveats.

---

## 4. Conclusion

The Location Atlas across `02_keyed_locations.md`, `04_keyed_locations.md`, and `handouts/node_map.md` is rich in atmospheric narrative and tactical design, but requires systematic mechanical refactoring for 100% TOR 2e compliance.

The comprehensive master survey report has been generated at:
`c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep/.agents/teamwork_preview_explorer_survey_1/survey_report.md`

All 10 keyed locations, 45+ fixed TNs, non-compliant skills, flat modifiers, and 6 formal Skill Endeavours have been fully analyzed, mapped, and provided with exact line-by-line refactoring templates. Milestone 1 (R1) is fully specified and ready for implementation.

---

## 5. Verification Method

To independently verify the survey findings:

1. **Verify Fixed TNs**:
   - Inspect `02_keyed_locations.md` and `04_keyed_locations.md` using pattern search for `TN 12`, `TN 14`, `TN 15`, `TN 16`.
2. **Verify Non-Existent Skills**:
   - Inspect occurrences of `Burglary TN`, `Old Lore`, `SLEIGHT`, `Customs` in `02_keyed_locations.md`, `04_keyed_locations.md`, and `handouts/node_map.md`.
3. **Verify Pre-gen Attribute TNs**:
   - Cross-check with `ORIGINAL_REQUEST.md:14-16` and `handouts/band_worksheet.md`:
     - Torvir: STR TN 13, HRT TN 18, WIT TN 15
     - Einar: STR TN 14, HRT TN 17, WIT TN 15
     - Khoril: STR TN 13, HRT TN 16, WIT TN 16
     - Band TN: 15 (Readiness 5)
4. **Inspect Master Survey Report**:
   - View `c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep/.agents/teamwork_preview_explorer_survey_1/survey_report.md`.
