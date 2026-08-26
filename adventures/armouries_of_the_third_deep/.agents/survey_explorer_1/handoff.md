# Handoff Report: survey_explorer_1

**Handoff Type**: Hard (Task Complete)  
**Agent**: `survey_explorer_1`  
**Working Directory**: `c:/Users/ante/Documents/github/Moria/adventures/armouries_of_the_third_deep/.agents/survey_explorer_1`  
**Date**: 2026-08-26  
**Parent Orchestrator ID**: `4520ebd2-4ae5-45e8-aaf7-6750f3bc27b8`

---

## 1. Observation

Direct textual observations and verbatim extractions from the adventure suite:

### A. R1: Player Agency Violations
- `02_band_mechanics.md:291`: `Leader Check: Khoril rolls TRAVEL (Heart TN 16) or ENHEARTEN (Heart TN 16), invoking his Leadership Trait for +1d.`
- `02_band_mechanics.md:343–346`: `Command (Khoril): Khoril rolls BATTLE...`, `Inspire (Torvir or Khoril)...`, `Fight (Torvir or Einar)...`, `Duel (Torvir): Torvir engages the enemy Champion...`
- `04_keyed_locations.md:215`: `Marching Discipline (Khoril's Leadership): Khoril rolls TRAVEL or ENHEARTEN (Heart TN: 16) invoking Leadership Trait (+1d)...`
- `04_keyed_locations.md:473–474`: `Torvir's Curse of Vengeance: On failure, Torvir flies into uncontrollable rage and must spend his next action attacking the idol with his Great Axe...`, `Einar's Dragon-sickness: On failure, Einar becomes obsessed with prying molten gold-leaf from the idol, wasting 10 minutes.`
- `04_keyed_locations.md:991`: `Duel Combat Task (Torvir): Torvir challenges Grimnar in single combat in Forward stance...`
- `05_adversaries_and_hazards.md:261–267`: Grimnar's ambush explicitly script-targets Khoril ("the horn-bearer") and Einar ("the locksmith") and reacts to Torvir's advance.
- `06_relics_and_rewards.md:257–258`: `PARTICIPANTS: Primary: Einar (Treasure Hunter) & Bróga (Vaultbreaker), Support: Torvir (Anchor/Brace), Khoril (Lookout/Acoustic Dampener)`

### B. R2: Hardcoded Pre-gen Target Numbers
- `02_band_mechanics.md:137`: `CRAFT — Strength TN: Torvir 13, Einar 14, Khoril 13`
- `03_operational_mechanics.md:76`: `ATHLETICS test (Strength TN: Torvir 13, Einar 14, Khoril 13, Ill-favoured or at -1d)`
- `03_operational_mechanics.md:225`: `CRAFT (Strength TN: Torvir 13, Einar 14, Khoril 13)`
- `04_keyed_locations.md:142, 184, 190, 196, 202, 207, 225, 283, 290, 295, 300, 332, 372, 377, 385, 391, 395, 399, 466, 470, 478, 483, 490, 496, 569, 572, 578, 584, 589, 593, 660, 662, 665, 669, 675, 681, 687, 691, 757, 761, 765, 772, 778, 783, 787, 791, 795, 864, 866, 875, 881, 886, 965, 974, 981, 987, 1064, 1068, 1073`: Over 60 skill test entries specifying `(Wits TN: Torvir 15, Einar 15, Khoril 16)`, `(Strength TN: Torvir 13, Einar 14, Khoril 13)`, or `(Heart TN: Torvir 18, Einar 17, Khoril 16)`.
- `05_adversaries_and_hazards.md:105, 114, 119, 157, 188, 193, 303, 408–409, 416–417, 467, 473–475, 491, 495, 503–504, 521–531, 556–563`: Repeated pre-gen formula listings.
- `06_relics_and_rewards.md:241, 242, 270, 275, 278` and `07_gm_playbook_and_pacing.md:87, 100, 106, 113, 115, 119, 150, 156, 160, 165, 205, 262, 267, 272, 367`.

### C. R3: Boxed Read-Aloud Text Quality & Spoilers
- `04_keyed_locations.md:360` (Location 3: The First Armoury):
  `Över den centrala gången löper tunna, spända senor mellan järnstolpar, riggade till motvägda lieklingor som dryper av ett vidrigt, glänsande svart gift.`
  *(Directly reveals the concealed sinew tripwires, scythe trap, and black poison before any check is made!)*
- `04_keyed_locations.md:746` (Location 7: The Poisoned Halls):
  `...hans stenhänder är alltjämt knutna kring en förseglad cylinder av tungt bly.`
  *(Spots the lead scroll tube across the toxic gas-filled room before players explore).*
- `04_keyed_locations.md:851` (Location 8: The Upper Armoury):
  `...som bröt upp den yttre porten för århundraden sedan, bara för att genast kvävas till döds av den giftiga ångan.`
  *(Narrative lore exposition rather than immediate sensory description).*

