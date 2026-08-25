# Original User Request

## 2026-08-25T12:37:53Z

Refactor and strictly align the entire **Armouries of the Third Deep** adventure module suite for *The One Ring 2e* (TOR 2e) to adhere 100% to official core rules and *Moria: Through the Doors of Durin*. Eliminate all GM-assigned fixed TNs for player heroes (replacing them with character-sheet Attribute TNs [20 − Attribute], Risk/Consequences of Failure, Degrees of Success [$\mathbf{6}$ icons], Favoured/Ill-favoured states, bonus/penalty dice, and Skill Endeavours with Resistance ratings). Purge non-existent skills (like "Burglary", correctly treated as a Distinctive Feature) and fabricated mechanics (like "garrison supply points"). Access all project files directly without PowerShell.

Working directory: c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep
Integrity mode: development

## Core Rules Refactoring Directives

### 1. Target Number (TN) & Resolution Architecture
- **No Arbitrary Hero TNs**: Never assign fixed TNs (e.g. "TN 14", "TN 16") to Player-Hero tests. In TOR 2e, all hero test Target Numbers are derived directly from the character sheet:
  - **Strength TN** = $20 - \text{STR}$ (Torvir: 13, Einar: 14, Khoril: 13)
  - **Heart TN** = $20 - \text{HRT}$ (Torvir: 18, Einar: 17, Khoril: 16)
  - **Wits TN** = $20 - \text{WIT}$ (Torvir: 15, Einar: 15, Khoril: 16)
- **Official Difficulty Modifiers**: Adjust difficulty only through official TOR 2e mechanisms:
  - **Favoured / Ill-favoured**: Roll two Feat dice, keep the higher / lower result.
  - **Bonus / Penalty Dice**: Granting $\pm 1\text{d}$ or $\pm 2\text{d}$ to the roll.
  - **Skill Endeavours**: Multi-step complex tasks defined by **Resistance** (e.g. Resistance 3 to 9) and allowable attempts / consequences.
  - **Band Tests**: Band rolls roll Feat Die + Disposition rating against the Band's TN ($20 - \text{Readiness}$, which is TN 15 for Readiness 5).

### 2. Risk, Consequences & Degrees of Success
Every skill check presentation across all module files must follow the official TOR 2e format:
- **Skill Tested**: One of the 18 official skills (Awe, Athletics, Awareness, Hunting, Song, Craft, Enhearten, Travel, Insight, Healing, Courtesy, Battle, Persuade, Stealth, Scan, Explore, Riddle, Lore).
- **Condition / Modifiers**: Normal, Favoured, Ill-favoured, or $\pm 1\text{d}/\pm 2\text{d}$.
- **Consequence of Failure**: Specific narrative and mechanical price (Endurance loss, Weary condition, Shadow gain, +1 Alert/Noise Point, alarm triggered, broken lock, lost time).
- **Degrees of Success ($\mathbf{6}$ icons)**: Clear, tangible benefits for each Success icon rolled (e.g. doing it silently, cutting time in half, revealing hidden lore, recovering extra supplies, granting $+1\text{d}$ to an ally's subsequent check).

### 3. Skill & Trait Integrity
- Strictly enforce the official 18 skills. Ensure Distinctive Features (e.g. *Burglary*, *Enemy-lore (Orcs)*, *Fierce*, *Cunning*, *Wary*, *Leadership*) are correctly described as Traits that can be invoked to gain a bonus die ($+1\text{d}$) on applicable skill rolls (e.g. invoking *Burglary* on a **STEALTH**, **SCAN**, or **CRAFT** roll).
- Purge any fabricated terms, non-existent stats, or placeholder systems (e.g. "garrison supply points", "sleight skill").

## Requirements

### R1. Complete System Audit & Refactoring of Location Atlas
Refactor all 10 keyed locations in `02_keyed_locations.md` and `04_keyed_locations.md`:
- Replace all fixed TN prompts with official TOR 2e test blocks specifying: **Skill**, **Attribute Base**, **Modifiers (Favoured/Ill-favoured/Bonus Dice)**, **Consequences on Failure**, and **Success Icon ($\mathbf{6}$) Extra Effects**.
- Format complex actions (e.g. bypassing the King's Door, clearing toxic vents, fortifying the Upper Gatehouse) as formal **Skill Endeavours** with explicit Resistance ratings, allowed skills, and failure thresholds.

### R2. Refactoring of Delve Mechanics, Band Rules & Operational Systems
Audit and update `01_delve_mechanics_and_alert_system.md`, `02_band_mechanics.md`, and `03_operational_mechanics.md`:
- Ensure Band marching discipline uses Khoril's **TRAVEL** or **LEADERSHIP** (Wits/Heart TN) or Band **MANOEUVRE** (Band TN 15), with precise noise escalation rules on Failure and noise reduction on $\mathbf{6}$s.
- Clarify Balrog toxic gas (*Breath of the Pit*) exposure tests as **Protection / Endurance** rolls against the hero's Strength TN, specifying the exact effects of field respirators and herbs.

### R3. Adversary & Combat Proficiencies Certification
Audit and certify all stat blocks in `03_adversaries_and_hazards.md` and `05_adversaries_and_hazards.md`:
- Verify all adversary stats (The Mauler, Grimnar, Grik, Udûn Sniffers, Orc Soldiers/Guards) match official TOR 2e math (Attribute Level, Endurance, Might, Hate, Parry, Armour, Combat Proficiencies with Damage/Injury ratings, and Fell Abilities).
- Ensure *The Mauler*'s **Dull-Witted** Riddle combat task uses the hero's **RIDDLE** test (Wits TN) in Forward stance, removing 1 Hate per Success icon.

### R4. Relics, Relic Profiles & GM Play Aids Overhaul
Audit and update `04_loot_relics_and_rewards.md`, `06_relics_and_rewards.md`, `05_gm_screen_and_play_aids.md`, `07_gm_playbook_and_pacing.md`, and all `handouts/`:
- Ensure all Enchanted Rewards and Blessings on *Durin's Axe*, *Shield of the Deep Gate*, *Mattock of the Iron Vanguard*, and *Mail of Unyielding Stone* strictly use official TOR 2e mechanics (Favoured rolls, $+1\text{d}$ bonuses, Injury/Damage modifications, and Eye Awareness adjustments).
- Update the 1-Page Rapid GM Cheat Sheet (`handouts/gm_cheat_sheet.md`) and Band Worksheet (`handouts/band_worksheet.md`) to display the heroes' actual Attribute TNs (Torvir: STR 13/HRT 18/WIT 15; Einar: STR 14/HRT 17/WIT 15; Khoril: STR 13/HRT 16/WIT 16) and Band TN 15, with clear test matrices.

## Acceptance Criteria

### TOR 2e Rules Compliance & Mathematical Rigor
- [ ] Zero arbitrary hero Target Numbers (no "TN 14", "TN 16" on player tests); all tests reference the hero's Attribute TN.
- [ ] Every skill check in the module specifies Consequences of Failure and Extra Success Icon ($\mathbf{6}$) effects.
- [ ] Complex multi-step operations are formatted as formal Skill Endeavours with explicit Resistance scores.
- [ ] All 18 skills are valid TOR 2e skills; all Distinctive Features are properly designated as Traits.
- [ ] All fabricated terms (e.g. "garrison supply points") are completely removed.

### Verification
- [ ] Module documents and handouts are fully consistent, cross-referenced, and ready for immediate table use.
