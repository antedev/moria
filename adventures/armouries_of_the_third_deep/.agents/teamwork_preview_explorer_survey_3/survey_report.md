# Comprehensive System Survey Report: Adversaries, Hazards, Relics, GM Aids & Handouts
### Investigation for Milestones 3 & 4 (R3 & R4 Refactoring)
**Inspector**: `teamwork_preview_explorer_survey_3`  
**Date**: 2026-08-25  
**Working Directory**: `c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep/.agents/teamwork_preview_explorer_survey_3`

---

## Executive Summary

A comprehensive read-only survey was conducted across all 9 assigned files in the *Armouries of the Third Deep* adventure suite:
- `03_adversaries_and_hazards.md` & `05_adversaries_and_hazards.md` (Adversaries & Hazards)
- `04_loot_relics_and_rewards.md` & `06_relics_and_rewards.md` (Relics & Rewards)
- `05_gm_screen_and_play_aids.md` & `07_gm_playbook_and_pacing.md` (GM Screen & Pacing Playbook)
- `handouts/gm_cheat_sheet.md`, `handouts/band_worksheet.md`, `handouts/dying_scribe_letter.md` (Player & GM Handouts)

### Key Survey Discoveries & Systematic Deficiencies:
1. **Widespread Fixed TN Violations**: GM-assigned fixed TNs (e.g., TN 12, TN 14, TN 15, TN 16) pervade adversary fell abilities (Strike Fear TN 14, Scavenged Carapace TN 14, Craven TN 14), environmental hazards (Balrog Miasma TN 14, Collapses TN 14, Pitfalls TN 14), skill challenges, and GM reference sheets. All player checks must be converted to character Attribute TNs (Torvir: STR 13/HRT 18/WIT 15; Einar: STR 14/HRT 17/WIT 15; Khoril: STR 13/HRT 16/WIT 16) or Band TN 15.
2. **Adversary Mathematical Discrepancies & Contradictions**: Substantial contradictions exist between Chapter 3 summary blocks and Chapter 5 detailed stat blocks (e.g., Grimnar Endurance 36 vs 32, Parry +2 vs +6; Grik AL 3 vs AL 2/3, Endurance 12 vs 8/12; Orc Soldiers AL 4 vs AL 3; Orc Guards AL 5 vs AL 4). Mathematical balance must be unified strictly against official TOR 2e core rules and *Moria: Through the Doors of Durin*.
3. **The Mauler's "Dull-Witted" Riddle Duel Alignment**: While the combat task is well-conceived, it currently includes arbitrary TN 14 text in Chapter 5 and lacks explicit "(Wits TN)" specification in Chapter 3 and handouts.
4. **Fabricated Mechanics & Trait Violations**: Non-canonical mechanics (specifically "+50 Garrison Supply Points") appear in relic logs, hoard inventories, and handouts. "Burglary" is frequently referenced as a skill with assigned TNs rather than as a Distinctive Feature (Trait) granting bonus dice ($+1\text{d}$) to applicable skills (Scan, Stealth, Craft).
5. **Relic & Enchanted Reward Mechanics**: Relics (*Durin's Axe*, *Shield of the Deep Gate*, *Mattock of the Iron Vanguard*, *Mail of Unyielding Stone*) feature strong narrative flavor but require strict alignment to TOR 2e Enchanted Qualities (*Keen*, *Grievous*, *Fell*, *Reinforced*, *Cunning Make*, *Rune-scored*) and official Eye Awareness / Hunt mechanics (+4 Eye Awareness upon claiming the Axe).

---

## 1. Mathematical & Rules Audit of Adversaries (R3)

### 1.1 Apex Adversary: The Mauler (Armoured Great Cave-Troll)
- **Current State**:
  - `03_adversaries_and_hazards.md` (lines 13–42): AL 10, End 80, Might 2, Hate 10, Parry —, Armour 5. Crush 3 (6/12, Seize), Maul 3 (8/16, Break Shield).
  - `05_adversaries_and_hazards.md` (lines 85–117): AL 10, End 80, Might 2, Hate 10, Parry 5 (claims +5 from scrap plating). Maul 3d (8/16), Seize 3d (4/6, 12), Scrap Shrapnel 2d (6/12).
- **TOR 2e Mathematical Audit & Violations**:
  - **Parry**: In TOR 2e, Cave-trolls have Parry `—` (0). Giving a troll Parry +5 drastically breaks the math: a hero attacking with Strength TN 13 would need an 18 to hit. The scrap armor is already modeled by **Armour 5d** (which rolls 5 Protection dice against Piercing Blows). Troll Parry must be set to `—`.
  - **Endurance & Might**: AL 10, Endurance 80 ($10 \times 8$), Might 2, Hate 10 are 100% compliant with TOR 2e Troll math.
  - **Fell Ability — Strike Fear**: Incorrectly specifies "VALOUR test (TN 14)" in both files. In TOR 2e, Strike Fear forces all heroes within sight to make a **VALOUR** test against their own **Heart TN** (Torvir: 18, Einar: 17, Khoril: 16).
  - **Fell Ability — Scavenged Iron Carapace**: Incorrectly requires "Craft or Athletics test (TN 14)". Must be a **CRAFT** or **ATHLETICS** test against the hero's **Strength TN**.
  - **Fell Ability — Dull-Witted**: Must explicitly state: "Player-heroes in Forward stance can use their main combat action to attempt a **RIDDLE** test (**Wits TN**). On a success, The Mauler loses 1 Hate, plus 1 additional Hate per Success icon ($\mathbf{6}$) rolled. 3 cumulative successes pacify or bypass the creature."

### 1.2 Archfoe: Grimnar the Disgraced (Great Orc Chieftain / Stalker)
- **Current Contradictions & Audit**:
  - **Endurance**: `03` states **36**; `05` states **32**. Standard TOR 2e Great Orc Chieftain (AL 6) Endurance is $6 \times 6 = \mathbf{36}$. Unify to **36** (Weary at 0 Hate).
  - **Might**: `03` states **2**; `05` states **1 (or Might 2 in Apex Ambush)**. Reconcile to **Might 2** (takes 2 Wounds to kill; 2 actions per round).
  - **Hate**: Reconcile to **6** (or 7 in full vengeance mode).
  - **Parry**: `03` states **+2**; `05` states **6 (+3 Base + 3 from dual-wielding)**. A Parry of +6 makes Torvir need 19 and Einar need 20 to hit. In TOR 2e, Orc Chieftains have Parry +2 (or +3 with an off-hand parrying dagger). Set Parry to **+2** (or +3 when dual-wielding).
  - **Armour**: **3d** (Reinforced Orc Mail).
  - **Combat Proficiencies**:
    - *Heavy Scimitar*: 3d (Damage 5, Injury 16, Pierce / Break Shield).
    - *Stolen Dwarven Dagger*: 3d (Damage 4, Injury 14, Keen [Pierce on 9–10]). Reconcile damage from 3 to 4.
    - *Broad-headed Spear*: 2d (Damage 5, Injury 16, Pierce, Throwable).
  - **Fell Abilities**: *Denizen of the Dark*, *Hatred (Durin's Folk)* (Favoured attacks vs Torvir and Khoril), *Snake-like Speed* (Spend 1 Hate to make incoming attack Ill-favoured), *Great Leap* (Spend 1 Hate to bypass Shield-Wall), *Vengeful Strike* (Spend 1 Hate to deliver free retaliation strike when hit), *Hideous Toughness* (resets to 18).
  - **Pursuit Check**: In `05` line 289, "Athletics (TN 16) or Ranged Attack (TN 16)" must be replaced by **ATHLETICS** (**Strength TN**) or Ranged Attack vs Grimnar's Parry TN.

### 1.3 Goblin Informant: Grik the Skulker
- **Current Contradictions & Audit**:
  - `03` lists AL 3, End 12, Might 1, Hate 2, Parry +3, Armour 1d.
  - `05` lists AL 2 (or AL 3), End 8 (or 12), Might 1, Hate 2 (or 3), Parry 4 (+1 Base + 3), Armour 1d (or 2d).
  - **Unified Standard**: **Attribute Level 3**, **Endurance 12**, **Might 1**, **Hate 2**, **Parry +3**, **Armour 1d**.
  - **Proficiencies**: Jagged Knife 2d (Damage 3, Injury 12, Pierce on 10), Blown Bone-Darts / Slingshot 2d (Damage 2, Injury 10/12, Moderate Poison).
  - **Fell Abilities**: *Craven* (flees when wounded), *Sneak in Shadows* (Stealth rolls Favoured, 0 Noise), *Snake-like Speed*.
  - **Detection & Social Matrix**: Replace all fixed TNs (Scan TN 16, Persuade TN 14, Enhearten TN 14, Riddle TN 14, Awe TN 14) with hero Attribute TNs:
    - Detecting Grik: Opposed **SCAN** test (**Wits TN**).
    - Social Negotiation: **PERSUADE** (**Heart TN**), **ENHEARTEN** (**Heart TN**), **RIDDLE** (**Wits TN**), **AWE** (**Strength TN** / **Heart TN**).

### 1.4 Garrison Ranks & Squad Adversaries
Reconcile the severe discrepancies between `03` and `05`:

| Adversary Type | Unified AL | Endurance | Might | Hate | Parry | Armour | Primary Attacks & Proficiencies | Key Fell Abilities |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| **Orc Soldier** | 3 | 12 | 1 | 3 | +1 | 2d | Orc-axe 2d (Dmg 3, Inj 18, Break Shield)<br>Short Bow 2d (Dmg 3, Inj 14) | *Denizen of the Dark*, *Hate Sunlight*, *Craven* |
| **Orc Guard** | 4 | 16 | 1 | 4 | +2 | 3d | Heavy Scimitar 3d (Dmg 4, Inj 16, Pierce)<br>Heavy Spear 3d (Dmg 4, Inj 14, Pierce) | *Denizen of the Dark*, *Hate Sunlight*, *Thick Armour* (+1d Armour) |
| **Udûn Sniffer** | 4 | 16 | 1 | 4 | +0 | 3d | Torch-staff 3d (Dmg 4, Inj 14, Fiery Blow)<br>Blowdart / Bow 2d (Dmg 2/3, Inj 12, Poison) | *Denizen of the Dark*, *Heartless*, *Keen Scent* (+2d Awareness), *Black Venom* |
| **Orc Drummer** | 3 | 12 | 1 | 3 | +1 | 2d | Curved Knife 2d (Dmg 3, Inj 14, Pierce)<br>Drum-Beater 2d (Dmg 3, Inj 12) | *Denizen of the Dark*, *Hate Sunlight*, *Drums in the Deep* (1 Hate = +3 Eye) |
| **Black Uruk** | 5 | 20 | 1 | 5 | +2 | 3d | Broadsword 3d (Dmg 4, Inj 16, Pierce)<br>Bow of Horn 3d (Dmg 3, Inj 14) | *Horrible Strength* (Ill-favoured Protection), *Thick Armour* |
| **Black Uruk Captain** | 6 | 24 | 2 | 6 | +3 | 4d | Great Scimitar 3d (Dmg 5, Inj 16, Break Shield)<br>Iron Javelin 2d (Dmg 5, Inj 14) | *Horrible Strength*, *Yell of Triumph* (Restores 1 Hate to allies) |

---

## 2. Environmental Hazard Mechanics Audit (R3)

### 2.1 Balrog Toxic Miasma (*Breath of the Pit*) (Locations 7 & 8)
- **Current Issues**:
  - `03` line 134 lists "ENDURANCE TN 14 hourly w/ masks".
  - `05` lines 508–530 lists fixed Craft TN 14/15, Athletics TN 16 / Craft TN 16.
- **TOR 2e Refactored Mechanics**:
  - **Exposure Checks**: Heroes make an **ENDURANCE / PROTECTION** test against their **Strength TN** (Torvir: 13, Einar: 14, Khoril: 13) or **HEALING** test against **Heart TN**.
  - **Unprotected Exposure**: Check every exploration turn (or 1 minute in combat), Ill-favoured. Failure = lose Endurance equal to Feat die; Eye of Sauron ($\mathbf{S}$) = 0 Endurance & Dying.
  - **Protected Exposure (Herbs/Vinegar cloths)**: Check every hour. Failure = lose 1–6 Endurance; Eye of Sauron ($\mathbf{S}$) = Severe Poison.
  - **Masterwork Respirator Masks**: Constructed via **CRAFT** test (**Strength TN**, $+1\text{d}$ if using workshop tools in Location 5/8; or Skill Endeavour). Grants 4 hours of absolute immunity.
  - **Venting Overhead Flue**: **ATHLETICS** or **CRAFT** (**Strength TN**). Success clears the chamber in 3 rounds ($+3$ Noise Points).

### 2.2 Slag-Worm Tremors & Structural Collapses
- **Current Issues**: `03` line 135 lists "ATHLETICS TN 14", "SCAN TN 12"; `05` line 544–552 lists "Scan TN 14", "Athletics TN 14", "Athletics TN 16".
- **TOR 2e Refactored Mechanics**:
  - **Detection**: **SCAN** (**Wits TN**, Favoured for Einar with *The Broken Key*).
  - **Evasion**: **ATHLETICS** (**Strength TN**) or **PROTECTION** roll (Armour dice).
  - **Clearing Rubble**: **ATHLETICS** (**Strength TN**) or Band **WAR** roll (3d) against **Band TN 15**.

### 2.3 Scrap-Traps & Subterranean Pitfalls (Location 3)
- **Current Issues**: `03` line 136 and `05` line 568 list "SCAN TN 14", "CRAFT TN 12/14".
- **TOR 2e Refactored Mechanics**:
  - **Spotting Traps**: **SCAN** (**Wits TN**, Favoured for Einar).
  - **Disarming Traps**: **CRAFT** (**Strength TN**, $+1\text{d}$ invoking *Burglary* Trait).
  - **Failure**: Triggers scythe/pitfall (Damage 15, Moderate Poison, $+2$ Noise Points).

### 2.4 Orc Desecration Idol (Location 4)
- **Current Issues**: `03` line 137 lists "VALOUR TN 14", "LORE TN 12"; `05` line 597 lists "Valour TN 14".
- **TOR 2e Refactored Mechanics**:
  - **Dread Aura**: **VALOUR** test against **Heart TN** (Torvir: 18, Einar: 17, Khoril: 16).
  - **Reciting Ancient Litanies**: **LORE** (**Wits TN**) or **SONG** (**Heart TN**) grants $+1\text{d}$ to allies' Valour tests.

---

## 3. Relics, Relic Profiles & Loot Tables Audit (R4)

### 3.1 Durin's Axe (The Royal Heirloom of Khazad-dûm)
- **Weapon Type**: Great Axe (Two-handed) | Damage 9 (Base 7 + Superior Grievous +2) | Injury 20 | Load 4.
- **TOR 2e Enchanted Qualities & Virtues**:
  1. *Rune-Scored*: Attack rolls made with Durin's Axe are **Favoured**. (Purge flat "+1 Feat die" text in 06 line 79).
  2. *Superior Grievous*: Increases weapon Damage by $+2$ (Total Damage 9).
  3. *Superior Keen*: Scores a Piercing Blow on a Feat die result of **8, 9, or 10**.
  4. *Flame of Hope*: Radiant cold azure fire illuminates 30 ft (negating total darkness penalties). Wielder may spend 1 Hope to grant all allies $+1\text{d}$ on attack rolls and Protection tests for 1 round or clear Faltering.
  5. *Gleam of Terror*: The wielder's **AWE** rolls for *Intimidate Foe* combat tasks are automatically **Favoured**; on a success, target loses 2 Hate/Resolve and minions of AL $\le 4$ flee to rear rank. (Replaces arbitrary "Valour test TN 16").
  6. *The Weight of Doom*: Lifting the axe increases **Strategic Eye Awareness by +4 immediately**.

### 3.2 Masterwork Tunnel-Guard Relics
- **Shield of the Deep Gate**: Reinforced Great Shield | Parry modifier $+3$ | Load 3. Qualities: *Reinforced* (Unbreakable), *Cunning Make*. Virtue (*Unyielding*): Bearer cannot be knocked down or seized by Huge creatures in Forward/Defensive stance; $+1\text{d}$ to Band War rolls in Shield-Wall.
- **Mattock of the Iron Vanguard (Mattock of Moria-Silver)**: Two-handed Mattock | Damage 8 (Base 7 + Grievous +1) | Injury 18/20 | Load 3. Qualities: *Grievous*, *Close Fitting*, *Superior Craftsmanship*. Virtue (*Gleaming Edge*): Attacks against subterranean foes are **Favoured**; enemy Protection rolls suffer $-1\text{d}$; $+2\text{d}$ to Craft/Athletics/Band War checks to shatter stone barriers.
- **Mail of Unyielding Stone**: Coat of Mail | Protection 5d | Load 12 (Base 16 with *Close Fitting* $-4$). Qualities: *Close Fitting*, *Reinforced*. Virtue (*Impenetrable*): Spend 1 Hope on failed Protection roll to downgrade injury severity by one tier; takes half damage from falling rock/crush hazards.
- **Stolen Dagger of Durin**: Dagger | Damage 4 | Injury 14 | Load 0. Qualities: *Keen* (Pierce 9–10), *Luminous Starlight* (glows near Orcs/Trolls, negates darkness penalties).
- **Helm of the Iron Watch**: Dwarven Helm | Protection $+1\text{d}$ | Load 1. Virtue (*Vigilant Sentinel*): **Favoured** on Awareness and Scan underground; immune to drop ambushes.
- **Pike of the Under-Gate**: Long Spear / Pike (Two-handed) | Damage 5 | Injury 16 | Load 3. Qualities: *Keen*, *Grievous*, *Foe-Piercer* (allows melee attack from behind Defensive ally; strikes first on enemy charges).

### 3.3 Skill Endeavour: Cracking the King's Door (`06` Section 4.3)
- **Current Issues**: Treats "Burglary" as a skill (lines 265, 274); assigns fixed TNs (Scan TN 14, Craft TN 15, Burglary TN 15, Riddle TN 16, Athletics TN 14).
- **TOR 2e Refactoring**:
  - **Structure**: Formal Skill Endeavour, **Resistance 6**, **Time Limit 3 Turns**.
  - **Turn 1 (Tumbler Alignment)**: **SCAN** or **CRAFT** (**Wits TN / Strength TN**). Einar's *Broken Key* grants Favoured status; Bróga adds $+1\text{d}$.
  - **Turn 2 (Deadfall Bypass)**: **CRAFT** (**Strength TN**, $+1\text{d}$ if invoking Trait *Burglary*) or **RIDDLE** (**Wits TN**). Complication on failure = $+2$ Noise Points.
  - **Turn 3 (Forcing Gromril Tumbler)**: **CRAFT** or **ATHLETICS** (**Strength TN**) or Band **EXPERTISE** roll (2d vs Band TN 15). Torvir can spend 1 Hope to grant $+1\text{d}$.

### 3.4 Purging Fabricated Mechanics ("Garrison Supply Points")
- **Occurrences**:
  - `06_relics_and_rewards.md`: lines 30, 299, 341.
  - `07_gm_playbook_and_pacing.md`: lines 32, 227, 377.
  - `handouts/gm_cheat_sheet.md`: line 169.
  - `handouts/band_worksheet.md`: lines 15, 116.
- **Refactoring Solution**: Completely remove "+50 Garrison Supply Points". Replace with canonical narrative and mechanical rewards:
  - Equipping 50 frontline Dwarves of Balin's colony with dwarf-mail, shields, and masterwork weapons.
  - Securing the Upper Mansions against counter-attacks.
  - Providing royal material proof for King Dáin Ironfoot in Erebor, securing 500 veteran reinforcements in 2990 TA.
  - Awarding $+4$ Adventure Points, $+3$ Skill Points, and $+2$ Fellowship Score.

### 3.5 D66 Scavenge Table Modernization (`04` & `06`)
- Replace flat "+1 / +2" modifiers with official TOR 2e bonus dice ($+1\text{d}$) or Favoured states:
  - Entry 16 (04): Lock-picks grant $+1\text{d}$ to Craft rolls when invoking *Burglary*.
  - Entry 44 (04): Dried healing roots allow an immediate **HEALING** test (**Heart TN**).
  - Entry 62 (04): Rusted key grants Favoured status on Einar's next Scan roll.
  - Entry 33 (06): Torn page grants $+1\text{d}$ on Scan rolls to locate hidden vault chests.
  - Entry 46 (06): Severed troll-claw grants $+1\text{d}$ to **AWE** on *Intimidate Foe*.
  - Entry 62 (06): Mouthpiece grants $+1\text{d}$ to **BATTLE** rolls.

---

## 4. GM Screen, Playbook & Handout Files Audit (R4)

### 4.1 1-Page Rapid GM Cheat Sheet (`handouts/gm_cheat_sheet.md` & `05` §1)
- **Current Issues**:
  - Lacks a dedicated Hero Attribute TN reference block.
  - All 10 area summary entries list fixed TNs (e.g., Area 1: Stealth TN 14, Area 6: Riddle TN 14, Area 7: Endurance TN 14).
  - Adversary combat profiles list outdated/inconsistent numbers and Strike Fear (2 Shadow) without Heart TN.
- **Refactoring Blueprint**:
  1. Add **Player-Hero Quick-Reference Block**:
     - **Torvir Hammerstone**: STR 7 (TN 13) | HRT 2 (TN 18) | WIT 5 (TN 15) | Parry 15 | Mail 5d | Axe 3d (8/20, Pierce 9–10)
     - **Einar son of Anar**: STR 6 (TN 14) | HRT 3 (TN 17) | WIT 5 (TN 15) | Parry 20 | Mail 3d | Sword 3d (4/16, Keen) | *Broken Key* (Favoured Scan)
     - **Khoril Hornblower**: STR 7 (TN 13) | HRT 3 (TN 16 via Prowess) | WIT 4 (TN 16) | Parry 17 | Mail 3d | Axe 3d (6/18) | *Battle-horn* (+1d Battle)
     - **Band Readiness**: 5 (Band TN 15)
  2. Convert all 10 Area rows from fixed TNs to Skill (Attribute TN) format with Failure Consequences and $\mathbf{6}$-icon benefits.
  3. Reconcile Adversary Combat Reference table with verified stats (Grimnar End 36, Parry +2; Grik AL 3, End 12, Parry +3; The Mauler Parry —, etc.).

### 4.2 Band Management Worksheet (`handouts/band_worksheet.md` & `05` §2)
- **Current Issues**:
  - Step 2 Leader Actions (lines 137–140) list incorrect fixed TN 14s (e.g., Khoril Battle TN 14 instead of Heart TN 16; Enhearten TN 14 instead of Heart TN 16; Einar Scan TN 14 instead of Wits TN 15).
  - Contains references to "+50 Supply" in expedition headers and squad descriptions.
- **Refactoring Blueprint**:
  1. Embed the complete Hero Attribute TN Matrix directly into the header.
  2. Update Step 2 Hero Leader Actions:
     - **Khoril**: Command (**BATTLE** [Heart TN 16] $\rightarrow$ $+1\text{d}$ to Clash) | Inspire (**ENHEARTEN** [Heart TN 16] $\rightarrow$ $+1$ Hope / clear Faltering).
     - **Torvir**: Fight (Great Axe **STRENGTH TN 13** $+$ Adversary Parry) | Duel (Single combat vs Champion, negates Might penalty).
     - **Einar**: Fight (Sword **STRENGTH TN 14** $+$ Adversary Parry) | Flank / Lockpick (**SCAN / CRAFT** [Wits TN 15 / Strength TN 14], $+1\text{d}$ invoking *Burglary*).
  3. Purge all "+50 Supply" text.

### 4.3 GM Playbook & Pacing (`07_gm_playbook_and_pacing.md`)
- **Current Issues**:
  - Turn-by-turn notes throughout Acts I, II, and III contain numerous fixed TNs (Travel TN 14, Scan +2, Craft TN 14, Craft TN 16, Burglary TN 14, Valour TN 14, Old Lore TN 14, etc.).
  - Section 3 Hero Spotlight Matrix (lines 250–263) contains "Burglary Mastery", "Squad Guide (TN 14)", "The Broken Key (+2 / Adv)".
  - Contains "+50 Garrison Supply Points" in lines 32, 227, 377.
- **Refactoring Blueprint**:
  1. Replace all fixed TN prompts with official Skill (Attribute TN) format.
  2. Fix Trait terminology: *Burglary* is a Distinctive Feature (Trait) used with Scan/Craft/Stealth; *The Broken Key* grants **Favoured** rolls on Scan; *Battle-horn* grants $+1\text{d}$ to Battle.
  3. Replace "+50 Garrison Supply Points" with canonical colony rewards.

### 4.4 The Dying Scribe's Slate (`handouts/dying_scribe_letter.md`)
- **Current Issues**:
  - Section 4 (lines 126–142) contains fixed TNs: "Lore / Scan (TN 12)", "Craft / Healing (TN 14)", "Riddle / Old Khuzdul (TN 14)", "see Craft TN 15 mask".
- **Refactoring Blueprint**:
  - Convert Section 4 skill checks to:
    - **LORE / SCAN** (**Wits TN**, Favoured for Einar with *The Broken Key*).
    - **CRAFT** (**Strength TN**) / **HEALING** (**Heart TN**).
    - **RIDDLE** (**Wits TN**, Khoril invoking *Old Khuzdul* lore).
    - Reference Craft (Strength TN) for respirator masks.

---

## 5. Concrete Refactoring Guidance for Milestones 3 & 4

### Milestone 3 (R3: Adversaries & Hazards) Execution Plan:
1. **Adversary Stat Blocks Alignment (`03` & `05`)**:
   - Ensure every stat block displays: Attribute Level, Endurance, Might, Hate, Parry, Armour, Combat Proficiencies (Rank, Damage, Injury, Special Damage), and Fell Abilities.
   - Set The Mauler's Parry to `—` (scrap plating modeled via Armour 5d).
   - Set Grimnar's Endurance to 36, Might to 2, Parry to +2, Dagger Damage to 4.
   - Set Grik's AL to 3, Endurance to 12, Parry to +3.
   - Set Udûn Sniffers, Orc Soldiers, Orc Guards, Drummers, and Black Uruks to verified canonical profiles.
   - Refactor all Fell Abilities to use hero Attribute TNs (**VALOUR** vs Heart TN for Strike Fear; **CRAFT/ATHLETICS** vs Strength TN for Scavenged Carapace).
2. **The Mauler's "Dull-Witted" Riddle Duel**:
   - Refactor both files to explicitly use: **RIDDLE** test (**Wits TN**) in Forward stance; success removes 1 Hate $+$ 1 Hate per Success icon ($\mathbf{6}$); 3 successes pacify the troll.
3. **Hazard Matrices & Rules Refactoring (`03` & `05`)**:
   - Format every environmental hazard with: **Trigger**, **Primary Skill Test (Attribute TN)**, **Modifiers (Favoured/Ill-favoured/Bonus Dice)**, **Consequences on Failure**, and **Degrees of Success ($\mathbf{6}$ icons)**.

### Milestone 4 (R4: Relics, GM Aids & Handouts) Execution Plan:
1. **Relic & Hoard Profiles (`04` & `06`)**:
   - Durin's Axe: Great Axe (Two-handed, 9/20/4), *Rune-Scored* (Favoured attacks), *Superior Grievous* (+2 Dmg), *Superior Keen* (Pierce 8–10), *Flame of Hope* (30 ft light, +1d on Hope spend), *Gleam of Terror* (Favoured Awe / Intimidate Foe), *The Weight of Doom* (+4 Eye Awareness).
   - Tunnel-Guard Relics: Fully specify *Shield of the Deep Gate*, *Mattock of Moria-Silver*, *Mail of Unyielding Stone*, *Helm of the Iron Watch*, *Pike of the Under-Gate*.
   - Purge "+50 Garrison Supply Points" across all chapters and handouts.
   - Refactor the Lockbreaker Skill Endeavour in `06` (Resistance 6, Time Limit 3 Turns, hero Attribute TNs, *Burglary* Trait $+1\text{d}$).
   - Modernize D66 Scavenge Tables to use TOR 2e $+1\text{d}$ and Favoured modifiers.
2. **GM Playbook & Screen Overhaul (`05` & `07`)**:
   - Strip all fixed TNs from session notes, room summaries, and adversary matrices.
   - Embed Hero Attribute TN tables into `05` and `07`.
3. **Handouts Overhaul (`handouts/gm_cheat_sheet.md`, `band_worksheet.md`, `dying_scribe_letter.md`)**:
   - Embed Hero Attribute TN blocks (Torvir: STR 13/HRT 18/WIT 15; Einar: STR 14/HRT 17/WIT 15; Khoril: STR 13/HRT 16/WIT 16) and Band TN 15.
   - Purge fixed TNs and "+50 Supply Points" from all three handout files.
