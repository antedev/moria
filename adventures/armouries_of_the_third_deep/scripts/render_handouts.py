#!/usr/bin/env python3
"""
render_handouts.py — Master Print & PDF Generator for Moria Handouts
====================================================================
Transforms adventure handouts into gorgeous, print-ready A4 PDF and HTML documents
optimized for grayscale / black & white printing on standard desktop printers.

Uses Microsoft Edge / Chromium headless PDF engine with CSS Paged Media.

Outputs:
  - handouts/html/*.html (Standalone interactive & browser-printable HTML)
  - handouts/pdf/*.pdf  (High-resolution vector A4 PDFs)
  - handouts/pdf/handouts_complete_bundle.pdf (All handouts unified in 1 print package)

Usage:
  python scripts/render_handouts.py
"""

import os
import sys
import subprocess
from pathlib import Path
from typing import Optional, List, Tuple

BASE_DIR = Path(__file__).resolve().parent.parent
HANDOUTS_SRC = BASE_DIR / "handouts"
HTML_DIR = HANDOUTS_SRC / "html"
PDF_DIR = HANDOUTS_SRC / "pdf"

EDGE_PATHS = [
    Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
    Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
    Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
]

def find_pdf_engine() -> Optional[Path]:
    for p in EDGE_PATHS:
        if p.exists():
            return p
    return None

# =============================================================================
# CSS STYLESHEET (A4 Grayscale & Dwarven Design)
# =============================================================================

COMMON_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;900&family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400&family=JetBrains+Mono:wght@400;600&display=swap');

@page {
    size: A4 portrait;
    margin: 10mm 12mm 12mm 12mm;
}

@page :left {
    @bottom-left {
        content: "The Armouries of the Third Deep — The One Ring 2e";
        font-family: 'Cinzel', serif;
        font-size: 7pt;
        color: #666;
    }
    @bottom-right {
        content: counter(page);
        font-family: 'Cinzel', serif;
        font-size: 8pt;
        font-weight: bold;
    }
}

@page :right {
    @bottom-left {
        content: "The Armouries of the Third Deep — The One Ring 2e";
        font-family: 'Cinzel', serif;
        font-size: 7pt;
        color: #666;
    }
    @bottom-right {
        content: counter(page);
        font-family: 'Cinzel', serif;
        font-size: 8pt;
        font-weight: bold;
    }
}

* {
    box-sizing: border-box;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
}

body {
    font-family: 'Cormorant Garamond', 'Georgia', serif;
    font-size: 9.5pt;
    line-height: 1.25;
    color: #111;
    background-color: #fff;
    margin: 0;
    padding: 0;
}

h1, h2, h3, h4, .cinzel {
    font-family: 'Cinzel', 'Palatino', serif;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin: 0;
    color: #000;
}

h1 {
    font-size: 15pt;
    font-weight: 900;
    text-align: center;
    border-bottom: 2px solid #222;
    padding-bottom: 2px;
    margin-bottom: 4px;
}

h2 {
    font-size: 11pt;
    font-weight: 700;
    border-bottom: 1px solid #444;
    padding-bottom: 1px;
    margin-top: 6px;
    margin-bottom: 3px;
    background: #f0f0f0;
    padding-left: 4px;
}

h3 {
    font-size: 9.5pt;
    font-weight: 700;
    margin-top: 4px;
    margin-bottom: 2px;
}

.subtitle {
    text-align: center;
    font-size: 8pt;
    font-style: italic;
    color: #444;
    margin-bottom: 6px;
}

/* Grayscale Table Styling */
table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 3px;
    margin-bottom: 5px;
    font-size: 8.5pt;
}

th, td {
    border: 1px solid #333;
    padding: 2.5px 4px;
    text-align: left;
    vertical-align: top;
}

th {
    background-color: #e2e2e2;
    font-family: 'Cinzel', serif;
    font-size: 8pt;
    font-weight: bold;
    color: #000;
}

tr:nth-child(even) td {
    background-color: #f7f7f7;
}

/* Grids & Cards */
.grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
}

.grid-3 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 6px;
}

.card {
    border: 1.5px solid #222;
    padding: 5px 7px;
    background: #fff;
    margin-bottom: 5px;
    border-radius: 2px;
}

.card-header {
    font-family: 'Cinzel', serif;
    font-size: 8.5pt;
    font-weight: bold;
    background: #e8e8e8;
    margin: -5px -7px 4px -7px;
    padding: 2px 7px;
    border-bottom: 1px solid #333;
}

/* Rune & In-World Prop Styling */
.rune-frame {
    border: 3px double #222;
    padding: 10px;
    background: #fafafa;
    position: relative;
}

.cirth-inscription {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11pt;
    letter-spacing: 0.15em;
    background: #eee;
    padding: 8px;
    border: 1px dashed #444;
    text-align: center;
    margin: 6px 0;
}

/* Checkboxes & Form Elements */
.checkbox-box {
    display: inline-block;
    width: 10px;
    height: 10px;
    border: 1.2px solid #000;
    margin-right: 3px;
    vertical-align: middle;
}

