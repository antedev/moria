#!/usr/bin/env python3
"""
build_master_document.py — Master Adventure Book & A4 PDF Generator
====================================================================
Compiles all 7 chapters and 4 handout appendices of 'The Armouries of the Third Deep'
into a single, comprehensive Master Adventure Document (Markdown, HTML, and A4 PDF).

Features:
  - Unified Master Markdown: 'armouries_of_the_third_deep_master.md'
  - Print-Ready Master HTML: 'print/armouries_of_the_third_deep_master.html'
  - High-Resolution A4 PDF:  'print/armouries_of_the_third_deep_master.pdf'
  - Elegant Tolkien/Dwarven typography (Cinzel, Cormorant Garamond, JetBrains Mono)
  - A4 Paged Media with running headers, footers, page-break controls
  - Dedicated styling for Swedish read-aloud boxes, stat blocks, ASCII maps, and tables
"""

import os
import re
import sys
import subprocess
from pathlib import Path
from typing import List, Tuple, Optional
import markdown2

BASE_DIR = Path(__file__).resolve().parent.parent
PRINT_DIR = BASE_DIR / "print"

CHAPTER_FILES: List[Tuple[str, str, Path]] = [
    ("Chapter 1", "Campaign Context & Staging", BASE_DIR / "01_campaign_context.md"),
    ("Chapter 2", "Squad Management & Band Operations", BASE_DIR / "02_band_mechanics.md"),
    ("Chapter 3", "Operational Mechanics & Hazards", BASE_DIR / "03_operational_mechanics.md"),
    ("Chapter 4", "Spatial Atlas & Keyed Locations 1–10", BASE_DIR / "04_keyed_locations.md"),
    ("Chapter 5", "Adversaries, Fell Abilities & Hazards", BASE_DIR / "05_adversaries_and_hazards.md"),
    ("Chapter 6", "Relics, Rewards & Scavenge Tables", BASE_DIR / "06_relics_and_rewards.md"),
    ("Chapter 7", "GM Playbook, Scene Pacing & Prep", BASE_DIR / "07_gm_playbook_and_pacing.md"),
]

APPENDIX_FILES: List[Tuple[str, str, Path]] = [
    ("Appendix A", "Operational Node Map & Schematic", BASE_DIR / "handouts" / "node_map.md"),
    ("Appendix B", "1-Page Rapid GM Cheat Sheet", BASE_DIR / "handouts" / "gm_cheat_sheet.md"),
    ("Appendix C", "Dwarf Vanguard Band Worksheet", BASE_DIR / "handouts" / "band_worksheet.md"),
    ("Appendix D", "Player Handout: Dying Scribe's Slate", BASE_DIR / "handouts" / "dying_scribe_letter.md"),
]

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


