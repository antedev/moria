# BRIEFING — 2026-08-25T12:44:39Z

## Mission
Refactor all 10 keyed locations across 02_keyed_locations.md, 04_keyed_locations.md, and handouts/node_map.md to strict The One Ring 2e (TOR 2e) rules, eliminating 5e artifacts, fixed TNs, fake skills, flat modifiers, and fake reward currencies.

## 🔒 My Identity
- Archetype: worker
- Roles: implementer, qa, specialist
- Working directory: c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep/.agents/teamwork_preview_worker_m1_1
- Original parent: 0ab3be44-c0b4-427c-bda9-4dd26be538c0
- Milestone: Milestone 1 / Keyed Locations Refactor

## 🔒 Key Constraints
- Eliminate all fixed TNs on player-hero tests; replace with standard TOR 2e Attribute TN format with canonical premade TNs (Torvir 13/18/15, Einar 14/17/15, Khoril 13/16/16).
- Use Band Disposition tests against Band TN 15 for adversary passive checks.
- Every skill test specifies: Skill, Attribute TN, Modifiers (Favoured/Ill-favoured/+1d), Consequence of Failure, and Degrees of Success (6 icons).
- Implement formal Skill Endeavours (Resistance 3 and 6) with explicit resistance, allowed skills, failure costs, and success icons for Loc 2, 3, 4, 5, 7, 9.
- Purge fake skills (Burglary as a skill, Sleight, Old Lore, Customs, Dread, Greed, Catwalks) and 5e flat modifiers (+2/Advantage).
- Treat Burglary, Leadership, Smith, etc. as Distinctive Features/Traits granting +1d or automatic action.
- Purge "+50 Garrison Supply Points" and replace with authentic Moria campaign rewards (Experience, Fellowship score, Treasure, Superior Dwarf-forged gear, magical runes, Moria lore/prestige).
- Update summary tables in 04_keyed_locations.md and handouts/node_map.md.
- Write changes.md and handoff.md in working directory.

## Current Parent
- Conversation ID: 0ab3be44-c0b4-427c-bda9-4dd26be538c0
- Updated: 2026-08-25T12:44:39Z

## Task Summary
- **What to build**: Full TOR 2e refactor of 10 keyed locations across 02_keyed_locations.md, 04_keyed_locations.md, and handouts/node_map.md.
- **Success criteria**: Strict compliance with TOR 2e core rules and Moria supplement rules; no remaining fixed TNs on heroes; authentic Skill Endeavours; no 5e mechanics.
- **Interface contracts**: PROJECT.md & survey_report.md
- **Code layout**: Markdown adventure module files in adventures/armouries_of_the_third_deep/

## Change Tracker
- **Files modified**:
  - `02_keyed_locations.md` — Full TOR 2e test block refactor for Locations 1–10, 6 Skill Endeavours, Trait integration.
  - `04_keyed_locations.md` — Full TOR 2e chapter refactor, 6 Skill Endeavours, Scribe Frár harmonization, summary matrix refactor.
  - `handouts/node_map.md` — Refactored elevation cross-section, connection matrix, bypass flues table, and withdrawal flowchart.
  - `changes.md` — Detailed work and changes report.
  - `handoff.md` — 5-component handoff report.
- **Build status**: Complete & Verified (0 illegal patterns found via grep).
- **Pending issues**: None.

## Quality Status
- **Build/test result**: Pass (Grep verification clean for all 18 skills, Attribute TNs, Band TN 15, zero fake skills/rewards).
- **Lint status**: Clean.
- **Tests added/modified**: Verified via regex search across all owned files.

## Loaded Skills
None

## Key Decisions Made
- Replaced all fixed TNs with explicit Attribute TN blocks for Torvir (STR 13/HRT 18/WIT 15), Einar (STR 14/HRT 17/WIT 15), and Khoril (STR 13/HRT 16/WIT 16).
- Formatted 6 major set-piece tasks as formal Skill Endeavours (Resistance 3 and 6).
- Harmonized Scribe identity in Location 7 to *Frár son of Frerin, Scribe of the Third Deep* to match `handouts/dying_scribe_letter.md`.
- Converted *Burglary*, *Smith*, *Leadership*, *Vaultbreaker* into Distinctive Features (Traits) granting +1d.
- Replaced `+50 Garrison Supply Points` with 40 Dwarf Mail-shirts, 30 Heavy Shields, 50 War-Mattocks/Axes (+2 Band Readiness, 50 Treasure Points tribute, Royal Renown with King Dáin Ironfoot).

## Artifact Index
- `changes.md` — Detailed work report
- `handoff.md` — 5-component handoff report
