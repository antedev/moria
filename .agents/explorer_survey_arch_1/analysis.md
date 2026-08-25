# Module Architecture & Location Design Survey
**Adventure Module**: *The Armouries of the Third Deep*  
**System**: *The One Ring 2nd Edition* (TOR 2e) – *Moria: Through the Doors of Durin*  
**Target Path**: `c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep`  
**Author**: Explorer Subagent (`explorer_survey_arch_1`)  
**Date**: 2026-08-24 / 2989 TA  

---

## 1. Executive Summary & Design Philosophy

The *Armouries of the Third Deep* is a high-tension, squad-level dungeon delve designed for 2–3 tabletop sessions. It bridges the tactical skirmish rules of *The One Ring 2e* with deep subterranean expedition management.

### Key Design Pillars
1. **Squad-Level Operations with Band Mechanics**: The three Player-heroes (**Torvir Hammerstone**, **Einar son of Anar**, **Khoril Hornblower**) command a disciplined squad of 6–8 veteran Dwarf Companions (*Bláin, Fáin, Dúrmer, Hjoldring, Bróga, Austri, Dolg*). The adventure provides explicit tactical roles for the Band (Rearguard, Forward Screen, Porter Salvage Squad, Shield-wall Phalanx).
2. **Tactical Infiltration & Dynamic Alert Economy**: Rather than arbitrary monster closets, the complex is governed by a 4-Stage Alert Tracker (0: Quiet Shadows, 1: Unease & Scent, 2: Hunted & Barricaded, 3: Drums in the Deep) driven by a transparent Sound Economy. Players can fight contained skirmishes without automatically triggering overwhelming TPK hordes.
3. **Sensory-Rich, Interactive 10-Room Dungeon**: Every room provides boxed read-aloud descriptions, structured GM sensory bullets (Lighting, Drafts, Echoes, Smells), interactable environmental mechanisms, TOR 2e skill checks with defined TNs, and squad tactical options.
4. **Compelling 3-Act Pacing**: From the vertical infiltration (Act I), through toxic hazards and desecrated halls (Act II), to the climactic vault heist, troll duel, and frantic fighting withdrawal (Act III).
5. **High Table Facilitation**: Complete facilitator suite including a 1-Page Rapid GM Cheat Sheet, Band Worksheet, ASCII Node Maps, and a Session-by-Session Playbook.

---

## 2. Comprehensive Survey of the 10 Keyed Locations

```
========================================================================================
                                 ELEVATION PROFILE & NODE MAP
========================================================================================
 [Descent Shaft from Thistlebeard's Caves]
                    │
                    ▼
           ┌─────────────────┐
           │ 1. MUSTERING    │◄───────────────────────────────┐
           │    YARD         │                                │
           └────────┬────────┘                                │
                    │                                         │
                    ▼                                         │
           ┌─────────────────┐                                │
           │ 2. UPPER        │ (Fortified Fallback Redoubt)   │
           │    GATEHOUSE    │                                │
           └────────┬────────┘                                │
                    │                                         │
                    ▼                                         │
           ┌─────────────────┐                                │
           │ 3. FIRST        │                                │
           │    ARMOURY      │                                │
           └────────┬────────┘                                │
                    │                                         │
                    ▼                                         │
           ┌─────────────────┐                                │
           │ 4. BROKEN HALL  │ (Morgoth/Balrog Idol & Lore)   │
           └────────┬────────┘                                │
                    │                                         │
                    ▼                                         │
           ┌─────────────────┐                                │
           │ 5. SECOND       │ (Siege Engines / Grond-ram)    │
           │    ARMOURY      │                                │
           └────────┬────────┘                                │
                    │                                         │
         ┌──────────┴──────────┐                              │
         │                     │                              │
         ▼                     ▼                              │
┌─────────────────┐   ┌─────────────────┐                     │
│ 7. POISONED     │   │ 6. HALL OF THE  │                     │
│    HALLS        │   │    MAULER       │                     │
│ (Toxic Miasma & │   │ (Armored Troll) │                     │
│  Scribe Letter) │   └────────┬────────┘                     │
└────────┬────────┘            │                              │
         │                     │                              │
         ▼                     ▼                              │
┌─────────────────┐   ┌─────────────────┐                     │
│ 8. UPPER        │   │ 9. KING'S DOOR  │                     │
│    ARMOURY      │   │ (Runic Portal)  │                     │
│ (Salvage Cache) │   └────────┬────────┘                     │
└─────────────────┘            │                              │
                               ▼                              │
                      ┌─────────────────┐                     │
                      │ 10. LOWER       │ (Durin's Axe &      │
                      │     ARMOURY     │  Greater Hoard)     │
                      └────────┬────────┘                     │
                               │                              │
                               └────── [FIGHTING WITHDRAWAL] ─┘
========================================================================================
```

---

### Location 1: The Mustering-Yard
* **Role**: Infiltration Landing & Crossroads  
* **Elevation**: Upper Tier (Level 3A)  
* **Connections**: North to Descent Shaft (Thistlebeard connection); South to Location 2 (Upper Gatehouse); East to collapsed gallery.

#### Boxed Read-Aloud Text
> *You emerge onto a high stone overlook gazing across a cavernous subterranean yard carved from the living basalt of the mountain. Vast octagonal pillars, thick as ancient oaks and scored with blackened scorch-marks from the fire of Durin’s Bane, march into the suffocating gloom. Below lies a stone pavilion where ancient Dwarf-captains once marshaled thousands. Now, broken spears and rusted iron shards lie scattered across cracked flagstones, and a chill, sulfurous draft whispers through the dark.*