### D. R4: Non-Canonical Rules & "Daunted" Condition
- `04_keyed_locations.md:472`: `The character gains 2 Shadow Points (Dread) and suffers the Daunted condition (cannot spend Hope points) for 1 hour.`
- `04_keyed_locations.md:477`: `...clearing the Daunted condition from all companions.`
- `04_keyed_locations.md:486`: `...removes Daunted from all heroes, and restores +1 Band Hope.`
- `04_keyed_locations.md:1065`: `...suffers the Daunted condition for 1 hour.`
- `05_adversaries_and_hazards.md:115`: `...suffer 2 Shadow (Dread) and become Daunted (cannot spend Hope for the rest of the battle).`

---

## 2. Logic Chain

1. **Premise 1 (TOR 2e Resolution & Pregen Independence)**: In *The One Ring 2e*, player character Target Numbers are calculated on character sheets ($20 - \text{Attribute}$). An adventure module must be runnable with any custom Fellowship or pre-generated company.
   - *Observation*: Chapters 2, 3, 4, 5, 6, and 7 hardcode `Torvir 15, Einar 15, Khoril 16` into dozens of obstacle entries.
   - *Inference*: Hardcoding these numbers breaks standard TOR 2e convention and invalidates use with any other party composition. All must be replaced with standard skill check prompts (e.g. `**SCAN roll**`).

2. **Premise 2 (Player Agency & Neutral Presentation)**: An adventure module should present the environment, hazards, and choices neutrally to the GM so that the players choose who performs which action and how they approach problems.
   - *Observation*: Multiple chapters mandate which pre-gen acts (e.g., Khoril commands, Torvir duels, Einar lockpicks, Torvir flies into rage, Einar loots gold).
   - *Inference*: These prescriptive directives violate player agency and must be reframed as neutral GM situational prompts and open tactical options.

3. **Premise 3 (Integrity of Read-Aloud Text)**: Boxed read-aloud descriptions must only convey immediate sensory impressions (sight, sound, smell, scale) visible upon entry without spoiling hidden hazards or secret doors.
   - *Observation*: Location 3's read-aloud text explicitly reveals the concealed sinew tripwires, scythe blades, and poison vats. Location 7 reveals the lead tube across an opaque gas-filled room.
   - *Inference*: These boxed texts spoil player discovery and nullify mechanical checks (**SCAN** / Scout Screen). They must be rewritten to describe only immediate visible features.

4. **Premise 4 (Core Rules Canonical Compliance)**: TOR 2e defines specific conditions (**Weary**, **Miserable**, **Wounded**) and resolved effects for fear/dread (Shadow gains, Hope loss, Bout of Madness triggers).
   - *Observation*: "Daunted" appears 5 times across `04_keyed_locations.md` and `05_adversaries_and_hazards.md` as an invented status effect blocking Hope expenditure.
   - *Inference*: "Daunted" is non-canonical and must be purged across all files, replaced with official TOR 2e mechanics.

---

## 3. Caveats

1. **Swedish Boxed Text**: All 10 boxed read-aloud sections in `04_keyed_locations.md` are currently written in Swedish while the surrounding module is in English. While Swedish provides strong atmospheric prose, the team should decide whether to maintain Swedish or translate to English during refactoring; however, regardless of language, the spoiler content must be stripped.
2. **Quickstart & Handouts Sync**: This survey focused primarily on the 7 core modular chapters (`01` through `07`), though quickstart files and handouts were checked for cross-references. Full file-by-file text editing will need to ensure quickstart files and handouts are synchronized in downstream tasks.

---

## 4. Conclusion

The audit identifies four specific, well-defined refactoring requirements:
1. **R1**: Reframe all prescriptive PC references across Chapters 2–7 into neutral company choices.
2. **R2**: Strip all hardcoded pre-gen TNs (`Torvir X, Einar Y, Khoril Z`) from all skill check blocks, replacing them with standard TOR 2e skill roll notations.
3. **R3**: Rewrite the boxed read-aloud descriptions for Location 3, Location 7, and Location 8 to eliminate spoilers and historical exposition.
4. **R4**: Purge all 5 occurrences of the non-canonical "Daunted" condition in `04_keyed_locations.md` and `05_adversaries_and_hazards.md`, aligning fear and poison rules strictly with TOR 2e core mechanics.

All detailed findings, line numbers, and snippets have been recorded in `analysis.md`.

---

## 5. Verification Method

To verify these findings independently:
1. **Search for Hardcoded Pre-gen TNs**:
   - Grep query: `grep_search` with Query `Torvir 15` or `Torvir 13` across `01_campaign_context.md` through `07_gm_playbook_and_pacing.md`.
2. **Search for "Daunted" Condition**:
   - Grep query: `grep_search` with Query `Daunted` across the entire workspace directory. Confirm occurrences in `04_keyed_locations.md` (lines 472, 477, 486, 1065) and `05_adversaries_and_hazards.md` (line 115).
3. **Inspect Read-Aloud Spoilers**:
   - `view_file` on `04_keyed_locations.md` around lines 360–361 (Location 3), 746–747 (Location 7), and 851–852 (Location 8).
