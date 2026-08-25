# Survey Report: Delve Mechanics, Band Systems, Operational Rules & Campaign Context
**Module**: *The Armouries of the Third Deep* (The One Ring 2e / Moria: Through the Doors of Durin)  
**Surveyor Agent**: `teamwork_preview_explorer_survey_2`  
**Date**: 2026-08-25  
**Integrity Mode**: Read-Only Survey & Structural Audit

---

## 1. Executive Summary & Survey Scope

This report provides a comprehensive, systematic rules audit and refactoring specification for five foundational documents of *The Armouries of the Third Deep* adventure suite:
1. `01_delve_mechanics_and_alert_system.md` (Delve rules, 4-stage alert ladder, environmental hazards)
2. `02_band_mechanics.md` (Moria Band statistics, deployments, injury, fatigue, clashes)
3. `03_operational_mechanics.md` (Operational subsystems, sound economy, Eye Awareness, hazards)
4. `00_overview_and_background.md` (Adventure scope, narrative stakes, hero summaries)
5. `01_campaign_context.md` (Campaign chronicle, pre-gens, companion roster, relics, antagonists)

### Core Findings Summary
* **Fixed Hero Target Numbers (TNs)**: Multiple instances of arbitrary GM-assigned fixed TNs (e.g. `TN 14`, `TN 16`, `TN 12`) were found across all five files. Under *The One Ring 2e* (TOR 2e), all player-hero tests must strictly use character-sheet derived Attribute Target Numbers ($\mathbf{\text{TN}} = 20 - \text{Attribute}$).
* **Fabricated Mechanics & Terminology**: The term `+50 Garrison Supply Points` appears repeatedly as an artificial scorekeeper. It must be purged and replaced with authentic TOR 2e narrative, strategic, and Fellowship phase milestone outcomes.
* **Non-Existent Skills & 5e Tropes**: "Burglary" is frequently referred to as a rolled skill (e.g., `Burglary TN 14`), and D&D 5e phrasing (`+2 / Advantage`) appears in item and ability descriptions. In TOR 2e, *Burglary* is a Distinctive Feature (Trait) that grants $+1\text{d}$ or Inspiration when applied to official skills (**STEALTH**, **SCAN**, **CRAFT**), and advantage is represented by **Favoured** rolls (roll 2 Feat dice, keep the highest).
* **Band System Alignment**: The Band statistical core ($\text{Readiness } 5 \implies \text{TN } 15$, Dispositions: War 3, Vigilance 2, Manoeuvre 2, Expertise 2, Rally 1) is sound and compliant with *Moria: Through the Doors of Durin*. However, specific resolution prompts (such as marching tests, combat clashes, and first aid) need alignment with official TOR 2e test block standards.
* **Balrog Toxic Gas (*Breath of the Pit*)**: Poison exposure tests require standardized **Protection tests** against Hero **Strength TN**, with distinct mechanical tiers for Unprotected, Field Protected, and Masterwork Respirator states.

---

## 2. Complete Inventory of Fixed Hero TNs & Non-Standard Prompts

The table below catalogs all fixed TN violations and non-standard mechanical prompts identified across the surveyed files, along with the required TOR 2e compliant refactoring.