.bubble {
    display: inline-block;
    width: 12px;
    height: 12px;
    border: 1.2px solid #000;
    border-radius: 50%;
    margin-right: 2px;
    vertical-align: middle;
}

.page-break {
    page-break-before: always;
    break-before: page;
}

.avoid-break {
    page-break-inside: avoid;
    break-inside: avoid;
}

/* High-Density ASCII Map Container */
.ascii-map {
    font-family: 'JetBrains Mono', monospace;
    font-size: 6.8pt;
    line-height: 1.1;
    background: #fdfdfd;
    border: 1.5px solid #333;
    padding: 6px;
    white-space: pre;
    overflow: hidden;
}

.stat-badge {
    display: inline-block;
    border: 1px solid #444;
    background: #e8e8e8;
    padding: 1px 3px;
    font-size: 7.5pt;
    font-family: 'Cinzel', serif;
    font-weight: bold;
    margin-right: 3px;
}
"""

# =============================================================================
# HTML TEMPLATES
# =============================================================================

def build_gm_cheat_sheet_html() -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>GM Rapid Reference Cheat Sheet — Armouries of the Third Deep</title>
<style>{COMMON_CSS}</style>
</head>
<body>

<h1>The Armouries of the Third Deep — GM Rapid Cheat Sheet</h1>
<div class="subtitle">The One Ring 2e • Moria: Through the Doors of Durin • Balin's Expedition 2989 T.A.</div>

<div class="grid-2">
    <!-- Left Column: Heroes & Core Systems -->
    <div>
        <div class="card avoid-break">
            <div class="card-header">1. PLAYER-HERO TARGET NUMBERS (ATTRIBUTE TN)</div>
            <table>
                <tr>
                    <th>Hero & Calling</th>
                    <th>STR TN</th>
                    <th>HRT TN</th>
                    <th>WIT TN</th>
                    <th>Parry / Mail</th>
                    <th>Key Distinctive Traits (+1d)</th>
                </tr>
                <tr>
                    <td><b>Torvir Hammerstone</b><br><i>Champion (Durin)</i></td>
                    <td><b>13</b></td>
                    <td><b>18</b></td>
                    <td><b>15</b></td>
                    <td>15 / 5d</td>
                    <td>Fierce, Willful, <i>Enemy-lore (Orcs)</i></td>
                </tr>
                <tr>
                    <td><b>Einar son of Anar</b><br><i>Treasure Hunter (Iron)</i></td>
                    <td><b>14</b></td>
                    <td><b>17</b></td>
                    <td><b>15</b></td>
                    <td>20 / 3d</td>
                    <td>Cunning, Wary, <i>Burglary</i>, Broken Key (+2 Scan)</td>
                </tr>
                <tr>
                    <td><b>Khoril Hornblower</b><br><i>Captain (Durin)</i></td>
                    <td><b>13</b></td>
                    <td><b>16</b></td>
                    <td><b>16</b></td>
                    <td>17 / 3d</td>
                    <td>Wary, Cunning, <i>Leadership</i>, Battle Horn (+1 Battle)</td>
                </tr>
            </table>
            <div style="font-size:7.5pt; color:#444;">
                * <b>Band Target Number</b>: <b>TN 15</b> (20 − Readiness Rating 5). Dispositions: War 3, Vigilance 2, Manoeuvre 2, Expertise 2, Rally 1.
            </div>
        </div>

        <div class="card avoid-break">
            <div class="card-header">2. THE 4-STAGE ALERT TRACKER & NOISE ECONOMY</div>
            <table>
                <tr>
                    <th>Alert Stage</th>
                    <th>Points</th>
                    <th>Infiltration Effects & Enemy Posture</th>
                </tr>
                <tr>
                    <td><b>0: Quiet Shadows</b></td>
                    <td>0–3 AP</td>
                    <td>Standard patrol routines; careless sentries; standard Stealth.</td>
                </tr>
                <tr>
                    <td><b>1: Unease & Sniffers</b></td>
                    <td>4–7 AP</td>
                    <td>Torches lit; Udûn sniffers & bats released; <b>Stealth is Ill-favoured</b>.</td>
                </tr>
                <tr>
                    <td><b>2: Hunted & Barricaded</b></td>
                    <td>8–11 AP</td>
                    <td>Chokepoints barricaded; sentry squads doubled; <b>Grimnar stalks rear</b>.</td>
                </tr>
                <tr>
                    <td><b>3: Drums in the Deep</b></td>
                    <td>12+ AP</td>
                    <td>Iron drums sound general alarm! <b>10 combat rounds / 2 turns to extract</b>.</td>
                </tr>
            </table>
            <div style="font-size:7.5pt; line-height:1.2;">
                <b>Noise Triggers</b>: Unmuffled march (+1 AP) • Echo combat (+1 AP/round) • Horn (+3 AP, +1 Eye) • Stone smash (+2 AP) • Troll roar (+3 AP) • Durin's Axe lifted (<b>+4 Eye Awareness</b>).<br>
                <b>Noise Relief</b>: Silent kill in R1 (-1 AP) • Diversion fire (-2 AP) • Decoy trap (-2 AP) • Gatehouse fortified (-1 AP/Act).
            </div>
        </div>

        <div class="card avoid-break">
            <div class="card-header">3. CRITICAL HAZARDS & SKILL ENDEAVOURS</div>
            <div style="font-size:8pt; line-height:1.25;">
                • <b>Balrog Toxic Gas (Breath of the Pit)</b>: Entering Areas 7/8. With respirator/herbs, test <b>Protection (STR TN)</b> once per hour. Failure: 2 End loss + Weary. (Without masks: roll every 1 minute for 4 End loss + Dread).<br>
                • <b>Slag-Worms Collapse</b>: Explosive noise causes iron collapse. Test <b>ATHLETICS (STR TN)</b> or take 8 Dmg (Inj 16).<br>
                • <b>Area 2 Gatehouse Fortification</b>: Skill Endeavour <b>Resistance 3</b> (CRAFT / EXPLORE).<br>
                • <b>Area 3 Scythe Trap Network</b>: Skill Endeavour <b>Resistance 3</b> (CRAFT / SCAN).<br>
                • <b>Area 4 Balrog Idol Toppling</b>: Skill Endeavour <b>Resistance 3</b> (ATHLETICS / CRAFT).<br>
                • <b>Area 5 Siege Ballista Calibrate</b>: Skill Endeavour <b>Resistance 3</b> (CRAFT / BATTLE).<br>
                • <b>Area 7 Squad Respirators</b>: Skill Endeavour <b>Resistance 3</b> (HEALING / CRAFT).<br>
                • <b>Area 9 King's Door Lock</b>: Skill Endeavour <b>Resistance 6</b> (CRAFT / LORE).
            </div>
        </div>
    </div>

    <!-- Right Column: Keyed Locations & Adversary Stats -->
    <div>
        <div class="card avoid-break">
            <div class="card-header">4. 10 KEYED LOCATIONS OPERATIONAL MATRIX</div>
            <table>
                <tr>
                    <th>Loc # & Landmark</th>
                    <th>Key Skill Checks</th>
                    <th>Consequence on Failure / 6s</th>
                </tr>
                <tr>
                    <td><b>1. Mustering-Yard</b></td>
                    <td>STEALTH roll to slip past<br>BATTLE roll for ambush</td>
                    <td>Fail: Patrol spotted (+1 AP)<br>6: Silent kill / +1d on opening round</td>
                </tr>
                <tr>
                    <td><b>2. Upper Gatehouse</b></td>
                    <td>CRAFT roll Endeavour Res 3<br>AWARENESS roll spot trap</td>
                    <td>Fail: Door unsecured<br>6: +1 extraction round / -1 AP per Act</td>
                </tr>
                <tr>
                    <td><b>3. First Armoury</b></td>
                    <td>SCAN roll (Favoured)<br>CRAFT roll (+1d) scavenge arms</td>
                    <td>Fail: 4 Dmg + loud crash (+2 AP)<br>6: Recovers 12 spearheads & pry-bars</td>
                </tr>
                <tr>
                    <td><b>4. Broken Hall</b></td>
                    <td>VALOUR roll vs Dread (+1 Shad)<br>LORE/RIDDLE roll Cartouche</td>
                    <td>Flaw trigger: Wrath urges idol smash<br>6: Reveals King's Key is in Old Moria</td>
                </tr>
                <tr>
                    <td><b>5. Second Armoury</b></td>
                    <td>CRAFT roll Endeavour Res 3<br>ATHLETICS roll to aim ram</td>
                    <td>Fail: Ballista jams<br>6: Heavy Ballista armed (24 Dmg to Troll!)</td>
                </tr>
                <tr>
                    <td><b>6. Hall of Mauler</b></td>
                    <td>STEALTH roll across scrap<br>RIDDLE roll duel in Forward</td>
                    <td>Fail: Troll awakens (+3 AP)<br>6: Strips 1 Hate/icon from The Mauler</td>
                </tr>
                <tr>
                    <td><b>7. Poisoned Halls</b></td>
                    <td>PROTECTION roll (gas) hourly<br>SCAN roll find Scribe Letter</td>
                    <td>Fail: 2 End loss + Weary<br>6: Recovers Scribe Slate & 3 Gromril Mails</td>
                </tr>
                <tr>
                    <td><b>8. Upper Armoury</b></td>
                    <td>EXPLORE roll clear gas cache</td>
                    <td>Yields 30 masterwork Dwarven weapons</td>
                </tr>
                <tr>
                    <td><b>9. King's Door</b></td>
                    <td>CRAFT roll Endeavour Res 6<br>VALOUR roll Blood of Durin</td>
                    <td>Fail: Lock jams; requires Marshal Key<br>6: Adamant door unlocks smoothly</td>
                </tr>
                <tr>
                    <td><b>10. Lower Vault</b></td>
                    <td>Greater Hoard (120 TP)</td>
                    <td><b>Claiming Durin's Axe: +4 Eye Awareness!</b></td>
                </tr>
            </table>
        </div>

        <div class="card avoid-break">
            <div class="card-header">5. ADVERSARY COMBAT PROFILES</div>
            <table>
                <tr>
                    <th>Adversary</th>
                    <th>Stats & Armour</th>
                    <th>Proficiencies & Special Attacks</th>
                    <th>Fell Abilities & Key Tactics</th>
                </tr>
                <tr>
                    <td><b>THE MAULER</b><br><i>Armoured Cave-Troll</i></td>
                    <td>AL 10, End 80<br>Might 2, Hate 10<br>Parry —, <b>Armour 5</b></td>
                    <td>• Crush 3 (6/12, Seize)<br>• Maul 3 (8/16, Break Shield)</td>
                    <td><b>Dull-Witted</b> (Riddle duel strips Hate)<br><b>Hideous Toughness</b> (Reset to 40 End)<br><b>Strike Fear</b> (2 Shadow) • <b>Thick Hide</b> (+2d)</td>
                </tr>
                <tr>
                    <td><b>GRIMNAR</b><br><i>Disgraced Great Orc</i></td>
                    <td>AL 6, End 36<br>Might 2, Hate 6<br><b>Parry +2, Armour 3d</b></td>
                    <td>• Heavy Scimitar 3 (5/16)<br>• Stolen Dagger 3 (4/14 Keen)</td>
                    <td><b>Hatred (Durin's Folk, Favoured)</b><br><b>Snake-Speed (Ill-favoured)</b><br><b>Vengeful Strike</b> • <b>Hideous Toughness</b></td>
                </tr>

                <tr>
                    <td><b>UDÛN SNIFFERS</b><br><i>Deep Trackers (x4)</i></td>
                    <td>AL 4, End 16<br>Hate 3, Armour 2d</td>
                    <td>• Serrated Spear 2 (4/14 Pois)<br>• Short Bow 2 (3/12)</td>
                    <td><b>Blood-Scent</b> (Ignores darkness penalties)<br><b>Orc-Poison</b> (2 End loss / 10 min on Injury)</td>
                </tr>
            </table>
        </div>
    </div>
</div>

</body>
</html>
"""

