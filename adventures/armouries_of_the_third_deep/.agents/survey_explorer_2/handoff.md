# Handoff Report: Quickstart & Handouts Audit (R1–R5)
**Agent**: `survey_explorer_2`  
**Date**: 2026-08-26  
**Status**: Complete (Hard Handoff)  
**Target File**: `analysis.md`

---

## 1. Observation

Direct observations and evidence collected across all files in `quickstart/` and `handouts/`:

### R1: Player Agency Violations
* `quickstart/02_keyed_locations.md:211`:
  > `*Torvir's Curse of Vengeance*: On failure, Torvir flies into uncontrollable rage and must spend his next turn attacking the idol (**+2 Noise Points**, gains 2 Fatigue).`
* `quickstart/02_keyed_locations.md:212`:
  > `*Einar's Dragon-sickness*: On failure, Einar becomes obsessed with prying molten gold-leaf from the idol, wasting 10 minutes.`
* `quickstart/02_keyed_locations.md:424`:
  > `The Blood of Durin Inscription Ritual — AWE (Strength TN: Torvir 13, Khoril 13) or ENHEARTEN (Heart TN: Torvir 18, Khoril 16): Context: Torvir or Khoril (of Durin's royal line) slicing their palm...`
* `quickstart/02_keyed_locations.md:455`:
  > `Resisting Dragon-Sickness & Greed — Shadow Test (Heart TN: Einar 17 or Wits TN: Einar 15): Modifiers: Einar's Dragon-sickness Flaw makes this test Ill-favoured... On failure: Einar gains 2 Shadow (Greed) and becomes compelled to stuff every golden goblet...`
* `handouts/band_worksheet.md:141-146`:
  > `• Khoril Hornblower : [ ] Command (BATTLE [Heart TN 16] -> +1d to Clash)`  
  > `• Torvir Hammerstone : [ ] Fight (Great Axe vs STRENGTH TN 13 + Adversary Parry/Might)`  
  > `• Einar son of Anar : [ ] Fight (Sword vs STRENGTH TN 14 + Adversary Parry/Might)`

### R2: Hardcoded Pregen TN Listings
* `quickstart/01_delve_mechanics_and_alert_system.md:23`:
  > `• Stealth tests are resolved against Hero Wits TN (Torvir 15, Einar 15, Khoril 16).`
* `quickstart/02_keyed_locations.md:82`:
  > `* **Perimeter Infiltration — STEALTH (Wits TN: Torvir 15, Einar 15, Khoril 16)**:`
* `quickstart/02_keyed_locations.md:94`:
  > `* **Ambush Assault — BATTLE (Heart TN: Torvir 18, Einar 17, Khoril 16)**:`
* `quickstart/02_keyed_locations.md:132`:
  > `*Allowed Skills*: **CRAFT** (Strength TN: Torvir 13, Einar 14, Khoril 13), **ATHLETICS** (Strength TN: Torvir 13, Einar 14, Khoril 13), **BATTLE** (Heart TN: Torvir 18, Einar 17, Khoril 16).`
* `quickstart/03_adversaries_and_hazards.md:32`:
  > `action to attempt a RIDDLE test (Wits TN: Torvir 15, Einar 15, Khoril 16)`
* `quickstart/04_loot_relics_and_rewards.md:144`:
  > `against their Heart TN (Torvir 18, Einar 17, Khoril 16).`
* `quickstart/05_gm_screen_and_play_aids.md:123`:
  > `Call for Dread tests (VALOUR vs Heart TN: Torvir 18, Einar 17, Khoril 16).`
* `handouts/node_map.md:16`:
  > `▼ (Wild Land Travel — TRAVEL [Heart TN: Torvir 18, Einar 17, Khoril 16])`

### R3: Boxed Read-Aloud Text Quality & Spoilers
* `quickstart/02_keyed_locations.md:284` (Location 6):
  > `...sover Slaktaren – ett Grottroll av skräckinjagande mått, med hela kroppen inkapslad i ett absurt pansar av järnplåtar, ringbrynjedelar och dvärgsköldar bultade rakt in i dess hud.`
* `quickstart/02_keyed_locations.md:401` (Location 9):
  > `...I mitten av porten finns två distinkta nyckelhål: ett smitt av skimrande mithril-legering (Kungens nyckelhål), det andra format av mörkt meteoritjärn (Fältherrens nyckelhål).`
* Read-aloud text across all 10 locations in `quickstart/02_keyed_locations.md` is in Swedish (*Högläsningstext*).

