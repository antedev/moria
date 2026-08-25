# Master Survey Report: Location Atlas Audit & TOR 2e Refactoring
## *The Armouries of the Third Deep* Adventure Suite
**Audited Files**:
- `02_keyed_locations.md`
- `04_keyed_locations.md`
- `handouts/node_map.md`
- *Cross-referenced with `handouts/gm_cheat_sheet.md`, `handouts/band_worksheet.md`, `00_overview_and_background.md`*

---

## 1. Executive Summary

A comprehensive, line-by-line audit of the Location Atlas across `02_keyed_locations.md`, `04_keyed_locations.md`, and `handouts/node_map.md` was conducted to certify strict adherence to *The One Ring 2nd Edition* (TOR 2e) core rules and *Moria: Through the Doors of Durin*.

### Key Survey Findings
1. **Pervasive Fixed/Arbitrary Hero TNs**: Over 45 distinct instances of fixed target numbers (e.g., `TN 12`, `TN 14`, `TN 15`, `TN 16`) are assigned directly to Player-Hero skill rolls across the Location Atlas. In TOR 2e, GM-assigned fixed TNs do not exist; all Player-Hero test Target Numbers are strictly derived from character-sheet Attribute TNs: $\text{TN} = 20 - \text{Attribute}$.
2. **Non-Existent Skills & Trait Conflation**:
   - **`Burglary`** is repeatedly presented as a skill test (e.g., `Burglary TN 14`, `Burglary TN 16`, `Burglary 14`) rather than an official Distinctive Feature (Trait) that grants $+1\text{d}$ to an official skill roll (**STEALTH**, **CRAFT**, or **SCAN**).
   - **`Sleight`** (`02_keyed_locations.md:134`) is an invented non-TOR skill, which must be refactored to **STEALTH** or **CRAFT**.
   - **`Old Lore`** is used extensively in place of the official skill **LORE** (Wits).
   - **`Customs`** (`handouts/node_map.md:307`) is a legacy 1e skill, which must be refactored to **COURTESY** (Heart), **PERSUADE** (Wits), or **RIDDLE** (Wits).
   - **`Dread`**, **`Greed`**, and **`Catwalks`** are incorrectly listed as skills in test headers and summary matrices.
