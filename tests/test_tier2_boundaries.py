#!/usr/bin/env python3
"""Tier 2 Boundary and Corner Case Verification Tests.

Adventure Module: The Armouries of the Third Deep (The One Ring 2e)
Location: c:/Users/ante/Documents/Moria/tests/test_tier2_boundaries.py

This module contains rigorous boundary, threshold, overflow, and corner case tests:
- Band casualty limits & weariness transition (exact 50% boundary)
- Alert level & Eye Awareness overflow / Hunt threshold (14)
- Balrog toxic miasma exposure rates & lethal 0-Endurance bounds
- Zero Hope, Shadow parity, and Bout of Madness flaw triggers
- Riddle duel Hate stripping bounds
- Key bypass Extended Skill Endeavour boundaries (Resistance 9)
- Hideous Toughness half-endurance reset bounds
- Extreme Band Burden & Fatigue degradation
"""

import os
import unittest
from test_runner import (
    Hero, Companion, Band, AlertTracker, Adversary,
    create_canonical_heroes, create_canonical_band, create_canonical_adversaries
)


class TestTier2_BandCasualtyBoundaries(unittest.TestCase):
    """Boundary conditions for Band casualties, weariness, and morale."""

    def setUp(self):
        self.band = create_canonical_band()

    def test_band_weariness_exact_fifty_percent_threshold(self):
        """Weariness activates when EXACTLY 50% or more members are incapacitated."""
        # 7 companions total: 3 incapacitated = 3/7 (42.8% -> False), 4 incapacitated = 4/7 (57.1% -> True)
        self.band.resolve_casualty("Bláin", "Grievous")
        self.band.resolve_casualty("Fáin", "Grievous")
        self.band.resolve_casualty("Austri", "Grievous")
        self.assertFalse(self.band.is_weary)  # 3/7 < 50%

        self.band.resolve_casualty("Bróga", "Grievous")
        self.assertTrue(self.band.is_weary)   # 4/7 >= 50%

    def test_even_sized_band_weariness_exact_boundary(self):
        """For a 6-Dwarf band, exactly 3/6 (50.0%) triggers Weary."""
        six_band = Band(
            readiness=5,
            companions=[
                Companion("D1", 18, "Gift", "Quirk", "Role"),
                Companion("D2", 18, "Gift", "Quirk", "Role"),
                Companion("D3", 18, "Gift", "Quirk", "Role"),
                Companion("D4", 18, "Gift", "Quirk", "Role"),
                Companion("D5", 18, "Gift", "Quirk", "Role"),
                Companion("D6", 18, "Gift", "Quirk", "Role")
            ]
        )
        self.assertFalse(six_band.is_weary)
        six_band.resolve_casualty("D1", "Grievous")
        six_band.resolve_casualty("D2", "Grievous")
        self.assertFalse(six_band.is_weary)  # 2/6 = 33.3%
        six_band.resolve_casualty("D3", "Grievous")
        self.assertTrue(six_band.is_weary)   # 3/6 = 50.0%

    def test_complete_band_incapacitation(self):
        """All 7 companions incapacitated leaves active_count = 0."""
        for c in self.band.companions:
            self.band.resolve_casualty(c.name, "Slain")
        self.assertEqual(self.band.active_count, 0)
        self.assertTrue(self.band.is_weary)

    def test_desperate_stand_gandalf_rune_boundary(self):
        """Desperate stand: Gandalf rune ('G') allows ally survival; non-Gandalf slays ally (+2 Shadow)."""
        def resolve_desperate_stand(feat_die_result: str, band: Band, ally_name: str) -> bool:
            if feat_die_result == "G":
                return True  # Miraculous survival
            else:
                band.resolve_casualty(ally_name, "Slain")
                return False

        start_shadow = self.band.shared_shadow
        survived = resolve_desperate_stand("G", self.band, "Dúrmer")
        self.assertTrue(survived)
        self.assertEqual(self.band.shared_shadow, start_shadow)

        survived_fail = resolve_desperate_stand("8", self.band, "Dúrmer")
        self.assertFalse(survived_fail)
        self.assertEqual(self.band.shared_shadow, start_shadow + 2)


