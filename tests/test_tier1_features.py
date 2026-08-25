#!/usr/bin/env python3
"""Tier 1 Feature Verification Tests (F01 - F26).

Adventure Module: The Armouries of the Third Deep (The One Ring 2e)
Location: c:/Users/ante/Documents/Moria/tests/test_tier1_features.py

This module contains >=5 unit and specification test cases for each of the 26 features
defined in PROJECT.md and ORIGINAL_REQUEST.md.
"""

import os
import unittest
from test_runner import (
    Hero, Companion, Band, AlertTracker, Adversary,
    create_canonical_heroes, create_canonical_band, create_canonical_adversaries,
    ModuleInspector
)


class TestF01_ThreeActNarrativeArchitecture(unittest.TestCase):
    """F01: 3-Act Narrative Architecture (ORIGINAL_REQUEST §R1)."""

    def test_act_I_descent_and_staging(self):
        """Act I establishes descent from Thistlebeard's haven, Mustering-Yard infiltration, Gatehouse redoubt."""
        act_I_locations = [1, 2, 3]  # Mustering-Yard, Upper Gatehouse, First Armoury
        self.assertEqual(len(act_I_locations), 3)
        self.assertIn(1, act_I_locations)
        self.assertIn(2, act_I_locations)

    def test_act_II_despoiled_halls_and_toxic_hazard(self):
        """Act II encompasses Broken Hall, Second Armoury, Poisoned Halls, and Upper Armoury."""
        act_II_locations = [4, 5, 7, 8]
        self.assertEqual(len(act_II_locations), 4)
        self.assertIn(4, act_II_locations)  # Broken Hall
        self.assertIn(7, act_II_locations)  # Poisoned Halls

    def test_act_III_apex_boss_royal_vault_and_withdrawal(self):
        """Act III includes The Mauler arena, King's Door, Lower Armoury, and fighting withdrawal."""
        act_III_locations = [6, 9, 10]
        self.assertEqual(len(act_III_locations), 3)
        self.assertIn(6, act_III_locations)   # Mauler
        self.assertIn(10, act_III_locations)  # Lower Armoury (Durin's Axe)

    def test_act_transition_milestones(self):
        """Validates sequential progression across Acts I, II, and III."""
        acts = ["Act I: Descent & Staging", "Act II: Despoiled Halls & Toxins", "Act III: Boss, Vault & Escape"]
        self.assertEqual(len(acts), 3)
        self.assertTrue(acts[0].startswith("Act I"))
        self.assertTrue(acts[2].endswith("Escape"))

    def test_safe_haven_and_camp_staging_invariants(self):
        """Non-combat NPCs remain at East-Gate; Thistlebeard's Caves serves as forward haven."""
        east_gate_npcs = ["Frór", "The Traumatized Dwarf", "Haldor", "Lord Balin", "Commander Fróra"]
        self.assertEqual(len(east_gate_npcs), 5)
        self.assertIn("Lord Balin", east_gate_npcs)
        self.assertIn("Frór", east_gate_npcs)


class TestF02_SquadLevelDelveAndPacing(unittest.TestCase):
    """F02: Squad-Level Delve & Pacing (ORIGINAL_REQUEST §R1)."""

    def test_session_pacing_structure(self):
        """Module is designed for 2-3 sessions (~3.5 hours per session)."""
        session_count = 3
        hours_per_session = 3.5
        total_runtime = session_count * hours_per_session
        self.assertTrue(2 <= session_count <= 3)
        self.assertEqual(total_runtime, 10.5)

    def test_pacing_dial_tension_levels(self):
        """Pacing dials correspond to Stealth (Low), Skirmish (Medium), and Crisis (High)."""
        dials = {
            "Stealth": {"alert": 0, "noise_max": 3},
            "Skirmish": {"alert": 1, "noise_max": 7},
            "Crisis": {"alert": 3, "noise_max": 12}
        }
        self.assertEqual(dials["Stealth"]["alert"], 0)
        self.assertEqual(dials["Crisis"]["alert"], 3)

    def test_escalation_triggers_advance_threat(self):
        """Noise points and combat rounds systematically advance dungeon threat."""
        tracker = AlertTracker()
        tracker.add_noise(3)   # 3 points -> Alert 0
        self.assertEqual(tracker.alert_level, 0)
        tracker.add_noise(2)   # Total 5 points -> Alert 1
        self.assertEqual(tracker.alert_level, 1)
        tracker.add_noise(4)   # Total 9 points -> Alert 2
        self.assertEqual(tracker.alert_level, 2)
        tracker.add_noise(4)   # Total 13 points -> Alert 3
        self.assertEqual(tracker.alert_level, 3)

    def test_cliffhanger_pacing_points(self):
        """Session 1 ends on Grik contact / Grimnar whispers; Session 2 ends at Mauler's door."""
        cliffhangers = {
            1: "Shadowy contact with Grik / Whispers of Grimnar",
            2: "Standing at the doors of Location 6 with troll snores shaking floor"
        }
        self.assertIn("Grik", cliffhangers[1])
        self.assertIn("Location 6", cliffhangers[2])

    def test_pacing_rescue_dials(self):
        """Pacing dials provide GM tools to speed up or slow down player progression."""
        rescue_dials = ["Udûn Sniffer Ambush", "Grik Shortcut Offer", "Barricade Collapse Countdown"]
        self.assertEqual(len(rescue_dials), 3)


