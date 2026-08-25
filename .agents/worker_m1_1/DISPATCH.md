## 2026-08-24T22:16:00Z
You are a Worker subagent responsible for Milestone 1 (M1) of the Moria adventure module project.
Your assigned working directory is: c:/Users/ante/Documents/Moria/.agents/worker_m1_1
Please create and maintain your coordination files within your working directory.

Authoritative Request & Specifications:
Read the following files before starting:
- c:/Users/ante/Documents/Moria/.agents/ORIGINAL_REQUEST.md (Read first!)
- c:/Users/ante/Documents/Moria/PROJECT.md (Architecture, M1 scope, interface contracts)
- Reference survey reports:
  - c:/Users/ante/Documents/Moria/.agents/spec_miner_survey_rules_1/spec_report.md
  - c:/Users/ante/Documents/Moria/.agents/spec_miner_survey_campaign_1/spec_report.md
  - c:/Users/ante/Documents/Moria/.agents/explorer_survey_arch_1/analysis.md

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Scope of Exclusive Ownership:
You exclusively own and will author the following 3 files in `c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep/`:
1. `01_campaign_context.md`
2. `02_band_mechanics.md`
3. `03_operational_mechanics.md`

Detailed Requirements for Milestone 1:
1. `01_campaign_context.md`:
   - Historical setting (Year 2989 TA, Balin's Expedition, East-Gate staging, Lord Balin & Commander Fróra, King Dáin in Erebor).
   - Complete Player-Hero profiles: Torvir Hammerstone (Champion, STR 7/TN 13, Great Axe Mastery, Grievous, Vengeance), Einar son of Anar (Treasure Hunter, STR 6/TN 14, Swords, Keen, Durin's Way, Parry 20, The Broken Key [+2 Scan], Dragon-sickness), Khoril Hornblower (Captain, STR 7/TN 13, Guide TN 14, Battle-horn [+1 Battle], Axes Mastery, Lure of Power).
   - The 7 active Dwarf Companions (*Bláin, Fáin, Dúrmer [Hardened], Hjoldring, Bróga, Austri, Dolg*) with detailed backgrounds, gifts, quirks, baseline health.
   - Safe Haven (*Caves of Thrym Thistlebeard*), safe placement of non-combat NPCs (*Frór, Haldor, Traumatized Dwarf*), and Relic attunement constraints (*The Eye of Thrym* inactive in Third Deep).
2. `02_band_mechanics.md`:
   - Full integration of Moria Band rules: Band Readiness 5 (TN 15), Dispositions (War 3, Vigilance 2, Manoeuvre 2, Expertise 2, Rally 1).
   - 4 distinct tactical squad deployment roles: Forward Scout Screen (Vigilance), Shield-Wall Phalanx (Interception/Defense), Rearguard Choke Point Defense (Gatehouse hold), Heavy Salvage Porter Squad (Equipment transport).
   - Band Fatigue, Band Morale/Hope, Injury tracking (5 tiers), Weary condition, and Desperate Stand rules.
   - Stealth & Marching discipline rules, Khoril's leadership integration.
3. `03_operational_mechanics.md`:
   - 4-Stage Alert Tracker: Alert 0 (Quiet Shadows), Alert 1 (Unease & Scent), Alert 2 (Hunted & Barricaded), Alert 3 (Drums in the Deep) with triggers, patrol behavior, and escalation countdowns.
   - Sound & Action Economy table: Explicit Noise Point values for all actions (stealth 0, quiet melee +1, loud melee +2, stone smash +3, siege weapon/breach +4, Khoril's horn +5) mapping to Alert progression and Eye Awareness (Hunt Threshold 14).
   - Environmental Hazards: Balrog neurotoxic miasma (minute/hour degradation, Craft TN 15 respirators, Healing remedies, suffocation/injury rules), structural collapse, and water perils.

Deliverables:
- Write the 3 complete, publication-grade markdown files in `c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep/`.
- Write handoff report in `c:/Users/ante/Documents/Moria/.agents/worker_m1_1/handoff.md`.
- Send message to parent orchestrator when complete.
