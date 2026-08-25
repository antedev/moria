# Milestone 4 / R4 Handoff Report: Relics, Rewards, GM Play Aids & Handouts Overhaul
**Worker**: `teamwork_preview_worker_m4_1`  
**Date**: 2026-08-25  
**Working Directory**: `c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep/.agents/teamwork_preview_worker_m4_1`

---

## 1. Observation

Direct investigation of the 8 assigned project files revealed specific, systematic violations of *The One Ring 2e* (TOR 2e) rules and *Moria: Through the Doors of Durin*:

1. **Relics & Loot Tables (`04_loot_relics_and_rewards.md` & `06_relics_and_rewards.md`)**:
   - `04_loot_relics_and_rewards.md:20` listed `LOAD: 3` for Great Axe (standard TOR 2e Great Axe load is 4).
   - `04_loot_relics_and_rewards.md:31` and `06_relics_and_rewards.md:97` assigned an arbitrary fixed `Valour test (TN 16)` to Durin's Axe's *Gleam of Terror*.
   - `06_relics_and_rewards.md:79` contained the non-standard phrase `"+1 to Feat die rolls on attacks"` rather than official TOR 2e **Favoured** status.
   - `06_relics_and_rewards.md:30, 299, 341` listed `"+50 GARRISON SUPPLY POINTS FOR BALIN"`.
   - `06_relics_and_rewards.md:265, 274` formatted "Burglary" as a standalone skill roll with fixed TNs (`Burglary (TN 15)`, `Scan (TN 14)`, `Craft (TN 15)`, `Riddle (TN 16)`).
   - `04_loot_relics_and_rewards.md:107` contained `Healing test (TN 12)` in Scavenge Item 44.
   - `06_relics_and_rewards.md:315, 404, 431, 455` contained non-standard modifiers: `Advantage on all Explore rolls`, `Grants +2 on Scan rolls`, `+1 to Intimidate Foe`, `+1 to subsequent Battle`.

2. **GM Screen & Session Playbook (`05_gm_screen_and_play_aids.md` & `07_gm_playbook_and_pacing.md`)**:
   - `05_gm_screen_and_play_aids.md:17–26` contained fixed TNs for all 10 areas (`STEALTH TN 14`, `CRAFT TN 14`, `SCAN TN 14`, `VALOUR TN 14`, `RIDDLE TN 14`, `ENDURANCE TN 14`, `CRAFT TN 16`).
   - `05_gm_screen_and_play_aids.md:29–34` contained contradictory adversary statistics (The Mauler Parry 5 instead of `—`, Grimnar Endurance 32 instead of 36, Grik AL 2/3 and End 8/12 instead of AL 3 / End 12).
   - `07_gm_playbook_and_pacing.md:32, 227, 377` contained `"+50 Garrison Supply Points"`.
   - `07_gm_playbook_and_pacing.md:99–204` contained fixed TNs: `Guide (TN 14)`, `Scan (+2 from The Broken Key)`, `Craft TN 14`, `Craft TN 16 / Battle TN 14`, `Burglary TN 14`, `Valour TN 14`, `Old Lore TN 14`, `Craft TN 15`, `Extended Skill Endeavour (... vs TN 16)`.
   - `07_gm_playbook_and_pacing.md:250–263` used non-canonical terminology: `Burglary Mastery`, `The Broken Key (+2 / Adv)`, `Squad Guide (TN 14)`.

3. **Handouts Suite (`handouts/gm_cheat_sheet.md`, `band_worksheet.md`, `dying_scribe_letter.md`, `README.md`)**:
   - `handouts/gm_cheat_sheet.md` lacked a dedicated Hero Attribute TN reference block; listed fixed TNs across all 10 area summary rows.
   - `handouts/band_worksheet.md:15, 116` referenced `"+50 Supply"`, and lines 138–140 listed fixed TN 14s for hero actions (`Battle TN 14`, `Enhearten TN 14`, `Burglary / Scan TN 14`).
   - `handouts/dying_scribe_letter.md:128–140` contained fixed TNs: `Lore / Scan (TN 12)`, `Craft / Healing (TN 14)`, `Riddle / Old Khuzdul (TN 14)`, `Craft TN 15 mask`.
   - `README.md` listed an incomplete directory table and lacked explicit Hero Attribute TN references.

---

## 2. Logic Chain

