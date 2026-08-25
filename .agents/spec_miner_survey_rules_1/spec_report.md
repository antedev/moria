# Authoritative System Rules and Mechanics Specification Report
**Project**: The One Ring 2e — Moria: Armouries of the Third Deep  
**Source Material**: 
- `TOR_Moria_2404.pdf` / `TOR_Moria_2404.jsonl`
- `The_One_Ring_Core_Rules_2401_(Third_Printing).pdf` / `The_One_Ring_Core_Rules_2401_(Third_Printing).jsonl`
- `The_One_Ring_Ruins_of_the_Lost_Realm.jsonl`
- `TOR_Starter_Set_The_Shire_2202.jsonl`

---

## Features Discovered

| # | Category | Feature | Description | Inputs | Outputs | Error / Failure Behavior | Discovered Via |
|---|----------|---------|-------------|--------|---------|--------------------------|----------------|
| 1 | Adversary Formatting | Stat Block Core Schema | Standardised presentation format for adversaries replacing 3 player attributes with single Attribute Level | Attribute Level (1–12+), Endurance, Might (1–3), Hate/Resolve, Parry (+0 to +3, —), Armour (1–5d), Combat Proficiencies | Adversary profile used in combat rounds | Missing stat defaults to standard archetype values | Core Rules pp. 143–144 |
| 2 | Adversary Mechanics | Hate vs. Resolve | Fighting drive and ability fuel. Hate = minions of Shadow (no mercy/quarter); Resolve = non-monstrous/misguided (can surrender; killing may be a Misdeed) | Spend 1 pt during attack or Protection roll | Gains (+1d) on roll; powers Fell Abilities | At 0 Hate/Resolve, creature becomes Weary; max spend/round = Might | Core Rules p. 143 |
| 3 | Adversary Mechanics | Might & Multi-Attacks | Determines number of Wounds to kill outright and number of attacks per round | Might rating (1, 2, or 3) | 1, 2, or 3 attacks per round; splits or focuses targets | At 0 Endurance, creature is taken out regardless of Might | Core Rules p. 143 |
| 4 | Adversary Mechanics | Special Damage Options | Triggered by spending Success icons (6s) on adversary attack rolls | 1 Success icon per trigger | Heavy Blow (+Attribute Level End loss), Break Shield (smashes shield), Pierce (+2 to Feat die for Injury TN), Seize (forces Forward stance/Brawling) | Cannot break magical/reward shields | Core Rules p. 144 |
| 5 | Fell Abilities | Comprehensive Catalog | Innate special powers and combat behaviors for monsters and dark servants | Hate/Resolve expenditure or passive trigger | Modifiers, area debuffs, bonus dice, resurrection | Can spend last point of Hate/Resolve | Core Rules pp. 144–157, Moria pp. 53–71 |
| 6 | Band Play | Band Structure & Readiness | Group mechanics for 6–8 Dwarven companions and allies | Starting Readiness (4 or 5), Dispositions (War, Vig, Man, Exp, Rally) | Readiness TN = $20 - \text{Readiness}$ (e.g. TN 15 at Readiness 5) | Readiness drops on casualties or prolonged crises | Moria pp. 189–195 |
| 7 | Band Play | Band Hope & Shadow | Shared pool dynamics for company allies | Shared Hope pool (max +5), Shared Shadow pool | Boosts Band actions and morale | Ally Severe/Grievous = +1 Shadow (Dread); Ally Death/Lost = +2 Shadow (Dread) | Moria pp. 192–193 |
| 8 | Band Play | Band Conditions: Injury & Fatigue | 5 Injury tiers (Fleeting, Moderate, Severe, Grievous, Lingering) & 4 Fatigue tiers | Rally rolls against Readiness TN + mods | Status tracking and degradation | $\ge 50\%$ incapacitated triggers Band Weary (1, 2, 3 on Success dice = 0) | Moria pp. 194–198 |
| 9 | Band Play | Desperate Stand | Ally sacrifice mechanic when critical roll fails | Failed critical test / death roll | Re-roll Favoured and Inspired | On Gandalf rune ($\text{G}$) ally survives; otherwise ally is lost/slain | Moria p. 195 |
| 10 | Band Play | Battles & Clashes | Turn-based mass combat structure with Leader Focus and Band Stance | Stance (Aggressive, Balanced, Guarded, Fleeing), Leader Action | Clash roll: War or Manoeuvre vs Readiness TN + Foe Might | Loss of Band Readiness / ally casualties on failure | Moria pp. 200–215 |
| 11 | Eye Awareness | Moria Noise Economy | Acoustic triggers accelerating Enemy attention in underground vaults | Lesser Noise (+1), Loud Noise (+2), Powerful Noise (+3) | Eye Awareness increase | Pushes score toward Hunt Threshold (14 in Moria) | Moria p. 39 |
| 12 | Eye Awareness | Discovery & Escapes | Foe look-outs reporting Company position to chieftains | Lone foe (+1), Messenger (+2), Messenger + nearby enemies (+3) | Eye Awareness increase | Faster triggering of Revelation episodes | Moria p. 39 |
| 13 | Revelation Episodes | Moria Revelation Tables | Specific event tables triggered when Eye Awareness $\ge$ Hunt Threshold (14) | Feat die roll on Dire Portents, Orc Assault, Terrors of the Dark, or Ghâsh! | Dynamic perils, ambushes, Nameless Things, Balrog encounters | Eye Awareness resets to 0 after episode resolution | Moria pp. 40–43 |
| 14 | Moria Hazards | Toxic Halls & Balrog Miasma | Lethal environmental fumes preserved in Second Deep & Armouries | Exposure frequency and protective gear | Raw: Grievous poison (roll/min); Protected: Severe poison (roll/hr) | Hero reduced to 0 Endurance is Dying | Moria pp. 151–154, Core p. 134 |
| 15 | Moria Hazards | Underground Waters | Tainted springs, well hazards, and mine tailings | Feat die roll on Water Peril Table | Clean water, Orc-filth, Bitter water, Mine poison, Malice of Durin's Bane | Severe poison or 2 Shadow (Sorcery) + hallucinations | Moria p. 35 |
| 16 | Moria Relics | Durin's Axe | Royal heirloom Great Axe forged by Aulë the Smith | Wielded by Hero (special Dwarf bonuses) | Rune-scored, Sup. Grievous, Sup. Keen; Dwarf unlocks Flame of Hope & Gleam of Terror | Claiming raises Company Eye Awareness by +4 instantly | Moria p. 154 |
| 17 | Moria Relics | Mithril Alloys & Wargear | Native Mithril, True Mithril, Ithildin, Mithril-steel, Erceleb, Thilevril, Sullied Mithril | Crafting and equipment rewards | Reduced Load (0 for helm/buckler), moon-letters, memory recording, fire blades | Sullied Mithril is corrupt Mordor devilry | Moria pp. 183–184 |
| 18 | Moria Relics | The Split Keys | Royal security system for Lower Armoury (King's Key & Marshal's Key) | Physical recovery in Last Redoubt (King) and Goblin Village (Marshal) | Opens The King's Door (Location 9) | Missing keys require Daunting/Disastrous intrusion attempts | Moria pp. 92, 153–154 |