def build_band_worksheet_html() -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Band Management Worksheet — The Armouries of the Third Deep</title>
<style>{COMMON_CSS}</style>
</head>
<body>

<h1>Dwarf Companion Band — Tactical Worksheet</h1>
<div class="subtitle">Moria Band Engine • Readiness Rating 5 (Band TN 15) • Balin's Vanguard (2989 T.A.)</div>

<div class="grid-2">
    <div class="card">
        <div class="card-header">EXPEDITION SQUAD METRICS</div>
        <table>
            <tr>
                <th>Metric</th>
                <th>Rating / Value</th>
                <th>Mechanical Effect at Table</th>
            </tr>
            <tr>
                <td><b>Band Readiness</b></td>
                <td><b>5 (Band TN 15)</b></td>
                <td>Roll Feat Die + Disposition against TN 15 for all Band tests.</td>
            </tr>
            <tr>
                <td><b>Band Size & Load</b></td>
                <td><b>7 Dwarves (Heavy Load)</b></td>
                <td>Can haul 600 lbs of recovered wargear without hero penalties.</td>
            </tr>
            <tr>
                <td><b>Band Hope</b></td>
                <td><span class="bubble"></span><span class="bubble"></span><span class="bubble"></span><span class="bubble"></span><span class="bubble"></span><span class="bubble"></span><span class="bubble"></span><span class="bubble"></span><span class="bubble"></span><span class="bubble"></span><span class="bubble"></span><span class="bubble"></span> (12 / 12)</td>
                <td>Spend to grant +1d to Band roll. Demoralized at 0 (-1d to all rolls).</td>
            </tr>
            <tr>
                <td><b>Alert Tracker</b></td>
                <td>[ 0 ] [ 1 ] [ 2 ] [ 3 ] [ 4 ] [ 5 ] [ 6 ] [ 7 ] [ 8 ] [ 9 ] [ 10 ] [ 11 ] [ 12+ ]</td>
                <td>0–3: Normal | 4–7: Sniffers | 8–11: Hunted | 12+: General Alarm</td>
            </tr>
            <tr>
                <td><b>Eye Awareness</b></td>
                <td>[ 2 ] [ 3 ] [ 4 ] [ 5 ] [ 6 ] [ 7 ] [ 8 ] [ 9 ] [ 10 ] [ 11 ] [ 12 ] [ 13 ] <b>[ 14 HUNT ]</b></td>
                <td>Revelation Episode triggers when Eye Awareness reaches 14!</td>
            </tr>
        </table>
    </div>

    <div class="card">
        <div class="card-header">THE 5 BAND DISPOSITIONS</div>
        <table>
            <tr>
                <th>Disposition</th>
                <th>Rating</th>
                <th>Active Table Function</th>
            </tr>
            <tr>
                <td><b>WAR</b></td>
                <td><b>+3d</b></td>
                <td>Melee clashes, holding chokepoints, forming shield-wall phalanxes.</td>
            </tr>
            <tr>
                <td><b>VIGILANCE</b></td>
                <td><b>+2d</b></td>
                <td>Scout screens, detecting ambushes, spotting Orc patrol lanterns.</td>
            </tr>
            <tr>
                <td><b>MANOEUVRE</b></td>
                <td><b>+2d</b></td>
                <td>Marching discipline, keeping armor muffled, swift tactical repositioning.</td>
            </tr>
            <tr>
                <td><b>EXPERTISE</b></td>
                <td><b>+2d</b></td>
                <td>Smithing, bracing stone archways, repairing siege engines, prying chests.</td>
            </tr>
            <tr>
                <td><b>RALLY</b></td>
                <td><b>+1d</b></td>
                <td>Recovering from fear, restoring morale after troll encounters.</td>
            </tr>
        </table>
    </div>
