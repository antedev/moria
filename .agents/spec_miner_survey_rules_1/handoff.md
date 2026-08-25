# Handoff Report: TOR 2e Authoritative Rules & Mechanics Mining

## 1. Observation
- **Authoritative Sources Investigated**:
  - `c:/Users/ante/Documents/Moria/output/quick_indexes/TOR_Moria_2404.jsonl` (Pages 1–237)
    - Lines 39–44: Journey sequence in the dark, Water Peril table (p. 35), Marching tests (p. 37), Eye Awareness & Sound Economy (p. 39: Lesser Noise +1, Loud Noise +2, Powerful Noise +3; Minion escapes +1 to +3), Revelation tables (pp. 40–43: Dire Portents, Orc Assault, Terrors of the Dark, Ghâsh!), Moria-madness Shadow Path (p. 43).
    - Lines 55–71: Fell Foes (Orcs of Moria, Orcs of Udûn, Orcs of Mordor, Black Uruks, Durin's Bane / The Balrog p. 60, Ash-wraiths p. 63, Great Carrion Bats p. 64, Marrow-eaters p. 65, Stone Toads p. 66, Tappers p. 67).
    - Lines 155–160: The Armouries of the Third Deep (Locations 1–10, pp. 151–154; The Mauler troll stat block p. 152; Poison of the Armouries & Durin's Axe p. 154; Goblin Village & Granny Goblin pp. 154–156).
    - Lines 185–190: On Mithril (p. 183), Mithril Enchanted Rewards (p. 184), Moria Magical Treasure Index (p. 185: Marvellous Artefacts & Wondrous Items), Dwarves of Nogrod & Belegost (p. 186).
    - Lines 191–226: Solo and Band Play Rules (Readiness TN $20 - \text{Readiness}$, 5 Dispositions [War, Vigilance, Manoeuvre, Expertise, Rally], Band Hope/Shadow, 5 Injury tiers, 4 Fatigue tiers, Desperate Stand, Battles & Clashes).
  - `c:/Users/ante/Documents/Moria/output/quick_indexes/The_One_Ring_Core_Rules_2401_(Third_Printing).jsonl`
    - Lines 135–140: Skill Endeavours (Resistance 3/6/9, Time Limits), Risk Levels (Standard, Hazardous, Foolish), Sources of Injury (p. 134: Cold, Falling, Fire, Suffocation, Poison), Endurance loss levels (Moderate = Favoured Feat die, Severe = Feat die, Grievous = Ill-favoured Feat die).
    - Lines 145–155: Adversary Stat Block Schema (Attribute Level, Might, Endurance, Hate/Resolve, Parry, Armour, Combat Proficiencies), Special Damage Options (Heavy Blow, Break Shield, Pierce, Seize, Fiery Blow), Fell Abilities Catalog.
- **Specification Report Created**:
  - Full report written to `c:/Users/ante/Documents/Moria/.agents/spec_miner_survey_rules_1/spec_report.md`.

## 2. Logic Chain
1. **Adversary Formatting**: *The One Ring 2e* utilizes a unified single `Attribute Level` ($L$) rather than 3 individual player attributes, which acts as the numerical scaling factor for Heavy Blow ($+L$), special abilities, and threat gauging. Might ($M \in \{1, 2, 3\}$) dictates both attack actions per round and the number of Wounds needed to slay the foe. Hate and Resolve govern stamina and special abilities, where reaching 0 triggers the Weary condition.
2. **Band Engine Integration**: For an 8-dwarf band operating in Moria (e.g. Balin's veterans with Readiness 5), the target number for all group challenges is $\text{Readiness TN} = 20 - 5 = 15$. Group degradation follows strict mathematical thresholds ($\ge 50\%$ incapacitated $\rightarrow$ Band Weary: dice showing 1, 2, 3 yield 0).
3. **Sound Economy & Alert Tracker**: Every tactical action that creates acoustic vibration (combat rounds, shattering portals, blasting stone) or allows enemy scouts to escape directly increases the Company's Eye Awareness. In Moria's Dark Land environment (Hunt Threshold 14), accumulating 14 Eye Awareness immediately triggers a Revelation episode (Orc Assault, Terrors of the Dark, or Balrog Ghâsh!).
4. **Environmental Hazard Mechanics**: The Balrog's venom in the Poisoned Halls and Armouries is classified as a Grievous Poison (damage test every minute unprotected; every hour protected with cloths/herbs). Remediation requires a Healing roll at (-1d) or (-2d), or Craft tests (TN 15) to fashion respirators.
5. **Relic & Lore Architecture**: Durin's Axe provides top-tier weapon traits (*Rune-scored*, *Superior Grievous*, *Superior Keen*, and Dwarf pre-unlocked *Flame of Hope* and *Gleam of Terror*), balanced by a severe campaign-level drawback (+4 Eye Awareness instantly upon claim). The royal vault security is governed by the two split keys (The King's Key in the Last Redoubt, and The Marshal's Key in Goblin Village).

## 3. Caveats
- **PowerShell Execution**: No shell commands were run, strictly honoring the project directive "Access all project files directly without PowerShell".
- **Solo / Band Rules Compatibility**: The Band play mechanics extracted from the Moria supplement seamlessly wrap the core 2e rules, enabling smooth transition between individual Player-Hero actions (Torvir, Einar, Khoril) and collective Band Clashes (the 8 Dwarven allies).

## 4. Conclusion
All five primary investigative areas have been mined, rigorously verified against the official JSONL rulebook indexes, and compiled into `spec_report.md`:
1. Exact TOR 2e Stat Block schema, adversary formulas, and 20+ Fell Abilities.
2. Complete Moria Band system (Readiness TN 15, Dispositions, Fatigue/Injury tiers, Desperate Stand, Battles & Clashes).
3. 4-Stage Alert Tracker (Alert 0–3) seamlessly mapped to the Moria Sound Economy and Eye Awareness rules.
4. Comprehensive Environmental Hazards (Armouries Poison, Water Peril table, fire, suffocation, crafting remedies).
5. Moria Relics & Magic Items (Durin's Axe, Mithril wargear alloys, the Split Keys, War-Horn of the Underworld).

## 5. Verification Method
- Inspect `c:/Users/ante/Documents/Moria/.agents/spec_miner_survey_rules_1/spec_report.md` using `view_file` to verify the presence of all rules, mathematical formulas, and tables.
- Cross-reference specific page excerpts against `c:/Users/ante/Documents/Moria/output/quick_indexes/TOR_Moria_2404.jsonl` (pp. 39–44, 53–71, 151–156, 183–226) and `The_One_Ring_Core_Rules_2401_(Third_Printing).jsonl` (pp. 131–155).
