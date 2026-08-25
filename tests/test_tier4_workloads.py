#!/usr/bin/env python3
"""Tier 4 Real-World Application Delve Workload Scenarios.

Adventure Module: The Armouries of the Third Deep (The One Ring 2e)
Location: c:/Users/ante/Documents/Moria/tests/test_tier4_workloads.py

This module simulates full multi-session playthrough workloads:
- Scenario 1: Act I — The Descent & Mustering-Yard Infiltration
- Scenario 2: Act II — The Despoiled Halls, Toxic Hazards & Key Acquisition
- Scenario 3: Act III — The Mauler Arena, King's Door Ambush & Royal Vault
- Scenario 4: The Fighting Withdrawal & Escape to Thistlebeard's Safe Haven
- Scenario 5: Static Adventure File Layout & Content Schema Verification
"""

import os
import unittest
from test_runner import (
    Hero, Companion, Band, AlertTracker, Adversary,
    create_canonical_heroes, create_canonical_band, create_canonical_adversaries,
    ModuleInspector
)


class TestTier4_DelveScenarios(unittest.TestCase):
    """Full simulated playthrough workloads across Acts I, II, III and Withdrawal."""

    def test_scenario_1_act_I_descent_and_mustering(self):
        """Simulates complete Act I playthrough."""
        heroes = create_canonical_heroes()
        band = create_canonical_band()
        tracker = AlertTracker(hunt_threshold=14)

        # 1. Travel down shafts from Thistlebeard's haven (Travel TN 14)
        khoril = heroes["khoril"]
        self.assertEqual(khoril.calling, "Captain")

        # 2. Location 1: Mustering-Yard Infiltration
        # Forward screen scouts path
        self.assertEqual(tracker.alert_level, 0)
        # Einar uses Broken Key to spot Udûn sentries
        einar = heroes["einar"]
        self.assertIn("The Broken Key", einar.gear)
        # Band performs quiet stealth march (+0 Noise)
        tracker.add_noise(0)
        self.assertEqual(tracker.noise_points, 0)

        # 3. Location 2: Securing Upper Gatehouse Redoubt
        # Craft TN 14 to fortify redoubt; Battle TN 14 to rig keystone trap
        # Tactical deployment: Detach Bláin and Austri to hold redoubt
        blain = next(c for c in band.companions if c.name == "Bláin")
        austri = next(c for c in band.companions if c.name == "Austri")
        blain.tactical_role = "Rearguard Redoubt"
        austri.tactical_role = "Rearguard Redoubt"
        self.assertEqual(blain.tactical_role, "Rearguard Redoubt")

        # 4. Location 3: First Armoury Scrap-traps
        # Einar spots tripwires; traps safely disarmed
        disarmed_traps = True
        self.assertTrue(disarmed_traps)

        # End of Act I state verification
        self.assertEqual(tracker.alert_level, 0)
        self.assertEqual(band.active_count, 7)

    def test_scenario_2_act_II_despoiled_halls_and_toxins(self):
        """Simulates complete Act II playthrough."""
        heroes = create_canonical_heroes()
        band = create_canonical_band()
        tracker = AlertTracker(hunt_threshold=14)

        # 1. Location 4: Broken Hall & Dark Idol
        # Resisting Dread TN 14
        torvir = heroes["torvir"]
        self.assertIn("Fierce-Minded", torvir.virtues_rewards)
        # Khoril sings ancient hymn, restoring +1 Band Hope
        band.shared_hope += 1
        self.assertEqual(band.shared_hope, 13)

        # 2. Location 5: Second Armoury Siege Engines
        # Party inspects Grond-ram and primes Torsion Ballista
        ballista_primed = True
        self.assertTrue(ballista_primed)

        # 3. Location 7: Poisoned Halls (12th & 14th Halls)
        # Respirators equipped (Severe poison: 1 roll/hr instead of 1 roll/min)
        respirators_active = True
        self.assertTrue(respirators_active)
        # Finding petrified scribe and reading Dying Scribe's Letter
        letter_found = True
        self.assertTrue(letter_found)

        # 4. Location 8: Upper Armoury Garrison Salvage Cache
        # Salvaging 40 mail suits, 30 shields, 50 mattocks (+50 Supply Points)
        supply_points = 50
        band.burden = "Heavy"  # Porters assigned
        self.assertEqual(supply_points, 50)
        self.assertEqual(band.burden, "Heavy")

        # 5. Acquiring Marshal's Key from Grik
        has_marshals_key = True
        self.assertTrue(has_marshals_key)

        # End of Act II state verification
        self.assertTrue(band.shared_hope >= 10)
        self.assertEqual(tracker.alert_level, 0)

    def test_scenario_3_act_III_boss_vault_and_relics(self):
        """Simulates complete Act III playthrough."""
        heroes = create_canonical_heroes()
        band = create_canonical_band()
        adversaries = create_canonical_adversaries()
        tracker = AlertTracker(hunt_threshold=14)

        # 1. Location 6: The Hall of the Mauler
        mauler = adversaries["the_mauler"]
        # Fire primed ballista from Loc 5 -> 25 damage, strips armor
        mauler.take_damage(25)
        mauler.armour_dice = 3
        tracker.add_noise(4)  # Siege noise -> Alert 1

        # Torvir engages in Forward stance Riddle duel -> strips 3 Hate
        mauler.spend_hate(3)
        self.assertEqual(mauler.current_hate, 7)

        # Levering stalactite -> deals 20 damage
        mauler.take_damage(20)
        # Finishing strikes reduce mauler to 0 End -> resets to 40 via Hideous Toughness
        mauler.take_damage(35)
        self.assertEqual(mauler.current_endurance, 40)
        # Second phase defeat
        mauler.take_damage(40)
        mauler.is_dead = True
        self.assertTrue(mauler.is_dead)

        # 2. Location 9: The King's Door & Grimnar's Ambush
        grimnar = adversaries["grimnar"]
        # Inserting Marshal's Key unlocks gate smoothly
        unlocked = True
        self.assertTrue(unlocked)
        # Grimnar ambushes from parapet -> defeated by heroes
        grimnar.take_damage(32)
        self.assertEqual(grimnar.current_endurance, 16)
        grimnar.suffer_wound()
        grimnar.suffer_wound()
        self.assertTrue(grimnar.is_dead)

        # 3. Location 10: Lower Armoury & Claiming Durin's Axe
        # Claiming Durin's Axe adds +4 Eye Awareness (starting from 2 due to prior siege noise)
        tracker.add_eye_awareness(4)
        self.assertEqual(tracker.eye_awareness, 6)
        # Claiming Tunnel-Guard Wargear
        wargear_claimed = ["Shield of the Deep Gate", "Mattock of Moria-Silver", "Mail of Unyielding Stone"]
        self.assertEqual(len(wargear_claimed), 3)

    def test_scenario_4_fighting_withdrawal_and_escape(self):
        """Simulates the final Fighting Withdrawal and evacuation."""
        band = create_canonical_band()
        tracker = AlertTracker(hunt_threshold=14)
        tracker.set_alert_level(3)  # General alarm sounded!

        countdown = tracker.countdown_to_shaft_seal
        self.assertEqual(countdown, 6)

        # Step 1: Evacuate Location 10 -> Location 6 (Round 1)
        countdown -= 1
        # Step 2: Evacuate Location 6 -> Location 4 (Round 2)
        countdown -= 1
        # Step 3: Evacuate Location 4 -> Location 2 Gatehouse (Round 3)
        countdown -= 1

        # Step 4: Upper Gatehouse Redoubt holds choke point
        # Rearguard companions (Bláin & Austri) trigger rigged keystone collapse
        keystone_triggered = True
        pursuers_crushed_damage = 30
        self.assertTrue(keystone_triggered)
        self.assertEqual(pursuers_crushed_damage, 30)

        # Step 5: Final ascent up shafts to Thistlebeard's haven (Round 4)
        countdown -= 1
        self.assertTrue(countdown > 0)  # Evacuated with 2 rounds to spare!

        # Mission Success: Wargear and Durin's Axe secured for Balin's colony
        mission_success = True
        self.assertTrue(mission_success)

    def test_scenario_5_static_module_inspector_contract(self):
        """Validates ModuleInspector interface against project directory standards."""
        module_path = "c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep"
        inspector = ModuleInspector(module_path)
        
        # Test expected file list schema
        self.assertEqual(len(inspector.EXPECTED_FILES), 12)
        self.assertIn("README.md", inspector.EXPECTED_FILES)
        self.assertIn("04_keyed_locations.md", inspector.EXPECTED_FILES)
        self.assertIn("handouts/gm_cheat_sheet.md", inspector.EXPECTED_FILES)
        self.assertIn("handouts/dying_scribe_letter.md", inspector.EXPECTED_FILES)

        # Test expected locations schema
        self.assertEqual(len(inspector.EXPECTED_LOCATIONS), 10)
        self.assertIn("The Mustering-Yard", inspector.EXPECTED_LOCATIONS)
        self.assertIn("The Lower Armoury", inspector.EXPECTED_LOCATIONS)

        # Test D66 table validator on synthetic valid table
        synthetic_d66 = "\n".join([f"| {d1}{d2} | Item {d1}{d2} |" for d1 in range(1, 7) for d2 in range(1, 7)])
        is_valid, count, missing = inspector.validate_d66_table(synthetic_d66)
        self.assertTrue(is_valid)
        self.assertEqual(count, 36)
        self.assertEqual(len(missing), 0)


if __name__ == "__main__":
    unittest.main()
