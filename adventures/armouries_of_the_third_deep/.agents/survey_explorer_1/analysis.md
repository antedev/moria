# Comprehensive Survey & System Audit Report: Armouries of the Third Deep

**Date**: 2026-08-26  
**Auditor**: `survey_explorer_1`  
**Target Suite**: `c:/Users/ante/Documents/github/Moria/adventures/armouries_of_the_third_deep/`  
**Scope**: Modular chapter files (`01_campaign_context.md` through `07_gm_playbook_and_pacing.md`), quickstart files, handouts, and system mechanics.

---

## Executive Summary

A comprehensive survey and forensic audit of all markdown chapter files in *The Armouries of the Third Deep* was conducted against four foundational design and rules criteria:
1. **R1: Player Agency Violations & Prescriptive PC Assumptions**
2. **R2: Hardcoded Pre-gen Target Numbers (TNs)**
3. **R3: Boxed Read-Aloud Text Quality, Tone & Spoilers**
4. **R4: Canon The One Ring 2e (TOR 2e) Rules, Adversaries & Condition Integrity**

The audit confirmed that while the architectural layout, narrative pacing, and Band mechanics provide a robust and flavorful adventure framework, extensive refactoring is required across all 7 modular chapter files to eliminate prescriptive player actions, remove dozens of hardcoded pre-gen Target Numbers (`Torvir 15, Einar 15, Khoril 16`), purge the non-canonical **"Daunted"** condition, and repair critical spoiler leaks in boxed read-aloud descriptions (notably Locations 3, 7, and 8).

---

## Audit Matrix by Chapter

| Chapter File | R1: Agency Violations | R2: Hardcoded Pregen TNs | R3: Read-Aloud Spoilers / Purple Prose | R4: Non-Canonical Rules / Conditions | Status |
|---|---|---|---|---|---|
| `01_campaign_context.md` | Minor (Relic/item descriptions prescribe PC usage) | Minor (TN listings in Pregen stat blocks & guide role) | N/A | Clean | **Requires Alignment** |
| `02_band_mechanics.md` | High (Prescribes specific PC combat/leader actions) | Moderate (Hardcoded TNs in leader checks) | N/A | Minor (Faltering/Fatigue terminology) | **Requires Alignment** |
| `03_operational_mechanics.md` | Moderate (Prescribes Einar scanning, Khoril horn) | Moderate (Hardcoded TNs in hazard resolutions) | N/A | Minor (Ad-hoc poison/suffocation mechanics) | **Requires Alignment** |
| `04_keyed_locations.md` | **Critical** (Extensive PC action dictations across all 10 locations) | **Critical** (60+ occurrences of `Torvir 15, Einar 15, Khoril 16`, etc.) | **Critical** (Major trap/prop spoilers in Locations 3, 7, 8; Swedish text) | **Critical** (4 occurrences of invented "Daunted" condition) | **Major Refactor Required** |
| `05_adversaries_and_hazards.md` | High (Grimnar/Mauler tactics scripted against specific PCs) | High (20+ hardcoded pre-gen TNs in stat blocks/hazards) | N/A | **Critical** ("Daunted" condition in Strike Fear; ad-hoc poison/dying rules) | **Major Refactor Required** |
| `06_relics_and_rewards.md` | High (Prescribes Einar lockpicking, Torvir dueling/intimidating) | Moderate (Hardcoded TNs in lock/social checks) | N/A | Clean (Craft rewards well-modeled) | **Requires Alignment** |
| `07_gm_playbook_and_pacing.md` | **Critical** (Turn-by-turn pacing scripts exact PC choices) | High (Hardcoded TNs across session timelines) | N/A | Clean | **Requires Alignment** |

---

## 1. Audit R1: Player Agency Violations & Prescriptive Text

### 1.1 Nature of the Issue
Throughout the modular chapters, encounter text frequently bypasses player choice by asserting which hero attempts an action, how they react emotionally, or how they use their distinctive traits. This converts open tactical choices into scripted cutscenes.