def generate_master_markdown() -> str:
    """Combines all chapters and appendices into a single unified master markdown file."""
    parts: List[str] = []

    # Title & Frontmatter
    parts.append("""# THE ARMOURIES OF THE THIRD DEEP
## A Masterclass Tabletop Delve for *The One Ring 2e* (*Moria: Through the Doors of Durin*)
### Complete Master Campaign Volume & Reference Atlas

---

> *"The world was young, the mountains green,*  
> *No stain yet on the Moon was seen,*  
> *No words were laid on stream or stone*  
> *When Durin woke and walked alone.*  
> *A king he was on carven throne*  
> *In many-pillared halls of stone,*  
> *With golden roof and silver floor,*  
> *And runes of power upon the door."*  
> — **The Song of Durin**

---

## Table of Contents & Master Volume Contents

* **Chapter 1: Campaign Context & Staging**
  * Historical Setting (2989 TA), Geopolitical Stakes, Lord Balin's Directives & Veteran Player-Heroes
* **Chapter 2: Squad Management, Marching & Band Operations**
  * The 8 Companion Specialists, Marching Formations, Band Dispositions & The 5-Tier Injury System
* **Chapter 3: Operational Mechanics, Alert Tracker & Environmental Hazards**
  * The 4-Stage Alert Ladder, Noise Points, Strategic Eye Awareness & Balrog Toxic Gas (*Breath of the Pit*)
* **Chapter 4: Keyed Locations & Spatial Atlas (Locations 1–10)**
  * Complete 10-Room Delve Atlas, Sensory Profiles, Swedish Read-Aloud Texts (*Högläsningstexter*), and TOR 2e Skill Tests
* **Chapter 5: Adversaries, Foes & Hazards**
  * Complete Mathematical Stat Blocks for The Mauler (AL 10 Troll), Grimnar the Disgraced (AL 6 Great Orc), and Garrison Ranks
* **Chapter 6: Relics, Rewards, Scavenge Tables & Royal Vault Loot**
  * Durin's Axe (Royal Artifact), Masterwork Tunnel-Guard Relics, Greater Hoard of Khazad-dûm & D66 Scavenge Table
* **Chapter 7: GM Playbook, Scene Pacing & Session Preparation**
  * Three-Act Session Playbook, Revelation Crisis Triggers, Table Cheat Sheets & Dynamic Encounter Flowcharts
* **Appendices: Tabletop Play Aids & Handouts**
  * **Appendix A**: Operational Node Map & Tactical Schematic
  * **Appendix B**: 1-Page Rapid GM Cheat Sheet & Operational Matrix
  * **Appendix C**: Dwarf Vanguard Band Worksheet & Tracking Log
  * **Appendix D**: In-World Player Handout — The Dying Scribe's Slate

---
""")

    # Append Chapters
    for label, title, path in CHAPTER_FILES:
        if path.exists():
            text = path.read_text(encoding="utf-8")
            parts.append(f"\n\n<!-- PAGE BREAK: {label} -->\n\n---\n\n")
            parts.append(text)
        else:
            print(f"[!] Warning: File missing: {path}")

    # Append Appendices
    parts.append("\n\n<!-- PAGE BREAK: APPENDICES -->\n\n---\n\n# APPENDICES: TABLETOP PLAY AIDS & HANDOUTS\n\n")
    for label, title, path in APPENDIX_FILES:
        if path.exists():
            text = path.read_text(encoding="utf-8")
            parts.append(f"\n\n<!-- PAGE BREAK: {label} -->\n\n---\n\n## {label}: {title}\n\n")
            parts.append(text)
        else:
            print(f"[!] Warning: File missing: {path}")

    return "\n".join(parts)


def build_master_html(md_content: str) -> str:
    """Transforms master markdown into publication-quality, A4 print-styled HTML."""

    # Convert markdown to HTML using markdown2
    extras = [
        "tables",
        "fenced-code-blocks",
        "header-ids",
        "strike",
        "smarty-pants",
        "cuddled-lists",
    ]
    raw_html = markdown2.markdown(md_content, extras=extras)

    # Post-process HTML for styling
    # 1. Swedish read-aloud boxes
    def replace_read_aloud(match):
        content = match.group(1)
        return f"""
<div class="boxed-read-aloud">
    <div class="read-aloud-badge">ᚱᚢᚾ HÖGLÄSNINGSTEXT (SWEDISH READ-ALOUD)</div>
    <div class="read-aloud-body">{content}</div>
</div>
"""
    raw_html = re.sub(r"<blockquote>\s*<p>\s*<em>(.*?)</em>\s*</p>\s*</blockquote>", replace_read_aloud, raw_html, flags=re.DOTALL)
    raw_html = re.sub(r"<blockquote>(.*?)</blockquote>", r'<div class="styled-quote">\1</div>', raw_html, flags=re.DOTALL)

    # 2. Add page break divs before chapters
    raw_html = re.sub(r"<!-- PAGE BREAK: (.*?) -->", r'<div class="page-break" data-chapter="\1"></div>', raw_html)

    # 3. Enhance pre/code blocks for ASCII maps
    raw_html = re.sub(r"<pre><code>", '<div class="ascii-card"><pre><code>', raw_html)
    raw_html = re.sub(r"</code></pre>", "</code></pre></div>", raw_html)

    # Build complete HTML Document
    html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>The Armouries of the Third Deep — Master Campaign Volume</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;800;900&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

