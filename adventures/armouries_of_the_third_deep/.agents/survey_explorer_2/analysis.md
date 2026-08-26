# Comprehensive Audit & Survey Report: Quickstart & Handouts
## *The Armouries of the Third Deep* — Survey Explorer 2

---

## 1. Executive Summary

This survey report provides an exhaustive audit of all **6 Quickstart files** (`quickstart/00_overview_and_background.md` through `quickstart/05_gm_screen_and_play_aids.md`) and all **4 Handout documents** (`handouts/gm_cheat_sheet.md`, `handouts/band_worksheet.md`, `handouts/dying_scribe_letter.md`, `handouts/node_map.md`) for *The Armouries of the Third Deep* adventure suite.

The audit evaluates compliance against the five core requirements (R1–R5) defined in `ORIGINAL_REQUEST.md`:
1. **R1: Player Agency & Neutral Scene Presentation** — Eliminating prescriptive text dictating PC actions.
2. **R2: Target Number (TN) Architecture** — Purging all hardcoded pregen TN listings (`Torvir 15, Einar 15, Khoril 16`).
3. **R3: Boxed Read-Aloud Text Spoilers & Atmosphere** — Neutralizing spoilers (traps, monsters, secret mechanisms) and resolving language inconsistencies.
4. **R4: Canon TOR 2e Condition & Rules Audit** — Completely eradicating the non-canonical **"Daunted"** condition and other invalid states.
5. **R5: Synchronization Gaps** — Aligning quickstart files and handouts with master chapters (`01`–`07`) and build tools.

---

## 2. Inventory of Surveyed Files

