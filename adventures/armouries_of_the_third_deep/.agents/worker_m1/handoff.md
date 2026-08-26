# Milestone M1 Handoff Report: Keyed Locations Refactoring & Alignment

**Agent**: `worker_m1` (implementer, qa, specialist)  
**Milestone**: M1 (Keyed Locations Refactoring & Alignment)  
**Date**: 2026-08-26  
**Owned Files Modified**:
- `c:/Users/ante/Documents/github/Moria/adventures/armouries_of_the_third_deep/04_keyed_locations.md`
- `c:/Users/ante/Documents/github/Moria/adventures/armouries_of_the_third_deep/quickstart/02_keyed_locations.md`

---

## 1. Observation

1. **Hardcoded Pre-gen TNs**:
   - In `04_keyed_locations.md`, over 60 occurrences of hardcoded pregen Target Numbers existed (e.g. lines 142, 184, 190, 196, 202, 207, 215, 225, 283, 290, 295, 300, 332, 372, 377, 385, 391, 395, 399, 466, 470, 478, 483, 490, 496, etc.), formatted as `(Wits TN: Torvir 15, Einar 15, Khoril 16)`, `(Strength TN: Torvir 13, Einar 14, Khoril 13)`, `(Heart TN: Torvir 18, Einar 17, Khoril 16)`.
   - In `quickstart/02_keyed_locations.md`, over 40 occurrences of identical pregen TN formulas existed across lines 82–464.
2. **Player Agency Violations**:
   - Prescriptive character scripting was pervasive: e.g. `04_keyed_locations.md:215` (*"Marching Discipline (Khoril's Leadership): Khoril rolls TRAVEL..."*), `04_keyed_locations.md:473` (*"Torvir's Curse of Vengeance: On failure, Torvir flies into uncontrollable rage and must spend his next action attacking the idol with his Great Axe..."*), `04_keyed_locations.md:474` (*"Einar's Dragon-sickness: On failure, Einar becomes obsessed..."*), `04_keyed_locations.md:991` (*"Duel Combat Task (Torvir): Torvir challenges Grimnar..."*).
   - In `quickstart/02_keyed_locations.md:98`, the text prescribed: *"Torvir and the Dwarf vanguard cut down 2 sentries immediately..."* and in lines 455–459 scripted Einar's exact psychological reactions to gold.
3. **Boxed Read-Aloud Text Spoilers & Purple Prose**:
   - `04_keyed_locations.md:360` explicitly described hidden scythe traps and venom (*"...riggade till motvägda lieklingor som dryper av ett vidrigt, glänsande svart gift"*).
   - `04_keyed_locations.md:649` directly revealed the sleeping troll and its armor carapace in the read-aloud box (*"...ligger ett monstruöst Grottroll... inkapslat i ett ogenomträngligt järnpansar"*).
   - `04_keyed_locations.md:746` pointed out the lead scroll tube clutched by the scribe in the far corner of a room shrouded in dense toxic gas.
   - `04_keyed_locations.md:946` gave away the exact two-key puzzle mechanism and metals in the boxed description.
4. **Non-Canonical "Daunted" Condition**:
   - In `04_keyed_locations.md`, "Daunted" appeared at lines 472, 477, 486, 1065.
   - In `quickstart/02_keyed_locations.md`, "Daunted" appeared at lines 210, 215, 224, 452.
   - It was defined as an invented status effect where heroes *"cannot spend Hope points for 1 hour"*.

---

## 2. Logic Chain

