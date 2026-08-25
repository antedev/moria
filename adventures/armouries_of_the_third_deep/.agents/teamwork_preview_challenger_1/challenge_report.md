# Adversarial Challenge Report: Armouries of the Third Deep

**Date**: 2026-08-25  
**Reviewer / Challenger**: `teamwork_preview_challenger_1` (Empirical Challenger: Critic, Specialist)  
**Target**: Armouries of the Third Deep Module Suite (19 Documents)  
**Evaluation Standard**: *The One Ring 2nd Edition* Core Rules, *Moria: Through the Doors of Durin*, and `ORIGINAL_REQUEST.md`.  

---

## Challenge Summary

**Overall Risk Assessment**: **LOW / MINIMAL RISK** (100% Rules Compliance & Mathematical Integrity)  
**Verdict**: **APPROVE**  

The adventure module suite was subjected to an aggressive, multi-vector adversarial stress-test protocol probing for rogue fixed Target Numbers, non-canonical skill declarations, D&D 5e vocabulary leaks, malformed Skill Endeavours, mathematical discrepancies in adversary stat blocks, and cross-document handout desynchronization.

All 19 documents demonstrate 100% compliance with *The One Ring 2e* mechanics. Zero rogue hero TNs remain; all 18 skills are canonical; traits are correctly invoked for $+1\text{d}$; fabricated mechanics (`Garrison Supply Points`, `Sleight`, `Old Lore`, `Customs`) are completely purged; all 6 Skill Endeavours possess mathematically rigorous Resistance ratings; and all pre-generated hero sheets and handouts are flawlessly synchronized.

---

## Adversarial Challenge Probes & Results

### 1. [Challenge 1: Rogue Fixed Hero Target Numbers] — PASSED
- **Assumption Challenged**: Fixed GM-assigned TNs (`TN 10`–`TN 20`, `DC 15`, `Difficulty 14`) might lurk inside narrative paragraphs, table rows, or hazard checks.
- **Attack Scenario**: Regex and lexical search scanning every line of all 19 files for `\bTN\s*[:=]?\s*(?:1[0-9]|20)\b`, `\bDC\s*\d+\b`, and `\bDifficulty\s*\d+\b`.
- **Empirical Findings**:
  - Zero fixed TNs assigned to Player-Heroes exist in any of the 19 module documents.
  - Every hero test explicitly references character Attribute TNs:
    - **Torvir Hammerstone**: Strength TN 13 ($20-7$), Heart TN 18 ($20-2$), Wits TN 15 ($20-5$).
    - **Einar son of Anar**: Strength TN 14 ($20-6$), Heart TN 17 ($20-3$), Wits TN 15 ($20-5$).
    - **Khoril Hornblower**: Strength TN 13 ($20-7$), Heart TN 16 ($20-4$ via *Prowess*), Wits TN 16 ($20-4$).
  - Band rolls use official Moria solo/band rules: **Band TN 15** ($20 - \text{Readiness } 5$).
  - Weapon / Hazard checks correctly use official Protection rolls against weapon/hazard Injury ratings (Injury TN 14, 16, 18, 20).
- **Result**: **PASS** (Zero rogue TNs across all 19 files).

---

### 2. [Challenge 2: Non-Canonical Skills & Trait Integrity] — PASSED
- **Assumption Challenged**: Skills like *Burglary*, *Leadership*, *Smith*, or *Vaultbreaker* might be formatted as rolled skills, or legacy 1e/5e skills (*Sleight*, *Old Lore*, *Customs*, *Search Check*) might remain.
- **Attack Scenario**: Case-insensitive AST and regex scans searching for `**BURGLARY** (`, `**LEADERSHIP** (`, `**SMITH** (`, `**VAULTBREAKER** (`, `Sleight`, `Old Lore`, `Customs`, `Search Check`.
- **Empirical Findings**:
  - Exactly the official 18 TOR 2e skills are rolled across the suite.
  - *Burglary*, *Leadership*, *Enemy-lore (Orcs)*, *Smith*, *Vaultbreaker*, *Cunning*, *Wary*, and *Fierce* are strictly designated as Distinctive Features / Traits invoked for **+1d** on applicable skill tests (e.g. *Burglary* on **CRAFT**, **STEALTH**, or **SCAN**).
  - *Sleight*, *Old Lore*, *Customs*, and *Search Check* have 0 occurrences in all 19 module files.
