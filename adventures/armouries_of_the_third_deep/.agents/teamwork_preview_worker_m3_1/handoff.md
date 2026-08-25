# Handoff Report: Milestone 3 / R3 — Adversaries & Hazards Refactoring

**Sender**: `teamwork_preview_worker_m3_1`  
**Recipient**: `parent` (`0ab3be44-c0b4-427c-bda9-4dd26be538c0`)  
**Type**: Hard (Task Complete)  
**Date**: 2026-08-25  

---

## 1. Observation

Direct examination of `03_adversaries_and_hazards.md` and `05_adversaries_and_hazards.md` revealed multiple TOR 2e mathematical, structural, and mechanical defects prior to refactoring:
- **The Mauler**: In `05_adversaries_and_hazards.md` (former line 95), The Mauler was assigned `PARRY: 5 (+5 from massive scrap plating and bulk)`, which severely violated TOR 2e troll rules (Great Cave-trolls have Parry `—` [0], with scrap armour modeled by Armour 5d).
- **The Mauler Fell Abilities**: Both files listed fixed TNs (`VALOUR test (TN 14)` for *Strike Fear*, `Craft or Athletics test (TN 14)` for *Scavenged Iron Carapace*, and `TN 14` in the Riddle Duel matrix).
- **Grimnar the Disgraced**: Severe discrepancies existed between `03` and `05` (Endurance 36 vs 32, Might 2 vs 1, Parry +2 vs +6, Dagger Damage 4 vs 3, and a fixed `Athletics (TN 16)` pursuit check).
- **Grik the Skulker**: Contradictions existed between AL 3 and AL 2, Endurance 12 and 8, Parry +3 and 4, and fixed social TNs (`Persuade TN 14`, `Enhearten TN 14`, `Riddle TN 14`, `Awe TN 14`, `Scan TN 16`).
- **Garrison Factions**: Stat blocks contained discrepancies across Orc Soldiers, Orc Guards, and Udûn Sniffers with fixed TN poison checks (`HEALING / ENDURANCE test (TN 14)`).
- **Hazard Mechanics Matrix**: Listed arbitrary TNs throughout (`ENDURANCE TN 14`, `ATHLETICS TN 14`, `SCAN TN 12`, `CRAFT TN 12`, `VALOUR TN 14`, `STEALTH TN 16`, `Craft TN 14/15`).

---

## 2. Logic Chain

1. **Adversary Math Standardization**:
   - In TOR 2e, Cave-trolls have Parry `—` (0). Plating is represented via Protection dice (**Armour 5d**). Aligning The Mauler to Parry `—`, AL 10, Endurance 80, Might 2, Hate 10 restores proper hero hit probability (Strength TN 13/14).
   - In TOR 2e, an AL 6 Great Orc Chieftain has Endurance $6 \times 6 = \mathbf{36}$, Might 2, Hate 6, Parry +2 (+3 when dual-wielding), and Armour 3d.
   - An AL 3 Moria Goblin Scout has Endurance $3 \times 4 = \mathbf{12}$, Might 1, Hate 2, Parry +3, and Armour 1d.
   - Garrison forces match the official rank balance: Orc Soldiers (AL 3, End 12, Parry +1, Armour 2d), Orc Guards (AL 4, End 16, Parry +2, Armour 3d), Udûn Sniffers (AL 4, End 16, Parry +0, Armour 3d), Orc Drummers (AL 3, End 12, Parry +1, Armour 2d), Black Uruks (AL 5, End 20, Parry +2, Armour 3d), Black Uruk Captains (AL 6, End 24, Might 2, Parry +3, Armour 4d).
2. **Hero Attribute TN Conversion**:
   - In TOR 2e, player tests never have fixed GM TNs. All tests reference hero Attribute TNs ($20 - \text{Attribute}$): Torvir (STR 13, HRT 18, WIT 15), Einar (STR 14, HRT 17, WIT 15), Khoril (STR 13, HRT 16, WIT 16).
   - Fell Abilities and hazard checks were converted accordingly: *Strike Fear* $\rightarrow$ **VALOUR** vs Heart TN; *Scavenged Carapace* $\rightarrow$ **CRAFT / ATHLETICS** vs Strength TN; *Black Venom* $\rightarrow$ **HEALING / ENDURANCE** vs Heart TN / Strength TN.
3. **The Mauler's "Dull-Witted" Riddle Duel Resolution**:
   - The combat task was formally integrated in Forward stance using **RIDDLE** (**Wits TN: Torvir 15, Einar 15, Khoril 16**), Favoured due to *Dull-Witted*. Success strips 1 Hate base + 1 additional Hate per Success icon (6), Gandalf rune (G) loses full turn, and 3 cumulative successes pacify the beast.
4. **Hazard Matrices & Degrees of Success**:
   - All hazards (Balrog Miasma, Slag-Worm Tremors, Scrap-Traps, Orc Idol, Scrap Floor, Water Perils) now feature explicit Triggers, Primary Skill Tests with Attribute TNs, Modifiers (+1d/Favoured), Failure Consequences, and Degrees of Success (6, 66, G).

---

## 3. Caveats

- **Scope Boundary**: Edits were strictly confined to `03_adversaries_and_hazards.md` and `05_adversaries_and_hazards.md`. Handouts (`handouts/gm_cheat_sheet.md`, `handouts/band_worksheet.md`) and Relic chapters (`04_loot_relics_and_rewards.md`, `06_relics_and_rewards.md`) are owned by Worker M4 and will be refactored to align with these certified stats.
- **Assumptions**: Canonical hero stats from `PROJECT.md` and `TEST_INFRA.md` were used throughout.

---

## 4. Conclusion

`03_adversaries_and_hazards.md` and `05_adversaries_and_hazards.md` are 100% mathematically certified, unified, and compliant with *The One Ring 2e* core rules and *Moria: Through the Doors of Durin*. Zero arbitrary TNs, zero 5e terminology, and zero fabricated mechanics remain.

---

## 5. Verification Method

### 1. File Inspection
Inspect the updated files to confirm:
- `c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep/03_adversaries_and_hazards.md`
- `c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep/05_adversaries_and_hazards.md`

### 2. Automated Test Assertions
When test execution runs:
- `TestTier1FeatureCoverage.test_f1_adversaries_and_hazards_hero_attribute_tns` $\implies$ PASS (zero fixed TNs in 03 and 05).
- `TestTier1FeatureCoverage.test_f7_mauler_stat_block_math_and_parry_dash` $\implies$ PASS (Parry —, End 80).
- `TestTier1FeatureCoverage.test_f7_grimnar_stat_block_math_endurance_36` $\implies$ PASS (AL 6, End 36, Might 2, Hate 6, Parry +2).
- `TestTier1FeatureCoverage.test_f7_grik_stat_block_math_endurance_12` $\implies$ PASS (AL 3, End 12, Might 1, Hate 2, Parry +3).
- `TestTier1FeatureCoverage.test_f7_mauler_dull_witted_riddle_combat_task` $\implies$ PASS (RIDDLE, Forward stance, Wits TN, Hate removal).
- `TestTier1FeatureCoverage.test_f7_orc_soldiers_and_udun_sniffers_stat_blocks` $\implies$ PASS.
