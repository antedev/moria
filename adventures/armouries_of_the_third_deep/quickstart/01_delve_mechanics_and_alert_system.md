# Delve Mechanics, Squad Operations & The Alert Tracker
## Operational Systems for High-Stakes Underground Infiltration

---

> *"There are older and fouler things than Orcs in the deep places of the world... Walk softly, keep your shields muffled, and let no iron strike stone."*

---

## 1. The 4-Stage Alert Tracker

To prevent arbitrary instant party wipes while maintaining terrifying subterranean tension, the Armouries delve uses a dedicated **4-Stage Alert Tracker**. 

The Alert Level measures local Orc responsiveness and readiness within the Third Deep. It advances through noise, lingering in rooms, allowing sentries to flee, or triggering environmental collapses.

```
+-----------------------------------------------------------------------------+
|                            THE 4-STAGE ALERT LADDER                         |
+-----------------------------------------------------------------------------+
|                                                                             |
|  [ ALERT 0: SILENT SHADOWS ] (0–3 Alert Points)                             |
|  • Orc patrols follow routine routes; drowsy, careless sentries.            |
|  • Stealth tests are resolved against Hero Wits TN (Torvir 15, Einar 15, Khoril 16). |
|  • Surprise round automatically granted on ambushing sentries.              |
|                                                                             |
|                                     │                                       |
|                                     ▼                                       |
|  [ ALERT 1: UNEASE & SNIFFERS ] (4–7 Alert Points)                          |
|  • Torches lit; Udûn sniffers & cave bats released into corridors.          |
|  • Stealth rolls become Ill-favoured (roll 2 Feat dice, keep worst).        |
|  • Wandering patrols double-check suspicious sounds.                        |
|                                                                             |
|                                     │                                       |
|                                     ▼                                       |
|  [ ALERT 2: HUNTED & BARRICADED ] (8–11 Alert Points)                       |
|  • Choke points fortified with barricades; sentry squads doubled.           |
|  • Grimnar actively stalks the expedition from behind.                      |
|  • Fleeing sentries raise Alert to Level 3 in 2 rounds unless slain.        |
|                                                                             |
|                                     │                                       |
|                                     ▼                                       |
|  [ ALERT 3: DRUMS IN THE DEEP ] (12+ Alert Points)                          |
|  • Iron drums sound throughout the Deeps; general alarm.                    |
|  • Heavy Orc shock-troops dispatched from Malech's Fortress.                |
|  • The Company has 10 Combat Rounds / 2 Turns to evacuate or be swarmed.    |
|                                                                             |
+-----------------------------------------------------------------------------+
```

---

## 2. Noise Economy & Alert Triggers

Every action that creates sound or leaves evidence generates **Alert Points (AP)**:

| Action / Event | Alert Points (AP) | Eye Awareness | Notes |
| :--- | :---: | :---: | :--- |
| **Unmuffled Band March (Per Level/Area)** | +1 AP | +0 | Occurs if Band Manoeuvre test fails. |
| **Melee Combat Round (Silenced/Contained)** | +0 AP | +0 | Melee combat contained within a sealed room. |
| **Melee Combat Round (Echoing Hall)** | +1 AP / round | +0 | Mustering-Yard, Broken Hall, or Second Armoury. |
| **Blowing Khoril's Battle Horn** | +3 AP | +1 | Grants immediate +1d to all companions in combat. |
| **Orc Sentry Escapes or Screams Alarm** | +3 AP | +1 | Prevented if slain in Round 1 or surprised. |
| **Smashing Iron Doors / Stonework (Axes/Rams)** | +2 AP | +0 | Using brute force instead of lock-picking. |
| **The Mauler Roars / Catapult Fired** | +3 AP | +1 | Massive subterranean rumble. |
| **Slag-Worm / Ceiling Collapse** | +2 AP | +0 | Loud echoing cave-in. |
| **Claiming Durin's Axe from the Vault** | +0 AP | **+4** | Mystic pulse through the roots of the mountain. |