</div>

<h2>Active Companion Roster & Squad Assignment Tracker</h2>
<table>
    <tr>
        <th>Companion Dwarf</th>
        <th>Specialty & Gear</th>
        <th>Max End</th>
        <th>Current End</th>
        <th>Injury Box</th>
        <th>Assigned Tactical Squad Role</th>
    </tr>
    <tr>
        <td><b>Dúrmer</b></td>
        <td>Veteran Heavy Infantry • Tower Shield</td>
        <td>22</td>
        <td>[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; / 22 ]</td>
        <td><span class="checkbox-box"></span> Uninjured<br><span class="checkbox-box"></span> Moderate<br><span class="checkbox-box"></span> Severe</td>
        <td>
            <span class="checkbox-box"></span> <b>Vanguard Shield-Wall</b> (Absorbs 1 Pierce for a hero)<br>
            <span class="checkbox-box"></span> <b>Gatehouse Guard</b> (Holds extraction point)
        </td>
    </tr>
    <tr>
        <td><b>Hjoldring</b></td>
        <td>Stonemason • Heavy Wedges & Mallet</td>
        <td>18</td>
        <td>[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; / 18 ]</td>
        <td><span class="checkbox-box"></span> Uninjured<br><span class="checkbox-box"></span> Moderate<br><span class="checkbox-box"></span> Severe</td>
        <td>
            <span class="checkbox-box"></span> <b>Engineering Specialist</b> (Braces collapses/traps)<br>
            <span class="checkbox-box"></span> <b>Forward Sentry Screen</b>
        </td>
    </tr>
    <tr>
        <td><b>Bláin</b></td>
        <td>Scout • Crossbow & Short Axe</td>
        <td>18</td>
        <td>[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; / 18 ]</td>
        <td><span class="checkbox-box"></span> Uninjured<br><span class="checkbox-box"></span> Moderate<br><span class="checkbox-box"></span> Severe</td>
        <td>
            <span class="checkbox-box"></span> <b>Forward Recon Scout</b> (Spots patrols ahead)<br>
            <span class="checkbox-box"></span> <b>Ranged Suppressing Fire</b> (Strips 1 Hate/round)
        </td>
    </tr>
    <tr>
        <td><b>Fáin</b></td>
        <td>Smith Apprentice • Iron Crowbars & Wedges</td>
        <td>18</td>
        <td>[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; / 18 ]</td>
        <td><span class="checkbox-box"></span> Uninjured<br><span class="checkbox-box"></span> Moderate<br><span class="checkbox-box"></span> Severe</td>
        <td>
            <span class="checkbox-box"></span> <b>Heavy Salvage Porter</b> (Hauls 300 lbs wargear)<br>
            <span class="checkbox-box"></span> <b>Siege Ballista Mechanic</b> (Assists Area 5)
        </td>
    </tr>
    <tr>
        <td><b>Bróga</b></td>
        <td>Crossbow Marksman • Sentry</td>
        <td>12</td>
        <td>[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; / 12 ]</td>
        <td><span class="checkbox-box"></span> Uninjured<br><span class="checkbox-box"></span> Moderate<br><span class="checkbox-box"></span> Severe</td>
        <td>
            <span class="checkbox-box"></span> <b>Gatehouse Guard</b> (Fortifies Upper Gatehouse)<br>
            <span class="checkbox-box"></span> <b>Ranged Overwatch</b>
        </td>
    </tr>
    <tr>
        <td><b>Austri</b></td>
        <td>Porter & Heavy Infantry</td>
        <td>18</td>
        <td>[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; / 18 ]</td>
        <td><span class="checkbox-box"></span> Uninjured<br><span class="checkbox-box"></span> Moderate<br><span class="checkbox-box"></span> Severe</td>
        <td>
            <span class="checkbox-box"></span> <b>Heavy Salvage Porter</b> (Hauls 300 lbs wargear)<br>
            <span class="checkbox-box"></span> <b>Rearguard Defender</b>
        </td>
    </tr>
    <tr>
        <td><b>Dolg</b></td>
        <td>Tower Shield & Broad Mattock</td>
        <td>18</td>
        <td>[ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; / 18 ]</td>
        <td><span class="checkbox-box"></span> Uninjured<br><span class="checkbox-box"></span> Moderate<br><span class="checkbox-box"></span> Severe</td>
        <td>
            <span class="checkbox-box"></span> <b>Rearguard Chokepoint Defense</b> (Delays swarms)<br>
            <span class="checkbox-box"></span> <b>Vanguard Shield-Wall</b>
        </td>
    </tr>