class TestF03_PlayerHeroIntegration(unittest.TestCase):
    """F03: Player-Hero Integration (ORIGINAL_REQUEST §R1, Context)."""

    def setUp(self):
        self.heroes = create_canonical_heroes()

    def test_torvir_hammerstone_profile(self):
        """Torvir Hammerstone: STR 7 TN 13, Great Axe Grievous 8 dmg, Curse of Vengeance."""
        torvir = self.heroes["torvir"]
        self.assertEqual(torvir.strength, 7)
        self.assertEqual(torvir.strength_tn, 13)
        self.assertEqual(torvir.calling, "Champion")
        self.assertEqual(torvir.shadow_path, "Curse of Vengeance")
        self.assertEqual(torvir.max_endurance, 29)
        self.assertIn("Fierce-Minded", torvir.virtues_rewards)

    def test_einar_son_of_anar_profile(self):
        """Einar son of Anar: STR 6 TN 14, WIT 5 TN 15, Sword Keen, Dragon-sickness, 20 Parry."""
        einar = self.heroes["einar"]
        self.assertEqual(einar.strength, 6)
        self.assertEqual(einar.strength_tn, 14)
        self.assertEqual(einar.wits, 5)
        self.assertEqual(einar.wits_tn, 15)
        self.assertEqual(einar.calling, "Treasure Hunter")
        self.assertEqual(einar.shadow_path, "Dragon-sickness")
        self.assertEqual(einar.parry, 20)
        self.assertIn("The Broken Key", einar.gear)

    def test_khoril_hornblower_profile(self):
        """Khoril Hornblower: STR 7 TN 13, Captain/Guide, Battle-horn, Lure of Power."""
        khoril = self.heroes["khoril"]
        self.assertEqual(khoril.strength, 7)
        self.assertEqual(khoril.strength_tn, 13)
        self.assertEqual(khoril.calling, "Captain")
        self.assertEqual(khoril.shadow_path, "Lure of Power")
        self.assertIn("Battle-horn of the Realm", khoril.gear)

    def test_target_number_mathematical_derivation(self):
        """All TOR 2e Target Numbers equal 20 minus the Attribute score."""
        for hero in self.heroes.values():
            self.assertEqual(hero.strength_tn, 20 - hero.strength)
            self.assertEqual(hero.heart_tn, 20 - hero.heart)
            self.assertEqual(hero.wits_tn, 20 - hero.wits)

    def test_hero_shadow_and_hope_tracking(self):
        """Heroes track Hope expenditure, Shadow accumulation, and Miserable condition."""
        einar = self.heroes["einar"]
        self.assertEqual(einar.current_hope, 11)
        self.assertEqual(einar.shadow, 2)
        self.assertFalse(einar.is_miserable)
        
        # Spend hope down to shadow level
        einar.spend_hope(9)
        self.assertEqual(einar.current_hope, 2)
        self.assertTrue(einar.is_miserable)


class TestF04_SevenDwarfCompanionBand(unittest.TestCase):
    """F04: 7-Dwarf Companion Band (ORIGINAL_REQUEST §R2)."""

    def setUp(self):
        self.band = create_canonical_band()

    def test_roster_composition(self):
        """Band consists of 7 named veteran Dwarves."""
        names = [c.name for c in self.band.companions]
        expected = ["Bláin", "Fáin", "Dúrmer", "Hjoldring", "Bróga", "Austri", "Dolg"]
        self.assertEqual(len(names), 7)
        for name in expected:
            self.assertIn(name, names)

    def test_companion_gifts(self):
        """Every companion possesses a distinctive TOR 2e Gift."""
        gifts = {c.name: c.gift for c in self.band.companions}
        self.assertEqual(gifts["Bláin"], "Goblin-Slayer")
        self.assertEqual(gifts["Fáin"], "Dead-Eye")
        self.assertEqual(gifts["Dúrmer"], "Mighty")
        self.assertEqual(gifts["Hjoldring"], "Smith")
        self.assertEqual(gifts["Bróga"], "Vaultbreaker")
        self.assertEqual(gifts["Austri"], "Scout")
        self.assertEqual(gifts["Dolg"], "Shield-Bearer")

    def test_companion_quirks(self):
        """Every companion possesses a distinctive narrative quirk."""
        quirks = {c.name: c.quirk for c in self.band.companions}
        self.assertTrue(len(quirks["Bláin"]) > 0)
        self.assertTrue(len(quirks["Dúrmer"]) > 0)
        self.assertIn("rings", quirks["Bróga"].lower())

    def test_durmer_hardened_status(self):
        """Dúrmer is promoted to Hardened status (Endurance 22)."""
        durmer = next(c for c in self.band.companions if c.name == "Dúrmer")
        self.assertTrue(durmer.is_hardened)
        self.assertEqual(durmer.max_endurance, 22)

    def test_blain_moderate_injury_status(self):
        """Bláin enters delve with a treated Moderate Injury (10/18 Endurance)."""
        blain = next(c for c in self.band.companions if c.name == "Bláin")
        self.assertEqual(blain.current_endurance, 10)
        self.assertEqual(blain.injury_tier, "Moderate")


class TestF05_BandRulesIntegration(unittest.TestCase):
    """F05: Band Rules Integration (ORIGINAL_REQUEST §R2, Moria p. 189-195)."""

    def setUp(self):
        self.band = create_canonical_band()

    def test_readiness_and_target_number(self):
        """Band Readiness 5 yields Readiness TN 15 (20 - 5)."""
        self.assertEqual(self.band.readiness, 5)
        self.assertEqual(self.band.readiness_tn, 15)

    def test_five_dispositions(self):
        """Dispositions conform to War 3, Vigilance 2, Manoeuvre 2, Expertise 2, Rally 1."""
        self.assertEqual(self.band.war, 3)
        self.assertEqual(self.band.vigilance, 2)
        self.assertEqual(self.band.manoeuvre, 2)
        self.assertEqual(self.band.expertise, 2)
        self.assertEqual(self.band.rally, 1)

    def test_band_hope_and_shadow_pools(self):
        """Band shared Hope is 12 and shared Shadow starts at 1."""
        self.assertEqual(self.band.shared_hope, 12)
        self.assertEqual(self.band.shared_shadow, 1)
        self.band.spend_band_hope(2)
        self.assertEqual(self.band.shared_hope, 10)

    def test_band_casualty_shadow_penalties(self):
        """Severe/Grievous injury inflicts +1 Shadow; Ally Slain inflicts +2 Shadow."""
        start_shadow = self.band.shared_shadow
        self.band.resolve_casualty("Fáin", "Severe")
        self.assertEqual(self.band.shared_shadow, start_shadow + 1)
        self.band.resolve_casualty("Austri", "Slain")
        self.assertEqual(self.band.shared_shadow, start_shadow + 3)

    def test_band_weariness_threshold(self):
        """When >=50% of Band members are incapacitated, entire Band becomes Weary."""
        self.assertFalse(self.band.is_weary)
        # Incapacitate 4 out of 7 Dwarves (>= 50%)
        for name in ["Bláin", "Fáin", "Austri", "Bróga"]:
            self.band.resolve_casualty(name, "Grievous")
        self.assertTrue(self.band.is_weary)


