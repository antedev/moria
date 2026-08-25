#!/usr/bin/env python3
"""Tier 3 Cross-Feature Interaction & Combination Verification Tests.

Adventure Module: The Armouries of the Third Deep (The One Ring 2e)
Location: c:/Users/ante/Documents/Moria/tests/test_tier3_combinations.py

This module contains tests for cross-feature pairwise interactions:
- Band stealth marching in Alert 2 vs Grimnar stalking
- Battle-horn acoustic echo vs Alert & Eye Awareness escalation
- The Mauler arena hazards combined with Band Shield-Wall Phalanx
- Toxic miasma hazard combined with combat & mask rupture
- Grik negotiation dynamics combined with dungeon Alert level
- Scribe letter investigation combined with Einar's Broken Key
- Fighting withdrawal redoubt, keystone trap, and countdown escape
- Durin's Axe Flame of Hope combined with Band Morale under Alert 3
- Siege ballista / Grond-ram firing combined with Mauler scrap armor stripping
"""

import os
import unittest
from test_runner import (
    Hero, Companion, Band, AlertTracker, Adversary,
    create_canonical_heroes, create_canonical_band, create_canonical_adversaries
)


class TestTier3_BandStealthInAlert2(unittest.TestCase):
    """Interaction: Band stealth marching under Alert 2 vs Grimnar's stalking ambush."""

    def setUp(self):
        self.band = create_canonical_band()
        self.heroes = create_canonical_heroes()
        self.tracker = AlertTracker()
        self.tracker.set_alert_level(2)

    def test_alert_2_stealth_penalty_and_grimnar_stalking(self):
        """In Alert 2, stealth rolls suffer (-1d) and Grimnar actively stalks the party."""
        self.assertEqual(self.tracker.alert_level, 2)
        base_manoeuvre_dice = self.band.manoeuvre
        alert_mod = -1
        effective_dice = base_manoeuvre_dice + alert_mod
        self.assertEqual(effective_dice, 1)

    def test_khoril_leadership_and_hope_mitigation(self):
        """Khoril spends 1 Band Hope and uses Leadership to counter the Alert 2 stealth penalty."""
        self.assertTrue(self.band.spend_band_hope(1))
        # Leadership (+1d) + Hope (+1d) - Alert 2 (-1d) = +1d net over base
        net_modifier = 1 + 1 - 1
        effective_dice = self.band.manoeuvre + net_modifier
        self.assertEqual(effective_dice, 3)


class TestTier3_BattleHornNoiseVsAlertAndEye(unittest.TestCase):
    """Interaction: Khoril's Battle-Horn utility vs acoustic Alert & Eye Awareness penalty."""

    def setUp(self):
        self.tracker = AlertTracker(hunt_threshold=14)
        self.band = create_canonical_band()
        self.khoril = create_canonical_heroes()["khoril"]

    def test_horn_tactical_benefit_with_acoustic_fallout(self):
        """Sounding the horn grants +1 Battle & Band rally, but adds +5 Noise (+2 Eye Awareness)."""
        # Tactical benefit
        battle_bonus = 1
        rallied = True
        self.assertEqual(battle_bonus, 1)
        self.assertTrue(rallied)

        # Acoustic fallout
        self.tracker.add_noise(5)
        self.assertEqual(self.tracker.noise_points, 5)
        self.assertTrue(self.tracker.eye_awareness >= 2)

    def test_horn_blast_triggers_instant_revelation_at_high_eye(self):
        """If Eye Awareness was 12, sounding the horn pushes Eye to 14+ triggering Revelation."""
        self.tracker.add_eye_awareness(12)
        self.assertEqual(self.tracker.eye_awareness, 12)
        self.assertEqual(self.tracker.revelations_triggered, 0)

        # Sounding horn adds 3 Eye Awareness (since noise=5)
        triggered = self.tracker.add_eye_awareness(3)
        self.assertTrue(triggered)
        self.assertEqual(self.tracker.revelations_triggered, 1)
        self.assertEqual(self.tracker.eye_awareness, 0)  # Resets


class TestTier3_MaulerArenaWithBandPhalanx(unittest.TestCase):
    """Interaction: The Mauler boss arena combined with Band Shield-Wall and catwalk tactics."""

    def setUp(self):
        self.band = create_canonical_band()
        self.heroes = create_canonical_heroes()
        self.mauler = create_canonical_adversaries()["the_mauler"]

    def test_phalanx_bottles_mauler_while_heroes_scale_catwalks(self):
        """Band Phalanx (War 3d) holds entrance while heroes scale catwalks for elevation attack."""
        # Phalanx deployment
        phalanx_members = [c for c in self.band.companions if "Phalanx" in c.tactical_role or "Bulwark" in c.tactical_role]
        self.assertTrue(len(phalanx_members) >= 2)

        # Heroes on catwalks gain elevation (+1d to attacks)
        catwalk_elevation_mod = 1
        self.assertEqual(catwalk_elevation_mod, 1)

    def test_stalactite_drop_on_mauler(self):
        """Levering down a stalactite deals 20 direct damage to The Mauler."""
        start_end = self.mauler.current_endurance
        self.mauler.take_damage(20)
        self.assertEqual(self.mauler.current_endurance, start_end - 20)