### 1.2 Documented Occurrences & Exact Snippets

#### A. `02_band_mechanics.md`
- **Line 86**: `...enables Einar's Favoured SCAN checks.`  
  *Issue*: Assumes Einar is always the scout making Scan checks.
- **Line 104**: `Einar Synergy: Einar can move up alongside the screen without breaking stealth, allowing him to use The Broken Key...`  
  *Issue*: Scripting PC tactical choices.
- **Line 115**: `...creating room for Torvir's Great Axe swings.`  
  *Issue*: Assumes Torvir is the vanguard attacker.
- **Line 291**: `Leader Check: Khoril rolls TRAVEL (Heart TN 16) or ENHEARTEN (Heart TN 16), invoking his Leadership Trait for +1d.`  
  *Issue*: Prescribes Khoril as the sole leader rolling Travel/Enhearten.
- **Lines 343–346**:
  - `Command (Khoril): Khoril rolls BATTLE...`
  - `Inspire (Torvir or Khoril): Hero rolls ENHEARTEN...`
  - `Fight (Torvir or Einar): Hero attacks...`
  - `Duel (Torvir): Torvir engages the enemy Champion...`  
  *Issue*: Hardcodes specific leader combat tasks to specific pre-gen names.

#### B. `03_operational_mechanics.md`
- **Line 61**: `Einar can make Scan tests without risk of alerting guards.`
- **Lines 105, 128**: `Sounding Khoril's Battle-horn of the Realm`

#### C. `04_keyed_locations.md`
- **Line 203**: `Torvir invoking Enemy-lore (Orcs) or Dwarven Lore gains +1d.`
- **Line 208**: `Torvir invoking Enemy-lore (Orcs) grants +1d.`
- **Line 215**: `Marching Discipline (Khoril's Leadership): Khoril rolls TRAVEL or ENHEARTEN (Heart TN: 16)...`
- **Line 296**: `Einar invoking The Broken Key rolls Favoured.`
- **Line 378**: `Einar invoking The Broken Key rolls Favoured.`
- **Line 473**: `Torvir's Curse of Vengeance: On failure, Torvir flies into uncontrollable rage and must spend his next action attacking the idol with his Great Axe, generating +2 Noise Points and gaining 2 Fatigue!`  
  *Issue*: Forces a specific character action rather than presenting standard Shadow/Dread mechanics.
- **Line 474**: `Einar's Dragon-sickness: On failure, Einar becomes obsessed with prying molten gold-leaf from the idol, wasting 10 minutes.`
- **Line 483**: `Banish the Gloom — SONG (Strength TN: Khoril 13) or ENHEARTEN (Heart TN: Khoril 16): Khoril or a companion sings...`
- **Line 496**: `Prying the Idol's Jewels — STEALTH (Wits TN: Einar 15) or CRAFT (Strength TN: Einar 14)`
- **Line 796**: `Einar invoking The Broken Key rolls Favoured.`
- **Line 802**: `First Aid Overwatch (Einar): Einar keeps soothing balms ready...`
- **Line 959**: `Einar and Bróga can attempt the Skill Endeavour...`
- **Line 975**: `Einar invoking The Broken Key rolls Favoured.`
- **Line 981**: `The Blood of Durin Inscription Ritual — AWE (Strength TN: Torvir 13, Khoril 13) or ENHEARTEN... Context: Torvir or Khoril (being of Durin's royal line) slicing their palm...`
- **Line 991**: `Duel Combat Task (Torvir): Torvir challenges Grimnar in single combat...`
- **Line 994**: `Form a protective testudo over Einar while he works the locks...`
- **Line 1068**: `Resisting Dragon-Sickness & Greed — Shadow Test (Heart TN: Einar 17 or Wits TN: Einar 15)... Consequence of Failure: Einar gains 2 Shadow Points (Greed)...`
- **Line 1079**: `Ceremonial Guard (Torvir & Khoril): Torvir lifts Durin's Axe while Khoril sounds a low, solemn note...`

