# Milestone 3 / R3 Work Report: Adversaries & Hazards Refactoring

**Agent**: `teamwork_preview_worker_m3_1`  
**Roles**: implementer, qa, specialist  
**Date**: 2026-08-25  
**Target Files Modified**:
- `03_adversaries_and_hazards.md`
- `05_adversaries_and_hazards.md`

---

## Summary of Changes

### 1. Adversary Stat Block Mathematical Certification & Unification
Both Chapter 3 (`03_adversaries_and_hazards.md`) and Chapter 5 (`05_adversaries_and_hazards.md`) were completely audited, unified, and brought into 100% compliance with *The One Ring 2nd Edition* core rules and *Moria: Through the Doors of Durin*:

* **The Mauler (Armoured Great Cave-Troll)**:
  - **Stats**: Attribute Level 10, Endurance 80 (Weary at 0 Hate), Might 2 (2 Wounds to kill; 2 actions/round), Hate 10, **Parry — (0)** (scrap plate is modeled by Armour 5d, completely eliminating the broken +5 Parry modifier), Armour 5d.
  - **Proficiencies**: Maul / Club 3d (Damage 8, Injury 16, Break Shield, Heavy Blow), Crush / Seize 3d (Damage 4/6, Injury 12, Seize), Scrap Shrapnel 2d (Damage 6, Injury 12, Ranged missile, Area burst).
  - **Fell Abilities**:
    - *Dull-Witted*: Player-heroes in Forward stance test **RIDDLE** (**Wits TN: Torvir 15, Einar 15, Khoril 16**), Favoured due to *Dull-Witted*. On success: loses 1 Hate base + 1 additional Hate per Success icon (6); Gandalf rune (G) loses full turn; 3 cumulative successes pacify or bypass.
    - *Hideous Toughness*: Reduces to 0 Endurance $\rightarrow$ Piercing Blow; surviving Protection resets Endurance to 40.
    - *Strike Fear*: Spend 1 Hate $\rightarrow$ **VALOUR** test vs **Heart TN** (Torvir 18, Einar 17, Khoril 16). Failure = 2 Shadow (Dread) + Daunted.
    - *Thick Hide*: Spend 1 Hate on Protection roll for +2d Armour (7d total).
    - *Scavenged Iron Carapace*: Weapon lodged on unpenetrated Piercing Blow unless **CRAFT** or **ATHLETICS** vs **Strength TN** (Torvir 13, Einar 14, Khoril 13) succeeds. Ballista hit strips plating (5d to 3d).