@page {{
    size: A4 portrait;
    margin: 14mm 14mm 16mm 14mm;
    @top-center {{
        content: "THE ARMOURIES OF THE THIRD DEEP — THE ONE RING 2E";
        font-family: 'Cinzel', serif;
        font-size: 7pt;
        letter-spacing: 0.15em;
        color: #777;
        border-bottom: 0.5pt solid #ccc;
        padding-bottom: 3mm;
    }}
    @bottom-left {{
        content: "Moria: Through the Doors of Durin";
        font-family: 'Cinzel', serif;
        font-size: 7pt;
        color: #777;
    }}
    @bottom-right {{
        content: "Page " counter(page);
        font-family: 'Cinzel', serif;
        font-weight: 700;
        font-size: 7.5pt;
        color: #333;
    }}
}}

@page :first {{
    margin-top: 20mm;
    @top-center {{ content: ""; border: none; }}
}}

*, *:before, *:after {{
    box-sizing: border-box;
}}

body {{
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 9.5pt;
    line-height: 1.35;
    color: #1a1a1a;
    background-color: #ffffff;
    margin: 0;
    padding: 0;
}}

/* Typography Hierarchy */
h1 {{
    font-family: 'Cinzel', serif;
    font-size: 15pt;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #000000;
    border-bottom: 1.5pt solid #222;
    padding-bottom: 3pt;
    margin-top: 16pt;
    margin-bottom: 6pt;
    page-break-after: avoid;
    break-after: avoid;
}}

h2 {{
    font-family: 'Cinzel', serif;
    font-size: 12pt;
    font-weight: 700;
    letter-spacing: 0.05em;
    color: #1a1a1a;
    border-bottom: 0.75pt solid #666;
    padding-bottom: 2pt;
    margin-top: 12pt;
    margin-bottom: 5pt;
    page-break-after: avoid;
    break-after: avoid;
}}

h3 {{
    font-family: 'Cinzel', serif;
    font-size: 10pt;
    font-weight: 700;
    color: #222;
    margin-top: 9pt;
    margin-bottom: 3pt;
    page-break-after: avoid;
    break-after: avoid;
}}

h4 {{
    font-family: 'Cinzel', serif;
    font-size: 8.8pt;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    color: #333;
    margin-top: 7pt;
    margin-bottom: 2pt;
    page-break-after: avoid;
    break-after: avoid;
}}

p {{
    margin-top: 0;
    margin-bottom: 4.5pt;
    text-align: justify;
}}

strong {{
    font-weight: 700;
    color: #000;
}}

em {{
    font-style: italic;
}}

hr {{
    border: none;
    border-top: 0.75pt solid #bbb;
    margin: 8pt 0;
}}

/* Lists */
ul, ol {{
    margin-top: 2pt;
    margin-bottom: 5pt;
    padding-left: 14pt;
}}

li {{
    margin-bottom: 1.5pt;
}}

/* Tables */
table {{
    width: 100%;
    border-collapse: collapse;
    margin-top: 5pt;
    margin-bottom: 7pt;
    font-size: 7.8pt;
    line-height: 1.22;
    page-break-inside: avoid;
    break-inside: avoid;
}}

th {{
    font-family: 'Cinzel', serif;
    font-weight: 700;
    font-size: 7.8pt;
    letter-spacing: 0.03em;
    background-color: #222;
    color: #fff;
    padding: 3pt 4.5pt;
    text-align: left;
    border: 0.5pt solid #222;
}}

td {{
    padding: 2.5pt 4pt;
    border: 0.5pt solid #bbb;
    vertical-align: top;
}}

tr:nth-child(even) {{
    background-color: #f7f7f7;
}}

/* Boxed Read-Aloud (Högläsning) */
.boxed-read-aloud {{
    background-color: #f9f8f5;
    border: 1pt solid #8c7b64;
    border-left: 3.5pt solid #5a4a32;
    border-radius: 2pt;
    padding: 5pt 8pt;
    margin-top: 6pt;
    margin-bottom: 7pt;
    page-break-inside: avoid;
    break-inside: avoid;
    box-shadow: 0 1pt 2pt rgba(0,0,0,0.05);
}}

.read-aloud-badge {{
    font-family: 'Cinzel', serif;
    font-size: 7pt;
    font-weight: 800;
    letter-spacing: 0.08em;
    color: #5a4a32;
    border-bottom: 0.5pt dashed #aa9980;
    padding-bottom: 1.5pt;
    margin-bottom: 3.5pt;
}}

