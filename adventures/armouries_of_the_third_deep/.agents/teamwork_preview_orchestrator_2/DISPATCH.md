## 2026-08-26T04:53:29Z
You are the Project Orchestrator for the comprehensive structural, narrative, and mechanical revision of "The Armouries of the Third Deep" adventure module for The One Ring 2nd Edition (TOR 2e).

## Working Directory
Your working directory is: `c:/Users/ante/Documents/github/Moria/adventures/armouries_of_the_third_deep/.agents/teamwork_preview_orchestrator_2`
Project directory: `c:/Users/ante/Documents/github/Moria/adventures/armouries_of_the_third_deep`

## Authoritative User Request
Read `c:/Users/ante/Documents/github/Moria/adventures/armouries_of_the_third_deep/.agents/ORIGINAL_REQUEST.md` for the full request and acceptance criteria.

## Objectives & Requirements
1. **R1. Player Agency & Neutral Scene Presentation**: Remove all narrative assumptions and prescriptive text that dictates character actions (e.g. "Khoril rolls...", "Einar searches...", "Torvir invokes..."). Reframe all scenes, rooms, encounters, and obstacles so the GM presents the environment, sensory details, and available tactical choices neutrally, letting the players decide how their company responds and who attempts what action.
2. **R2. Streamline Skill Checks & Remove Hardcoded Pregen Attribute TNs**: Remove all hardcoded target number listings for specific pre-gens (e.g. `(Wits TN: Torvir 15, Einar 15, Khoril 16)`) across all keyed locations, hazards, and encounters. Format all checks using standard The One Ring 2e conventions (e.g., "**SCAN roll**", "**STEALTH roll**", "**EXPLORE roll**" along with standard situational modifiers such as `+1d`, `-1d`, `Favoured`, or `Ill-favoured`). Players roll against the Target Numbers on their own character sheets.
3. **R3. Boxed Read-Aloud Text Clean-Up & Spoiler Removal**: Rewrite all boxed read-aloud descriptions across all 10 keyed locations so they are concise, evocative, and atmosphere-setting without overly flowery purple prose. Strip out all spoilers of hidden information—such as concealed tripwires, scythe traps, poison vats, ambush positions, or hidden doors. Those elements must remain strictly in the GM reference sections until players inspect or detect them.
4. **R4. Canon TOR 2e Rule Audit & Condition Correction**: Remove all non-canonical rules and invented conditions (specifically the "Daunted" condition, which does not exist in TOR 2e core rules). Replace effects with canonical TOR 2e mechanics (Shadow points/Dread, Weary, Miserable, Wounded, Hope loss, Bout of Madness triggers). Audit adversary stats, abilities, and hazard mechanics to ensure strict adherence to The One Ring 2nd Edition rules.
5. **R5. Master Document, Quickstart, and Handout Synchronization**: Apply the revisions consistently across all modular chapter markdown files (`01_campaign_context.md` through `07_gm_playbook_and_pacing.md`), quickstart files (`quickstart/00` to `05`), and handouts. Ensure the build pipeline (`scripts/build_master_document.py`, `scripts/build_handouts.py`) compiles the updated master document (`armouries_of_the_third_deep_master.md`), HTML, and print assets cleanly with zero build errors.
