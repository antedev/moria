# Chapter 5: Adversaries, Foes & Subterranean Hazards

> *"There are older and fouler things than Orcs in the deep places of the world... but even the common vermin of the Deeps fight with the desperate fury of cornered beasts when the shadows lengthen."*  
> — *Ancient Lore of the Longbeards*

---

## 1. Subterranean Combat & Adversary System

In *The One Ring 2nd Edition* (*Moria: Through the Doors of Durin*), combat within the claustrophobic vaults of Khazad-dûm is rapid, brutal, and lethal. Adversaries do not track the three Player-Hero attributes (Strength, Heart, Wits); instead, each foe is defined by a single unified **Attribute Level**, fueling their combat target numbers, damage output, defensive thresholds, and fell powers.

```
========================================================================================
                          TOR 2e ADVERSARY STATISTICAL SCHEMA
========================================================================================
 ATTRIBUTE LEVEL (AL) : Core rating (1–12+). Sets default TNs and Heavy Blow bonuses.
 ENDURANCE (End)      : Physical stamina and structural hit points.
 MIGHT (M)            : Actions/attacks per round (1, 2, or 3) & Wounds required to kill.
 HATE / RESOLVE       : Fuel rating for bonus dice (+1d) and Fell Ability activation.
 PARRY                : Modifier added to the Player-Hero's Strength TN (+0 to +3, or —).
 ARMOUR               : Protection test dice rolled when struck by a Piercing Blow (1d–5d).
 PROFICIENCIES        : Attack Name, Rank (dice rolled), Damage, Injury, Special Damage.
 FELL ABILITIES       : Innate monstrous traits, tactical reactions, and aura effects.
========================================================================================
```

---

### 1.1 Core Adversary Combat Rules