#### D. `05_adversaries_and_hazards.md`
- **Lines 104–105, 154**: `The negotiating hero (Torvir, Einar, or Khoril)...`
- **Line 235**: `Hatred (Durin's Folk): Attack rolls against Torvir, Khoril, and Dwarf Companions...`
- **Line 242**: `Vengeful Strike: If struck in melee by Torvir, Einar, or Khoril...`
- **Lines 261–267**: Grimnar's tactics scripted: `targeting Khoril (the horn-bearer) and Einar (the locksmith)... When Torvir or the Shield-Wall advances... strike at Einar while he works the lock mechanisms...`
- **Lines 281–285**: Scripted combat dialogue specifically insulting Torvir, Einar, and Khoril.
- **Line 473**: `Hjoldring, Einar, or Bróga can assemble...`
- **Line 490**: `Einar or Austri can detect shifting keystones...`
- **Line 600**: `Khoril can spend 1 point of Band Hope...`
- **Line 608**: `allow Torvir's Enemy-lore (Orcs) or Einar's Scan...`

#### E. `06_relics_and_rewards.md`
- **Line 115**: `Torvir Hammerstone's Destiny: If Torvir takes up the axe...`
- **Line 237**: `carried by Einar or Khoril`
- **Line 242**: `Torvir can terrify Grik into surrendering the key immediately.`
- **Lines 257–258**: `PARTICIPANTS: Primary: Einar (Treasure Hunter) & Bróga (Vaultbreaker), Support: Torvir (Anchor/Brace), Khoril (Lookout/Acoustic Dampener)`
- **Line 271**: `Einar Synergy: Einar gains Favoured status...`
- **Line 279**: `Torvir Support: Torvir can spend 1 Hope...`

#### F. `07_gm_playbook_and_pacing.md`
- **Lines 100, 106, 119, 132, 150–153, 213, 258–273, 358, 360, 372, 419**: Session scheduling repeatedly tells the GM that specific heroes perform specific actions.

---

## 2. Audit R2: Hardcoded Pre-gen Target Numbers (TNs)

### 2.1 Nature of the Issue
In *The One Ring 2e*, Player-Hero Target Numbers are calculated strictly from character attributes ($20 - \text{Attribute}$) and live on player character sheets. Modules must **never** hardcode specific TN numbers for pre-generated characters inside adventure obstacle descriptions. 

### 2.2 Inventory of Hardcoded TN Listings