1. **Step 1 (TOR 2e Resolution Compliance)**: In TOR 2e, GMs do not assign arbitrary Target Numbers to Player-Heroes. Every hero roll is resolved against an Attribute TN derived as $20 - \text{Attribute Rating}$ (Torvir: STR 13/HRT 18/WIT 15; Einar: STR 14/HRT 17/WIT 15; Khoril: STR 13/HRT 16/WIT 16). Band rolls are resolved against **Band TN 15** ($20 - \text{Readiness 5}$). Therefore, every fixed TN prompt across all 8 files had to be refactored into the official format: `**SKILL** (<Attribute> TN)` or `Band **<DISPOSITION>** against **Band TN 15**`.
2. **Step 2 (Skill & Trait Purity)**: The One Ring 2e defines exactly 18 official skills. Terms like "Burglary", "Leadership", "Smith", and "Vaultbreaker" are Distinctive Features (Traits) that grant $+1\text{d}$ to official skills (**STEALTH**, **SCAN**, **CRAFT**, **BATTLE**), while "Old Lore", "Sleight", and "Customs" do not exist. All instances treating traits as standalone skills were converted into proper Trait invocations.
3. **Step 3 (Relics & Enchanted Qualities)**: Relics in TOR 2e use defined Enchanted Qualities (*Rune-Scored*, *Superior Grievous*, *Superior Keen*, *Reinforced*, *Cunning Make*, *Close Fitting*) and Cultural Virtues (*Flame of Hope*, *Gleam of Terror*, *Unyielding*, *Gleaming Edge*, *Impenetrable*, *Vigilant Sentinel*, *Foe-Piercer*). *Durin's Axe* and the 5 Tunnel-Guard Relics + Dagger were rewritten to strictly use these mechanics and official Eye Awareness escalation (+4 on claiming the Axe).
4. **Step 4 (Purge of Fabricated Mechanics)**: `+50 Garrison Supply Points` was a video-game scorekeeping placeholder. It was purged and replaced with canonical campaign rewards: equipping 50 frontline Dwarves with gromril-mail and masterwork weapons, securing the Upper Mansions against Orc counter-attacks, providing royal proof for King Dáin Ironfoot in Erebor to dispatch 500 veteran reinforcements in 2990 TA, and awarding $+4$ Adventure Points, $+3$ Skill Points, and $+2$ Fellowship Score.
5. **Step 5 (Tabletop Handouts Alignment)**: Handouts and GM play aids must provide immediate, accurate numbers for table facilitation. Dedicated Hero Attribute TN matrices and Band TN 15 blocks were embedded in `handouts/gm_cheat_sheet.md`, `handouts/band_worksheet.md`, `05_gm_screen_and_play_aids.md`, and `README.md`.

---

## 3. Caveats

No caveats. All 8 assigned files have been completely refactored, verified, and reconciled against the rest of the adventure module suite.

---

## 4. Conclusion

Milestone 4 (R4) is 100% complete across all 8 owned files:
- `04_loot_relics_and_rewards.md`
- `06_relics_and_rewards.md`
- `05_gm_screen_and_play_aids.md`
- `07_gm_playbook_and_pacing.md`
- `handouts/gm_cheat_sheet.md`
- `handouts/band_worksheet.md`
- `handouts/dying_scribe_letter.md`
- `README.md`

Every relic, loot table, GM aid, pacing guide, and player handout is mathematically sound, strictly adherent to TOR 2e core rules, and ready for immediate table use.

---

## 5. Verification Method

To independently verify the refactored files:

1. **Zero Fixed Hero TNs**:
   - Inspect `04_loot_relics_and_rewards.md`, `06_relics_and_rewards.md`, `05_gm_screen_and_play_aids.md`, `07_gm_playbook_and_pacing.md`, and all `handouts/`.
   - Confirm all player tests reference `Strength TN`, `Heart TN`, or `Wits TN` (or explicit hero values 13/18/15, 14/17/15, 13/16/16).
2. **Zero Fabricated Supply Points**:
   - Search for `supply point` across all 8 files $\implies$ 0 occurrences.
3. **Trait & Skill Integrity**:
   - Confirm *Burglary* is only invoked as a Trait granting $+1\text{d}$ to Craft, Scan, or Stealth.
   - Confirm *Leadership* is only invoked as a Trait.
   - Confirm zero occurrences of non-canonical skills (*Sleight*, *Old Lore*, *Customs*).
4. **Relic & Adversary Math**:
   - Confirm *Durin's Axe* has Damage 9, Injury 20, Load 4, *Rune-Scored* (Favoured), *Superior Grievous* (+2), *Superior Keen* (Pierce 8–10 / $\mathbf{G}$), *Flame of Hope*, *Gleam of Terror*, +4 Eye Awareness.
   - Confirm *The Mauler* has Parry `—`, End 80, Might 2; *Grimnar* has End 36, Might 2, Parry +2; *Grik* has AL 3, End 12, Parry +3.
5. **Skill Endeavour**:
   - Confirm the Lockbreaker Skill Endeavour in `06_relics_and_rewards.md` §4.3 has Resistance 6, Time Limit 3 Turns, and valid Attribute TN checks.