#### GM Sensory Bullets
* **Lighting**: Pitch darkness; faint green bio-luminescent lichen clings to high arches. Lantern light reveals vast shadows stretching between columns.
* **Drafts**: A cold, steady upward draft pulls from the lower vents, bearing the faint, acrid tang of sulfur and ancient soot.
* **Echoes**: Massive reverberation; an unshielded cough or clanking mail-shirt carries 100 paces. Water droplets tap rhythmically against distant flags.
* **Smells**: Old soot, damp stone, rancid animal grease, and the faint, biting ozone of burnt rock.

#### Interactables & Environmental Features
* **Scorched Pavilion**: Blackened stone dais with shattered command tables; grants elevated cover (+1 Parry) in tactical skirmishes.
* **Flanking Pillar Galleries**: Raised side-ledges (10 ft above yard floor) offering high ground for archery and stealth flanking.
* **Udûn Sentry Post**: A crude hide tent nestled behind pillar #4 where 2 Udûn Sniffers keep loose watch.

#### TOR 2e Skill Checks
* **Scan (TN 14)**: Spot the Udûn sentry post and memorize patrol timing without being seen (*Einar gains +2 / Advantage from The Broken Key*).
* **Stealth (TN 14 / Band Manoeuvre)**: Lead the expedition across the open flags to the Upper Gatehouse without alerting the sentries.
* **Battle / Lore (TN 14)**: Identify the ancient defensive kill-zones and read the Balrog scorches (confirms passage of Durin's Bane a thousand years ago).

#### Tactical Options & Band Roles
* **Forward Scout Screen**: Deploy Einar and 2 scouts (*Bróga, Austri*) along the high gallery to silently eliminate or bypass the Udûn sentries.
* **Stealth March**: Khoril leads the Band in single-file felt-wrapped marching order (*Band Manoeuvre roll* vs Alert Tracker).

---

### Location 2: The Upper Gatehouse
* **Role**: Fortified Forward Rally Point & Retreat Choke Point  
* **Elevation**: Upper Tier (Level 3A)  
* **Connections**: North to Location 1 (Mustering-Yard); South to Location 3 (First Armoury); East to collapsed murder-hole corridor.

#### Boxed Read-Aloud Text
> *Before you stands the inner gatehouse of the Upper Armouries. Massive adamant-reinforced blast-doors lie buckled outward, warped by ancient explosive heat and siege rams. Broken iron chains and counterweights hang limply from ceiling winches. Narrow murder-holes pierce the thick stone battlements above, looking out over the approach. The masonry is battered but unyielding—a natural fortress in the throat of the deep.*

#### GM Sensory Bullets
* **Lighting**: Heavy shadow; narrow ceiling embrasures let in no light, but block line-of-sight from the yard.
* **Drafts**: Violent whistling draft funnels through the crushed portal, moaning like a horn.
* **Echoes**: The structure muffles sounds from within, deadening speech to a dull mutter.
* **Smells**: Pulverized stone dust, dry iron rust, and dried bat droppings.

#### Interactables & Environmental Features
* **Buckled Adamant Blast-Doors**: Can be reinforced using timber and iron wedges to create an impenetrable defensive redoubt.
* **Ceiling Winch & Keystone**: A cracked stone keystone above the archway can be rigged with a trip-rope to trigger a controlled cave-in on pursuers.
* **Arrow Slits & Murder Holes**: Provide total cover (+3 Parry, immune to missile fire from outside) for defenders.

#### TOR 2e Skill Checks
* **Craft (TN 14)**: Fortify the gatehouse using scrap beams and iron spikes, establishing a secure Safe Rally Point (reduces retreat difficulty by 2).
* **Craft (TN 16) / Battle (TN 14)**: Rig the keystone collapse trap (inflicts 30 damage / instantly crushes vanguard when triggered during withdrawal).
* **Explore (TN 14)**: Identify a hidden crawl-vent leading into Location 3 that bypasses the main corridor.

#### Tactical Options & Band Roles
* **Rearguard Redoubt (Crucial Decision)**: Leave 2–3 veteran Dwarf Companions (*e.g., Bláin, Austri, Dolg*) to hold the Gatehouse. This guarantees a safe withdrawal route, prevents rear ambushes, and grants +2 Band Readiness during the final escape.

---

### Location 3: The First Armoury
* **Role**: Despoiled Outpost & Trap Hazard  
* **Elevation**: Middle Tier (Level 3B)  
* **Connections**: North to Location 2 (Upper Gatehouse); South to Location 4 (Broken Hall); West to maintenance tunnel.

#### Boxed Read-Aloud Text
> *Long rows of stone weapon racks stand stripped and desolate, their ancient bronze fittings torn away. Orcish debris covers the floor: piles of broken shields, gnawed bones, and crude iron caltrops. Across the far threshold, thin black cords stretch between iron stanchions, rigged to counterweighted scrap-blades smeared with a foul, glistening tar.*

#### GM Sensory Bullets
* **Lighting**: Total darkness; oily sheen of black poison on traps catches lantern light with an iridescent gleam.
* **Drafts**: Stagnant, sluggish air smelling of rot.
* **Echoes**: Every loose pebble or scuffed boot scrapes loudly against the stone.
* **Smells**: Orc filth, rancid tallow, and the nauseating, bitter stench of Orc venom.

#### Interactables & Environmental Features
* **Orcish Scrap-Traps**: Three interlocking tripwires connected to falling scythe-blades coated in black venom (*Injury 16, Poisoned condition*).
* **Poison Vats**: Rusted iron cauldrons containing coagulated Orc blade-venom.
* **Concealed Floor Cache**: A loose flagstone under rack #12 concealing serviceable Dwarven throwing axes and iron spikes.

#### TOR 2e Skill Checks
* **Scan (TN 14)**: Spot the tripwires and hidden pressure plates (*Einar +2 from The Broken Key*).
* **Burglary (TN 14) / Craft (TN 14)**: Disarm the scrap-traps silently (Failure = triggers trap, deals 14 damage and generates +2 Noise).
* **Healing (TN 14) / Lore (TN 14)**: Safely harvest 3 doses of Orc blade-poison (+2 Injury rating to weapon attacks for 1 encounter).

#### Tactical Options & Band Roles
* **Trap Resetting**: The party can re-arm the scythe traps to face backwards toward Location 2, creating an automated obstacle against Orc pursuers.
* **Band Expertise**: Deploy *Fáin* (Dwarf smith) to assist in silent trap disarming without raising Alert.

---

### Location 4: The Broken Hall
* **Role**: Dread Encounter, Lore Clue & Psychological Crucible  
* **Elevation**: Middle Tier (Level 3B)  
* **Connections**: North to Location 3 (First Armoury); South to Location 5 (Second Armoury); East to Old Moria sealed archway.

#### Boxed Read-Aloud Text
> *This grand vaulted hall was once an honour court celebrating the ancient martial victories of Durin’s Folk. Noble bas-reliefs of Dwarven kings in battle have been brutally defaced with crude obsidian chisels and smeared with dried blood. In the centre of the hall looms a grotesque effigy: a towering idol of jagged black iron and charred bones, depicting the flaming shadow of the Balrog. A palpable aura of malice radiates from the dark idol, chilling the heart and whispering despair.*

#### GM Sensory Bullets
* **Lighting**: Pitch black; the iron idol seems to swallow light, casting elongated demonic shadows against the defaced murals.
* **Drafts**: A sudden, sickeningly warm downdraft emanates from the idol, carrying the scent of burning blood.
* **Echoes**: Voices sound muffled and hollow, as if the room itself is choking on ancient horror.
* **Smells**: Dried gore, burnt bone, char, and old malice.

#### Interactables & Environmental Features
* **The Balrog/Morgoth Idol**: Central dark totem (12 ft high). Imbued with lingering Shadow; radiates Dread.
* **Defaced Dwarven Frieze**: Detailed carving of the First Age founding of Khazad-dûm. An unbroken cartouche at the lower border contains secret architectural glyphs.
* **Toppling Winch**: Old scaffolding behind the idol can be leveraged to overturn the blasphemous statue.

#### TOR 2e Skill Checks
* **Dread Test (Awe / Courage TN 14)**: Resist the aura of the idol.  
  * *Failure*: Gain 2 Shadow Points (Dread) and become *Daunted* for the next hour.
  * *Torvir (Curse of Vengeance)*: If Torvir fails, his rage boils over—he must strike the idol or an enemy immediately, adding +2 Noise.
  * *Einar (Dragon-sickness)*: Einar notices gold-leaf veins within the idol's base; failing the test tempts him to pry out the gold, risking a trap.
* **Riddle / Old Lore (TN 14)**: Decipher the hidden cartouche on the mural. Reveals that the *King's Door* (Location 9) possesses a dual-locking mechanism requiring the *Marshal's Key* and the *Crown-Invocation*.
* **Song / Enhearten (TN 14)**: Khoril or a companion sings an ancient hymn of Durin to counter the idol's gloom (+1 Band Hope on success).
* **Athletics (TN 14)**: Topple the idol into rubble (generates +2 Noise unless muffled with cloth).

#### Tactical Options & Band Roles
* **Spiritual Cleansing**: Torvir smashes the idol after a successful Enhearten roll, purging the Shadow from the hall and bolstering Band Morale (+1 Hope).

---

### Location 5: The Second Armoury (Heavy Siege Engines)
* **Role**: Tactical Sandbox & Heavy Artillery  
* **Elevation**: Middle Tier (Level 3B)  
* **Connections**: North to Location 4 (Broken Hall); South to Location 6 (Hall of the Mauler); West to Location 7 (Poisoned Halls).

#### Boxed Read-Aloud Text
> *You enter a vast hangar smelling of dry cedar, iron grease, and ancient pine pitch. Massive timber frames rise into the shadows: Dwarven siege engines of colossal scale. An iron-headed battering ram—the legendary Grond-ram of the Third Deep—rests upon greased bronze tracks facing the southern archway. Nearby, heavy torsion ballistas and counterweighted catapults stand ready, their coiled sinew springs miraculously preserved in airtight oiled skins.*

#### GM Sensory Bullets
* **Lighting**: Deep gloom; timber frames create a maze of shadows and catwalks.
* **Drafts**: A gentle, dry draft filters through the ceiling vents, rustling dried canvas coverings.
* **Echoes**: Low acoustic resonance; the heavy timbers absorb footsteps.
* **Smells**: Cedarwood, linseed oil, ancient grease, and cured leather.

#### Interactables & Environmental Features
* **The Grond-Ram**: Massive iron-shod ram on iron wheels and bronze guide tracks. Can be released down the ramp to smash the iron gates of Location 6 or crush an entire Orc squad.
* **Dwarven Torsion Ballista**: Heavy twin-limb engine loaded with a 6-foot steel-tipped harpoon bolt.
* **Counterweight Crane**: Can hoist 2-ton stone counterweights or drop them as an area-of-effect crushing hazard.
* **Barricade Timbers**: Stacked cedar balks ready to be assembled into rapid defensive chokepoints.

#### TOR 2e Skill Checks
* **Craft (TN 14)**: Inspect and prime the Grond-ram or torsion ballista. Ensures flawless operation when triggered.
* **Athletics (TN 14) / Band War (TN 15)**: Manhandle the ram into firing position or construct an impassable timber barricade in 10 minutes.
* **Battle (TN 14)**: Establish an interlocking kill-zone utilizing the siege weapons against incoming reinforcements.

#### Tactical Options & Band Roles
* **Breaching the Mauler's Lair**: Firing the ballista through the doors into Location 6 can automatically strip *The Mauler's* scrap armor or deal 25 damage before melee begins!
* **Barricade Holding**: Deploy 2 Dwarf Companions with heavy shields behind a newly built cedar barricade to lock down the eastern approach.

---

### Location 6: The Hall of the Mauler
* **Role**: Apex Boss Arena & Tactical Environment  
* **Elevation**: Lower Tier (Level 3C)  
* **Connections**: North to Location 5 (Second Armoury); South to Location 9 (King's Door); East to collapsed ore chutes.

#### Boxed Read-Aloud Text
> *A colossal vaulted chamber opens before you, its ceiling lost in darkness forty feet above. Iron catwalks crisscross the upper vault, dangling from rusted chains. The floor is a graveyard of crushed wargear and shattered masonry. In the centre, sleeping upon a mountain of scrap metal and gnawed bones, lies a monstrous Great Cave-troll. Scavenged dwarven breastplates, iron boiler plates, and jagged shield-rims have been crudely wired into its thick hide, turning the brute into an armored juggernaut.*

#### GM Sensory Bullets
* **Lighting**: Dim twilight cast by faint luminescent moss on high stalactites.
* **Drafts**: Heavy, rhythmic gusts of hot, foul breath like the pulsing exhaust of a smelting furnace.
* **Echoes**: The troll’s guttural snores shake the floor stones; loose pebbles vibrate in rhythm.
* **Smells**: Ammoniac troll musk, rotting meat, scorched iron, and stale blood.

#### Interactables & Environmental Features
* **High Catwalks (15–20 ft up)**: Narrow iron walkways offering total elevation advantage against the troll. Reachable via chain ladders.
* **Hanging Stalactites**: Fractured limestone spikes above the troll's nest; can be shot or levered down.
* **Scrap-Armor Plating**: The Mauler has 6 Armour dice, but individual plates are held by brittle Orc-wire.
* **Weapon Piles**: Piles of heavy dwarf-mattocks and anvils usable as improvised high-impact throwing weapons.

#### TOR 2e Skill Checks
* **Riddle (TN 14)**: Engage the troll in a Riddle duel (Combat Task) exploiting its *Dull-Witted* trait. Success makes The Mauler hesitate, lose its action, or swing wildly at empty air.
* **Athletics (TN 14)**: Scale chain ladders to reach the catwalks or swing across chains to strike from above.
* **Craft / Athletics (TN 14)**: Target a cracked ceiling anchor with an arrow or lever to drop a 2-ton stalactite onto the Mauler (deals 20 damage, ignores armor, Knocks Prone).
* **Hunting / Awareness (TN 14)**: Spot the master wire holding the troll's chest armor (called shot severing the wire reduces its Armour from 6d to 3d).

#### Tactical Options & Band Roles
* **Shield-Wall Phalanx**: Deploy 4 Dwarf Companions in Defensive Stance (*Band War*) at the entrance arch to bottle the troll while Torvir and Einar flank from the catwalks.
* **Stealth Bypass**: Slip the entire expedition along the perimeter catwalks without waking the beast (*Band Manoeuvre TN 15*).

---

### Location 7: The Poisoned Halls (Twelfth & Fourteenth Halls)
* **Role**: Environmental Hazard & Key Investigation  
* **Elevation**: Middle Tier / Depressed Basin (Level 3B-minus)  
* **Connections**: East to Location 5 (Second Armoury); South to Location 8 (Upper Armoury); West to sealed ventilation ducts.

#### Boxed Read-Aloud Text
> *A ghastly emerald-yellow vapor clings to the flagstones of this long, pillared hall, rising to chest height like a creeping swamp. Within the eerie mist stand dozens of Dwarven warriors in full war-gear, frozen in place like stone statues—their flesh calcified and preserved by the ancient volcanic miasma of the Balrog. At the far end, slumped over a stone desk, lies the preserved form of an ancient Dwarf scribe, a lead scroll tube gripped tightly in his petrified fingers.*

#### GM Sensory Bullets
* **Lighting**: Unsettling yellow-green phosphorescence reflecting through thick fog. Visibility limited to 10 paces.
* **Drafts**: Oppressive, dead calm. The air is heavy, oily, and hot.
* **Echoes**: Sound is heavily muffled by the vapor; shouts become dull gasps.
* **Smells**: Pungent bitter almonds, stinging sulfur, metallic copper, and ozone.

#### Interactables & Environmental Features
* **Balrog Toxic Miasma**: Corrosive neurotoxin filling the lower 5 feet of the chamber.
  - *Hazard Rules*: Breathing the fumes requires a **Healing / Endurance TN 14** test every 10 minutes. Failure inflicts 2 Endurance loss and the *Weary* condition.
  - *Remedies*: Soaked vinegar cloths, crushed Athelas/King’s foil, or improvised Dwarf filter masks (Craft TN 14) negate the hazard for 1 hour.
* **Petrified Dwarf Scribe**: Holds the sealed lead tube containing the *Dying Scribe's Letter* (Handout #1).
* **Jammed Ventilation Flue**: Overhead iron damper lever that can vent the gas if unjammed.

#### TOR 2e Skill Checks
* **Scan (TN 14)**: Spot the scribe’s desk and avoid stepping into deep floor fissures (*Einar +2 from The Broken Key*).
* **Craft (TN 14)**: Construct squad respirator masks from leather, charcoal, and vinegar cloths.
* **Craft (TN 16) / Athletics (TN 16)**: Unjam the overhead ventilation flue (vents the miasma in 3 rounds, but the screeching iron generates +3 Noise).
* **Riddle / Old Lore (TN 14)**: Translate the dying scribe's runic letter, revealing the exact history and secret mechanism of the *Marshal's Key*.

#### Tactical Options & Band Roles
* **Rapid Transit Screen**: Khoril leads a sprint through the hall with holding-breath discipline (*Band Manoeuvre TN 15*).

---

### Location 8: The Upper Armoury
* **Role**: Garrison Salvage Cache & Goblin Grave  
* **Elevation**: Middle Tier (Level 3B)  
* **Connections**: North to Location 7 (Poisoned Halls); East to Location 9 (King's Door); South to emergency escape flues.

#### Boxed Read-Aloud Text
> *Sealed from the toxic gas by heavy bronze shutters, this vaulted storehouse remains untouched by the centuries. The desiccated corpses of half a dozen goblin looters lie huddled near the threshold, their skin withered black from attempting to breach the toxic perimeter. Beyond them stand tall iron armoires and sealed stone chests filled with rows of gleaming dwarf-mail, heavy tower-shields, and razor-sharp war-mattocks—enough masterwork wargear to equip an entire company of Balin’s vanguard.*

#### GM Sensory Bullets
* **Lighting**: Dark, but the crisp reflection of polished dwarf-steel gleams brilliantly in torchlight.
* **Drafts**: Completely sealed; cool, sterile, dry air.
* **Echoes**: Clean, sharp acoustics; footsteps ring like chimes on clean stone.
* **Smells**: Machine oil, dry cedar shavings, polished iron, and the dry husk of dead goblins.

#### Interactables & Environmental Features
* **Garrison Salvage Cache**: Contains 40 suits of Dwarf Mail-shirts (Protection 3d), 30 Heavy Tunnel-Shields (+2 Parry), and 50 Masterwork War-Mattocks/Axes (Damage 6, Injury 18).
* **Lead-Sealed Munitions Chest**: Locked iron chest containing 6 flasks of Dwarven Liquid Fire (alchemical incendiary weapons, Damage 8, Piercing Blow on 8+).
* **Goblin Looters' Pouch**: On the chief goblin corpse: 12 silver pennies, a stolen map of the Third Deep, and a bone whistle.

#### TOR 2e Skill Checks
* **Craft (TN 14)**: Safely crack the lead seals on the Munitions Chest without detonating the liquid fire.
* **Burglary (TN 14)**: Pick the masterwork dwarven lock on the officer's locker (*Einar +2 from The Broken Key*).
* **Explore / Battle (TN 14)**: Organize the wargear into 6 balanced transport packs for the Companion Band.

#### Tactical Options & Band Roles
* **Heavy Salvage Porter Squad**: Assign 4 Dwarf Companions (*e.g., Dúrmer, Hjoldring, Fáin, Bláin*) as porters. This secures the wargear for Balin’s garrison (+50 Garrison Supply Points), but temporarily reduces the Band’s combat rating by 1.

---

### Location 9: The King's Door
* **Role**: Runic Gate Puzzle & Ambush Choke Point  
* **Elevation**: Deepest Tier (Level 3C)  
* **Connections**: North to Location 6 (Hall of the Mauler) and Location 8 (Upper Armoury); South to Location 10 (Lower Armoury / Royal Vault).

#### Boxed Read-Aloud Text
> *At the terminus of the grand avenue rises the legendary King’s Door. Crafted from solid star-iron and polished granite, the massive portal bears the inlaid silver Ithildin runes of the Crown and Anvil of Durin. Twin keyholes flank the archway: one set high in the shape of a Marshall’s baton, the other set low in the sign of the King. The runes gleam with a faint, watchful starlight, sensing the presence of Durin’s true heirs.*

#### GM Sensory Bullets
* **Lighting**: Soft silver-blue Ithildin glow pulsing gently from the runes when approached by Dwarves of Durin's Folk.
* **Drafts**: Total stillness; a sacred, cool hush envelops the threshold.
* **Echoes**: The acoustics are deep and harmonic; a whisper resonates like a chord in a cathedral.
* **Smells**: Pure ozone, star-metal, ancient incense, and cold mountain stone.

#### Interactables & Environmental Features
* **The Dual Runic Locks**: Requires either the *Marshal's Key* (held by Grik/Udûn Patrol) OR a masterwork lockpicking endeavour, alongside the spoken invocation of Durin.
* **Ithildin Inscription**: Reads: *"None shall pass into the Vault of Kings save by the Marshal's Word and Durin's Will."*
* **Overhead Defensive Parapet**: Raised balcony where Grimnar the Disgraced and his elite stalkers attempt their sudden ambush while the party is unlocking the gate.

#### TOR 2e Skill Checks
* **Riddle / Old Lore (TN 14)**: Decipher the ceremonial invocation of Durin to activate the keyholes.
* **Burglary (TN 16 / Extended Endeavour, 4 rolls)**: Attempt to pick the adamant master lock without the Marshal's Key (*Einar's specialty; +2 from The Broken Key*).
* **Awareness (TN 14)**: Spot Grimnar and his 4 Udûn Stalkers crouching on the overhead parapet before they launch their surprise volley of poisoned javelins.

#### Tactical Options & Band Roles
* **Perimeter Defense Phalanx**: Khoril deploys the Companion Band in a tight circle around Einar while he works the lock, granting Einar total protection against ranged attacks.
* **Instant Opening**: If the party acquired the *Marshal's Key* from Grik or the Udûn patrol, the door opens smoothly in 1 round, completely avoiding the lockpicking delay.

---

### Location 10: The Lower Armoury (The Royal Vault)
* **Role**: Legendary Treasure Vault, Artifact Chamber & Final Objective  
* **Elevation**: Deepest Sanctuary (Level 3C)  
* **Connections**: North to Location 9 (King's Door).

#### Boxed Read-Aloud Text
> *The King’s Door glides open on silent, greased pivots, revealing the inner sanctum of Khazad-dûm’s royal wargear. The air here is pure and untouched by the corruption of Orcs or the breath of shadow. Gold and mithril filigree dance across soaring vaulted ribs. Resting upon a central dais of black marble, bathed in an eternal column of pale light, lies Durin’s Axe—its rune-scored steel pulsing with ancient power. Around it rest suits of gromril-mail and weapons of the First Age, untouched since the fall of the mountain realm.*

#### GM Sensory Bullets
* **Lighting**: Radiant gold and silver luminescence reflecting from mirror-polished mithril and marble.
* **Drafts**: Crisp, sweet, sacred air; smells like mountain snow and cedar incense.
* **Echoes**: Every footstep lands with profound, solemn gravity.
* **Smells**: Pure cedar, gold dust, ancient resin, and clean mountain wind.

#### Interactables & Environmental Features
* **The Dais of Durin**: Black marble pedestal supporting *Durin’s Axe*.
  - *Claiming Durin's Axe*: Inflicts a surge of spiritual presence—instantly adds **+4 to Strategic Eye Awareness** and alerts every Orc chieftain in the Third Deep!
* **Royal Relic Coffers**: Three engraved stone chests containing:
  - *Shield of the Deep Gate* (Wondrous Item: +3 Parry, immune to Piercing Blows on rolling an 11 or 12).
  - *Mattock of Moria-Silver* (Fell Weapon: Damage 7, Injury 20, Keen).
  - *Mail of Unyielding Stone* (Enchanted Armour: Protection 5d, Load 12, Weary resistance).
* **Vault Blast Barricade**: The inner vault doors can be bolted from within, allowing a brief 30-minute Short Rest / Rally before the fighting withdrawal.

#### TOR 2e Skill Checks
* **Awe / Song (TN 14)**: Gaze upon the sacred relic without being overwhelmed by reverent awe.
* **Greed / Shadow Test (TN 14)**: Resist the overwhelming allure of the treasure.  
  * *Einar (Dragon-sickness)*: Must test against Dragon-sickness. Failure inflicts 2 Shadow Points and an obsession with securing every piece of gold.
* **Craft / Lore (TN 14)**: Safely remove *Durin’s Axe* from its runic stasis field without triggering an alarm bell.

#### Tactical Options & Band Roles
* **Secure & Pack**: Assign Khoril to lead the ceremonial extraction while the Band packs the legendary relics into armored panniers.
* **Short Rest & Fortify**: Seal the vault door for 30 minutes to spend Fellowship Points, restore Hope, and assign fighting withdrawal stances.

---

## 3. 3-Act Narrative Architecture & Session Pacing

```
========================================================================================
                          3-ACT NARRATIVE & PACING FLOW
========================================================================================

  ACT I: THE DESCENT & MUSTERING-YARD (Session 1: ~3.5 Hours)
  ┌──────────────────────────────────────────────────────────────────────────────────┐
  │ • Staging from Thistlebeard's Safe Haven (Travel TN 14 down climbing shafts)     │
  │ • Infiltration of Location 1 (Mustering-Yard): Stealth vs Udûn sentries           │
  │ • Securing Location 2 (Upper Gatehouse): Fortifying Forward Redoubt & Rearguard  │
  │ • Scouting Location 3 (First Armoury): Trap disarming & Black Venom discovery    │
  │ • CLIFFHANGER: Shadowy contact with Grik / Whispers of Grimnar in the deeps     │
  └────────────────────────────────────────┬─────────────────────────────────────────┘
                                           │
                                           ▼
  ACT II: THE DESPOILED HALLS & TOXIC HAZARD (Session 2: ~3.5 Hours)
  ┌──────────────────────────────────────────────────────────────────────────────────┐
  │ • Location 4 (Broken Hall): Morgoth Idol Dread test & Ancient Inscription        │
  │ • Location 5 (Second Armoury): Siege engine tactical sandbox & Grond-ram prep    │
  │ • Location 7 (Poisoned Halls): Balrog Miasma hazard, Scribe's Letter clue        │
  │ • Location 8 (Upper Armoury): Garrison wargear salvage & Porter assignment       │
  │ • Corridors: Acquiring the Marshal's Key (Bargain with Grik vs Ambush Patrol)    │
  │ • CLIFFHANGER: Standing at the doors of Location 6 with troll snores shaking floor│
  └────────────────────────────────────────┬─────────────────────────────────────────┘
                                           │
                                           ▼
  ACT III: THE MAULER, THE VAULT & WITHDRAWAL (Session 3: ~3.5 Hours)
  ┌──────────────────────────────────────────────────────────────────────────────────┐
  │ • Location 6 (Hall of the Mauler): Boss battle / Riddle duel / Catwalk tactics    │
  │ • Location 9 (King's Door): Runic unlocking under pressure; Grimnar's Ambush     │
  │ • Location 10 (Royal Vault): Claiming Durin's Axe (+4 Eye Awareness trigger!)    │
  │ • THE FIGHTING WITHDRAWAL: Escaping across Locations 6->5->4->2->1               │
  │   - Band holds choke points, keystone collapse triggered at Upper Gatehouse      │
  │ • EPILOGUE: Return to Lord Balin & Fróra with arms for 50 Dwarves & Royal Relic  │
  └──────────────────────────────────────────────────────────────────────────────────┘
========================================================================================
```

### Pacing Curves & Escalation Triggers

| Pacing Dial | Low Tension / Stealth | Rising Tension / Skirmish | Climax / Crisis |
| :--- | :--- | :--- | :--- |
| **Alert Tier** | Alert 0 (Quiet Shadows) | Alert 1–2 (Unease / Hunted) | Alert 3 (Drums in the Deep) |
| **Noise Index** | 0–3 Noise Points | 4–11 Noise Points | 12+ Noise Points |
| **Adversary Behavior** | Routine patrols, snoozing sniffers | Double sentries, barricaded doors, Grimnar stalking | Full garrison mobilization, war drums, tunnel cutoff |
| **Band Deployment** | Forward Screen & Stealth March | Tactical Phalanx & Choke Guards | Porter Escort & Desperate Rearguard |
| **GM Intervention** | Describe eerie lore, drafts, whispers | Drop hints of clanking armor, bat swarms | Impose round-by-round escape countdown timers |

---

## 4. Infiltration, Alert System & Sound Economy

### 4-Stage Alert Tracker Subsystem

```
========================================================================================
                                4-STAGE ALERT TRACKER
========================================================================================
 [ALERT 0: QUIET SHADOWS] ──► [ALERT 1: UNEASE & SCENT] ──► [ALERT 2: HUNTED & BARRICADED] ──► [ALERT 3: DRUMS IN THE DEEP]
   Noise: 0–3 Points            Noise: 4–7 Points              Noise: 8–11 Points               Noise: 12+ Points
   • Routine patrols            • Udûn sniffers active         • Choke points fortified        • Full garrison assault
   • Surprise rounds allowed    • +1 to enemy Awareness        • Grimnar stalks expedition     • Tunnel collapse countdown
========================================================================================
```

### Sound Action Economy Table

| Action Taken by Expedition | Noise Points | Impact on Alert Tracker |
| :--- | :---: | :--- |
| Stealth movement / silent exploration | +0 | None |
| Whisper communication / picking locks quietly | +0 | None |
| Standard spoken discussion / looting chests | +1 | 1/4 of an Alert step |
| Melee combat round (muffled weapons, fast kill) | +1 | 1/4 of an Alert step |
| Loud combat round (shouting, clashing iron, spells) | +2 | Advances Alert Tracker by 1/2 Tier |
| Sledgehammering doors / Toppling stone idol | +3 | Advances Alert Tracker by 1 Full Tier |
| Firing Siege Ballista / Triggering Grond-ram | +4 | Advances Alert Tracker by 1 Full Tier |
| Khoril blowing the Battle-Horn of the Realm | +5 | **Instantly advances Alert Tracker to Alert 3!** |
| Claiming *Durin's Axe* from Royal Pedestal | Special | **+4 Strategic Eye Awareness** & alerts all deeps |

---

## 5. Band Integration & Squad Operations

### Companion Band Roster & State

* **Band Readiness**: 5 (TN 15 for Band Tests)
* **Band Dispositions**: War 3, Vigilance 2, Manoeuvre 2, Expertise 2, Rally 1
* **Band Hope**: 12 | **Shadow**: 1 | **Fellowship Pool**: 4 Points
* **Squad Members**:
  1. **Bláin**: Veteran tunnel-fighter (10/18 End, Moderate Injury: 1/1) – *Ideal for Rearguard*
  2. **Fáin**: Smith & engineer (15/18 End) – *Ideal for Siege Weapons & Trap Disarming*
  3. **Dúrmer**: Stalwart heavy warrior (22/22 End) – *Phalanx Anchor*
  4. **Hjoldring**: Heavy shield-bearer (18/18 End) – *Phalanx Defender*
  5. **Bróga**: Quick-footed scout (12/12 End) – *Forward Screen*
  6. **Austri**: Crossbow marksman (10/18 End) – *Overwatch Guard*
  7. **Dolg**: Stout porter (18/18 End) – *Salvage Logistics Lead*

### Squad Tactical Deployments

```
========================================================================================
                               BAND TACTICAL DEPLOYMENTS
========================================================================================
 1. FORWARD SCOUT SCREEN (2 Dwarves):
    • Rolls Band Vigilance (2d) to detect ambushes before Player-heroes enter.
    • Allows Einar to make Scan rolls with +2 bonus without risk of surprise.

 2. REARGUARD CHOKE DEFENSE (2–3 Dwarves stationed at Location 2 Gatehouse):
    • Prevents enemy flanking attacks from behind.
    • Guarantees an open extraction route during Act III Fighting Withdrawal.

 3. HEAVY SALVAGE PORTER SQUAD (4 Dwarves):
    • Dedicated to hauling 40+ suits of Dwarf-mail from Location 8 Upper Armoury.
    • Secures +50 Garrison Supply Points for Balin upon successful return.

 4. SHIELD-WALL PHALANX (4 Dwarves in Defensive Stance):
    • Forms a protective bastion around the heroes; intercepts 1 attack per round.
    • Rolls Band War (3d) to execute coordinated shield-thrusts.
========================================================================================
```

---

## 6. GM Facilitator Tool Suite Specifications

### Tool 1: Rapid GM Cheat Sheet (1-Page Dashboard)
* **Purpose**: Instant at-the-table lookup for DCs, adversary stats, noise points, and room sensory cues.
* **Contents**:
  - Summary matrix of all 10 rooms (Room #, Illumination, Primary Obstacle, Key TNs, Alert Noise Rating, Key Loot).
  - Quick-stat box for *The Mauler*, *Grimnar*, *Grik*, and *Udûn Patrols*.
  - Toxic Gas hazard flow chart & remedy rules.
  - Alert Tracker gauge.

### Tool 2: Band Management Worksheet
* **Purpose**: Fillable/trackable sheet for companion HP, injuries, readiness, and active tactical stances.
* **Contents**:
  - Readiness tracking box with situational modifiers (+1 for Hardened leader, -1 for overburdened).
  - 7-Companion roster table with check-boxes for Endurance, Wounds, and Stances.
  - Band Disposition roll guide (War, Vigilance, Manoeuvre, Expertise, Rally).
  - Fatigue and Band Hope track.

### Tool 3: ASCII / Markdown Node Maps & Elevation Diagrams
* **Purpose**: High-clarity spatial navigation tool showing elevations, connections, secret passages, and choke points.
* **Contents**:
  - Master 3-Tier Elevation Diagram (Level 3A, 3B, 3C).
  - High-Contrast Connection Node Graph with door types and trap markers.
  - Tactical Room Floorplans for Location 2 (Gatehouse Redoubt), Location 5 (Siege Workshop), Location 6 (Mauler's Lair), and Location 9/10 (Royal Vault).

### Tool 4: Session-by-Session GM Playbook
* **Purpose**: Step-by-step facilitator notes guiding the GM through pacing, dialogue hooks, roleplay prompts, and emergency adjustments.
* **Contents**:
  - Session 1, Session 2, and Session 3 detailed running checklists.
  - Character-specific spotlights: Torvir's Vengeance triggers, Einar's Greed & Broken Key opportunities, Khoril's Captain choices.
  - "Pacing Rescue Dials": What to do if players are moving too fast (trigger Udûn sniffer ambush) or too slow (Grik offers a shortcut in exchange for silver).

---

## 7. Proposed File & Directory Layout

To ensure modularity, pristine organization, and adherence to project conventions, the adventure module will be structured in `c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep` as follows:

```
c:/Users/ante/Documents/Moria/adventures/armouries_of_the_third_deep/
├── README.md                          # Adventure Overview, Synopsis, Master File Index
├── 01_campaign_context.md             # Campaign Staging, Hero Profiles, Band Rules & Roster
├── 02_operational_mechanics.md        # Alert Tracker (0-3), Sound Economy, Toxic Hazard, Stealth
├── 03_act_I_descent_mustering.md      # Act I Narrative & Locations 1-3 (Mustering-Yard, Gatehouse, First Armoury)
├── 04_act_II_despoiled_halls.md       # Act II Narrative & Locations 4, 5, 7, 8 (Broken Hall, Second Armoury, Poisoned Halls, Upper Armoury)
├── 05_act_III_royal_vault_escape.md   # Act III Narrative & Locations 6, 9, 10 (Hall of Mauler, King's Door, Lower Armoury) + Fighting Withdrawal
├── 06_adversaries_and_hazards.md      # Full TOR 2e Stat Blocks (The Mauler, Grimnar, Grik, Udûn Patrols, Hazards)
├── 07_relics_loot_tables.md           # Durin's Axe, Tunnel-Guard Wargear, Marshal's Key, D66 Scavenge Table
├── 08_gm_playbook_and_pacing.md       # Session-by-Session GM Running Guide, Pacing Dials, Triggers
└── handouts/
    ├── gm_cheat_sheet.md              # 1-Page Condensed GM Reference Dashboard
    ├── band_worksheet.md              # Companion Tracking Sheet & Stance Card
    ├── node_map.md                    # ASCII / Markdown Maps, Elevation Cross-Sections & Tactical Flowcharts
    └── dying_scribe_letter.md         # In-world Prop / Player Handout (Ancient Khuzdul Letter)
```

---

## 8. Interface Contracts & Cross-Module Dependencies

| File | Depends On | Provides To |
| :--- | :--- | :--- |
| `01_campaign_context.md` | `campaign_log.md`, `session_prep_armouries.md` | Hero stats, Band baseline for Acts I–III |
| `02_operational_mechanics.md` | TOR 2e Core Rules, Moria Supplement | Alert Tracker & Noise values for Acts I–III |
| `03_act_I_descent_mustering.md` | `01_campaign_context.md`, `02_operational_mechanics.md` | Locations 1–3, Session 1 content |
| `04_act_II_despoiled_halls.md` | `02_operational_mechanics.md`, `06_adversaries_and_hazards.md` | Locations 4, 5, 7, 8, Session 2 content |
| `05_act_III_royal_vault_escape.md` | `06_adversaries_and_hazards.md`, `07_relics_loot_tables.md` | Locations 6, 9, 10, Boss fight & Escape |
| `06_adversaries_and_hazards.md` | TOR 2e Adversary Rules | Stat blocks for Acts I, II, III |
| `07_relics_loot_tables.md` | TOR 2e Relic Rules | Magic items, D66 Scavenge table |
| `08_gm_playbook_and_pacing.md` | All Act files | Master running guide for GM |
| `handouts/*` | Module text | At-the-table playable assets |

---

## 9. Conclusion & Survey Recommendations

1. **Location Design Completeness**: All 10 locations have distinct mechanical roles, avoiding any redundant "empty corridors." Every room combines narrative flavour, interactive tactical elements, and clear skill tests.
2. **Band Rule Cohesion**: Integrating the 6–8 Dwarf Companions elevates the adventure from standard dungeoneering into a true expeditionary military operation.
3. **Pristine Modularity**: The proposed 8-chapter + handouts directory structure provides seamless navigation for GMs and clean implementation boundaries for builder subagents.