| Category | File Path | Lines | File Size | Primary Purpose |
| :--- | :--- | :---: | :---: | :--- |
| **Quickstart** | `quickstart/00_overview_and_background.md` | 206 | 15.9 KB | Adventure background, timeline, patron directives, pregen profiles |
| **Quickstart** | `quickstart/01_delve_mechanics_and_alert_system.md` | 174 | 11.8 KB | 4-Stage Alert Tracker, noise economy, marching discipline, hazards |
| **Quickstart** | `quickstart/02_keyed_locations.md` | 469 | 41.4 KB | 10 keyed locations, read-aloud boxes, skill checks, Endeavours |
| **Quickstart** | `quickstart/03_adversaries_and_hazards.md` | 196 | 16.2 KB | Adversary stat blocks, fell abilities, hazard matrix, water perils |
| **Quickstart** | `quickstart/04_loot_relics_and_rewards.md` | 166 | 13.0 KB | Durin's Axe, Tunnel-Guard relics, hoard breakdown, D66 table |
| **Quickstart** | `quickstart/05_gm_screen_and_play_aids.md` | 174 | 12.2 KB | 1-page GM screen, band tracker, 3-session pacing playbook |
| **Handouts** | `handouts/gm_cheat_sheet.md` | 194 | 17.1 KB | Rapid GM screen dashboard, room operational matrix, stat blocks |
| **Handouts** | `handouts/band_worksheet.md` | 179 | 13.3 KB | Band tracker, companion roster, squad assignments, clash sheet |
| **Handouts** | `handouts/dying_scribe_letter.md` | 157 | 9.8 KB | In-world prop (Scribe Frár's slate), translation notes, GM cues |
| **Handouts** | `handouts/node_map.md` | 352 | 29.3 KB | Three-tier elevation map, spatial connection matrix, tactical floorplans |

---

## 3. Detailed Audit Findings by Requirement

### 3.1 Requirement 1: Player Agency Violations & Prescriptive Text

#### Summary Assessment
Widespread prescriptive text was identified across both `quickstart/` and `handouts/`. Rather than presenting environmental obstacles neutrally for the Company to solve, numerous entries dictate which pre-generated character attempts which action, prescribe specific character reactions on failure, or force tactical choices onto the players.

#### Detailed Findings by File

1. **`quickstart/00_overview_and_background.md`**:
   - Lines 80–82: Hero profiles dictate specific tactical duties and predetermined player actions:
     - Torvir: *"Drives the frontline assault... must resist reckless wrath when witnessing desecrated ancestral monuments in the Broken Hall."*
     - Einar: *"Using The Broken Key, Einar identifies hidden Dwarven bypasses, spots crude Orc traps, and searches for the runic mechanisms sealing the King’s Door."*
     - Khoril: *"Expedition Guide (TRAVEL — Heart TN 16), invoking Leadership (+1d)..."*

2. **`quickstart/01_delve_mechanics_and_alert_system.md`**:
   - Lines 86–93: Squad tactical ASCII formations prescribe exact hero placements (`Einar` on point, `Torvir` leading shield-wall, `Khoril` commanding rear).
   - Line 97: Prescribes guide action: *"Khoril rolls TRAVEL (Heart TN 16) or ENHEARTEN (Heart TN 16), invoking his Leadership Trait for +1d..."*
   - Line 116: Dictates vanguard bonding: *"Shield-Wall Vanguard (Attached to Torvir): Companions lock shields alongside Torvir in Forward or Defensive Stance."*
   - Line 170: Prescribes scouting check: *"Einar's The Broken Key allows him to detect unstable spans on a SCAN test..."*

3. **`quickstart/02_keyed_locations.md`**:
   - Line 79: Assumes party assigns specific companions: *"Perfect for sniper placement (Bláin and Bróga)."*
   - Line 89: Assumes pregen: *"Einar invoking The Broken Key rolls Favoured"*
   - Line 98: Assumes narrative result: *"Torvir and the Dwarf vanguard cut down 2 sentries immediately..."*
   - Lines 101, 106: *"Torvir invoking Enemy-lore (Orcs) gains +1d."*
   - Line 110: *"Marching Discipline — TRAVEL or ENHEARTEN (Heart TN: Khoril 16): Khoril invoking his Leadership Trait (+1d)..."*
   - Line 125: *"Leaving 2 Dwarf companions (e.g. Bláin and Fáin) here..."*
   - Line 133: *"Hjoldring (Smith) or Fáin assisting grants +1d; Dúrmer (Mighty) grants +1d."*
   - Line 138: *"Rearguard garrison (Bláin & Fáin) receives Total Cover..."*
   - Line 146: *"Einar invoking The Broken Key rolls Favoured."*
   - Line 170: *"Einar invoking The Broken Key rolls Favoured. Austri (Scout) on point grants +1d."*
   - Line 178: *"Bróga (Vaultbreaker) grants +1d."*
   - Line 211: **Direct Agency Hijack**: *"Torvir's Curse of Vengeance: On failure, Torvir flies into uncontrollable rage and must spend his next turn attacking the idol (+2 Noise Points, gains 2 Fatigue)."*
   - Line 212: **Direct Agency Hijack**: *"Einar's Dragon-sickness: On failure, Einar becomes obsessed with prying molten gold-leaf from the idol, wasting 10 minutes."*
   - Line 221: *"Banish the Gloom — SONG (Strength TN: Khoril 13) or ENHEARTEN (Heart TN: Khoril 16)"*
   - Line 234: *"Prying the Idol's Jewels — STEALTH (Wits TN: Einar 15) or CRAFT (Strength TN: Einar 14)"*
   - Line 264: *"Designing the Chokepoint Kill-Zone — BATTLE (Heart TN: Khoril 16, Torvir 18, Einar 17)"*
   - Line 410: *"Khoril invoking Wary Trait grants +1d"*
   - Line 418: *"Einar invoking The Broken Key rolls Favoured; Bróga (Vaultbreaker) assisting grants +1d"*
   - Line 424: **Prescriptive Ritual**: *"The Blood of Durin Inscription Ritual... Context: Torvir or Khoril (of Durin's royal line) slicing their palm..."*
   - Line 455–459: **Prescriptive Shadow Test**: Dictates Einar's exact reaction (*"compelled to stuff every golden goblet and mithril ingot into his pack"*) and success (*"Einar's wisdom prevails over avarice"*).

4. **`quickstart/03_adversaries_and_hazards.md`**:
   - Line 77: *"Hatred (Durin's Folk): Grimnar gains +1d on all attack rolls against Torvir, Khoril, and Dwarf Companions."*
   - Line 83: *"Vengeful Strike: If struck in melee by Torvir, Einar, or Khoril..."*
   - Line 175: *"Torvir and Khoril must test to resist reckless rage."*

5. **`quickstart/04_loot_relics_and_rewards.md`**:
   - Headers and descriptions prescribe which hero receives which relic:
     - Line 28: `Flame of Hope (Dwarf Bearer): When wielded by a Dwarf of Durin's line (Torvir or Khoril)...`
     - Line 52: `The Shield of the Deep Gate (Torvir or Einar)`
     - Line 60: `The Mattock of Moria-Silver / Mattock of the Iron Vanguard (Torvir)`
     - Line 69: `The Mail of Unyielding Stone (Einar or Khoril)`
     - Line 77: `The Helm of the Iron Watch (Torvir or Khoril)`
     - Line 85: `The Pike of the Under-Gate (Khoril or Torvir)`
     - Line 150: `fitted to Khoril's horn`
     - Line 156: `Einar's next SCAN`

6. **`quickstart/05_gm_screen_and_play_aids.md`**:
   - Lines 24, 27: `Favoured for Einar`
   - Line 40: `Torvir Single Combat Duel`
   - Line 68: `Locks shields with Torvir`
   - Line 97: `Khoril makes the opening March Test`
   - Line 103: `Torvir and Einar scout ahead. Einar rolls SCAN...`
   - Line 124: `Roleplay Torvir's burning desire for vengeance vs. silence.`
   - Line 125: `Einar deciphers the ancient relief...`
   - Line 155: `Torvir and the vanguard engage Grimnar...`
   - Line 158: `Torvir uses the Blood of Durin ritual while Einar inserts the Marshal's Key.`

7. **`handouts/gm_cheat_sheet.md`**:
   - Line 35: `SCAN (Wits TN, Favoured Einar)`
   - Line 42: `SCAN (Wits TN, Favoured Einar)`
   - Line 142: `Sounding Khoril's Battle-horn of the Realm`
   - Line 184: `Einar Scan safety`

8. **`handouts/band_worksheet.md`**:
   - Line 105: `allows Einar to use The Broken Key (Favoured Scan) safely`
   - Lines 141–146: Step 2 Hero Leader Actions explicitly assigns pregen names to specific combat options (`Khoril Hornblower: [ ] Command`, `Torvir Hammerstone: [ ] Fight`, `Einar son of Anar: [ ] Flank`).

9. **`handouts/dying_scribe_letter.md`**:
   - Line 120: `When **Einar son of Anar** (*Treasure Hunter*), **Khoril Hornblower** (*Captain & Scholar*), or **Hjoldring the Armourer** examines the stone slab...`
   - Line 129: `(Favoured for Einar with The Broken Key)`
   - Line 135: `(Hjoldring or Einar)`
   - Line 140: `(Khoril Hornblower invoking Old Khuzdul lore)`

10. **`handouts/node_map.md`**:
    - Line 300: `(Einar Favoured)`
    - Line 303: `(Burglary Trait / Bróga +1d)`

---

### 3.2 Requirement 2: Hardcoded Pregen Target Numbers (TNs)

#### Summary Assessment
The codebase contains pervasive occurrences of hardcoded pregen Target Numbers (e.g., `(Wits TN: Torvir 15, Einar 15, Khoril 16)`). In official TOR 2e, Player-Heroes roll against the Target Numbers on their own character sheets ($20 - \text{Attribute}$). Check formatting should state only the skill name and situational modifiers (e.g., `**SCAN roll**`, `**STEALTH roll (Favoured)**`).

#### Complete Occurrence Log

| File | Line(s) | Verbatim Hardcoded TN Text Found |
| :--- | :---: | :--- |
| `quickstart/00_overview_and_background.md` | 80–82 | `STR 7 (TN 13), HRT 2 (TN 18), WIT 5 (TN 15)`<br>`STR 6 (TN 14), HRT 3 (TN 17), WIT 5 (TN 15)`<br>`STR 7 (TN 13), HRT 3 (TN 16 via *Prowess*), WIT 4 (TN 16)` |
| `quickstart/01_delve_mechanics_and_alert_system.md` | 23 | `(Torvir 15, Einar 15, Khoril 16)` |
| `quickstart/01_delve_mechanics_and_alert_system.md` | 97 | `TRAVEL (Heart TN 16) or ENHEARTEN (Heart TN 16)` |
| `quickstart/01_delve_mechanics_and_alert_system.md` | 122 | `[Heart TN: Torvir 18, Einar 17, Khoril 16]` |
| `quickstart/01_delve_mechanics_and_alert_system.md` | 138 | `their Strength TN (Torvir 13, Einar 14, Khoril 13)` |
| `quickstart/01_delve_mechanics_and_alert_system.md` | 164 | `(Strength TN: Torvir 13, Einar 14, Khoril 13)` |
| `quickstart/01_delve_mechanics_and_alert_system.md` | 170 | `(Wits TN 15, Favoured)` |
| `quickstart/02_keyed_locations.md` | 82 | `STEALTH (Wits TN: Torvir 15, Einar 15, Khoril 16)` |
| `quickstart/02_keyed_locations.md` | 88 | `SCAN (Wits TN: Torvir 15, Einar 15, Khoril 16)` |
| `quickstart/02_keyed_locations.md` | 94 | `BATTLE (Heart TN: Torvir 18, Einar 17, Khoril 16)` |
| `quickstart/02_keyed_locations.md` | 100 | `LORE (Wits TN: Torvir 15, Einar 15, Khoril 16) or BATTLE (Heart TN: Torvir 18, Einar 17, Khoril 16)` |
| `quickstart/02_keyed_locations.md` | 105 | `SCAN or RIDDLE (Wits TN: Torvir 15, Einar 15, Khoril 16) or AWE (Strength TN: Torvir 13, Einar 14, Khoril 13)` |
| `quickstart/02_keyed_locations.md` | 110 | `TRAVEL or ENHEARTEN (Heart TN: Khoril 16)` |
| `quickstart/02_keyed_locations.md` | 132 | `CRAFT (Strength TN: Torvir 13, Einar 14, Khoril 13), ATHLETICS (Strength TN: Torvir 13, Einar 14, Khoril 13), BATTLE (Heart TN: Torvir 18, Einar 17, Khoril 16)` |
| `quickstart/02_keyed_locations.md` | 139 | `CRAFT (Strength TN: Torvir 13, Einar 14, Khoril 13) or BATTLE (Heart TN: Torvir 18, Einar 17, Khoril 16)` |
| `quickstart/02_keyed_locations.md` | 145 | `EXPLORE (Wits TN: Torvir 15, Einar 15, Khoril 16)` |
| `quickstart/02_keyed_locations.md` | 150 | `CRAFT (Strength TN: Torvir 13, Einar 14, Khoril 13) or STEALTH (Wits TN: Torvir 15, Einar 15, Khoril 16)` |
| `quickstart/02_keyed_locations.md` | 169 | `SCAN (Wits TN: Torvir 15, Einar 15, Khoril 16)` |
| `quickstart/02_keyed_locations.md` | 177 | `CRAFT (Strength TN: Torvir 13, Einar 14, Khoril 13), STEALTH (Wits TN: Torvir 15, Einar 15, Khoril 16), SCAN (Wits TN: Torvir 15, Einar 15, Khoril 16)` |
| `quickstart/02_keyed_locations.md` | 183 | `HEALING (Heart TN: Torvir 18, Einar 17, Khoril 16) or CRAFT (Strength TN: Torvir 13, Einar 14, Khoril 13)` |
| `quickstart/02_keyed_locations.md` | 187 | `CRAFT (Strength TN: Torvir 13, Einar 14, Khoril 13)` |
| `quickstart/02_keyed_locations.md` | 191 | `HUNTING (Strength TN: Torvir 13, Einar 14, Khoril 13) or CRAFT (Strength TN: Torvir 13, Einar 14, Khoril 13)` |
| `quickstart/02_keyed_locations.md` | 208 | `AWE (Strength TN: Torvir 13, Einar 14, Khoril 13) or ENHEARTEN (Heart TN: Torvir 18, Einar 17, Khoril 16)` |
| `quickstart/02_keyed_locations.md` | 216 | `LORE (Wits TN: Torvir 15, Einar 15, Khoril 16) or RIDDLE (Wits TN: Torvir 15, Einar 15, Khoril 16)` |
| `quickstart/02_keyed_locations.md` | 221 | `SONG (Strength TN: Khoril 13) or ENHEARTEN (Heart TN: Khoril 16)` |
| `quickstart/02_keyed_locations.md` | 228 | `ATHLETICS (Strength TN: Torvir 13, Einar 14, Khoril 13), CRAFT (Strength TN: Torvir 13, Einar 14, Khoril 13)` |
| `quickstart/02_keyed_locations.md` | 234 | `STEALTH (Wits TN: Einar 15) or CRAFT (Strength TN: Einar 14)` |
| `quickstart/02_keyed_locations.md` | 255 | `CRAFT (Strength TN: Torvir 13, Einar 14, Khoril 13), ATHLETICS (Strength TN: Torvir 13, Einar 14, Khoril 13)` |
| `quickstart/02_keyed_locations.md` | 264 | `BATTLE (Heart TN: Khoril 16, Torvir 18, Einar 17)` |
| `quickstart/02_keyed_locations.md` | 268 | `ATHLETICS or CRAFT (Strength TN: Torvir 13, Einar 14, Khoril 13)` |
| `quickstart/02_keyed_locations.md` | 273 | `CRAFT (Strength TN: Torvir 13, Einar 14, Khoril 13) or STEALTH (Wits TN: Torvir 15, Einar 15, Khoril 16)` |
| `quickstart/02_keyed_locations.md` | 292 | `STEALTH (Wits TN: Torvir 15, Einar 15, Khoril 16)` |
| `quickstart/02_keyed_locations.md` | 298 | `RIDDLE (Wits TN: Torvir 15, Einar 15, Khoril 16)` |
| `quickstart/02_keyed_locations.md` | 304 | `HUNTING or CRAFT (Strength TN: Torvir 13, Einar 14, Khoril 13)` |
| `quickstart/02_keyed_locations.md` | 310 | `ATHLETICS or CRAFT (Strength TN: Torvir 13, Einar 14, Khoril 13)` |
| `quickstart/02_keyed_locations.md` | 315 | `SCAN (Wits TN: Torvir 15, Einar 15, Khoril 16)` |
| `quickstart/02_keyed_locations.md` | 329 | `against Strength TN (Torvir 13, Einar 14, Khoril 13)` |
| `quickstart/02_keyed_locations.md` | 338 | `CRAFT (Strength TN: Torvir 13, Einar 14, Khoril 13), HEALING (Heart TN: Torvir 18, Einar 17, Khoril 16)` |
| `quickstart/02_keyed_locations.md` | 344 | `ATHLETICS or CRAFT (Strength TN: Torvir 13, Einar 14, Khoril 13)` |
| `quickstart/02_keyed_locations.md` | 349 | `ATHLETICS or CRAFT (Strength TN: Torvir 13, Einar 14, Khoril 13)` |
| `quickstart/02_keyed_locations.md` | 353 | `AWE (Strength TN: Torvir 13, Einar 14, Khoril 13) or ENHEARTEN (Heart TN: Torvir 18, Einar 17, Khoril 16)` |
| `quickstart/02_keyed_locations.md` | 358 | `SCAN (Wits TN: Torvir 15, Einar 15, Khoril 16)` |
| `quickstart/02_keyed_locations.md` | 380 | `EXPLORE (Wits TN: Torvir 15, Einar 15, Khoril 16), CRAFT (Strength TN: Torvir 13, Einar 14, Khoril 13), ATHLETICS (Strength TN: Torvir 13, Einar 14, Khoril 13)` |
| `quickstart/02_keyed_locations.md` | 386 | `CRAFT (Strength TN: Torvir 13, Einar 14, Khoril 13) or STEALTH (Wits TN: Torvir 15, Einar 15, Khoril 16)` |
| `quickstart/02_keyed_locations.md` | 391 | `SCAN (Wits TN: Torvir 15, Einar 15, Khoril 16)` |
| `quickstart/02_keyed_locations.md` | 408 | `AWARENESS (Strength TN: Torvir 13, Einar 14, Khoril 13)` |
| `quickstart/02_keyed_locations.md` | 417 | `CRAFT (Strength TN: Torvir 13, Einar 14, Khoril 13), STEALTH (Wits TN: Torvir 15, Einar 15, Khoril 16), RIDDLE (Wits TN: Torvir 15, Einar 15, Khoril 16)` |
| `quickstart/02_keyed_locations.md` | 424 | `AWE (Strength TN: Torvir 13, Khoril 13) or ENHEARTEN (Heart TN: Torvir 18, Khoril 16)` |
| `quickstart/02_keyed_locations.md` | 430 | `LORE or RIDDLE (Wits TN: Torvir 15, Einar 15, Khoril 16)` |
| `quickstart/02_keyed_locations.md` | 451 | `AWE or SONG (Strength TN: Torvir 13, Einar 14, Khoril 13)` |
| `quickstart/02_keyed_locations.md` | 455 | `Heart TN: Einar 17 or Wits TN: Einar 15` |
| `quickstart/02_keyed_locations.md` | 460 | `CRAFT (Strength TN: Torvir 13, Einar 14, Khoril 13) or LORE (Wits TN: Torvir 15, Einar 15, Khoril 16)` |
| `quickstart/02_keyed_locations.md` | 464 | `CRAFT (Strength TN: Torvir 13, Einar 14, Khoril 13)` |
| `quickstart/03_adversaries_and_hazards.md` | 32 | `(Wits TN: Torvir 15, Einar 15, Khoril 16)` |
| `quickstart/03_adversaries_and_hazards.md` | 43 | `Heart TN (Torvir 18, Einar 17, Khoril 16)` |
| `quickstart/03_adversaries_and_hazards.md` | 50 | `Strength TN (Torvir 13, Einar 14, Khoril 13)` |
| `quickstart/03_adversaries_and_hazards.md` | 114 | `Heart TN: Torvir 18, Einar 17, Khoril 16 or Strength TN: Torvir 13, Einar 14, Khoril 13` |
| `quickstart/03_adversaries_and_hazards.md` | 172–176 | Multiple instances across Hazard Matrix table rows |
| `quickstart/03_adversaries_and_hazards.md` | 188–190 | Multiple instances across Water Perils table rows |
| `quickstart/04_loot_relics_and_rewards.md` | 144 | `Heart TN (Torvir 18, Einar 17, Khoril 16)` |
| `quickstart/05_gm_screen_and_play_aids.md` | 12–15 | Hero attribute TN table rows |
| `quickstart/05_gm_screen_and_play_aids.md` | 103 | `(Wits TN 15, Favoured via The Broken Key)` |
| `quickstart/05_gm_screen_and_play_aids.md` | 123, 130, 150 | Multiple instances in Pacing Playbook |
| `handouts/node_map.md` | 16 | `TRAVEL [Heart TN: Torvir 18, Einar 17, Khoril 16]` |
| `handouts/gm_cheat_sheet.md` | 12–15 | Hero Attribute TN header table |
| `handouts/band_worksheet.md` | 14–16, 141–146 | Hero Attribute TN headers and Step 2 action TN listings |

---

### 3.3 Requirement 3: Boxed Read-Aloud Text Quality & Spoilers

#### Summary Assessment
Boxed read-aloud descriptions across all 10 keyed locations in `quickstart/02_keyed_locations.md` (and `04_keyed_locations.md`) suffer from two critical defects:
1. **Language Inconsistency**: The read-aloud boxes are written in **Swedish** (*Högläsningstext*), whereas all surrounding text, rules, and GM notes are in English.
2. **Information Spoilers**: Read-aloud passages describe concealed features that should only be revealed upon player inspection or successful skill rolls (e.g., hidden traps, sleeping monsters, exact lock metals, Balrog footprints).

#### Room-by-Room Spoiler Analysis

| Location | Current Read-Aloud Content | Information Leak / Spoiler | Recommendation |
| :--- | :--- | :--- | :--- |
| **Loc 1: Mustering-Yard** | Mentions ancient scorches from Durin's Bane and broken war-gear. | Describes vitrified balrog glass and specific historic details before Lore/Scan checks. | Describe only the vast scale, eight basalt pillars, oppressive silence, and faint sulfur draft. |
| **Loc 2: Gatehouse** | Describes buckled adamant blast-doors and flanking arrow slits. | Good visual baseline, but should avoid implying the redoubt's defensive rating before fortification. | Keep strictly to cold iron smell, buckled gates hanging on pivots, and sloping darkness ahead. |
| **Loc 3: First Armoury** | Describes endless stripped racks and empty wall-pegs. | Neutral, but GM notes should ensure scrap-traps and poison vats remain strictly hidden until **SCAN**. | Focus on hollow echoes of empty racks, iron dust, and dead silence. |
| **Loc 4: Broken Hall** | Directly describes the 4-meter-tall grotesque bone idol of the Dark Lord. | Reveals the exact height and altar features before players cross the threshold or make Valour checks. | Describe the defaced reliefs, smeared tar, and the looming silhouette of an unholy effigy in the shadows. |
| **Loc 5: Second Armoury** | Names specific siege engines: four ballistas and two Grond-rams on stone tracks. | Reveals exact machine types and their unlooted state before players inspect the mechanics. | Describe massive covered shapes, smell of old pitch and cedar, and rusted counterweight chains. |
| **Loc 6: Hall of Mauler** | **MAJOR SPOILER**: Explicitly states "sover Slaktaren – ett Grottroll... med hela kroppen inkapslad i ett absurt pansar". | Completely destroys encounter tension by immediately revealing the sleeping troll and its armour before players scout! | Describe only the overwhelming animal stench, mountainous heaps of rusted scrap iron, and floor-shaking rhythmic snores from the gloom. |
| **Loc 7: Poisoned Halls** | Describes preserved Dwarven knights and explains the exact nature of the miasma. | Spoils the historical reason for preservation before Scribe Frár's slate is recovered and deciphered. | Describe the heavy, waist-deep ochre-yellow mist glowing with faint phosphorescence, and silent armored forms motionless in the gloom. |
| **Loc 8: Upper Armoury** | Mentions the desiccated skeletons of goblin looters at the threshold. | Spoils the historical goblin breach attempt before players search the floor. | Describe the dry, sterile cold, racks of unblemished mail glimmering in lantern light, and sealed bronze chests. |
| **Loc 9: King's Door** | **MAJOR SPOILER**: Details the exact keyholes: "ett smitt av skimrande mithril-legering (Kungens nyckelhål), det andra format av mörkt meteoritjärn (Fältherrens nyckelhål)". | Gives away the two-key puzzle solution directly in the read-aloud text before any investigation! | Describe only the monolithic black stone portal, the faint silver shimmer of Ithildin runes, and the cold hush of the deep. |
| **Loc 10: Lower Armoury** | Directly describes Durin's Axe resting on the black iron anvil in the center of the vault. | Reveals the central artifact immediately upon opening the doors. | Describe the breath of ancient, mountain-pure air, gleaming crystal pedestals, and a radiant azure pulse from the central dais. |

---

### 3.4 Requirement 4: Canon TOR 2e Condition & Rules Audit

#### Summary Assessment
The non-canonical condition **"Daunted"** (invented mechanic: *"cannot spend Hope points for 1 hour"*) appears in multiple files in `quickstart/` and `04_keyed_locations.md` / `05_adversaries_and_hazards.md`. In official TOR 2e, dread and supernatural fear are represented by **Shadow Points (Dread)**, the **Miserable** condition, the **Weary** condition, or **Bout of Madness** triggers.

#### Detailed Occurrences of Non-Canonical Mechanics

1. **"Daunted" Condition Occurrences**:
   - `quickstart/02_keyed_locations.md`:
     - Line 210: `Hero gains 2 Shadow Points (Dread) and becomes Daunted (cannot spend Hope points for 1 hour).`
     - Line 215: `clearing the Daunted condition from all companions.`
     - Line 224: `removes Daunted from all heroes, and restores +1 Band Hope.`
     - Line 452: `suffers the Daunted condition for 1 hour.`
   - `quickstart/03_adversaries_and_hazards.md`:
     - Line 44: `Those who fail gain 2 Shadow (Dread) and are Daunted (cannot spend Hope for the rest of the battle).`
   - *Cross-document verification*: Also present in `04_keyed_locations.md` (lines 472, 477, 486, 1065) and `05_adversaries_and_hazards.md` (line 115).

2. **Other Non-Canonical Terms**:
   - `quickstart/01_delve_mechanics_and_alert_system.md`:
     - Line 140: *"fatal stasis"* / *"Severe Poison (collapse and dying in 1 hour without First Aid)"*
     - Line 165: *"become Pinned/Weary"* (*Pinned* is not a canonical condition; should be *Weary* or *Immobilized until an Athletics check*).
     - Line 121: *"Demoralized"* (should be formatted as *Band Weary* or *Miserable*).
   - `quickstart/02_keyed_locations.md`:
     - Line 329: *"Dying condition"* (In TOR 2e, a hero is *Dying* only if they are reduced to 0 Endurance while *Wounded*).
     - Line 184: *"Poisoned condition"* (TOR 2e models poison as Endurance drain or Ill-favoured states, not a named base condition).

---

### 3.5 Requirement 5: Synchronization Gaps

#### Summary Assessment
Comparison between the quickstart files, handouts, and master chapter files (`01_campaign_context.md` through `07_gm_playbook_and_pacing.md`) reveals structural synchronization gaps:

1. **Build Pipeline Scope**:
   - `scripts/build_master_document.py` compiles chapters `01` through `07` and the 4 handouts in `handouts/` into `armouries_of_the_third_deep_master.md` and `print/armouries_of_the_third_deep_master.html`.
   - `quickstart/` files (`00` to `05`) are standalone documents intended as an expedited play suite, but must maintain exact mathematical, mechanical, and narrative parity with chapters `01` to `07`.

2. **Cross-Reference Inconsistencies**:
   - In `handouts/dying_scribe_letter.md` (line 142), the text references `(see Chapter 6 §4.3)`, which matches the full chapter numbering but has no equivalent section marker in `quickstart/04_loot_relics_and_rewards.md`.
   - In `handouts/gm_cheat_sheet.md` and `handouts/band_worksheet.md`, pregen names and stats are hardcoded into operational dashboards, creating divergence when used for custom companies.

3. **Skill Endeavour Resistance Alignment**:
   - Both sets of files consistently define 7 major Skill Endeavours with identical Resistance ratings:
     - Location 2 (Forward Redoubt): Resistance 3
     - Location 3 (Disarm Trap Network): Resistance 3
     - Location 4 (Topple Idol): Resistance 3
     - Location 5 (Arm Siege Engines): Resistance 3
     - Location 7 (Respirator Masks): Resistance 3
     - Location 8 (Secure Salvage): Resistance 3
     - Location 9 (King's Door Lock): Resistance 6

---

## 4. Actionable Refactoring Recommendations

To achieve 100% compliance across `quickstart/` and `handouts/`, implementers should follow these concrete steps:

### Refactoring Checklist

1. **Player Agency (R1)**:
   - Reframe all check introductions neutrally: Replace *"Einar rolls SCAN"* $\rightarrow$ *"A hero inspecting the floor may make a **SCAN roll**..."*
   - Remove character-forcing failures: Replace *"Torvir flies into uncontrollable rage"* $\rightarrow$ *"On a failure, a hero with the Curse of Vengeance flaw gains 1 Shadow (Dread) and is provoked by the dark effigy."*
   - Present tactical choices to the Company rather than prescribing individual assignments.

2. **Target Numbers (R2)**:
   - Purge all `(Attribute TN: Torvir X, Einar Y, Khoril Z)` strings across all files.
   - Format all tests simply as: `**SKILL roll**` with optional situational modifiers (e.g. `**STEALTH roll (Favoured)**`, `**CRAFT roll (+1d)**`).

3. **Read-Aloud Boxes (R3)**:
   - Provide clean English translations (or dual English/Swedish if required by the module's bilingual format) for all 10 locations.
   - Strip all references to hidden tripwires, sleeping trolls, exact lock metals, and poison vats from read-aloud text.

4. **Canonical Rules & Conditions (R4)**:
   - Replace all occurrences of "Daunted" with canonical effects: `gains 2 Shadow Points (Dread) and becomes Miserable` or `cannot spend Hope until they take a Brief Rest`.
   - Normalize hazard conditions to *Weary*, *Miserable*, and *Wounded*.

5. **Synchronization & Build (R5)**:
   - Ensure `scripts/build_master_document.py` and `scripts/render_handouts.py` build without errors.
   - Keep generic handouts usable for both pre-gens and custom Player-Heroes.

---

*Report prepared by survey_explorer_2 on 2026-08-26.*