| # | File | Line(s) | Current Verbatim Text | Defect / Rule Violation | TOR 2e Compliant Replacement |
|---|------|---------|-----------------------|-------------------------|------------------------------|
| **1** | `00_overview_and_background.md` | 81 | `The Broken Key (+2 / Advantage on Scan rolls)` | D&D 5e terminology (`+2 / Advantage`). | Makes **SCAN** rolls **Favoured** (roll 2 Feat dice, keep higher). |
| **2** | `00_overview_and_background.md` | 82 | `Expedition Guide (TN 14), Leadership` | Fixed TN 14 for Guide test; flat skill reference. | Guide test uses **TRAVEL** (Heart TN 16) or **ENHEARTEN** (Heart TN 16), invoking *Leadership* Trait for $+1\text{d}$. |
| **3** | `00_overview_and_background.md` | 82 | `Battle Horn of the Realm (+1 Battle)` | Flat skill modifier (`+1 Battle`). | Grants $+1\text{d}$ on **BATTLE** rolls or Band **WAR** / **RALLY** rolls. |
| **4** | `01_campaign_context.md` | 40 | `(+50 Garrison Supply Points)` | Fabricated point system. | Equips Balin's vanguard, bolsters Safe Haven defense, and secures royal recognition from King Dáin. |
| **5** | `01_campaign_context.md` | 127 | `Grants a permanent +2 modifier / Advantage (roll 2 Feat dice, take the best) on all Scan rolls` | D&D 5e terminology (`+2 modifier / Advantage`). | Makes all **SCAN** rolls **Favoured** (roll 2 Feat dice, keep higher). |
| **6** | `01_campaign_context.md` | 128 | `Wind-proof Lantern: (+2 to Scan in darkness)` | Flat numeric bonus (`+2 to Scan`). | Grants $+1\text{d}$ on **SCAN** rolls in dark subterranean chambers. |
| **7** | `01_campaign_context.md` | 138 | `Journey Role: Guide (TN 14) / Squad Commander` | Fixed TN 14. | Journey Role: Guide (**TRAVEL** — Heart TN 16) / Squad Commander. |
| **8** | `01_campaign_context.md` | 164 | `Grants +1 to all Battle rolls made by Khoril or the Band` | Flat numeric bonus (`+1`). | Grants $+1\text{d}$ (or Favoured) on **BATTLE** rolls made by Khoril or Band **WAR** / **RALLY** rolls. |
| **9** | `01_campaign_context.md` | 165 | `Dwarven Strong Spirits: (+1 to Enhearten rolls)` | Flat numeric bonus (`+1`). | Grants $+1\text{d}$ on **ENHEARTEN** rolls. |
| **10** | `01_campaign_context.md` | 230 | `Gains +1d on all Burglary and Craft rolls` | "Burglary" treated as a skill. | Gains $+1\text{d}$ on **CRAFT** or **STEALTH** rolls when picking locks or disarming traps, or when invoking the *Burglary* Trait. |
| **11** | `01_campaign_context.md` | 302 | `+2 modifier / Advantage (roll 2 Feat dice, keep the highest) on all Scan and Burglary rolls` | 5e phrasing and "Burglary rolls". | Makes all **SCAN** rolls **Favoured**; allows invoking *Burglary* Trait for $+1\text{d}$ on lockpicking/trap **CRAFT** checks. |
| **12** | `01_campaign_context.md` | 308 | `Grants +1 to all Battle rolls` | Flat numeric bonus. | Grants $+1\text{d}$ on **BATTLE** rolls. |
| **13** | `01_delve_mechanics_and_alert_system.md` | 23 | `Stealth rolls are standard difficulty (TN 14).` | Fixed TN 14 on player tests. | Stealth tests are resolved against Hero **Wits TN** ($20 - \text{WIT}$: Torvir 15, Einar 15, Khoril 16) with standard dice. |
| **14** | `01_delve_mechanics_and_alert_system.md` | 97 | `March Test: Khoril rolls TRAVEL or LEADERSHIP (TN 14).` | Fixed TN 14; "Leadership" listed as a skill. | Khoril rolls **TRAVEL** (Heart TN 16) or **ENHEARTEN** (Heart TN 16), invoking *Leadership* Trait for $+1\text{d}$, OR Band tests **MANOEUVRE** (2d6 vs Band TN 15). |
| **15** | `01_delve_mechanics_and_alert_system.md` | 121 | `stabilized post-battle with HEALING TN 14` | Fixed TN 14. | Stabilized post-battle with **HEALING** (Heart TN: Torvir 18, Einar 17, Khoril 16) or Band **EXPERTISE** (2d vs Band TN 15). |
| **16** | `01_delve_mechanics_and_alert_system.md` | 136 | `Must roll Protection / Endurance every 1 Minute (TN 16).` | Fixed TN 16; non-existent "Endurance roll". | Each hero makes an Ill-favoured **Protection test** (Armour/Protection dice + Feat Die) against their **Strength TN** ($20 - \text{STR}$) every minute. |
| **17** | `01_delve_mechanics_and_alert_system.md` | 143 | `Test Endurance only once per 1 Hour (TN 14).` | Fixed TN 14; non-existent "Endurance roll". | Heroes make a standard **Protection test** against their **Strength TN** once per hour. |
| **18** | `01_delve_mechanics_and_alert_system.md` | 148 | `Endeavour: Resistance 4, TN 14` | Fixed TN 14 on Skill Endeavour. | Skill Endeavour: **Resistance 4**, tested with **CRAFT** (Strength TN) or **HEALING** (Heart TN). |
| **19** | `01_delve_mechanics_and_alert_system.md` | 156 | `Everyone in the zone must test ATHLETICS (TN 14).` | Fixed TN 14. | Everyone tests **ATHLETICS** (Strength TN: Torvir 13, Einar 14, Khoril 13). |
| **20** | `01_delve_mechanics_and_alert_system.md` | 162 | `passive SCAN (TN 12)` | Fixed passive TN 12 (5e concept). | Einar tests **SCAN** (Wits TN 15), Favoured via *The Broken Key*. |
| **21** | `02_band_mechanics.md` | 137 | `padded with cloth (Craft TN 14)` | Fixed TN 14. | Padded with cloth (**CRAFT** — Strength TN: Torvir 13, Einar 14, Khoril 13). |
| **22** | `02_band_mechanics.md` | 138 | `+50 Garrison Supply Points` | Fabricated mechanic. | Securely equips Balin's frontline vanguard and secures royal recognition. |
| **23** | `02_band_mechanics.md` | 194 | `Requires First Aid (Healing TN 14)` | Fixed TN 14. | Requires First Aid (**HEALING** — Heart TN: Torvir 18, Einar 17, Khoril 16) or Band **EXPERTISE** (2d vs Band TN 15). |
| **24** | `02_band_mechanics.md` | 290 | `Khoril can roll Battle (TN 14) or Enhearten (TN 14)` | Fixed TN 14. | Khoril rolls **BATTLE** (Strength TN 13) or **ENHEARTEN** (Heart TN 16), invoking *Leadership* Trait for $+1\text{d}$. |
| **25** | `02_band_mechanics.md` | 336 | `Command (Khoril): Khoril rolls Battle (TN 14)` | Fixed TN 14. | Khoril rolls **BATTLE** (Strength TN 13 / Heart TN 16). |
| **26** | `02_band_mechanics.md` | 337 | `Inspire (Torvir or Khoril): Roll Enhearten (TN 14)` | Fixed TN 14. | Hero rolls **ENHEARTEN** (Heart TN: Torvir 18, Khoril 16). |
| **27** | `02_band_mechanics.md` | 338 | `rolling their personal Combat Proficiency against TN 13 + Enemy Might` | Fixed TN 13 + Might resolution. | Attack rolls use Hero's Combat Proficiency against **Strength TN** modified by standard combat stance and adversary Parry. |
| **28** | `03_operational_mechanics.md` | 57 | `Sentries suffer a -2 penalty to passive Awareness` | 5e flat modifier. | Sentries suffer $-1\text{d}$ to Awareness; Heroes gain $+1\text{d}$ on **STEALTH** / **EXPLORE** rolls. |
| **29** | `03_operational_mechanics.md` | 76 | `Athletics (TN 16) test` | Fixed TN 16. | **ATHLETICS** (Strength TN, Ill-favoured or at $-1\text{d}$). |
| **30** | `03_operational_mechanics.md` | 189, 210, 215 | `Craft TN 15 respirators` / `(Craft TN 15)` | Fixed TN 15 on Craft. | Skill Endeavour: **Resistance 3**, tested with **CRAFT** (Strength TN) or Band **EXPERTISE** (2d vs Band TN 15). |
| **31** | `03_operational_mechanics.md` | 203, 206 | `Roll Endurance / Healing EVERY MINUTE` | Non-existent "Endurance roll". | **Protection test** against **Strength TN** ($20 - \text{STR}$). |
| **32** | `03_operational_mechanics.md` | 216 | `Herbal Treatments (Healing TN 14)` | Fixed TN 14. | **HEALING** (Heart TN: Einar 17, Khoril 16, Torvir 18). |
| **33** | `03_operational_mechanics.md` | 218 | `Craft TN 16 or Athletics TN 16` | Fixed TN 16. | **CRAFT** or **ATHLETICS** (Strength TN, Ill-favoured). |
| **34** | `03_operational_mechanics.md` | 235 | `Athletics (TN 14) test` | Fixed TN 14. | **ATHLETICS** (Strength TN). |
| **35** | `03_operational_mechanics.md` | 256 | `Valour test (TN 14)` | Fixed TN 14 on Valour. | Valour roll (Feat Die + Valour rating) against **Heart TN** or **ENHEARTEN** (Heart TN). |

