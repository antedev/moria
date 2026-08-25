# Handoff Report — Survey of Adversaries, Hazards, Relics, GM Aids & Handouts (R3 & R4)

**Agent ID**: `teamwork_preview_explorer_survey_3`  
**Working Directory**: `c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep/.agents/teamwork_preview_explorer_survey_3`  
**Milestone**: Survey 3 (Adversaries, Hazards, Relics, GM Aids & Handouts Audit for R3 & R4)  
**Date**: 2026-08-25  

---

## 1. Observation

Direct examination of the 9 assigned files revealed the following exact text, line numbers, and mechanical violations:

1. **Adversary Stat Block Math & Fell Ability Violations**:
   - `03_adversaries_and_hazards.md` (lines 37–39): Strike Fear states: `"Spend 1 Hate to force all Player-heroes to make a VALOUR test (TN 14)."`
   - `05_adversaries_and_hazards.md` (line 95): The Mauler's Parry is listed as: `"PARRY: 5 (— / Unarmoured baseline 0; +5 from massive scrap plating and bulk)"`. In standard TOR 2e, trolls have Parry `—`, and scrap plating is modeled solely via Armour (5d). Giving +5 Parry raises hero attack TN from 13 to 18.
   - `05_adversaries_and_hazards.md` (line 110): Strike Fear states: `"pass a Valour test (TN 14)"`. Line 114: Scavenged Iron Carapace states: `"unless the hero passes a Craft or Athletics test (TN 14)"`.
   - `05_adversaries_and_hazards.md` (line 152): The Riddle Duel specifies: `"Standard Riddle test against TN 14 (or Wits TN 15)"`.
   - `03_adversaries_and_hazards.md` (lines 50–55) vs `05_adversaries_and_hazards.md` (lines 206–211):
     - In `03`: Grimnar Endurance is **36**, Might is **2**, Parry is **+2**.
     - In `05`: Grimnar Endurance is **32**, Might is **1 (or Might 2 in Apex Ambush)**, Parry is **6 (+3 Base + 3 from dual-wielding stolen Dwarven dagger and speed)**.
   - `03_adversaries_and_hazards.md` (lines 79–84) vs `05_adversaries_and_hazards.md` (lines 309–315):
     - In `03`: Grik is AL 3, Endurance 12, Hate 2, Parry +3. Line 92: `"requires SCAN TN 16 to detect"`.
     - In `05`: Grik is AL 2 (or AL 3), Endurance 8 (or 12), Parry 4 (+1 Base + 3). Line 322: `"pass a Valour test (TN 14)"`. Lines 339–347: Social table has Persuade TN 14, Enhearten TN 14, Riddle TN 14.
   - `03_adversaries_and_hazards.md` (lines 105–126) vs `05_adversaries_and_hazards.md` (lines 378–457):
     - In `03`: Orc Soldiers are AL 4, End 18; Orc Guards are AL 5, End 24; Udûn Sniffers have Parry +1, Armour 2d.
     - In `05`: Quick Matrix lists Orc Soldiers AL 3, End 12; Orc Guards AL 4, End 16; Udûn Sniffers Parry —, Armour 3d.

2. **Environmental Hazards Fixed TNs**:
   - `03_adversaries_and_hazards.md` (lines 134–138): Hazard matrix lists: `"ENDURANCE TN 14"`, `"ATHLETICS TN 14"`, `"SCAN TN 12"`, `"SCAN TN 14"`, `"CRAFT TN 12"`, `"VALOUR TN 14"`, `"LORE TN 12"`, `"STEALTH TN 16"`.
   - `05_adversaries_and_hazards.md` (lines 527–600): Miasma, tremors, and pitfalls list: `"Craft TN 14 / TN 15"`, `"Athletics TN 16 or Craft TN 16"`, `"Scan (TN 14)"`, `"Athletics (TN 14)"`, `"Athletics (TN 16)"`, `"Valour (TN 14)"`.

3. **Relics, Relic Profiles & Fabricated Mechanics**:
   - `04_loot_relics_and_rewards.md` (line 32): Gleam of Terror lists: `"make a Valour test (TN 16) or flee"`. Line 88: Lockpicks give `"+1d to Craft/Burglary"`. Line 107: `"Healing test (TN 12)"`.
   - `06_relics_and_rewards.md` (lines 30, 299, 341): Lists `"+50 GARRISON SUPPLY POINTS FOR BALIN"`.
   - `06_relics_and_rewards.md` (lines 265, 274): Skill Endeavour lists `"Burglary"` as an eligible skill with `"Burglary (TN 15)"`, alongside `"Scan (TN 14)"`, `"Craft (TN 15)"`, `"Riddle (TN 16)"`.
   - `06_relics_and_rewards.md` (line 79): Rune-scored specifies `"+1 to Feat die rolls on attacks"`.

4. **GM Aids & Handouts**:
   - `05_gm_screen_and_play_aids.md` (lines 17–26, 74–123): All 10 area summaries and session notes assign fixed TN 14s.
   - `07_gm_playbook_and_pacing.md` (lines 32, 227, 377): Lists `"+50 Garrison Supply Points"`. Lines 99–160 list `"Guide (TN 14)"`, `"Burglary TN 14"`, `"Old Lore TN 14"`, `"Extended Skill Endeavour (Einar + The Broken Key vs TN 16)"`. Line 257 lists `"Burglary Mastery"`.
   - `handouts/gm_cheat_sheet.md` (lines 14–52): Every single area row assigns fixed TN 14/15/16. Lacks a dedicated Hero Attribute TN reference block.
   - `handouts/band_worksheet.md` (lines 138–140): Step 2 Leader Actions state: `"Khoril: Command (Battle TN 14 -> +1d to Clash) | Inspire (Enhearten TN 14 -> +1 Hope)"`, `"Einar: Flank / Lockpick (Burglary / Scan TN 14)"`. Lacks Hero Attribute TNs (Torvir: STR 13/HRT 18/WIT 15; Einar: STR 14/HRT 17/WIT 15; Khoril: STR 13/HRT 16/WIT 16).
   - `handouts/dying_scribe_letter.md` (lines 128–138): Translation table lists `"Lore / Scan (TN 12)"`, `"Craft / Healing (TN 14)"`, `"Riddle / Old Khuzdul (TN 14)"`.

