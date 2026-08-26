# Chapter 3: Operational Mechanics, Alert Systems & Environmental Hazards

> *"The dark was not empty. It was full of listening stone, and every breath of wind through the cracked flues carried the stink of brimstone and old ash."*

---

## 1. The 4-Stage Alert Tracker Subsystem

To simulate high-stakes subterranean infiltration without resorting to arbitrary monster spawns or automatic, overwhelming total party kills, operations in the Third Deep are regulated by the **4-Stage Alert Tracker**.

The Alert Tracker measures the local garrison’s awareness, suspicion, and defensive readiness. It advances when the expedition generates **Noise Points** or allows enemy messengers to escape, and directly dictates enemy behavior, patrol frequency, ambient tension, and tactical modifiers.

```
========================================================================================
                                 4-STAGE ALERT TRACKER
========================================================================================
 [ALERT 0: QUIET SHADOWS] ──► [ALERT 1: UNEASE & SCENT] ──► [ALERT 2: HUNTED & BARRICADED] ──► [ALERT 3: DRUMS IN THE DEEP]
   Noise: 0–3 Points            Noise: 4–7 Points              Noise: 8–11 Points               Noise: 12+ Points
   • Routine patrols            • Udûn sniffers active         • Choke points fortified        • Full garrison assault
   • Surprise rounds allowed    • Sentry watches doubled       • Grimnar stalks expedition     • Tunnel seal countdown
========================================================================================
```

---

### 1.1 Alert Stage Profiles & Mechanical Impact

```
========================================================================================
                              ALERT STAGE DETAILED MATRIX
========================================================================================
 STAGE            ATMOSPHERE & SENSORY CUES    ENEMY POSTURE & BEHAVIOR    MECHANICAL MODIFIERS
----------------------------------------------------------------------------------------
 Alert 0:         Tomb-like stillness; cold    Sentries loose and drowsy;  All Stealth & Explore 
 Quiet Shadows    drafts; slow water drops     Orcs gambling or squabbling tests gain +1d. 
 (0–3 Noise)      in distant shafts.           behind crude hides.         Surprise rounds allowed.
----------------------------------------------------------------------------------------
 Alert 1:         Faint rhythmic knocks in     Udûn sniffers and cave bats Standard rolls. 
 Unease & Scent   walls (tom-tap, tap-tom);    dispatched to check drafts; Wandering encounter 
 (4–7 Noise)      scent of burnt grease.       sentries stand to arms.     check on Feat Die (S).
----------------------------------------------------------------------------------------
 Alert 2:         Distant horn echoes; sulfur  Barricades manned; iron     Awareness to avoid 
 Hunted &         smoke in galleries; torches  portals bolted from inside; ambushes loses -1d. 
 Barricaded       lit along high balconies.    Grimnar actively stalks.    Hunt Threshold -2.
 (8–11 Noise)
----------------------------------------------------------------------------------------
 Alert 3:         Thunderous "Doom, doom"      Full garrison mobilization; Revelation Episode! 
 Drums in Deep    drums shake the foundations; Black Uruk shock-troops      Boss/Ambush triggered. 
 (12+ Noise)      toxic fumes vented in ducts. seal the exit shafts.       6-Round Seal Countdown!
========================================================================================
```

---

#### Alert 0: Quiet Shadows (0–3 Noise Points)
* **Atmosphere**: The vast halls are wrapped in suffocating, tomb-like stillness. Faint drafts whistle through ancient ventilation flues, and slow water droplets chime like glass against distant flags.
* **Enemy Posture**: Orc sentry posts are relaxed. Goblins are asleep in hide tents, squabbling over bone dice, or gnawing cave-bat wings. Sentries suffer **-1d** to Awareness tests.
* **Tactical Benefits**:
  * All **STEALTH** and **EXPLORE rolls** made by Player-Heroes or the Band gain **+1d**.
  * The Company automatically gains a **Surprise Round** on any combat engagement initiated from stealth.
  * Heroes can make **SCAN rolls** without risk of alerting guards.

#### Alert 1: Unease & Scent (4–7 Noise Points)
* **Atmosphere**: Rhythmic, unsettling tapping sounds echo through stone walls (*tom-tap, tap-tom*). The acrid smell of burnt animal grease and guttering tallow torches drifts down from upper balconies.
* **Enemy Posture**: Orc lookouts realize something is amiss. Sentry watches are doubled, and two-man patrols of **Udûn Sniffers** accompanied by screeching cave bats are dispatched to investigate unusual drafts.
* **Tactical Impact**:
  * Standard dice pools apply (no bonus dice for stealth).
  * Whenever the Company spends more than 10 minutes in an unfortified location, the GM rolls a Feat Die: on the **Eye of Sauron ($\mathbf{S}$)**, a roaming Udûn Sniffer patrol enters the chamber.
  * Attempting to rest outside of a fortified redoubt restores only half normal Endurance.