</table>

<div class="grid-2 avoid-break" style="margin-top:6px;">
    <div class="card">
        <div class="card-header">TACTICAL SQUAD DEPLOYMENT RULES</div>
        <div style="font-size:8pt; line-height:1.2;">
            1. <b>Gatehouse Garrison (2 Dwarves)</b>: Secures extraction redoubt. Adds +2 to final withdrawal and reduces Alert by -1 AP per Act.<br>
            2. <b>Salvage Porter Squad (2 Dwarves)</b>: Carries up to 600 lbs of recovered wargear/mithril without penalizing hero Fatigue.<br>
            3. <b>Shield-Wall Phalanx</b>: Absorbs 1 Piercing Blow per battle on behalf of a hero.<br>
            4. <b>Crossbow Suppressing Fire</b>: Strips 1 Hate point per round from enemy commanders on a successful War test.
        </div>
    </div>

    <div class="card">
        <div class="card-header">BAND MARCHING & COMBAT RESOLUTION</div>
        <div style="font-size:8pt; line-height:1.2;">
            • <b>Marching Test</b>: March leader tests <b>TRAVEL roll</b> or Band rolls <b>MANOEUVRE (TN 15)</b>. Failure: +1 Alert Point.<br>
            • <b>Band Clash in Combat</b>: Roll Feat Die + WAR (3d) vs TN 15. Each success inflicts 4 Endurance damage on enemy minion mob; each 6 icon inflicts a Piercing Blow.<br>
            • <b>Casualty Threshold</b>: If $\ge 4$ companions become wounded, the Band becomes <b>Weary</b> (-1d to all rolls).
        </div>
    </div>
