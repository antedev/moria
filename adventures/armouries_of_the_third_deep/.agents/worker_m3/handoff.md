# Milestone M3 Handoff Report

**Agent**: `worker_m3`  
**Working Directory**: `c:/Users/ante/Documents/github/Moria/adventures/armouries_of_the_third_deep/.agents/worker_m3`  
**Milestone**: M3 — Relics, Rewards, GM Playbook, Quickstart Appendices, Handouts  
**Date**: 2026-08-26  
**Status**: COMPLETE (Hard Handoff)  

---

## 1. Observation

A forensic audit of the 8 owned files assigned to Milestone M3 identified several systemic violations across Requirements R1, R2, R4, and R5 prior to refactoring:

1. **R1 (Player Agency & Prescriptive Scripting)**:
   - `06_relics_and_rewards.md`: Scripted Torvir Hammerstone as the sole wielder in Section 2.3; scripted Einar and Khoril in Grik negotiation offerings (Section 4.2); assigned Einar and Bróga as mandatory primary participants in the Lockbreaker Skill Endeavour (Section 4.3).
   - `07_gm_playbook_and_pacing.md`: Explicitly scripted Torvir, Einar, and Khoril into specific encounter steps in Sessions 1–3 (lines 100, 106, 119, 150–153, 160, 205, 213, 277, 281, 282, 358, 360, 372).
   - `quickstart/04_loot_relics_and_rewards.md`: Relic section headers were labeled with specific character assignments (e.g. `### 1. The Shield of the Deep Gate (Torvir or Einar)`).
   - `quickstart/05_gm_screen_and_play_aids.md`: Pacing playbook scripted specific character actions throughout Sessions 1–3.
   - `handouts/band_worksheet.md`: Section 4 (Band Clash Resolution Sheet Step 2) hardcoded specific PC leader actions (`• Khoril Hornblower: Command`, `• Torvir Hammerstone: Fight/Duel`, `• Einar son of Anar: Flank/Lockpick`).
   - `handouts/dying_scribe_letter.md`: Section 4 restricted runemaster insights to specific named characters (`When Einar son of Anar, Khoril Hornblower, or Hjoldring... examines the stone slab`).

2. **R2 (Hardcoded Pregen TN Listings)**:
   - `06_relics_and_rewards.md`: Embedded hardcoded TN listings in check text (`**RIDDLE** (**Wits TN: Torvir 15, Einar 15, Khoril 16**)`, `**SCAN** (**Wits TN: Torvir 15...**)`, `**CRAFT** (**Strength TN: Torvir 13...**)`).
   - `07_gm_playbook_and_pacing.md`: Multiple instances of `(Wits TN: Torvir 15, Einar 15, Khoril 16)`, `(Heart TN: Torvir 18, Einar 17, Khoril 16)`, `(Strength TN: Torvir 13, Einar 14, Khoril 13)`.
   - `quickstart/04_loot_relics_and_rewards.md`: D66 table entry 44 had `against their Heart TN (Torvir 18, Einar 17, Khoril 16)`.
   - `quickstart/05_gm_screen_and_play_aids.md`: Cheat sheet matrix and pacing playbook embedded `(Wits TN)`, `(Heart TN)`, `(Strength TN)` and pregen TN parentheticals.
   - `handouts/gm_cheat_sheet.md`: Room operational matrix and hazard matrix embedded `(Wits TN)`, `(Strength TN)`, `(Heart TN)`.
   - `handouts/node_map.md`: Cross-section included `TRAVEL [Heart TN: Torvir 18, Einar 17, Khoril 16]`.

3. **R4 (Canon TOR 2e Rules & Condition Audit)**:
   - `06_relics_and_rewards.md`: Line 92 contained non-canonical condition `clears the Faltering condition immediately`. Line 99 contained `Dread test against Heart TN`.
   - `quickstart/04_loot_relics_and_rewards.md`: Line 32 contained `clear the Faltering condition immediately`.
   - `handouts/band_worksheet.md`: Line 61–85 contained fatigue checkbox `[ ] Faltering`. Line 142 contained `clear Faltering`.

4. **R5 (Synchronization)**:
   - Discrepancies existed between `06_relics_and_rewards.md` and `quickstart/04_loot_relics_and_rewards.md`, and between `07_gm_playbook_and_pacing.md`, `quickstart/05_gm_screen_and_play_aids.md`, and the 4 handouts in terms of formatting and check descriptions.

---

## 2. Logic Chain

1. **Player Agency Restoration (R1)**:
   - In a tabletop roleplaying module, player-heroes make their own tactical decisions and role assignments. Prescribing which pre-generated hero performs an action robs players of agency and breaks utility when custom characters are used.
   - *Action*: All prescriptive phrasing was refactored into open choices and neutral role designations (e.g. "A champion...", "A scout...", "The Company's leader..."). Relic headers and Band Clash action options were generalized for any party configuration.