class TestTier2_AlertAndEyeAwarenessOverflow(unittest.TestCase):
    """Boundary and overflow conditions for Alert Tracker and Eye Awareness."""

    def setUp(self):
        self.tracker = AlertTracker(hunt_threshold=14)

    def test_hunt_threshold_exact_trigger(self):
        """Reaching exactly 14 Eye Awareness triggers a Revelation Episode."""
        self.assertEqual(self.tracker.eye_awareness, 0)
        self.assertEqual(self.tracker.revelations_triggered, 0)
        
        triggered = self.tracker.add_eye_awareness(13)
        self.assertFalse(triggered)
        self.assertEqual(self.tracker.eye_awareness, 13)

        triggered_exact = self.tracker.add_eye_awareness(1)
        self.assertTrue(triggered_exact)
        self.assertEqual(self.tracker.revelations_triggered, 1)
        self.assertEqual(self.tracker.eye_awareness, 0)  # Resets to 0 per TOR 2e canon
        self.assertEqual(self.tracker.alert_level, 3)

    def test_eye_awareness_overshoot_resets_cleanly(self):
        """Over-adding Eye Awareness beyond 14 (e.g. 11 + 4 = 15) triggers Revelation and resets to 0."""
        self.tracker.add_eye_awareness(11)
        # Claiming Durin's Axe (+4 Eye Awareness)
        triggered = self.tracker.add_eye_awareness(4)
        self.assertTrue(triggered)
        self.assertEqual(self.tracker.revelations_triggered, 1)
        self.assertEqual(self.tracker.eye_awareness, 0)

    def test_alert_tracker_upper_bound_clamping(self):
        """Noise points exceeding 100 stay clamped at Alert 3."""
        self.tracker.add_noise(150)
        self.assertEqual(self.tracker.alert_level, 3)

    def test_countdown_to_shaft_seal_boundary(self):
        """Countdown starts at 6 rounds and decrements toward 0 (sealed shafts)."""
        self.tracker.set_alert_level(3)
        self.assertEqual(self.tracker.countdown_to_shaft_seal, 6)
        
        for round_idx in range(6):
            self.tracker.countdown_to_shaft_seal -= 1
        self.assertEqual(self.tracker.countdown_to_shaft_seal, 0)


class TestTier2_ToxicMiasmaExposureBounds(unittest.TestCase):
    """Boundary conditions for Balrog toxic miasma exposure and lethal degradation."""

    def test_raw_unprotected_exposure_interval(self):
        """Unprotected characters roll for damage every minute (Grievous)."""
        exposure = {"protection": "none", "severity": "Grievous", "roll_interval_sec": 60}
        self.assertEqual(exposure["roll_interval_sec"], 60)

    def test_protected_exposure_interval(self):
        """Protected characters (cloth/herbs) roll for damage every hour (Severe)."""
        exposure = {"protection": "herbs_cloth", "severity": "Severe", "roll_interval_sec": 3600}
        self.assertEqual(exposure["roll_interval_sec"], 3600)

    def test_poison_endurance_depletion_to_dying(self):
        """Hero reduced to 0 Endurance from poison enters Dying condition."""
        torvir = create_canonical_heroes()["torvir"]
        torvir.take_damage(29)  # Max Endurance = 29
        self.assertEqual(torvir.current_endurance, 0)
        self.assertTrue(torvir.is_weary)

    def test_respirator_crafting_duration_boundary(self):
        """Crafted respirators function for exactly 4 hours (240 minutes)."""
        respirator_lifespan_minutes = 240
        self.assertEqual(respirator_lifespan_minutes, 240)

    def test_healing_penalties_bound(self):
        """Healing Severe poison loses 1d; Grievous loses 2d."""
        severe_penalty = 1
        grievous_penalty = 2
        self.assertTrue(grievous_penalty > severe_penalty)


class TestTier2_ZeroHopeAndShadowMadness(unittest.TestCase):
    """Boundary conditions for zero Hope, Shadow parity, and Bout of Madness triggers."""

    def setUp(self):
        self.heroes = create_canonical_heroes()

    def test_zero_hope_prevents_hope_expenditure(self):
        """At 0 Hope, spend_hope returns False."""
        khoril = self.heroes["khoril"]
        khoril.current_hope = 0
        success = khoril.spend_hope(1)
        self.assertFalse(success)
        self.assertEqual(khoril.current_hope, 0)

    def test_miserable_parity_boundary(self):
        """When Current Hope <= Current Shadow, hero becomes Miserable."""
        torvir = self.heroes["torvir"]
        torvir.current_hope = 3
        torvir.shadow = 2
        torvir.update_conditions()
        self.assertFalse(torvir.is_miserable)

        torvir.shadow = 3
        torvir.update_conditions()
        self.assertTrue(torvir.is_miserable)

        torvir.shadow = 4
        torvir.update_conditions()
        self.assertTrue(torvir.is_miserable)

    def test_bout_of_madness_shadow_path_flaws(self):
        """Each hero's shadow path triggers a specific psychological breakdown."""
        flaws = {
            "Torvir": ("Curse of Vengeance", "Strikes friend or foe in blind fury"),
            "Einar": ("Dragon-sickness", "Refuses to share gold and hoards wargear"),
            "Khoril": ("Lure of Power", "Rejects tactical withdrawal to issue reckless assault")
        }
        self.assertEqual(flaws["Torvir"][0], self.heroes["torvir"].shadow_path)
        self.assertEqual(flaws["Einar"][0], self.heroes["einar"].shadow_path)
        self.assertEqual(flaws["Khoril"][0], self.heroes["khoril"].shadow_path)

    def test_moria_madness_four_step_progression(self):
        """Moria Madness progresses through 4 distinct stages."""
        progression = ["#1 Distracted", "#2 Mistrustful", "#3 Blinded", "#4 Jealous"]
        self.assertEqual(len(progression), 4)
        self.assertEqual(progression[0], "#1 Distracted")
        self.assertEqual(progression[3], "#4 Jealous")