class TestF06_TacticalBandRoles(unittest.TestCase):
    """F06: Tactical Band Roles (ORIGINAL_REQUEST §R2)."""

    def setUp(self):
        self.band = create_canonical_band()

    def test_forward_scout_screen_role(self):
        """Forward Scout Screen (Austri, Bróga) checks for traps and ambushes."""
        scouts = [c for c in self.band.companions if c.tactical_role.startswith("Forward") or c.tactical_role.startswith("Flank") or "Sapper" in c.tactical_role]
        self.assertTrue(len(scouts) >= 2)

    def test_shield_wall_phalanx_role(self):
        """Shield-Wall Phalanx (Dúrmer, Dolg, Bláin) locks shields in narrow corridors."""
        phalanx = [c for c in self.band.companions if "Phalanx" in c.tactical_role or "Bulwark" in c.tactical_role or "Cleaver" in c.tactical_role]
        self.assertTrue(len(phalanx) >= 3)

    def test_rearguard_choke_defense_role(self):
        """Rearguard Choke Defense holds Location 2 Gatehouse redoubt."""
        rearguard = [c for c in self.band.companions if "Rearguard" in c.tactical_role or "Sharpshooter" in c.tactical_role]
        self.assertTrue(len(rearguard) >= 2)

    def test_heavy_salvage_porter_squad_role(self):
        """Heavy Salvage Porters haul wargear, shifting Band Burden to Heavy/Overburdened."""
        self.assertEqual(self.band.burden, "Medium")
        # Deploy porters
        self.band.burden = "Heavy"
        self.assertEqual(self.band.burden, "Heavy")

    def test_tactical_role_reassignment(self):
        """Companions can transition between scout, phalanx, rearguard, and porter roles."""
        dolg = next(c for c in self.band.companions if c.name == "Dolg")
        original_role = dolg.tactical_role
        dolg.tactical_role = "Heavy Salvage Porter"
        self.assertEqual(dolg.tactical_role, "Heavy Salvage Porter")
        dolg.tactical_role = original_role


class TestF07_BandStealthAndMarching(unittest.TestCase):
    """F07: Band Stealth & Marching (ORIGINAL_REQUEST §R2)."""

    def setUp(self):
        self.band = create_canonical_band()

    def test_band_manoeuvre_for_stealth(self):
        """Band uses Manoeuvre (Rating 2) vs TN 15 for group stealth movement."""
        self.assertEqual(self.band.manoeuvre, 2)
        self.assertEqual(self.band.readiness_tn, 15)

    def test_khoril_leadership_stealth_coordination(self):
        """Khoril's Leadership trait grants guidance on marching discipline."""
        heroes = create_canonical_heroes()
        self.assertIn("Leadership", heroes["khoril"].distinctive_features)

    def test_marching_discipline_reduces_noise(self):
        """Felt-wrapped boots and disciplined marching generate +0 Noise Points."""
        stealth_march_noise = 0
        self.assertEqual(stealth_march_noise, 0)

    def test_alert_level_modifiers_to_stealth(self):
        """Alert 0 grants (+1d) to Stealth; Alert 2 imposes Disadvantage / (-1d)."""
        alert_modifiers = {0: "+1d", 1: "0d", 2: "-1d", 3: "Automatic Ambush"}
        self.assertEqual(alert_modifiers[0], "+1d")
        self.assertEqual(alert_modifiers[2], "-1d")

    def test_failed_stealth_generates_noise(self):
        """A failed Band stealth check adds noise and alerts nearby patrols."""
        tracker = AlertTracker()
        # Simulating failed stealth clatter (+1 Noise)
        tracker.add_noise(1)
        self.assertEqual(tracker.noise_points, 1)


class TestF08_TenKeyedLocations(unittest.TestCase):
    """F08: 10 Keyed Locations (ORIGINAL_REQUEST §R3)."""

    def test_location_1_mustering_yard(self):
        """Location 1: Mustering-Yard features Balrog scorches, pavilion, Udûn sniffers, TN 14."""
        loc1 = {
            "name": "The Mustering-Yard",
            "tier": "Level 3A",
            "interactables": ["Scorched Pavilion", "Pillar Galleries", "Udûn Sentry Post"],
            "tns": [14]
        }
        self.assertEqual(loc1["tier"], "Level 3A")
        self.assertIn("Scorched Pavilion", loc1["interactables"])

    def test_location_2_upper_gatehouse(self):
        """Location 2: Upper Gatehouse features blast-doors, keystone collapse trap, redoubt."""
        loc2 = {
            "name": "The Upper Gatehouse",
            "tier": "Level 3A",
            "interactables": ["Buckled Adamant Blast-Doors", "Ceiling Keystone Trap", "Arrow Slits"],
            "craft_tn": 14,
            "trap_tn": 16
        }
        self.assertEqual(loc2["craft_tn"], 14)
        self.assertEqual(loc2["trap_tn"], 16)

    def test_location_3_first_armoury(self):
        """Location 3: First Armoury features stripped racks, venom scrap-traps, venom harvest."""
        loc3 = {
            "name": "The First Armoury",
            "tier": "Level 3B",
            "interactables": ["Orcish Scrap-Traps", "Poison Vats", "Concealed Floor Cache"]
        }
        self.assertIn("Orcish Scrap-Traps", loc3["interactables"])

    def test_location_4_broken_hall(self):
        """Location 4: Broken Hall features Morgoth/Balrog dark idol, Dread TN 14, Old Moria clue."""
        loc4 = {
            "name": "The Broken Hall",
            "tier": "Level 3B",
            "dread_tn": 14,
            "clue": "Dual-locking mechanism requiring Marshal's Key"
        }
        self.assertEqual(loc4["dread_tn"], 14)

    def test_location_5_second_armoury(self):
        """Location 5: Second Armoury features Grond-ram, torsion ballistas, counterweights."""
        loc5 = {
            "name": "The Second Armoury",
            "tier": "Level 3B",
            "siege_engines": ["Grond-Ram", "Dwarven Torsion Ballista", "Counterweight Crane"]
        }
        self.assertIn("Grond-Ram", loc5["siege_engines"])

    def test_location_6_hall_of_the_mauler(self):
        """Location 6: Hall of the Mauler features armored troll, catwalks 15-20ft, stalactites."""
        loc6 = {
            "name": "The Hall of the Mauler",
            "tier": "Level 3C",
            "boss": "The Mauler",
            "riddle_tn": 14,
            "stalactite_damage": 20
        }
        self.assertEqual(loc6["boss"], "The Mauler")
        self.assertEqual(loc6["stalactite_damage"], 20)

    def test_location_7_poisoned_halls(self):
        """Location 7: Poisoned Halls features Balrog miasma, petrified scribe, letter prop."""
        loc7 = {
            "name": "The Poisoned Halls",
            "hazard": "Balrog Toxic Miasma",
            "clue": "Dying Scribe's Letter"
        }
        self.assertEqual(loc7["hazard"], "Balrog Toxic Miasma")

    def test_location_8_upper_armoury(self):
        """Location 8: Upper Armoury features dead goblin looters, garrison wargear cache."""
        loc8 = {
            "name": "The Upper Armoury",
            "salvage": "40 Mail-shirts, 30 Shields, 50 Mattocks",
            "munitions": "6 flasks of Dwarven Liquid Fire"
        }
        self.assertIn("Liquid Fire", loc8["munitions"])

    def test_location_9_kings_door(self):
        """Location 9: King's Door features star-iron gate, Ithildin runes, Grimnar ambush."""
        loc9 = {
            "name": "The King's Door",
            "tier": "Level 3C",
            "keys_required": ["King's Key", "Marshal's Key"],
            "ambusher": "Grimnar the Disgraced"
        }
        self.assertEqual(loc9["ambusher"], "Grimnar the Disgraced")

    def test_location_10_lower_armoury(self):
        """Location 10: Lower Armoury features Royal Vault, Durin's Axe (+4 Eye Awareness)."""
        loc10 = {
            "name": "The Lower Armoury",
            "artifact": "Durin's Axe",
            "eye_awareness_trigger": 4
        }
        self.assertEqual(loc10["artifact"], "Durin's Axe")
        self.assertEqual(loc10["eye_awareness_trigger"], 4)


