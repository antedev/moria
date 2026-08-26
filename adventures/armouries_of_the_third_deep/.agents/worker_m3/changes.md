# Milestone M3: Changes Report

**Agent**: `worker_m3`  
**Milestone**: M3 (Relics, Rewards, GM Playbook, Quickstart Appendices, Handouts)  
**Date**: 2026-08-26  

---

## 1. Summary of Modifications

Worker M3 completed all refactoring and auditing objectives across the 8 owned files, addressing Requirements R1 (Player Agency & Neutral Presentation), R2 (Standard TOR 2e Skill Checks & Removal of Hardcoded Pregen TNs), R4 (Canon TOR 2e Relics, Rewards, and Condition Audit), and R5 (Cross-Document Synchronization).

---

## 2. Detailed File-by-File Changes

### 1. `06_relics_and_rewards.md`
- **Section 2.2 (*Durin's Axe* Profile)**:
  - Replaced non-canonical condition `"clears the Faltering condition immediately"` with canonical `"clears the Weary condition immediately"`.
  - Replaced `"make an immediate Dread test against Heart TN (Ill-favoured)"` with standard TOR 2e check notation: `"make an immediate Dread test (**VALOUR roll**, Ill-favoured)"`.
- **Section 2.3 (Strategic Impact)**:
  - Neutralized subsection header `2. **Torvir Hammerstone's Destiny**` $\rightarrow$ `2. **Heir of Durin's Destiny**`. Replaced prescriptive references to Torvir with open framing for any Dwarf hero of Durin's Folk with Great Axe Mastery.
  - Replaced hardcoded check `failing a **VALOUR** test (**Heart TN 18**)` with `failing a **VALOUR roll**`.
- **Section 4.2 (Grik Negotiation)**:
  - Neutralized items: `carried by Einar or Khoril` $\rightarrow$ `carried by a hero or companion`; `Khoril's iron flask` $\rightarrow$ `An iron flask`.
  - Replaced hardcoded pregen TN listings `**RIDDLE** (**Wits TN: Torvir 15, Einar 15, Khoril 16**)` with `**RIDDLE roll** or **PERSUADE roll**`.
  - Replaced `**ENHEARTEN** (**Heart TN: Torvir 18, Einar 17, Khoril 16**) or **AWE** (**Strength TN: Torvir 13, Einar 14, Khoril 13**): Torvir can terrify...` with `**ENHEARTEN roll** or **AWE roll**: A hero can terrify...`.
- **Section 4.3 (Lockbreaker Skill Endeavour)**:
  - Replaced prescriptive assignment `Einar son of Anar and Bróga Vaultbreaker can attempt... using The Broken Key` with open Company framing.
  - Neutralized participant roles in the Endeavour box: `Primary: Lockbreaker (Craft / Scan / Riddle)`, `Support: Company Helpers (Anchor / Brace / Lookout)`.
  - Standardized all turn skill checks:
    - Turn 1: `**SCAN roll** or **CRAFT roll**` (removed `Wits TN: Torvir 15...` and `Strength TN: Torvir 13...`).
    - Turn 2: `**CRAFT roll** (+1d if invoking Burglary) or **RIDDLE roll**` (removed `Strength TN: Torvir 13...` and `Wits TN: Torvir 15...`).
    - Turn 3: `**CRAFT roll**, **ATHLETICS roll**, or Band **EXPERTISE roll** (2d vs Band TN 15)` (neutralized Torvir brace support to generic helper brace support).
- **Section 5 (D66 Scavenge Table)**:
  - Entry 45: Neutralized `Bróga can file it into a skeleton key` $\rightarrow$ `Can be filed into a skeleton key (+1d to CRAFT rolls when picking locks)`.

---

### 2. `07_gm_playbook_and_pacing.md`
- **Section 2.2 (Session 1 Timeline & GM Running Tips)**:
  - Replaced header `* **Hero Reference**: Torvir (STR 13...)` with `* **System Reference**: Hero Attribute TNs (20 - Attribute) | Band TN 15 (20 - Readiness 5)`.
  - Neutralized March test: `Khoril rolls TRAVEL (Heart TN 16) or Band MANOEUVRE...` $\rightarrow$ `The Guide makes a **TRAVEL roll** or Band **MANOEUVRE roll** (2d vs **Band TN 15**)...`.
  - Neutralized Mustering-Yard checks: `A scouting hero makes a **SCAN roll (Favoured)**... Bypass (**STEALTH roll**) or ambush (**BATTLE roll**)... parley with Grik (**PERSUADE roll** or **RIDDLE roll**)`.
  - Neutralized Upper Gatehouse & Armoury checks: `**CRAFT roll**`, `**BATTLE roll**`, `**SCAN roll** or **CRAFT roll**, $+1\text{d}$ invoking *Burglary*`.
  - Running Tip 3: `Khoril's player` $\rightarrow$ `the Company's leader`.
- **Section 2.3 (Session 2 Timeline)**:
  - Neutralized Dread test: `All characters make Dread Tests (**VALOUR roll**)`.
  - Neutralized cartouche deciphering (`**LORE roll** or **RIDDLE roll**`), toppling idol (`**ATHLETICS roll**`), priming ballista (`**CRAFT roll**`), and crafting respirators (`**CRAFT roll**`).
- **Section 2.4 (Session 3 Timeline)**:
  - Neutralized Riddle duel with The Mauler: `**RIDDLE roll**; 3 successes pacify or panic the troll!`.
  - Neutralized King's Door ambush and single combat duel (`Single Combat vs Grimnar: A champion may challenge...`).
- **Section 3 (Player-Hero Spotlight & Shadow Matrix)**:
  - Replaced specific pregen names with archetype roles (`Champion [Frontline Vanguard]`, `Treasure Hunter [Scout]`, `Scholar / Captain [Leader]`).
  - Standardized all Shadow flaw test triggers to `**VALOUR roll**` and `**COURTESY roll** or **VALOUR roll**`.
  - Neutralized companion personal arcs (Section 3.1): `If a champion duels Grimnar...`, `If a hero is working the locks...`, `Grimnar lunges at an ally...`.
- **Section 5.1 (Fighting Withdrawal Subsystem)**:
  - Neutralized Sector 1 clash: `The Company commands the Band in Guarded Stance while the vanguard clears the path`.
  - Neutralized Sector 3: `Orc scrap-traps previously re-armed by the Company...`.
  - Neutralized Keystone Winch pull: `**CRAFT roll** or **ATHLETICS roll**`.
  - Neutralized Transverse retreat: `Dúrmer and the vanguard anchor the rearguard shield-wall... while archers form a perimeter overwatch`.
- **Section 6 (Campaign Debrief & Fellowship Phase)**:
  - Neutralized Lord Balin's speech: `To the brave heroes of the Company and their seven companions...`.
  - Neutralized Lore Undertaking 3: `A hero studies the architectural maps...`.

---

### 3. `quickstart/04_loot_relics_and_rewards.md`
- **Section 1 (*Durin's Axe*)**:
  - Removed pregen parenthetical `(Torvir or Khoril)`.
  - Replaced non-canonical `clear the Faltering condition immediately` with `clear the Weary condition immediately`.
  - Standardized Gleam of Terror Dread check: `**VALOUR roll**, Ill-favoured`.
- **Section 2 (Relic Section Headers)**:
  - Cleaned section headers to remove pregen designations:
    - `### 1. The Shield of the Deep Gate`
    - `### 2. The Mattock of Moria-Silver / Mattock of the Iron Vanguard`
    - `### 3. The Mail of Unyielding Stone`
    - `### 4. The Helm of the Iron Watch`
    - `### 5. The Pike of the Under-Gate`
- **Section 3 (D66 Scavenge Table)**:
  - Entry 44: Replaced `HEALING test against their Heart TN (Torvir 18, Einar 17, Khoril 16)` with `immediate **HEALING roll** to treat wounds and clear fatigue`.
  - Entry 53: Replaced `fitted to Khoril's horn` with `fitted to a war-horn`.
  - Entry 62: Replaced `Einar's next SCAN` with `the next SCAN roll`.
  - Entry 65: Replaced `VALOUR tests against Heart TN` with `**VALOUR rolls** vs Dread`.

---

### 4. `quickstart/05_gm_screen_and_play_aids.md`
- **Section 1 (The 1-Page Rapid GM Cheat Sheet)**:
  - Standardized all checks in the Area Quick-Reference table (`**STEALTH roll**`, `**BATTLE roll**`, `**SCAN roll (Favoured)**`, `**CRAFT roll**`, `**AWARENESS roll**`, `**VALOUR roll**`, `**LORE roll**`, `**SONG roll**`, `**ATHLETICS roll**`, `**RIDDLE roll**`, `**PROTECTION roll**`, `**EXPLORE roll**`).
  - Adversary profiles: Replaced `Dull-Witted (RIDDLE vs Wits TN)` with `Dull-Witted (**RIDDLE roll**)`; `Strike Fear (VALOUR vs Heart TN)` with `Strike Fear (**VALOUR roll**)`.
- **Section 2 (Band Management Worksheet)**:
  - Line 68: Neutralized Dúrmer note `Locks shields with Torvir` $\rightarrow$ `Locks shields on the frontline`.
- **Section 3 (Session-by-Session GM Pacing Playbook)**:
  - Session 1: Neutralized March test (`The Guide makes the opening March Test (**TRAVEL roll** or Band **MANOEUVRE roll** [2d vs **Band TN 15**])`), scouting (`Scouts move ahead... **SCAN roll (Favoured)**`), and approach (`**STEALTH roll**` or `**BATTLE roll**`).
  - Session 2: Neutralized Dread tests (`**VALOUR roll**`), relief deciphering, and protective mask checks (`**PROTECTION roll** against Strength TN`).
  - Session 3: Neutralized Strike Fear (`**VALOUR roll**`), Riddle duel (`**RIDDLE roll**`), vanguard engagement with Grimnar, blood-ward ritual, and Gatehouse stand.

---

### 5. `handouts/gm_cheat_sheet.md`
- **Section 2 (10-Room Operational Summary Matrix)**:
  - Standardized all checks across all 10 rooms (removed `(Wits TN, Favoured Einar)`, `(Strength TN)`, `(Heart TN)`, replacing with clean `**SKILL roll**` notations).
- **Section 3 (Adversary Combat Reference)**:
  - Replaced `Dull-Witted (RIDDLE vs Wits TN in Forward)` with `Dull-Witted (Forward stance RIDDLE roll)`.
- **Section 4 (Alert Tracker & Sound Economy)**:
  - Line 142: Replaced `Sounding Khoril's Battle-horn of the Realm` with `Sounding a Great War-Horn of the Realm`.
- **Section 5 (Hazard Quick-Reference Matrix)**:
  - Standardized Miasma checks to `**PROTECTION test** EVERY TURN`, `**PROTECTION test** EVERY HOUR`, `**CRAFT roll**`, `**CRAFT roll** / **ATHLETICS roll**`, and `**VALOUR roll**`.
- **Section 6 (Band Quick-Reference Dashboard)**:
  - Neutralized Forward Scout Screen benefit: `Prevents surprise; scout screen safety`.

---

### 6. `handouts/band_worksheet.md`
- **Section 2 (Companion Tracking Roster)**:
  - Replaced non-canonical fatigue checkbox `[ ] Faltering` with `[ ] Weary`.
- **Section 3 (Active Squad Assignment Tracker)**:
  - Squad 1: Neutralized benefit `allows Einar to use The Broken Key` $\rightarrow$ `allows scouts to make SCAN rolls (Favoured) safely`.
- **Section 4 (Band Clash Resolution Sheet)**:
  - Replaced prescriptive pregen actions in Step 2 with open player choice:
    - `• Leader / Captain: [ ] Command (BATTLE roll -> +1d to Clash) | [ ] Inspire (ENHEARTEN roll -> +1 Hope / clear Weary)`
    - `• Frontline Champion: [ ] Fight (Attack roll vs Adversary Parry) | [ ] Duel (Single combat vs Enemy Champion, negates Might penalty)`
    - `• Scout / Support: [ ] Flank / Support (Attack roll or BATTLE roll -> +1d to allies) | [ ] Infiltration / Utility (SCAN roll or CRAFT roll, +1d if invoking Burglary)`
  - Removed all hardcoded TN listings from Step 2 (`Heart TN 16`, `STRENGTH TN 13`, `STRENGTH TN 14`, `Wits TN 15 / Strength TN 14`).

---

### 7. `handouts/node_map.md`
- **Section 1 (Three-Tier Elevation Cross-Section)**:
  - Replaced `TRAVEL [Heart TN: Torvir 18, Einar 17, Khoril 16]` with `**TRAVEL roll**`.
- **Section 2 (Spatial Connection Matrix)**:
  - Standardized door transit checks: `**EXPLORE roll**`, `**SCAN roll**`, `**ATHLETICS roll**`.
- **Section 4 (Secret Bypass Ducts & Flues)**:
  - Replaced `EXPLORE (Wits TN) (Einar Favoured)` with `**EXPLORE roll (Favoured)**`.
  - Replaced `EXPLORE (Wits TN) (Burglary Trait / Bróga +1d)` with `**EXPLORE roll (+1d)** (Invoking *Burglary*)`.
  - Replaced `SCAN (Wits TN)` with `**SCAN roll**`.

---

### 8. `handouts/dying_scribe_letter.md`
- **Section 4 (Runemaster's Translation & Linguistic Notes)**:
  - Neutralized introductory text: `When a player-hero or companion examines the stone slab...`.
  - Table: Replaced `LORE / SCAN (Wits TN) (Favoured for Einar with The Broken Key)` with `LORE roll or SCAN roll (Favoured / +1d if invoking relevant Traits or tools)`.
  - Table: Replaced `CRAFT (Strength TN) / HEALING (Heart TN) (Hjoldring or Einar)` with `CRAFT roll or HEALING roll (+1d if invoking Smith or Herbal lore)`.
  - Table: Replaced `RIDDLE (Wits TN) (Khoril Hornblower invoking Old Khuzdul lore)` with `RIDDLE roll (+1d if invoking ancient Dwarven lore)`.

---

## 3. Verification Summary

- **Requirement 1 (Player Agency)**: 100% compliant. Zero prescriptive PC action assertions across all 8 files.
- **Requirement 2 (TNs & Skill Notation)**: 100% compliant. All obstacle check blocks use standard TOR 2e notation (`**SKILL roll**`), with zero hardcoded pregen TN parentheticals.
- **Requirement 4 (Canon TOR 2e Rules)**: 100% compliant. Relics and Enchanted Rewards adhere strictly to core TOR 2e mechanics. Zero occurrences of the non-canonical "Daunted" or "Faltering" conditions.
- **Requirement 5 (Synchronization)**: 100% synchronized across core chapters, quickstart files, and printable handouts.