#### Alert 2: Hunted & Barricaded (8–11 Noise Points)
* **Atmosphere**: Bellowing iron horn blasts echo between pillars. Choking sulfur smoke billows from brazier vents, and shadows dance wildly across the high vaulted roofs.
* **Enemy Posture**: The Orcs recognize a disciplined Dwarven infiltration. Major corridors and archways are barred with heavy cedar balks and iron chains. Murder-holes are manned by archers with poisoned arrows. **Grimnar the Disgraced** actively stalks the party, preparing a coordinated ambush.
* **Tactical Penalties**:
  * Awareness tests made to detect concealed ambushes lose **-1d**.
  * Forcing closed stone doors requires an **ATHLETICS roll (Ill-favoured or at -1d)** or generating **+2 Noise Points** with crowbars.
  * Strategic Eye Awareness Hunt Threshold is temporarily reduced by **2 points** (e.g. from 14 to 12).

#### Alert 3: Drums in the Deep (12+ Noise Points)
* **Atmosphere**: A deep, rolling rumble—*"Doom, doom, roll-and-go"*—shakes the bedrock of the mountain as the massive war-drums of Malech's Fortress begin their terrible cadence.
* **Enemy Posture**: Total garrison mobilization. Heavy Black Uruk shock-troops, armored Orc guards, and cave-trolls pour into the thoroughfares. Orc engineers begin winching down iron portcullises and dumping loose slag down the ascent shafts.
* **The Revelation Episode**: Triggers an immediate **Moria Revelation Episode** (see Section 2.2).
* **The Escape Countdown**: The GM initiates a strict **6-Round / 6-Turn Evacuation Timer**. If the Company does not reach and secure Keyed Location 2 (The Upper Gatehouse) before the countdown expires, the main transverse avenue (Westward Drift) back to Thrym's Safe Haven is collapsed or sealed with iron portcullises, forcing a desperate detour through the lethal lower goblin pits!

---

## 2. Sound & Action Economy Table

In the acoustics of Khazad-dûm, stone acts as an amplifier. Noise Points accumulate across delve actions, directly advancing the Alert Tracker and adding to the Company's Strategic Eye Awareness.

```
========================================================================================
                             SOUND & ACTION ECONOMY TABLE
========================================================================================
 DELVE ACTION PERFORMED                            NOISE PTS   ALERT TRACKER IMPACT
----------------------------------------------------------------------------------------
 Silent stealth movement / shadow crawl            +0 Noise    None
 Whisper communication / muffled lockpicking       +0 Noise    None
 Spoken conversation / opening stone chests        +1 Noise    Advances Alert by 1/4 Step
 Melee combat round (muffled weapons, 1-rd kill)  +1 Noise    Advances Alert by 1/4 Step
 Loud combat round (shouting, clashing iron, bow)  +2 Noise    Advances Alert by 1/2 Tier
 Extended combat engagement (4+ combat rounds)     +3 Noise    +1 Full Tier, +1 Eye Awareness
 Sledgehammering doors / Toppling stone idol       +3 Noise    +1 Full Tier, +1 Eye Awareness
 Firing Siege Ballista / Triggering Grond-ram      +4 Noise    +1 Full Tier, +1 Eye Awareness
 Sounding the Battle-horn of the Realm             +5 Noise    INSTANT ALERT 3! (+2 Eye)
 Claiming Durin's Axe from Royal Dais              Special     +4 STRATEGIC EYE AWARENESS!
========================================================================================
```

---

### 2.1 Strategic Eye Awareness & The Hunt Threshold
In addition to the immediate local Alert Tracker, actions within the Third Deep interact with the overarching **Strategic Eye Awareness** rules from *The One Ring 2e* (*Moria Supplement pp. 38–43*).

```
========================================================================================
                            STRATEGIC EYE AWARENESS TRACK
========================================================================================
 REGION CLASSIFICATION:       Dark Land (Default Base Hunt Threshold: 14)
 STARTING EYE AWARENESS:      0 Points (Post-Fellowship Phase clean baseline)
 HUNT THRESHOLD:              14 Points (Reduced to 12 at Alert Tier 2)
 REVELATION TRIGGER:          Triggers immediately when Eye Awareness >= Hunt Threshold!
========================================================================================
```