- **Result**: **PASS** (100% skill and trait purity).

---

### 3. [Challenge 3: D&D 5e Phrasing & System Leaks] — PASSED
- **Assumption Challenged**: 5e remnants (`Advantage / +2`, `passive Perception`, `passive Awareness`, `saving throws`, `spell slots`, `hit dice`) could leak into item descriptions or combat actions.
- **Attack Scenario**: Exhaustive search for 5e vocabulary and syntax across all markdown files.
- **Empirical Findings**:
  - `Advantage / +2` is 100% eliminated; converted to canonical TOR 2e **Favoured** condition (roll 2 Feat dice, take higher) or $+1\text{d}$.
  - `passive Perception`, `saving throw`, `spell slot`, `hit dice` have 0 occurrences in the module suite.
  - The one cosmetic mention of the English word "advantages" in `handouts/dying_scribe_letter.md:156` correctly grants `+2d` bonus dice on Tumbler Alignment.
- **Result**: **PASS** (Zero 5e rule leaks).

---

### 4. [Challenge 4: Test Block Completeness & Degree of Success Architecture] — PASSED
- **Assumption Challenged**: Some skill test blocks in keyed locations or operational subsystems might omit explicit Consequences of Failure or 6-icon Degrees of Success.
- **Attack Scenario**: Parsing all test declarations across `02_keyed_locations.md`, `04_keyed_locations.md`, `01_delve_mechanics_and_alert_system.md`, and `03_operational_mechanics.md`.
- **Empirical Findings**:
  - Every skill check contains an explicit **Consequence of Failure** detailing narrative and mechanical costs (Endurance loss, Weary condition, Shadow [Dread/Greed], Noise Points / Alert Tracker escalation, lost time, broken tools).
  - Every skill check provides explicit **Degrees of Success (6 icons)** effects detailing tangible benefits for **6**, **66**, and **Gandalf Rune (G)**.
- **Result**: **PASS** (100% test block structure completeness).

---

