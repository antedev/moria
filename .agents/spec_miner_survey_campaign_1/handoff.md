# Handoff Report: Campaign & Narrative Specification Mining
**Agent**: `spec_miner_survey_campaign_1`  
**Milestone**: Milestone 1 - Campaign Chronicle, Character Profiles, Lore & Narrative Context Extraction  
**Destination Report**: `c:/Users/ante/Documents/Moria/.agents/spec_miner_survey_campaign_1/spec_report.md`  
**Timestamp**: 2026-08-25T00:15:00Z

---

## 1. Observation
1. **Campaign Log Inspection (`c:/Users/ante/Documents/Moria/campaign_log.md`)**:
   - Lines 11–22: *Torvir Hammerstone* (Champion, STR 7/TN 13, HRT 2/TN 18, WIT 5/TN 15, Great Axe Mastery [Dmg 7, Inj 20], Grievous [+1 Dmg], Coat of Mail 5d, Helm +1d, Parry 15, Max End 29, Hope 10/10, Shadow 0 post-Slave Mine cleansing, Carries *The Eye of Thrym*).
   - Lines 24–35: *Einar son of Anar* (Treasure Hunter, STR 6/TN 14, HRT 3/TN 17, WIT 5/TN 15, Swords Mastery, Keen Sword [Dmg 4, Inj 16, Pierce 9–10], Mail-shirt 3d, Helm +1d, Reinforced Shield +1 Parry, *Durin's Way* +2 Parry underground, Total Parry 20, Max End 28, Hope 11/11, Shadow 2, Carries *The Broken Key* [+2 / Advantage to Scan]).
   - Lines 37–50: *Khoril Hornblower* (Captain, Guide TN 14, STR 7/TN 13, HRT 3/TN 16 via *Prowess*, WIT 4/TN 16, Long-hafted Axe [Dmg 6, Inj 18/20], Bow [Dmg 3, Inj 14], Total Parry 17, Max End 29, Hope 11/11, Shadow 1, Carries *Battle-horn of the Realm* [+1 Battle]).
   - Lines 53–74: Band Readiness 5 (TN 15), Medium Size (5–8), Dispositions: War 3, Vigilance 2, Manoeuvre 2, Expertise 2, Rally 1; Active Companions: *Bláin, Fáin, Dúrmer, Hjoldring, Bróga, Austri, Dolg*.
   - Lines 76–80: Rescued Captives: *Frór, The Traumatized Dwarf, Haldor* (safe at East-Gate).
   - Lines 95–106: Antagonist dynamics: *Grimnar the Disgraced* (Great Orc Bodyguard, defeated at Durin's Bridge, seeking revenge), *Malech One-eye* (Fortress of Malech/Palace of Stairs), *Grik* (Goblin spy for Granny Goblin), *Bildor* (survived, saved for later).
2. **Session Prep Inspection (`c:/Users/ante/Documents/Moria/session_prep_armouries.md`)**:
   - Lines 20–34: Extended Fellowship Phase restores Hope (Einar 11, Torvir 10, Khoril 11) and cleanses 2 Shadow each (Einar 2, Torvir 0, Khoril 1); Band heals injuries and promotes Dúrmer to Hardened.
   - Lines 54–59: Undertaking *Reclaim a Safe Haven (Caves of Thrym Thistlebeard)* establishes haven and shifts path to Wild Land (+3 AP, +3 SP).
   - Lines 62–84: Balin arrives in person at East-Gate; Commander Fróra tasks the squad to recover proof of Moria's wargear to persuade King Dáin Ironfoot in Erebor.
3. **Moria Sourcebook Verification (`c:/Users/ante/Documents/Moria/output/quick_indexes/TOR_Moria_2404.jsonl`)**:
   - Pages 151–154: *The Armouries of the Third Deep* (10 Keyed Locations: Mustering-Yard, Upper Gatehouse, First Armoury, Broken Hall, Second Armoury, Hall of the Mauler, Poisoned Halls, Upper Armoury, King's Door, Lower Armoury; The Mauler stat block: Attribute Level 10, End 80, Might 2, Hate 10, Armour 5d, Dull-Witted, Hideous Toughness, Strike Fear, Thick Hide; Durin's Axe rules; Balrog poison rules).
   - Pages 96–100: *The Caves of Thrym Thistlebeard* (Safe Haven features, Blood-vine, Thrym's Eye sapphire scrying mechanics).
   - Pages 110–115: *The Fortress of Malech* (Malech One-eye stats, Yagul the Snatcher, Brute Uftak, Reekbat, Drummer alert network).
   - Pages 176–180: *Balin's Expedition* (2989 TA historical timeline, council options, logistical constraints).
   - Pages 191–206: *Solo Play & Band Rules* (Band Readiness, Dispositions, Gifts, Quirks, Injury conditions, Burden, Weary).
4. **Core Rules Reference (`c:/Users/ante/Documents/Moria/output/quick_indexes/The_One_Ring_Core_Rules_2401_(Third_Printing).jsonl`)**:
   - Pages 148–154: Great Orc Chief (Level 7, End 48, Hate 7, Armour 4d), Great Orc Bodyguard (Level 6, End 24/32, Hate 6, Armour 3d, Hideous Toughness), Orc Soldiers, Orc Guards, Goblin Archers.

---

## 2. Logic Chain
1. **Premise**: The adventure module requires a mathematically balanced, lore-accurate, and structurally sound foundation integrating existing campaign continuity with official *The One Ring 2e* mechanics.
2. **Character & Band Integration**:
   - Torvir, Einar, and Khoril have specific tactical strengths (Torvir's high damage/axe mastery, Einar's elite Parry of 20 and scanning capabilities via *The Broken Key*, Khoril's Guide role and battle leadership).
   - The 7 companions (*Bláin, Fáin, Dúrmer, Hjoldring, Bróga, Austri, Dolg*) map cleanly to tactical squad roles (Phalanx, Sentry Sharpshooter, Sapper/Vaultbreaker, Scout, Salvage Porter).
   - Band Readiness 5 sets the Band TN at 15 (`20 - 5 = 15`), and Dispositions (*War 3, Vigilance 2, Manoeuvre 2, Expertise 2, Rally 1*) provide the dice pools for all squad-level actions.
3. **Lore & Relic Bounds**:
   - *The Eye of Thrym* is explicitly tied to statues in Thistlebeard's Caves; it is inactive in the Third Deep, preserving tension and preventing remote scanning exploits.
   - *The Broken Key* gives +2/Advantage on Scan tests, making Einar the premier trap-finder.
   - *Khoril's Battle-horn* gives +1 Battle and allows Band rally, but increases the Alert Tracker (+1) and Eye Awareness (+2) due to subterranean acoustic echo.
   - *Durin's Axe* is a royal artifact in the Lower Vault, protected by the sealed King's Door and a +4 Eye Awareness surge upon claim.
4. **Antagonist Threat Escalation**:
   - *Grimnar the Disgraced* provides a personal nemesis narrative stemming from the Durin's Bridge battle, stalking the party and setting up an ambush at the King's Door.
   - *The Mauler* provides an epic set-piece encounter with both physical and non-lethal (Riddle duel) solutions.
   - *Grik the Skulker* acts as a neutral goblin conduit providing clues to the lost Marshal's Key.
   - An anti-swarm Alert Tracker (0 to 3) prevents sudden TPK hordes while enforcing stealth discipline.

---

## 3. Caveats
- *Bildor* (Frór's traitorous brother) survived the slave-mine raid according to the campaign log, but per the original request and narrative focus, he is deliberately held in reserve for future campaign arcs and does not appear in the Third Deep armouries.
- Rescued non-combatants (*Frór, The Traumatized Dwarf, Haldor*) are safely stationed at the East-Gate camp and do not accompany the tactical strike team into the Third Deep.

---

## 4. Conclusion
All campaign context, mechanical statblocks, companion rosters, relic statuses, antagonist profiles, and narrative pacing frameworks have been rigorously verified against authoritative sources and documented in `spec_report.md`. The design is fully primed for subsequent module architecture, dungeon design, and GM play aid generation.

---

## 5. Verification Method
- Inspect `c:/Users/ante/Documents/Moria/.agents/spec_miner_survey_campaign_1/spec_report.md` for complete tables and section-by-section coverage.
- Cross-reference stat numbers with `c:/Users/ante/Documents/Moria/campaign_log.md` lines 11–74.
- Cross-reference landmark details and adversary stats with `output/quick_indexes/TOR_Moria_2404.jsonl` lines 100–105 (Thistlebeard), 114–119 (Malech), 155–160 (Armouries), and 194–205 (Band rules).
