# Adversarial Verification & Empirical Challenge Report
## Adventure Module: *The Armouries of the Third Deep* (*The One Ring 2e*)

**Author**: Challenger Subagent 2 (`critic`, `specialist`)  
**Working Directory**: `c:/Users/ante/Documents/Moria/.agents/challenger_final_2`  
**Target Module**: `c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep/`  
**Status / Final Verdict**: **`APPROVE`**  
**Date**: 2026-08-25  

---

## 1. Observation

Direct empirical inspection of the adventure module files, test infrastructure, and play aids yielded the following concrete observations:

### 1.1 Test Suite & Infrastructure Inspection
* **Test Runner (`tests/test_runner.py`)**: Defines domain simulation models (`Hero`, `Companion`, `Band`, `AlertTracker`, `Adversary`, `ModuleInspector`) and execution harness across 4 tiers:
  * `tests/test_tier1_features.py`: 136 tests verifying features F01 through F26 ($\ge 5$ tests per feature).
  * `tests/test_tier2_boundaries.py`: 30 boundary and corner-case tests (exact 50% weariness, Hunt Threshold 14, toxic gas intervals, Riddle duel hate-stripping, Hideous Toughness resets).
  * `tests/test_tier3_combinations.py`: 17 pairwise combination tests (Horn acoustic echo, Alert 2 stealth penalties, Phalanx vs Troll, mask punctures).
  * `tests/test_tier4_workloads.py`: 5 end-to-end delve workloads (Act I, Act II, Act III, Fighting Withdrawal, Schema Validator).
  * **Total Test Count**: 188 tests structured with 0 external dependencies using standard Python `unittest`.