---

## Edge Cases

| # | Feature | Input / Condition | Observed Behavior & Authoritative Rule |
|---|---------|-------------------|----------------------------------------|
| 1 | Balrog Combat | Hero attacks Durin's Bane with mundane weapon | **Demon of Might**: Balrog is completely immune to Endurance loss and Wounds from non-magical weapons. Even against magical weapons, Balrog can spend 1 Hate to cancel a Wound unless wrought specifically for the Bane of the Enemy. |
| 2 | Balrog Combat | Balrog reduced to 0 Endurance | **Demon of Might / Hideous Toughness**: Balrog is not slain; the attack causes a Piercing Blow instead. If still alive after Protection roll, Endurance immediately resets to half maximum (75 Endurance). |
| 3 | Balrog Aura | Hero strikes Balrog with close combat weapon | **Flame of Udûn**: Hero instantly suffers Severe Endurance loss from fire damage upon hitting. Only negated if Balrog is immersed in water. |
| 4 | Balrog Aura | Hero spends Hope in sight of Balrog | **Dreadful Spells**: Balrog spends 1 Hate; hero must pass an Ill-favoured Wisdom test or gain 3 Shadow (Sorcery) and have the Hope point cancelled/wasted. |
| 5 | The Mauler | Hero in Forward stance attempts Riddle task | **Dull-Witted**: Hero rolls Riddle as main action. On success, Mauler loses 1 Hate + 1 additional Hate per Success icon (6). |
| 6 | Poison Halls | Heroes explore Location 7/8 with improvised wet cloth & herbs | **Poison of the Armouries**: Endurance loss rate drops from Grievous (roll every minute) to Severe (roll every hour). Healing rolls to cure lose (1d). |
| 7 | Band Desperate Stand | Band fails critical test; ally sacrificed | **Desperate Stand**: Roll is repeated Favoured and Inspired. If Feat die shows Gandalf rune ($\text{G}$), ally miraculously survives; otherwise ally is killed or lost. |
| 8 | Band Weariness | $\ge 50\%$ of Band suffering Severe/Grievous injury or Spent/Collapsed fatigue | **Band Weary**: All Band rolls become Weary — Success dice showing 1, 2, 3 count as 0. |
| 9 | Moria Madness | Dwarf hero suffers Bout of Madness in Moria | Can replace standard Shadow Path flaw with **Moria-madness** flaw progression: #1 Distracted $\rightarrow$ #2 Mistrustful $\rightarrow$ #3 Blinded $\rightarrow$ #4 Jealous. |
| 10 | Orc Drummers | Orc Drummer acts during combat round | **Drums in the Deep**: Spends 1 Hate to forfeit attack and increase Company's Eye Awareness by +3 directly. |

