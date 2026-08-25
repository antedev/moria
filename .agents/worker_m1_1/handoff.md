# Milestone 1 Handoff Report: Core System Framework & Operational Mechanics

**Agent**: `worker_m1_1` (Worker Subagent for Milestone 1)  
**Parent Agent**: `9e364a2f-478d-4b95-8767-7bc001dad526`  
**Working Directory**: `c:/Users/ante/Documents/Moria/.agents/worker_m1_1`  
**Delivered Chapters**:
1. `c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep/01_campaign_context.md`
2. `c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep/02_band_mechanics.md`
3. `c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep/03_operational_mechanics.md`

---

## 1. Observation

1. **Assignment & Scope**:
   * According to `ORIGINAL_REQUEST.md` and `PROJECT.md` (§Milestones M1, lines 55–57), Milestone 1 exclusively owns the core system framework and operational foundations comprising Chapters 1, 2, and 3 of the adventure module.
2. **Canonical Data & Formulas**:
   * `spec_miner_survey_rules_1/spec_report.md` established:
     - Band Readiness: Rating 5 $\implies$ Readiness TN: $\mathbf{15}$ ($\text{TN} = 20 - 5$).
     - Band Dispositions: War 3, Vigilance 2, Manoeuvre 2, Expertise 2, Rally 1.
     - Strategic Eye Awareness: Base Hunt Threshold 14 (Dark Land) / 16 (Safe Haven Wild Land).
     - Balrog Toxic Miasma: Grievous poison (unprotected: roll/minute) / Severe poison (protected: roll/hour) / Craft TN 15 respirators.
   * `spec_miner_survey_campaign_1/spec_report.md` established:
     - Torvir Hammerstone: STR 7 (TN 13), HEART 2 (TN 18), WITS 5 (TN 15), Great Axe Mastery, Grievous, Vengeance, Eye of Thrym (inactive).
     - Einar son of Anar: STR 6 (TN 14), HEART 3 (TN 17), WITS 5 (TN 15), Swords Mastery, Keen, Durin's Way, Reinforced Shield (Parry 20), The Broken Key (+2/Advantage on Scan), Dragon-sickness.
     - Khoril Hornblower: STR 7 (TN 13), HEART 3 (TN 16 via Prowess), WITS 4 (TN 16), Guide TN 14, Battle-horn (+1 Battle, Band Rally, Alert tradeoff), Axes Mastery, Durin's Way, Reinforced Shield (Parry 17), Lure of Power.
     - 7 Active Companions: *Bláin, Fáin, Dúrmer (Hardened), Hjoldring, Bróga, Austri, Dolg*.
     - Safe Haven: *Caves of Thrym Thistlebeard* (Second Deep); Non-combat NPCs (*Frór, Haldor, Traumatized Dwarf*) safe at East-Gate.
3. **Authored Files**:
   * `01_campaign_context.md`: Authored with complete historical setting (Balin's Expedition 2989 TA, Fróra, Dáin), full hero sheets, 7 companion rosters with gifts/quirks, Haven details, safe NPC placement, and relic constraints.
   * `02_band_mechanics.md`: Authored with Moria Band rules (Readiness 5 / TN 15), 4 tactical squad roles, 5 injury tiers, 4 fatigue tiers, Band Weary ($\ge 50\%$ incapacitated), Desperate Stand (Gandalf rune survival), stealth formations, and mass combat clashes.
   * `03_operational_mechanics.md`: Authored with 4-Stage Alert Tracker (Alert 0–3), full Sound Action Economy table, Strategic Eye Awareness / Revelation episodes, Balrog neurotoxic miasma, structural collapses, and subterranean water peril table.

---

## 2. Logic Chain

1. **System & Setting Harmony**: All three Player-Hero profiles were constructed using standard *The One Ring 2e* mechanics, cultural virtues (*Fierce-Minded*, *Durin's Way*, *Redoubtable*), and exact calculated Target Numbers ($\text{TN} = 20 - \text{Attribute}$).
2. **Band Operational Utility**: To ensure the 7 Dwarf companions enhance gameplay rather than cluttering table management, the Band system aggregates actions into 5 Dispositions and 4 clear tactical roles (Forward Screen, Shield-Wall, Rearguard, Salvage Porters).
3. **Anti-Swarm & Tension Management**: The 4-Stage Alert Tracker directly bridges player choices (stealth vs loud actions) with local enemy escalation and overarching Eye Awareness. This allows tactical skirmishing without triggering unrealistic immediate TPK swarms, while providing a clear 6-turn escape countdown at Alert 3.
4. **Narrative & Relic Constraints**: *The Eye of Thrym* is explicitly established as inert outside Thistlebeard's Caves, keeping focus on *The Broken Key* and *Battle-horn of the Realm*, preventing out-of-scope scrying in the Third Deep.

---

## 3. Caveats

* **Downstream Milestone Dependencies**:
  - Keyed locations 1–10 (`04_keyed_locations.md`, Milestone 2) must reference the exact Alert Tiers and Noise Point costs defined in `03_operational_mechanics.md`.
  - Adversary stat blocks (`05_adversaries_and_hazards.md`, Milestone 3) should adhere to the adversary profiles (The Mauler, Grimnar, Grik, Udûn patrols) established in Chapter 1 and Chapter 3.
  - Relic and hoard tables (`06_relics_and_rewards.md`, Milestone 4) should expand on *Durin's Axe*, *Tunnel-Guard Wargear*, and *The Marshal's Key*.

---

## 4. Conclusion

Milestone 1 is **100% complete**. All three foundation chapters (`01_campaign_context.md`, `02_band_mechanics.md`, `03_operational_mechanics.md`) have been authored to publication-grade standards, fully populated with zero placeholders, and verified for mathematical and canonical consistency with *The One Ring 2nd Edition* and *Moria: Through the Doors of Durin*.

---

## 5. Verification Method

To independently verify Milestone 1:
1. Inspect `c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep/01_campaign_context.md`:
   - Verify historical setting (2989 TA, Balin, Fróra, King Dáin).
   - Verify stat blocks for Torvir, Einar, and Khoril (Attributes, TNs, Parry scores, virtues, masteries, shadow flaws).
   - Verify profiles for the 7 Companions (*Bláin, Fáin, Dúrmer, Hjoldring, Bróga, Austri, Dolg*).
   - Verify Safe Haven and NPC placement at East-Gate.
2. Inspect `c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep/02_band_mechanics.md`:
   - Verify Readiness 5 $\implies$ TN 15; Dispositions (War 3, Vigilance 2, Manoeuvre 2, Expertise 2, Rally 1).
   - Verify 4 Tactical Squad Roles and mechanical bonuses.
   - Verify 5 Injury Tiers, 4 Fatigue Tiers, Band Weary rule, and Desperate Stand resolution.
3. Inspect `c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep/03_operational_mechanics.md`:
   - Verify 4-Stage Alert Tracker (0: Quiet Shadows, 1: Unease & Scent, 2: Hunted & Barricaded, 3: Drums in the Deep).
   - Verify Sound & Action Economy table (Noise values 0 to +5).
   - Verify Balrog Miasma rules (Craft TN 15 respirators, exposure rates), structural collapse, and Water Perils table.