</div>

</body>
</html>
"""

def build_dying_scribe_letter_html() -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>In-World Handout — The Dying Scribe's Basalt Slate</title>
<style>{COMMON_CSS}</style>
</head>
<body>

<h1>In-World Artifact Handout — Scribe Frár's Basalt Slate</h1>
<div class="subtitle">Recovered from the Twelfth Hall of the Poisoned Deeps • Preserved since 1980 T.A.</div>

<div class="rune-frame" style="margin-top:10px;">
    <div style="text-align:center; font-family:'Cinzel', serif; font-size:11pt; font-weight:bold; letter-spacing:0.1em; border-bottom:1px solid #333; padding-bottom:4px; margin-bottom:8px;">
        ▲ BASALT SLATE OF THE DWARVEN MARSHAL'S OFFICE ▲
    </div>

    <div class="cirth-inscription">
        ᚴᚪᛋᚪᛞ ᛞᚢᛗ • ᛒᚪᛚᚱᚩᚷ • ᚷᚪᛋᚻ • ᛗᚪᚱᛋᚻᚪᛚ ᚠᚪᛚᛚᛖᚾ<br>
        ᚴᛖᛁ • ᛋᛁᚴᛋᛏᛖᛖᚾᛏᚻ • ᚠᛁᚠᛏᚻ • ᛞᛖᛖᛈ • ᚷᚩᛒᛚᛁᚾᛋ • ᚢᛞᚢᚾ<br>
        ᚴᛁᚾᚷ • ᛋᛖᚾᛞ • ᚴᛖᛁ • ᚱᛖᛞᚩᚢᛒᛏ • ᛞᚢᚱᛁᚾ • ᚪᚾᚡᛁᛚ • ᛒᛚᚩᚩᛞ
    </div>

    <div style="margin-top:12px; padding:8px 12px; background:#fff; border:1px solid #555;">
        <h3 style="text-align:center; font-size:10pt; margin-bottom:6px;">RUNEMASTER TRANSLATION (LORE / CRAFT TEST SUCCESS)</h3>
        <p style="font-size:10pt; font-style:italic; line-height:1.4; margin:0; text-align:justify;">
            "The fire-demon’s breath fills the fourteenth hall... No helm nor cloth can stay the burning vapour. The Tunnel-guards stand fast, but their breath turns to ash where they stand. 
            <br><br>
            Hear me, King Durin! The Marshal of the Armies has fallen in the Sixteenth Hall of the Fifth Deep, and his Iron Key was torn from his breast by the fleeing goblin-swarms. The Lower Vault cannot be opened without it! 
            <br><br>
            Send the King’s Key from the Last Redoubt, or let the blood of Durin and the ancient Craft of Aulë command the adamant seal, else the Axe of the First Father is sealed in the dark forever..."
        </p>
        <div style="text-align:right; font-family:'Cinzel', serif; font-size:8pt; margin-top:6px; font-weight:bold;">
            — Frár, Scribe of the Royal Arsenal (Year 1980 of the Third Age)
        </div>
    </div>
</div>

<div class="card avoid-break" style="margin-top:12px;">
    <div class="card-header">LOREMASTER INSTRUCTIONS & SKILL REVELATIONS</div>
    <table style="margin:0;">
        <tr>
            <th>Skill Tested</th>
            <th>Required Check</th>
            <th>Lore & Clues Revealed to the Fellowship</th>
        </tr>
        <tr>
            <td><b>LORE / SCAN</b></td>
            <td><b>LORE roll / SCAN roll</b> (Favoured / +1d)</td>
            <td>Identifies the script as Royal Khuzdul Cirth. Confirms the <b>Marshal's Key</b> was carried into the deep warrens (connecting toward Goblin Village or Udûn tracks), while the <b>King's Key</b> was sealed in the Last Redoubt (Old Moria).</td>
        </tr>
        <tr>
            <td><b>CRAFT / HEALING</b></td>
            <td><b>CRAFT roll / HEALING roll (+1d)</b></td>
            <td>Recognizes the runic schematics sketched on the reverse of the slate: reveals the <b>King's Door uses a dual-interlocking cam mechanism</b> and can be bypassed via the <b>Blood of Durin ritual</b> (VALOUR roll) if the King's Key is missing.</td>
        </tr>
        <tr>
            <td><b>RIDDLE</b></td>
            <td><b>RIDDLE roll (+1d)</b></td>
            <td>Deciphers the marginal scratches at the bottom of the slab: Scribe Frár scratched the tumbler layout—3 left, 2 right, 1 center—granting +2d on the Turn 1 roll of the Lockbreaker Skill Endeavour.</td>
        </tr>
    </table>
</div>

</body>
</html>
"""