### 2.1 De-escalating Alert Points
Alert points can be reduced during the delve through smart tactical play:
* **Silent Sentry Elimination**: Killing a sentry squad in 1 round without noise reduces current room suspicion: **-1 AP**.
* **Clever Diversion**: Creating a collapsed tunnel, rigging a siege engine counterweight, or igniting a grease fire in an opposite wing: **-2 AP** (diverts patrols away for 1 hour).
* **Bribing Grik the Goblin**: Handing over looted Orc silver (or a shiny trinket) to Grik to misdirect patrols: **-2 AP**.
* **Fortifying the Upper Gatehouse**: Leaving 2 Dwarf companions to secure the door prevents rear patrols from surprising the party: **-1 AP per Act**.

---

## 3. Squad Operations & Dwarf Band Rules

Operating with **6 to 8 veteran Dwarf companions** gives the Company immense combat stopping power and salvage capacity, but requires discipline to avoid making noise.

```
                          SQUAD TACTICAL FORMATIONS
                          
  [1. POINT RECON]        [2. SHIELD-WALL PHALANX]    [3. REARGUARD EXTRACTION]
  
     (Einar)                     (Torvir)                    (Dúrmer & Dolg)
        │                           │                               │
  (Bláin Scout)             (Dúrmer & Dolg)                  (Salvage Squad)
        │                           │                               │
  [Main Company]            (Einar & Khoril)                (Torvir & Khoril)
        │                           │                               │
  (Khoril Guide)             (Bláin & Bróga)                     (Einar)
```

### 3.1 Squad Marching Discipline (Noise Prevention)
When moving the entire company and band between major halls or across hostile sectors:
* **March Test**: Khoril rolls **TRAVEL** (Heart TN 16) or **ENHEARTEN** (Heart TN 16), invoking his *Leadership* Trait for **+1d**, OR the GM rolls Band **MANOEUVRE** (2d6) against **Band TN 15** ($20 - \text{Readiness } 5$).
  * **Success ($\ge 1$ Icon)**: The squad moves silently, stepping in the shadows of the pillars (**+0 Alert / Noise Points** added).
  * **Success Icons ($\mathbf{6}$)**: Each $\mathbf{6}$ rolled reduces ambient suspicion by **-1 Noise Point** (stepping in rhythm to muffle gear), or grants **+1d** to the Point Scout's next check.
  * **Failure**: Clanking mail or loose gravel echoes down the galleries (**+1 Alert Point**).
  * **Gandalf Rune ($\mathbf{G}$)**: The squad finds a hidden maintenance crawlway, completely bypassing the next encounter zone.
  * **Eye of Sauron ($\mathbf{S}$)**: A shield slips or an iron pry-bar clatters on stone (**+2 Alert Points**) and immediately triggers a wandering scout patrol.

### 3.2 Deploying Dwarf Companions (Band Tasks)
During each Act, the heroes may assign their 6–8 companions to specific **Squad Tasks**:

1. **Gatehouse Garrison (2 Dwarves — e.g. Dúrmer & Bróga)**:
   * Hold the Upper Gatehouse as a secure extraction redoubt.
   * *Benefit*: Guarantees a safe retreat route and grants **+1d** to the Company's final escape and withdrawal tests.
2. **Salvage & Porter Squad (2 Dwarves — e.g. Fáin & Austri)**:
   * Tasked with carrying heavy crowbars, iron spikes, and hauling recovered gromril-mail/weapons.
   * *Benefit*: Allows the party to loot up to **40 suits of ancient mail and wargear** without penalizing hero Fatigue/Load.
3. **Flanking Crossbow Screen (2 Dwarves — e.g. Bláin & Hjoldring)**:
   * Stationed along high balconies or behind pillars in combat.
   * *Benefit*: Provides ranged suppressing fire, stripping 1 Hate per round from enemy leaders.
4. **Shield-Wall Vanguard (Attached to Torvir)**:
   * Companions lock shields alongside Torvir in Forward or Defensive Stance.
   * *Benefit*: Absorbs 1 Piercing Blow per battle on behalf of a hero (companion suffers Moderate Injury instead).

