# E2E Test Infra: The Armouries of the Third Deep

## Test Philosophy
- **Requirement-Driven & Opaque-Box**: Derived strictly from `ORIGINAL_REQUEST.md` (Requirements R1 through R7 and Acceptance Criteria), independent of internal authoring style.
- **Methodology**: Systematic 4-tier testing framework:
  1. **Tier 1 - Feature Coverage**: Direct verification of every discrete requirement and feature (F01–F26) with >=5 specific test assertions per feature area.
  2. **Tier 2 - Boundary & Corner Cases**: Edge conditions (e.g. Band casualty threshold, Alert level 3 overflow, toxic mask failure, zero Hope, maximum Eye Awareness, Riddle duel failures).
  3. **Tier 3 - Cross-Feature Combinations**: Pairwise and multi-feature interactions (e.g. Band stealth rolls in Alert 2; horn blast noise triggering patrol + eye awareness; Mauler combat with catwalk collapse + Band phalanx).
  4. **Tier 4 - Real-World Application Scenarios**: Full multi-session walkthroughs from Descent (Act I) through King's Door / Durin's Axe claiming and Fighting Withdrawal (Act III).

## Feature Inventory & Test Coverage Goals
| # | Feature | Requirement Source | Tier 1 (Min Cases) | Tier 2 (Boundaries) | Tier 3 (Interactions) | Tier 4 (Workloads) |
|---|---------|-------------------|:------------------:|:-------------------:|:---------------------:|:------------------:|
| F01 | 3-Act Narrative Architecture | ORIGINAL_REQUEST §R1 | 5 | 5 | ✓ | Scenario 1, 2, 3 |
| F02 | Squad-Level Delve & Pacing | ORIGINAL_REQUEST §R1 | 5 | 5 | ✓ | Scenario 1, 2, 3 |
| F03 | Player-Hero Integration | ORIGINAL_REQUEST §R1 | 5 | 5 | ✓ | Scenario 1, 2 |
| F04 | 7-Dwarf Companion Band | ORIGINAL_REQUEST §R2 | 5 | 5 | ✓ | Scenario 1, 2, 3 |
| F05 | Band Rules Integration | ORIGINAL_REQUEST §R2 | 5 | 5 | ✓ | Scenario 2, 3 |
| F06 | Tactical Band Roles | ORIGINAL_REQUEST §R2 | 5 | 5 | ✓ | Scenario 1, 2, 3 |
| F07 | Band Stealth & Marching | ORIGINAL_REQUEST §R2 | 5 | 5 | ✓ | Scenario 1, 2 |
| F08 | 10 Keyed Locations | ORIGINAL_REQUEST §R3 | 10 (1/room) | 10 (1/room) | ✓ | Scenario 1, 2, 3 |
| F09 | 4-Stage Alert Tracker | ORIGINAL_REQUEST §R4 | 5 | 5 | ✓ | Scenario 1, 2, 3 |
| F10 | Sound Action Economy | ORIGINAL_REQUEST §R4 | 5 | 5 | ✓ | Scenario 1, 2, 3 |
| F11 | Einar's Broken Key Utility | ORIGINAL_REQUEST §R4 | 5 | 5 | ✓ | Scenario 2 |
| F12 | Khoril's Battle-Horn Utility | ORIGINAL_REQUEST §R4 | 5 | 5 | ✓ | Scenario 3 |
| F13 | Relic Attunement Constraints | ORIGINAL_REQUEST §Context | 5 | 5 | ✓ | Scenario 1, 2, 3 |
| F14 | The Mauler Stat Block & Arena | ORIGINAL_REQUEST §R5 | 5 | 5 | ✓ | Scenario 3 |
| F15 | Grimnar the Disgraced | ORIGINAL_REQUEST §R5 | 5 | 5 | ✓ | Scenario 3 |
| F16 | Grik the Skulker | ORIGINAL_REQUEST §R5 | 5 | 5 | ✓ | Scenario 2 |
| F17 | Orc Patrols & Sentries | ORIGINAL_REQUEST §R5 | 5 | 5 | ✓ | Scenario 1, 2, 3 |
| F18 | Environmental Hazards | ORIGINAL_REQUEST §R5 | 5 | 5 | ✓ | Scenario 2, 3 |
| F19 | Durin's Axe Artifact | ORIGINAL_REQUEST §R6 | 5 | 5 | ✓ | Scenario 3 |
| F20 | Tunnel-Guard Wargear | ORIGINAL_REQUEST §R6 | 5 | 5 | ✓ | Scenario 2, 3 |
| F21 | The Marshal's Key | ORIGINAL_REQUEST §R6 | 5 | 5 | ✓ | Scenario 2, 3 |
| F22 | D66 Moria Scavenge Table | ORIGINAL_REQUEST §R6 | 6 | 6 | ✓ | Scenario 1, 2 |
| F23 | Rapid GM Cheat Sheet | ORIGINAL_REQUEST §R7 | 5 | 5 | ✓ | Play Aid Verification |
| F24 | Band Management Worksheet | ORIGINAL_REQUEST §R7 | 5 | 5 | ✓ | Play Aid Verification |
| F25 | ASCII Elevation Node Map | ORIGINAL_REQUEST §R7 | 5 | 5 | ✓ | Play Aid Verification |
| F26 | Session-by-Session Playbook | ORIGINAL_REQUEST §R7 | 5 | 5 | ✓ | Play Aid Verification |

## Verification Harness & Test Execution Plan
- The E2E Testing Track will build an automated inspection and verification harness (e.g. Python verification script or structural test suite) that validates:
  1. File completeness and layout compliance in `c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep/`.
  2. All 10 locations contain boxed read-aloud text, GM sensory bullets (Lighting, Drafts, Echoes, Smells), interactables, and TOR 2e skill TNs.
  3. All adversary stat blocks conform mathematically to TOR 2e rules (Attribute Level, Endurance, Might, Hate, Parry, Armour, Proficiencies, Fell Abilities).
  4. Band rules (Band Readiness 5, Dispositions, Roles, Fatigue, Morale) are comprehensively specified and usable.
  5. Alert tracker (Alert 0–3), Sound Action Economy, and Eye Awareness rules are fully articulated.
  6. All relics, D66 table (36 items), and GM play aids exist and contain no placeholders.
- When the test suite is ready, the testing orchestrator publishes `TEST_READY.md`.