.read-aloud-body {{
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 9.2pt;
    font-style: italic;
    color: #222;
    line-height: 1.32;
}}

/* Quotes */
.styled-quote {{
    background-color: #fafafa;
    border-left: 2pt solid #555;
    padding: 3.5pt 7pt;
    margin: 5pt 0;
    font-style: italic;
    page-break-inside: avoid;
    break-inside: avoid;
}}

/* ASCII & Stat Box Cards */
.ascii-card {{
    background-color: #fafafa;
    border: 0.75pt solid #333;
    border-radius: 2pt;
    margin: 5pt 0 7pt 0;
    padding: 3.5pt 5pt;
    page-break-inside: avoid;
    break-inside: avoid;
}}

pre {{
    margin: 0;
    font-family: 'JetBrains Mono', Consolas, monospace;
    font-size: 6.5pt;
    line-height: 1.15;
    color: #111;
    white-space: pre-wrap;
    word-break: break-all;
}}

code {{
    font-family: 'JetBrains Mono', Consolas, monospace;
    font-size: 7.8pt;
    background-color: #eee;
    padding: 0.5pt 2pt;
    border-radius: 1.5pt;
}}

pre code {{
    background-color: transparent;
    padding: 0;
    font-size: 6.5pt;
}}

/* Page Break Controls */
.page-break {{
    page-break-before: always;
    break-before: page;
}}

@media print {{
    body {{
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
    }}
}}
</style>
</head>
<body>

{raw_html}

</body>
</html>
"""
    return html_doc


def main():
    PRINT_DIR.mkdir(parents=True, exist_ok=True)
    master_md_path = BASE_DIR / "armouries_of_the_third_deep_master.md"
    master_html_path = PRINT_DIR / "armouries_of_the_third_deep_master.html"
    master_pdf_path = PRINT_DIR / "armouries_of_the_third_deep_master.pdf"

    print("=================================================================")
    print(" BUILD MASTER ADVENTURE BOOK & A4 PDF GENERATOR")
    print("=================================================================")

    # 1. Generate Master Markdown Document
    print("[*] Assembling all 7 Chapters and 4 Appendices into master Markdown...")
    master_md = generate_master_markdown()
    master_md_path.write_text(master_md, encoding="utf-8")
    print(f"[+] Master Markdown generated: {master_md_path.name} ({len(master_md.splitlines())} lines, {len(master_md)} bytes)")

    # 2. Generate Master HTML Document
    print("[*] Compiling A4 print-optimized HTML publication...")
    master_html = build_master_html(master_md)
    master_html_path.write_text(master_html, encoding="utf-8")
    print(f"[+] Master HTML generated: {master_html_path.relative_to(BASE_DIR)} ({len(master_html)} bytes)")

    # 3. Render A4 PDF via Headless Chromium / Edge
    engine = find_pdf_engine()
    if engine:
        print(f"[*] PDF Engine detected: {engine}")
        print(f"[*] Rendering A4 Master PDF to: {master_pdf_path.relative_to(BASE_DIR)}...")
        cmd = [
            str(engine),
            "--headless",
            "--disable-gpu",
            "--no-sandbox",
            "--run-all-compositor-stages-before-draw",
            "--no-pdf-header-footer",
            f"--print-to-pdf={master_pdf_path}",
            str(master_html_path.resolve()),
        ]
        try:
            res = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            if master_pdf_path.exists() and master_pdf_path.stat().st_size > 0:
                print(f"[OK] Master A4 PDF generated: {master_pdf_path.name} ({master_pdf_path.stat().st_size:,} bytes)")
            else:
                print(f"[!] PDF generation failed: {res.stderr}")
        except subprocess.TimeoutExpired:
            print("[!] PDF generation timed out (exceeded 30 seconds).")
    else:
        print("[!] No Chromium/Edge PDF engine found. Master HTML is ready for manual browser print.")

    print("=================================================================")
    print("[SUCCESS] MASTER PUBLICATION READY!")
    print(f"   Markdown : {master_md_path}")
    print(f"   HTML     : {master_html_path}")
    print(f"   PDF (A4) : {master_pdf_path}")
    print("=================================================================")


if __name__ == "__main__":
    main()