### 3.3 Band Casualties & Hope Tracking
* **Band Hope (Starts at 12)**: If Band Hope reaches 0, companion Dwarves become *Demoralized* (-1d to all Band actions; cannot perform sacrifice saves).
* **Band Injury**: If a companion is reduced to 0 Endurance or takes a severe blow, mark a **Moderate Injury** (can be stabilized post-battle with **HEALING** [Heart TN: Torvir 18, Einar 17, Khoril 16] or Band **EXPERTISE** [2d vs Band TN 15]).

---

## 4. Subterranean Environmental Hazards

```
===============================================================================
                     HAZARD 1: THE BREATH OF THE PIT
===============================================================================
  [Origin]: Balrog Neurotoxic Miasma lingering in the Twelfth & Fourteenth Halls
  [Visual]: Heavy, oily ochre vapour pooling along the flagstones; smells of 
            brimstone, copper, and dead stars.
  
  [EXPOSURE WITHOUT PROTECTION]
  • Each hero must make a Protection test (Armour dice + Feat Die) against 
    their Strength TN (Torvir 13, Einar 14, Khoril 13) EVERY 1 MINUTE (Ill-favoured).
  • Failure: Suffer 4 Endurance loss & gain 1 Shadow (Dread). If Endurance hits 0,
    the hero collapses unconscious into fatal stasis. On Eye of Sauron (S): Suffer
    Severe Poison (collapse and dying in 1 hour without First Aid).

  [EXPOSURE WITH FIELD PRECAUTIONS]
  • Precautions: Linen masks soaked in Dwarf Liquor / Healing herbs (Athelas / 
    Cave-moss), skin wrapped tightly in leather grease.
  • Test Protection against Strength TN only once per 1 HOUR (Standard roll).
  • Failure: Suffer 2 Endurance loss (Weary). On Eye of Sauron (S): Suffer Severe Poison.

  [MASTERWORK RESPIRATOR IMMUNITY]
  • Crafted dwarf-mask filter (Skill Endeavour: Resistance 3 using CRAFT [Strength TN] 
    or Band EXPERTISE [2d vs Band TN 15]).
  • Provides 4 HOURS OF COMPLETE IMMUNITY for up to 10 characters (no rolls required).
  
  [THE DWARF REMEDY]
  • A hero can brew a neutralizing salve using Balin's medical supplies (Skill 
    Endeavour: Resistance 4, using CRAFT [Strength TN] or HEALING [Heart TN]). 
    Success makes 4 Dwarves immune to the fumes for 2 hours.
===============================================================================
```

### Hazard 2: Congealed Slag-Worms
* **Description**: Huge sinuous masses of molten iron and slag that dripped from the foundries when the Balrog destroyed the upper smelters. They hang suspended over doorways and arches like sleeping dragons of black glass.
* **Trigger**: Any explosive noise (Khoril's horn, troll impacts) or vigorous hammering causes a slag-worm to fracture.
* **Mechanics**: Everyone in the zone must test **ATHLETICS** (Strength TN: Torvir 13, Einar 14, Khoril 13) or roll a **Protection test** (4d vs Strength TN).
  * *Failure*: Crushed by falling iron slag (Suffer 8 Damage, Injury rating 16, and become Pinned/Weary).
  * *Orc Lore*: Orcs believe slag-worms are cursed; dropping a slag-worm onto an Orc patrol automatically routs them in terror (**Strike Panic**).

### Hazard 3: Structural Adamant Collapses
* **Description**: Damaged archways where Dwarven keystones have slipped under seismic tremors.
* **Mechanics**: Einar's *The Broken Key* allows him to detect unstable spans on a **SCAN** test (Wits TN 15, Favoured). If triggered, Hjoldring (Stonemason companion) can brace the ceiling with iron wedges in 1 round using **CRAFT** (Strength TN) or Band **WAR** (3d vs Band TN 15).

---
*Proceed to `02_keyed_locations.md` for full descriptions, sensory boxed text, and room mechanics.*