---

# Detailed Rulebook Specifications

## 1. Exact TOR 2e Stat Block Structure & Formulas

### Adversary Profile Schema
Every adversary stat block in *The One Ring 2e* is defined by the following standard fields:

$$\begin{aligned}
\textbf{Name} &\quad \text{Descriptive Name} \\
\textbf{Distinctive Features} &\quad \text{Two traits (e.g. \textit{Brutish, Lumbering} or \textit{Fierce, Strong})} \\
\textbf{Attribute Level} &\quad \text{Single integer } L \in [1, 12+] \\
\textbf{Endurance} &\quad \text{Base stamina/health points } (E) \\
\textbf{Might} &\quad \text{Actions/round \& Wounds to kill } (M \in \{1, 2, 3\}) \\
\textbf{Hate / Resolve} &\quad \text{Fuel rating } H \in [1, 12+] \text{ (Hate for Shadow; Resolve for Men/Dwarves)} \\
\textbf{Parry} &\quad \text{Bonus added to Player-hero Strength TN } (P \in \{+0, +1, +2, +3, —\}) \\
\textbf{Armour} &\quad \text{Protection test dice } (A \in [1\text{d}, 5\text{d}]) \\
\textbf{Combat Proficiencies} &\quad \text{Attack Name } R \text{ (Damage/Injury, Special Damage)} \\
\textbf{Fell Abilities} &\quad \text{Unique special rules and reaction triggers}
\end{aligned}$$

### Stat Relationships & Rules
- **Attack Target Number**: A Player-hero attacking an adversary rolls against $\text{Strength TN} + \text{Adversary Parry}$.
- **Adversary Attack Rolls**: Adversaries roll a Feat die + Success dice equal to their Combat Proficiency rating against the target hero's $\text{Strength TN} + \text{Hero Shield/Parry}$.
- **Feat Die Inversion**: For servants of the Shadow, the Eye of Sauron ($\text{S}$) is the highest result (10 / automatic success), and the Gandalf rune ($\text{G}$) counts as 0.
- **Piercing Blow Threshold**: An adversary scores a Piercing Blow on a roll of 10 or Eye ($\text{S}$) on the Feat die.
- **Hate/Resolve Expenditure**: Spend 1 point to add (+1d) to an attack or Protection roll, or to activate a Fell Ability. Max spend per round = Might ($M$).
- **Special Damage Mechanics**:
  - **Heavy Blow**: 1 icon $\rightarrow$ Inflicts additional Endurance loss equal to Attribute Level ($+L$).
  - **Break Shield**: 1 icon $\rightarrow$ Smashes target's mundane shield (loses shield Parry bonus permanently).
  - **Pierce**: 1 icon $\rightarrow$ Adds $+2$ to the Feat die result for the purpose of beating the target's Injury TN.
  - **Seize**: 1 icon $\rightarrow$ Target is pinned into Forward stance making only Brawling attacks until spending a 6 on an attack roll to escape.
  - **Fiery Blow**: 1 icon $\rightarrow$ Target suffers severe/grievous fire damage.

---

## 2. Adversary Catalog: Moria & Armouries Encounters