* **Grimnar the Disgraced (Great Orc Chieftain / Stalker)**:
  - **Stats**: Unified across both files to Attribute Level 6, **Endurance 36** (Weary at 0 Hate), **Might 2**, **Hate 6**, **Parry +2** (+3 when dual-wielding with stolen Dwarven dagger), **Armour 3d**.
  - **Proficiencies**: Heavy Scimitar 3d (Damage 5, Injury 16, Pierce, Break Shield), Stolen Dwarven Dagger 3d (Damage 4, Injury 14, Keen [Pierce on 9–10 / Eye]), Broad-headed Spear 2d (Damage 5, Injury 16, Pierce, Throwable).
  - **Fell Abilities**: *Denizen of the Dark*, *Hatred (Durin's Folk)* (+1d on attack rolls vs Dwarves), *Snake-like Speed* (Spend 1 Hate to make incoming attack Ill-favoured), *Great Leap* (Spend 1 Hate to leap over frontline / Shield-Wall to engage Rearward heroes), *Vengeful Strike* (Spend 1 Hate for immediate retaliation strike when hit), *Hideous Toughness* (survives Piercing Blow $\rightarrow$ resets to 18 End), *Fierce Command* (Spend 1 Hate to grant 2 Orcs immediate bonus attacks), *Hate Sunlight*, *Craven Ambush* (Piercing Blow on surprise), *Gleaming Dagger* (Famous Dagger of Durin recovery).
  - **Pursuit Check**: Replaced arbitrary TN 16 with **ATHLETICS** (**Strength TN: Torvir 13, Einar 14, Khoril 13**) or Ranged Attack vs Grimnar's Parry TN.

* **Grik the Skulker (Goblin Informant & Scout)**:
  - **Stats**: Unified to Attribute Level 3, **Endurance 12**, **Might 1**, **Hate 2**, **Parry +3**, **Armour 1d**.
  - **Proficiencies**: Jagged Knife 2d (Damage 3, Injury 12, Pierce on 10), Blown Bone-Darts / Slingshot 2d (Damage 2, Injury 10, Poison: Black Venom).
  - **Fell Abilities**: *Craven* (Valour check vs AL 3 on Endurance loss), *Sneak in Shadows* (Stealth Favoured, 0 Noise), *Snake-like Speed* (1 Hate makes incoming melee attack Ill-favoured), *Treacherous Bargain*.
  - **Detection & Social Matrix**:
    - Spotting: Opposed **SCAN** (**Wits TN: Torvir 15, Einar 15, Khoril 16**, Favoured for Einar).
    - Social Tests: **PERSUADE** (**Heart TN: Torvir 18, Einar 17, Khoril 16**), **ENHEARTEN** (**Heart TN**), **RIDDLE** (**Wits TN**), **AWE** (**Strength TN: Torvir 13, Einar 14, Khoril 13** / **Heart TN**).

* **Garrison & Sentry Squads**:
  - **Orc Soldiers**: AL 3, End 12, Might 1, Hate 3, Parry +1, Armour 2d; Orc-axe 2d (3/18, Break Shield), Short Bow 2d (3/14, Pierce); *Denizen of the Dark*, *Hate Sunlight*, *Craven*.
  - **Orc Guards**: AL 4, End 16, Might 1, Hate 4, Parry +2, Armour 3d; Heavy Scimitar 3d (4/16, Pierce), Heavy Spear 3d (4/14, Pierce); *Denizen of the Dark*, *Hate Sunlight*, *Thick Armour*, *Shield-Wall*.
  - **Udûn Sniffers**: AL 4, End 16, Might 1, Hate 4, Parry +0 (—), Armour 3d; Torch-staff 3d (4/14, Fiery Blow), Poisoned Blowdart / Bow 2d (2/12, Poison: Black Venom); *Denizen of the Dark*, *Heartless*, *Keen Scent* (+2d Awareness), *Hate Sunlight*.
  - **Orc Drummers**: AL 3, End 12, Might 1, Hate 3, Parry +1, Armour 2d; Curved Knife 2d (3/14, Pierce), Bone Drum-Beater 2d (3/12, Heavy Blow); *Denizen of the Dark*, *Hate Sunlight*, *Drums in the Deep* (Spend 1 Hate = +3 Strategic Eye Awareness, +2 Alert Points).
  - **Black Uruks**: AL 5, End 20, Might 1, Hate 5, Parry +2, Armour 3d; Broadsword 3d (4/16, Pierce), Bow of Horn 3d (3/14, Pierce); *Horrible Strength* (Spend 1 Hate $\rightarrow$ target Protection Ill-favoured), *Thick Armour*.
  - **Black Uruk Captain**: AL 6, End 24, Might 2, Hate 6, Parry +3, Armour 4d; Great Scimitar 3d (5/16, Break Shield, Pierce), Iron Javelin 2d (5/14, Pierce); *Horrible Strength*, *Yell of Triumph* (Spend 1 Hate $\rightarrow$ restore 1 Hate to all Orcs).

---

### 2. Full Hazard Mechanics & TOR 2e Integration
All subterranean hazards were formatted with complete mechanical rigor (Trigger, Primary Skill Test with Attribute TNs, Modifiers, Failure Consequences, and Degrees of Success [6, 66, Gandalf]):

1. **Balrog Toxic Miasma (*Breath of the Pit*)**:
   - Primary Test: **ENDURANCE / PROTECTION** (**Strength TN: Torvir 13, Einar 14, Khoril 13**) or **HEALING** (**Heart TN: Torvir 18, Einar 17, Khoril 16**).
   - Tiers: Unprotected (Ill-favoured, tested every minute in combat or exploration turn); Protected (tested hourly); Masterwork Respirators (4 hours complete immunity).
   - Degrees of Success: 6 = no Endurance loss + +1d to companion; 66 = clean air pocket; G = clear Weary or restore 1 Hope.
   - Respirators: **CRAFT** (**Strength TN**, $+1\text{d}$ in workshop; Skill Endeavour Resistance 3/4).
   - Flue Damper: **ATHLETICS** or **CRAFT** (**Strength TN**).
2. **Slag-Worm Tremors & Structural Collapses**:
   - Detection: **SCAN** (**Wits TN**, Favoured for Einar with *The Broken Key*).
   - Evasion: **PROTECTION TEST** (Armour dice vs Injury 16) or **ATHLETICS** (**Strength TN**). Failure: 20–30 Crushing Damage and Pinned (Weary).
   - Degrees of Success: 6 = 0 damage; 66 = pull companion clear; G = intact Dwarven arch.
   - Rubble Clearing: **ATHLETICS** (**Strength TN**) or Band **WAR** (3d vs Band TN 15).
3. **Scrap-Traps & Subterranean Pitfalls**:
   - Detection: **SCAN** (**Wits TN**, Favoured for Einar).
   - Disarm: **CRAFT** (**Strength TN**, $+1\text{d}$ invoking *Burglary* Trait).
   - Failure: 15 Damage, Moderate Poison, +2 Alert Points.
   - Degrees of Success: 6 = silent disarm + scrap parts; 66 = resets trap for foes; G = secret floor cache.
4. **Orc Desecration Idol**:
   - Test: **VALOUR** (**Heart TN: Torvir 18, Einar 17, Khoril 16**).
   - Modifiers: **LORE** (**Wits TN**) or **SONG** (**Heart TN**) grants $+1\text{d}$ to allies' tests.
   - Failure: 1 Shadow (Dread).
   - Degrees of Success: 6 = +1d on next attack vs Orcs; 66 = clear 1 Shadow; G = +1d to attacks and Protection for 1 round.
5. **Subterranean Water Perils**:
   - Complete Feat Die resolution table converted to Hero Attribute TNs (Valour/Healing vs Heart TN).

---

### 3. Terminology & Legacy Purge
- 0 arbitrary hero TNs remaining across both files.
- Purged all non-existent skills (`Sleight`, `Old Lore`, `Customs`, `Search`).
- Purged all D&D 5e phrasing (`Advantage / +2`, `saving throw`, `DC`, `Garrison Supply Points`).