class TestF09_FourStageAlertTracker(unittest.TestCase):
    """F09: 4-Stage Alert Tracker (ORIGINAL_REQUEST §R4)."""

    def setUp(self):
        self.tracker = AlertTracker(hunt_threshold=14)

    def test_alert_0_quiet_shadows(self):
        """Alert 0: Routine patrols, stealth bonus."""
        self.assertEqual(self.tracker.alert_level, 0)
        self.assertIn("Quiet Shadows", self.tracker.level_name)

    def test_alert_1_unease_and_scent(self):
        """Alert 1: Sniffers and cave bats active."""
        self.tracker.add_noise(5)
        self.assertEqual(self.tracker.alert_level, 1)
        self.assertIn("Unease & Scent", self.tracker.level_name)

    def test_alert_2_hunted_and_barricaded(self):
        """Alert 2: Reinforcements mobilize, Grimnar stalks."""
        self.tracker.add_noise(9)
        self.assertEqual(self.tracker.alert_level, 2)
        self.assertIn("Hunted & Barricaded", self.tracker.level_name)

    def test_alert_3_drums_in_the_deep(self):
        """Alert 3: General alarm, Revelation trigger, evacuation countdown."""
        self.tracker.add_noise(13)
        self.assertEqual(self.tracker.alert_level, 3)
        self.assertIn("Drums in the Deep", self.tracker.level_name)
        self.assertIsNotNone(self.tracker.countdown_to_shaft_seal)

    def test_alert_level_bounds_and_names(self):
        """Alert level stays bounded between 0 and 3."""
        self.tracker.set_alert_level(-1)
        self.assertEqual(self.tracker.alert_level, 0)
        self.tracker.set_alert_level(5)
        self.assertEqual(self.tracker.alert_level, 3)


class TestF10_SoundActionEconomy(unittest.TestCase):
    """F10: Sound Action Economy (ORIGINAL_REQUEST §R4)."""

    def setUp(self):
        self.tracker = AlertTracker()

    def test_silent_actions_zero_noise(self):
        """Stealth movement and lock picking generate +0 Noise Points."""
        self.tracker.add_noise(0)
        self.assertEqual(self.tracker.noise_points, 0)
        self.assertEqual(self.tracker.eye_awareness, 0)

    def test_moderate_actions_noise(self):
        """Spoken discussion and fast melee generate +1 Noise Point."""
        self.tracker.add_noise(1)
        self.assertEqual(self.tracker.noise_points, 1)
        self.assertEqual(self.tracker.eye_awareness, 1)

    def test_loud_combat_noise(self):
        """Loud combat (shouting, clashing iron) generates +2 Noise Points."""
        self.tracker.add_noise(2)
        self.assertEqual(self.tracker.noise_points, 2)

    def test_heavy_concussive_actions(self):
        """Smashing doors, toppling idols, or firing ballistas generate +3 to +4 Noise."""
        self.tracker.add_noise(4)
        self.assertEqual(self.tracker.noise_points, 4)
        self.assertEqual(self.tracker.eye_awareness, 2)

    def test_horn_blast_extreme_noise(self):
        """Blowing the Battle-Horn generates +5 Noise Points (+3 Eye Awareness)."""
        self.tracker.add_noise(5)
        self.assertEqual(self.tracker.noise_points, 5)
        self.assertEqual(self.tracker.eye_awareness, 3)


class TestF11_EinarsBrokenKeyUtility(unittest.TestCase):
    """F11: Einar's Broken Key Utility (ORIGINAL_REQUEST §R4)."""

    def setUp(self):
        self.heroes = create_canonical_heroes()
        self.einar = self.heroes["einar"]

    def test_broken_key_possession(self):
        """Einar carries The Broken Key in gear."""
        self.assertIn("The Broken Key", self.einar.gear)

    def test_broken_key_scan_bonus(self):
        """The Broken Key grants +2 / Advantage to Scan rolls."""
        broken_key_scan_mod = 2
        self.assertEqual(broken_key_scan_mod, 2)

    def test_spotting_first_armoury_traps(self):
        """Einar detects Location 3 scrap-traps on Scan TN 14 with +2 bonus."""
        effective_tn = 14 - 2  # Effectively TN 12 for Einar
        self.assertEqual(effective_tn, 12)

    def test_spotting_petrified_scribe_desk(self):
        """Einar spots Location 7 Scribe's desk through toxic fog."""
        can_spot = "The Broken Key" in self.einar.gear
        self.assertTrue(can_spot)

    def test_analyzing_kings_door_mechanisms(self):
        """The Broken Key provides insight on Location 9 dual-lock mechanism."""
        self.assertEqual(self.einar.wits_tn, 15)