### 1. The Mauler (Armoured Great Cave-troll)
*Obsessed with armoring itself after suffering pain at Dimrill Dale; dwells in Location 6.*
- **Distinctive Features**: Brutish, Lumbering
- **Attribute Level**: 10
- **Endurance**: 80
- **Might**: 2
- **Hate**: 10
- **Parry**: —
- **Armour**: 5d
- **Combat Proficiencies**: Crush 3 (6/12, Seize), Maul 3 (8/16, Break Shield)
- **Fell Abilities**:
  - *Dull-Witted*: Heroes in Forward stance can make a **Riddle** test as main action. On success, Mauler loses 1 Hate (+1 per Success icon).
  - *Hideous Toughness*: Attack reducing it to 0 Endurance causes a Piercing Blow instead. If it survives, Endurance resets to 40 (half max).
  - *Strike Fear*: Spend 1 Hate $\rightarrow$ all heroes in sight gain 2 Shadow (Dread). Failed Valour = daunted (no Hope).
  - *Thick Hide*: Spend 1 Hate $\rightarrow$ gain (+2d) on Protection roll.

### 2. Udûn-orc Fanatic
*Crazed fire-worshippers serving the Balrog in the Deeps.*
- **Distinctive Features**: Crazed, Tough
- **Attribute Level**: 4
- **Endurance**: 16
- **Might**: 1
- **Hate**: 4
- **Parry**: —
- **Armour**: 3d
- **Combat Proficiencies**: Torch-staff 3 (4/14, Fiery Blow [Severe fire loss])
- **Fell Abilities**:
  - *Denizen of the Dark*: Favoured attack rolls in darkness.
  - *Heartless*: Immune to Intimidate Foe unless Magical success.
  - *Hate Sunlight*: Loses 1 Hate per round in direct sun.

### 3. Udûn-orc Fire-touched
*Moria zealots warped by the fiery aura of the Balrog.*
- **Distinctive Features**: Frenzied, Fearsome
- **Attribute Level**: 6
- **Endurance**: 24
- **Might**: 2
- **Hate**: 6
- **Parry**: —
- **Armour**: 3d
- **Combat Proficiencies**: Torch-staff 3 (4/14, Fiery Blow [Severe fire loss])
- **Fell Abilities**:
  - *Denizen of the Dark*: Favoured attack rolls in darkness.
  - *Heartless*: Immune to Intimidate Foe unless Magical success.
  - *Hideous Toughness*: 0 Endurance causes Piercing Blow; if alive, resets to 12 Endurance.
  - *Hate Sunlight*: Loses 1 Hate per round in direct sun.

### 4. Black Uruk & Black Uruk Captain (Mordor Infiltrators)
- **Black Uruk**: Attr 5, End 20, Might 1, Hate 5, Parry +2, Armour 3d. Broad-bladed sword 3 (4/16, Pierce), Bow of Horn 3 (3/14, Pierce). Fell: *Horrible Strength* (1 Hate makes target Protection roll Ill-favoured), *Thick Armour* (1 Hate for +2d Protection).
- **Black Uruk Captain**: Attr 6, End 24, Might 1, Hate 6, Parry +3, Armour 4d. Broad-bladed Sword 3 (4/16, Pierce), Bow of Horn 3 (3/14, Pierce). Fell: *Horrible Strength*, *Yell of Triumph* (1 Hate restores 1 Hate to all allies).

### 5. Moria-Orc Drummer
- **Stats**: Same as Orc Soldier (Attr 3, End 12, Might 1, Hate 3, Parry +1, Armour 2d. Orc-axe 2 [3/18, Break Shield], Bow 2 [3/14, Pierce]).
- **Fell Ability**: *Drums in the Deep* — Instead of attacking, spend 1 Hate to increase the Eye Awareness of the Company by +3.