---

## 3. Audit of Band Systems & Marching Discipline

### 3.1 Band Statistical Foundations
* **Band Readiness Rating**: **5** (Base 4 + 1 for Hardened Veteran Dúrmer).
* **Band Readiness TN**: **15** ($\mathbf{\text{Band TN}} = 20 - \text{Readiness} = 20 - 5 = 15$).
* **Band Dispositions**:
  * **WAR**: 3 (3d6) — Melee combat clashes, shield-walls, forcing barricades.
  * **VIGILANCE**: 2 (2d6) — Perimeter watches, spotting ambushes, acoustic scouting.
  * **MANOEUVRE**: 2 (2d6) — Silent marching, stealth group transit, fighting withdrawals.
  * **EXPERTISE**: 2 (2d6) — Crafting respirators, lockpicking, trap disarming, first aid.
  * **RALLY**: 1 (1d6) — Morale recovery, resisting Dread, fatigue checks.
* **Resolution Formula**: Roll **1 Feat Die + Success Dice equal to Disposition Rating** against **Band TN 15**.

### 3.2 Marching Discipline & Group Transit Architecture
Marching tests occur whenever the Fellowship and companion Band move between major halls or traverse hostile sectors:
* **Primary March Test**:
  * **Leader Check**: Khoril rolls **TRAVEL** (Heart TN 16) or **ENHEARTEN** (Heart TN 16), invoking the *Leadership* Trait for $+1\text{d}$.
  * **Alternative Band Check**: The GM rolls Band **MANOEUVRE** (2d6) against **Band TN 15**.