1. **From Observation 1**: In TOR 2e core rules, Player-Hero Target Numbers are calculated strictly from character-sheet attributes ($20 - \text{Attribute}$) and must never be hardcoded into adventure obstacle descriptions. By removing all `(Attribute TN: Torvir X...)` strings and replacing them with canonical `**SKILL roll**` notation (while preserving Band TN 15 and trap Injury TNs), the module is brought into 100% compliance with TOR 2e resolution architecture.
2. **From Observation 2**: Dictating PC actions strips player agency and converts interactive tabletop roleplaying into scripted cutscenes. By replacing hero-specific prompts with open company choices, trait invocation rules (+1d), and generalized flaw triggers, the GM is provided with neutral environmental presentation tools, restoring full player agency.
3. **From Observation 3**: Read-aloud text must only convey immediate sensory impressions upon entering a space (sight, sound, smell, temperature, scale). Revealing concealed traps, ambushers, sleeping monsters, and puzzle keys before skill checks ruins exploration tension. Removing these spoilers moves secret details strictly into GM reference notes.
4. **From Observation 4**: "Daunted" is an invented, non-canonical status. In official TOR 2e, dread and supernatural malice are resolved through Shadow Points (Dread/Greed), the **Miserable** condition, the **Weary** condition, and Hope loss/restoration. Replacing all 8 occurrences in the keyed location files restores mechanical canon.

---

## 3. Caveats

- **Scope Boundary**: Worker M1 has exclusive write ownership of `04_keyed_locations.md` and `quickstart/02_keyed_locations.md`. Upstream chapter files (`01`–`03`, `05`–`07`), other quickstart files, handouts, and scripts are owned by parallel workers (M2, M3, M4) and were not modified by this worker.
- **Bilingual Presentation**: `04_keyed_locations.md` provides atmospheric boxed text in English matching the master document language, while `quickstart/02_keyed_locations.md` provides atmospheric boxed text in Swedish (*Högläsningstext*), with both versions strictly stripped of all spoilers.

---

## 4. Conclusion

- Milestone M1 tasks (R1, R2, R3, R4) for `04_keyed_locations.md` and `quickstart/02_keyed_locations.md` are 100% complete.
- Zero occurrences of hardcoded pregen TN listings remain.
- Zero occurrences of prescriptive pregen names or scripted actions remain.
- Zero occurrences of the non-canonical "Daunted" condition remain.
- All 10 boxed read-aloud text descriptions are concise, atmospheric, and free of spoilers.
- All 6 Skill Endeavour blocks across Locations 2, 3, 4, 5, 7, and 9 maintain exact canonical Resistance ratings and allowed skills.

---

## 5. Verification Method

To independently verify the modifications made by Worker M1:

1. **Verify Absence of "Daunted" Condition**:
   ```bash
   grep -rn "Daunted" 04_keyed_locations.md quickstart/02_keyed_locations.md
   ```
   *Expected result*: 0 matches.

2. **Verify Absence of Hardcoded Pre-gen TNs**:
   ```bash
   grep -rn "Torvir 1" 04_keyed_locations.md quickstart/02_keyed_locations.md
   grep -rn "Einar 1" 04_keyed_locations.md quickstart/02_keyed_locations.md
   grep -rn "Khoril 1" 04_keyed_locations.md quickstart/02_keyed_locations.md
   ```
   *Expected result*: 0 matches.

3. **Verify Absence of Prescriptive Pregen Names in Skill Test Blocks**:
   ```bash
   grep -rn "Torvir" 04_keyed_locations.md quickstart/02_keyed_locations.md
   grep -rn "Einar" 04_keyed_locations.md quickstart/02_keyed_locations.md
   grep -rn "Khoril" 04_keyed_locations.md quickstart/02_keyed_locations.md
   ```
   *Expected result*: 0 matches.

4. **Verify Skill Endeavours**:
   - Location 2: Fortifying the Forward Redoubt (Resistance 3)
   - Location 3: Disarming the Scythe Scrap-Trap Network (Resistance 3)
   - Location 4: Controlled Toppling of the Balrog Idol (Resistance 3)
   - Location 5: Calibrating & Arming the Siege Engines (Resistance 3)
   - Location 7: Assembling Squad Respirator Masks (Resistance 3)
   - Location 9: Bypassing the Adamant Runic Lock (Resistance 6)