* **Gaining Eye Awareness**:
  * Loud actions generating 3+ Noise Points: **+1 Eye Awareness**.
  * Sounding the *Battle-horn of the Realm*: **+2 Eye Awareness**.
  * Claiming the royal artifact *Durin's Axe*: **+4 Eye Awareness**.
  * Orc Drummers using *Drums in the Deep* Fell Ability: **+3 Eye Awareness**.
  * Allowing enemy messengers or lookouts to escape:

```
========================================================================================
                            ENEMY DISCOVERY & ESCAPE MATRIX
========================================================================================
 ESCAPE CIRCUMSTANCE                               EYE AWARENESS GAIN
----------------------------------------------------------------------------------------
 Lone surviving Orc / Goblin flees combat           +1 Eye Awareness
 Organized scout or messenger slips into vents      +2 Eye Awareness
 Messenger reaches an active warband / garrison     +3 Eye Awareness
========================================================================================
```

---

### 2.1 Operational Tests: Degrees of Success (6 icons)
When Player-Heroes or the Band make operational checks (Stealth, Scan, Explore, Craft):
* **6 (One 6 icon)**: Action completed silently without raising the Alert Tracker (+0 Noise Points) or grants a minor tactical advantage.
* **66 (Two 6 icons)**: Flawless execution; generates 0 Noise Points and grants +1d to the lead hero's next test in the room.
* **Gandalf (G)**: Critical ancestral breakthrough; uncovers a hidden dwarven stash or bypasses a hazard completely without rolling.

---

### 2.2 Revelation Episodes in the Third Deep
When Strategic Eye Awareness reaches or exceeds the **Hunt Threshold (14)**, a **Revelation Episode** occurs immediately. The GM rolls a Feat Die on the table below:

```
========================================================================================
                        THIRD DEEP REVELATION EPISODE TABLE
========================================================================================
 FEAT DIE ROLL   EPISODE TYPE          TACTICAL CRISIS & ENEMY DEPLOYMENT
----------------------------------------------------------------------------------------
 1–3             Orc Assault           A reinforced warband of 8 Moria Orc Guards and 
                                       4 Udûn Sniffers charges the party's position.
 4–6             Grimnar's Ambush      Grimnar the Disgraced and 4 elite stalkers strike 
                                       from overhead catwalks with poisoned javelins.
 7–9             Terrors of the Dark   A Nameless Thing (The Wailing Horror) or Ash-wraith 
                                       crawls from a deep fissure; all roll Dread tests.
 10              The Shadow Looms      The air turns scalding hot; Durin's Bane stirs in 
                                       the abyss; all heroes gain 3 Shadow (Sorcery).
 Eye (S)         Ghâsh!                Durin's Bane unleashes a burst of demonic fire; 
                                       chambers fill with smoke; immediate flee required!
 Gandalf (G)     Dwarven Echoes        A secret stone shutter opens, providing an ancient 
                                       escape flue; Eye Awareness resets with NO ambush!
========================================================================================
```

* **Resetting Eye Awareness**: After the Revelation Episode is resolved (or escaped), Strategic Eye Awareness **resets to 0**.

---

## 3. Environmental Hazards of the Third Deep

The physical environment of the Third Deep is as lethal as its Orcish inhabitants. Centuries of neglect, volcanic venting, and demonic corruption have left three major environmental perils.

```
                  ┌──────────────────────────────────────────────┐
                  │      ENVIRONMENTAL HAZARDS OF THIRD DEEP     │
                  └──────────────────────┬───────────────────────┘
                                         │
         ┌───────────────────────────────┼───────────────────────────────┐
         ▼                               ▼                               ▼
 [BALROG NEUROTOXIC MIASMA]     [STRUCTURAL COLLAPSE]         [TAINTED WATER PERILS]
  • Preserved toxic breath       • Cracked lintels & vaults    • Untested springs & pits
  • Poison/Dread effects         • 30 Dmg keystone traps       • 1d12 Water Peril roll
  • Masterwork respirators       • Clearing rubble via War     • Sorcery/Poison effects
```

---

### 3.1 The Balrog Neurotoxic Miasma (*Breath of the Pit* / Poison of the Armouries)
* **Origin & Lore**: Preserved within the depressed vaults of **Location 7 (The Poisoned Halls)** and **Location 8 (The Upper Armoury)** is the lingering volcanic breath unleashed by Durin's Bane during the slaughter of the ancient Dwarven captains. It hangs as an oily, emerald-yellow vapor rising to chest height.