---

## 2. Logic Chain

1. **Premise**: In *The One Ring 2e*, all Player-Hero tests resolve against character Attribute Target Numbers ($20 - \text{Attribute}$), never against arbitrary GM-assigned fixed TNs.
2. **Inference from Hero Profiles** (`01_campaign_context.md` lines 50–165):
   - Torvir: STR 7 (TN 13), HRT 2 (TN 18), WIT 5 (TN 15).
   - Einar: STR 6 (TN 14), HRT 3 (TN 17), WIT 5 (TN 15).
   - Khoril: STR 7 (TN 13), HRT 3 (TN 16 via *Prowess* [Heart]), WIT 4 (TN 16).
   - Band Readiness is 5 $\rightarrow$ Band TN is $20 - 5 = \mathbf{15}$.
3. **Inference for Adversary Stat Blocks**:
   - The Mauler's Parry in `05` (+5) violates TOR 2e troll design (trolls have no parry bonus; armor is Protection dice). Troll Parry must be `—`.
   - Grimnar's stats in `03` (AL 6, End 36, Might 2, Parry +2, Hate 6) follow official Great Orc Chief math ($6 \times 6 = 36$ End), while `05`'s stats (End 32, Parry +6) are internally broken and contradictory.
   - The Mauler's "Dull-Witted" Riddle combat task requires a **RIDDLE** test (**Wits TN**) in Forward stance, removing 1 Hate base $+ 1$ Hate per Success icon ($\mathbf{6}$).
   - Strike Fear forces a **VALOUR** test against the hero's **Heart TN**, not TN 14.
4. **Inference for Relics & Rewards**:
   - Durin's Axe must use standard TOR 2e Qualities: Great Axe (Two-handed, 9/20/4), *Rune-Scored* (Favoured attacks), *Superior Grievous* (+2 Dmg), *Superior Keen* (Pierce on 8–10), *Flame of Hope* (30 ft light, +1d on Hope spend), *Gleam of Terror* (Favoured Awe on *Intimidate Foe*), and *The Weight of Doom* (+4 Eye Awareness).
   - "+50 Garrison Supply Points" is a fabricated system that violates the core rules and must be replaced with narrative and canonical rewards.
   - "Burglary" is not one of the 18 official TOR 2e skills; it is a Distinctive Feature (Trait) that grants $+1\text{d}$ on applicable skill tests (Scan, Stealth, Craft).
5. **Inference for Handouts**:
   - `handouts/gm_cheat_sheet.md` and `handouts/band_worksheet.md` must display the heroes' actual Attribute TNs and Band TN 15, and all room/action matrices must use the official Skill (Attribute TN) format.

---

## 3. Caveats

- **Scope Boundary**: This survey was strictly read-only and covered the 9 assigned adversary, hazard, relic, GM aid, and handout files. Location files (`02_keyed_locations.md`, `04_keyed_locations.md`) and Delve/Band files (`01_delve_mechanics_and_alert_system.md`, `02_band_mechanics.md`, `03_operational_mechanics.md`) were audited by peer survey agents.
- **Assumption on Great Orc Math**: Grimnar's profile is unified as an AL 6 Great Orc Chieftain with Endurance 36, Might 2, Hate 6, Parry +2, Armour 3d. If the orchestrator wishes to treat him as a lesser stalker, AL 5 / End 24 would be canonical, but AL 6 / End 36 best matches his narrative status as an Archfoe.

---

## 4. Conclusion

The module files for Adversaries, Hazards, Relics, GM Aids, and Handouts require targeted refactoring to eliminate fixed TNs, resolve stat contradictions, purge fabricated supply points, fix trait usage, and ensure 100% adherence to *The One Ring 2e* core rules.

Complete, granular recommendations and refactoring blueprints have been authored in:
`c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep/.agents/teamwork_preview_explorer_survey_3/survey_report.md`

---

## 5. Verification Method

To independently verify these survey findings:
1. **Grep Search for Fixed TNs**:
   - Run a grep search for `TN 14`, `TN 12`, `TN 15`, `TN 16` across `03_adversaries_and_hazards.md`, `05_adversaries_and_hazards.md`, `04_loot_relics_and_rewards.md`, `06_relics_and_rewards.md`, `05_gm_screen_and_play_aids.md`, `07_gm_playbook_and_pacing.md`, and `handouts/`.
2. **Grep Search for Fabricated Mechanics & Trait Errors**:
   - Run a grep search for `Supply Points` and `Burglary TN` across all markdown files.
3. **Inspect Key Stat Blocks**:
   - `view_file` on `03_adversaries_and_hazards.md` (lines 18–41, 50–70) and `05_adversaries_and_hazards.md` (lines 91–116, 206–233) to verify stat differences.
4. **Invalidation Condition**:
   - If any Player-Hero check still contains an arbitrary fixed TN or if an adversary stat contradicts official TOR 2e formulas, the refactoring implementation for R3/R4 must be revised.