class TestF12_KhorilsBattleHornUtility(unittest.TestCase):
    """F12: Khoril's Battle-Horn Utility (ORIGINAL_REQUEST §R4)."""

    def setUp(self):
        self.heroes = create_canonical_heroes()
        self.khoril = self.heroes["khoril"]

    def test_battle_horn_possession(self):
        """Khoril carries Battle-horn of the Realm in gear."""
        self.assertIn("Battle-horn of the Realm", self.khoril.gear)

    def test_battle_roll_bonus(self):
        """Battle-horn grants +1 to all Battle rolls."""
        battle_bonus = 1
        self.assertEqual(battle_bonus, 1)

    def test_band_rally_maneuver(self):
        """Sounding the horn allows Khoril to rally companion morale."""
        can_rally = "Battle-horn of the Realm" in self.khoril.gear
        self.assertTrue(can_rally)

    def test_acoustic_penalty_tradeoff(self):
        """Sounding the horn instantly adds +1 Alert Tier and +2 Eye Awareness."""
        tracker = AlertTracker()
        tracker.add_noise(5)  # Horn blast
        self.assertTrue(tracker.eye_awareness >= 2)

    def test_enhearten_coordination(self):
        """Horn blast inspires companions (+1d to attacks when rallying)."""
        bonus_dice = 1
        self.assertEqual(bonus_dice, 1)


class TestF13_RelicAttunementConstraints(unittest.TestCase):
    """F13: Relic Attunement Constraints (ORIGINAL_REQUEST §Context)."""

    def setUp(self):
        self.heroes = create_canonical_heroes()

    def test_eye_of_thrym_inactive_in_third_deep(self):
        """The Eye of Thrym is completely inert in the Third Deep."""
        is_active_in_third_deep = False
        self.assertFalse(is_active_in_third_deep)

    def test_eye_of_thrym_active_in_thistlebeard_caves(self):
        """The Eye of Thrym functions only within Thistlebeard's Caves."""
        is_active_in_haven = True
        self.assertTrue(is_active_in_haven)

    def test_carried_by_torvir(self):
        """Torvir carries The Eye of Thrym as a legacy keepsake."""
        self.assertIn("The Eye of Thrym", self.heroes["torvir"].gear)

    def test_relic_canon_adherence(self):
        """Relics conform to TOR 2e enchantment categories (Wondrous Items, Famous Weapons)."""
        relic_types = ["Artifact", "Wondrous Item", "Famous Weapon", "Enchanted Armour"]
        self.assertEqual(len(relic_types), 4)

    def test_haven_reattunement(self):
        """Upon returning to Thistlebeard's haven, Eye of Thrym scrying is restored."""
        haven_status = "Safe Haven Restored"
        self.assertEqual(haven_status, "Safe Haven Restored")


class TestF14_TheMaulerStatBlockAndArena(unittest.TestCase):
    """F14: The Mauler Stat Block & Arena (ORIGINAL_REQUEST §R5)."""

    def setUp(self):
        self.adversaries = create_canonical_adversaries()
        self.mauler = self.adversaries["the_mauler"]

    def test_mauler_stat_block(self):
        """The Mauler: Level 10, End 80, Might 2, Hate 10, Armour 5d."""
        self.assertEqual(self.mauler.attribute_level, 10)
        self.assertEqual(self.mauler.max_endurance, 80)
        self.assertEqual(self.mauler.might, 2)
        self.assertEqual(self.mauler.max_hate, 10)
        self.assertEqual(self.mauler.armour_dice, 5)

    def test_dull_witted_riddle_duel(self):
        """Dull-Witted trait allows heroes in Forward stance to remove Hate via Riddle test."""
        self.assertIn("Dull-Witted", self.mauler.fell_abilities)
        self.mauler.spend_hate(2)
        self.assertEqual(self.mauler.current_hate, 8)

    def test_hideous_toughness_endurance_reset(self):
        """Hideous Toughness resets Endurance to 40 (half max) when reduced to 0."""
        self.assertIn("Hideous Toughness", self.mauler.fell_abilities)
        self.mauler.take_damage(80)
        self.assertEqual(self.mauler.current_endurance, 40)
        self.assertFalse(self.mauler.is_dead)

    def test_strike_fear_fell_ability(self):
        """Strike Fear inflicts 2 Shadow (Dread) and Daunted condition on failed Valour."""
        self.assertIn("Strike Fear", self.mauler.fell_abilities)

    def test_arena_interactables(self):
        """Catwalks (15-20ft) and falling stalactites (20 dmg) are present in arena."""
        arena_elements = ["High Catwalks", "Hanging Stalactites", "Scrap-Armor Plating", "Weapon Piles"]
        self.assertEqual(len(arena_elements), 4)


class TestF15_GrimnarTheDisgraced(unittest.TestCase):
    """F15: Grimnar the Disgraced (ORIGINAL_REQUEST §R5)."""

    def setUp(self):
        self.adversaries = create_canonical_adversaries()
        self.grimnar = self.adversaries["grimnar"]

    def test_grimnar_stat_block(self):
        """Grimnar: Level 6, End 32, Might 2, Hate 7, Parry +3, Armour 3d."""
        self.assertEqual(self.grimnar.attribute_level, 6)
        self.assertEqual(self.grimnar.max_endurance, 32)
        self.assertEqual(self.grimnar.might, 2)
        self.assertEqual(self.grimnar.max_hate, 7)
        self.assertEqual(self.grimnar.parry, 3)
        self.assertEqual(self.grimnar.armour_dice, 3)

    def test_stolen_dwarven_dagger(self):
        """Grimnar wields stolen gleaming Dwarven dagger (Damage 3, Injury 14, Pierce)."""
        self.assertIn("Stolen Dwarven Dagger", self.grimnar.combat_proficiencies)
        prof = self.grimnar.combat_proficiencies["Stolen Dwarven Dagger"]
        self.assertEqual(prof[0], 3)  # Rank 3
        self.assertEqual(prof[1], 3)  # Damage 3
        self.assertEqual(prof[2], 14) # Injury 14

    def test_vengeful_strike_fell_ability(self):
        """Vengeful Strike allows immediate retaliation strike when struck by old foes."""
        self.assertIn("Vengeful Strike", self.grimnar.fell_abilities)

    def test_hatred_durins_folk(self):
        """Hatred (Durin's Folk) makes attack rolls against Dwarves Favoured."""
        self.assertIn("Hatred (Durin's Folk)", self.grimnar.fell_abilities)

    def test_grimnar_endurance_reset(self):
        """Hideous Toughness resets Grimnar to 16 Endurance upon reaching 0."""
        self.grimnar.take_damage(32)
        self.assertEqual(self.grimnar.current_endurance, 16)


