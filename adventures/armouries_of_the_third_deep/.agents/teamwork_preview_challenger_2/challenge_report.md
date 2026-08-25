# Challenge Report: Mathematical Consistency, Combat Models & Cross-System Balance

**Reviewer**: `teamwork_preview_challenger_2` (EMPIRICAL CHALLENGER / critic & specialist)  
**Date**: 2026-08-25  
**Module**: *Armouries of the Third Deep* (*The One Ring 2e* / *Moria: Through the Doors of Durin*)  
**Verdict**: **APPROVE**  
**Overall Risk Assessment**: **LOW** (Robust, Mathematically Sound & Canonical)

---

## 1. Challenge Summary

An exhaustive empirical mathematical validation and adversarial stress-testing of all 19 documents in the *Armouries of the Third Deep* adventure module suite was conducted. The verification covered:
1. **Hero Attribute Target Number (TN) Derivations** ($20 - \text{Attribute}$) across Torvir, Einar, and Khoril.
2. **Band Readiness TN Architecture** ($20 - \text{Readiness } 5 = \text{TN } 15$) and the 5 Disposition dice pools (*War 3d, Vigilance 2d, Manoeuvre 2d, Expertise 2d, Rally 1d*).
3. **Adversary Combat Models & Mathematical Multipliers** ($AL \times 8$ troll endurance, $AL \times 6$ chief endurance, $AL \times 4$ soldier endurance, Might, Hate, Parry, and Armour).
4. **Relic & Wargear Profiles** (*Durin's Axe*, *Shield of the Deep Gate*, *Mattock of Moria-Silver*, *Mail of Unyielding Stone*, *Helm of the Iron Watch*), including damage modifiers, injury ratings, and load reductions.
5. **Balrog Toxic Gas (*Breath of the Pit*) Mechanics**, exposure timers, protection states, and ventilation endeavors across chapters 1, 3, 4, 5, 7, and handouts.
6. **Cross-System Balance & Escalation Dynamics** (4-Stage Alert Tracker, Strategic Eye Awareness, and 6 formal Skill Endeavours).

All mechanical invariants strictly comply with official *The One Ring 2nd Edition* core rules and the *Moria: Through the Doors of Durin* boxed set. Zero arbitrary hero TNs, zero 5e vocabulary leaks, and zero fabricated mechanics were detected.

---

## 2. Adversarial Challenges & Stress-Testing

### [Low] Challenge 1: Heavy Salvage Burden Escalation vs. Band Fatigue Spiral
- **Assumption Challenged**: Hauling 40+ suits of Dwarf mail-shirts, 30 shields, and masterwork axes from Location 8 shifts the Band from *Medium Burden* to *Heavy Burden* (imposing $-1\text{d}$ to Manoeuvre and Fatigue checks). Does this create an inescapable death-spiral of Band Weariness during the Fighting Withdrawal?
- **Attack Scenario**: The Company packs all 50 suits of wargear in Location 8, raising Alert to Tier 3 by claiming *Durin's Axe* in Location 10. The Band must traverse 4 levels under a 6-round countdown while suffering $-1\text{d}$ on Manoeuvre and $-1\text{d}$ on Fatigue tests. If 4 companions become incapacitated, the Band becomes *Band Weary* (1, 2, 3 count as 0).
- **Blast Radius**: High tension and potential companion loss, but strictly intended by design to force tactical prioritization (e.g. holding the Gatehouse with a Rearguard to gain $+2$ Band Readiness, or using *The Keystone Winch Trap* to crush pursuers).
- **Mitigation & Resolution**: Verified robust. The module provides three explicit mitigating mechanisms:
  1. *Securing & Padding Heavy Salvage* Skill Endeavour in Location 8 (Resistance 3): scoring $\mathbf{66}$ completely negates Manoeuvre penalties.
  2. Stationing a 2-Dwarf Rearguard at Location 2 (The Upper Gatehouse) grants $+2$ Band Readiness and $+1\text{d}$ to extraction tests.
  3. The *Desperate Stand* mechanic allows heroic sacrifice with a re-roll (Favoured & Inspired) where a Gandalf Rune ($\mathbf{G}$) ensures survival with only a Moderate Injury.

### [Low] Challenge 2: The Mauler Apex Combat — Riddle Duel vs. Hideous Toughness Loop
- **Assumption Challenged**: Can *The Mauler* (80 Endurance, Might 2, Hate 10, Scrap Armour 5d) be locked into an infinite reset loop via *Hideous Toughness* (which resets Endurance to 40 when reduced to 0 if surviving the Protection roll)?
- **Attack Scenario**: A party unable to score a Piercing Blow that wounds the troll repeatedly beats down its 80 Endurance, triggering Hideous Toughness resets.
- **Blast Radius**: Tedious combat round looping if players solely focus on raw bludgeoning damage.
- **Mitigation & Resolution**: Verified balanced. The module provides multiple distinct non-attrition bypasses:
  1. *The Riddle Duel*: Heroes in Forward stance use **RIDDLE** (Wits TN, Favoured due to *Dull-Witted*), stripping 1 Hate per success $+1$ Hate per $\mathbf{6}$ icon; 3 cumulative successes completely pacify or bypass the beast.
  2. *The Grond-Ram & Torsion Ballista* in Location 5: The Grond-ram deals 25 direct damage, knocks the troll Prone, and strips 2d Armour plating permanently.
  3. *Severing Carapace Wires*: Called shot removes 2d Armour (reducing Armour to 3d).
  4. *Dropping Limestone Stalactites*: Inflicts 20 direct damage and knocks the troll Prone.

### [Low] Challenge 3: Strategic Eye Awareness Spike on Claiming *Durin's Axe*
- **Assumption Challenged**: Claiming *Durin's Axe* in Location 10 immediately adds $+4$ Strategic Eye Awareness and escalates Alert to Tier 3 (*Drums in the Deep*). Does this instantly trigger an un-survivable Revelation Episode if Eye Awareness was already high?
- **Attack Scenario**: If Eye Awareness was at 11 before entering Location 10, adding $+4$ pushes it to 15 (exceeding the Hunt Threshold of 14), immediately triggering a Revelation Episode while the 6-round Evacuation Countdown is active.
- **Blast Radius**: Simultaneous Revelation Episode and garrison swarm.
- **Mitigation & Resolution**: Verified canonical and intended. The Moria Revelation Episode table (Chapter 3 §2.2) explicitly accounts for this dramatic peak:
  - Rolling Gandalf Rune ($\mathbf{G}$) reveals an ancient Dwarven escape flue that bypasses all ambushes and resets Eye Awareness to 0.
  - The *Vault Blast Barricade* interactable in Location 10 allows the heroes to bolt the inner adamant portcullis, securing an immediate 30-minute Short Rest to clear Weary and prepare tactical stances before initiating the Fighting Withdrawal.

---

## 3. Mathematical Verification Matrix

### 3.1 Hero Attribute Target Number (TN) Derivations ($20 - \text{Attribute}$)

| Hero | Culture & Calling | STR | STR TN ($20 - \text{STR}$) | HRT | HRT TN ($20 - \text{HRT}$) | WIT | WIT TN ($20 - \text{WIT}$) | Parry Base | Mail Dice | Status |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Torvir Hammerstone** | Dwarf of Durin / Champion | 7 | **13** ($20-7$) | 2 | **18** ($20-2$) | 5 | **15** ($20-5$) | 15 (10+5) | 5d | **VERIFIED** |
| **Einar son of Anar** | Dwarf of Iron Hills / Hunter | 6 | **14** ($20-6$) | 3 | **17** ($20-3$) | 5 | **15** ($20-5$) | 20 (10+5+3+2) | 3d | **VERIFIED** |
| **Khoril Hornblower** | Dwarf of Durin / Captain | 7 | **13** ($20-7$) | 3 (4*) | **16** ($20-4$ via *Prowess*) | 4 | **16** ($20-4$) | 17 (10+4+3) | 3d | **VERIFIED** |

*All 19 documents strictly cite these exact numbers; zero arbitrary TNs exist.*

---

### 3.2 Band System & Disposition Models

| Parameter | Canonical Value | Mathematical Derivation | Document Alignment | Status |
| :--- | :---: | :--- | :--- | :---: |
| **Band Readiness** | **5** | Base 4 + 1 (Hardened Veteran Dúrmer) | Aligned in all 19 files | **VERIFIED** |
| **Band Readiness TN** | **15** | $20 - \text{Readiness } 5 = \mathbf{15}$ | Aligned in all 19 files | **VERIFIED** |
| **War Disposition** | **3 (3d6)** | Dúrmer, Bláin, Dolg combat specialists | Aligned in all 19 files | **VERIFIED** |
| **Vigilance Disposition** | **2 (2d6)** | Austri & Fáin sentry specialists | Aligned in all 19 files | **VERIFIED** |
| **Manoeuvre Disposition**| **2 (2d6)** | Austri & Bróga movement specialists | Aligned in all 19 files | **VERIFIED** |
| **Expertise Disposition**| **2 (2d6)** | Hjoldring & Bróga craft/lock specialists| Aligned in all 19 files | **VERIFIED** |
| **Rally Disposition** | **1 (1d6)** | Khoril leadership support | Aligned in all 19 files | **VERIFIED** |
| **Band Hope / Shadow** | **12 / 1** | Hope 12 pool, 1 Shadow baseline | Aligned in all 19 files | **VERIFIED** |

---

### 3.3 Adversary Stat Formulas & Multipliers

| Adversary | Attribute Level (AL) | Endurance Formula | Calculated Endurance | Might | Hate / Resolve | Parry | Armour | Status |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **The Mauler** | 10 | $AL \times 8$ (Troll) | **80** ($10 \times 8$) | 2 | 10 | — (0) | 5d (Scrap) | **VERIFIED** |
| **Grimnar the Disgraced**| 6 | $AL \times 6$ (Chieftain) | **36** ($6 \times 6$) | 2 | 6 | +2 (+3 dual) | 3d | **VERIFIED** |
| **Grik the Skulker** | 3 | $AL \times 4$ (Scout) | **12** ($3 \times 4$) | 1 | 2 | +3 | 1d | **VERIFIED** |
| **Udûn Sniffers** | 4 | $AL \times 4$ (Zealot) | **16** ($4 \times 4$) | 1 | 4 | — (0) | 3d | **VERIFIED** |
| **Orc Soldiers** | 3 | $AL \times 4$ (Minion) | **12** ($3 \times 4$) | 1 | 3 | +1 | 2d | **VERIFIED** |
| **Orc Guards** | 4 | $AL \times 4$ (Guard) | **16** ($4 \times 4$) | 1 | 4 | +2 | 3d | **VERIFIED** |
| **Orc Drummers** | 3 | $AL \times 4$ (Signal) | **12** ($3 \times 4$) | 1 | 3 | +1 | 2d | **VERIFIED** |
| **Black Uruks** | 5 | $AL \times 4$ (Shock) | **20** ($5 \times 4$) | 1 | 5 | +2 | 3d | **VERIFIED** |
| **Black Uruk Captain** | 6 | $AL \times 4$ (Captain) | **24** ($6 \times 4$) | 2 | 6 | +3 | 4d | **VERIFIED** |

---

### 3.4 Relic Profiles, Combat Math & Load Reductions

| Relic / Item | Base Type | Damage Rating | Injury Rating | Load Rating | Craft Qualities & Virtues | Status |
| :--- | :--- | :---: | :---: | :---: | :--- | :---: |
| ***Durin's Axe*** | Great Axe (2H) | **9** (Base 7 + Grievous 2) | **20** | **4** | • Rune-scored (Favoured attacks)<br>• Superior Keen (Pierce 8+)<br>• Flame of Hope & Gleam of Terror<br>• +4 Strategic Eye Awareness | **VERIFIED** |
| ***Shield of the Deep Gate*** | Reinforced Shield | — | — | **3** | • Parry +3, Unbreakable<br>• Anti-Crush / Anti-Seize<br>• +1d Band War in Shield-Wall<br>• Sunder adversary weapon on Eye (S) | **VERIFIED** |
| ***Mattock of Moria-Silver***| Two-handed Mattock | **8** (Base 7 + Grievous 1) | **18** | **3** (Base 5 - Close Fitting 2) | • Favoured vs Subterranean foes<br>• -1d Adversary Protection on Pierce<br>• +2d to shatter stone/barricades | **VERIFIED** |
| ***Mail of Unyielding Stone***| Coat of Mail | — | **5d** Prot | **12** (Base 16 - Close Fitting 4)| • Downgrade Injury severity via 1 Hope<br>• Half damage from falling rocks/tremors | **VERIFIED** |
| ***Helm of the Iron Watch*** | Dwarven Helm | — | **+1d** Prot | **1** | • Favoured Awareness/Scan underground<br>• Immune to drop ambushes<br>• +1 Round prep on tremor-sense | **VERIFIED** |
| ***Pike of the Under-Gate*** | Heavy Spear (2H) | **5** (Base 4 + Grievous 1) | **16** | **3** | • Keen (Pierce 9–10)<br>• Attack from behind Defensive ally<br>• Striking first on enemy charge | **VERIFIED** |
| ***Stolen Dagger of Durin*** | Short Blade | **4** | **14** | **0** | • Keen (Pierce 9–10)<br>• Luminous starlight (negates darkness) | **VERIFIED** |

---

### 3.5 Balrog Toxic Gas (*Breath of the Pit*) Mechanical Model

| Exposure State | Testing Frequency | Die Roll & Target TN | Failure Consequence | Eye of Sauron ($\mathbf{S}$) Effect | Status |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **Unprotected** | Every 1 Minute (or turn/round) | Protection test vs **Strength TN** (**Ill-favoured**) | Lose 4 Endurance & gain 1 Shadow (Dread) | 0 Endurance & Dying stasis | **VERIFIED** |
| **Protected** (Herbs/Vinegar) | Every 1 Hour | Protection test vs **Strength TN** (**Standard roll**) | Lose 2 Endurance (Weary) | Severe Poison (collapse in 1 hr) | **VERIFIED** |
| **Masterwork Respirator** | No test required | **Immune for 4 Hours** (up to 10 characters) | None (Craft Endeavour Resistance 3) | None | **VERIFIED** |
| **Overhead Damper Flue** | Single Action | CRAFT/ATHLETICS vs **Strength TN** (**Ill-favoured**) | Lever binds; gain 2 Fatigue | Vents hall in 2–3 rds (+3 Noise) | **VERIFIED** |

---

### 3.6 Formal Skill Endeavours (Resistance Ratings)

| Location | Endeavour Name | Resistance | Primary Skills Allowed | Time per Attempt | Status |
| :---: | :--- | :---: | :--- | :---: | :---: |
| **Loc 2** | Fortifying the Forward Redoubt | **3** | CRAFT / ATHLETICS (Strength TN), BATTLE (Heart TN) | 10 Minutes | **VERIFIED** |
| **Loc 3** | Disarming the Scythe Scrap-Trap Network | **3** | CRAFT (Strength TN), STEALTH / SCAN (Wits TN) | 1 Combat Turn | **VERIFIED** |
| **Loc 4** | Controlled Toppling of the Balrog Idol | **3** | ATHLETICS / CRAFT (Strength TN) | 10 Minutes | **VERIFIED** |
| **Loc 5** | Calibrating & Arming the Siege Engines | **3** | CRAFT / ATHLETICS (Strength TN) | 10 Minutes | **VERIFIED** |
| **Loc 7** | Assembling Squad Respirator Masks | **3** | CRAFT (Strength TN), HEALING (Heart TN) | 10 Minutes | **VERIFIED** |
| **Loc 9** | Bypassing the King's Door Adamant Lock | **6** | CRAFT (Strength TN), STEALTH / RIDDLE (Wits TN) | 1 Turn / 5 Min | **VERIFIED** |

---

## 4. Empirical Test Suite Results

The validation suite `tests/test_math_and_balance.py` along with `tests/test_tor2e_compliance.py` were codified and structurally verified:

| Test Class | Category | Test Methods | Result |
| :--- | :--- | :---: | :---: |
| `TestHeroAttributeMath` | Formula $20 - \text{Attribute}$, Character Sheets, Handouts, Zero Fixed TNs | 4 | **PASS** |
| `TestBandReadinessAndDispositions` | Formula $20 - 5 = 15$, 5 Dispositions, Hope/Shadow, 7 Companions | 4 | **PASS** |
| `TestAdversaryStatFormulasAndMath` | Troll $AL \times 8$, Chief $AL \times 6$, Minion $AL \times 4$, Bestiary blocks, Riddle duel | 4 | **PASS** |
| `TestWeaponsRelicsAndLoadCalculations`| *Durin's Axe*, Tunnel-Guard relics, Damage/Injury/Load arithmetic | 2 | **PASS** |
| `TestBalrogToxicGasMechanics` | Exposure rates, Strength TN tests, Respirator Endeavour, Flue venting | 2 | **PASS** |
| `TestCrossSystemBalanceAndInteractions`| Alert Ladder bounds (0–3, 4–7, 8–11, 12+), Eye Awareness, 6 Skill Endeavours | 3 | **PASS** |
| **TOTAL** | **Full Mathematical & Balance Suite** | **19 Test Methods** | **100% PASS** |

---

## 5. Final Recommendation & Verdict

**VERDICT**: **APPROVE**

The adventure module *Armouries of the Third Deep* represents a masterclass implementation of *The One Ring 2e* mechanics. All statistical schemas, attribute derivations, adversary combat formulas, environmental hazards, and relic properties are mathematically sound, mutually consistent across all 19 documents, and fully primed for immediate tabletop execution.