def build_node_map_html() -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Tactical Node Map — The Armouries of the Third Deep</title>
<style>{COMMON_CSS}</style>
</head>
<body>

<h1>Tactical Spatial Atlas & Elevation Node Map</h1>
<div class="subtitle">The Armouries of the Third Deep • Subterranean Levels 3A, 3B, 3C • Moria Delve Atlas</div>

<div class="ascii-map">
========================================================================================================
                                3-TIER ELEVATION CROSS-SECTION & FLOWCHART
========================================================================================================

 [LEVEL 3A: UPPER RESIDENCE]  <--- The Westward Drift from Thrym Thistlebeard's Haven
               │
               ▼
   +───────────────────────+
   │ 2. UPPER GATEHOUSE    │  <--- [EXPEDITION RALLY REDOUBT] (CRAFT Res 3 to fortify; -1 AP/Act)
   +───────────┬───────────+
               │ (Wide Granitic Stairway - March Test: TRAVEL roll / Band Manoeuvre TN 15)
               ▼
   +───────────────────────+
┌──┤ 1. MUSTERING-YARD     ├──┐  <--- [NEUTRAL GROUND] (Sentry Squad: 4 Orc Soldiers, 1 Udûn Sniffer)
│  +───────────┬───────────+  │       (STEALTH roll to slip past | BATTLE roll to ambush)
│ (West Flank) │ (Central)    │ (East Flank)
▼              ▼              ▼
+───────────+  +───────────+  +───────────+
│ 3. FIRST  │  │ 4. BROKEN │  │ 5. SECOND │ [LEVEL 3B: THE WEAPONS MANUFACTORY]
│   ARMOURY │  │    HALL   │  │   ARMOURY │ • Area 3: Scrap-traps (SCAN roll) | 12 Spearheads
│(Scrap-Trap│  │ (Morgoth  │  │ (Siege     │ • Area 4: VALOUR roll vs Dread | Last Redoubt Clue
│ Traps)    │  │  Idol)    │  │  Engines) │ • Area 5: Heavy Ballista (Craft Res 3; 24 Dmg to Troll!)
+───────────+  +─────┬─────+  +─────┬─────+
                     │              │
                     ▼              │
        +─────────────────────────+ │
        │ 7. THE POISONED HALLS   │◄┘  <--- [FATAL HAZARD] (Balrog Miasma: PROTECTION roll hourly)
        │ (12th & 14th Halls)     │         (Preserved Dwarf Knights | Scribe's Dying Slate recovered)
        +────────────┬────────────+
                     │
                     ▼
        +─────────────────────────+
        │ 8. THE UPPER ARMOURY    │  <--- [PRISTINE CACHE] (30 Masterwork Dwarf Weapons & Mail)
        +────────────┬────────────+
                     │
        ┌────────────┴──────────────────────────┐
        ▼                                       ▼
+─────────────────────────+           +─────────────────────────+
│ 6. HALL OF THE MAULER   │           │ 9. THE KING'S DOOR      │ [LEVEL 3C: THE ROYAL VAULT]
│ (Armoured Cave-Troll)   │           │ (Adamant Ithildin Seal) │ • Area 6: The Mauler (AL 10 Troll)
│ • Forward Riddle Duel   │           +────────────┬────────────+ • Area 9: Skill Endeavour Res 6
│ • Grimnar Catwalk Ambush│                        │              (Marshal's Key + Blood of Durin)
+───────────┬─────────────+                        ▼
                                      +─────────────────────────+
                                      │ 10. THE LOWER ARMOURY   │ <--- [THE GREATER HOARD]
                                      │ (The Grand Royal Vault) │ • 120 Treasure Points in Mithril
                                      │  [ DURIN'S AXE ]        │ • DURIN'S AXE (+4 Eye Awareness!)
                                      +─────────────────────────+

========================================================================================================
CONNECTING SUBTERRANEAN PATHWAYS:
• Eastern Fissure: Descends 2 miles to Goblin Village (Lower Moria Orc Warrens).
• South-Eastern Gallery: Connects to the Ledge of Woe & The Wailing Stairs descending to the Mines.
========================================================================================================
</div>

<div class="grid-2 avoid-break" style="margin-top:6px;">
    <div class="card">
        <div class="card-header">CRITICAL TACTICAL BYPASSES & CHOKEPOINTS</div>
        <div style="font-size:8pt; line-height:1.25;">
            • <b>The Flue Bypass</b>: A narrow ventilation shaft connects Area 2 directly to Area 5, bypassing the central Mustering-Yard entirely (requires <b>EXPLORE roll</b>).<br>
            • <b>The Catwalk Overwatch</b>: High stone walkways run above Area 6 and Area 1, accessible via stone rungs. Perfect for companion crossbow marksmen (Bláin & Bróga).<br>
            • <b>The Keystone Collapse Point</b>: Over Area 2, an unstable archway can be rigged to collapse during the final withdrawal, sealing the gallery against Malech's shock-troops.
        </div>
    </div>

    <div class="card">
        <div class="card-header">EXTRACTION & WITHDRAWAL CHECKLIST</div>
        <div style="font-size:8pt; line-height:1.25;">
            1. <span class="checkbox-box"></span> Secure Upper Gatehouse with 2 Dwarves in Act I.<br>
            2. <span class="checkbox-box"></span> Recover Scribe Slate & Marshal's Key in Act II.<br>
            3. <span class="checkbox-box"></span> Prime Heavy Ballista in Area 5 for troll defense.<br>
            4. <span class="checkbox-box"></span> Claim Durin's Axe (<b>Eye Awareness +4</b>) in Act III.<br>
            5. <span class="checkbox-box"></span> Form Companion Shield-Wall and extract 600 lbs wargear along the Westward Drift to Thistlebeard Haven!
        </div>
    </div>
</div>

</body>
</html>
"""

# =============================================================================
# RENDERING PIPELINE
# =============================================================================

def render_all():
    HTML_DIR.mkdir(parents=True, exist_ok=True)
    PDF_DIR.mkdir(parents=True, exist_ok=True)

    handouts = [
        ("gm_cheat_sheet", build_gm_cheat_sheet_html),
        ("band_worksheet", build_band_worksheet_html),
        ("dying_scribe_letter", build_dying_scribe_letter_html),
        ("node_map", build_node_map_html),
    ]

    engine = find_pdf_engine()
    print(f"[*] PDF Engine detected: {engine}")

    generated_html_files = []
    generated_pdf_files = []

    for name, builder in handouts:
        html_content = builder()
        html_path = HTML_DIR / f"{name}.html"
        pdf_path = PDF_DIR / f"{name}.pdf"

        html_path.write_text(html_content, encoding="utf-8")
        generated_html_files.append(html_path)
        print(f"[+] HTML written: {html_path.relative_to(BASE_DIR)}")

        if engine:
            cmd = [
                str(engine),
                "--headless",
                "--disable-gpu",
                "--no-pdf-header-footer",
                f"--print-to-pdf={pdf_path}",
                str(html_path)
            ]
            res = subprocess.run(cmd, capture_output=True, text=True)
            if res.returncode == 0 and pdf_path.exists():
                generated_pdf_files.append(pdf_path)
                print(f"[OK] PDF rendered: {pdf_path.relative_to(BASE_DIR)} ({pdf_path.stat().st_size} bytes)")
            else:
                print(f"[!] PDF generation failed for {name}: {res.stderr}")

    # Build unified complete bundle
    bundle_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>All Handouts Complete Bundle — The Armouries of the Third Deep</title>
<style>
{COMMON_CSS}
</style>
</head>
<body>
{build_gm_cheat_sheet_html().split('<body>')[1].split('</body>')[0]}
<div class="page-break"></div>
{build_band_worksheet_html().split('<body>')[1].split('</body>')[0]}
<div class="page-break"></div>
{build_dying_scribe_letter_html().split('<body>')[1].split('</body>')[0]}
<div class="page-break"></div>
{build_node_map_html().split('<body>')[1].split('</body>')[0]}
</body>
</html>
"""
    bundle_html_path = HTML_DIR / "handouts_complete_bundle.html"
    bundle_pdf_path = PDF_DIR / "handouts_complete_bundle.pdf"

    bundle_html_path.write_text(bundle_html, encoding="utf-8")
    print(f"[+] Complete Bundle HTML: {bundle_html_path.relative_to(BASE_DIR)}")

    if engine:
        cmd = [
            str(engine),
            "--headless",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={bundle_pdf_path}",
            str(bundle_html_path)
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0 and bundle_pdf_path.exists():
            print(f"[OK] Complete Bundle PDF rendered: {bundle_pdf_path.relative_to(BASE_DIR)} ({bundle_pdf_path.stat().st_size} bytes)")

    print("\n=======================================================")
    print("[SUCCESS] ALL HANDOUTS RENDERED SUCCESSFULLY!")
    print(f"   HTML Folder: {HTML_DIR}")
    print(f"   PDF Folder : {PDF_DIR}")
    print("=======================================================")

if __name__ == "__main__":
    render_all()