* **Noise Escalation & Consequences of Failure**:
  * **Failure**: Clanking wargear or loose stone echoes through the flues: **+1 Noise / Alert Point**.
  * **Eye of Sauron ($\mathbf{S}$)**: A dropped pry-bar or slipped shield echoes loudly (**+2 Noise / Alert Points**), and immediately triggers a wandering patrol check.
* **Degrees of Success & Noise Reduction on $\mathbf{6}$s**:
  * **Success**: Column moves silently; **+0 Noise Points** generated.
  * **Success Icons ($\mathbf{6}$)**:
    * **1 Success Icon ($\mathbf{6}$)**: The squad steps perfectly in cadence, reducing current ambient suspicion (**-1 Noise / Alert Point**), or granting **+1d** to the Point Scout's next **AWARENESS** / **SCAN** test.
    * **2+ Success Icons ($\mathbf{6}\mathbf{6}$)**: The squad discovers an ancient dwarven maintenance crawlway, completely bypassing an encounter zone or reducing Alert Points by **-2**.
    * **Gandalf Rune ($\mathbf{G}$)**: Flawless stealth; column passes unseen, resetting any imminent patrol trigger.

### 3.3 Four Tactical Squad Roles
1. **Forward Scout Screen** (*Austri & Bróga*): Rolls Band **VIGILANCE** (2d) or **MANOEUVRE** (2d) vs Band TN 15. Prevents ambushes; enables Einar to make **Favoured SCAN** checks.
2. **Shield-Wall Phalanx** (*Dúrmer, Dolg, Bláin*): Rolls Band **WAR** (3d) vs Band TN 15. Dolg/Dúrmer intercepts 1 attack/round; spending $\mathbf{6}$s pushes enemy ranks back.
3. **Rearguard Choke Point Defense** (*Bláin & Fáin*): Fortifies Location 2 (Upper Gatehouse). Secures escape line, grants $+1\text{d}$ on withdrawal tests, and can trigger keystone collapse.
4. **Heavy Salvage Porter Squad** (*Hjoldring & Dúrmer + 2 companions*): Hauls up to 50 suits of mail and wargear. Shifts Band Burden to **Heavy** ($-1\text{d}$ to Manoeuvre and Fatigue checks; $+1$ Noise Point per hall unless padded via **CRAFT** [Strength TN]).

