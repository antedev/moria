# BRIEFING — 2026-08-26T05:06:00Z

## Mission
Execute Milestone M2 refactoring across Delve, Band, Operational, Adversary, Hazard, Campaign Context, and Quickstart files to enforce player agency (R1), remove hardcoded pregen TNs (R2), and eliminate non-canonical mechanics (R4, e.g. "Daunted" condition) for 100% strict TOR 2e canon compliance.

## 🔒 My Identity
- Archetype: worker_m2
- Roles: implementer, qa, specialist
- Working directory: c:/Users/ante/Documents/github/Moria/adventures/armouries_of_the_third_deep/.agents/worker_m2
- Original parent: 4520ebd2-4ae5-45e8-aaf7-6750f3bc27b8
- Milestone: M2 (Delve, Band, Operational Mechanics, Adversaries & Hazards, Campaign Overview & Quickstart 00, 01, 03)

## 🔒 Key Constraints
- Exclusive file write ownership:
  - `01_campaign_context.md`
  - `02_band_mechanics.md`
  - `03_operational_mechanics.md`
  - `05_adversaries_and_hazards.md`
  - `quickstart/00_overview_and_background.md`
  - `quickstart/01_delve_mechanics_and_alert_system.md`
  - `quickstart/03_adversaries_and_hazards.md`
- Do not touch files owned by other milestones (M1, M3, M4, E2E).
- Remove all hardcoded pregen Target Number listings (e.g. `(Wits TN: Torvir 15, Einar 15, Khoril 16)`).
- Standardize all skill checks to official TOR 2e notation (`**SKILL roll**` or `**SKILL test**`).
- Remove prescriptive character action scripting; present situations neutrally for player choice.
- Purge the non-canonical "Daunted" condition and replace with official TOR 2e mechanics (Shadow/Dread, Weary, Miserable, Hope loss).
- Audit all adversary stat blocks, fell abilities, combat proficiencies, and hazards.

## Current Parent
- Conversation ID: 4520ebd2-4ae5-45e8-aaf7-6750f3bc27b8
- Updated: 2026-08-26T05:06:00Z

## Task Summary
- **What to build**: Complete refactoring of M2 files to align with TOR 2e canon, player agency, and clean test formatting.
- **Success criteria**: Zero hardcoded pregen TNs, zero "Daunted" occurrences, zero prescriptive scripting in M2 files, strict TOR 2e mechanics.
- **Interface contracts**: `PROJECT.md` and `ORIGINAL_REQUEST.md`

## Key Decisions Made
- Use standard TOR 2e roll notation: `**SKILL roll**` (e.g., `**TRAVEL roll**`, `**ENHEARTEN roll**`, `**STEALTH roll**`, `**BATTLE roll**`, `**SCAN roll**`, `**PROTECTION test**`, `**VALOUR test**`).
- Replace "Daunted" in Strike Fear / Dread effects with official TOR 2e rules: 2 Shadow Points (Dread) and Miserable condition if Shadow >= Hope.
- Neutralized all pregen scripting across tactical formations, March tests, First Aid, and combat adversary tactics.

## Change Tracker
- **Files modified**:
  - `01_campaign_context.md` — Neutralized relic descriptions and journey role TNs.
  - `02_band_mechanics.md` — Neutralized squad formations, march checks, first aid, and leader actions.
  - `03_operational_mechanics.md` — Streamlined alert ladder, standardized noise triggers, refactored miasma & collapse hazards.
  - `05_adversaries_and_hazards.md` — Purged "Daunted", neutralized Mauler & Grimnar tactics, certified all adversary stat blocks and hazard matrices.
  - `quickstart/00_overview_and_background.md` — Neutralized pregen delve roles, cleaned up guide check.
  - `quickstart/01_delve_mechanics_and_alert_system.md` — Modernized alert ladder, squad formations, and hazards.
  - `quickstart/03_adversaries_and_hazards.md` — Purged "Daunted", standardized 5-row hazard matrix and water perils.
- **Build status**: Complete & Verified PASS
- **Pending issues**: None

## Quality Status
- **Build/test result**: All 7 files verified clean; 0 hardcoded pregen check TNs; 0 Daunted occurrences.
- **Lint status**: Clean
- **Tests added/modified**: Verified all test notation patterns and cross-chapter consistency.

## Loaded Skills
- None required directly

## Artifact Index
- `DISPATCH.md` — Assignment instructions
- `BRIEFING.md` — Working state and identity
- `progress.md` — Liveness and step tracking
- `changes.md` — Complete ledger of modifications
- `handoff.md` — 5-component handoff report
