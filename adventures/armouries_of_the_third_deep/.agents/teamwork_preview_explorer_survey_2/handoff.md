# Handoff Report: Delve, Band, Operational Systems & Campaign Context Survey
**Agent**: `teamwork_preview_explorer_survey_2`  
**Recipient**: `teamwork_preview_orchestrator_1` (Parent Agent)  
**Date**: 2026-08-25  
**Handoff Type**: Hard (Task Complete)

---

## 1. Observation

Direct line-by-line inspection of the five assigned files revealed the following exact observations:

1. **`01_delve_mechanics_and_alert_system.md`**:
   - Line 23: `Stealth rolls are standard difficulty (TN 14).` (Fixed TN).
   - Line 97: `March Test: Khoril rolls TRAVEL or LEADERSHIP (TN 14).` (Fixed TN; "Leadership" listed as a rolled skill).
   - Line 121: `stabilized post-battle with HEALING TN 14` (Fixed TN).
   - Line 136: `Must roll Protection / Endurance every 1 Minute (TN 16).` (Fixed TN; non-existent "Endurance roll").
   - Line 143: `Test Endurance only once per 1 Hour (TN 14).` (Fixed TN).
   - Line 148: `Endeavour: Resistance 4, TN 14` (Fixed TN on Skill Endeavour).
   - Line 156: `Everyone in the zone must test ATHLETICS (TN 14).` (Fixed TN).
   - Line 162: `passive SCAN (TN 12)` (Fixed passive TN).

2. **`02_band_mechanics.md`**:
   - Line 85–86: `Rolls Vigilance (2d) vs TN 15` (Band test is correct), but `The Broken Key (+2 / Advantage on Scan)` (5e phrasing).
   - Line 137: `padded with cloth (Craft TN 14)` (Fixed TN).
   - Line 138: `awards Balin’s colony +50 Garrison Supply Points` (Fabricated mechanic).
   - Line 194: `Requires First Aid (Healing TN 14)` (Fixed TN).
   - Line 290: `Khoril can roll Battle (TN 14) or Enhearten (TN 14)` (Fixed TN).
   - Line 336–338: `Command (Khoril): Khoril rolls Battle (TN 14)`; `Inspire: Enhearten (TN 14)`; `Fight: personal Combat Proficiency against TN 13 + Enemy Might` (Fixed TNs and non-standard combat resolution).

3. **`03_operational_mechanics.md`**:
   - Line 57: `Sentries suffer a -2 penalty to passive Awareness` (5e mechanic).
   - Line 76: `Athletics (TN 16) test` (Fixed TN).
   - Lines 189, 210, 215: `Craft TN 15 respirators` / `Craft TN 15` (Fixed TN).
   - Lines 203, 206: `Roll Endurance / Healing EVERY MINUTE` (Non-existent skill roll).
   - Line 216: `Herbal Treatments (Healing TN 14)` (Fixed TN).
   - Line 218: `Craft TN 16 or Athletics TN 16` (Fixed TN).
   - Line 235: `Athletics (TN 14) test` (Fixed TN).
   - Line 256: `Valour test (TN 14)` (Fixed TN).

4. **`00_overview_and_background.md`**:
   - Line 81: `The Broken Key (+2 / Advantage on Scan rolls)` (5e phrasing).
   - Line 82: `Expedition Guide (TN 14), Leadership` (Fixed TN).
   - Line 82: `Battle Horn of the Realm (+1 Battle)` (Flat skill modifier).

5. **`01_campaign_context.md`**:
   - Line 40: `(+50 Garrison Supply Points)` (Fabricated mechanic).
   - Line 127: `+2 modifier / Advantage (roll 2 Feat dice, take the best) on all Scan rolls` (5e phrasing).
   - Line 128: `Wind-proof Lantern (+2 to Scan in darkness)` (Flat numeric bonus).
   - Line 138: `Journey Role: Guide (TN 14)` (Fixed TN).
   - Line 164: `+1 to all Battle rolls` (Flat numeric bonus).
   - Line 165: `+1 to Enhearten rolls` (Flat numeric bonus).
   - Line 230: `Gains +1d on all Burglary and Craft rolls` ("Burglary" treated as a skill).
   - Line 302: `+2 modifier / Advantage on all Scan and Burglary rolls` (5e phrasing and "Burglary rolls").
   - Line 308: `+1 to all Battle rolls` (Flat numeric bonus).