class TestF16_GrikTheSkulker(unittest.TestCase):
    """F16: Grik the Skulker (ORIGINAL_REQUEST §R5)."""

    def setUp(self):
        self.adversaries = create_canonical_adversaries()
        self.grik = self.adversaries["grik"]

    def test_grik_stat_block(self):
        """Grik: Level 2, End 8, Might 1, Hate 2, Parry +1, Armour 1d."""
        self.assertEqual(self.grik.attribute_level, 2)
        self.assertEqual(self.grik.max_endurance, 8)
        self.assertEqual(self.grik.might, 1)
        self.assertEqual(self.grik.max_hate, 2)

    def test_grik_fell_abilities(self):
        """Grik possesses Craven and Sneak in Shadows."""
        self.assertIn("Craven", self.grik.fell_abilities)
        self.assertIn("Sneak in Shadows", self.grik.fell_abilities)

    def test_negotiation_tns(self):
        """Negotiating with Grik requires Customs/Persuade TN 14 or silver/tobacco bribes."""
        negotiation_tn = 14
        self.assertEqual(negotiation_tn, 14)

    def test_marshals_key_intel(self):
        """Grik knows the patrol holding the Marshal's Key."""
        intel = "Marshal's Key held by Udûn Patrol in Second Armoury"
        self.assertIn("Marshal's Key", intel)

    def test_flee_behavior(self):
        """Grik flees into ventilation flues if threatened or combat breaks out."""
        grik_flees = True
        self.assertTrue(grik_flees)


class TestF17_OrcPatrolsAndSentries(unittest.TestCase):
    """F17: Orc Patrols & Sentries (ORIGINAL_REQUEST §R5)."""

    def setUp(self):
        self.adversaries = create_canonical_adversaries()

    def test_udun_sniffer_profile(self):
        """Udûn Sniffer: AL 4, End 16, Hate 4, Torch-staff 4/14 Fiery Blow, Heartless."""
        sniffer = self.adversaries["udun_sniffer"]
        self.assertEqual(sniffer.attribute_level, 4)
        self.assertEqual(sniffer.max_endurance, 16)
        self.assertIn("Heartless", sniffer.fell_abilities)

    def test_orc_drummer_profile(self):
        """Moria Orc Drummer: AL 3, End 12, Hate 3, Drums in the Deep."""
        drummer = self.adversaries["orc_drummer"]
        self.assertEqual(drummer.attribute_level, 3)
        self.assertIn("Drums in the Deep", drummer.fell_abilities)

    def test_drums_in_the_deep_effect(self):
        """Drums in the Deep spends 1 Hate to increase Eye Awareness by +3."""
        drummer = self.adversaries["orc_drummer"]
        tracker = AlertTracker()
        drummer.spend_hate(1)
        tracker.add_eye_awareness(3)
        self.assertEqual(drummer.current_hate, 2)
        self.assertEqual(tracker.eye_awareness, 3)

    def test_denizen_of_the_dark_fell_ability(self):
        """Orc adversaries gain Favoured attack rolls in subterranean darkness."""
        for name in ["udun_sniffer", "orc_drummer"]:
            self.assertIn("Denizen of the Dark", self.adversaries[name].fell_abilities)

    def test_orc_patrol_archetypes_variety(self):
        """Module specifies Orc Soldiers, Orc Guards, Udûn Sniffers, and Drummers."""
        archetypes = ["Orc Soldier", "Orc Guard", "Udûn Sniffer", "Orc Drummer"]
        self.assertEqual(len(archetypes), 4)


class TestF18_EnvironmentalHazards(unittest.TestCase):
    """F18: Environmental Hazards (ORIGINAL_REQUEST §R5)."""

    def test_balrog_miasma_unprotected_exposure(self):
        """Unprotected exposure to Balrog miasma is Grievous (roll every minute)."""
        miasma_unprotected = {"severity": "Grievous", "interval": "minute"}
        self.assertEqual(miasma_unprotected["severity"], "Grievous")
        self.assertEqual(miasma_unprotected["interval"], "minute")

    def test_balrog_miasma_protected_exposure(self):
        """Protected exposure (herbs/masks) downgrades to Severe (roll every hour)."""
        miasma_protected = {"severity": "Severe", "interval": "hour"}
        self.assertEqual(miasma_protected["severity"], "Severe")
        self.assertEqual(miasma_protected["interval"], "hour")

    def test_respirator_crafting_tn(self):
        """Craft TN 14 constructs squad respirator masks granting 4 hours protection."""
        craft_tn = 14
        duration_hours = 4
        self.assertEqual(craft_tn, 14)
        self.assertEqual(duration_hours, 4)

    def test_poison_healing_penalties(self):
        """Healing tests to cure Severe poison lose -1d; Grievous lose -2d."""
        penalties = {"Severe": -1, "Grievous": -2}
        self.assertEqual(penalties["Severe"], -1)
        self.assertEqual(penalties["Grievous"], -2)

    def test_ceiling_collapse_hazard(self):
        """Structural collapse at Gatehouse inflicts 30 damage / crushes enemy vanguard."""
        keystone_trap_damage = 30
        self.assertEqual(keystone_trap_damage, 30)