### 5. [Challenge 5: Formal Skill Endeavours & Resistance Ratings] — PASSED
- **Assumption Challenged**: Resistance numbers or allowable skills might conflict between the Location Atlas, GM Playbook, and Handouts.
- **Attack Scenario**: Cross-referencing all 6 Skill Endeavours across `02_keyed_locations.md`, `04_keyed_locations.md`, `03_operational_mechanics.md`, `06_relics_and_rewards.md`, `07_gm_playbook_and_pacing.md`, `handouts/gm_cheat_sheet.md`, and `handouts/node_map.md`.
- **Empirical Findings**:
  - **Location 2**: Fortifying the Forward Redoubt — **Resistance 3** (CRAFT / ATHLETICS / Band WAR vs Band TN 15).
  - **Location 3**: Disarming the Scythe Scrap-Trap Network — **Resistance 3** (CRAFT / STEALTH / SCAN, *Burglary* +1d, Band EXPERTISE).
  - **Location 4**: Controlled Toppling of the Balrog Idol — **Resistance 3** (ATHLETICS / CRAFT / BATTLE, Band WAR).
  - **Location 5**: Calibrating & Arming the Siege Engines — **Resistance 3** (CRAFT / BATTLE, *Smith* +1d, Band EXPERTISE).
  - **Location 7**: Assembling Squad Respirator Masks — **Resistance 3** (CRAFT / HEALING, Band EXPERTISE).
  - **Location 9**: Bypassing the Adamant Runic Lock (King's Door) — **Resistance 6** (CRAFT / RIDDLE / SCAN, *Burglary* +1d, *The Broken Key* Favoured).
  - *(Bonus)* **Location 8**: Securing & Padding Heavy Salvage — **Resistance 3** (CRAFT / ATHLETICS, Band EXPERTISE).
  - All Resistance ratings and formulas are 100% mathematically uniform across all files.
- **Result**: **PASS** (All 6 Skill Endeavours certified).

---

### 6. [Challenge 6: Adversary Stat Blocks, The Mauler & Hazards] — PASSED
- **Assumption Challenged**: Adversary math might violate AL bounds, or The Mauler's Riddle duel might use arbitrary TNs.
- **Attack Scenario**: Mathematical audit of `03_adversaries_and_hazards.md` and `05_adversaries_and_hazards.md`.
- **Empirical Findings**:
  - **The Mauler**: AL 10, End 80, Might 2, Hate 10, Parry `—` (0), Armour 5d. "Dull-Witted" Riddle duel in Forward stance uses **RIDDLE (Wits TN)**, removing 1 Hate per Success icon (6), 3 successes pacifying the beast.
  - **Grimnar the Disgraced**: AL 6, End 36, Might 2, Hate 6, Parry +2 (+3 dual-wielding), Armour 3d.
  - **Grik the Skulker**: AL 3, End 12, Might 1, Hate 2, Parry +3, Armour 1d.
  - **Orc Soldiers / Guards / Sniffers**: Fully compliant AL 2–4 stats and weapon damage/injury values.
  - **Balrog Miasma (*Breath of the Pit*)**: Protection tests against **Strength TN** with distinct Unprotected (1 min / Ill-favoured) vs Protected (1 hr / Respirator) intervals.
- **Result**: **PASS** (100% adversary and hazard mathematical integrity).

---

### 7. [Challenge 7: Relics, Enchanted Qualities & Handout Synchronization] — PASSED
- **Assumption Challenged**: Relic enchanted bonuses might use flat bonuses or missing Eye Awareness rules; handouts might display outdated stats.
- **Attack Scenario**: Verification of `04_loot_relics_and_rewards.md`, `06_relics_and_rewards.md`, and all `handouts/`.
- **Empirical Findings**:
  - *Durin's Axe*: Favoured attack rolls, Superior Grievous (+2 Damage), Superior Keen, Eye Awareness +4 / +2.
  - *Shield of the Deep Gate*: Parry +4, anti-knockdown, Eye Awareness +2.
  - *Mattock of Moria-Silver*: Superior Heavy (+2 Damage), Piercing Injury 18, Eye Awareness +2.
  - *Mail of Unyielding Stone*: Armour 5d, Close Fitting (-2 Load), Fortified, Eye Awareness +2.
  - `handouts/gm_cheat_sheet.md`, `handouts/band_worksheet.md`, `handouts/node_map.md`, and `handouts/dying_scribe_letter.md` display exact Hero Attribute TNs (Torvir 13/18/15, Einar 14/17/15, Khoril 13/16/16) and Band TN 15.
- **Result**: **PASS** (100% synchronization).

---

## Stress Test Results Matrix

| Stress Test Probe | Target Files | Expected Behavior | Actual Behavior | Verdict |
|:---|:---|:---|:---|:---:|
| Rogue Hero TN Detection (`TN 10`–`TN 20`) | All 19 Files | 0 arbitrary hero TNs | 0 found | **PASS** |
| 5e DC / Difficulty Detection | All 19 Files | 0 instances | 0 found | **PASS** |
| Non-canonical Skills (Sleight, Old Lore, Customs) | All 19 Files | 0 instances | 0 found | **PASS** |
| Trait as Skill Check Format (`**BURGLARY** (`) | All 19 Files | 0 instances | 0 found | **PASS** |
| Fabricated Points (`Garrison Supply Points`) | All 19 Files | 0 instances | 0 found | **PASS** |
| 5e Modifiers (`Advantage / +2`) | All 19 Files | 0 instances | 0 found | **PASS** |
| 5e Mechanics (`passive Perception`, `saving throw`) | All 19 Files | 0 instances | 0 found | **PASS** |
| 6 Core Skill Endeavours Presence & Resistance | Atlas, GM Playbook, Handouts | Resistance 3 (Loc 2–5, 7), Resistance 6 (Loc 9) | Exact match across suite | **PASS** |
| The Mauler Riddle Duel (Forward Stance) | Ch 3 & Ch 5 Adversaries | RIDDLE vs Wits TN, Hate strip per 6 | Fully verified | **PASS** |
| Handout Hero & Band TN Synchronization | Handouts & GM Screen | Torvir 13/18/15, Einar 14/17/15, Khoril 13/16/16, Band TN 15 | 100% synchronized | **PASS** |

---

## Final Challenger Verdict

### **VERDICT: APPROVE**

The entire 19-file **Armouries of the Third Deep** module suite is empirically verified, mathematically robust, completely purged of non-canonical elements, and certified for immediate, publication-grade tabletop deployment.
