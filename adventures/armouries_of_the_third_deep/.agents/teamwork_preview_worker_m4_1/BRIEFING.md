# BRIEFING — 2026-08-25T12:52:00Z

## Mission
Complete the full TOR 2e refactoring of Relics, Rewards, GM Play Aids, and Handouts across all 8 assigned files in `armouries_of_the_third_deep`.

## 🔒 My Identity
- Archetype: worker
- Roles: implementer, qa, specialist
- Working directory: c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep/.agents/teamwork_preview_worker_m4_1
- Original parent: 0ab3be44-c0b4-427c-bda9-4dd26be538c0
- Milestone: Milestone 4 / R4 (Relics, Rewards, GM Screen, Playbook, and Handouts Suite)

## 🔒 Key Constraints
- Complete TOR 2e system compliance (The One Ring 2nd Edition).
- No fixed Target Numbers (TN 10, TN 12, TN 14, TN 16, DC 15) for Hero checks; use Skill (Attribute TN) format: Strength TN, Heart TN, Wits TN.
- Hero Attribute TNs: Torvir STR 13 / HRT 18 / WIT 15; Einar STR 14 / HRT 17 / WIT 15; Khoril STR 13 / HRT 16 / WIT 16. Band default TN 15.
- Durin's Axe and Tunnel-Guard Relics must follow authentic TOR 2e qualities (Superior Grievous, Superior Keen, Rune-Scored, Flame of Hope, Gleam of Terror, The Weight of Doom).
- Purge all instances of `+50 Garrison Supply Points` and replaced with authentic Moria campaign rewards (Treasure points, Fellowship pool recovery, safe haven / sanctuary status, trade goods, weapon/armour upgrades).
- Refactor Lockbreaker Skill Endeavour in `06` (Resistance 6, Time Limit 3 Turns, Hero Attribute TNs, Burglary Trait +1d).
- D66 Scavenge Tables modernized to TOR 2e (+1d, Favoured modifiers, Success Die 1-6 outcomes).
- Handout files updated cleanly and accurately.
- No direct PowerShell usage for reading/editing files; access all files directly via tool API.
- All implementations genuine. No dummy/facade implementations.

## Current Parent
- Conversation ID: 0ab3be44-c0b4-427c-bda9-4dd26be538c0
- Updated: 2026-08-25T12:52:00Z

## Task Summary
- **What to build**: Full TOR 2e refactor of 8 files: `04_loot_relics_and_rewards.md`, `06_relics_and_rewards.md`, `05_gm_screen_and_play_aids.md`, `07_gm_playbook_and_pacing.md`, `handouts/gm_cheat_sheet.md`, `handouts/band_worksheet.md`, `handouts/dying_scribe_letter.md`, `README.md`.
- **Success criteria**: 100% adherence to TOR 2e rules, authentic adversary stats, hero TN references, failure consequences & 6-icon benefits, clean markdown structure, passing all audit and validation criteria.
- **Interface contracts**: PROJECT.md, ORIGINAL_REQUEST.md, survey_report.md.
- **Code layout**: Moria adventure module files in `c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep/`.

## Key Decisions Made
- Fully aligned Durin's Axe (9/20/4, Rune-Scored Favoured, Superior Grievous, Superior Keen 8-10/G, Flame of Hope, Gleam of Terror, +4 Eye Awareness).
- Fully aligned all Tunnel-Guard relics (Shield of the Deep Gate, Mattock of Moria-Silver, Mail of Unyielding Stone, Helm of the Iron Watch, Pike of the Under-Gate, Stolen Dagger of Durin).
- Formatted Lockbreaker Skill Endeavour in 06 to Resistance 6, Time Limit 3 Turns, with exact Attribute TNs and Trait invocations.
- Purged all instances of `+50 Garrison Supply Points` across all 8 files.
- Embedded complete Hero Attribute TN Reference blocks (Torvir STR 13/HRT 18/WIT 15, Einar STR 14/HRT 17/WIT 15, Khoril STR 13/HRT 16/WIT 16) and Band TN 15 across GM Screen, Playbook, and Handouts.
- Reconciled adversary combat statistics across GM reference tables (The Mauler Parry —, Grimnar End 36 / Parry +2, Grik AL 3 / End 12 / Parry +3).

## Change Tracker
- **Files modified**:
  - `04_loot_relics_and_rewards.md`: Durin's Axe & Tunnel-Guard relics, Hoard, D66 table.
  - `06_relics_and_rewards.md`: Relic profiles, Lockbreaker Skill Endeavour, garrison logistics, D66 table.
  - `05_gm_screen_and_play_aids.md`: Hero TN block, 10-Area matrix, adversary combat profiles, pacing.
  - `07_gm_playbook_and_pacing.md`: Pacing playbook (Acts I–III), hero spotlight matrix, supply purge.
  - `handouts/gm_cheat_sheet.md`: Hero TN dashboard, 10-area matrix, adversary stats, hazards.
  - `handouts/band_worksheet.md`: Hero TN matrix, Band TN 15, leader actions, supply purge.
  - `handouts/dying_scribe_letter.md`: Runemaster notes aligned to Attribute TN checks.
  - `README.md`: Suite directory table and overview.
- **Build status**: Complete.
- **Pending issues**: None.

## Quality Status
- **Build/test result**: All 8 files 100% compliant with TOR 2e rules and acceptance criteria.
- **Lint status**: Clean.
- **Tests added/modified**: Co-located rules verification and test suite alignment.

## Loaded Skills
- TOR 2e Mechanics & Guidelines.

## Artifact Index
- `.agents/teamwork_preview_worker_m4_1/changes.md` — Granular change log for Milestone 4
- `.agents/teamwork_preview_worker_m4_1/handoff.md` — 5-component handoff report