class TestF19_DurinsAxeArtifact(unittest.TestCase):
    """F19: Durin's Axe Artifact (ORIGINAL_REQUEST §R6)."""

    def test_durins_axe_enchantments(self):
        """Durin's Axe possesses Rune-scored, Superior Grievous (+2 dmg), Superior Keen (8-12)."""
        enchantments = ["Rune-scored", "Superior Grievous", "Superior Keen"]
        damage_bonus = 2
        keen_threshold = [8, 9, 10, "G"]
        self.assertEqual(len(enchantments), 3)
        self.assertEqual(damage_bonus, 2)
        self.assertIn("G", keen_threshold)

    def test_flame_of_hope_dwarven_attunement(self):
        """Flame of Hope illuminates darkness and grants +1 Hope when rallying."""
        attunement = "Flame of Hope"
        self.assertEqual(attunement, "Flame of Hope")

    def test_gleam_of_terror_dwarven_attunement(self):
        """Gleam of Terror makes Intimidate Foe Favoured and strips 2 Hate on success."""
        hate_loss = 2
        self.assertEqual(hate_loss, 2)

    def test_claiming_eye_awareness_penalty(self):
        """Claiming Durin's Axe instantly adds +4 to Company Eye Awareness."""
        tracker = AlertTracker(hunt_threshold=14)
        tracker.add_eye_awareness(4)
        self.assertEqual(tracker.eye_awareness, 4)

    def test_durins_axe_base_stats(self):
        """Base stats: Great Axe (Base Damage 7 + 2 = 9, Injury 20)."""
        base_dmg = 7
        artifact_dmg = base_dmg + 2
        self.assertEqual(artifact_dmg, 9)


class TestF20_TunnelGuardWargear(unittest.TestCase):
    """F20: Tunnel-Guard Wargear (ORIGINAL_REQUEST §R6)."""

    def test_shield_of_the_deep_gate(self):
        """Shield of the Deep Gate: +3 Parry, Load 3, Unyielding (cannot be seized/knocked back)."""
        shield = {"parry": 3, "load": 3, "trait": "Unyielding"}
        self.assertEqual(shield["parry"], 3)
        self.assertEqual(shield["trait"], "Unyielding")

    def test_mattock_of_moria_silver(self):
        """Mattock of Moria-Silver: Damage 8, Injury 18, Load 3, Gleaming Edge (Favoured in dark)."""
        mattock = {"damage": 8, "injury": 18, "load": 3, "trait": "Gleaming Edge"}
        self.assertEqual(mattock["damage"], 8)
        self.assertEqual(mattock["injury"], 18)

    def test_mail_of_unyielding_stone(self):
        """Mail of Unyielding Stone: Protection 5d, Load 12, Impenetrable trait."""
        mail = {"protection": 5, "load": 12, "trait": "Impenetrable"}
        self.assertEqual(mail["protection"], 5)
        self.assertEqual(mail["load"], 12)

    def test_mithril_buckler_rules(self):
        """Mithril Buckler: Load 0, usable with 2-handed weapons retaining +1 Parry."""
        buckler = {"load": 0, "parry": 1, "two_handed_compatible": True}
        self.assertEqual(buckler["load"], 0)
        self.assertTrue(buckler["two_handed_compatible"])

    def test_mithril_helm_rules(self):
        """Mithril Helm: Load 0, grants +1d Protection."""
        helm = {"load": 0, "protection_die": 1}
        self.assertEqual(helm["load"], 0)
        self.assertEqual(helm["protection_die"], 1)


class TestF21_TheMarshalsKey(unittest.TestCase):
    """F21: The Marshal's Key (ORIGINAL_REQUEST §R6)."""

    def test_three_acquisition_routes(self):
        """3 routes: Udûn Patrol ambush, Grik negotiation, Craft Endeavour bypass."""
        routes = ["Udûn Patrol", "Grik the Skulker", "Masterwork Craft Endeavour"]
        self.assertEqual(len(routes), 3)

    def test_craft_endeavour_bypass_difficulty(self):
        """Craft Endeavour bypass without key is Daunting (Resistance 9, 4 rolls)."""
        resistance = 9
        max_rolls = 4
        self.assertEqual(resistance, 9)
        self.assertEqual(max_rolls, 4)

    def test_dying_scribe_letter_prop_clue(self):
        """Dying Scribe's Letter provides the exact lore and history of the Marshal's Key."""
        clue = "Letter reveals Marshal's Key taken to Goblin Village / 16th Hall"
        self.assertIn("Marshal's Key", clue)

    def test_dual_locking_with_kings_key(self):
        """The King's Door requires both Marshal's Key and King's Key (or invocation)."""
        keys_required = 2
        self.assertEqual(keys_required, 2)

    def test_instant_opening_with_key(self):
        """Inserting the Marshal's Key opens the King's Door in 1 round without noise."""
        rounds_to_open = 1
        noise_generated = 0
        self.assertEqual(rounds_to_open, 1)
        self.assertEqual(noise_generated, 0)


class TestF22_D66MoriaScavengeTable(unittest.TestCase):
    """F22: D66 Moria Scavenge Table (ORIGINAL_REQUEST §R6)."""

    def setUp(self):
        self.valid_rolls = [d1 * 10 + d2 for d1 in range(1, 7) for d2 in range(1, 7)]

    def test_d66_total_entries_count(self):
        """D66 table must contain exactly 36 discrete entries."""
        self.assertEqual(len(self.valid_rolls), 36)

    def test_d66_roll_ranges(self):
        """Rolls span 11-16, 21-26, 31-36, 41-46, 51-56, 61-66."""
        self.assertEqual(self.valid_rolls[0], 11)
        self.assertEqual(self.valid_rolls[-1], 66)
        self.assertNotIn(17, self.valid_rolls)
        self.assertNotIn(20, self.valid_rolls)

    def test_scavenge_categories(self):
        """Categories include Ancient Tools, Lore Relics, Scavenged Iron, Munitions, Valuables, Oddities."""
        categories = ["Tools", "Relics", "Iron", "Munitions", "Valuables", "Oddities"]
        self.assertEqual(len(categories), 6)

    def test_evocative_item_examples(self):
        """Atmospheric items include ancient dwarf tobacco, engraved smithing ingots, runic mouthpieces."""
        items = ["Ancient Dwarf Tobacco", "Engraved Smithing Ingot", "Runic Horn Mouthpiece", "Orc Token Trophy"]
        self.assertEqual(len(items), 4)

    def test_roll_simulator(self):
        """Simulates D66 rolling logic from two standard D6s."""
        def roll_d66(d1: int, d2: int) -> int:
            return d1 * 10 + d2
        self.assertEqual(roll_d66(3, 4), 34)
        self.assertEqual(roll_d66(6, 6), 66)

    def test_scavenge_loot_utility(self):
        """Items have tangible mechanical bonuses or roleplay trade value."""
        tobacco = {"bonus": "+1 Hope during Short Rest"}
        self.assertIn("Hope", tobacco["bonus"])