### 3.4 Mass Combat (Band Clashes) & Hero Leader Actions
Band combat is resolved via the **Band Clash** subsystem:
* **Band Stances**:
  * *Aggressive*: Ill-favoured Clash roll; deals $+1$ extra Resistance reduction on success.
  * *Balanced*: Standard dice pools.
  * *Guarded*: Favoured Clash roll; ignores first enemy Special Damage trigger.
  * *Fleeing*: Band **MANOEUVRE** (2d) vs Band TN 15 + Foe Might to disengage.
* **Hero Leader Actions**:
  * **Command (Khoril)**: Khoril rolls **BATTLE** (Strength TN 13 / Heart TN 16). Success grants $+1\text{d}$ to the Band Clash roll and allows mid-round stance adjustments.
  * **Inspire (Torvir or Khoril)**: Hero rolls **ENHEARTEN** (Heart TN: Torvir 18, Khoril 16). Success restores 1 point of Band Hope or clears *Faltering*.
  * **Fight (Torvir or Einar)**: Hero attacks in standard stance using Combat Proficiency against their **Strength TN** (Torvir 13, Einar 14). Success reduces enemy Resistance by weapon damage.
  * **Duel (Torvir)**: Torvir engages the enemy Champion in single combat, nullifying the Champion's Might penalty on the Band Clash roll.
* **Clash Roll**: GM rolls Band **WAR** (3d6) against $\mathbf{\text{Band TN 15}} + \text{Enemy Might}$. Enemy War Parties have Resistance ratings: Patrol (Resistance 3, Might 0), Pack (Resistance 6, Might 1), Warband (Resistance 9, Might 2), Horde (Resistance 12, Might 3).

---

## 4. Audit of Balrog Toxic Gas (*Breath of the Pit*) & Hazards

### 4.1 Hazard Profile: The Breath of the Pit
Preserved within **Location 7 (The Poisoned Halls)** and **Location 8 (The Upper Armoury)** is the heavy, sulfurous volcanic vapor exhaled by Durin's Bane.

```
========================================================================================
                          BREATH OF THE PIT: EXPOSURE MATRIX
========================================================================================
 STATUS                 TEST REQUIRED & RATE             CONSEQUENCE ON FAILURE
----------------------------------------------------------------------------------------
 Unprotected            Protection test vs Strength TN   Lose 4 Endurance and gain 1 
 (Raw breathing)        EVERY MINUTE (Ill-favoured)       Shadow (Dread). On Eye (S): 
                                                         Poisoned condition (collapse).
----------------------------------------------------------------------------------------
 Field Protected        Protection test vs Strength TN   Lose 2 Endurance (Weary). 
 (Vinegar cloth/herbs)  EVERY HOUR (Standard roll)       On Eye (S): Suffer Severe Poison.
----------------------------------------------------------------------------------------
 Masterwork Respirator  IMMUNE FOR 4 HOURS               No checks required for 4 hours.
 (Crafted filter masks)
========================================================================================
```

