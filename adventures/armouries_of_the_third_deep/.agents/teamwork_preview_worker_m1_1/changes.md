# Changes Report: Location Atlas TOR 2e Refactoring (Milestone 1 / R1)

## Executive Summary
All 10 keyed locations across `02_keyed_locations.md`, `04_keyed_locations.md`, and `handouts/node_map.md` have been refactored to 100% compliance with *The One Ring 2nd Edition* (TOR 2e) core rules and *Moria: Through the Doors of Durin*. All 45+ fixed player-hero target numbers, non-existent skills, flat modifiers, and fabricated reward systems have been completely eliminated.

---

## Detailed File Changes

### 1. `02_keyed_locations.md`
- **Location 1 (The Mustering-Yard)**:
  - Replaced `STEALTH TN 14` with `**STEALTH** (Wits TN: Torvir 15, Einar 15, Khoril 16)` specifying Alert Tier 0 (+1d), basalt pillar cover, consequence of failure (+1 Noise Point), and 6/66 success benefits.
  - Replaced `SCAN TN 14 / Einar with Broken Key rolls with +2` with `**SCAN** (Wits TN: Torvir 15, Einar 15, Khoril 16)` with Einar Favoured roll, failure consequences, and 6/66 success benefits.
  - Replaced `BATTLE TN 14` with `**BATTLE** (Heart TN: Torvir 18, Einar 17, Khoril 16)` ambush assault test block.
  - Added `**LORE** (Wits TN) or **BATTLE** (Heart TN)` for scorch mark analysis.
  - Replaced parley test with `**PERSUADE** or **RIDDLE** (Wits TN)` for Grik the Skulker.
  - Added Khoril's `**TRAVEL** or **ENHEARTEN** (Heart TN)` (*Leadership* Trait +1d) / Band **MANOEUVRE** (2d) against **Band TN 15**.
- **Location 2 (The Upper Gatehouse)**:
  - Converted fortification check into formal **Skill Endeavour: Fortifying the Forward Redoubt (Resistance 3)** with CRAFT (Strength TN), ATHLETICS (Strength TN), BATTLE (Heart TN), Hjoldring/Dúrmer modifiers (+1d), failure consequences (+1 Noise/attempt), and 6/66 degrees of success.
  - Refactored `AWARENESS TN 14` to `**CRAFT** (Strength TN) or **BATTLE** (Heart TN)` for rigging the Keystone Winch Trap (30 Damage, Protection 4d vs Injury TN 18, +4 Noise).
  - Added `**EXPLORE** (Wits TN)` for the maintenance flue bypass.
  - Converted `Burglary TN 14` armoire check to `**CRAFT** (Strength TN) or **STEALTH** (Wits TN)`, invoking *Burglary* Trait (+1d).
- **Location 3 (The First Armoury)**:
  - Replaced `SCAN TN 14` with `**SCAN** (Wits TN)` (Einar Favoured).
  - Implemented formal **Skill Endeavour: Disarming the Scythe Scrap-Trap Network (Resistance 3)** with CRAFT (Strength TN), STEALTH (Wits TN), SCAN (Wits TN), *Burglary* Trait (+1d), Bróga (+1d), Eye of Sauron trigger (4d vs Strength TN + Shield, 14 Dmg, Injury TN 16 Black Venom), and 6/66 degrees of success.
  - Replaced `HUNTING / CRAFT TN 14` with `**HUNTING** or **CRAFT** (Strength TN)` for concealed arming cache scavenging.
  - Added `**HEALING** (Heart TN) or **CRAFT** (Strength TN)` for harvesting Black Orc-Venom.
  - Added `**CRAFT** (Strength TN)` for re-arming traps.