* **Target Numbers for Attacks**:
  * **Player-Hero attacking an Adversary**: The hero rolls against $\mathbf{\text{Strength TN} + \text{Adversary Parry modifier}}$.
  * **Adversary attacking a Player-Hero**: The adversary rolls **1 Feat Die + Success Dice equal to Combat Proficiency** against $\mathbf{\text{Hero's Target TN} + \text{Hero Shield/Parry modifier}}$.
* **The Feat Die for Servants of Shadow**:
  * The **Eye of Sauron ($\mathbf{S}$)** represents the ultimate result: it counts as **10** (and triggers a Piercing Blow).
  * The **Gandalf Rune ($\mathbf{G}$)** counts as **0** (a total miss/fumble for dark creatures).
* **Piercing Blows**:
  * An adversary scores a Piercing Blow whenever the Feat Die shows a **10** or the **Eye of Sauron ($\mathbf{S}$)**.
  * The struck Player-Hero must immediately make a **Protection Test** (rolling their Armour dice + Helm) against the weapon's **Injury rating**. On a failure, the hero suffers a **Wound**.
* **Hate & Resolve Expenditure**:
  * Minions of the Shadow burn **Hate**; non-corrupted beings utilize **Resolve**.
  * An adversary may spend **1 point of Hate** to add **+1d** to an attack roll, **+1d** to a Protection test, or to trigger an active **Fell Ability**.
  * The maximum Hate spent in a single combat round cannot exceed the adversary's **Might rating**.
  * When an adversary is reduced to **0 Hate**, it becomes **Weary** and cannot spend Hate until rested.
* **Special Damage Triggers**: Each Success icon ($\mathbf{6}$) scored on an adversary's successful attack roll can trigger one Special Damage option:
  * **Heavy Blow**: The adversary expends 1 Success icon to inflict additional Endurance loss equal to its **Attribute Level ($+L$)**.
  * **Break Shield**: Smashes the target's non-magical shield, destroying it permanently (hero loses shield Parry bonus).
  * **Pierce**: Adds **+2** to the Feat Die result for the purpose of beating the hero's Injury TN.
  * **Seize**: The hero is pinned into **Forward Stance**, unable to change stances and restricted to Brawling attacks until spending a Success icon ($\mathbf{6}$) on an attack roll to break free.
  * **Fiery Blow**: Inflicts immediate **Severe or Grievous fire damage** (burning gear, igniting cloaks, and rupturing respirators).

---

### 1.2 Morale, Rout & Break Points

Orcs and goblins are cowardly by nature, driven only by fear of their chieftains and hatred of the Free Peoples. A skirmish rarely fights to the last minion.

```
========================================================================================
                                 MORALE BREAK POINT MATRIX
========================================================================================
 TRIGGER EVENT                    MORALE CHECK REQUIRED           ROUT CONSEQUENCE
----------------------------------------------------------------------------------------
 Chieftain / Champion Slain       Roll Valour vs TN 14            Warband breaks immediately; 
 (e.g. Grimnar or Black Uruk)     (Ill-favoured for Goblins)      minions flee into side vents.
----------------------------------------------------------------------------------------
 Casualties Exceed 50%            Roll Valour vs TN 12            Surviving Orcs enter Craven 
 (Half of warband defeated)       (Craven foes check instantly)   state; withdraw to barricades.
----------------------------------------------------------------------------------------
 The Mauler Defeated / Pacified   No roll needed                  All accompanying goblins scatter 
 (Troll collapses or befriends)   Automatic Goblin Panic          screaming in blind terror.
----------------------------------------------------------------------------------------
 Powerful Light / Flame Unleashed Roll Valour vs TN 15            Orcs suffer -1d to all attacks 
 (Durin's Axe Flame of Hope)      (Hate Sunlight applies)         and attempt to flee darkward.
========================================================================================
```

---

## 2. Apex Adversary: The Mauler (Armoured Great Cave-Troll)

> *"A mountain of scarred grey flesh encased in twisted plates of scavenged iron, rusted boiler plates, and crushed Dwarven shields. When it swings its tree-trunk maul, the stone arches tremble."*

```
========================================================================================
                     THE MAULER (ARMOUR-CLAD GREAT CAVE-TROLL)
========================================================================================
 "Driven mad by the memory of steel biting flesh, the beast has forged itself into an iron tomb."
 Culture: Great Cave-troll of Moria | Distinctive Features: Brutish, Lumbering, Terrified of Pain
----------------------------------------------------------------------------------------
 ATTRIBUTE LEVEL: 10
 ENDURANCE:       80 (Weary at 0 Hate)
 MIGHT:           2 (Takes 2 Wounds to kill; 2 attacks per combat round)
 HATE:            10
 PARRY:           5 (— / Unarmoured baseline 0; +5 from massive scrap plating and bulk)
 ARMOUR:          5d (Twisted scrap-iron, boiler shields, anvil fragments)
----------------------------------------------------------------------------------------
 COMBAT PROFICIENCIES:
 • Heavy Club / Maul:  3d  (Damage 8, Injury 14 / 16, Break Shield, Heavy Blow)
 • Seize / Slam:       3d  (Damage 4 / 6, Injury 12, Seize)
 • Scrap Shrapnel:     2d  (Damage 6, Injury 12, Ranged missile, Area burst)
----------------------------------------------------------------------------------------
 FELL ABILITIES:
 • Dull-Witted: Heroes in Forward Stance may engage in a Riddle duel as their main combat 
   action. On a success, the Mauler becomes confused/panicked and loses 1 Hate (+1 Hate 
   per Success icon). 3 cumulative successes pacify or bypass the beast.
 • Hideous Toughness: Unarmed blows cannot harm the troll. When an attack reduces the 
   Mauler to 0 Endurance, it causes a Piercing Blow instead. If it survives the Protection 
   roll, its Endurance immediately resets to 40 (half maximum).
 • Strike Fear: Spend 1 Hate at combat start. All heroes within sight must pass a Valour 
   test (TN 14) or suffer 2 Shadow (Dread) and become Daunted (cannot spend Hope).
 • Thick Hide: Spend 1 Hate on a Protection roll to gain +2d Armour dice (rolling 7d total).
 • Scavenged Iron Carapace: If a Piercing Blow fails to wound, the attacker's weapon 
   becomes lodged in the plating unless the hero passes a Craft or Athletics test (TN 14). 
   A direct hit from a siege engine strips this plating, reducing Armour from 5d to 3d.
========================================================================================
```

```
                        [THE MAULER'S LAIR: COMBAT TOPOLOGY]
                                (Location 6 Drill Hall)

               ┌────────────────── [HIGH CATWALKS] ──────────────────┐
               │  (15–20 ft elevation; +1d ranged; sweepable by maul)│
               └───────────┬─────────────────────────────┬───────────┘
                           │                             │
                           ▼                             ▼
                  [FALLING STALACTITES]         [WEAPON SCRAP HEAPS]
                  (Lever down: 20 Dmg)          (Hurled for 6 Dmg AoE)
                           │                             │
                           └──────────────┬──────────────┘
                                          ▼
                               [THE MAULER'S ARENA]
                                • 80 Endurance (Might 2)
                                • Scrap-Iron Plating (5d)
                                • Riddle Duel Choke Point
```

---

### 2.1 The Riddle Duel Combat Task

The Mauler is not merely a brute; it is a creature broken by cognitive trauma from the Battle of Azanulbizar. Driven by an overwhelming terror of physical pain, the troll's primitive mind struggles between ferocious rage and paralyzing fear.

```
========================================================================================
                          THE MAULER RIDDLE DUEL MECHANICS
========================================================================================
 • STANCE REQUIREMENT : The negotiating hero (Torvir, Einar, or Khoril) must stand in 
                        FORWARD STANCE, facing the troll within arm's reach.
 • ACTION COST        : Executing the Riddle duel consumes the hero's main combat action.
 • TARGET NUMBER      : Standard Riddle test against TN 14 (or Wits TN 15).
 • RESOLUTION TRACK   : 3 Successes required before 3 Failures.
----------------------------------------------------------------------------------------
 SUCCESSES / OUTCOMES :
 • 1st Success : The Mauler halts its swing mid-air, blinking in confusion. It loses 
                 1 Hate (+1 additional Hate per Success icon rolled).
 • 2nd Success : The troll drops its club to clasp its iron-plated ears, weeping in 
                 frustration. It loses 2 Hate and forfeits its next attack round.
 • 3rd Success : Complete cognitive breakdown! The troll cowers against the north wall, 
                 whimpering and covering its head. It is PACIFIED and will not attack 
                 unless struck with weapons.
----------------------------------------------------------------------------------------
 FAILURES / RETALIATION :
 • 1st Failure : The Mauler roars in anger; gains +1d on its next Maul attack.
 • 2nd Failure : The troll sweeps its club across the floor, generating +2 Noise Points.
 • 3rd Failure : The duel collapses! The Mauler enters a blind berserk frenzy, attacking 
                 with +2 Damage on all strikes for the remainder of the encounter.
========================================================================================
```

---

### 2.2 Dynamic Arena Tactics (Location 6)

The Hall of the Mauler is an interactive combat playground featuring three major tactical mechanics:

1. **Catwalk Sweeping (15–20 ft Elevation)**:
   * Heroes scaling the ancient iron inspection ladders can reach the perimeter catwalks, gaining **+1d on ranged attacks** and immunity to ground-level slam attacks.
   * *The Mauler's Reaction*: The troll can use one attack action to sweep its 12-foot tree-trunk club through the iron catwalk struts. All characters on that section must make an **Athletics (TN 14)** test:
     * *Success*: The hero leaps to an adjacent pillar or ceiling chain, holding fast.
     * *Failure*: The catwalk buckles! The character falls 20 feet to the stone flags below, suffering **10 Falling Damage** and landing Prone.
2. **Stalactite Dropping (20 Direct Damage)**:
   * Colossal mineral stalactites hang from the cracked ceiling vaults directly above the troll's scrap-nest.
   * A hero on the high catwalks can use their action to lever loose a cracked stalactite with a crowbar, spear, or war-mattock (**Athletics TN 14** or **Craft TN 14**).
   * *Impact*: The falling stone spear crashes into the Mauler, inflicting **20 Direct Damage** (bypassing Armour) and knocking the beast Prone.
3. **Weapon Pile Hurling (Improvised Area Missiles)**:
   * The Mauler frequently digs both hands into heaps of rusted broadswords, iron wedges, and bucklers, hurling a wave of shrapnel at heroes in Open or Rearward stance.
   * *Resolution*: Ranged attack roll (2d) against all heroes in the target arc. Targets hit suffer **6 Damage (Injury 12)** and must pass a **Protection test** or become Weary from shrapnel lacerations.
4. **Siege Engine Integration (Stripping the Carapace)**:
   * If the party managed to aim and prime the heavy Dwarven Torsion Ballista from **Location 5 (The Second Armoury)** into Location 6, firing the harpoon bolt deals **25 Direct Damage** and **permanently strips the troll's scrap-iron plating**, reducing its Armour rating from **5d to 3d**.

---

## 3. Archfoe: Grimnar the Disgraced (Great Orc Bodyguard)

> *"A towering, whipcord-muscled Great Orc chieftain whose leather harness is adorned with blackened Dwarven beards. He twitches with manic speed, brandishing a notched heavy scimitar in one claw and a gleaming, stolen Dwarven dirk in the other."*

```
========================================================================================
                     GRIMNAR THE DISGRACED (GREAT ORC STALKER)
========================================================================================
 "Humiliated at Durin's Bridge, he will buy his redemption with the blood of the Longbeards."
 Culture: Great Orc of the Misty Mountains | Distinctive Features: Fierce, Vengeful, Cunning
----------------------------------------------------------------------------------------
 ATTRIBUTE LEVEL: 6
 ENDURANCE:       32 (Weary at 0 Hate)
 MIGHT:           1 (or Might 2 in Apex Ambush; 2 attacks per round when dual-wielding)
 HATE:            6 (or 7 in full vengeance mode)
 PARRY:           6 (+3 Base + 3 from dual-wielding stolen Dwarven dagger and speed)
 ARMOUR:          3d (Scavenged heavy dwarf-mail reinforced with boiled leather)
----------------------------------------------------------------------------------------
 COMBAT PROFICIENCIES:
 • Heavy Scimitar:         3d  (Damage 5, Injury 16 / 18, Break Shield, Pierce)
 • Stolen Dwarven Dagger:  3d  (Damage 3, Injury 14, Keen [Pierce on 9–10 or S])
 • Broad-headed Spear:     2d  (Damage 5, Injury 16, Pierce, Throwable)
----------------------------------------------------------------------------------------
 FELL ABILITIES:
 • Denizen of the Dark: Attack rolls are Favoured when fighting in subterranean darkness.
 • Fierce Shot: When throwing his broad-headed spear from stealth, gains +1d and +2 Damage.
 • Great Leap: Spend 1 Hate to leap over frontline defenders (bypassing the Shield-Wall) 
   to land directly in front of Rearward heroes or archers.
 • Hate Sunlight: Loses 1 Hate per round if exposed to full direct sunlight.
 • Hatred (Durin's Folk): Attack rolls against Torvir, Khoril, and Dwarf Companions 
   are permanently Favoured.
 • Hideous Toughness: Unarmed attacks cannot harm him. When an attack reduces Grimnar 
   to 0 Endurance, it causes a Piercing Blow; if he survives the Protection roll, his 
   Endurance immediately resets to 16 (half maximum).
 • Snake-like Speed: Spend 1 Hate when targeted by an incoming melee or ranged attack 
   to make the attacker's roll Ill-favoured.
 • Vengeful Strike: If struck in melee by Torvir, Einar, or Khoril, Grimnar may spend 
   1 Hate as an immediate reaction to deliver a free retaliation strike against that hero.
========================================================================================
```

---

### 3.1 Ambush Tactics at Keyed Location 9 (The King's Door)

Grimnar is a cunning hunter who refuses to fight on fair terms. He utilizes the architecture of the Third Deep to stage a multi-phase ambush:

```
========================================================================================
                          GRIMNAR'S AMBUSH DOCTRINE (ROOM 9)
========================================================================================
 PHASE 1: THE CROSSFIRE (Catwalk Overwatch)
 • Position: Grimnar and 2 Udûn Sniffers man the high stone lintels 25 feet above the door.
 • Action: Opens with poisoned broad-headed spear throws targeting Khoril (the horn-bearer) 
   and Einar (the locksmith) to prevent them from opening the adamant portal.

 PHASE 2: THE GREAT LEAP (Bypassing the Phalanx)
 • Trigger: When Torvir or the Shield-Wall advances to engage his front ranks.
 • Action: Grimnar activates Great Leap, bounding over the locked shields to strike at 
   Einar while he works the lock mechanisms with The Broken Key.

 PHASE 3: DUAL-WIELDING FRENZY & RETALIATION
 • Stance: Fights in Forward Stance with Heavy Scimitar and Stolen Dwarven Dagger.
 • Tactic: Uses Snake-like Speed to avoid heavy axe blows while triggering Vengeful Strike 
   whenever struck, turning every clash into a bloodbath.
========================================================================================
```

---

### 3.2 Grudge Narrative Dialogue & Combat Taunts

During combat, Grimnar taunts the Player-Heroes with venomous callbacks to prior campaign milestones:

* **Against Torvir**: *"Where is your forge now, hammer-dwarf? Your brothers screamed as their beards burned at the bridge, and your skin will make fine straps for my scabbard!"*
* **Against Einar**: *"I recognize that broken bit of iron in your hand! Your cousin died clutching it in the slave-pits, and it won't save you from my knife!"*
* **Against Khoril**: *"Blow your brass horn, little herald! Blow it until your lungs burst! Malech's drummers are answering, and your tomb is already sealed!"*
* **On Brandishing the Stolen Dagger**: *"Look at the craft of it! Dwarven steel cuts Dwarven mail sweeter than butter. Shall I carve your name beside your brother's on the hilt?"*

---

### 3.3 Tactical Retreat & Reinforcement Triggers

Grimnar is vengeful but not suicidal. He knows when to break contact:

```
========================================================================================
                           GRIMNAR'S RETREAT PROTOCOL
========================================================================================
 • RETREAT TRIGGER 1 : If Grimnar is reduced to <= 8 Endurance and has 0 Hate remaining.
 • RETREAT TRIGGER 2 : If both accompanying Udûn Sniffers are slain and Torvir lands a 
                       Piercing Blow that penetrates his Armour.
 • ESCAPE ROUTE      : Grimnar hurls a smoke-bomb of crushed brimstone into the doorway 
                       and slips through a narrow drainage flue leading toward Location 1.
 • PURSUIT CHECK     : To prevent his escape, a hero must succeed on an Athletics (TN 16) 
                       or Ranged Attack (TN 16) test before he reaches the flue.
 • ESCAPE CONSEQUENCE: If Grimnar escapes, he immediately sounds the garrison horns, 
                       advancing the Alert Tracker directly to Alert Tier 3!
========================================================================================
```

---

## 4. Goblin Informant: Grik the Skulker (Scout & Spy)

> *"A scrawny, yellow-eyed goblin wrapped in patched badger-skins and greasy leather straps. He clings to the shadow behind the great fluted pillars of the Mustering-Yard, chewing bitter roots and clutching a serrated skinning knife."*

```
========================================================================================
                     GRIK THE SKULKER (GOBLIN SCOUT & INFORMANT)
========================================================================================
 "He hates the great Orcs, fears the fire-devils, and worships bright silver above all."
 Culture: Moria Goblin / Sneak | Distinctive Features: Cunning, Talkative, Cowardly
----------------------------------------------------------------------------------------
 ATTRIBUTE LEVEL: 2 (or AL 3 as an elite tunnel scout)
 ENDURANCE:       8 (or 12 Endurance)
 MIGHT:           1
 HATE:            2 (or 3 Hate)
 PARRY:           4 (+1 Base + 3 from small stature and dodging)
 ARMOUR:          1d (or 2d in patched hides)
----------------------------------------------------------------------------------------
 COMBAT PROFICIENCIES:
 • Jagged Knife:      2d  (Damage 2 / 3, Injury 12 / 14, Pierce on 10)
 • Blown Bone-Darts:  2d  (Damage 2, Injury 10, Poison: Moderate Endurance drain)
----------------------------------------------------------------------------------------
 FELL ABILITIES:
 • Craven: If Grik suffers even 1 point of Endurance loss or witnesses an ally fall, 
   he must pass a Valour test (TN 14) or immediately drop his weapons and flee or surrender.
 • Fierce Shot: Gains +1d on ranged dart attacks launched from complete concealment.
 • Sneak in Shadows: When rolling Stealth to hide in darkness or narrow crawlspaces, 
   all tests are Favoured and generate 0 Noise Points.
========================================================================================
```

---

### 4.1 Social Interaction & Negotiation Table

Grik is an opportunistic survivor serving **Granny Goblin** in the lower settlements. He despises the brutal Udûn Orcs and is willing to sell vital intelligence to the Dwarves—provided they do not kill him first.

```
========================================================================================
                          GRIK THE SKULKER NEGOTIATION MATRIX
========================================================================================
 APPROACH / SKILL TEST         TN     SUCCESS OUTCOME & REVELATION
----------------------------------------------------------------------------------------
 Persuade / Customs            TN 14  Grik agrees to talk; demands a token bribe of 
                                      bright silver, Beorning honey-rations, or tobacco.
----------------------------------------------------------------------------------------
 Enhearten / Intimidate        TN 14  Grik cowers and spills patrol shift times for 
                                      Location 1 and Location 3 without asking for silver.
----------------------------------------------------------------------------------------
 Riddle (Trading Secrets)      TN 14  Grik reveals the secret acoustic blind spots in the 
                                      Mustering-Yard (+1d on all Band Manoeuvre tests).
----------------------------------------------------------------------------------------
 BRIBE DEMAND                 VALUE   INTELLIGENCE DELIVERED
----------------------------------------------------------------------------------------
 5 Silver Pennies / Tobacco     —     The Marshal's Key Lore: Confirms that an Udûn 
                                      patrol in the Second Armoury holds the copper key!
----------------------------------------------------------------------------------------
 10 Silver Pennies / Dwarven   —     Safe Passage: Details the hidden crawl-vent between 
 Liquor Flask                        Location 2 and Location 3, completely bypassing 
                                      the sentry post at the main gate.
----------------------------------------------------------------------------------------
 Promise of Granny's Safety    —     Troll Weakness: Whispers that the big grey brute in 
                                      Location 6 is terrified of riddles and loud bells!
========================================================================================
```

* **Flee / Panic Behavior**:
  * If the party attacks Grik, draws steel aggressively, or allows the **Alert Tracker to reach Tier 2+**, Grik screeches in terror and scrambles up a 6-inch drainage chute, disappearing into the walls.
  * If captured, Grik can be interrogated using **Persuade (TN 14)** or **Awe (TN 14)** to yield the exact layout of Keyed Locations 1, 2, and 5.

---

## 5. Garrison Ranks: Orc Patrols & Sentry Squads

The armed forces of the Third Deep consist of two rival factions forced into uneasy cooperation: the standard **Moria Orcs** (cave scavengers) and the fanatical **Udûn Orcs** (fire-worshippers serving the shadow of Durin's Bane).

```
========================================================================================
                          GARRISON ADVERSARY QUICK MATRIX
========================================================================================
 ADVERSARY TYPE      AL  END  MIGHT HATE PARRY ARMOUR  MAIN ATTACK       DAMAGE / INJURY
----------------------------------------------------------------------------------------
 Orc Soldier         3   12     1     3   +1    2d     Orc-axe 2d        Dmg 3, Inj 18 (Break)
 Orc Guard           4   16     1     4   +2    3d     Heavy Scimitar 3d Dmg 4, Inj 16 (Pierce)
 Udûn Sniffer        4   16     1     4    —    3d     Torch-staff 3d    Dmg 4, Inj 14 (Fiery)
 Moria Orc Drummer   3   12     1     3   +1    2d     Curved Knife 2d   Dmg 3, Inj 14 (Pierce)
 Black Uruk          5   20     1     5   +2    3d     Uruk Sword 3d     Dmg 4, Inj 16 (Pierce)
 Black Uruk Captain  6   24     1     6   +3    4d     Great Scimitar 3d Dmg 5, Inj 16 (Pierce)
========================================================================================
```

---

### 5.1 Detailed Sentry & Patrol Stat Blocks

#### 1. Moria Orc Soldier (Attribute Level 3)
* **Culture**: Moria Goblin / Scout | **Distinctive Features**: Sullen, Sneaking
* **Endurance**: 12 | **Might**: 1 | **Hate**: 3 | **Parry**: +1 | **Armour**: 2d (Crude leather & iron scrap)
* **Combat Proficiencies**:
  * *Orc-axe*: 2d (Damage 3, Injury 18, Break Shield)
  * *Short Bow*: 2d (Damage 3, Injury 14, Pierce)
* **Fell Abilities**:
  * *Denizen of the Dark*: Attack rolls are Favoured in darkness.
  * *Hate Sunlight*: Loses 1 Hate per round in sunlight.
  * *Craven*: Must pass Valour (TN 14) or flee if health drops below half.

#### 2. Moria Orc Guard (Attribute Level 4)
* **Culture**: Moria Orc / Heavy Sentry | **Distinctive Features**: Brutish, Disciplined
* **Endurance**: 16 | **Might**: 1 | **Hate**: 4 | **Parry**: +2 | **Armour**: 3d (Scavenged dwarf-mail)
* **Combat Proficiencies**:
  * *Heavy Scimitar*: 3d (Damage 4, Injury 16, Pierce)
  * *Heavy Spear*: 3d (Damage 4, Injury 14, Pierce)
* **Fell Abilities**:
  * *Denizen of the Dark*: Attack rolls are Favoured in darkness.
  * *Hate Sunlight*: Loses 1 Hate per round in sunlight.
  * *Thick Armour*: Spend 1 Hate on a Protection test to roll +1d Armour.

#### 3. Udûn Sniffer / Fire-Fanatic (Attribute Level 4)
* **Culture**: Udûn Zealot / Balrog Worshipper | **Distinctive Features**: Crazed, Tough, Keen Scent
* **Endurance**: 16 | **Might**: 1 | **Hate**: 4 | **Parry**: — | **Armour**: 3d (Soot-caked hides & ash)
* **Combat Proficiencies**:
  * *Torch-staff*: 3d (Damage 4, Injury 14, Fiery Blow [Severe fire damage])
  * *Poisoned Blowdart*: 2d (Damage 2, Injury 12, Poison [Black Venom])
* **Fell Abilities**:
  * *Denizen of the Dark*: Attack rolls are Favoured in darkness.
  * *Heartless*: Immune to the *Intimidate Foe* combat action unless triggered by a Magical or Gandalf result.
  * *Keen Scent / Tracker*: Gains +2d on Awareness rolls to detect hidden intruders by scent.
  * *Hate Sunlight*: Loses 1 Hate per round in direct sunlight.

#### 4. Moria Orc Drummer (Attribute Level 3)
* **Culture**: Moria Orc / Signal Corps | **Distinctive Features**: Deformed, Loud
* **Endurance**: 12 | **Might**: 1 | **Hate**: 3 | **Parry**: +1 | **Armour**: 2d (Hide vest)
* **Combat Proficiencies**:
  * *Curved Knife*: 2d (Damage 3, Injury 14, Pierce)
  * *Bone Drum-Beater*: 2d (Damage 3, Injury 12, Heavy Blow)
* **Fell Abilities**:
  * *Denizen of the Dark*: Attack rolls are Favoured in darkness.
  * *Hate Sunlight*: Loses 1 Hate per round in sunlight.
  * *Drums in the Deep*: Instead of making an attack action, the Drummer may spend **1 Hate** to beat its massive kettle-drum, instantly raising the Company's **Strategic Eye Awareness by +3**!

#### 5. Black Uruk of Mordor (Attribute Level 5 — Elite Reinforcement)
* **Culture**: Uruk of Mordor / Shock-Troop | **Distinctive Features**: Fierce, Strong, Relentless
* **Endurance**: 20 | **Might**: 1 | **Hate**: 5 | **Parry**: +2 | **Armour**: 3d (Black iron plate)
* **Combat Proficiencies**:
  * *Broad-bladed Sword*: 3d (Damage 4, Injury 16, Pierce)
  * *Bow of Horn*: 3d (Damage 3, Injury 14, Pierce)
* **Fell Abilities**:
  * *Horrible Strength*: Spend 1 Hate when scoring a Piercing Blow to make the target hero's Protection roll **Ill-favoured**.
  * *Thick Armour*: Spend 1 Hate on a Protection roll to gain +2d Armour.

#### 6. Black Uruk Captain (Attribute Level 6 — Vanguard Commander)
* **Culture**: Uruk of Mordor / War-Leader | **Distinctive Features**: Cruel, Commanding
* **Endurance**: 24 | **Might**: 1 (or Might 2) | **Hate**: 6 | **Parry**: +3 | **Armour**: 4d (Full black plate)
* **Combat Proficiencies**:
  * *Great Scimitar*: 3d (Damage 5, Injury 16, Pierce, Break Shield)
  * *Iron Javelin*: 2d (Damage 5, Injury 14, Pierce)
* **Fell Abilities**:
  * *Horrible Strength*: Spend 1 Hate on a Piercing Blow to make the hero's Protection roll Ill-favoured.
  * *Yell of Triumph*: Spend 1 Hate when an ally or hero falls to immediately restore **1 Hate** to all Orcs within earshot.

---

### 5.2 Weapon Poison Mechanics (Black Orc-Venom)

Many sentry weapons (darts, arrows, and scavenged dagger blades in Locations 1, 3, and 9) are coated in thick, distilled mountain-spider venom mixed with corpse-grease.

```
========================================================================================
                              BLACK ORC-VENOM RULES
========================================================================================
 • TRIGGER           : When an adversary lands a Piercing Blow using a poisoned weapon, 
                       or spends a Success icon (6) to inject venom.
 • INITIAL EFFECT    : Target must make an immediate ENDURANCE / HEALING test (TN 14):
   - Success : The venom is resisted; target suffers standard weapon damage only.
   - Failure : The target contracts MODERATE POISON (loses 4 Endurance immediately 
               and gains the Weary condition until treated).
 • SEVERE INFECTION  : If the Feat Die shows the Eye of Sauron (S), the poison is SEVERE 
                       (loses 8 Endurance, suffers -1d on all physical tests, and requires 
                       First Aid to halt necrotic spread).
 • TREATMENT         : First Aid treatment requires a Healing (TN 14) test during a rest. 
                       Healing rolls lose (-1d) if Severe, and (-2d) if Grievous.
========================================================================================
```

---

## 6. Subterranean Environmental Hazards

The physical architecture of the Third Deep is an ancient, crumbling ruin beset by geothermal vents, demonic corruption, and centuries of structural fatigue.

```
                  ┌──────────────────────────────────────────────┐
                  │    ENVIRONMENTAL HAZARDS OF THE THIRD DEEP   │
                  └──────────────────────┬───────────────────────┘
                                         │
         ┌───────────────────────────────┼───────────────────────────────┐
         ▼                               ▼                               ▼
 [BALROG TOXIC MIASMA]         [SLAG-WORM TREMORS]           [PITFALLS & CHASMS]
  • Preserved toxic breath      • Seismic tremors & cave-ins  • Rungless vertical drops
  • 1-min vs 1-hr checks        • 30 Dmg keystone collapse    • 30–60 ft falls (Athletics)
  • Craft TN 15 respirators     • Athletics / Awareness TNs   • Band safety rope lines
```

---

### 6.1 Hazard 1: The Balrog Neurotoxic Miasma

* **Location & Context**: Preserved within the depressed vaults of **Location 7 (The Poisoned Halls)** and **Location 8 (The Upper Armoury)**. Unleashed by Durin's Bane during the slaughter of the Dwarven Tunnel-guards, this emerald-tinged vapor pools at floor level and rises to chest height.

```
========================================================================================
                               TOXIC MIASMA EXPOSURE MATRIX
========================================================================================
 EXPOSURE TIER         TESTING INTERVAL           FAILURE CONSEQUENCE
----------------------------------------------------------------------------------------
 1. Unprotected        Roll Endurance / Healing   Ill-favoured Feat Die roll:
    (Raw inhalation,   EVERY MINUTE               • 1–10: Lose that much Endurance.
     exposed mucous)                              • Eye (S): Reduced to 0 End & DYING!
----------------------------------------------------------------------------------------
 2. Protected          Roll Endurance / Healing   Standard Feat Die roll:
    (Vinegar cloths,   EVERY HOUR                 • 1–6: Lose that much Endurance.
     chewed herbs)                                • Eye (S): Suffer Severe Poison.
----------------------------------------------------------------------------------------
 3. Masterwork Mask    COMPLETE IMMUNITY          No tests required for 4 continuous 
    (Craft TN 15 mask) FOR 4 HOURS                exploration hours.
========================================================================================
```

* **Remedies & Engineering Solutions**:
  1. **Constructing Respirator Masks (Craft TN 14 / TN 15)**: Hjoldring, Einar, or Bróga can assemble up to 10 squad respirators utilizing oiled leather, charcoal granules, fine brass mesh, and dwarf-goggles. Success grants **4 hours of absolute immunity**.
  2. **Emergency Field Mask Repair**: If an Udûn Torch-staff scores a *Fiery Blow* against a hero wearing a mask, the mask ruptures! Repairing it in combat requires a **Craft (TN 14)** action (1 round).
  3. **Unjamming the Overhead Flue Damper**: In Location 7, a hero can climb the iron chimney wall and force open the ceiling ventilation lever (**Athletics TN 16** or **Craft TN 16**). Success vents the toxic fog from the chamber in 3 combat rounds, but the shrieking iron generates **+3 Noise Points**.

---

### 6.2 Hazard 2: Slag-Worm Tremors & Structural Collapses

Centuries of mining by subterranean worms and the immense mass of Mount Silvertine have left the granite ribs of the Third Deep precarious.

```
========================================================================================
                               STRUCTURAL COLLAPSE RULES
========================================================================================
 • TRIGGER ACTIONS   : Firing heavy siege engines (Location 5), toppling the stone idol 
                       (Location 4), detonating explosive powders, or pulling the 
                       Upper Gatehouse keystone winch (Location 2).
 • DETECTION CHECK   : Einar or Austri can detect shifting keystones via Scan (TN 14) 
                       (Einar rolls Favoured with The Broken Key).
 • HAZARD RESOLUTION : All characters in the 30-foot collapse zone must make a 
                       PROTECTION TEST (rolling 4d Armour) or ATHLETICS (TN 14) test:
   - Success : The character dives clear, taking 10 Falling Rubble Damage.
   - Failure : The character suffers 20 to 30 CRUSHING DAMAGE and is PINNED under fallen 
               masonry (suffering the Weary condition until extracted).
 • CLEARING RUBBLE   : Freeing a pinned ally requires an Athletics (TN 16) test or a 
                       collective Band War (3d) check against Readiness TN 15.
========================================================================================
```

---

### 6.3 Hazard 3: Subterranean Pitfalls & Chasm Crossings

Between the Mustering-Yard and the lower arsenals lie deep natural fissures, eroded drainage shafts, and deliberately cut Orc pitfalls.

```
========================================================================================
                             PITFALL & CHASM HAZARD MATRIX
========================================================================================
 HAZARD TYPE           LOCATION          TN / MECHANIC           CONSEQUENCE ON FAILURE
----------------------------------------------------------------------------------------
 False Flagstone Pit   Location 3        Scan TN 14              Falls 30 ft onto iron spikes: 
 (Orc Scrap-Trap)      (First Armoury)   (Disarm Craft TN 14)    15 Damage, Moderate Poison.
----------------------------------------------------------------------------------------
 Fractured Chasm       Location 1 -> 2   Athletics TN 14         Slips into the abyss! Must pass 
 (Acoustic Bridge)     (Gatehouse)       (Rope anchor +1d)       Athletics (TN 16) or be held by 
                                                                 companion rope line (+2 Noise).
----------------------------------------------------------------------------------------
 Rungless Ladder       Location 7 -> 8   Athletics TN 14         Falls 40 ft into toxic pool: 
 (Corroded Shaft)      (Upper Armoury)   (Climbing Rig +1d)      16 Damage, mask compromised.
========================================================================================
```

---

### 6.4 Hazard 4: Subterranean Water Perils Table

Whenever a character drinks from an untested pool, well, or cistern in the Third Deep, the GM rolls the **Feat Die**:

```
========================================================================================
                             SUBTERRANEAN WATER PERIL TABLE
========================================================================================
 FEAT DIE ROLL   WATER CONDITION & GAMEPLAY EFFECT
----------------------------------------------------------------------------------------
 Gandalf (G)     Pristine Ancient Dwarven Spring: Crystal-clear mineral water. Restores 
                 2 points of Hope and clears 1 tier of Fatigue immediately!
 9–10            Icy Snowmelt: Freezing runoff from Silvertine; refreshing and safe.
 7–8             Orc-Filth: Befouled with offal and tallow grease. Moderate Poison 
                 (Endurance loss 4, cleared by Short Rest).
 5–6             Bitter Mineral Water: Heavy with alkali. Must pass Valour (TN 14) 
                 to swallow; failure causes violent nausea (-1d on physical tests for 1 hr).
 3–4             Acidic Mine Runoff: Tainted with nitric acid and heavy metals. Severe 
                 Poison (Endurance loss 8; requires First Aid to purge).
 1–2             Malice of Durin's Bane: Tainted by demonic residue. The imbiber gains 
                 2 Shadow Points (Sorcery) and experiences terrifying hallucinations.
 Eye (S)         The Lurker's Pool: The water is clear, but the cistern is guarded by a 
                 concealed Udûn sentry ambush or a subterranean stone-crawler!
========================================================================================
```

---

## 7. Tactical GM Dashboard & Adversary Combat Matrix

```
=======================================================================================================
                                     RAPID ADVERSARY COMBAT MATRIX
=======================================================================================================
 FOE NAME            AL  END  MIGHT HATE PARRY ARMOUR  MAIN ATTACK       DMG/INJ   KEY FELL ABILITY
-------------------------------------------------------------------------------------------------------
 The Mauler          10  80     2    10    5     5d    Maul / Club 3d    8 / 16    Dull-Witted, Toughness
 Grimnar Disgraced    6  32     1/2   6/7  6     3d    Scimitar/Dagger 3d 5 / 16    Snake-Speed, Retaliate
 Grik the Skulker     2/3 8/12  1     2/3  4     1d/2d Jagged Knife 2d   3 / 12    Craven, Sneak Shadows
 Udûn Sniffer         4  16     1     4    —     3d    Torch-staff 3d    4 / 14    Fiery Blow, Keen Scent
 Orc Guard            4  16     1     4   +2     3d    Scimitar 3d       4 / 16    Denizen Dark, Thick Arm
 Orc Soldier          3  12     1     3   +1     2d    Orc-axe 2d        3 / 18    Craven, Break Shield
 Orc Drummer          3  12     1     3   +1     2d    Knife 2d          3 / 14    Drums in Deep (+3 Eye)
 Black Uruk           5  20     1     5   +2     3d    Broadsword 3d     4 / 16    Horrible Strength
 Black Uruk Captain   6  24     1     6   +3     4d    Great Scimitar 3d 5 / 16    Yell of Triumph
=======================================================================================================
```

---

### 7.1 Band Combat Integration Rules

When running mass skirmishes involving the Player-Heroes and their seven companion Dwarves against these adversary profiles, apply the following squad mechanics:

1. **Interception vs The Mauler**: If The Mauler targets a Player-Hero with a crushing *Maul* strike, **Dolg the Bulwark** or **Dúrmer the Iron-Shouldered** can use their combat reaction to interpose their tower-shield, taking the blow against their own Armour (3d/4d) and Endurance.
2. **Countering Grimnar's Speed**: If Grimnar uses *Snake-like Speed* to make a hero's attack Ill-favoured, **Khoril** can spend 1 point of Band Hope or use his *Leadership* action to coordinate a flanking maneuver with **Bláin**, restoring the attack to standard or Favoured status.
3. **Suppressing Orc Drummers**: When an Orc Drummer begins chanting to use *Drums in the Deep*, **Fáin Iron-Visor** can make an overwatch shot from Rearward stance (rolling 3d with *Dead-Eye*) to neutralize the drummer before the kettle-drum sounds.

---

### 7.2 Safety & Escalation Rules for the GM

* **Avoiding Unfair Swarms**: Never spawn additional adversary waves unless the **Alert Tracker** actively advances to a new Tier or a surviving Orc escapes into a side flue.
* **The Mauler Escalation Arc**: If the party engages The Mauler in straight melee without using the catwalks, stalactites, or Riddle duel, allow **Torvir's Enemy-lore (Orcs/Trolls)** or **Einar's Scan** to highlight the loose ceiling stones or the beast's weeping fear of pain.
* **Rewarding Stealth**: Defeating sentries silently in 1 round generates **+0 Noise Points**, allowing tactical parties to clear outposts in Locations 1, 3, and 5 without raising the dungeon alarm.
