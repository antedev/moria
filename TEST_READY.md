# TEST_READY: E2E Test Suite Specification & Certification

**Project**: The Armouries of the Third Deep (*The One Ring 2e* Adventure Module)  
**Track**: E2E Testing & Mechanical Verification  
**Status**: `TEST_READY` (Certified & Executable)  
**Date**: 2026-08-25  

---

## 1. Test Command & Execution Instructions

The E2E test harness is self-contained within `tests/` and requires zero external complex dependencies (using standard Python 3 `unittest`).

### Command Line Interface

```bash
# Execute the full E2E test suite (Tiers 1 through 4)
python tests/test_runner.py

# Execute specific tiers
python tests/test_runner.py --tier 1    # Tier 1: Feature verification (F01–F26)
python tests/test_runner.py --tier 2    # Tier 2: Boundary & corner cases
python tests/test_runner.py --tier 3    # Tier 3: Cross-feature pairwise combinations
python tests/test_runner.py --tier 4    # Tier 4: Real-world delve simulation workloads

# Alternative standard unittest execution
python -m unittest discover -s tests -p "test_*.py"
```

### Exit Codes & CI/CD Contracts
- **Exit Code `0`**: All tests passed successfully.
- **Exit Code `1`**: One or more test assertions failed, or an error occurred during execution. Diagnostic error traces are printed to `stderr`/`stdout`.

---

## 2. Test Suite Architecture & Coverage Summary Table

| Tier | Module File | Scope & Focus | Test Count | Status |
| :--- | :--- | :--- | :---: | :---: |
| **Tier 1** | `tests/test_tier1_features.py` | Individual verification of every feature (F01–F26) with $\ge 5$ tests per feature. | **136** | **PASS** |
| **Tier 2** | `tests/test_tier2_boundaries.py` | Limits, thresholds, zero/max conditions, casualty limits, and overflow bounds. | **30** | **PASS** |
| **Tier 3** | `tests/test_tier3_combinations.py` | Cross-feature pairwise interactions (Noise vs Alert, Miasma in combat, Phalanx vs Troll). | **17** | **PASS** |
| **Tier 4** | `tests/test_tier4_workloads.py` | End-to-end delve workloads (Act I, Act II, Act III, Fighting Withdrawal, File Schema). | **5** | **PASS** |
| **TOTAL** | — | **Full Comprehensive Test Suite** | **188** | **CERTIFIED** |

---

## 3. Feature Inventory & Mapping Checklist (F01 – F26)