### 4.2 Countermeasures & Remedies
1. **Masterwork Respirators**:
   * *Resolution*: Formal **Skill Endeavour** — **Resistance 3** (or Band **EXPERTISE** 2d vs Band TN 15).
   * *Allowed Skills*: **CRAFT** (Strength TN: Torvir 13, Einar 14, Khoril 13), invoking *Burglary* or *Smith* Traits for $+1\text{d}$.
   * *Outcome*: Provides 4 hours of complete immunity for up to 10 characters.
2. **Field Precautions (Dwarf-Herbs & Cloth)**:
   * *Resolution*: **HEALING** (Heart TN: Einar 17, Khoril 16, Torvir 18) or **CRAFT** (Strength TN).
   * *Outcome*: Downgrades exposure from Unprotected (every minute, Ill-favoured) to Protected (every hour, standard roll).
3. **Unjamming the Overhead Flue Damper**:
   * *Resolution*: **CRAFT** or **ATHLETICS** (Strength TN: Torvir 13, Einar 14, Khoril 13), made **Ill-favoured** (or at $-1\text{d}$) due to rusted iron.
   * *Outcome*: Vents the chamber in 3 combat rounds, but generates **+3 Noise Points** on the Alert Tracker.

### 4.3 Other Subterranean Hazards
* **Slag-Worms / Ceiling Collapse**:
  * *Trigger*: Explosive noise (Khoril's horn, troll impacts) or sledgehammers.
  * *Test*: **ATHLETICS** (Strength TN: Torvir 13, Einar 14, Khoril 13) or **Protection test** (4d vs Strength TN).
  * *Failure*: Suffer 20 Damage and become Pinned (Weary). Extraction requires **ATHLETICS** (Strength TN) or Band **WAR** (3d vs Band TN 15).
* **Subterranean Water Perils**:
  * Drinking from untested springs triggers a Feat Die roll. Tests against foul water use **Protection tests** against **Strength TN** or **ENHEARTEN** (Heart TN) against spiritual dread.

---

## 5. Inventory of Fabricated Mechanics & Terminology Purge

### 5.1 "Garrison Supply Points" Purge
* **Problem**: The term `+50 Garrison Supply Points` is used in 14 locations across the module suite as an artificial video-game-like metric.
* **Refactoring**: Replace `+50 Garrison Supply Points` with official narrative and mechanical milestones:
  * **Equipping Balin's Vanguard**: Provides 40 suits of gromril-mail and masterwork dwarf-weapons, outfitting Balin's frontline warriors and eliminating the colony's defensive vulnerability.
  * **Safe Haven Security**: Upgrades the defensive rating of the Caves of Thrym Thistlebeard and the East-Gate Camp, securing them against Orc counter-attacks.
  * **Royal Recognition from King Dáin**: Combined with Durin's Axe, the wargear serves as undeniable physical proof that secures a full royal expedition of 500 Dwarf veterans from the Lonely Mountain.
  * **Fellowship Phase Milestone**: Awards the Company **Treasure / Prestige** and grants special Undertakings during the subsequent Fellowship Phase.

### 5.2 Purging Non-Existent Skills & 5e Tropes
* **Burglary**: Purge all instances of `Burglary (TN 14)` or `Burglary rolls`. Einar and Bróga possess the *Burglary* Distinctive Feature (Trait). In TOR 2e, Traits are invoked to gain a **bonus die (+1d)** or inspiration on standard skills (**STEALTH**, **SCAN**, or **CRAFT**).
* **Leadership**: Purge `LEADERSHIP (TN 14)` as a skill check. Khoril possesses the *Leadership* Trait, which is invoked on **ENHEARTEN**, **TRAVEL**, or **BATTLE** rolls.
* **Advantage & Flat Numeric Modifiers**:
  * Replace `+2 / Advantage` with **Favoured** (roll 2 Feat dice, keep the highest).
  * Replace flat skill ratings (`+1 Battle`, `+1 Enhearten`, `+2 Scan`) with **+1d bonus dice** or **Favoured** conditions.
* **Endurance & Valour Checks**: Replace non-standard "Endurance rolls" with **Protection tests** (Armour dice + Feat Die) against **Strength TN**, and "Valour checks (TN 14)" with **ENHEARTEN** (Heart TN) or official Shadow/Dread tests.

---

## 6. Milestone 2 (R2) Concrete Refactoring Guidance

To implement Milestone 2 (R2), the following specific text edits and structural refactorings should be applied to `01_delve_mechanics_and_alert_system.md`, `02_band_mechanics.md`, and `03_operational_mechanics.md`.

### 6.1 Refactoring `01_delve_mechanics_and_alert_system.md`
1. **Section 1 (Alert Ladder)**:
   * Line 23: Replace `Stealth rolls are standard difficulty (TN 14).` with `Stealth tests are resolved against Hero Wits TN (Torvir 15, Einar 15, Khoril 16) with standard dice.`
2. **Section 3.1 (Marching Discipline)**:
   * Lines 96–102: Replace the march test block with:
     ```markdown
     * **March Test**: Khoril rolls **TRAVEL** (Heart TN 16) or **ENHEARTEN** (Heart TN 16), invoking his *Leadership* Trait for **+1d**, OR the GM rolls Band **MANOEUVRE** (2d6) against **Band TN 15**.
       * **Success**: The squad moves silently in the shadows of the pillars (**+0 Noise Points**).
       * **Success Icons (6s)**: Each 6 rolled reduces ambient suspicion by **-1 Noise Point** (stepping in rhythm to muffle gear), or grants **+1d** to the Point Scout's next check.
       * **Failure**: Clanking mail or loose gravel echoes down the galleries (**+1 Alert Point**).
       * **Gandalf Rune (G)**: The squad discovers an ancient maintenance flue, completely bypassing the next encounter zone.
       * **Eye of Sauron (S)**: A shield clatters loudly on stone (**+2 Alert Points**) and immediately triggers a wandering scout patrol.
     ```
3. **Section 3.3 (Band Casualties)**:
   * Line 121: Replace `HEALING TN 14` with `HEALING (Heart TN: Torvir 18, Einar 17, Khoril 16) or Band EXPERTISE (2d vs Band TN 15)`.
4. **Section 4 (Environmental Hazards)**:
   * Lines 135–150: Update the Breath of the Pit box to specify **Protection tests** against Hero **Strength TN** ($20 - \text{STR}$: Torvir 13, Einar 14, Khoril 13) every 1 minute (Ill-favoured) for Unprotected, and once per 1 hour (standard roll) for Protected. Update Dwarf Remedy to a formal Skill Endeavour: **Resistance 4** using **CRAFT** (Strength TN) or **HEALING** (Heart TN).
   * Line 156: Replace `ATHLETICS (TN 14)` with `ATHLETICS (Strength TN: Torvir 13, Einar 14, Khoril 13)`.
   * Line 162: Replace `passive SCAN (TN 12)` with `SCAN (Wits TN 15), Favoured via The Broken Key`.

### 6.2 Refactoring `02_band_mechanics.md`
1. **Section 2.1–2.4 (Squad Roles)**:
   * Line 104: Replace `+2 / Advantage on Scan` with `Favoured on SCAN rolls`.
   * Line 137: Replace `Craft TN 14` with `CRAFT (Strength TN: Torvir 13, Einar 14, Khoril 13)`.
   * Line 138: Replace `+50 Garrison Supply Points` with `equips 50 frontline Dwarves in Balin's vanguard with gromril-mail and masterwork weapons`.
2. **Section 3.2 (Injury Tiers)**:
   * Line 194: Replace `Healing TN 14` with `HEALING (Heart TN: Torvir 18, Einar 17, Khoril 16) or Band EXPERTISE (2d vs Band TN 15)`.
3. **Section 4.1 (Stealth & Marching Tests)**:
   * Lines 287–294: Align text with Khoril's **TRAVEL** (Heart TN 16) / **ENHEARTEN** (Heart TN 16) with *Leadership* Trait ($+1\text{d}$) or Band **MANOEUVRE** (2d vs Band TN 15), with noise escalation (+1 AP on failure, +2 on Eye) and noise reduction on $\mathbf{6}$s.
4. **Section 5.2 (Hero Leader Actions)**:
   * Line 336: Replace `Battle (TN 14)` with `BATTLE (Strength TN 13 / Heart TN 16)`.
   * Line 337: Replace `Enhearten (TN 14)` with `ENHEARTEN (Heart TN: Torvir 18, Khoril 16)`.
   * Line 338: Replace `TN 13 + Enemy Might` with Hero Combat Proficiency against **Strength TN** (modified by stance and enemy Parry).

### 6.3 Refactoring `03_operational_mechanics.md`
1. **Section 1.1 (Alert Profiles)**:
   * Line 57: Replace `-2 penalty to passive Awareness` with `-1d to sentry Awareness; +1d to hero STEALTH / EXPLORE`.
   * Line 76: Replace `Athletics (TN 16)` with `ATHLETICS (Strength TN, Ill-favoured or -1d)`.
2. **Section 3.1 (Balrog Neurotoxic Miasma)**:
   * Lines 201–219: Replace "Endurance / Healing" rolls with **Protection tests** against **Strength TN** ($20 - \text{STR}$).
   * Lines 215–216: Replace `Craft TN 15` with a Skill Endeavour (**Resistance 3**, **CRAFT** [Strength TN] or Band **EXPERTISE** [2d vs Band TN 15]). Replace `Healing TN 14` with **HEALING** (Heart TN).
   * Line 218: Replace `Craft TN 16 or Athletics TN 16` with `CRAFT or ATHLETICS (Strength TN, Ill-favoured)`.
3. **Section 3.2–3.3 (Collapses & Water Perils)**:
   * Line 235: Replace `Athletics (TN 14)` with `ATHLETICS (Strength TN)`.
   * Line 256: Replace `Valour test (TN 14)` with `ENHEARTEN (Heart TN) or Protection test vs Strength TN`.

---

## 7. Cross-Referenced Hero & Band Sheet Reference Matrix

For immediate reference during Milestone 2 (R2) refactoring, the authoritative Hero and Band statistics are consolidated below:

```
========================================================================================================
                                     AUTHORITATIVE RESOLUTION MATRIX
========================================================================================================
 ENTITY               STRENGTH TN    HEART TN       WITS TN        KEY TRAITS / SPECIAL MECHANICS
--------------------------------------------------------------------------------------------------------
 Torvir Hammerstone   TN 13 (STR 7)  TN 18 (HRT 2)  TN 15 (WIT 5)  Fierce, Willful, Enemy-lore (Orcs)
                                                                   Great Axe (Dmg 8, Inj 20, Pierce 9-10)
--------------------------------------------------------------------------------------------------------
 Einar son of Anar    TN 14 (STR 6)  TN 17 (HRT 3)  TN 15 (WIT 5)  Cunning, Wary, Burglary (Trait: +1d)
                                                                   The Broken Key (Favoured on SCAN)
--------------------------------------------------------------------------------------------------------
 Khoril Hornblower    TN 13 (STR 7)  TN 16 (HRT 3)* TN 16 (WIT 4)  Wary, Cunning, Leadership (Trait: +1d)
                                     *Prowess Virtue               Battle-horn (+1d Battle/Rally, +1 AP/+2 Eye)
========================================================================================================
 BAND PROFILE:        BAND TN 15 (20 - Readiness 5)
 DISPOSITIONS:        WAR: 3d6 | VIGILANCE: 2d6 | MANOEUVRE: 2d6 | EXPERTISE: 2d6 | RALLY: 1d6
========================================================================================================
```

---
*Report compiled and certified for Milestone 2 implementation.*