| File | Line Numbers | Hardcoded Text Snippet |
|---|---|---|
| `02_band_mechanics.md` | 137 | `CRAFT — Strength TN: Torvir 13, Einar 14, Khoril 13` |
| `02_band_mechanics.md` | 291 | `TRAVEL (Heart TN 16) or ENHEARTEN (Heart TN 16)` |
| `02_band_mechanics.md` | 343 | `BATTLE (Strength TN 13 / Heart TN 16)` |
| `02_band_mechanics.md` | 344 | `ENHEARTEN (Heart TN: Torvir 18, Khoril 16)` |
| `02_band_mechanics.md` | 345 | `Strength TN (Torvir 13, Einar 14)` |
| `03_operational_mechanics.md` | 76 | `ATHLETICS test (Strength TN: Torvir 13, Einar 14, Khoril 13...)` |
| `03_operational_mechanics.md` | 225 | `CRAFT (Strength TN: Torvir 13, Einar 14, Khoril 13)` |
| `03_operational_mechanics.md` | 226 | `HEALING (Heart TN: Torvir 18, Einar 17, Khoril 16)` |
| `03_operational_mechanics.md` | 228 | `CRAFT or ATHLETICS (Strength TN: Torvir 13, Einar 14, Khoril 13...)` |
| `03_operational_mechanics.md` | 245–246 | `ATHLETICS test (Strength TN: Torvir 13, Einar 14, Khoril 13)` |
| `04_keyed_locations.md` | 142, 184, 190, 196, 202, 207, 215, 225 | `Wits TN: Torvir 15, Einar 15, Khoril 16`, `Heart TN: Torvir 18...`, `Strength TN: Torvir 13...` |
| `04_keyed_locations.md` | 283, 290, 295, 300 | `Strength TN: Torvir 13, Einar 14, Khoril 13`, `Wits TN: ...` |
| `04_keyed_locations.md` | 332, 372, 377, 385, 391, 395, 399 | `Strength TN: ...`, `Heart TN: ...`, `Wits TN: ...` |
| `04_keyed_locations.md` | 466, 470, 478, 483, 490, 496 | `Wits TN: ...`, `Heart TN: ...`, `Strength TN: ...`, `Wits TN: Einar 15`, `Strength TN: Einar 14` |
| `04_keyed_locations.md` | 569, 572, 578, 584, 589, 593 | `Strength TN: ...`, `Heart TN: Khoril 16, Torvir 18, Einar 17`, `Wits TN: ...` |
| `04_keyed_locations.md` | 660, 662, 665, 669, 675, 681, 687, 691 | `Strength TN: ...`, `Wits TN: ...` |
| `04_keyed_locations.md` | 757, 761, 765, 772, 778, 783, 787, 791, 795 | `Strength TN: ...`, `Heart TN: ...`, `Wits TN: ...` |
| `04_keyed_locations.md` | 864, 866, 875, 881, 886 | `Strength TN: ...`, `Wits TN: ...` |
| `04_keyed_locations.md` | 965, 974, 981, 987 | `Strength TN: ...`, `Wits TN: ...`, `Heart TN: Torvir 18, Khoril 16` |
| `04_keyed_locations.md` | 1064, 1068, 1073 | `Strength TN: ...`, `Heart TN: Einar 17 or Wits TN: Einar 15`, `Wits TN: ...` |
| `05_adversaries_and_hazards.md` | 32, 105, 114, 119, 157, 188, 193, 303 | `Torvir 13, Einar 14, Khoril 13`, `Wits TN: Torvir 15...`, `Heart TN: Torvir 18...` |
| `05_adversaries_and_hazards.md` | 408–409, 416–417, 467, 473–475, 491, 495, 503–504, 521–531, 556–563 | Extensive repetitions of pre-gen TN formulas |
| `06_relics_and_rewards.md` | 115, 241, 242, 270, 275, 278 | `Heart TN 18`, `Wits TN: Torvir 15...`, `Strength TN: ...` |
| `07_gm_playbook_and_pacing.md` | 87, 100, 106, 113, 115, 119, 150, 156, 160, 165, 205, 262, 267, 272, 367 | Repetitions of pre-gen TN listings in facilitator timelines |

### 2.3 Required Canonical Replacement Format
Replace all occurrences with standard TOR 2e check format:
- `**SCAN roll**` (or `**SCAN test**`)
- `**STEALTH roll**`
- `**ATHLETICS roll**`
- `**CRAFT roll**`
- `**BATTLE roll**`
- `**LORE roll**`
- `**RIDDLE roll**`
- `**AWE roll**`
- `**ENHEARTEN roll**`
- `**HEALING roll**`
- `**VALOUR test**`
- `**PROTECTION test**`
Include standard situational modifiers (`+1d`, `-1d`, `Favoured`, `Ill-favoured`, or formal **Skill Endeavours with Resistance ratings**).

---

## 3. Audit R3: Boxed Read-Aloud Text Quality & Spoiler Audit

### 3.1 Overview of All 10 Keyed Locations in `04_keyed_locations.md`

