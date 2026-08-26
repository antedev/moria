# Changes Record — Milestone M1: Keyed Locations Refactoring

**Agent**: `worker_m1` (implementer, qa, specialist)  
**Date**: 2026-08-26  
**Files Modified**:
1. `c:/Users/ante/Documents/github/Moria/adventures/armouries_of_the_third_deep/04_keyed_locations.md`
2. `c:/Users/ante/Documents/github/Moria/adventures/armouries_of_the_third_deep/quickstart/02_keyed_locations.md`

---

## 1. Requirement 1: Player Agency & Neutral Scene Presentation (R1)

### `04_keyed_locations.md`
- **Eliminated all prescriptive PC actions**:
  - Replaced hardcoded guide prescriptions (*"Marching Discipline (Khoril's Leadership): Khoril rolls TRAVEL..."*) with open leadership options (*"Marching Discipline: A Player-Hero leading the Company rolls TRAVEL or ENHEARTEN (invoking Leadership Trait grants +1d)..."*).
  - Replaced hardcoded scouting actions (*"Einar invoking The Broken Key..."*) with neutral item/gift interactions (*"A hero investigating with The Broken Key rolls Favoured..."*).
  - Replaced forced flaw actions (*"Torvir's Curse of Vengeance: On failure, Torvir flies into uncontrollable rage and must spend his next action attacking the idol with his Great Axe..."*) with generalized flaw mechanics (*"Curse of Vengeance Flaw: On a failure, a hero possessing the Curse of Vengeance Flaw gains 1 additional Shadow Point (Dread) and must spend their next action striking the blasphemous effigy..."*).
  - Replaced forced hoard actions (*"Einar's Dragon-sickness: On failure, Einar becomes obsessed..."*) with generalized flaw mechanics (*"Dragon-sickness Flaw: On a failure, a hero possessing the Dragon-sickness Flaw is transfixed by the gold-leaf veins..."*).
  - Replaced hardcoded ritual prescriptions (*"The Blood of Durin Inscription Ritual... Torvir or Khoril (being of Durin's royal line)..."*) with open lineage mechanics (*"A Dwarf hero of Durin's royal lineage slices their palm..."*).
  - Replaced hardcoded duel combat task (*"Duel Combat Task (Torvir): Torvir challenges Grimnar..."*) with neutral combat task presentation (*"Duel Combat Task: A hero in Forward stance challenges Grimnar in single combat (AWE roll vs Grimnar's Attribute Level 6)..."*).
  - Replaced hardcoded artifact claim (*"Torvir lifts Durin's Axe while Khoril sounds a low, solemn note..."*) with neutral ceremonial actions (*"Ceremonial Claim: A Dwarf hero lifts Durin's Axe while the Company marks the sacred moment..."*).
  - Purged 100% of pregen names (`Torvir`, `Einar`, `Khoril`) from room descriptions and check titles across all 10 locations.

### `quickstart/02_keyed_locations.md`
- **Eliminated all prescriptive PC actions**:
  - Replaced hardcoded party assumptions (*"Torvir and the Dwarf vanguard cut down 2 sentries immediately..."*) with company actions (*"The Company eliminates 2 sentries immediately before they can sound an alarm horn..."*).
  - Replaced forced character flaw actions (*"Torvir's Curse of Vengeance: On failure, Torvir flies into uncontrollable rage..."*) with standard Flaw triggers.
  - Replaced prescriptive hoard interactions (*"Einar gains 2 Shadow Points (Greed) and becomes compelled to stuff every golden goblet..."*) with open Shadow tests against avarice.
  - Purged 100% of pregen names (`Torvir`, `Einar`, `Khoril`) from all 10 location descriptions and skill check prompts.

---

## 2. Requirement 2: Streamline Skill Checks & Remove Hardcoded Pregen Attribute TNs (R2)

### `04_keyed_locations.md`
- **Removed 60+ occurrences of hardcoded pregen TN listings**:
  - Purged all instances of `(Wits TN: Torvir 15, Einar 15, Khoril 16)`, `(Strength TN: Torvir 13, Einar 14, Khoril 13)`, `(Heart TN: Torvir 18, Einar 17, Khoril 16)`, etc.
