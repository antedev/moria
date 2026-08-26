# Handoff Report — Milestone M2: Core Mechanics, Band Systems, Adversaries & Hazards

**Agent**: `worker_m2`  
**Parent Agent**: `orchestrator` (`4520ebd2-4ae5-45e8-aaf7-6750f3bc27b8`)  
**Date**: 2026-08-26  
**Status**: COMPLETE (Hard Handoff)  

---

## 1. Observation

Direct observations and evidence from the codebase prior to and after Worker M2 refactoring:

1. **Non-Canonical "Daunted" Condition**:
   - `05_adversaries_and_hazards.md:115`: *The Mauler's Strike Fear* previously stated: `VALOUR test against their Heart TN (Torvir: 18, Einar: 17, Khoril 16) or suffer 2 Shadow (Dread) and become Daunted (cannot spend Hope for the rest of the battle).`
   - `quickstart/03_adversaries_and_hazards.md:44`: *The Mauler's Strike Fear* previously stated: `Those who fail gain 2 Shadow (Dread) and are Daunted (cannot spend Hope for the rest of the battle).`
   - *Current State*: Both instances have been purged and replaced with canonical TOR 2e mechanics (`VALOUR test or gain 2 Shadow Points [Dread]; heroes whose current Shadow equals or exceeds their Hope become Miserable`).

2. **Hardcoded Pregen Target Numbers (`Torvir 15, Einar 15, Khoril 16`, etc.)**:
   - `01_campaign_context.md:139`: Hardcoded `(TRAVEL — Heart TN 16)`.
   - `02_band_mechanics.md:137, 193–200, 287–348`: Hardcoded `CRAFT (Strength TN: Torvir 13, Einar 14, Khoril 13)`, Heart TNs in First Aid table, and `ENHEARTEN (Heart TN: Torvir 18, Khoril 16)`.
   - `03_operational_mechanics.md:55, 76, 225–228, 245, 267`: Over 10 occurrences of hardcoded pregen TNs across alert escalation and environmental hazard countermeasures.
   - `05_adversaries_and_hazards.md:32, 105, 114, 119, 157, 188, 193, 303, 408, 416, 467, 473–475, 491, 495, 503, 521, 526, 530, 556, 559, 562`: Over 25 occurrences of hardcoded pregen TN listings.
   - `quickstart/00_overview_and_background.md:82`: Hardcoded `(TRAVEL — Heart TN 16)`.
   - `quickstart/01_delve_mechanics_and_alert_system.md:23, 97, 122, 138, 164`: Multiple occurrences of pregen TNs and specific character scriptings.
   - `quickstart/03_adversaries_and_hazards.md:32, 43, 50, 114, 172–176, 188–190`: Over 15 occurrences of pregen TNs in stat blocks, hazard matrix, and water perils.
   - *Current State*: Every check across all 7 assigned files has been standardized to `**SKILL roll**` (e.g. `**SCAN roll**`, `**STEALTH roll**`, `**CRAFT roll**`, `**HEALING roll**`, `**ATHLETICS roll**`, `**VALOUR test**`, `**PROTECTION test**`) with situational dice modifiers (`+1d`, `-1d`, `Favoured`, `Ill-favoured`), failure consequences, and 6-icon degrees of success. Zero hardcoded pregen TNs remain.

3. **Prescriptive PC Scripting & Agency Violations**:
   - `02_band_mechanics.md`: Prescriptive text dictating that Einar is point recon, Torvir is shield-wall anchor, and Khoril is guide.
   - `05_adversaries_and_hazards.md`: Grimnar's tactics, fell abilities (*Hatred*, *Vengeful Strike*), dialogue labels, and retreat conditions specifically scripted against Torvir, Einar, and Khoril.
   - *Current State*: All roles, tactical formations, adversary targeting rules, and dialogue cues are fully generalized to archetypes and open Player-Hero actions.

---

## 2. Logic Chain

1. **Observation 1 & 2**: TOR 2e rules state that Target Numbers are individual properties derived on each player's character sheet ($20 - \text{Attribute}$), and the core rules do not contain an invented "Daunted" status condition.
2. **Inference**: Hardcoding pregen TNs in module text clutters the presentation, breaks compatibility with custom player-created heroes, and misrepresents the core system. The "Daunted" condition creates non-standard rules confusion for Loremaster and players alike.
3. **Action Taken**: Refactored all check notation across all assigned files to clean TOR 2e format, replaced all "Daunted" references with official conditions (Shadow Points / Dread, Miserable, Weary), and removed all prescriptive hero assignment language.
4. **Conclusion**: The operational mechanics, squad band systems, adversary stat blocks, and subterranean hazard matrices in both master chapters and quickstart files are now 100% compliant with TOR 2e rules canon and maintain complete player agency.

---

## 3. Caveats

- **Files Outside Scope**: Keyed location chapters (`04_keyed_locations.md`, `quickstart/02_keyed_locations.md`), relics & rewards (`06_relics_and_rewards.md`, `quickstart/04_loot_relics_and_rewards.md`), GM playbook (`07_gm_playbook_and_pacing.md`, `quickstart/05_gm_screen_and_play_aids.md`), and standalone handouts are owned by other workers (M1, M3, M4) and were not modified by Worker M2.
- **Band TN**: The Band Target Number of 15 ($20 - \text{Readiness 5}$) is preserved throughout, as it represents canonical Moria Band mechanics.

---

## 4. Conclusion

Milestone M2 is fully completed. All 7 assigned files have been thoroughly audited, refactored, and certified:
- `01_campaign_context.md`
- `02_band_mechanics.md`
- `03_operational_mechanics.md`
- `05_adversaries_and_hazards.md`
- `quickstart/00_overview_and_background.md`
- `quickstart/01_delve_mechanics_and_alert_system.md`
- `quickstart/03_adversaries_and_hazards.md`

All requirements of R1 (player agency), R2 (streamline skill checks / remove hardcoded TNs), and R4 (canon TOR 2e rules audit, purging "Daunted", certifying adversary stat blocks) have been successfully fulfilled for the M2 scope.

---

## 5. Verification Method

To independently verify Worker M2's changes:

1. **Verify Complete Purge of "Daunted" in Assigned Files**:
   Search for `Daunted` across `01_campaign_context.md`, `02_band_mechanics.md`, `03_operational_mechanics.md`, `05_adversaries_and_hazards.md`, `quickstart/00_overview_and_background.md`, `quickstart/01_delve_mechanics_and_alert_system.md`, and `quickstart/03_adversaries_and_hazards.md`.
   *Expected Result*: 0 matches.

2. **Verify Removal of Hardcoded Pregen TNs**:
   Search for `Torvir 15`, `Torvir 13`, `Einar 15`, `Einar 14`, `Khoril 16`, or `Strength TN:` in the assigned files.
   *Expected Result*: 0 matches in skill check listings (only present in pregen character profile definitions in `quickstart/00_overview_and_background.md`).

3. **Verify Standard Check Notation**:
   Inspect `02_band_mechanics.md`, `03_operational_mechanics.md`, `05_adversaries_and_hazards.md`, and `quickstart/01` / `quickstart/03`.
   *Expected Result*: All skill tests are formatted as `**SKILL roll**` or `**TEST test**` with explicit situational modifiers (`+1d`, `-1d`, `Favoured`, `Ill-favoured`) and 6-icon degrees of success.