### R4: Non-Canonical Conditions & Rules
* `quickstart/02_keyed_locations.md:210`:
  > `*Consequence of Failure*: Hero gains **2 Shadow Points (Dread)** and becomes **Daunted** (cannot spend Hope points for 1 hour).`
* `quickstart/02_keyed_locations.md:215`:
  > `**66**: Resolute defiance; inspires the Company, clearing the Daunted condition from all companions.`
* `quickstart/02_keyed_locations.md:224`:
  > `**6**: Singing *The Song of Durin* cleanses the oppressive aura, removes Daunted from all heroes, and restores **+1 Band Hope**.`
* `quickstart/02_keyed_locations.md:452`:
  > `*Consequence of Failure*: Overwhelmed by sorrow and reverent weeping; suffers the Daunted condition for 1 hour.`
* `quickstart/03_adversaries_and_hazards.md:44`:
  > `Those who fail gain 2 Shadow (Dread) and are Daunted (cannot spend Hope for the rest of the battle).`

### R5: Synchronization Gaps
* `scripts/build_master_document.py` stitches chapters `01`–`07` and handouts, but excludes `quickstart/` (which exists as a parallel standalone delve).
* `handouts/dying_scribe_letter.md:142` cross-references `(see Chapter 6 §4.3)`.

---

## 2. Logic Chain

1. **Step 1 (Agency)**: The One Ring 2e rules emphasize company freedom of action. The presence of hardcoded character directives (e.g. `quickstart/02_keyed_locations.md:211`, `quickstart/05_gm_screen_and_play_aids.md:103`, `handouts/band_worksheet.md:141-146`) removes player decision-making, converting an open-ended tabletop scenario into a scripted cutscene.
2. **Step 2 (TN Resolution)**: In TOR 2e, Target Numbers are determined solely by the character sheet ($20 - \text{Attribute}$); embedding strings like `(Wits TN: Torvir 15, Einar 15, Khoril 16)` in over 50 places breaks game flow for non-pregen parties and contradicts core rules formatting.
3. **Step 3 (Read-Aloud Integrity)**: Boxed read-aloud descriptions are intended for table recitation upon entering a room. Directly naming the sleeping troll in Location 6 or detailing the exact keyholes in Location 9 gives away tactical solutions and hidden threats before any player skill roll or inspection.
4. **Step 4 (Condition Canon)**: TOR 2e has four primary status conditions: *Weary*, *Miserable*, *Wounded*, and temporary states (*Poisoned*, *Frightened*). The term "Daunted" is an invented homebrew condition that prevents spending Hope, which is not part of the official ruleset and must be replaced by Shadow (Dread), Miserable, or Hope loss.
5. **Step 5 (Synchronization)**: If the quickstart documents and handouts diverge in rules, TN notation, or terminology from the main chapters `01` through `07`, GMs running from quickstart or printing handouts will encounter conflicting mechanics.

---

## 3. Caveats

* **No Source Code Edits Made**: In accordance with the Explorer / Auditor read-only mandate, no edits were made directly to `quickstart/`, `handouts/`, or `scripts/`.
* **Bilingual Formatting**: The main chapters feature English text with Swedish read-aloud boxes. If the project intends to maintain Swedish read-aloud boxes, they must be pruned of spoilers; if English read-aloud text is preferred for international tables, full translations should be provided.

---

## 4. Conclusion

The quickstart files and handouts contain substantial non-canonical rules ("Daunted"), over 50 instances of hardcoded pregen TN listings, multiple player agency violations, and boxed read-aloud text spoilers. A comprehensive refactoring is required across all 6 quickstart markdown files and 4 handout files to align them 100% with TOR 2e core rules and the master chapters.

---

## 5. Verification Method

To independently verify these findings, perform the following searches:
1. **Search for "Daunted"**:
   ```bash
   grep -rn "Daunted" quickstart/ handouts/
   ```
   *Expected matches*: `quickstart/02_keyed_locations.md` (lines 210, 215, 224, 452) and `quickstart/03_adversaries_and_hazards.md` (line 44).
2. **Search for Pregen TN Listings**:
   ```bash
   grep -rn "Torvir 15" quickstart/ handouts/
   ```
   *Expected matches*: Over 40 occurrences across `quickstart/01`, `quickstart/02`, `quickstart/03`, `quickstart/05`, and `handouts/node_map.md`.
3. **Inspect Read-Aloud Spoilers**:
   View `quickstart/02_keyed_locations.md` at line 284 (Location 6) and line 401 (Location 9).
4. **Invalidation Conditions**:
   If a search for `Daunted` or `Torvir 15` in `quickstart/` yields zero results, the audit findings are no longer applicable.