2. **Skill Check Notation & Pregen TN Purge (R2)**:
   - Official TOR 2e mechanics calculate Target Numbers dynamically as `20 - Attribute Rating` on the player's character sheet. Hardcoding specific pregen TN numbers into adventure text creates confusion, clutters readability, and invalidates custom characters.
   - *Action*: All obstacle check references were converted into standard TOR 2e notation: `**SKILL roll**` (e.g. `**SCAN roll**`, `**STEALTH roll**`, `**CRAFT roll (+1d)**`, `**VALOUR roll**`). All hardcoded parentheticals listing pregen TNs were purged from obstacle descriptions, while retaining the overview reference dashboards in cheat sheets as required by math verification tests.

3. **TOR 2e Canon Rules Alignment (R4)**:
   - TOR 2e rules define specific status conditions (*Weary*, *Miserable*, *Wounded*) and resolution mechanics for fear and dread (*Shadow Points [Dread]*, *Hope loss*, *Bout of Madness*). Homebrew conditions like "Daunted" or "Faltering" contradict core rules.
   - *Action*: "Faltering" was replaced with "Weary"; all fear and dread tests were aligned with standard `**VALOUR roll**` mechanics; all relic Enchanted Rewards (*Durin's Axe*, *Shield of the Deep Gate*, *Mattock of Moria-Silver*, *Mail of Unyielding Stone*, *Helm of the Iron Watch*, *Pike of the Under-Gate*) were validated against canonical qualities (*Rune-scored*, *Superior Grievous*, *Superior Keen*, *Reinforced*, *Close Fitting*, *Impenetrable*, *Vigilant Sentinel*, *Foe-Piercer*).

4. **Multi-Asset Synchronization (R5)**:
   - The module presents rules across full chapters, quickstart booklets, and handouts. Ensuring identical mechanical descriptions, item names, stats, and check notations guarantees effortless GM reference at the table.
   - *Action*: All 8 files were cross-checked and aligned so that quickstart entries, handouts, and full chapters match 100%.

---

## 3. Caveats

- **Character Overview Dashboards**: The reference tables in `handouts/gm_cheat_sheet.md` (lines 12–15), `handouts/band_worksheet.md` (lines 14–16), and `quickstart/05_gm_screen_and_play_aids.md` (lines 12–15) intentionally list the pregen attributes and calculated TNs (`Torvir: STR 7 (TN 13)...`) as an at-a-glance GM summary dashboard. This is explicitly exempted in `test_r2_pregen_tns.py` (line 268) and strictly asserted in `test_math_and_balance.py` (line 123). All action check blocks within the bodies of these documents have been completely purged of hardcoded TNs.
- **Master Assembly**: Master document re-compilation (`build_master_document.py`) should be run during final integration after all milestone workers complete their respective chapters.

---

## 4. Conclusion

All assigned files under Milestone M3 write ownership:
1. `06_relics_and_rewards.md`
2. `07_gm_playbook_and_pacing.md`
3. `quickstart/04_loot_relics_and_rewards.md`
4. `quickstart/05_gm_screen_and_play_aids.md`
5. `handouts/gm_cheat_sheet.md`
6. `handouts/band_worksheet.md`
7. `handouts/node_map.md`
8. `handouts/dying_scribe_letter.md`

have been fully remediated and validated. The files are 100% compliant with Requirements R1, R2, R4, and R5, with zero prescriptive PC scripting, zero hardcoded pregen TN parentheticals in check lines, zero non-canonical conditions, and full synchronization across the repository.

---

## 5. Verification Method

To independently verify all changes:

1. **Verify Absence of Prescriptive PC Scripting (R1)**:
   - Check `06_relics_and_rewards.md`, `07_gm_playbook_and_pacing.md`, `quickstart/04_loot_relics_and_rewards.md`, `handouts/node_map.md`, and `handouts/dying_scribe_letter.md` for occurrences of `Torvir`, `Einar`, or `Khoril`. Expect **0 matches**.
   - Inspect `handouts/band_worksheet.md` Step 2 (lines 140–147) to confirm generic hero leader actions (`Leader / Captain`, `Frontline Champion`, `Scout / Support`).

2. **Verify Absence of Hardcoded Pregen TNs in Check Lines (R2)**:
   - Search for `Wits TN:`, `Heart TN:`, `Strength TN:`, `(Torvir 15`, `Torvir 18`, `Einar 14` in check blocks across all 8 files. Expect **0 matches**.
   - Verify that all skill checks are formatted as `**SKILL roll**` (e.g. `**SCAN roll**`, `**STEALTH roll**`, `**CRAFT roll (+1d)**`, `**VALOUR roll**`).

3. **Verify TOR 2e Canon Rules & Conditions (R4)**:
   - Search for `daunted` or `faltering` across all 8 files. Expect **0 matches**.
   - Verify *Durin's Axe* qualities in `06_relics_and_rewards.md` and `quickstart/04_loot_relics_and_rewards.md` (*Rune-Scored*, *Superior Grievous*, *Superior Keen*, *Flame of Hope*, *Gleam of Terror*, +4 Eye Awareness).

4. **Verify Test Suite Integrity**:
   - `python -m unittest tests/test_r1_pc_scripting.py`
   - `python -m unittest tests/test_r2_pregen_tns.py`
   - `python -m unittest tests/test_r4_adversary_conditions.py`
   - `python -m unittest tests/test_math_and_balance.py`
   - `python -m unittest tests/test_r5_assembly_and_sync.py`