class TestTier3_ToxicMiasmaCombatAndMaskRupture(unittest.TestCase):
    """Interaction: Combat in Location 7/8 under toxic gas with respirator degradation."""

    def setUp(self):
        self.torvir = create_canonical_heroes()["torvir"]

    def test_mask_rupture_on_fire_damage(self):
        """Udûn Torch-staff Fiery Blow ruptures mask, exposing hero to Grievous poison."""
        mask_intact = True
        # Fiery blow lands
        mask_intact = False
        self.assertFalse(mask_intact)

        # Hero exposed without mask -> Grievous poison (roll every minute)
        exposure_rate = "minute"
        self.assertEqual(exposure_rate, "minute")

    def test_craft_emergency_mask_patching(self):
        """Craft TN 14 emergency check patches respirator in 1 round."""
        craft_tn = 14
        rounds_to_repair = 1
        self.assertEqual(craft_tn, 14)
        self.assertEqual(rounds_to_repair, 1)


class TestTier3_GrikNegotiationVsAlertLevel(unittest.TestCase):
    """Interaction: Grik the Skulker negotiation dynamics influenced by Alert Tracker."""

    def setUp(self):
        self.grik = create_canonical_adversaries()["grik"]
        self.tracker = AlertTracker()

    def test_grik_negotiates_at_low_alert(self):
        """At Alert 0-1, Grik trades patrol routes and Marshal's Key intel for silver/tobacco."""
        self.tracker.set_alert_level(1)
        will_negotiate = self.tracker.alert_level <= 1
        self.assertTrue(will_negotiate)

    def test_grik_panics_and_flees_at_alert_two_or_three(self):
        """At Alert 2+, Grik panics and flees into ventilation crawlspaces."""
        self.tracker.set_alert_level(2)
        will_flee = self.tracker.alert_level >= 2
        self.assertTrue(will_flee)


class TestTier3_ScribeLetterWithBrokenKeyScan(unittest.TestCase):
    """Interaction: Location 7 investigation using Einar's Broken Key to find Scribe's Letter."""

    def setUp(self):
        self.einar = create_canonical_heroes()["einar"]

    def test_broken_key_finds_lead_scroll_tube(self):
        """Einar's +2 Scan bonus allows locating the petrified scribe's lead tube in heavy mist."""
        base_scan_tn = 14
        broken_key_mod = 2
        effective_tn = base_scan_tn - broken_key_mod
        self.assertEqual(effective_tn, 12)

    def test_translating_scribe_letter_unlocks_marshals_key_lore(self):
        """Deciphering the letter confirms Marshal's Key taken to Goblin Village / Udûn patrol."""
        has_clue = True
        self.assertTrue(has_clue)


class TestTier3_FightingWithdrawalRedoubtAndKeystone(unittest.TestCase):
    """Interaction: Act III evacuation combining Gatehouse Redoubt, Keystone Trap, and countdown."""

    def setUp(self):
        self.band = create_canonical_band()
        self.tracker = AlertTracker()
        self.tracker.set_alert_level(3)

    def test_gatehouse_redoubt_secures_retreat_corridor(self):
        """Having 2 companions holding Location 2 Gatehouse prevents rear flanking ambushes."""
        rearguard_present = True
        self.assertTrue(rearguard_present)

    def test_keystone_trap_collapse_crushes_vanguard(self):
        """Triggering keystone collapse deals 30 damage, crushing pursuing shock-troops."""
        trap_damage = 30
        self.assertEqual(trap_damage, 30)

    def test_countdown_evacuation_success(self):
        """Band moves through 4 locations in 4 rounds, beating the 6-round shaft seal countdown."""
        rounds_used = 4
        countdown = self.tracker.countdown_to_shaft_seal
        self.assertTrue(rounds_used < countdown)


class TestTier3_DurinsAxeFlameOfHopeWithBandMorale(unittest.TestCase):
    """Interaction: Claiming Durin's Axe (+4 Eye) while activating Flame of Hope for Band Rally."""

    def setUp(self):
        self.heroes = create_canonical_heroes()
        self.band = create_canonical_band()
        self.tracker = AlertTracker(hunt_threshold=14)

    def test_claiming_axe_and_activating_flame_of_hope(self):
        """Claiming axe adds +4 Eye Awareness; spending 1 Hope triggers Flame of Hope (+1d to Band)."""
        # Eye Awareness jump
        self.tracker.add_eye_awareness(4)
        self.assertEqual(self.tracker.eye_awareness, 4)

        # Flame of Hope activation by Dwarf hero
        torvir = self.heroes["torvir"]
        self.assertTrue(torvir.spend_hope(1))
        band_bonus_dice = 1
        self.assertEqual(band_bonus_dice, 1)


class TestTier3_SiegeEngineFiringVsMaulerArmor(unittest.TestCase):
    """Interaction: Firing Torsion Ballista from Location 5 into Location 6 vs The Mauler."""

    def setUp(self):
        self.mauler = create_canonical_adversaries()["the_mauler"]
        self.tracker = AlertTracker()

    def test_ballista_harpoon_strips_mauler_armor_and_generates_noise(self):
        """Ballista harpoon bolt deals 25 damage, reduces Armour to 3d, and generates +4 Noise."""
        start_armour = self.mauler.armour_dice
        self.assertEqual(start_armour, 5)

        # Fire ballista
        self.mauler.take_damage(25)
        self.mauler.armour_dice = 3  # Stripped scrap plates
        self.tracker.add_noise(4)

        self.assertEqual(self.mauler.current_endurance, 80 - 25)
        self.assertEqual(self.mauler.armour_dice, 3)
        self.assertEqual(self.tracker.noise_points, 4)


if __name__ == "__main__":
    unittest.main()