- **Location 4 (The Broken Hall)**:
  - Replaced `VALOUR Test (TN 14)` with `**AWE** (Strength TN: Torvir 13, Einar 14, Khoril 13) or **ENHEARTEN** (Heart TN: Torvir 18, Einar 17, Khoril 16)` against Balrog Idol Dread, including individual Flaw triggers (*Curse of Vengeance*, *Dragon-sickness*).
  - Replaced `LORE TN 14` with `**LORE** or **RIDDLE** (Wits TN)` for the Royal Cartouche.
  - Implemented formal **Skill Endeavour: Controlled Toppling of the Balrog Idol (Resistance 3)** with ATHLETICS (Strength TN), CRAFT (Strength TN), Dúrmer (+1d), blanket muffling, failure penalties (+3 Noise / Alert 1), and 6/66 success benefits.
  - Purged `SLEIGHT TN 14` and replaced with `**STEALTH** (Wits TN) or **CRAFT** (Strength TN)`, invoking *Burglary* Trait (+1d).
  - Added `**SONG** (Strength TN) or **ENHEARTEN** (Heart TN)` for *The Song of Durin*.
- **Location 5 (The Second Armoury / Siege Foundry)**:
  - Implemented formal **Skill Endeavour: Calibrating & Arming the Siege Engines (Resistance 3)** with CRAFT (Strength TN), ATHLETICS (Strength TN), Hjoldring (*Smith* +1d), and explicit payoffs for Grond-Ram (25 Direct Dmg, Prone, -2d Carapace, +4 Noise) and Torsion Ballista (4d vs Target TN, 30 Dmg, Injury TN 22).
  - Added `**BATTLE** (Heart TN)` for chokepoint kill-zone design.
  - Replaced `ATHLETICS TN 14` with `**ATHLETICS** or **CRAFT** (Strength TN)` for cedar barricading.
  - Added `**CRAFT** (Strength TN) or **STEALTH** (Wits TN)` invoking *Burglary* Trait (+1d) for the Master Engineer's Chest.
- **Location 6 (The Hall of the Mauler)**:
  - Replaced `STEALTH TN 16` with `**STEALTH** (Wits TN)` (Ill-favoured on scrap floor, normal on catwalks) / Band **MANOEUVRE** (2d) against **Band TN 15**.
  - Replaced `RIDDLE TN 14` with `**RIDDLE** (Wits TN)` in Forward stance, making the check **Favoured** due to The Mauler's *Dull-Witted* Fell Ability (-1 Hate plus -1 Hate per 6 icon).
  - Added `**HUNTING** or **CRAFT** (Strength TN)` Called Shot to sever master copper carapace wires (-2d Armour).
  - Added `**ATHLETICS** or **CRAFT** (Strength TN)` for dropping 2-ton limestone stalactites (20 Direct Dmg, Prone, -1d Armour, +3 Noise).