- **Formatted all skill tests in canonical TOR 2e notation**:
  - Standardized check labels: `**STEALTH roll**`, `**SCAN roll**`, `**BATTLE roll**`, `**LORE roll**`, `**CRAFT roll**`, `**ATHLETICS roll**`, `**HEALING roll**`, `**HUNTING roll**`, `**AWE roll**`, `**ENHEARTEN roll**`, `**SONG roll**`, `**AWARENESS roll**`, `**RIDDLE roll**`, `**EXPLORE roll**`, `**PROTECTION test**`, `**SHADOW test**`.
  - Retained canonical non-hero target numbers where appropriate: `Band TN 15`, `Target Strength TN + Shield`, and adversary/trap `Injury TN`.
  - Fully preserved and standardized all Skill Endeavour blocks:
    * Location 2: `Skill Endeavour: Fortifying the Forward Redoubt (Resistance 3)`
    * Location 3: `Skill Endeavour: Disarming the Scythe Scrap-Trap Network (Resistance 3)`
    * Location 4: `Skill Endeavour: Controlled Toppling of the Balrog Idol (Resistance 3)`
    * Location 5: `Skill Endeavour: Calibrating & Arming the Siege Engines (Resistance 3)`
    * Location 7: `Skill Endeavour: Assembling Squad Respirator Masks (Resistance 3)`
    * Location 9: `Skill Endeavour: Bypassing the Adamant Runic Lock (Resistance 6)`
  - Standardized all sub-bullets under test blocks to include explicit `*Modifiers*:`, `*Consequence of Failure*:`, and `*Degrees of Success (6 icons)*:` with `**6**:` and `**66**:` effects.

### `quickstart/02_keyed_locations.md`
- **Removed 40+ occurrences of hardcoded pregen TN listings**:
  - Purged all `(Wits TN: Torvir 15, Einar 15, Khoril 16)`, `(Strength TN: ...)`, etc.
  - Standardized all skill checks to `**SKILL roll**` and `**PROTECTION test**` / `**SHADOW test**`.
  - Retained canonical Resistance ratings on all 6 Skill Endeavours (Resistance 3 and Resistance 6).

---

## 3. Requirement 3: Boxed Read-Aloud Text Clean-Up & Spoiler Removal (R3)