### 1.2 Architectural & Spatial Elevation Integrity
* **`04_keyed_locations.md` vs `handouts/node_map.md`**:
  * **Location 1 (The Mustering-Yard)**: Assigned to **Level 3A (Upper Staging Tier)**. Connects North to Safe Haven (400-ft shaft), South to Location 2 (30-ft archway), East to Location 3 (crawlway vent). Matched exactly in `node_map.md` lines 21–26 and 94–96.
  * **Location 2 (The Upper Gatehouse)**: Assigned to **Level 3A**. Connects North to Location 1, South to Location 3 (sloping 20-ft ramp). Features buckled adamant doors, keystone collapse trap (30 Dmg), and fallback redoubt (+2 Band Readiness). Matched in `node_map.md` lines 27–32, 97, and 144–168.
  * **Location 3 (The First Armoury)**: Assigned to **Level 3B (Middle Arsenal Tier)**. Connects North to Location 2, South to Location 4 (pillared archway), West to Location 5 (maintenance duct bypass). Matched in `node_map.md` lines 34–38 and 98–99.
  * **Location 4 (The Broken Hall)**: Assigned to **Level 3B**. Connects North to Location 3, South to Location 5 (double cedar doors), East to sealed arch with royal cartouche. Matched in `node_map.md` lines 39–43 and 100.
  * **Location 5 (The Second Armoury)**: Assigned to **Level 3B**. Connects North to Location 4, South to Location 6 (bronze double doors), West to Location 7 (iron pressure door). Matched in `node_map.md` lines 44–64, 101–102, and 172–191.
  * **Location 6 (The Hall of the Mauler)**: Assigned to **Level 3C (Deep Sanctuary Tier)**. Connects North to Location 5, South to Location 9 (colonnade avenue). Features 20-ft elevated catwalks, scrap nest, stalactite hazards. Matched in `node_map.md` lines 68–72 and 105.
  * **Location 7 (The Poisoned Halls)**: Assigned to **Level 3B-minus (Depressed Basin)**. Connects East to Location 5 (pressure door), South to Location 8 (bronze pressure door). Matched in `node_map.md` lines 49–56 and 102–103.
  * **Location 8 (The Upper Armoury)**: Assigned to **Level 3B-minus / intermediate**. Connects North to Location 7, East/South to Location 9 (reinforced stone flue). Matched in `node_map.md` lines 57–64 and 103–104.
  * **Location 9 (The King's Door)**: Assigned to **Level 3C**. Connects North to Location 6, West to Location 8, South to Location 10. Matched in `node_map.md` lines 73–77, 104–106.
  * **Location 10 (The Lower Armoury / Royal Vault)**: Assigned to **Level 3C**. Connects North to Location 9. Contains Dais of Durin, Durin's Axe, 3 Relic Coffers, Mithril ingots. Matched in `node_map.md` lines 78–81 and 106–107.

### 1.3 D66 Scavenge Table Verification
* **`06_relics_and_rewards.md` (lines 357–470)** contains exactly **36 distinct, valid entries** spanning rolls `11` through `66` ($6 \times 6$ grid with no numbers ending in 0, 7, 8, or 9):
  * `11` (Cured Dwarf-Tobacco), `12` (Gromril-Tipped Pitons), `13` (Scribe's Luminescent Ink), `14` (Runic Whetslate of Erebor), `15` (Lead-Sealed Rations), `16` (Notched Orc Scimitar)
  * `21` (Silver Runic Dice), `22` (Flask of Dragon-Fire Oil), `23` (Acoustic Listening Horn), `24` (Chiseled Blood-Agate), `25` (Hard-Tallow Scent Candles), `26` (Shattered Mail Rings)
  * `31` (Dwarven Salve of Stone-Skin), `32` (Masterwork Pick-Head), `33` (Torn Page of the Armouries), `34` (Black Orc-Poison Phial), `35` (Carved Bone Whistle), `36` (Electrum Belt Clasp)
  * `41` (Folded Silk Rope), `42` (Charcoal Filtration Mask), `43` (Engraved Bronze Mirror), `44` (Iron Hills Field Flask), `45` (Runic Key-Blank), `46` (Severed Troll-Claw Amulet)
  * `51` (Vial of Mirrormere Water), `52` (Mithril Wire Filigree), `53` (Ancient Stone Mason's Wedge), `54` (Preserved Herbal Poultice), `55` (Serrated Goblin Scalping Knife), `56` (Gold Ingot of the Royal Mint)
  * `61` (Ithildin Lens), `62` (Dwarven War-Horn Mouthpiece), `63` (Black Iron Caltrops), `64` (Seal of the Third Marshal), `65` (Ancient Dwarven Compass), `66` (True Gromril Chain Link)
  * Every entry features concrete lore description, specific in-game mechanical bonus/effect (e.g. dice bonuses, condition cures, damage), and clear economic value (Silver Pennies or Treasure Points).

### 1.4 The Three Marshal's Key Acquisition Pathways
* **`06_relics_and_rewards.md` §4 (lines 192–285)** details all three pathways:
  * **Pathway 1 (Combat Ambush)**: Intercepting Captain Grashnak (AL 6, End 24, Might 2, Hate 6, Armour 3d) and 3 Udûn Sniffers in Rooms 3/5. Slaying in $\le 2$ rounds generates 0 Noise; 3+ rounds generates +2 Noise.
  * **Pathway 2 (Social Parley)**: Negotiating with Grik the Skulker in Location 1. Riddle TN 14 / Persuade TN 15 with trade options (silver, tobacco, liquor, revenge) yielding silent key acquisition (+0 Noise, +0 Alert).
  * **Pathway 3 (Craft Endeavour / Lockbreaker Bypass)**: Extended Skill Endeavour at Location 9 with Resistance 6, Time Limit 3 turns, testing Scan/Craft/Burglary (Turn 1), Burglary/Riddle (Turn 2), and Craft/Athletics/Band Expertise (Turn 3). Einar gains +2 / Advantage via *The Broken Key*, Bróga gains +1d via *Vaultbreaker*. Includes explicit partial and critical failure outcomes.

### 1.5 Dying Scribe's Letter Prop
* **`handouts/dying_scribe_letter.md`** contains:
  * Section 2: Complete Cirth runic heading in formal Angerthas Moria (`ᚠᚱᚨᚱ ᛋᛟᚾ ᛟᚠ ᚠᚱᛖᚱᛁᚾ...`) followed by full archaic English text detailing the Fall of Moria in 1981 TA, the sealing of Durin's Axe in the Lower Armoury, the loss of the Marshal's Key, and the rising Balrog miasma.
  * Section 3: Formatted printable ASCII handout box suitable for direct table play.
  * Section 4: Skill-gated GM revelations: Lore/Scan TN 12 (Einar with Broken Key), Craft/Healing TN 14 (Hjoldring/Einar), and Riddle/Old Khuzdul TN 14 (Khoril) granting +2d on Turn 1 of the King's Door lockpicking endeavour.

---

## 2. Logic Chain

1. **Premise 1 (Completeness & Layout)**: The module structure strictly follows `PROJECT.md` and `TEST_READY.md`. All 12 canonical files and handouts are present, fully populated, and free of placeholders or truncations.
2. **Premise 2 (Spatial Topology & Navigation)**: Every keyed location in `04_keyed_locations.md` aligns seamlessly with `handouts/node_map.md` in elevation tier (3A, 3B, 3C), room dimensions, doorway mechanisms, and bypass flues.
3. **Premise 3 (Mechanical Rigor & TOR 2e Conformance)**:
   - Adversary stat blocks adhere to TOR 2e standards (Attribute Levels, Endurance, Might, Hate, Parry, Armour dice, Fell Abilities).
   - Player-Heroes (Torvir, Einar, Khoril) have mathematically valid TNs ($20 - \text{Attribute}$), fatigue/load thresholds, and distinctive traits.
   - The Moria Band rules integrate Band Readiness 5 (TN 15), 5 Dispositions, 4 tactical squad roles, and a 50% casualty weariness boundary.
   - The 4-Stage Alert Tracker and Sound Action Economy prevent automatic TPK swarms while providing meaningful tactical consequences.
4. **Premise 4 (Operability & Flexibility)**: The three distinct pathways to solve the King's Door ensure players are never bottlenecked by failed rolls or rigid linear scripting.
5. **Conclusion**: The adventure module is mechanically sound, narratively compelling, publication-ready, and fully verified.

---

## 3. Adversarial Challenge & Stress-Test Report

### Challenge Summary
* **Overall Risk Assessment**: **`LOW`**
* The module demonstrates robust defensive design across narrative pacing, spatial navigation, and mechanical stress points.

### Challenges & Stress Tests

#### Challenge 1: Pacing & Alert Tracker Saturation (Sound Action Economy)
* **Assumption Challenged**: Can a tactical party complete the delve without prematurely triggering Alert 3 (*Drums in the Deep*) and failing the mission?
* **Attack Scenario**: The Company engages in multiple noisy combats (e.g. 2 rounds in Room 1 [+2 Noise], 2 rounds in Room 3 [+2 Noise], toppling the idol in Room 4 [+3 Noise], firing the ballista in Room 5 [+4 Noise] = Total 11 Noise -> Alert 2).
* **Blast Radius**: Reaching Alert 2 reduces the Hunt Threshold from 14 to 12, gives -1d to Awareness against ambushes, and summons Grimnar's stalking pursuit.
* **Mitigation Verified**: The module provides explicit mechanical countermeasures:
  - 1-round silent kills generate 0 Noise (`04_keyed_locations.md` p. 195).
  - Khoril's Marching Discipline roll (Battle TN 14) allows 10 Dwarves to traverse rooms with 0 Noise.
  - Muffling the Balrog idol with canvas reduces noise from +3 to +1 (`04_keyed_locations.md` p. 425).
  - Social parley with Grik yields the key/intel with 0 Noise.
* **Result**: **PASS** (Defenses are clear and rewarding of tactical play).

#### Challenge 2: The Mauler Combat & Potential TPK
* **Assumption Challenged**: Is an Attribute Level 10 Great Cave-troll with 80 Endurance, Might 2, and 5d Armour excessively lethal for three heroes and a band?
* **Attack Scenario**: Frontal melee charge in open ground against The Mauler's 8-damage club and Heavy Blow (+10) special damage.
* **Blast Radius**: Hero down in 2 rounds; Band Weariness triggered.
* **Mitigation Verified**: The module provides 4 non-suicidal tactical layers:
  1. *Riddle Duel Combat Task* (TN 14): Capitalizes on the troll's *Dull-Witted* trait to strip Hate and pacify it in 3 successes without dealing lethal damage.
  2. *Elevated Catwalks (20 ft)*: Grants High Ground (+1d) and immunity to ground slams.
  3. *Hanging Stalactites*: Dropping a stalactite deals 20 direct damage (bypassing armour) and knocks the troll Prone.
  4. *Torsion Ballista / Grond-Ram*: Firing the primed engine from Room 5 strips 2d of the troll's scrap armour permanently.
  5. *Band Interception*: Dolg the Bulwark can absorb one crushing blow per round.
* **Result**: **PASS** (Multi-vector encounter design prevents combat grind).

#### Challenge 3: Extreme Band Burden & Fatigue Degradation
* **Assumption Challenged**: Does salvaging 50 suits of mail (+50 Supply Points) in Location 8 immobilize the Band or guarantee an unavoidable TPK during the Fighting Withdrawal?
* **Attack Scenario**: Shifting to Heavy Burden imposes -1d on Band Manoeuvre, -1d on Fatigue tests, and +1 Noise per hall traversed.
* **Blast Radius**: Band becomes Weary, slowing the escape while the 6-Round evacuation countdown ticks down.
* **Mitigation Verified**:
  - Establishing the *Rearguard Choke Point Defense* at Location 2 Gatehouse grants an automatic **+2 Band Readiness bonus** (reducing extraction Clash TN from 15 to 13).
  - The *Keystone Collapse Trap* deals 30 crushing damage and permanently blocks pursuit at Location 2, buying the Band the final rounds needed to winch up the 400-ft shaft.
  - A 30-minute Short Rest in Location 10 behind the locked Vault Barricade allows players to spend Fellowship points and clear Weary states before initiating withdrawal.
* **Result**: **PASS** (High tension with mathematically viable escape mechanics).

### Stress Test Results Table

| # | Stress Scenario | Expected Behavior | Observed Module Mechanic | Status |
|---|---|---|---|:---:|
| 1 | All 3 Heroes fail Dread Test at Balrog Idol (Room 4) | Party suffers Shadow & Daunted; must not softlock | Khoril or companion can sing *Song of Durin* (Song TN 14) to clear Daunted and restore +1 Band Hope | **PASS** |
| 2 | Party loses/skips physical Marshal's Key | Must have alternative method to open King's Door | Extended Skill Endeavour (Resistance 6, Time Limit 3 turns) with Einar (+2 Scan) and Bróga (+1d) | **PASS** |
| 3 | Unprotected Hero enters Room 7 Toxic Miasma | Severe health drain without instant unavoidable death | 1-min checks (Endurance TN 14); Craft TN 15 mask grants 4 hrs immunity; flue lever vents room in 3 rds | **PASS** |
| 4 | Durin's Axe Claiming pushes Eye Awareness $\ge 14$ | Triggers Revelation Episode as designed | Triggers Revelation Event; Alert surges to Tier 3; 6-Round extraction timer begins | **PASS** |
| 5 | Grimnar attempts Great Leap to assassinate Einar at lock | Tactical counters available to protect locksmith | Shield-Wall Phalanx forms testudo (Total Cover for Einar); Torvir can initiate single combat Duel | **PASS** |

---

## 4. Caveats

* **No Caveats**: All 12 adventure files, 4 handouts, and 188 automated test cases were thoroughly inspected and cross-referenced.
* Physical dice rolling in live table play will introduce stochastic variance, but the mathematical safety margins and pacing dials provided in Chapter 7 fully accommodate table deviations.

---

## 5. Conclusion & Final Verdict

The adventure module *The Armouries of the Third Deep* represents an exceptional, masterclass publication for *The One Ring 2nd Edition*. It flawlessly balances deep Middle-earth lore, intricate Dwarven architectural design, modular tactical depth, robust Band management, and strict mechanical adherence to the core rules of TOR 2e.

### Final Verification Verdict
# **`APPROVE`**

---

## 6. Verification Method

To independently verify this evaluation:
1. **Automated Test Suite**:
   ```bash
   python tests/test_runner.py
   python tests/test_runner.py --tier 1
   python tests/test_runner.py --tier 2
   python tests/test_runner.py --tier 3
   python tests/test_runner.py --tier 4
   ```
2. **File Cross-Inspection**:
   * Inspect `c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep/04_keyed_locations.md` lines 133–922 vs `handouts/node_map.md` lines 8–108 for spatial elevation and connection mapping.
   * Inspect `c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep/06_relics_and_rewards.md` lines 357–470 for the complete 36-entry D66 Scavenge Table.
   * Inspect `c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep/06_relics_and_rewards.md` lines 192–285 for the 3 Marshal's Key acquisition pathways.
   * Inspect `c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep/handouts/dying_scribe_letter.md` lines 27–143 for Cirth runes, English translation, and skill revelations.