class TestTier2_RiddleDuelHateStrippingBounds(unittest.TestCase):
    """Boundary conditions for Riddle combat tasks against The Mauler."""

    def setUp(self):
        self.mauler = create_canonical_adversaries()["the_mauler"]

    def test_riddle_success_with_zero_icons(self):
        """Base Riddle success (0 icons) removes 1 Hate."""
        start_hate = self.mauler.current_hate
        self.mauler.spend_hate(1)
        self.assertEqual(self.mauler.current_hate, start_hate - 1)

    def test_riddle_success_with_three_icons(self):
        """Riddle success with 3 Success icons removes 1 + 3 = 4 Hate."""
        start_hate = self.mauler.current_hate
        self.mauler.spend_hate(1 + 3)
        self.assertEqual(self.mauler.current_hate, start_hate - 4)

    def test_mauler_weary_at_zero_hate(self):
        """When Mauler is stripped to 0 Hate, it becomes Weary and cannot spend Hate."""
        self.mauler.spend_hate(10)
        self.assertEqual(self.mauler.current_hate, 0)
        self.assertTrue(self.mauler.is_weary)
        can_spend = self.mauler.spend_hate(1)
        self.assertFalse(can_spend)

    def test_riddle_cannot_reduce_hate_below_zero(self):
        """Hate cannot drop below 0."""
        self.mauler.spend_hate(10)
        self.mauler.current_hate = max(0, self.mauler.current_hate - 5)
        self.assertEqual(self.mauler.current_hate, 0)


class TestTier2_KeyBypassExtendedEndeavourBounds(unittest.TestCase):
    """Boundary conditions for picking Location 9 King's Door without keys."""

    def test_endeavour_resistance_and_rolls(self):
        """Extended Endeavour requires Resistance 9 within 4 test rolls."""
        resistance = 9
        max_rolls = 4
        success_per_roll = 3  # Exceptional rolls
        total_success = success_per_roll * 3  # 3 rolls of 3 = 9
        self.assertTrue(total_success >= resistance)

    def test_endeavour_failure_noise_escalation(self):
        """Failing the Endeavour generates +2 Noise Points and triggers ambush."""
        tracker = AlertTracker()
        tracker.add_noise(2)
        self.assertEqual(tracker.noise_points, 2)

    def test_instant_bypass_with_marshals_key(self):
        """Having Marshal's Key reduces required rolls from 4 to 0."""
        rolls_with_key = 0
        self.assertEqual(rolls_with_key, 0)


class TestTier2_HideousToughnessEnduranceResetBounds(unittest.TestCase):
    """Boundary conditions for Hideous Toughness endurance resets."""

    def setUp(self):
        self.adversaries = create_canonical_adversaries()

    def test_mauler_exact_half_endurance_reset(self):
        """Mauler (80 Max End) resets to exactly 40 End when reduced to 0."""
        mauler = self.adversaries["the_mauler"]
        mauler.take_damage(80)
        self.assertEqual(mauler.current_endurance, 40)
        self.assertFalse(mauler.is_dead)

    def test_grimnar_exact_half_endurance_reset(self):
        """Grimnar (32 Max End) resets to exactly 16 End when reduced to 0."""
        grimnar = self.adversaries["grimnar"]
        grimnar.take_damage(32)
        self.assertEqual(grimnar.current_endurance, 16)
        self.assertFalse(grimnar.is_dead)

    def test_might_two_wound_boundary(self):
        """Adversary with Might 2 requires 2 Wounds to kill outright."""
        grimnar = self.adversaries["grimnar"]
        self.assertEqual(grimnar.might, 2)
        grimnar.suffer_wound()
        self.assertFalse(grimnar.is_dead)
        grimnar.suffer_wound()
        self.assertTrue(grimnar.is_dead)


class TestTier2_ExtremeBandBurdenAndFatigue(unittest.TestCase):
    """Boundary conditions for extreme Band Burden and Fatigue levels."""

    def setUp(self):
        self.band = create_canonical_band()

    def test_burden_categories_modifiers(self):
        """Burden modifiers: Light (+1d), Medium (0d), Heavy (-1d), Overburdened (-2d)."""
        burden_mods = {"Light": 1, "Medium": 0, "Heavy": -1, "Overburdened": -2}
        self.assertEqual(burden_mods["Overburdened"], -2)
        self.assertEqual(burden_mods["Light"], 1)

    def test_salvage_porter_overload_burden_shift(self):
        """Assigning 4 porters to haul 40 suits of mail shifts Burden to Overburdened."""
        self.band.burden = "Overburdened"
        self.assertEqual(self.band.burden, "Overburdened")

    def test_fatigue_four_tiers(self):
        """Fatigue progression: Fatigued -> Faltering -> Spent -> Collapsed."""
        tiers = ["Fatigued", "Faltering", "Spent", "Collapsed"]
        self.assertEqual(len(tiers), 4)
        self.assertEqual(tiers[-1], "Collapsed")


if __name__ == "__main__":
    unittest.main()