3. **Flat Numerical Modifiers**: Multiple instances use non-TOR flat numerical bonuses (e.g., `Einar rolls with +2`, `Advantage / +2`, `+1 to all Battle rolls`). In TOR 2e, modifiers are strictly **Favoured / Ill-favoured** (rolling 2 Feat dice) or bonus/penalty dice ($\pm 1\text{d}$ or $\pm 2\text{d}$).
4. **Missing Consequences of Failure & Degrees of Success**: The vast majority of skill checks lack explicit mechanical prices for failure (Endurance loss, Weary, Shadow gain, Alert/Noise step) and offer no structured benefits for rolling Success icons ($\mathbf{6}$ and $\mathbf{6}\mathbf{6}$).
5. **Unstructured Multi-Step Operations**: Major set-piece actions (breaching the King's Door, clearing the toxic gas flue, crafting respirators, fortifying the Upper Gatehouse, preparing siege artillery, and disarming the scythe scrap-trap array) require conversion into formal **Skill Endeavours** with explicit Resistance ratings ($3, 6$) and round/time limits.
6. **Fabricated Mechanics**: Repeated references to `+50 Garrison Supply Points` must be purged and replaced with authentic Moria campaign rewards (Dwarven Wargear Caches, Treasure Points, Band Hope, Colony Armament, and Royal Renown for King Dáin).

---

## 2. Hero Attribute TN & Resolution Reference Matrix

In TOR 2e, Player-Heroes test against their individual Attribute Target Numbers:

$$\text{Attribute TN} = 20 - \text{Attribute Rating}$$

### Pre-Generated Fellowship Attribute TNs
| Hero | Culture & Calling | STRENGTH (TN) | HEART (TN) | WITS (TN) | Distinctive Features / Key Traits |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Torvir Hammerstone** | Dwarf of Durin (*Champion*) | **STR 7 (TN 13)** | **HRT 2 (TN 18)** | **WIT 5 (TN 15)** | *Enemy-lore (Orcs)*, *Fierce-Minded*, *Curse of Vengeance* |
| **Einar son of Anar** | Dwarf of Iron Hills (*Treasure Hunter*) | **STR 6 (TN 14)** | **HRT 3 (TN 17)** | **WIT 5 (TN 15)** | *Burglary*, *Durin's Way*, *Dragon-sickness*, *The Broken Key* |
| **Khoril Hornblower** | Dwarf of Durin (*Captain*) | **STR 7 (TN 13)** | **HRT 4 (TN 16)** | **WIT 4 (TN 16)** | *Leadership*, *Wary*, *Lure of Power*, *Battle-horn of the Realm* |
| **Band Baseline** | Balin's Vanguard Band | **Readiness 5 (Band TN 15)** | **Band Hope: 12** | **Band Shadow: 1** | *Dispositions: War 3d, Vigilance 2d, Manoeuvre 2d, Expertise 2d, Rally 1d* |

### The 18 Official TOR 2e Skills & Governing Attributes
| Attribute | Official Skills (6 per Attribute) |
| :--- | :--- |
| **STRENGTH** | **Awe**, **Athletics**, **Awareness**, **Hunting**, **Song**, **Craft** |
| **HEART** | **Enhearten**, **Travel**, **Insight**, **Healing**, **Courtesy**, **Battle** |
| **WITS** | **Persuade**, **Stealth**, **Scan**, **Explore**, **Riddle**, **Lore** |

---

## 3. Location-by-Location Comprehensive Survey & Refactoring Specifications

---

### Location 1: The Mustering-Yard (Crossroads of the Deep)
* **Elevation**: Upper Tier (Level 3A)
* **Role**: Infiltration Landing & Crossroads
* **Connections**: North (Vertical Shaft to Thrym's Haven), South (Granite Arch to Loc 2), East (Smuggler's Crawlway to Loc 3)
* **Baseline Threat**: Alert Tier 0 (*Quiet Shadows*); 2 Udûn Sniffers behind Pillar #4, Grik in north drainage slit.

#### Violations & Errata Found
1. `02_keyed_locations.md:82`: `Stealth Infiltration (STEALTH TN 14)` -> Fixed TN 14.
2. `02_keyed_locations.md:83`: `Ambush Assault (BATTLE TN 14)` -> Fixed TN 14.
3. `02_keyed_locations.md:84`: `Scan the Pavilion (SCAN TN 14 / Einar with Broken Key rolls with +2)` -> Fixed TN 14; flat "+2" modifier.
4. `04_keyed_locations.md:140`: `Explore TN 14` -> Fixed TN 14 (East crawlway bypass).
5. `04_keyed_locations.md:182`: `Scan (TN 14)` -> Fixed TN 14; `Einar's The Broken Key: Grants +2 modifier / Advantage`.
6. `04_keyed_locations.md:184`: `Stealth (TN 14) / Band Manoeuvre (2d6 vs TN 15)` -> Fixed TN 14 for heroes.
7. `04_keyed_locations.md:186`: `Battle / Old Lore (TN 14)` -> Fixed TN 14; non-existent skill `Old Lore`.
8. `04_keyed_locations.md:187`: `Persuade / Riddle (TN 14)` -> Fixed TN 14.
9. `04_keyed_locations.md:192`: `Khoril rolls Battle (TN 14)` -> Fixed TN 14.
10. `04_keyed_locations.md:202`: `Scan TN 14` -> Fixed TN 14.

#### Refactored TOR 2e Mechanical Blocks
* **Perimeter Infiltration — STEALTH (Wits TN)**:
  * *Target Number*: Wits TN (Torvir 15, Einar 15, Khoril 16).
  * *Modifiers*: Alert Tier 0 grants $+1\text{d}$; massive basalt pillars provide total cover.
  * *Consequence of Failure*: A companion's boot or shield clips an iron brazier stanchion, generating **$+1\text{ Noise Point}$** and alerting the sniffing hounds.
  * *Degrees of Success ($\mathbf{6}$ icons)*:
    * $\mathbf{6}$: The Company moves like smoke across the basalt floor; generates **$0\text{ Noise}$** and grants $+1\text{d}$ to the lead hero's next test in Location 2 or 3.
    * $\mathbf{6}\mathbf{6}$: Flawless silent infiltration; bypasses the sentries completely and identifies the optimal rear ambush angle.
* **Overlook Sentry Scouting — SCAN (Wits TN)**:
  * *Target Number*: Wits TN (Torvir 15, Einar 15, Khoril 16).
  * *Modifiers*: Einar invoking *The Broken Key* rolls **Favoured** (roll two Feat dice, keep higher).
  * *Consequence of Failure*: The sentry post is not spotted before entering open ground; Company loses surprise round if combat starts.
  * *Degrees of Success ($\mathbf{6}$ icons)*:
    * $\mathbf{6}$: Discovers the 2 Udûn Sniffers dozing behind Pillar #4, notes their bone-dice distraction, and spots Grik the Skulker hiding in the northern drainage slit.
    * $\mathbf{6}\mathbf{6}$: Also uncovers the discarded Orc message scroll regarding friction between Malech and Thu the Firespeaker.
* **Ancient Scorch Analysis — LORE or BATTLE (Wits TN or Heart TN)**:
  * *Target Number*: Wits TN (Lore) or Heart TN (Battle).
  * *Modifiers*: Torvir invoking *Enemy-lore (Orcs)* or *Dwarven Lore* gains $+1\text{d}$.
  * *Consequence of Failure*: Inconclusive inspection; wastes 10 minutes.
  * *Degrees of Success ($\mathbf{6}$ icons)*:
    * $\mathbf{6}$: Confirms the scorch marks are vitrified Balrog footprints from 1980 T.A. and identifies the engineered Dwarven defensive kill-zones across the plaza.
* **Parley with Grik the Skulker — PERSUADE or RIDDLE (Wits TN)**:
  * *Target Number*: Wits TN (Torvir 15, Einar 15, Khoril 16).
  * *Modifiers*: Offering Dwarf tobacco or 5 silver pennies grants $+1\text{d}$.
  * *Consequence of Failure*: Grik panics and darts into his 6-inch drainage chute, hissing a warning to the sentries ($+1\text{ Noise}$).
  * *Degrees of Success ($\mathbf{6}$ icons)*:
    * $\mathbf{6}$: Grik shares vital intelligence (Grimnar is stalking Level 3C; the Marshal's Key was taken down to Goblin Village) and provides a crude charcoal sketch of Location 3's tripwires.
* **Marching Discipline — TRAVEL or ENHEARTEN (Heart TN)**:
  * *Target Number*: Heart TN (Khoril 16), invoking *Leadership* Trait ($+1\text{d}$).
  * *Consequence of Failure*: The 10-Dwarf squad makes clattering noise ($+1\text{ Noise Point}$).
  * *Degrees of Success ($\mathbf{6}$ icons)*:
    * $\mathbf{6}$: Complete silence across the 100-pace plaza ($0\text{ Noise}$).

---

### Location 2: The Upper Gatehouse (The Shattered Threshold)
* **Elevation**: Upper Tier (Level 3A)
* **Role**: Fortified Forward Rally Point & Extraction Redoubt
* **Connections**: North (Mustering-Yard), South (Sloping Ramp to Loc 3), Murder-Hole Parapets
* **Baseline Threat**: Alert Tier 0; structural strain, overhead keystone trap.

#### Violations & Errata Found
1. `02_keyed_locations.md:99`: `Fortify the Gatehouse (CRAFT TN 14)` -> Fixed TN 14.
2. `02_keyed_locations.md:100`: `Spot Overhead Slag-Worm (AWARENESS TN 14)` -> Fixed TN 14.
3. `04_keyed_locations.md:257`: `Craft (TN 14) / Band Expertise (2d6 vs TN 15)` -> Fixed TN 14.
4. `04_keyed_locations.md:259`: `Craft (TN 16) / Battle (TN 14)` -> Fixed TN 16 and TN 14.
5. `04_keyed_locations.md:261`: `Explore (TN 14)` -> Fixed TN 14; `Einar +2 from The Broken Key`.
6. `04_keyed_locations.md:278`: `Gatehouse Armoire: Burglary TN 14 to open; Bróga gains +1d` -> Non-existent skill `Burglary TN 14`.

#### Refactored TOR 2e Mechanical Blocks
* **Skill Endeavour: Fortifying the Forward Redoubt (Resistance 3)**:
  * *Context*: Bracing the buckled adamant blast-doors with cedar balks, iron pitons, and granite blocks.
  * *Resistance*: **3**. Each test represents 10 minutes of disciplined labor.
  * *Allowed Skills*: **CRAFT** (Strength TN), **ATHLETICS** (Strength TN), **BATTLE** (Heart TN).
  * *Modifiers*: Hjoldring (*Smith*) or Fáin assisting grants $+1\text{d}$; Dúrmer (*Mighty*) grants $+1\text{d}$.
  * *Consequence of Failure*: Sledgehammer slips or timber creaks loudly ($+1\text{ Noise Point}$ per failed attempt); if unfinished after 3 attempts, the barricade is partial (+1 Parry instead of Total Cover).
  * *Degrees of Success ($\mathbf{6}$ icons)*:
    * $\mathbf{6}$: Contributes 2 points of Resistance.
    * $\mathbf{6}\mathbf{6}$: Contributes 3 points of Resistance (completes the endeavour in a single 10-minute turn!).
  * *Outcome on Success*: Establishes the Gatehouse as a **Fortified Forward Redoubt**. Rearguard garrison (Bláin & Fáin) receives **Total Cover (+3 Parry, immune to lower missile fire)** and adds **$+2\text{ Band Readiness}$** to the final Fighting Withdrawal.
* **Rigging the Keystone Winch Trap — CRAFT or BATTLE (Strength TN or Heart TN)**:
  * *Target Number*: Strength TN (Craft) or Heart TN (Battle).
  * *Modifiers*: Ill-favoured if attempted in pitch darkness without lantern light.
  * *Consequence of Failure*: The rusted winch jams or slips, dropping iron flakes ($+1\text{ Noise}$) and requiring a reset.
  * *Degrees of Success ($\mathbf{6}$ icons)*:
    * $\mathbf{6}$: Rigs a hair-trigger trip-rope. During withdrawal, triggering the trap is a free combat reaction, dropping 3 tons of granite (**30 Damage, Protection 4d vs Injury TN 18**) and permanently sealing the southern rampway with 10 tons of rubble.
* **Discovering the Maintenance Flue — EXPLORE (Wits TN)**:
  * *Target Number*: Wits TN (Torvir 15, Einar 15, Khoril 16).
  * *Modifiers*: Einar invoking *The Broken Key* rolls **Favoured**.
  * *Consequence of Failure*: Flue entrance behind left turret remains hidden; Company must proceed down the main ramp into Location 3.
  * *Degrees of Success ($\mathbf{6}$ icons)*:
    * $\mathbf{6}$: Locates the crawlway bypassing Location 3 directly into Location 5.
* **Opening the Armoire Wall-Locker — CRAFT or STEALTH (Strength TN or Wits TN)**:
  * *Target Number*: Strength TN (Craft) or Wits TN (Stealth).
  * *Modifiers*: Invoking the *Burglary* Trait (or Bróga's *Vaultbreaker* gift) grants $+1\text{d}$.
  * *Consequence of Failure*: Heavy bronze lock mechanism jams solid; forcing it requires iron crowbars ($+1\text{ Noise}$).
  * *Degrees of Success ($\mathbf{6}$ icons)*:
    * $\mathbf{6}$: Silent opening; recovers 24 masterwork arrows (+1 Ranged Damage), 4 iron grappling hooks with 50ft rope, and a flask of *Dwarven Blasting Pitch*.

---

### Location 3: The First Armoury (The Stripped Hall)
* **Elevation**: Middle Tier (Level 3B)
* **Role**: Despoiled Outpost & Trap Hazard
* **Connections**: North (Ramp to Loc 2), South (Pillared Arch to Loc 4), West (Maintenance Duct to Loc 5)
* **Baseline Threat**: Alert Tier 0–1; Orc scrap-traps, black-venom cauldrons.

#### Violations & Errata Found
1. `02_keyed_locations.md:115`: `Detect Traps (SCAN TN 14 / Einar with Broken Key rolls with +2)` -> Fixed TN 14; flat "+2".
2. `02_keyed_locations.md:115`: `test ATHLETICS (TN 14)` -> Fixed TN 14 (Trap avoidance).
3. `02_keyed_locations.md:116`: `Scavenge the Debris (HUNTING / CRAFT TN 14)` -> Fixed TN 14.
4. `04_keyed_locations.md:289`: `Explore TN 14` -> Fixed TN 14 (West duct bypass).
5. `04_keyed_locations.md:329`: `Healing (TN 14) or Endurance (TN 14) test` -> Fixed TN 14; non-existent "Endurance test".
6. `04_keyed_locations.md:334`: `Scan (TN 14)` -> Fixed TN 14; `+2 modifier / Advantage`.
7. `04_keyed_locations.md:336`: `Burglary (TN 14) / Craft (TN 14) / Band Expertise (2d6 vs TN 15)` -> Non-existent skill `Burglary TN 14`.
8. `04_keyed_locations.md:338`: `Healing (TN 14) / Craft (TN 14)` -> Fixed TN 14 (Venom harvesting).
9. `04_keyed_locations.md:340`: `Craft (TN 14)` -> Fixed TN 14 (Re-arming trap).

#### Refactored TOR 2e Mechanical Blocks
* **Detecting Sinew Tripwires — SCAN (Wits TN)**:
  * *Target Number*: Wits TN (Torvir 15, Einar 15, Khoril 16).
  * *Modifiers*: Einar invoking *The Broken Key* rolls **Favoured**. Austri (*Scout*) on point grants $+1\text{d}$.
  * *Consequence of Failure*: The tripwire is missed; lead character steps on the cord, triggering the trap!
  * *Degrees of Success ($\mathbf{6}$ icons)*:
    * $\mathbf{6}$: Spots both interlocking tripwire lines, the caltrop field, and the loose floor-flag concealing the arming cache beneath rack #12.
* **Skill Endeavour: Disarming the Scythe Scrap-Trap Network (Resistance 3)**:
  * *Context*: Wedging the counterweighted scythe pivots and snipping taut sinew cords silently.
  * *Resistance*: **3**.
  * *Allowed Skills*: **CRAFT** (Strength TN), **STEALTH** (Wits TN), **SCAN** (Wits TN).
  * *Modifiers*: Invoking the *Burglary* Trait grants $+1\text{d}$; Bróga (*Vaultbreaker*) grants $+1\text{d}$.
  * *Consequence of Failure*: On a failed roll, the mechanism slips. If a Feat die shows an Eye of Sauron ($\mathbf{S}$), the scythe swings down! Lead character faces an attack (4d vs Strength TN + Shield; on hit: 14 Damage, Piercing Blow Injury TN 16 coated in Black Venom, $+2\text{ Noise Points}$).
  * *Degrees of Success ($\mathbf{6}$ icons)*:
    * $\mathbf{6}$: Contributes 2 points of Resistance.
    * $\mathbf{6}\mathbf{6}$: Entire trap network disarmed silently in a single action ($0\text{ Noise}$).
* **Harvesting Black Orc-Venom — HEALING or CRAFT (Heart TN or Strength TN)**:
  * *Target Number*: Heart TN (Healing) or Strength TN (Craft).
  * *Consequence of Failure*: Hands shake; vial shatters or blade pricks skin (hero must make Protection roll vs Injury TN 14 or suffer the Poisoned condition: Weary + lose 2 Endurance per hour).
  * *Degrees of Success ($\mathbf{6}$ icons)*:
    * $\mathbf{6}$: Safely harvests 3 pristine vials of *Black Orc-Venom* (applying to a blade grants $+2\text{ Injury Rating}$ for 1 combat encounter).
* **Re-Arming Traps for Rearguard — CRAFT (Strength TN)**:
  * *Target Number*: Strength TN (Torvir 13, Einar 14, Khoril 13).
  * *Consequence of Failure*: Traps disabled permanently; cannot be reused.
  * *Degrees of Success ($\mathbf{6}$ icons)*:
    * $\mathbf{6}$: Re-arms scythe blades facing north; during Act III withdrawal, automatically ambushes the Orc vanguard (delays pursuit by 2 rounds).

---

### Location 4: The Broken Hall (Museum of Fallen Valor)
* **Elevation**: Middle Tier (Level 3B)
* **Role**: Dread Encounter, Lore Clue & Psychological Crucible
* **Connections**: North (Arch to Loc 3), South (Cedar Doors to Loc 5), East (Sealed Cartouche)
* **Baseline Threat**: Alert Tier 0–1; lingering Shadow / Dread aura of the 12-ft Balrog Idol.

#### Violations & Errata Found
1. `02_keyed_locations.md:127`: `Shadow Hazard: All heroes must make a VALOUR Test (TN 14)` -> Fixed TN 14.
2. `02_keyed_locations.md:133`: `Decipher the Desecrated Murals (LORE TN 14)` -> Fixed TN 14.
3. `02_keyed_locations.md:134`: `Plunder the Idol's Eye (STEALTH / SLEIGHT TN 14)` -> Fixed TN 14; non-existent skill `SLEIGHT`.
4. `04_keyed_locations.md:403, 410`: `Dread Test (Valour TN 14 or Awe TN 14)` -> Fixed TN 14.
5. `04_keyed_locations.md:405, 414`: `Old Lore TN 14 or Riddle TN 14` -> Fixed TN 14; non-existent skill `Old Lore`.
6. `04_keyed_locations.md:406`: `Athletics (TN 14) or Band War (3d6 vs TN 15)` -> Fixed TN 14.
7. `04_keyed_locations.md:415`: `Enhearten / Song (TN 14)` -> Fixed TN 14.
8. `04_keyed_locations.md:425, 428`: `Craft TN 14` -> Fixed TN 14 (twice).

#### Refactored TOR 2e Mechanical Blocks
* **Resisting Spiritual Dread — AWE (Strength TN) or ENHEARTEN (Heart TN)**:
  * *Target Number*: Strength TN (Awe: Torvir 13, Einar 14, Khoril 13) or Heart TN (Enhearten: Torvir 18, Einar 17, Khoril 16).
  * *Modifiers*: Dwarves testing vs Orc/Balrog desecration test **Ill-favoured** if they have an active Flaw.
  * *Consequence of Failure*: Hero gains **$2\text{ Shadow Points (Dread)}$** and becomes **Daunted** (cannot spend Hope points for 1 hour).
    * *Torvir's Curse of Vengeance*: On failure, Torvir flies into uncontrollable rage and must spend his next turn smashing the idol ($+2\text{ Noise Points}$, gains 2 Fatigue).
    * *Einar's Dragon-sickness*: On failure, Einar becomes obsessed with prying molten gold-leaf from the idol, wasting 10 minutes.
  * *Degrees of Success ($\mathbf{6}$ icons)*:
    * $\mathbf{6}$: Unshakable resolve; completely immune to the room's Dread aura and grants $+1\text{d}$ to an adjacent ally's test.
    * $\mathbf{6}\mathbf{6}$: Resolute defiance; inspires the Company, clearing the Daunted condition from all companions.
* **Deciphering the Royal Cartouche — LORE or RIDDLE (Wits TN)**:
  * *Target Number*: Wits TN (Torvir 15, Einar 15, Khoril 16).
  * *Modifiers*: Dwarf of Durin heritage grants $+1\text{d}$.
  * *Consequence of Failure*: Runic cipher remains garbled; key mechanics of the King's Door remain unknown until Location 9.
  * *Degrees of Success ($\mathbf{6}$ icons)*:
    * $\mathbf{6}$: Translates the master cipher (*"The Vault of the Crown shall yield neither to pick nor hammer, save when the Marshal's Baton turns the left ward and the King's Signet turns the right"*), confirming that the King's Door requires both keys or an extraordinary bypass endeavour.
* **Banish the Gloom — SONG or ENHEARTEN (Strength TN or Heart TN)**:
  * *Target Number*: Strength TN (Song: Khoril 13) or Heart TN (Enhearten: Khoril 16).
  * *Consequence of Failure*: Voice falters in the oppressive gloom; no effect.
  * *Degrees of Success ($\mathbf{6}$ icons)*:
    * $\mathbf{6}$: Singing *The Song of Durin* cleanses the oppressive aura, removes Daunted from all heroes, and restores **$+1\text{ Band Hope}$**.
* **Skill Endeavour: Controlled Toppling of the Balrog Idol (Resistance 3)**:
  * *Context*: Rigging crowbars and blanketing the stone base with canvas to topple the 12-foot iron effigy without alarming the deeps.
  * *Resistance*: **3**.
  * *Allowed Skills*: **ATHLETICS** (Strength TN), **CRAFT** (Strength TN).
  * *Modifiers*: Dúrmer (*Mighty*) grants $+1\text{d}$; wrapping in blankets (Craft) reduces acoustic impact.
  * *Consequence of Failure*: Idol crashes unpadded onto granite flagstones, generating **$+3\text{ Noise Points (+1 Alert Tier, +1 Eye Awareness)}$**.
  * *Degrees of Success ($\mathbf{6}$ icons)*:
    * $\mathbf{6}$: Contributes 2 points of Resistance.
    * $\mathbf{6}\mathbf{6}$: Idol is lowered gently in absolute silence ($+0\text{ Noise}$), restores $+1\text{ Band Hope}$, and allows 30 silver pennies (3 Treasure) of gold scrap to be safely recovered.

---

### Location 5: The Second Armoury (The Siege Workshop)
* **Elevation**: Middle Tier (Level 3B)
* **Role**: Tactical Sandbox & Heavy Artillery
* **Connections**: North (Cedar Doors to Loc 4), South (Bronze Doors to Loc 6), West (Pressure Door to Loc 7)
* **Baseline Threat**: Alert Tier 0–1; massive siege machinery, mobile Grond-ram.

#### Violations & Errata Found
1. `02_keyed_locations.md:148`: `Repair a Dwarf Ballista (CRAFT TN 14 / Hjoldring assists)` -> Fixed TN 14.
2. `02_keyed_locations.md:149`: `Barricade the Passage (ATHLETICS TN 14)` -> Fixed TN 14.
3. `04_keyed_locations.md:485`: `Operating Ballista: Athletics (TN 14) or Craft (TN 14)` -> Fixed TN 14.
4. `04_keyed_locations.md:488`: `Craft TN 14` -> Fixed TN 14 (Cedar balk barricade).
5. `04_keyed_locations.md:491`: `Craft (TN 14) / Band Expertise (2d6 vs TN 15)` -> Fixed TN 14.
6. `04_keyed_locations.md:493`: `Athletics (TN 14) / Band War (3d6 vs TN 15)` -> Fixed TN 14.
7. `04_keyed_locations.md:494`: `Battle (TN 14)` -> Fixed TN 14 (Artillery kill-zone).
8. `04_keyed_locations.md:506`: `Master Engineer's Chest: Burglary TN 14; Bróga gains +1d` -> Non-existent skill `Burglary TN 14`.

#### Refactored TOR 2e Mechanical Blocks
* **Skill Endeavour: Calibrating & Arming the Siege Engines (Resistance 3)**:
  * *Context*: Oiling bronze guide-tracks, stringing preserved sinew skeins, and loading the 6-foot star-iron harpoon.
  * *Resistance*: **3**.
  * *Allowed Skills*: **CRAFT** (Strength TN), **ATHLETICS** (Strength TN).
  * *Modifiers*: Hjoldring (*Smith*) grants $+1\text{d}$; Dwarven engineering tools grant $+1\text{d}$.
  * *Consequence of Failure*: Rusted gears grind loudly ($+1\text{ Noise Point}$ per failed attempt); takes 20 minutes instead of 10.
  * *Degrees of Success ($\mathbf{6}$ icons)*:
    * $\mathbf{6}$: Contributes 2 points of Resistance.
    * $\mathbf{6}\mathbf{6}$: Both the Grond-ram and Torsion Ballista are calibrated and cocked with masterwork precision.
  * *Mechanical Payoff*:
    * *Grond-Ram*: Released down the bronze tracks into Location 6, dealing **25 Direct Damage** to The Mauler (ignoring armour), knocking it Prone, and stripping 2d from its scrap carapace ($+4\text{ Noise}$).
    * *Torsion Ballista*: Ranged attack roll 4d vs Target TN (Damage 30, Piercing Blow Injury TN 22, anchors troll to doorway).
* **Designing the Chokepoint Kill-Zone — BATTLE (Heart TN)**:
  * *Target Number*: Heart TN (Khoril 16, Torvir 18, Einar 17).
  * *Consequence of Failure*: Poor tactical angles; siege engines cannot cover flanking archways.
  * *Degrees of Success ($\mathbf{6}$ icons)*:
    * $\mathbf{6}$: Flawless tactical placement; the companion band gains $+1\text{d}$ to all Band Clash and ranged rolls while fighting in Location 5.
* **Unlocking the Engineer's Strongbox — CRAFT or STEALTH (Strength TN or Wits TN)**:
  * *Target Number*: Strength TN (Craft) or Wits TN (Stealth), invoking *Burglary* Trait (+1d).
  * *Consequence of Failure*: Complex pin-tumbler jams; must be forced open with crowbars ($+1\text{ Noise}$).
  * *Degrees of Success ($\mathbf{6}$ icons)*:
    * $\mathbf{6}$: Silent opening; recovers 3 masterwork calipers, 2 flasks *Dwarven Lubricant Oil*, *Iron Spanner* (Club: Damage 4, Injury 14, Break Shield), and 4 star-iron harpoon heads.

---

### Location 6: The Hall of the Mauler (Lair of the Armoured Troll)
* **Elevation**: Lower Tier (Level 3C Drill Arena)
* **Role**: Apex Boss Arena & Dynamic Multi-Level Tactical Environment
* **Connections**: North (Blast Doors to Loc 5), South (Colonnade to Loc 9), East (Slag Chute)
* **Baseline Threat**: Alert Tier 1–2; **The Mauler** (Armoured Great Cave-troll, AL 10, Might 2, Hate 10, Armour 5d).

#### Violations & Errata Found
1. `02_keyed_locations.md:161`: `walking across a floor strewn with loose iron rings (STEALTH TN 16)` -> Fixed TN 16.
2. `02_keyed_locations.md:165`: `FORWARD STANCE / RIDDLE TN 14` -> Fixed TN 14.
3. `02_keyed_locations.md:166`: `spotted via SCAN TN 12` -> Fixed TN 12.
4. `04_keyed_locations.md:557`: `Athletics (TN 14) test to avoid losing footing` -> Fixed TN 14.
5. `04_keyed_locations.md:559`: `Athletics TN 14 or Craft TN 14` -> Fixed TN 14 (Stalactite drop).
6. `04_keyed_locations.md:562`: `Called Shot / Hunting (TN 14)` -> Fixed TN 14 (Sever master wire bundle).
7. `04_keyed_locations.md:566`: `Riddle Combat Task (TN 14 — The Riddle Duel)` -> Fixed TN 14.
8. `04_keyed_locations.md:570`: `Stealth (TN 16) / Band Manoeuvre (2d6 vs TN 16)` -> Fixed TN 16.
9. `04_keyed_locations.md:572`: `Athletics (TN 14)` -> Fixed TN 14 (Plunging strike).

#### Refactored TOR 2e Mechanical Blocks
* **The Catwalk Traverse — STEALTH (Wits TN)**:
  * *Target Number*: Wits TN (Torvir 15, Einar 15, Khoril 16).
  * *Modifiers*: Moving across scrap floor is **Ill-favoured** (-1d); moving along high catwalks is standard. Austri (*Scout*) leading grants $+1\text{d}$.
  * *Consequence of Failure*: A loose chain or iron ring clatters down into the nest ($+2\text{ Noise}$), waking The Mauler and initiating combat at Alert Tier 2!
  * *Degrees of Success ($\mathbf{6}$ icons)*:
    * $\mathbf{6}$: Company traverses the entire 40-pace hall in absolute silence ($0\text{ Noise}$), reaching Location 9 undetected.
* **Combat Task: The Riddle Duel (Forward Stance) — RIDDLE (Wits TN)**:
  * *Target Number*: Wits TN (Torvir 15, Einar 15, Khoril 16).
  * *Modifiers*: The Mauler's *Dull-Witted* Fell Ability makes this test **Favoured**!
  * *Consequence of Failure*: The troll ignores the mockery and swings its massive maul directly at the taunting hero (**Heavy Blow**, $+10\text{ Damage}$).
  * *Degrees of Success ($\mathbf{6}$ icons)*:
    * $\mathbf{6}$: The Mauler bellows in confusion, swinging at shadows; it loses **$1\text{ point of Hate}$** plus **$1\text{ additional Hate per }\mathbf{6}$ icon rolled**!
    * $\mathbf{Gandalf\ Rune\ (G)}$: The brute clutches its skull in terror, losing its entire turn; all Company attacks against it this round are Favoured.
* **Severing the Carapace Wires — HUNTING or CRAFT (Strength TN)**:
  * *Target Number*: Strength TN (Torvir 13, Einar 14, Khoril 13) in Forward Stance or from Catwalk.
  * *Modifiers*: Called Shot rules apply (must roll at least one $\mathbf{6}$ icon).
  * *Consequence of Failure*: Blade bounces off iron plates; hero is exposed to counter-attack.
  * *Degrees of Success ($\mathbf{6}$ icons)*:
    * $\mathbf{6}$: Snips the master copper wire bundle, dropping The Mauler's scrap Armour rating permanently from **5d to 3d**!
* **Dropping the Limestone Stalactite — ATHLETICS or CRAFT (Strength TN)**:
  * *Target Number*: Strength TN (Torvir 13, Einar 14, Khoril 13).
  * *Consequence of Failure*: Stalactite misses, smashing flagstones ($+3\text{ Noise Points, +1 Alert Tier}$).
  * *Degrees of Success ($\mathbf{6}$ icons)*:
    * $\mathbf{6}$: Direct hit: inflicts **20 Direct Damage** (bypassing Armour), knocks The Mauler **Prone**, and strips 1d from its Armour.

---

### Location 7: The Poisoned Halls (Twelfth & Fourteenth Halls)
* **Elevation**: Middle Tier / Depressed Basin (Level 3B-minus)
* **Role**: Environmental Hazard & Clue Investigation
* **Connections**: East (Pressure Door to Loc 5), South (Bronze Portal to Loc 8), Overhead (Vent Flues)
* **Baseline Threat**: Alert Tier 0–1; **The Breath of the Pit** (Lethal Balrog Neurotoxic Miasma).

#### Violations & Errata Found
1. `02_keyed_locations.md:176`: `With protective masks/herbs, test once per hour (TN 14)` -> Fixed TN 14.
2. `02_keyed_locations.md:177`: `VALOUR TN 12 to take wargear respectfully` -> Fixed TN 12.
3. `02_keyed_locations.md:180`: `SCAN TN 14 / Einar with Broken Key` -> Fixed TN 14.
4. `04_keyed_locations.md:635, 636`: `Endurance / Healing (TN 14) every minute` & `every hour` -> Fixed TN 14; non-existent "Endurance test".
5. `04_keyed_locations.md:637, 647`: `Masterwork Dwarf Respirator (Craft TN 15)` -> Fixed TN 15.
6. `04_keyed_locations.md:639`: `Athletics TN 12 or Craft TN 12` -> Fixed TN 12 (Prying lead scroll tube).
7. `04_keyed_locations.md:643`: `Athletics (TN 16) or Craft (TN 16)` -> Fixed TN 16 (Ceiling flue lever).
8. `04_keyed_locations.md:648`: `Healing (TN 14)` -> Fixed TN 14.
9. `04_keyed_locations.md:649`: `Riddle / Old Lore (TN 14)` -> Fixed TN 14; `Old Lore`.
10. `04_keyed_locations.md:650`: `Scan (TN 14)` -> Fixed TN 14; `+2 from The Broken Key`.

#### Refactored TOR 2e Mechanical Blocks
* **The Breath of the Pit Exposure — Protection Roll (Armour/Strength TN)**:
  * *Hazard Classification*: Balrog Volcanic Neurotoxin.
  * *Unprotected Exposure*: Tested every minute. Roll Protection dice against Strength TN (Torvir 13, Einar 14, Khoril 13), **Ill-favoured**. Failure inflicts $1\text{d6}$ Endurance loss; rolling an Eye of Sauron ($\mathbf{S}$) drops the character to 0 Endurance (**Dying condition!**).
  * *Protected Exposure (Herbal Poultices / Vinegar Cloths via Healing check)*: Tested once per hour. Failure inflicts $1\text{d3}$ Endurance loss; rolling an Eye of Sauron inflicts Severe Poison.
* **Skill Endeavour: Assembling Squad Respirator Masks (Resistance 3)**:
  * *Context*: Constructing airtight masks using oiled leather, charcoal granules, crushed sponge, and crystal goggles.
  * *Resistance*: **3**.
  * *Allowed Skills*: **CRAFT** (Strength TN), **HEALING** (Heart TN).
  * *Modifiers*: Hjoldring (*Smith*) grants $+1\text{d}$; utilizing laboratory supplies from Location 5 grants $+1\text{d}$.
  * *Consequence of Failure*: Flawed filter seals (provides only *Protected* status rather than full immunity).
  * *Degrees of Success ($\mathbf{6}$ icons)*:
    * $\mathbf{6}$: Contributes 2 points of Resistance.
    * $\mathbf{6}\mathbf{6}$: Completes masterwork respirators providing **4 hours of complete gas immunity** for up to 10 companions!
* **Unjamming the Overhead Exhaust Damper — ATHLETICS or CRAFT (Strength TN)**:
  * *Target Number*: Strength TN (Torvir 13, Einar 14, Khoril 13).
  * *Modifiers*: Ill-favoured due to rusted iron corrosion. Dúrmer (*Mighty*) grants $+1\text{d}$.
  * *Consequence of Failure*: The rusted iron lever binds solid; hero suffers 2 Fatigue from physical exertion.
  * *Degrees of Success ($\mathbf{6}$ icons)*:
    * $\mathbf{6}$: Lever frees with a screech ($+3\text{ Noise}$); exhaust flues open, venting the entire hall clear of toxic gas in 2 combat rounds!
* **Prying the Lead Scroll Tube — ATHLETICS or CRAFT (Strength TN)**:
  * *Target Number*: Strength TN (Torvir 13, Einar 14, Khoril 13).
  * *Consequence of Failure*: Calcified fingers snap; brittle lead tube is crushed, making runes partially illegible.
  * *Degrees of Success ($\mathbf{6}$ icons)*:
    * $\mathbf{6}$: Flawless extraction of Handout #1 (*The Dying Scribe's Letter*), revealing the full fate of the Marshal's Key.

---

### Location 8: The Upper Armoury (The Garrison Salvage Cache)
* **Elevation**: Middle Tier (Level 3B)
* **Role**: Garrison Salvage Cache & Goblin Grave
* **Connections**: North (Bronze Door to Loc 7), East (Reinforced Flue to Loc 9), South (Emergency Chimney)
* **Baseline Threat**: Alert Tier 0; desiccated goblin corpses, heavy wargear salvage.

#### Violations & Errata Found
1. `04_keyed_locations.md:688, 714, 740`: `+50 Garrison Supply Points for Balin!` -> Fabricated mechanic.
2. `04_keyed_locations.md:716`: `Craft (TN 14) or Burglary (TN 14)` -> Fixed TN 14; non-existent skill `Burglary`.
3. `04_keyed_locations.md:718`: `Scan TN 12` -> Fixed TN 12 (Searching goblin corpses).
4. `04_keyed_locations.md:724`: `Explore / Battle (TN 14)` -> Fixed TN 14 (Salvage packing).
5. `04_keyed_locations.md:725`: `Craft (TN 14)` -> Fixed TN 14 (Liquid fire seal).
6. `04_keyed_locations.md:726`: `Burglary (TN 14)` -> Fixed TN 14; non-existent skill `Burglary`.
7. `04_keyed_locations.md:731`: `Craft TN 14` -> Fixed TN 14 (Muffling wargear).

#### Refactored TOR 2e Mechanical Blocks
* **Purge of Fabricated Points & Refactored Rewards**:
  * *Purged Term*: `+50 Garrison Supply Points`.
  * *Official TOR 2e Rewards*:
    1. **The Garrison Wargear Hoard**: 40 Suits of Dwarf Mail-shirts (Protection 3d, Load 9), 30 Heavy Tunnel-Shields (+2 Parry, Load 2), 50 Masterwork War-Mattocks and Axes (Damage 6, Injury 18). Safely extracting this hoard equips Balin's frontline vanguard, permanently awards **$+2\text{ Band Readiness}$**, provides **$50\text{ Treasure Points}$** in colony tribute, and earns the royal favor of King Dáin Ironfoot.
    2. **Munitions Cache**: 6 flasks of *Dwarven Liquid Fire* (Missile Weapon: Damage 8, Injury 18, *Fiery Blow* [severe burning], illuminates 30ft radius).
    3. **Officer's Regalia**: 1 suit of *Reinforced Dwarf-mail* (Protection 4d, Load 12) and 1 *Gleaming Broadsword* (Damage 5, Injury 16, Keen).
* **Skill Endeavour: Securing & Padding Heavy Salvage (Resistance 3)**:
  * *Context*: Organizing 50 suits of heavy gromril-mail and weapons into transport litters and wrapping iron plates in felt.
  * *Resistance*: **3**.
  * *Allowed Skills*: **EXPLORE** (Wits TN), **CRAFT** (Strength TN), **ATHLETICS** (Strength TN).
  * *Modifiers*: Hjoldring (*Smith*) and Dúrmer (*Mighty*) each grant $+1\text{d}$.
  * *Consequence of Failure*: Crates clatter loudly ($+1\text{ Noise Point}$ per failed roll); packing takes 45 minutes instead of 20.
  * *Degrees of Success ($\mathbf{6}$ icons)*:
    * $\mathbf{6}$: Contributes 2 points of Resistance.
    * $\mathbf{6}\mathbf{6}$: Flawlessly packed and muffled ($0\text{ Noise}$); prevents Band Manoeuvre penalties during withdrawal.
* **Cracking the Munitions Seal — CRAFT or STEALTH (Strength TN or Wits TN)**:
  * *Target Number*: Strength TN (Craft) or Wits TN (Stealth), invoking *Burglary* Trait ($+1\text{d}$).
  * *Consequence of Failure*: Lead seal shears violently; 1 glass ampoule cracks, destroying 1 flask of Liquid Fire ($+1\text{ Noise}$).
  * *Degrees of Success ($\mathbf{6}$ icons)*:
    * $\mathbf{6}$: All 6 flasks of Liquid Fire extracted intact with zero hazard.

---

### Location 9: The King's Door (The Adamant Portal)
* **Elevation**: Deepest Tier (Level 3C)
* **Role**: Runic Gate Puzzle & Ambush Choke Point
* **Connections**: North (Colonnade to Loc 6), West (Flue to Loc 8), South (Threshold to Loc 10), Overhead (Ambush Parapet)
* **Baseline Threat**: Alert Tier 2; **Grimnar the Disgraced** (AL 6 Stalker) and 4 Udûn Stalkers positioned in overhead ambush.

#### Violations & Errata Found
1. `02_keyed_locations.md:208`: `Extended CRAFT Endeavour: Resistance 6, TN 16` -> Fixed TN 16.
2. `02_keyed_locations.md:211`: `VALOUR TN 14 test` -> Fixed TN 14 (Blood of Durin ritual).
3. `04_keyed_locations.md:795`: `Extended Burglary / Craft Endeavour (requires 3 Successes vs TN 16; Einar gains +2 / Advantage)` -> Fixed TN 16; non-existent skill `Burglary`; flat "+2".
4. `04_keyed_locations.md:801`: `Awareness (TN 14) / Band Vigilance (2d6 vs TN 15)` -> Fixed TN 14.
5. `04_keyed_locations.md:804`: `Riddle / Old Lore (TN 14)` -> Fixed TN 14; `Old Lore`.
6. `04_keyed_locations.md:805`: `Burglary (TN 16 / Extended Endeavour)` -> Non-existent skill `Burglary TN 16`.

#### Refactored TOR 2e Mechanical Blocks
* **Overhead Ambush Detection — AWARENESS (Strength TN)**:
  * *Target Number*: Strength TN (Torvir 13, Einar 14, Khoril 13).
  * *Modifiers*: Khoril invoking *Wary* Trait grants $+1\text{d}$. Forward Scout Screen (*Band Vigilance*) rolls 2d vs Band TN 15.
  * *Consequence of Failure*: Grimnar and his stalkers spring their ambush, gaining a **Surprise Round** (+1d to attacks; heroes cannot use Shield Parry).
  * *Degrees of Success ($\mathbf{6}$ icons)*:
    * $\mathbf{6}$: Spots the glint of poisoned javelins in the murder-holes before stepping into the kill-zone; Company avoids surprise and gains a free ranged volley.
* **Skill Endeavour: Bypassing the Adamant Runic Lock (Resistance 6)**:
  * *Context*: Picking the dual meteoric-iron and adamant tumblers if the *Marshal's Key* or royal blood is unavailable.
  * *Resistance*: **6**. Each attempt represents 1 combat round (or 5 minutes outside combat).
  * *Allowed Skills*: **CRAFT** (Strength TN 14 for Einar), **STEALTH** (Wits TN 15 for Einar), **RIDDLE** (Wits TN 15 for Einar).
  * *Modifiers*: Invoking the *Burglary* Trait grants $+1\text{d}$; Einar invoking *The Broken Key* rolls **Favoured**; Bróga (*Vaultbreaker*) assisting grants $+1\text{d}$.
  * *Consequence of Failure*: Fine pick binds ($+1\text{ Noise Point}$ per failed round); after 3 consecutive failures, a pick snaps, imposing $-1\text{d}$ on subsequent attempts.
  * *Degrees of Success ($\mathbf{6}$ icons)*:
    * $\mathbf{6}$: Contributes 2 points of Resistance.
    * $\mathbf{6}\mathbf{6}$: Contributes 3 points of Resistance!
  * *Outcome on Success*: The twin adamant wards click back in harmonic sequence; the King's Door swings open in total silence ($0\text{ Noise}$).
* **The Blood of Durin Inscription Ritual — AWE (Strength TN) or ENHEARTEN (Heart TN)**:
  * *Target Number*: Strength TN (Torvir 13, Khoril 13) or Heart TN (Torvir 18, Khoril 16).
  * *Modifiers*: Heir of Durin bloodline grants $+1\text{d}$ and **Favoured**.
  * *Consequence of Failure*: Hero loses 2 Endurance from the cut; the Crown rune fails to awaken; 1 Shadow Point (Dread) gained.
  * *Degrees of Success ($\mathbf{6}$ icons)*:
    * $\mathbf{6}$: The Ithildin Crown blazes with white starlight; the royal ward disengages instantly with a deep resonant tone.

---

### Location 10: The Lower Armoury (The Royal Vault)
* **Elevation**: Deepest Sanctuary (Level 3C)
* **Role**: Legendary Treasure Vault, Artifact Chamber & Ultimate Objective
* **Connections**: North (King's Door threshold)
* **Baseline Threat**: Sacred Sanctum; **Durin's Axe** claiming trigger ($+4\text{ Eye Awareness}$, instant Alert Tier 3).

#### Violations & Errata Found
1. `02_keyed_locations.md:223`: `Eye Awareness increases by +4 immediately!` -> Valid mechanic, but needs explicit link to Revelation Episode.
2. `04_keyed_locations.md:879`: `Awe / Song (TN 14)` -> Fixed TN 14.
3. `04_keyed_locations.md:881`: `Greed / Shadow Test (Valour TN 14)` -> Fixed TN 14; non-existent skill `Greed`.
4. `04_keyed_locations.md:883`: `Craft / Old Lore (TN 14)` -> Fixed TN 14; `Old Lore`.
5. `04_keyed_locations.md:891`: `Lifting Durin's Axe: Special (+4 Strategic Eye Awareness!)` -> Needs formal trigger block.

#### Refactored TOR 2e Mechanical Blocks
* **Contemplating the Royal Relic — AWE or SONG (Strength TN)**:
  * *Target Number*: Strength TN (Torvir 13, Einar 14, Khoril 13).
  * *Consequence of Failure*: Overwhelmed by sorrow and reverent weeping; suffers the Daunted condition for 1 hour.
  * *Degrees of Success ($\mathbf{6}$ icons)*:
    * $\mathbf{6}$: Heart filled with ancestral majesty; clears all *Weary* conditions from all Player-Heroes and restores **$+2\text{ Hope Points}$**.
* **Resisting Dragon-Sickness & Greed — Shadow Test (Heart TN / Wits TN)**:
  * *Target Number*: Heart TN (Einar 17) or Wits TN (Einar 15).
  * *Modifiers*: Einar's *Dragon-sickness* Flaw makes this test **Ill-favoured** (-1d).
  * *Consequence of Failure*: Einar gains **$2\text{ Shadow Points (Greed)}$** and becomes compelled to stuff every golden goblet and mithril ingot into his pack, shifting Band status to Heavy Burden.
  * *Degrees of Success ($\mathbf{6}$ icons)*:
    * $\mathbf{6}$: Einar's wisdom prevails over avarice; he focuses solely on securing the royal relics and mithril ingots.
* **Disengaging the Runic Stasis Field — CRAFT or LORE (Strength TN or Wits TN)**:
  * *Target Number*: Strength TN (Craft) or Wits TN (Lore).
  * *Consequence of Failure*: The stasis field discharges with a thunderous electrical snap, inflicting 5 Damage to the lifter and generating **$+2\text{ Noise Points}$**.
  * *Degrees of Success ($\mathbf{6}$ icons)*:
    * $\mathbf{6}$: The stasis field dissipates in complete silence; Durin's Axe is lifted cleanly from the black marble anvil.
* **Claiming Durin's Axe & The Revelation Trigger**:
  * Lifting the royal axe triggers a deep harmonic subterranean chime throughout the Third Deep:
    * **Strategic Eye Awareness**: Automatically spikes by **$+4\text{ Points}$**.
    * **Alarm Escalation**: The module immediately transitions to **Alert Tier 3 (*Drums in the Deep!*)**.
    * **The Fighting Withdrawal**: The 6-round evacuation countdown begins!

---

## 4. Summary Matrix Refactoring (Locations 1–10)

The summary matrices in `04_keyed_locations.md:908-921` and `handouts/gm_cheat_sheet.md:12-54` must be completely replaced with the certified TOR 2e matrix:

```
========================================================================================================================
                                     CERTIFIED TOR 2E LOCATION SUMMARY MATRIX
========================================================================================================================
 LOC  NAME                TIER     LIGHTING   PRIMARY HAZARD / OBSTACLE        KEY SKILL CHECKS (ATTRIBUTE) NOISE / ALERT IMPACT
------------------------------------------------------------------------------------------------------------------------
  1   Mustering-Yard      Level 3A Pitch/Moss Udûn Sentries / Open Ground      Stealth (WIT), Scan (WIT)    +0 (Sneak) / +1 (1-rd kill)
  2   Upper Gatehouse     Level 3A Shadow     Buckled Doors / Fallback Point   Craft (STR), Battle (HRT)    +1 (Fortify) / +4 (Cave-In)
  3   First Armoury       Level 3B Pitch      Scythe Scrap-Traps / Venom       Scan (WIT), Craft (STR)      +0 (Disarm) / +2 (Spring)
  4   Broken Hall         Level 3B Darkness   Balrog Idol Dread / Desecration  Awe (STR), Lore (WIT)        +0 (Lurk) / +3 (Topple)
  5   Second Armoury      Level 3B Gloom      Siege Engines / Heavy Machinery  Craft (STR), Athletics (STR) +0 (Prep) / +4 (Ram Fire)
  6   Hall of the Mauler  Level 3C Dim Moss   The Mauler (AL 10 Troll)         Riddle (WIT), Stealth (WIT)  +0 (Sneak) / +3 (Stalactite)
  7   Poisoned Halls      Level 3B Emerald    Balrog Neurotoxic Miasma         Protection (STR), Craft (STR)+0 (Silent) / +3 (Vent Flue)
  8   Upper Armoury       Level 3B Dark/Steel Garrison Salvage / Burden Shift  Explore (WIT), Craft (STR)   +1 (Pack) / +3 (Clatter)
  9   The King's Door     Level 3C Ithildin   Dual Locks / Grimnar Ambush      Awareness (STR), Craft (STR) +0 (Key) / +2 (Skirmish)
 10   Lower Armoury       Level 3C Radiant    Durin's Axe / Greater Hoard      Awe (STR), Shadow (HRT)      Special (+4 Eye / Alert 3)
========================================================================================================================
```

---

## 5. Formal Skill Endeavours Master Catalog

The following six complex operations must be formally formatted as **Skill Endeavours** with explicit Resistance ratings, allowed skills, failure penalties, and success multipliers:

| Endeavour Name | Location | Resistance | Allowed Official Skills | Time per Check | Primary Hazard on Failure |
| :--- | :---: | :---: | :--- | :---: | :--- |
| **1. Fortifying the Upper Gatehouse** | Loc 2 | **3** | **CRAFT** (STR), **ATHLETICS** (STR), **BATTLE** (HRT) | 10 min | $+1\text{ Noise}$; weak barricade (+1 Parry instead of Total Cover) |
| **2. Disarming the Scythe Trap Network** | Loc 3 | **3** | **SCAN** (WIT), **CRAFT** (STR), **STEALTH** (WIT) | 1 round | Trap springs (14 Dmg, Injury 16 + Black Venom, $+2\text{ Noise}$) |
| **3. Lowering the Balrog Dark Idol** | Loc 4 | **3** | **ATHLETICS** (STR), **CRAFT** (STR) | 5 min | Idol crashes onto flagstones ($+3\text{ Noise, +1 Alert Tier}$) |
| **4. Rigging & Priming Siege Engines** | Loc 5 | **3** | **CRAFT** (STR), **ATHLETICS** (STR) | 5 min | Machine slips ($+1\text{ Noise}$); bolt misfires |
| **5. Crafting Squad Respirator Masks** | Loc 7 | **3** | **CRAFT** (STR), **HEALING** (HRT) | 10 min | Flawed seals (provides only *Protected* status, not immunity) |
| **6. Picking the King's Adamant Lock** | Loc 9 | **6** | **CRAFT** (STR), **STEALTH** (WIT), **RIDDLE** (WIT) | 1 round | Pick snaps, $+1\text{ Noise/rd}$; Grimnar springs ambush |

---

## 6. Purge Dictionary: Fabricated Mechanics & Illegal Terms

| Current Non-Compliant Term | File & Line Instances | Certified TOR 2e Replacement |
| :--- | :--- | :--- |
| **`Burglary`** (as a skill) | `02:278`, `04:336`, `04:506`, `04:716`, `04:726`, `04:795`, `04:805`, `node_map:301` | **Distinctive Feature (Trait)** invoked on **CRAFT**, **STEALTH**, **SCAN**, or **ATHLETICS** to grant $+1\text{d}$. |
| **`Sleight`** | `02:134` | **STEALTH** (Wits TN) or **CRAFT** (Strength TN), invoking *Burglary* Trait. |
| **`Old Lore`** | `02:133`, `04:186`, `04:405`, `04:414`, `04:649`, `04:804`, `04:883` | **LORE** (Wits TN). |
| **`Customs`** | `handouts/node_map.md:307` | **COURTESY** (Heart TN), **PERSUADE** (Wits TN), or **RIDDLE** (Wits TN). |
| **`Dread 14` / `Greed 14` / `Catwalks 14`** | `04:913`, `04:915`, `04:919`, `handouts/gm_cheat_sheet.md:26,50` | **AWE** (Strength TN), **ENHEARTEN** (Heart TN), **VALOUR** (Heart TN), **ATHLETICS** (Strength TN). |
| **`+50 Garrison Supply Points`** | `04:120`, `04:688`, `04:714`, `04:740`, `04:898`, `node_map:350` | **40 Dwarf Mail-shirts, 30 Shields, 50 Mattocks/Axes** ($+2\text{ Band Readiness}$, 50 Treasure Points in colony tribute, Royal Renown with King Dáin). |
| **`+2 modifier / Advantage`** | `02:84`, `02:115`, `04:122`, `04:183`, `04:261`, `04:335`, `04:650`, `04:795`, `node_map:298` | **Favoured** roll (roll two Feat dice, take the better result) or $+1\text{d}$. |
| **`+1 to all Battle rolls`** | `04:123`, `00:82` | **$+1\text{d}$ to Battle rolls** or **Favoured**. |
| **`Endurance test (TN 14)`** | `02:176`, `04:329`, `04:635` | **Protection roll** (using Armour dice against Strength TN) or **ATHLETICS / HEALING** (Strength/Heart TN). |

---

## 7. Cross-Document Alignment & Discrepancy Resolutions

During the survey, several cross-document inconsistencies were identified and must be reconciled in Milestone 1:

1. **Dwarf Scribe Identity**:
   - `04_keyed_locations.md:639` refers to Scribe *Náli son of Náin*.
   - `handouts/node_map.md:53, 235` refers to Scribe *Frár*.
   - `handouts/dying_scribe_letter.md` must be checked to establish the authoritative name. **Recommendation**: Harmonize to *Náli son of Náin* (or whichever name is on the physical handout).
2. **King's Door Bypass Resistance**:
   - `02_keyed_locations.md:208` states `Resistance 6, TN 16`.
   - `04_keyed_locations.md:795` states `requires 3 Successes vs TN 16`.
   - **Resolution**: Set officially as **Resistance 6** Skill Endeavour, where each $\mathbf{6}$ icon grants an extra success, allowing 3 exceptional rolls to breach the door while reflecting an adamant masterwork lock.
3. **Band Dice Pools**:
   - Several lines state `Band Manoeuvre (2d6 vs TN 15)`.
   - **Resolution**: In official Moria solo/band rules, Band rolls roll **1 Feat Die + Disposition Success Dice** (e.g. Feat Die + 2d for Manoeuvre 2d) against **Band TN 15** ($20 - \text{Readiness 5}$).

---

## 8. Milestone 1 (R1) Implementation Action Plan

When R1 implementation begins, refactor `02_keyed_locations.md` and `04_keyed_locations.md` using the following standardized test block structure:

```markdown
* **[Skill Name] ([Attribute] TN)**: [Action description]
  * *Modifiers*: [Favoured / Ill-favoured, +/-1d, Trait / Item invocations]
  * *Consequence of Failure*: [Specific mechanical Endurance/Shadow/Noise/Alert penalty]
  * *Degrees of Success ($\mathbf{6}$ icons)*:
    * $\mathbf{6}$: [Tangible benefit: stealth, time reduction, bonus die to ally, extra information]
    * $\mathbf{6}\mathbf{6}$: [Superior benefit: instant completion, Hope restoration, bonus discovery]
```

This concludes the master survey of the Location Atlas.