1. **Location 1: The Mustering-Yard (Line 169)**
   - *Text*: Swedish prose describing high overlook, basalt plaza, octagonal pillars, scorches from Durin's Bane, scattered broken spears.
   - *Audit*: **PASS (No spoilers)**. Sets sensory atmosphere without revealing the Udûn sentries or Grik's hiding spot.
2. **Location 2: The Upper Gatehouse (Line 265)**
   - *Text*: Describes granite gatehouse, buckled adamant doors, murder-holes, dead counterweights.
   - *Audit*: **PASS (No spoilers)**. Accurately reflects visible architecture upon arrival.
3. **Location 3: The First Armoury (Line 360)**
   - *Text*: Despoiled weapon racks, bone piles, rusted caltrops.
   - *CRITICAL SPOILER*: *"Över den centrala gången löper tunna, spända senor mellan järnstolpar, riggade till motvägda lieklingor som dryper av ett vidrigt, glänsande svart gift."*
   - *Audit*: **FAIL (Critical Spoiler)**. Explicitly describes the concealed tripwires, scythe traps, and black venom to the players, completely eliminating the need for detection via **SCAN** or scout screens.
4. **Location 4: The Broken Hall (Line 455)**
   - *Text*: Defaced museum murals, obsidian hammer marks, 12-foot jagged Balrog idol radiating cold.
   - *Audit*: **PASS (No spoilers)**. The idol is massive and central; the secret cartouche is properly kept in GM reference notes.
5. **Location 5: The Second Armoury (Siege Workshop) (Line 555)**
   - *Text*: Cedar smell, oil, timber scaffolding, Grond-ram, torsion ballistas, counterweight crane.
   - *Audit*: **PASS (No spoilers)**. Large mechanical engines are immediately visible upon entering the illuminated workshop.
6. **Location 6: The Hall of the Mauler (Line 649)**
   - *Text*: Drill hall, iron catwalks, weapon heaps, sleeping scrap-clad Cave-Troll.
   - *Audit*: **PASS (No spoilers)**. Imposing boss room introduction that conveys scale and immediate sensory threat.
7. **Location 7: The Poisoned Halls (Line 746)**
   - *Text*: Emerald-yellow vapor, calcified Dwarven knights, slumped scribe at stone desk.
   - *CRITICAL SPOILER*: *"...vilan den bevarade gestalten av en urgammal dvärgskrivare – hans stenhänder är alltjämt knutna kring en förseglad cylinder av tungt bly."*
   - *Audit*: **FAIL (Spoiler & Fog Visibility Issue)**. Through 5 feet of dense, opaque toxic gas, the text immediately points out the specific lead scroll tube held by the scribe at the far side of the room, preempting exploration.
8. **Location 8: The Upper Armoury (Line 851)**
   - *Text*: Airtight bronze doors, rows of cedar lockers, gleaming mail, dead goblin looters.
   - *NARRATIVE SPOILER*: Tells players how the goblins died centuries ago (*"...som bröt upp den yttre porten för århundraden sedan, bara för att genast kvävas till döds av den giftiga ångan."*) rather than presenting immediate visual impressions.
   - *Audit*: **FAIL (Narrative Exposition)**. Should describe only the dried husks and pristine armaments.
9. **Location 9: The King's Door (Line 946)**
   - *Text*: Star-iron portal, glowing Ithildin runes of crown and anvil, dual keyholes.
   - *Audit*: **PASS (No spoilers)**. Accurately describes the majestic portal without spoiling Grimnar's ambush above.
10. **Location 10: The Lower Armoury / Royal Vault (Line 1043)**
    - *Text*: Pure air, white granite arches, black marble plinth, glowing Durin's Axe, First Age stone coffers.
    - *Audit*: **PASS (No spoilers)**. Evocative climax description.

---

## 4. Audit R4: Non-canonical Rules, Invented Conditions & Adversary Stats