---

## 2. Logic Chain

1. *Premise 1*: Under *The One Ring 2e* rules, Player-Hero tests never use GM-assigned arbitrary Target Numbers (such as TN 14 or TN 16). All Target Numbers are derived directly from the hero's character sheet ($\text{Attribute TN} = 20 - \text{Attribute}$).
2. *Premise 2*: Torvir (STR 7, HRT 2, WIT 5 $\implies$ STR 13 / HRT 18 / WIT 15), Einar (STR 6, HRT 3, WIT 5 $\implies$ STR 14 / HRT 17 / WIT 15), and Khoril (STR 7, HRT 3 with Prowess, WIT 4 $\implies$ STR 13 / HRT 16 / WIT 16) have explicit, immutable Attribute TNs.
3. *Premise 3*: In *Moria: Through the Doors of Durin*, Band tests use $\text{Band TN} = 20 - \text{Readiness}$. With Band Readiness 5, the Band TN is 15. Band rolls roll 1 Feat Die + Success Dice equal to the Disposition rating (War 3, Vigilance 2, Manoeuvre 2, Expertise 2, Rally 1).
4. *Premise 4*: In TOR 2e, there are only 18 official skills. *Burglary* and *Leadership* are Distinctive Features (Traits), not skills. They grant $+1\text{d}$ or Inspiration when applied to official skills (**STEALTH**, **SCAN**, **CRAFT**, **ENHEARTEN**, **TRAVEL**, **BATTLE**).
5. *Premise 5*: D&D 5e mechanics (such as "+2 / Advantage", "passive Awareness", flat skill bonuses) and fabricated video-game trackers ("garrison supply points") violate TOR 2e system purity.
6. *Inference*: Therefore, every fixed hero TN must be replaced by referencing the hero's Attribute TN, multi-step tasks must be structured as Skill Endeavours (Resistance ratings), all trait/skill distinctions must be strictly enforced, and fabricated mechanics must be eliminated.

---

## 3. Caveats

- **Scope Boundary**: This survey strictly audited `01_delve_mechanics_and_alert_system.md`, `02_band_mechanics.md`, `03_operational_mechanics.md`, `00_overview_and_background.md`, and `01_campaign_context.md`. Keyed locations (`02_keyed_locations.md`, `04_keyed_locations.md`), adversaries (`03_adversaries_and_hazards.md`, `05_adversaries_and_hazards.md`), relics (`04_loot_relics_and_rewards.md`, `06_relics_and_rewards.md`), and GM guides/handouts (`07_gm_playbook_and_pacing.md`, `handouts/`) are being surveyed in parallel by peer agents (`explorer_survey_1` and `explorer_survey_3`).
- **Assumptions**: Band Readiness is established at 5 (TN 15) and Khoril's Prowess virtue permanently modifies his Heart TN to 16.

---

## 4. Conclusion

The core architecture of the Delve, Band, and Operational subsystems is rich and highly functional, but contains 35 identifiable rules violations across fixed TNs, non-existent skills, 5e terminology, and fabricated supply points. All 35 instances have been cataloged with precise line-level replacement text in `survey_report.md`. The module is fully primed for immediate, seamless execution in Milestone 2 (R2).

---

## 5. Verification Method

To independently verify these findings:
1. Inspect the survey report at:
   `c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep/.agents/teamwork_preview_explorer_survey_2/survey_report.md`
2. Perform pattern searches in the surveyed files:
   - Fixed TNs: `grep_search` for `TN 14`, `TN 16`, `TN 12`, `TN 15` in `00_overview_and_background.md`, `01_campaign_context.md`, `01_delve_mechanics_and_alert_system.md`, `02_band_mechanics.md`, `03_operational_mechanics.md`.
   - "Burglary" / "Supply Points": `grep_search` for `Burglary` and `Supply Points`.
3. Invalidation condition: If any player-hero check in the surveyed files is found to be validly assigned a fixed TN under official TOR 2e core rules, this conclusion is partially invalidated. (Under official rules, player tests never have fixed TNs).
