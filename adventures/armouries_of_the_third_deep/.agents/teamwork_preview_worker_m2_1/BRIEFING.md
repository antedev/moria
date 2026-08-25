# BRIEFING — 2026-08-25T12:46:00Z

## Mission
Execute complete TOR 2e refactoring of Delve Mechanics, Band Systems, Operational Rules, and Campaign Background across 5 owned files (00_overview_and_background.md, 01_campaign_context.md, 01_delve_mechanics_and_alert_system.md, 02_band_mechanics.md, 03_operational_mechanics.md).

## 🔒 My Identity
- Archetype: implementer, qa, specialist
- Roles: [implementer, qa, specialist]
- Working directory: c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep/.agents/teamwork_preview_worker_m2_1
- Original parent: 0ab3be44-c0b4-427c-bda9-4dd26be538c0
- Milestone: M2 (Delve, Band & Operational Mechanics)

## 🔒 Key Constraints
- Zero arbitrary hero Target Numbers (no "TN 14", "TN 16" on player tests); all tests reference the hero's Attribute TN ($20 - \text{Attribute}$).
- All Band tests use Band TN 15 ($20 - \text{Readiness } 5$).
- Purge all instances of `+50 Garrison Supply Points` and replace with authentic narrative/campaign outcomes.
- Purge non-existent skills ("Burglary", "Leadership", "Endurance" rolls) and 5e phrasing ("+2 / Advantage", flat +1/+2 modifiers).
- Maintain 100% integrity: genuine implementations, real state and real behavior, no dummy code.

## Current Parent
- Conversation ID: 0ab3be44-c0b4-427c-bda9-4dd26be538c0
- Updated: 2026-08-25T12:46:00Z

## Task Summary
- **What to build**: Full TOR 2e refactoring across 5 files: `00_overview_and_background.md`, `01_campaign_context.md`, `01_delve_mechanics_and_alert_system.md`, `02_band_mechanics.md`, `03_operational_mechanics.md`.
- **Success criteria**: All fixed TNs purged, Band marching refactored, Balrog gas hazard standardized, supply points purged, non-existent skills and 5e terms purged, Hero Attribute TN matrix embedded. [STATUS: 100% COMPLETE]
- **Interface contracts**: PROJECT.md § Architecture & System Foundation, Survey Report 2.
- **Code layout**: PROJECT.md § Code Layout

## Key Decisions Made
- Embedded Hero Attribute TNs: Torvir (STR 13/HRT 18/WIT 15), Einar (STR 14/HRT 17/WIT 15), Khoril (STR 13/HRT 16/WIT 16).
- Embedded Band TN 15 (Readiness 5).
- Standardized Breath of the Pit exposure tests as Protection tests vs Strength TN (Unprotected: 1 min, Ill-favoured; Protected: 1 hr, standard; Respirators: 4 hrs immunity, Resistance 3 Skill Endeavour).
- Replaced all `+50 Garrison Supply Points` with narrative/campaign vanguard armament and royal recognition.
- Formatted *Burglary*, *Leadership*, *Smith*, *Enemy-lore* as Distinctive Features (Traits) granting +1d on valid TOR 2e skills.

## Change Tracker
- **Files modified**:
  - `00_overview_and_background.md`: Hero table Attribute TNs, Band TN 15, TOR 2e gear and traits.
  - `01_campaign_context.md`: Supply points purged, Quick Matrix updated, Einar/Khoril profiles and gear modernized to TOR 2e, Bróga trait corrected, Relics section updated.
  - `01_delve_mechanics_and_alert_system.md`: Alert 0 stealth test to Wits TN, Marching test refactored to Khoril TRAVEL/ENHEARTEN or Band MANOEUVRE (Band TN 15) with noise escalation/reduction, Band tasks and casualties updated, Breath of the Pit standardized, Slag-worm and collapse tests updated.
  - `02_band_mechanics.md`: Band TN 15 across all roles, Craft TN to Strength TN, supply points purged, First Aid healing to Heart TN / Band Expertise, Marching discipline updated, Hero leader actions and Band Clashes aligned with TOR 2e.
  - `03_operational_mechanics.md`: Alert 0 sentry penalty and Alert 2 door test updated, Toxic Miasma Degradation Matrix and countermeasures standardized to Protection tests vs Strength TN and Resistance 3 Respirator Endeavour, structural collapse and water perils updated.
- **Build status**: All files formatted, validated, and verified.
- **Pending issues**: None.

## Quality Status
- **Build/test result**: PASS. 0 fixed hero TNs, 0 supply points, 0 5e terms.
- **Lint status**: Clean markdown formatting.
- **Tests added/modified**: Verified via regex and pattern matching across all 5 files.

## Loaded Skills
- None required

## Artifact Index
- `.agents/teamwork_preview_worker_m2_1/DISPATCH.md` — Worker dispatch
- `.agents/teamwork_preview_worker_m2_1/BRIEFING.md` — Situational awareness
- `.agents/teamwork_preview_worker_m2_1/progress.md` — Progress tracker and heartbeat
- `.agents/teamwork_preview_worker_m2_1/changes.md` — Detailed changes report
- `.agents/teamwork_preview_worker_m2_1/handoff.md` — 5-component handoff report