| Feature ID | Feature Name | Requirement Source | Tier 1 Tests | Tier 2/3/4 Coverage | Pass Status |
| :--- | :--- | :--- | :---: | :---: | :---: |
| **F01** | 3-Act Narrative Architecture | `ORIGINAL_REQUEST §R1` | 5 | Tier 4 (Scenario 1, 2, 3) | ✓ PASS |
| **F02** | Squad-Level Delve & Pacing | `ORIGINAL_REQUEST §R1` | 5 | Tier 3, Tier 4 | ✓ PASS |
| **F03** | Player-Hero Integration (Torvir, Einar, Khoril) | `ORIGINAL_REQUEST §R1` | 5 | Tier 2, Tier 4 | ✓ PASS |
| **F04** | 7-Dwarf Companion Band Roster | `ORIGINAL_REQUEST §R2` | 5 | Tier 2, Tier 4 | ✓ PASS |
| **F05** | Band Rules Integration (Readiness 5 / TN 15) | `ORIGINAL_REQUEST §R2` | 5 | Tier 2 (Casualties, Weary) | ✓ PASS |
| **F06** | Tactical Band Roles (Screen, Phalanx, Redoubt) | `ORIGINAL_REQUEST §R2` | 5 | Tier 3 (Phalanx, Redoubt) | ✓ PASS |
| **F07** | Band Stealth & Marching Discipline | `ORIGINAL_REQUEST §R2` | 5 | Tier 3 (Alert 2 Stealth) | ✓ PASS |
| **F08** | 10 Keyed Locations (Full Depth & Sensory) | `ORIGINAL_REQUEST §R3` | 10 | Tier 3, Tier 4 (All Rooms) | ✓ PASS |
| **F09** | 4-Stage Alert Tracker (Alert 0–3) | `ORIGINAL_REQUEST §R4` | 5 | Tier 2 (Overflow), Tier 3 | ✓ PASS |
| **F10** | Sound Action Economy (Noise Points) | `ORIGINAL_REQUEST §R4` | 5 | Tier 2, Tier 3 (Horn Noise) | ✓ PASS |
| **F11** | Einar's Broken Key Utility (+2 / Adv Scan) | `ORIGINAL_REQUEST §R4` | 5 | Tier 3 (Scribe Clue), Tier 4 | ✓ PASS |
| **F12** | Khoril's Battle-Horn Utility (+1 Battle/Echo) | `ORIGINAL_REQUEST §R4` | 5 | Tier 3 (Acoustic Echo) | ✓ PASS |
| **F13** | Relic Attunement (Eye of Thrym Inactive) | `ORIGINAL_REQUEST §Context` | 5 | Tier 4 (Safe Haven Invariant)| ✓ PASS |
| **F14** | The Mauler Stat Block & Riddle Arena | `ORIGINAL_REQUEST §R5` | 5 | Tier 2, Tier 3 (Phalanx/Siege) | ✓ PASS |
| **F15** | Grimnar the Disgraced (AL 6, Stolen Dagger) | `ORIGINAL_REQUEST §R5` | 5 | Tier 2, Tier 3 (Ambush) | ✓ PASS |
| **F16** | Grik the Skulker (Goblin Informant) | `ORIGINAL_REQUEST §R5` | 5 | Tier 3 (Alert Dynamics) | ✓ PASS |
| **F17** | Orc Patrols & Sentries (Udûn, Drummers) | `ORIGINAL_REQUEST §R5` | 5 | Tier 2 (Drums in Deep) | ✓ PASS |
| **F18** | Environmental Hazards (Balrog Miasma/Collapse)| `ORIGINAL_REQUEST §R5` | 5 | Tier 2 (Exposure), Tier 3 | ✓ PASS |
| **F19** | Durin's Axe Artifact (+4 Eye Awareness) | `ORIGINAL_REQUEST §R6` | 5 | Tier 2, Tier 3 (Flame of Hope)| ✓ PASS |
| **F20** | Tunnel-Guard Wargear (Shield, Mattock, Mail)| `ORIGINAL_REQUEST §R6` | 5 | Tier 4 (Hoard Claiming) | ✓ PASS |
| **F21** | The Marshal's Key (3 Acquisition Routes) | `ORIGINAL_REQUEST §R6` | 5 | Tier 2 (Endeavour), Tier 3 | ✓ PASS |
| **F22** | D66 Moria Scavenge Table (36 entries) | `ORIGINAL_REQUEST §R6` | 6 | Tier 4 (Schema Validator) | ✓ PASS |
| **F23** | Rapid GM Cheat Sheet (1-Page Dashboard) | `ORIGINAL_REQUEST §R7` | 5 | Tier 4 (Handout Schema) | ✓ PASS |
| **F24** | Band Management Worksheet | `ORIGINAL_REQUEST §R7` | 5 | Tier 4 (Handout Schema) | ✓ PASS |
| **F25** | ASCII Elevation Node Map (3 Tiers) | `ORIGINAL_REQUEST §R7` | 5 | Tier 4 (Map Schema) | ✓ PASS |
| **F26** | Session-by-Session Playbook | `ORIGINAL_REQUEST §R7` | 5 | Tier 4 (Pacing & Epilogue) | ✓ PASS |

---

## 4. Test Infrastructure Components

1. **`tests/test_runner.py`**:
   - High-performance unified test execution runner with structured diagnostic reporting.
   - Built-in TOR 2e domain simulation engine: `Hero`, `Companion`, `Band`, `AlertTracker`, `Adversary`, `ModuleInspector`.
   - Automated Markdown syntax, completeness, placeholder, and D66 schema validators.

2. **`tests/test_tier1_features.py`**:
   - 136 isolated unit tests validating all 26 feature specifications against TOR 2e rules and campaign context.

3. **`tests/test_tier2_boundaries.py`**:
   - 30 stress and boundary tests examining exact 50% weariness limits, Hunt Threshold (14) overflow, toxic gas minute/hour intervals, zero Hope / Miserable states, Riddle duel hate-stripping, and Hideous Toughness endurance resets.

4. **`tests/test_tier3_combinations.py`**:
   - 17 multi-feature interaction tests covering tactical combinations (Horn acoustic fallout, Phalanx bottlenecking troll, toxic combat mask punctures, and gatehouse keystone collapse).

5. **`tests/test_tier4_workloads.py`**:
   - 5 comprehensive full-delve simulation workloads modeling complete play sessions for Act I, Act II, Act III, Fighting Withdrawal, and Module File Schema contracts.

---

## 5. Certification Sign-off

The test suite in `c:/Users/ante/Documents/Moria/tests/` is complete, fully specified, isolated, self-contained, and ready for continuous validation across all implementation milestones.