### `04_keyed_locations.md`
- Rewrote all 10 boxed read-aloud descriptions in English with evocative, concise, sensory-first prose:
  - **Location 1 (Mustering-Yard)**: Describes high overlook, colossal basalt pillars, vast paved floor, broken spears, and sulfur draft. Omits sentry camp placement and Grik ambush.
  - **Location 2 (Upper Gatehouse)**: Describes granite gatehouse, buckled adamant doors, murder-holes, and whistling draft. Omits keystone trap stats.
  - **Location 3 (First Armoury)**: **CRITICAL SPOILER REMOVED**. Describes empty despoiled weapon racks, bone refuse, and iron dust. Completely purged all descriptions of taut sinew tripwires, counterweighted scythes, and dripping black venom!
  - **Location 4 (Broken Hall)**: Describes marble pillars, defaced wall friezes, and the looming winged silhouette of the jagged iron Balrog effigy radiating cold. Omits the secret cartouche puzzle solution.
  - **Location 5 (Second Armoury)**: Describes vast workshop hall, aroma of cedar, machine oil, and pine resin, covered war machines, and crane scaffoldings.
  - **Location 6 (Hall of the Mauler)**: **MAJOR SPOILER REMOVED**. Describes suspended catwalks, apocalyptic graveyard of wargear, foul animal musk, and deep floor-shaking rhythmic snores. Completely removed the description of the sleeping troll and its armor carapace from the read-aloud text!
  - **Location 7 (Poisoned Halls)**: **CRITICAL SPOILER REMOVED**. Describes heavy waist-deep emerald-yellow vapor, motionless armored knights near the entrance, and stinging sulfur/ozone stench. Completely removed the far-room description of the slumped scribe and the lead scroll tube!
  - **Location 8 (Upper Armoury)**: **SPOILER REMOVED**. Describes pristine unlooted vault behind bronze doors, rows of cedar lockers, and gleaming dwarf-steel. Removed historical narrative explaining goblin deaths.
  - **Location 9 (The King's Door)**: **MAJOR SPOILER REMOVED**. Describes monumental star-iron and black granite portal, silver Ithildin runes of crown and anvil, and starlight glow. Completely purged the explicit description of the two keyholes and the two-key puzzle solution!
  - **Location 10 (Lower Armoury)**: Describes pure mountain air, slender white granite arches, mithril filigree, and the radiant glow over the central dais.

### `quickstart/02_keyed_locations.md`
- Rewrote all 10 boxed read-aloud descriptions in Swedish (*Högläsningstext*), strictly eliminating all trap, puzzle, and monster spoilers:
  - Location 3: Purged all mentions of tripwires, scythe blades, and venom.
  - Location 6: Purged the direct revelation of the sleeping troll and armor plating; focused on scale, catwalks, scrap heaps, and floor-shaking snores.
  - Location 7: Purged the far-room detail of the scribe with the lead tube through the dense fog.
  - Location 8: Purged the goblin death history.
  - Location 9: Purged the description of the two keyhole metals and puzzle mechanics.

---

## 4. Requirement 4: Canon TOR 2e Rule Audit & Condition Correction (R4)

### Purge of "Daunted" Condition
- `04_keyed_locations.md`:
  * Line 472: Replaced `suffers the Daunted condition (cannot spend Hope points) for 1 hour` with `becomes Miserable until taking a Rest`.
  * Line 477: Replaced `clearing the Daunted condition from all companions` with `clearing the Miserable condition from all companions and restoring +1 Hope`.
  * Line 486: Replaced `removes Daunted from all heroes, and restores +1 Band Hope` with `cleanses the oppressive aura, removes Miserable from all heroes, and restores +1 Band Hope`.
  * Line 1065: Replaced `suffers the Daunted condition for 1 hour` with `gains 1 Shadow Point (Dread) and becomes Miserable until taking a Rest`.
- `quickstart/02_keyed_locations.md`:
  * Line 210: Replaced `becomes Daunted` with `becomes Miserable until taking a Rest`.
  * Line 215: Replaced `clearing the Daunted condition` with `clearing the Miserable condition`.
  * Line 224: Replaced `removes Daunted` with `removes Miserable`.
  * Line 452: Replaced `suffers the Daunted condition for 1 hour` with `gains 1 Shadow Point (Dread) and becomes Miserable until taking a Rest`.

### Non-Canonical Condition & Hazard Alignment
- Replaced references to "Poisoned condition" with official mechanics: *Weary* condition + Endurance loss per hour until treated with First Aid.
- Replaced references to "Dying condition" on poison rolls with official mechanics: reduced to 0 Endurance and suffering a Wound (becoming *Dying* only if already Wounded).
- Verified Distinctive Features (*Burglary*, *Leadership*, *Smith*, *Vaultbreaker*, *Mighty*, *Wary*, *Enemy-lore*) are consistently invoked for `+1d` bonuses.

---

## 5. Verification Summary

| Check / Metric | `04_keyed_locations.md` | `quickstart/02_keyed_locations.md` | Status |
|---|:---:|:---:|:---:|
| Hardcoded Pregen TNs (`Torvir 15`, etc.) | 0 | 0 | **PASS (100% Clean)** |
| Prescriptive PC Names (`Torvir`, `Einar`, `Khoril`) | 0 | 0 | **PASS (100% Clean)** |
| Non-Canonical "Daunted" Occurrences | 0 | 0 | **PASS (100% Clean)** |
| Boxed Text Trap / Monster Spoilers | 0 | 0 | **PASS (100% Clean)** |
| Skill Endeavours Resistance Accuracy | 6/6 Exact | 6/6 Exact | **PASS (100% Clean)** |
| Official 18 Skills Compliance | 100% | 100% | **PASS (100% Clean)** |
| 5e Leaks (DC, Advantage, Spell slots) | 0 | 0 | **PASS (100% Clean)** |
