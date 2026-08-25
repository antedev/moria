# Project Orchestrator Master Plan

## Project: Tabletop Adventure Module — Armouries of the Third Deep (TOR 2e)
Target Path: `c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep`

### Overview & Objectives
Build a 2–3 session adventure module for The One Ring 2e (TOR 2e) fulfilling all requirements R1 to R7 from `ORIGINAL_REQUEST.md`.

### Phase 0: Survey & Spec Mining (Parallel Discovery)
Spawn 3 parallel agents:
1. `teamwork_preview_spec_miner` (Survey 1 - System & Rules): Mine TOR 2e mechanical rules, adversary stats, band rules, eye awareness, hazards from `rulebook.jsonl`, `TOR_Moria_2404.pdf`, `Source_Material/`.
2. `teamwork_preview_spec_miner` (Survey 2 - Narrative & Campaign): Mine `campaign_log.md`, `session_prep_armouries.md`, `TOR_Moria_2404.pdf` for hero state (Torvir, Einar, Khoril), companion band (Bláin, Fáin, etc.), safe haven, NPCs, villains (Grimnar, Malech, Grik).
3. `teamwork_preview_explorer` (Survey 3 - Location Architecture & Operational Flow): Map the 10 keyed locations, 3-act flow, 4-stage alert tracker, sound economy, stealth mechanics, and loot/relic specifications.

### Phase 1: Architecture & Decomposition
- Merge Survey reports into `PROJECT.md` at project root.
- Define feature inventory, milestone breakdown (3-7 milestones), interface contracts, code/file layout.
- Initialize `TEST_INFRA.md` for the E2E Testing Track.

### Phase 2: Dual Track Execution
- **E2E Testing Track**: Build testing infrastructure and verification suite (Tiers 1-4 tests covering R1-R7 acceptance criteria).
- **Implementation Track**: Sub-orchestrators for milestones:
  - Milestone 1: Core System Framework, Band Mechanics & Operational Rules (Alerts, Sound, Hazards)
  - Milestone 2: Narrative Flow, 3 Acts, and Keyed Locations (1-10 complete with boxed text, GM notes, checks)
  - Milestone 3: Adversary Stat Blocks, Combat Encounters & Environmental Hazards (The Mauler, Grimnar, Grik, Patrols)
  - Milestone 4: Relics, Custom Hoards, Tables & Handouts (Durin's Axe, Wargear, D66 Scavenge Table, Letters)
  - Milestone 5: GM Facilitator Tools, Playbook, Node Maps & Worksheets (Cheat Sheet, Band Sheet, Node Map, GM Playbook)
  - Final Milestone: Full E2E Test Suite Pass + Adversarial Coverage Hardening (Tier 5)

### Phase 3: Verification, Gating & Audit
- Rigorous gate per milestone: Explorer -> Worker -> Reviewer -> Challenger -> Forensic Auditor -> Gate decision.
- Zero tolerance for integrity violations.

### Phase 4: Final Acceptance & Sentinel Handoff
- Verify all R1-R7 requirements are completely met in target folder.
- Send completion message to Sentinel.