### 6. Durin's Bane (The Balrog of Moria)
- **Distinctive Features**: Mighty, Terrible
- **Attribute Level**: 12
- **Endurance**: 150
- **Might**: 3
- **Hate**: 12
- **Parry**: —
- **Armour**: 5d
- **Combat Proficiencies**: Flaming Sword 4 (8/24, Fiery Blow [Grievous fire loss]), Whip of Many Thongs 4 (6/18, Seize), Crush 3 (6/12, Break Shield)
- **Fell Abilities**:
  - *Deadly Wound*: Wounded targets make Ill-favoured Feat die rolls for Injury severity.
  - *Demon of Might*: Immune to Endurance loss and Wounds from non-magical weapons. Spends 1 Hate to cancel magical Wound (unless Bane weapon). 0 Endurance triggers Piercing Blow; resets to 75 Endurance if alive.
  - *Denizen of the Dark*: Favoured attack rolls in darkness.
  - *Dreadful Spells*: 1 Hate when hero spends Hope $\rightarrow$ Hero rolls Ill-favoured Wisdom; on fail/miserable, gains 3 Shadow (Sorcery) and Hope is lost/cancelled.
  - *Flame of Udûn*: Hero hitting Balrog in melee suffers Severe fire Endurance loss.
  - *Great Leap*: 1 Hate to attack any hero in any stance (including Rearward).
  - *Heartless*: Immune to Intimidate Foe unless Magical success.
  - *Horrible Strength*: 1 Hate on Piercing Blow makes target Protection roll Ill-favoured.
  - *Thing of Terror*: Round 1 start $\rightarrow$ all heroes roll Ill-favoured Valour; on fail/miserable, gain 3 Shadow (Dread) and are daunted (no Hope for entire fight).

### 7. Other Deeps Entities
- **Ash-wraith**: Attr 4, End 16, Might 1, Hate 4, Parry +1, Armour 1d. Fiery Touch 3 (4/14, Fiery Blow). Fell: *Flame of Udûn* (Moderate fire on hit), *Heartless*, *Snake-like Speed* (1 Hate to make incoming attack Ill-favoured).
- **Great Carrion Bat**: Attr 3, End 24, Might 2, Hate 3, Parry —, Armour 1d. Claws 3 (3/14, Seize), Fangs 3 (3/14, Pierce). Fell: *Craven*, *Ghastly Wings*, *Hate Sunlight*, *Wind-like Speed* (all incoming attacks Ill-favoured).
- **Marrow-eater**: Attr 4, End 30, Might 1, Hate 4, Parry +1, Armour 1d. Obsidian Knife 3 (3/14, Pierce), Sticky Fingers 3 (1/10, Seize). Fell: *Denizen of the Dark*, *Hate Sunlight*.
- **Stone Toad**: Attr 5, End 40, Might 2, Resolve 5, Parry —, Armour 4d. Bite 3 (5/16, Pierce), Crush 3 (5/12, Seize). Fell: *Great Leap*, *Hideous Toughness* (resets to 20 End), *Poison*, *Thick Hide* (+2d Protection).
- **The Wailing Horror (Nameless Thing)**: Attr 9, End 90, Might 2, Hate 9, Parry —, Armour 3d. Bite 3 (7/14, Pierce), Claw 3 (7/16, Seize). Fell: *Deadly Wound*, *Hate Sunlight*, *Hideous Toughness* (resets to 45 End), *Keening Wail* (1 Hate $\rightarrow$ 2 Shadow Dread, daunted), *Snake-like Speed*.
- **Dwarven Haunts**: Invisible slime-shadows. All heroes nearby gain 2 Shadow (Sorcery). Fail/Miserable = Load rating doubled until leaving area. Combat = repeat Shadow test every round.

---

## 3. The One Ring 2e Moria Band System