### 4.1 Invented "Daunted" Condition
The "Daunted" condition is non-canonical and does not exist in *The One Ring 2e*. It appears in 5 locations across the module:
1. `04_keyed_locations.md:472`: `...gains 2 Shadow Points (Dread) and suffers the Daunted condition (cannot spend Hope points) for 1 hour.`
2. `04_keyed_locations.md:477`: `...clearing the Daunted condition from all companions.`
3. `04_keyed_locations.md:486`: `...removes Daunted from all heroes...`
4. `04_keyed_locations.md:1065`: `...suffers the Daunted condition for 1 hour.`
5. `05_adversaries_and_hazards.md:115` (*The Mauler — Strike Fear*): `...suffer 2 Shadow (Dread) and become Daunted (cannot spend Hope for the rest of the battle).`

**Canonical Replacement**:
In TOR 2e, fear, dread, and supernatural awe are resolved using:
- **Shadow Points (Dread)**
- **Loss of Hope Points**
- Triggering the **Miserable** condition (when current Shadow $\ge$ current Hope)
- Fleeing the combat stance / Bout of Madness triggers

### 4.2 Ad-Hoc Hazard & Health Conditions
1. **"Poisoned Condition"**: Referenced in Location 3 (`04_keyed_locations.md:372`) and `05_adversaries_and_hazards.md:411`. In TOR 2e, poison inflicts direct Endurance loss, the **Weary** condition, or an immediate **Wound** (or increases Injury TN).
2. **"Dying Condition"**: Used in `04_keyed_locations.md:757` and `05_adversaries_and_hazards.md:455` as an instant effect when reduced to 0 Endurance on an Eye of Sauron ($\mathbf{S}$). In TOR 2e, a character becomes **Dying** only if reduced to 0 Endurance while already **Wounded**, or upon suffering a second Wound.

### 4.3 Adversary Stat Block Certification
- **The Mauler** (AL 10, End 80, Might 2, Hate 10, Armour 5d, Parry —): Core math is sound; *Dull-Witted* Riddle mechanic correctly engages Riddle skill; *Strike Fear* must be purged of "Daunted".
- **Grimnar the Disgraced** (AL 6, End 36, Might 2, Hate 6, Armour 3d, Parry +2/+3): Math is compliant with TOR 2e Great Orc profiles. Fell abilities (*Snake-like Speed*, *Great Leap*, *Denizen of the Dark*, *Hideous Toughness*) match core mechanics.
- **Udûn Sniffers / Orc Guards / Soldiers / Drummers / Black Uruks**: Stat blocks follow official Attribute Level scaling.

---

## 5. Actionable Remediation Roadmap

1. **Purge Pregen TNs**: Run a structured find-and-replace across all 7 modular markdown files, replacing all `(Attribute TN: Torvir X, Einar Y, Khoril Z)` prompts with standardized `**SKILL roll**` or `**SKILL test**` notation.
2. **Restore Player Agency**: Reframe all scene presentations neutrally. Replace character-specific action prompts (e.g., "Khoril rolls Travel", "Einar disarms", "Torvir smashes") with open company choices and GM guidance.
3. **Cleanse Boxed Read-Aloud Descriptions**:
   - **Location 3**: Strip the mention of tripwires, scythe blades, and venom; describe only stripped racks, shadows, and debris.
   - **Location 7**: Remove the far-room detail of the lead tube; describe the heavy emerald mist and petrified forms looming near the entrance.
   - **Location 8**: Remove the historical explanation of how the goblins died; describe the ancient storehouse and desiccated remains.
4. **Purge "Daunted" & Non-Canon Terms**: Replace all instances of "Daunted" with canonical Shadow (Dread) gains, Hope loss, or the Miserable condition.
5. **Update Scripts & Master Build**: Ensure `scripts/build_master_document.py` and `scripts/build_handouts.py` cleanly recompile `armouries_of_the_third_deep_master.md` and HTML assets with zero errors.