- **Location 7 (The Poisoned Halls)**:
  - Replaced flat TN 14 Endurance checks with Protection rolls against Strength TN (Torvir 13, Einar 14, Khoril 13) tested every minute (Ill-favoured unprotected; Eye of Sauron = Dying).
  - Implemented formal **Skill Endeavour: Assembling Squad Respirator Masks (Resistance 3)** with CRAFT (Strength TN), HEALING (Heart TN), Hjoldring (+1d), yielding 4 hours of total immunity for 10 dwarves.
  - Harmonized Scribe identity to **Frár son of Frerin, Scribe of the Third Deep** (Handout #1).
  - Replaced `VALOUR TN 12` with `**AWE** (Strength TN) or **ENHEARTEN** (Heart TN)` for respectful reclaim of ancestral wargear.
  - Added `**ATHLETICS** or **CRAFT** (Strength TN)` for unjamming the ceiling ventilation flue (+3 Noise).
- **Location 8 (The Upper Armoury)**:
  - Purged all occurrences of `+50 Garrison Supply Points` and replaced with authentic campaign rewards: 40 Dwarf Mail-shirts (3d), 30 Heavy Shields (+2 Parry), 50 War-Mattocks/Axes (Damage 6, Injury 18), awarding +2 Band Readiness, 50 Treasure Points in colony tribute, and Royal Renown with King Dáin Ironfoot.
  - Implemented formal **Skill Endeavour: Securing & Padding Heavy Salvage (Resistance 3)** with EXPLORE (Wits TN), CRAFT (Strength TN), ATHLETICS (Strength TN), Hjoldring (+1d), Dúrmer (+1d).
  - Replaced `Craft / Burglary TN 14` with `**CRAFT** (Strength TN) or **STEALTH** (Wits TN)`, invoking *Burglary* Trait (+1d) for Munitions Chest (6 flasks Liquid Fire) and Officer's Locker.
- **Location 9 (The King's Door)**:
  - Replaced `Extended CRAFT Endeavour: Resistance 6, TN 16` with formal **Skill Endeavour: Bypassing the Adamant Runic Lock (Resistance 6)** with CRAFT (Strength TN), STEALTH (Wits TN), RIDDLE (Wits TN), *Burglary* Trait (+1d), Einar's *The Broken Key* (**Favoured**), and Bróga (+1d).
  - Added `**AWARENESS** (Strength TN)` / Band **VIGILANCE** (2d) against **Band TN 15** for detecting Grimnar's overhead ambush.
  - Replaced `VALOUR TN 14` with `**AWE** (Strength TN) or **ENHEARTEN** (Heart TN)` (Favoured +1d for Durin's bloodline) for the Blood of Durin Inscription Ritual.
- **Location 10 (The Lower Armoury / Royal Vault)**:
  - Replaced `Awe / Song (TN 14)` with `**AWE** or **SONG** (Strength TN)` (clears Weary, restores +2 Hope).
  - Replaced `Greed / Shadow Test (Valour TN 14)` with Shadow Test: `**ENHEARTEN** (Heart TN) or **RIDDLE** (Wits TN)` (Ill-favoured for Einar's *Dragon-sickness*).
  - Replaced `Craft / Old Lore (TN 14)` with `**CRAFT** (Strength TN) or **LORE** (Wits TN)` for the runic stasis field.
  - Formalized Durin's Axe Claiming Trigger (+4 Strategic Eye Awareness, Alert Tier 3 Drums in the Deep, 6-round withdrawal countdown).

---

### 2. `04_keyed_locations.md`
- Audited and refactored the entire chapter text across all 10 locations in parallel with `02_keyed_locations.md`.
- Purged all legacy 5e terms (`+2 modifier / Advantage`, `+1 to all Battle rolls`, `Endurance / Healing (TN 14)`, `Burglary TN 14/16`, `Old Lore TN 14`, `Catwalks 14`, `Dread 14`, `Greed 14`).
- Harmonized Scribe name on line 639/760 from *Náli son of Náin* to **Frár son of Frerin, Scribe of the Third Deep** matching `handouts/dying_scribe_letter.md`.
- Replaced Section 4 Summary Table with the Certified TOR 2e Location Summary Matrix.

---

### 3. `handouts/node_map.md`
- Refactored Section 1 elevation cross-section (`Wild Land Travel — TRAVEL [Heart TN]`).
- Refactored Section 2 spatial connection matrix to use `[Attribute TN]` test notation.
- Refactored Section 4 secret bypass ducts table:
  - Purged `Old Lore`, `Burglary 14`, `Customs`, `+2 from Broken Key`.
  - Replaced with TOR 2e test blocks: `EXPLORE (Wits TN, Einar Favoured)`, `EXPLORE (Wits TN, Burglary Trait / Bróga +1d)`, `SCAN (Wits TN)`, `PERSUADE or RIDDLE (Wits TN)`.
- Refactored Section 5 Fighting Withdrawal flowchart:
  - Replaced `Band Clash vs Orc Advance Squad (War vs TN 15)` with `Band WAR 3d vs Band TN 15`.
  - Purged `+50 Garrison Supply Points` and replaced with authentic Moria campaign rewards (40 Mail-shirts, 30 Shields, 50 Mattocks/Axes, +2 Readiness, 50 Treasure tribute, Royal Renown for King Dáin).

---

## Verification Results
- 0 arbitrary fixed TNs on player heroes across all 3 files.
- 0 occurrences of fake skills (`Burglary` as skill, `Sleight`, `Old Lore`, `Customs`, `Dread`, `Greed`, `Catwalks`).
- 0 occurrences of `+50 Garrison Supply Points`.
- 0 occurrences of 5e flat modifiers (`+2 / Advantage`).
- 6 formal Skill Endeavours implemented with explicit Resistance (3 or 6), allowed skills, modifiers, consequences of failure, and degrees of success.