### Band Structure & Core Formula
$$\text{Readiness TN} = 20 - \text{Band Readiness}$$
For our active expedition (Balin's Veterans): $\text{Readiness} = 5 \implies \mathbf{\text{Readiness TN} = 15}$.

### The 5 Dispositions
1. **WAR (Rating 3)**: Resolves combat clashes, aggressive manoeuvres, and tactical assaults.
2. **VIGILANCE (Rating 2)**: Look-out duty, scouting, ambush detection, and perimeter defense.
3. **MANOEUVRE (Rating 2)**: Evasion, tactical withdrawal, navigating difficult terrain, and flight.
4. **EXPERTISE (Rating 2)**: Delving, engineering, trap disarming, lockpicking, and ancient lore.
5. **RALLY (Rating 1)**: Morale recovery, resisting fatigue, tending wounded, and rallying under fire.

### Band Pool Mechanics
- **Band Hope**: Shared Hope pool with capacity equal to $\sum \text{Hero Hope} + 5$. Expended to add (+1d) or trigger Inspired results.
- **Band Shadow**: Accumulates from trauma and losses:
  - Ally suffers Severe or Grievous injury $\rightarrow \mathbf{+1\text{ Shadow (Dread)}}$.
  - Ally slain or lost $\rightarrow \mathbf{+2\text{ Shadow (Dread)}}$.
- **Desperate Stand**: When a critical roll fails or an ally is about to perish, an ally steps forward. Re-roll the test **Favoured** and **Inspired**.
  - If the Feat die shows the Gandalf rune ($\text{G}$), the ally miraculously survives.
  - On any other result, the ally is slain or lost, and the Band gains 2 Shadow.

### Band Condition Degradation
- **Injury System (5 Tiers)**:
  1. *Fleeting*: Cleared after a short rest.
  2. *Moderate*: Cleared after a prolonged rest.
  3. *Severe*: Requires First Aid during a prolonged rest to reduce to Moderate.
  4. *Grievous*: Dying! Must receive First Aid within 1 hour to survive; prolonged rest First Aid drops it to Lingering.
  5. *Lingering*: Permanent penalty until Fellowship Phase. Another Grievous injury = immediate death.
  - *Endurance Test*: Roll **Rally** vs $\text{Readiness TN} + \text{Damage Threat}$ (Bothersome +0, Painful +1, Vicious +2, Dreadful +3).
- **Fatigue System (4 Tiers)**:
  - Tiers: *Fatigued* $\rightarrow$ *Faltering* $\rightarrow$ *Spent* $\rightarrow$ *Collapsed*.
  - *Fatigue Test*: Roll **Rally** vs $\text{Readiness TN} + \text{Fatigue Points}$, modified by Burden (Light +1d, Medium +0d, Heavy -1d, Overburdened -2d).
- **Band Weary**: If $\ge 50\%$ of Band members are incapacitated, severely injured, or spent/collapsed, the entire Band becomes **Weary**. All Success dice showing 1, 2, 3 count as 0.

### Mass Combat: Battles & Clashes
- **Clash Resolution**: Roll **War** (or **Manoeuvre**) vs $\text{Readiness TN} + \text{Enemy Might}$ ($-1\text{d}$ if an Archfoe is present).
- **Band Stance Options**:
  - *Aggressive*: Ill-favoured Clash roll; automatically reduces enemy Resistance by 1.
  - *Balanced*: Standard roll; full tactical flexibility.
  - *Guarded*: Favoured Clash roll; ignore enemy Special Damage icons.
  - *Fleeing*: Manoeuvre roll vs $\text{Readiness TN} + \text{Enemy Might}$ to disengage.
- **Leader Actions**:
  - *Command*: Roll **Battle** to grant bonus dice or stance benefits.
  - *Inspire*: Roll **Enhearten** to restore Band Hope or clear Faltering.
  - *Fight*: Attack directly using Combat Proficiency vs $\text{TN} + \text{Enemy Might}$.
  - *Duel*: Engage enemy Champion/Archfoe in single combat.
- **Enemy War Party Profiles**:
  - *Patrol*: Might 0, Resistance 3
  - *Pack*: Might 1, Resistance 6
  - *Warband*: Might 2, Resistance 9
  - *Horde*: Might 3, Resistance 12
  - *Archfoe Additions*: Lesser Archfoe (+0 Might, +1 Res, -1d Clash); Greater Archfoe (+1 Might, +3 Res, -1d Clash).

---

## 4. Eye Awareness, Noise Economy & 4-Stage Alert Tracker

### Moria Eye Awareness Fundamentals
- **Base Hunt Threshold**: **14** (Moria is classified as a Dark Land).
- **Revelation Trigger**: Occurs immediately when $\text{Eye Awareness} \ge \text{Hunt Threshold}$ (14).
- **Reset**: Eye Awareness resets to 0 upon resolving the Revelation Episode.

### Sound & Acoustic Economy
Moria's vast stone halls amplify vibrations across miles. Unwanted noise directly adds Eye Awareness:
$$\begin{array}{|l|c|l|}
\hline
\textbf{Noise Category} & \textbf{Eye Gain} & \textbf{Examples} \\
\hline
\text{Lesser Noise} & +1 & \text{Shouting, singing, dropping a stone into a shaft/well} \\
\text{Loud Noise} & +2 & \text{Melee combat, breaking down heavy doors, stone collapses} \\
\text{Powerful Noise} & +3 & \text{Orc war-drums, horn blasts, deliberate cave-ins, blast powders} \\
\hline
\end{array}$$

### Minion Discovery & Escape Penalties
$$\begin{array}{|l|c|l|}
\hline
\textbf{Discovery Event} & \textbf{Eye Gain} & \textbf{Circumstances} \\
\hline
\text{Lesser Discovery} & +1 & \text{A lone surviving enemy flees from combat} \\
\text{Major Discovery} & +2 & \text{An organized scout or messenger escapes} \\
\text{Perilous Discovery} & +3 & \text{A messenger escapes while reinforcements/warbands are near} \\
\hline
\end{array}$$

### 4-Stage Adventure Alert Tracker
To regulate dungeon tension during exploration of the Armouries of the Third Deep, the 4-Stage Alert Tracker maps to Eye Awareness and dungeon response:

```
[ALERT 0: UNDETECTED] ──(Eye 1-4)──> [ALERT 1: SUSPICION] ──(Eye 5-9)──> [ALERT 2: MOBILISATION] ──(Eye 10-13)──> [ALERT 3: GENERAL ALARM / HUNT (14+)]
```

1. **Alert 0: Undetected (Eye Awareness 0–4)**
   - *Atmosphere*: Tomb-like silence. Distant water drops.
   - *Enemy Posture*: Sentry posts relaxed, Goblins squabbling or sleeping.
   - *Modifications*: All Stealth and Explore tests gain (+1d).
2. **Alert 1: Suspicion / Tapping (Eye Awareness 5–9)**
   - *Atmosphere*: Faint rhythmic knocks echoing in walls (*tom-tap, tap-tom*).
   - *Enemy Posture*: Sentry patrols doubled; scouting parties dispatched to investigate noise.
   - *Modifications*: Standard rolls; Tappers may intervene (+1d or -1d).
3. **Alert 2: Mobilisation (Eye Awareness 10–13)**
   - *Atmosphere*: Orc-horns sounding in upper galleries; smell of sulphur and torch-smoke.
   - *Enemy Posture*: Doors barred from opposite side; ambush teams pre-positioned; Drummers ready.
   - *Modifications*: Awareness rolls to avoid ambush lose (-1d); Hunt Threshold reduced by 2.
4. **Alert 3: General Alarm & Hunt (Eye Awareness 14+)**
   - *Atmosphere*: "Doom, doom" drumbeats roll through the deeps. Choking fumes rise.
   - *Enemy Posture*: Full Revelation Episode triggered! Roving Great Cave-trolls, Udûn zealot swarms, or Balrog manifestations.
   - *Modifications*: Next encounter is an ambush or boss confrontation. Eye Awareness resets to 0 after resolution.

---

## 5. Environmental Hazards & Deeps Lore

### The Poison of the Armouries (Second & Third Deep)
- **Origin**: Noxious breath unleashed by Durin's Bane during the slaughter of the Dwarven Tunnel-guards in the Poisoned Halls (12th and 14th Halls of Second Deep).
- **Mechanical Exposure**:
  - *Unprotected*: Counts as **Grievous Poison**. Exposed characters roll for Endurance loss **every minute** (Ill-favoured Feat die roll: 1–10 = lose value; Eye = reduced to 0 Endurance and Dying).
  - *Protected* (All skin covered, wet cloth over nose/mouth, chewing dried medicinal herbs): Downgraded to **Severe Poison**. Roll for Endurance loss **every hour**.
- **Remedies & Countermeasures**:
  - *First Aid / Healing*: Successful **Healing** test removes poison. The roll loses (-1d) if Severe, and (-2d) if Grievous.
  - *Craft / Engineering*: A **Craft** test (TN 15) can construct sealed respirators using oiled leather, charcoal filters, and Dwarf-goggles, granting 4 hours of breathable air.

### Subterranean Water Hazards (Peril Table)
When drinking from untested springs in Moria, roll the Feat die:
- **Eye of Sauron ($\text{S}$)**: Pure water, but guarded by an ambush of Orcs or a Nameless Thing.
- **1–2 (Malice of Durin's Bane)**: 2 Shadow (Sorcery); fail = Moria-madness hallucinations.
- **3–4 (Poisoned by Mines)**: Tainted with mineral washings/nitric acid; Severe poison.
- **5–6 (Bitter Water)**: Must pass **Valour** test to force oneself to swallow.
- **7–8 (Orc-Filth)**: Befouled water; Moderate poison.
- **9–10 (Icy Cold)**: Freezing snow-melt; safe to drink, but seasonal.
- **Gandalf Rune ($\text{G}$)**: Pure, refreshing ancient Dwarven spring water!

---

## 6. Relics & Magic Items of the Armouries

### 1. Durin's Axe (Royal Artifact)
- **Type**: Great Axe
- **Lore**: Forged in the Elder Days by Aulë the Smith; wielded by the Kings of Khazad-dûm.
- **Enchanted Rewards**:
  - *Rune-scored*: +1 to Feat die rolls on attacks.
  - *Superior Grievous*: Damage rating increased by +2.
  - *Superior Keen*: Piercing Blow scored on a roll of 8, 9, 10, or $\text{G}$.
- **Dwarven Attunement**: If wielded by a Dwarf, it instantly manifests:
  - *Flame of Hope*: Illuminates dark areas; companions gain +1 Hope when rallying.
  - *Gleam of Terror*: Spend 1 Hope to force all foes in sight to make a Fear test.
- **Curse / Shadow Attraction**: Claiming Durin's Axe instantly raises Company **Eye Awareness by +4**.

### 2. Tunnel-Guard Wargear (Mithril-Forged)
- **Tunnel-Guard Mattock**: Two-handed weapon (Damage 7, Injury 18, Break Shield/Pierce), forged of Mithril-steel. Load 2.
- **Mithril Buckler / Shield**: Load 0. Can be used in conjunction with a 2-handed weapon (such as a Great Axe or Mattock) while retaining its +1 Parry bonus.
- **Mithril Helm**: Load 0. Grants +1d to Protection tests.

### 3. The Broken Key / The King's Key & Marshal's Key
- **The King's Key**: Stored in the royal sarcophagus in the *Last Redoubt* (p. 92).
- **The Marshal's Key**: Carried down into *Goblin Village* (p. 154) by Orc looters from the 16th Hall of Fifth Deep.
- **Function**: Inserting either key (or both to bypass internal warding) opens **The King's Door** (Location 9), granting access to the royal vault in the **Lower Armoury** (Location 10).

### 4. War-Horn of the Underworld (Wondrous Item)
- **Description**: Dragon's horn bound in steel and etched with ancient Khuzdul runes.
- **Blessings**: Blessing of **Battle** and **Enhearten**.
- **The Curse**: When sounded, any ally who hastens to aid the bearer suffers from **Ill-favoured Protection rolls** for the remainder of the battle.

---

## 7. The 10 Locations of the Armouries of the Third Deep

```
                      [1. Mustering-Yard]
                              │
                    [2. Upper Gatehouse]
                              │
             ┌────────────────┴────────────────┐
             ▼                                 ▼
    [3. First Armoury]                [4. The Broken Hall]
             │                                 │
    [5. Second Armoury]               [7. The Poisoned Halls]
             │                                 │
    [6. Hall of the Mauler]           [8. The Upper Armoury]
             │                                 │
             └────────────────┬────────────────┘
                              ▼
                     [9. The King's Door]
                              │
                    [10. The Lower Armoury]
                     (Durin's Axe & Vault)
```

1. **The Mustering-Yard**: Vast crossroads hall where Dwarf hosts assembled. Scorch marks from Balrog's first rising. Neutral parley ground between Udûn Orcs and Moria Orcs.
2. **The Upper Gatehouse**: Reinforced blast-doors shattered outward by demonic heat.
3. **The First Armoury**: Stripped bare by Orc scavengers; remaining weapons are bent, notched, and slathered in black Orc-venom.
4. **The Broken Hall**: Commemorative martial museum defiled by Orcs. Murals defaced with mockery of King Thrór's death. Dread test (1 Shadow, 2 for Dwarves). Scan reveals clue to King's Key in Last Redoubt.
5. **The Second Armoury**: Partially looted; contains remnants of Dwarven siege engines, ballistas, and battering rams. Scan test finds serviceable weapons.
6. **The Hall of the Mauler**: Lair of **The Mauler** (Armoured Great Cave-troll). Littered with heaps of stolen ironmongery and crushed skeletons.
7. **The Poisoned Halls**: 12th & 14th Halls of Second Deep. Preserved bodies of Dwarven knightly captains in stasis. Dying scribe's letter reveals Marshal's Key lost in Fifth Deep (taken to Goblin Village). Severe/Grievous poison hazard.
8. **The Upper Armoury**: Poisoned chamber containing goblin corpses and racks of unlooted dwarf-forged iron war-gear.
9. **The King's Door**: Massive rune-sealed portal bearing the Crown-and-Anvil of Durin. Requires King's Key or Marshal's Key to bypass.
10. **The Lower Armoury**: Sealed royal vault. Contains a Greater Hoard (at least 3 Famous Weapons/Armour), chests of refined Mithril ingots, and **Durin's Axe**.
