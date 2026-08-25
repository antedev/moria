## 2026-08-25T12:41:27Z

You are teamwork_preview_test_writer_e2e_1.
Your working directory is: c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep/.agents/teamwork_preview_test_writer_e2e_1

MANDATORY FIRST STEP:
Read the full authoritative request and project scope at:
- c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep/.agents/ORIGINAL_REQUEST.md
- c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep/PROJECT.md
- c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep/TEST_INFRA.md

YOUR MISSION:
Develop a comprehensive, automated Python E2E validation test harness in `tests/test_tor2e_compliance.py` (and any helper modules in `tests/` or `scripts/`) to systematically verify all 19 markdown files in the module suite against official *The One Ring 2e* core rules, *Moria: Through the Doors of Durin*, and the acceptance criteria in `ORIGINAL_REQUEST.md`.

YOUR WRITE OWNERSHIP:
- `tests/test_tor2e_compliance.py`
- `tests/`
- `scripts/`
- `c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep/TEST_READY.md`

TEST SUITE REQUIREMENTS (4 Tiers):
1. **Tier 1 (Feature Coverage, >=5 per feature)**:
   - Check all 19 files for zero arbitrary hero TNs (e.g. `TN 14`, `TN 16` on player rolls; regex checks ensuring all tests use `(Strength TN)`, `(Heart TN)`, `(Wits TN)`, or named hero TNs).
   - Check that all 18 official skills are valid TOR 2e skills (Awe, Athletics, Awareness, Hunting, Song, Craft, Enhearten, Travel, Insight, Healing, Courtesy, Battle, Persuade, Stealth, Scan, Explore, Riddle, Lore).
   - Check that *Burglary*, *Leadership*, *Enemy-lore*, *Smith*, *Vaultbreaker* are treated as Traits / Distinctive Features, NOT skills.
   - Check that fabricated terms (e.g. `Garrison Supply Points`, `supply points`, `Sleight`, `Old Lore`) are completely absent.
   - Check that Band mechanics specify Readiness 5 / Band TN 15 ($20 - 5$).
   - Check that adversary stat blocks have compliant math (The Mauler Parry `—`, Grimnar End 36 / Parry +2, Grik AL 3 / End 12 / Parry +3).
   - Check that all 6 Skill Endeavours (Loc 2 Fortify, Loc 3 Disarm, Loc 4 Topple, Loc 5 Siege, Loc 7 Respirators, Loc 9 King's Door) have explicit Resistance ratings.
2. **Tier 2 (Boundary & Corner Cases)**:
   - Case-insensitive checks for rogue TNs, formatting edge cases, D&D 5e phrasing (`+2 / Advantage`, `Advantage`, `Disadvantage`).
3. **Tier 3 (Cross-File Consistency)**:
   - Cross-check stats and TNs between module chapters and `handouts/gm_cheat_sheet.md`, `handouts/band_worksheet.md`, `handouts/node_map.md`.
4. **Tier 4 (Real-World Usability)**:
   - Verify every test block contains Failure Consequences and 6-icon Success benefits.

WHEN READY:
- Run the test suite using Python directly (or verify it can execute via python `tests/test_tor2e_compliance.py`).
- Generate `c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep/TEST_READY.md` with test runner command, tier breakdown, and coverage summary.
- Write your handoff to `c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep/.agents/teamwork_preview_test_writer_e2e_1/handoff.md` and send a completion message.
Access files directly without PowerShell.