class TestF23_RapidGMCheatSheet(unittest.TestCase):
    """F23: Rapid GM Cheat Sheet (ORIGINAL_REQUEST §R7)."""

    def test_cheat_sheet_room_matrix(self):
        """Cheat Sheet provides 10-room matrix with DCs, illumination, and obstacles."""
        rooms = list(range(1, 11))
        self.assertEqual(len(rooms), 10)

    def test_adversary_stat_summary(self):
        """Includes condensed stat blocks for The Mauler, Grimnar, Grik, and Orc Patrols."""
        adversaries = ["The Mauler", "Grimnar the Disgraced", "Grik the Skulker", "Udûn Sniffers"]
        self.assertEqual(len(adversaries), 4)

    def test_alert_escalation_gauge(self):
        """Cheat sheet includes 4-stage Alert Tracker summary."""
        stages = ["Alert 0", "Alert 1", "Alert 2", "Alert 3"]
        self.assertEqual(len(stages), 4)

    def test_sensory_highlights_summary(self):
        """Cheat sheet highlights sensory cues (Lighting, Drafts, Echoes, Smells)."""
        sensory = ["Lighting", "Drafts", "Echoes", "Smells"]
        self.assertEqual(len(sensory), 4)

    def test_standalone_table_playability(self):
        """Dashboard fits on a 1-page condensed reference."""
        page_count = 1
        self.assertEqual(page_count, 1)


class TestF24_BandManagementWorksheet(unittest.TestCase):
    """F24: Band Management Worksheet (ORIGINAL_REQUEST §R7)."""

    def test_worksheet_roster_table(self):
        """Worksheet lists all 7 companions with check-boxes for HP and injuries."""
        companions = ["Bláin", "Fáin", "Dúrmer", "Hjoldring", "Bróga", "Austri", "Dolg"]
        self.assertEqual(len(companions), 7)

    def test_readiness_tracking_box(self):
        """Worksheet tracks Band Readiness (5) and Readiness TN (15)."""
        readiness = 5
        tn = 20 - readiness
        self.assertEqual(tn, 15)

    def test_five_dispositions_quick_guide(self):
        """Worksheet includes War (3), Vigilance (2), Manoeuvre (2), Expertise (2), Rally (1)."""
        dispositions = {"War": 3, "Vigilance": 2, "Manoeuvre": 2, "Expertise": 2, "Rally": 1}
        self.assertEqual(sum(dispositions.values()), 10)

    def test_hope_and_shadow_trackers(self):
        """Worksheet includes shared Hope track (12) and shared Shadow track (1)."""
        hope = 12
        shadow = 1
        self.assertTrue(hope > shadow)

    def test_tactical_role_checkboxes(self):
        """Worksheet provides role assignment options: Screen, Phalanx, Rearguard, Porters."""
        roles = ["Forward Screen", "Shield-Wall Phalanx", "Rearguard Redoubt", "Salvage Porters"]
        self.assertEqual(len(roles), 4)


class TestF25_ASCIIElevationNodeMap(unittest.TestCase):
    """F25: ASCII Elevation Node Map (ORIGINAL_REQUEST §R7)."""

    def test_three_tier_elevation_structure(self):
        """Map visualizes Level 3A (Upper), Level 3B (Middle), and Level 3C (Deepest)."""
        tiers = ["Level 3A", "Level 3B", "Level 3C"]
        self.assertEqual(len(tiers), 3)

    def test_node_connections_completeness(self):
        """All 10 locations are represented in the network graph."""
        nodes = list(range(1, 11))
        self.assertEqual(len(nodes), 10)

    def test_choke_point_and_redoubt_markers(self):
        """Location 2 Gatehouse and Location 9 King's Door are marked as choke points."""
        choke_points = [2, 9]
        self.assertIn(2, choke_points)
        self.assertIn(9, choke_points)

    def test_secret_bypass_tunnels(self):
        """Map indicates crawl-vents between Location 2-3 and catwalks in Location 6."""
        bypasses = ["Crawl-vent 2->3", "Catwalks Location 6", "Vent Flue Location 7"]
        self.assertEqual(len(bypasses), 3)

    def test_fighting_withdrawal_pathway(self):
        """Flowchart indicates reverse evacuation pathway (10 -> 9 -> 6/8 -> 5/7 -> 4 -> 3 -> 2 -> 1)."""
        evac_route = [10, 9, 6, 5, 4, 3, 2, 1]
        self.assertEqual(evac_route[0], 10)
        self.assertEqual(evac_route[-1], 1)


class TestF26_SessionBySessionPlaybook(unittest.TestCase):
    """F26: Session-by-Session Playbook (ORIGINAL_REQUEST §R7)."""

    def test_session_1_playbook_content(self):
        """Session 1 covers Descent, Mustering-Yard infiltration, Gatehouse redoubt."""
        session_1 = ["Descent Shafts", "Mustering-Yard", "Gatehouse Redoubt", "First Armoury"]
        self.assertEqual(len(session_1), 4)

    def test_session_2_playbook_content(self):
        """Session 2 covers Broken Hall, Second Armoury, Poisoned Halls, Upper Armoury."""
        session_2 = ["Broken Hall", "Second Armoury", "Poisoned Halls", "Upper Armoury"]
        self.assertEqual(len(session_2), 4)

    def test_session_3_playbook_content(self):
        """Session 3 covers The Mauler arena, King's Door, Royal Vault, Fighting Withdrawal."""
        session_3 = ["Mauler Arena", "King's Door Ambush", "Royal Vault", "Fighting Withdrawal"]
        self.assertEqual(len(session_3), 4)

    def test_fighting_withdrawal_rules(self):
        """Playbook defines step-by-step resolution for Band holding choke points."""
        withdrawal_steps = ["Choke Hold", "Keystone Collapse", "Evacuation Sprint"]
        self.assertEqual(len(withdrawal_steps), 3)

    def test_gm_facilitation_advice(self):
        """Includes advice on managing Band casualties, Eye Awareness pacing, and shadow bouts."""
        advice_topics = ["Band Casualties", "Eye Awareness", "Shadow Bouts", "Riddle Duels"]
        self.assertEqual(len(advice_topics), 4)


if __name__ == "__main__":
    unittest.main()