```
========================================================================================
                               TOXIC MIASMA DEGRADATION MATRIX
========================================================================================
 PROTECTION STATUS             EXPOSURE TESTING RATE        CONSEQUENCE ON FAILURE
----------------------------------------------------------------------------------------
 Unprotected                   PROTECTION test              Lose 4 Endurance and gain 1 
 (Raw breathing, open skin)    (Ill-favoured)               Shadow Point (Dread). On Eye (S): 
                               EVERY MINUTE                 Severe Poison (lose 8 End, Weary).
----------------------------------------------------------------------------------------
 Protected                     PROTECTION test              Lose 2 Endurance (Weary). 
 (Vinegar cloth & herbs)       (Standard roll)              On Eye (S): Suffer Severe Poison 
                               EVERY HOUR                   (lose 6 Endurance).
----------------------------------------------------------------------------------------
 Masterwork Respirator         COMPLETE IMMUNITY            No tests required for 4 hours.
 (Crafted dwarf-mask filter)   FOR 4 HOURS
========================================================================================
```

* **Countermeasures & Engineering Remedies**:
  1. **Crafting Masterwork Respirators**: Skill Endeavour (**Resistance 3**). Heroes make **CRAFT rolls** (invoking Traits like *Smith* or *Burglary* for **+1d**), or the Band tests **EXPERTISE** (2d vs Band TN 15). Success crafts squad filter masks utilizing oiled leather, charcoal granules, crushed sponge, and dwarf-goggles, granting **4 hours of complete immunity** for up to 10 characters.
  2. **Field Herbal Treatments**: A hero makes a **HEALING roll** or **CRAFT roll** (+1d if using dried herbs or vinegar). Soaking cloth in strong vinegar, chewing dried *Athelas* or mountain herbs, and sealing collars with grease downgrades the hazard to **Protected status** (1 check per hour).
  3. **First Aid Triage**: Treating the poison on an afflicted character requires a **HEALING roll** (Ill-favoured if severe) or Band **EXPERTISE** (2d vs Band TN 15).
  4. **Unjamming the Flue**: In Location 7, unjamming the ancient overhead iron damper lever requires a **CRAFT roll** or **ATHLETICS roll (Ill-favoured)** due to corroded iron. Success vents the entire hall in 3 rounds, but the shrieking iron generates **+3 Noise Points**.

---

### 3.2 Structural Collapse & Falling Masonry
Thousands of years of subterranean tremors and the colossal weight of Mount Silvertine have weakened the granite ribs of the Third Deep.

```
========================================================================================
                                STRUCTURAL COLLAPSE RULES
========================================================================================
 • TRIGGER CONDITIONS: Firing siege ballistas, triggering the Grond-ram, toppling the 
   Morgoth idol, or pulling the Upper Gatehouse keystone winch.
 • IMPACT ZONE: 30-foot radius area of effect.
 • DAMAGE & PROTECTION: All targets in the zone must make a PROTECTION test (or ATHLETICS roll):
   - On a Failure: Target suffers 20 Damage and is PINNED under fallen stone (Weary until freed).
   - On a Success: Target suffers 10 Damage and dives clear to the perimeter.
 • CLEARING RUBBLE: Pinned characters require an ATHLETICS roll or a Band WAR (3d vs Band TN 15) 
   test to extract before suffocating.
========================================================================================
```

---

### 3.3 Subterranean Water Perils Table
Untested water sources in the deeps are frequently befouled by mine runoff, Orc filth, or lingering demonic sorcery. Whenever a character drinks from an untested pool or cistern in the Third Deep, roll the **Feat Die**:

```
========================================================================================
                            SUBTERRANEAN WATER PERIL TABLE
========================================================================================
 FEAT DIE ROLL   WATER CONDITION & EFFECTS
----------------------------------------------------------------------------------------
 Gandalf (G)     Pristine Ancient Dwarven Spring: Pure, chilled mineral water. Restores 
                 2 points of Hope or clears 1 tier of Fatigue immediately!
 9–10            Icy Snowmelt: Freezing cold runoff from Silvertine; refreshing and safe.
 7–8             Orc-Filth: Befouled with offal and rancid grease. Moderate Poison 
                 (Endurance loss 4, cured by Brief Rest).
 5–6             Bitter Mineral Water: Heavy with alkali. Must pass a PROTECTION test 
                 or ENHEARTEN roll to force swallow; failure causes violent nausea 
                 (-1d on all rolls for 1 hour).
 3–4             Acidic Mine Runoff: Tainted with nitric acid and heavy metals. Severe 
                 Poison (8 Endurance loss and Weary condition; requires First Aid to purge).
 1–2             Malice of Durin's Bane: Tainted by demonic residue. The imbiber suffers 
                 2 Shadow Points (Sorcery) and experiences terrifying hallucinations.
 Eye (S)         The Lurker's Pool: The water is clean, but the pool is inhabited by a 
                 stone-crawler or guarded by a concealed Udûn sentry ambush!
========================================================================================
```
