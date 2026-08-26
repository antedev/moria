# Survey Report: Build Pipeline, Scripts, Master Document & Repository Inventory
**Agent**: `survey_explorer_3`  
**Date**: 2026-08-26  
**Scope**: Repository structure, Python build scripts, master document assembly, presentation assets, dependencies, and R5 verification criteria in `c:/Users/ante/Documents/github/Moria/adventures/armouries_of_the_third_deep/`.

---

## Executive Summary

This investigation provides a comprehensive audit of the build automation pipeline, Python scripts, master document assembly, asset synchronization status, and complete file inventory for *The Armouries of the Third Deep* adventure suite for *The One Ring 2e* (TOR 2e).

Key findings:
1. **Build Scripts Architecture**:
   - `scripts/build_master_document.py` dynamically concatenates the 7 core chapter markdown files (`01` through `07`) and 4 appendix handout files (`handouts/*.md`), converts them via `markdown2` to publication-styled HTML (`print/armouries_of_the_third_deep_master.html`), and compiles A4 PDF (`print/armouries_of_the_third_deep_master.pdf`) via headless Microsoft Edge/Chrome.
   - `scripts/render_handouts.py` generates individual and bundled HTML and PDF handouts. **Critical Architectural Finding**: `render_handouts.py` contains hardcoded HTML templates rather than parsing `handouts/*.md`. Edits to `handouts/*.md` do NOT automatically propagate to `handouts/html/` or `handouts/pdf/` unless `scripts/render_handouts.py` is updated or refactored to parse markdown. Furthermore, the requirement mentions `scripts/build_handouts.py`, but the script in the repository is named `scripts/render_handouts.py`.
2. **Synchronization Status**:
   - The master document (`armouries_of_the_third_deep_master.md`), HTML files (`print/*.html`, `handouts/html/*.html`), and PDF files currently reflect the previous refactoring state.
   - They currently contain non-canonical "Daunted" conditions (5 instances in master md, 5 in master html, 4 in quickstart md), hardcoded pregen TN listings (`Torvir 13/15`, `Einar 14/15`, `Khoril 16`), prescriptive character action text, and spoiler-filled boxed read-aloud text.
   - They are **out of date** with respect to the new R1–R5 directives and will require full compilation after chapter and handout revisions are completed.
3. **Repository Inventory**:
   - 17 source markdown documents (7 full chapters, 4 handouts, 6 quickstart files).
   - 1 compiled master markdown document (`armouries_of_the_third_deep_master.md`).
   - 4 project/test documentation files (`PROJECT.md`, `README.md`, `TEST_INFRA.md`, `TEST_READY.md`).
   - 4 Python scripts in `scripts/`.
   - 4 Python test files in `tests/`.
   - 6 HTML presentation assets (1 master in `print/`, 5 in `handouts/html/`).
   - 6 PDF publication assets (1 master in `print/`, 5 in `handouts/pdf/`).
4. **Build Execution Dependencies & R5 Criteria**:
   - Python 3.10+ with `markdown2` package.
   - Headless Edge/Chrome browser for PDF compilation.
   - Full 3-layer synchronization (modular chapters -> master markdown -> HTML/PDF presentation assets) and test suite alignment.

---

## 1. Audit of Python Build Scripts in `scripts/`

The repository contains four Python files in `scripts/`:

```
scripts/
├── __init__.py
├── build_master_document.py
├── render_handouts.py
└── validate_module_suite.py
```

### 1.1 `scripts/build_master_document.py` (494 lines)

#### Purpose
Compiles all 7 adventure chapters and 4 handout appendices into:
1. Unified Master Markdown: `armouries_of_the_third_deep_master.md`
2. Print-Ready Master HTML: `print/armouries_of_the_third_deep_master.html`
3. High-Resolution A4 PDF: `print/armouries_of_the_third_deep_master.pdf`

#### Assembly Mechanism
1. **Source File Mapping**:
   - `CHAPTER_FILES`:
     - Chapter 1: `01_campaign_context.md`
     - Chapter 2: `02_band_mechanics.md`
     - Chapter 3: `03_operational_mechanics.md`
     - Chapter 4: `04_keyed_locations.md`
     - Chapter 5: `05_adversaries_and_hazards.md`
     - Chapter 6: `06_relics_and_rewards.md`
     - Chapter 7: `07_gm_playbook_and_pacing.md`
   - `APPENDIX_FILES`:
     - Appendix A: `handouts/node_map.md`
     - Appendix B: `handouts/gm_cheat_sheet.md`
     - Appendix C: `handouts/band_worksheet.md`
     - Appendix D: `handouts/dying_scribe_letter.md`
2. **Master Markdown Assembly (`generate_master_markdown()`)**:
   - Inserts fixed title block, *The Song of Durin* epigraph, and Master Table of Contents.
   - Appends each chapter separated by `\n\n<!-- PAGE BREAK: {label} -->\n\n---\n\n`.
   - Appends `# APPENDICES: TABLETOP PLAY AIDS & HANDOUTS` banner.
   - Appends each appendix separated by `\n\n<!-- PAGE BREAK: {label} -->\n\n---\n\n## {label}: {title}\n\n`.
   - Writes to `armouries_of_the_third_deep_master.md` in UTF-8.
3. **HTML Compilation & Post-Processing (`build_master_html(md_content)`)**:
   - Uses `markdown2.markdown()` with extras: `tables`, `fenced-code-blocks`, `header-ids`, `strike`, `smarty-pants`, `cuddled-lists`.
   - Regex transformations:
     - Converts Swedish read-aloud italicized blockquotes (`<blockquote>\s*<p>\s*<em>(.*?)</em>\s*</p>\s*</blockquote>`) into `<div class="boxed-read-aloud">` containing `<div class="read-aloud-badge">ᚱᚢᚾ HÖGLÄSNINGSTEXT (SWEDISH READ-ALOUD)</div>` and `<div class="read-aloud-body">`.
     - Converts standard blockquotes into `<div class="styled-quote">`.
     - Replaces `<!-- PAGE BREAK: ... -->` comments with `<div class="page-break" data-chapter="..."></div>`.
     - Wraps `<pre><code>` blocks into `<div class="ascii-card"><pre><code>` for clean map/stat card rendering.
   - Injects comprehensive print styling:
     - `@page { size: A4 portrait; margin: 14mm 14mm 16mm 14mm; @top-center { ... } @bottom-left { ... } @bottom-right { ... } }`
     - Font imports: *Cinzel* (headers/runes), *Cormorant Garamond* (body serif), *JetBrains Mono* (ASCII maps/code).
     - Grayscale print-optimized tables, avoiding orphan page breaks (`page-break-inside: avoid;`).
   - Writes to `print/armouries_of_the_third_deep_master.html`.
4. **PDF Compilation (`find_pdf_engine()`)**:
   - Scans for Edge/Chrome binaries at standard Windows installation paths:
     - `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe`
     - `C:\Program Files\Microsoft\Edge\Application\msedge.exe`
     - `C:\Program Files\Google\Chrome\Application\chrome.exe`
   - Executes headless command:
     `[engine, "--headless", "--disable-gpu", "--run-all-compositor-stages-before-draw", "--no-pdf-header-footer", f"--print-to-pdf={pdf_path}", str(html_path)]`
   - Writes to `print/armouries_of_the_third_deep_master.pdf`.

---

### 1.2 `scripts/render_handouts.py` (946 lines)

#### Purpose & Discrepancy Note
- Referenced in `ORIGINAL_REQUEST.md` as `scripts/build_handouts.py`, but present in the codebase as `scripts/render_handouts.py`.
- Generates 5 standalone HTML files in `handouts/html/` and 5 PDF files in `handouts/pdf/`.

#### Critical Architectural Analysis
Unlike `build_master_document.py`, `render_handouts.py` **does NOT parse the markdown files in `handouts/*.md`**.
Instead, it contains dedicated Python functions returning full HTML string templates:
1. `build_gm_cheat_sheet_html()` -> `handouts/html/gm_cheat_sheet.html`, `handouts/pdf/gm_cheat_sheet.pdf`
2. `build_band_worksheet_html()` -> `handouts/html/band_worksheet.html`, `handouts/pdf/band_worksheet.pdf`
3. `build_dying_scribe_letter_html()` -> `handouts/html/dying_scribe_letter.html`, `handouts/pdf/dying_scribe_letter.pdf`
4. `build_node_map_html()` -> `handouts/html/node_map.html`, `handouts/pdf/node_map.pdf`
5. Complete Bundle concatenation -> `handouts/html/handouts_complete_bundle.html`, `handouts/pdf/handouts_complete_bundle.pdf`

**Impact for R1–R5**:
- Lines 296–334, 736–748, and 784–832 of `render_handouts.py` contain hardcoded pregen Target Numbers (`STR TN 13/14`, `HRT TN 18/17/16`, `WIT TN 15/16`, `Torvir 15, Einar 15, Khoril 16`, `Scan WIT TN 15`, `Valour HRT TN 18`, `Protection STR TN 13`).
- To achieve 100% compliance across all generated handout assets, `scripts/render_handouts.py` must either:
  a. Have its internal HTML templates updated to match the revised TOR 2e notation (removing pregen TNs, neutral GM format).
  b. Or be refactored to dynamically render the `handouts/*.md` markdown files via `markdown2` like `build_master_document.py` does.
- Creating an alias or forwarding script `scripts/build_handouts.py -> scripts/render_handouts.py` is recommended to fulfill exact CLI expectations.

---

### 1.3 `scripts/validate_module_suite.py` (830 lines)

#### Purpose
Static and semantic validation tool checking all markdown documents across 4 tiers:
- **Tier 1 (Feature Coverage)**: Zero arbitrary hero TNs, official 18 skills, trait integrity, purged mechanics, formal skill endeavours, adversary stats, relic properties.
- **Tier 2 (Boundary & Corner Cases)**: Case-insensitive rogue TN regexes, D&D 5e phrasing leaks, syntax integrity.
- **Tier 3 (Cross-File Consistency)**: Consistency of hero attributes, Band stats, adversary endurance, keyed location names.
- **Tier 4 (Real-World Usability)**: Table readiness, node map completeness, alert ladder tiers.

#### Alignment with New Requirements
- Currently checks that hero TNs match the pre-gens (e.g. `Torvir: STR 13/HRT 18/WIT 15`).
- Must be updated to align with R1–R4:
  - Assert 0 occurrences of "Daunted" across all files.
  - Check that general skill test blocks do NOT hardcode pre-gen attribute numbers.
  - Verify neutral player agency and clean boxed read-aloud descriptions.

---

## 2. Current Master Document & Asset Synchronization Status

| Asset / File | File Type | Current Sync Status | Detected Deficiencies Relative to R1–R5 |
| :--- | :---: | :---: | :--- |
| `armouries_of_the_third_deep_master.md` | Master Markdown | **OUT OF DATE** | Contains 5 instances of "Daunted" condition (lines 1520, 1525, 1534, 2113, 2284); contains 200+ instances of hardcoded pregen TNs (`Torvir 13/15`, `Einar 14/15`, `Khoril 16`); prescriptive PC actions; spoilers in boxed read-aloud text. |
| `print/armouries_of_the_third_deep_master.html` | Master HTML | **OUT OF DATE** | Generated from previous master MD; contains 5 instances of "Daunted" condition (lines 2195, 2203, 2220, 3100, 3307); hardcoded pregen TNs. |
| `print/armouries_of_the_third_deep_master.pdf` | Master PDF | **OUT OF DATE** | Rendered from previous master HTML; contains old text and stat blocks. |
| `handouts/html/*.html` (5 files) | Handout HTML | **OUT OF DATE** | Generated from `render_handouts.py` HTML templates with hardcoded pregen TNs. |
| `handouts/pdf/*.pdf` (5 files) | Handout PDF | **OUT OF DATE** | Rendered from previous handout HTML files. |
| `quickstart/*.md` (6 files) | Quickstart MD | **OUT OF DATE** | `quickstart/02_keyed_locations.md` contains 4 instances of "Daunted" (lines 210, 215, 224, 452) and hardcoded pregen TNs. |

### Assembly Dependency Flow

```
[Modular Chapters: 01_*.md to 07_*.md]  ──┐
                                          ├──> scripts/build_master_document.py ──> armouries_of_the_third_deep_master.md
[Handouts Markdown: handouts/*.md]     ──┘                                       └──> print/armouries_of_the_third_deep_master.html
                                                                                     └──> print/armouries_of_the_third_deep_master.pdf

[Handout Templates / handouts/*.md]    ───────> scripts/render_handouts.py       ──> handouts/html/*.html
                                                                                 └──> handouts/pdf/*.pdf

[Quickstart: quickstart/00_*.md to 05_*.md] ─ (Standalone condensed edition)
```

---

## 3. Complete Repository File Inventory

### 3.1 Core Modular Adventure Chapters (Root Directory)
| Filename | Lines | Bytes | Description |
| :--- | :---: | :---: | :--- |
| `01_campaign_context.md` | 277 | 28,857 | Chapter 1: Campaign Context, 2989 TA Setting & Pre-gen Character Sheets |
| `02_band_mechanics.md` | 370 | 25,505 | Chapter 2: Squad Management, Band Dispositions & Tactical Squad Roles |
| `03_operational_mechanics.md` | 278 | 20,588 | Chapter 3: Operational Mechanics, Alert Ladder & Balrog Miasma |
| `04_keyed_locations.md` | 1,189 | 103,832 | Chapter 4: Keyed Locations 1–10 & Spatial Atlas |
| `05_adversaries_and_hazards.md` | 511 | 42,277 | Chapter 5: Adversaries, Foes & Mathematical Stat Blocks |
| `06_relics_and_rewards.md` | 572 | 43,656 | Chapter 6: Relics, Rewards, Durin's Axe & D66 Scavenge Tables |
| `07_gm_playbook_and_pacing.md` | 557 | 44,033 | Chapter 7: GM Playbook, Scene Pacing & Session Preparation |

### 3.2 Handouts (`handouts/`)
| Filename | Lines | Bytes | Description |
| :--- | :---: | :---: | :--- |
| `handouts/node_map.md` | 382 | 29,266 | Appendix A: Operational Node Map & Tactical Schematic |
| `handouts/gm_cheat_sheet.md` | 266 | 17,068 | Appendix B: 1-Page Rapid GM Cheat Sheet & Operational Matrix |
| `handouts/band_worksheet.md` | 224 | 13,296 | Appendix C: Dwarf Vanguard Band Worksheet & Tracking Log |
| `handouts/dying_scribe_letter.md` | 135 | 9,770 | Appendix D: In-World Player Handout (Dying Scribe's Basalt Slate) |

### 3.3 Quickstart Edition (`quickstart/`)
| Filename | Lines | Bytes | Description |
| :--- | :---: | :---: | :--- |
| `quickstart/00_overview_and_background.md` | 215 | 15,909 | Condensed Overview, Staging & Pre-gens |
| `quickstart/01_delve_mechanics_and_alert_system.md` | 177 | 11,826 | Condensed Delve Rules & Alert Tracker |
| `quickstart/02_keyed_locations.md` | 514 | 41,406 | Condensed Keyed Locations 1–10 |
| `quickstart/03_adversaries_and_hazards.md` | 224 | 16,213 | Condensed Adversary Stat Blocks & Bestiary |
| `quickstart/04_loot_relics_and_rewards.md` | 196 | 12,999 | Condensed Relics & Scavenge Tables |
| `quickstart/05_gm_screen_and_play_aids.md` | 174 | 12,240 | Condensed GM Screen Reference |

### 3.4 Master & Print Outputs (`print/` and root)
| Filename | Lines | Bytes | Description |
| :--- | :---: | :---: | :--- |
| `armouries_of_the_third_deep_master.md` | 4,653 | 385,654 | Unified Master Adventure Book (All Chapters + Appendices) |
| `print/armouries_of_the_third_deep_master.html` | 4,406 | 436,323 | A4 Print-Optimized Master HTML Publication |
| `print/armouries_of_the_third_deep_master.pdf` | — | 2,235,063 | High-Resolution Master A4 PDF Document |

### 3.5 Handout HTML & PDF Assets (`handouts/html/` and `handouts/pdf/`)
| Filename | Lines | Bytes | Description |
| :--- | :---: | :---: | :--- |
| `handouts/html/gm_cheat_sheet.html` | 208 | 15,060 | Standalone GM Cheat Sheet HTML |
| `handouts/html/band_worksheet.html` | 191 | 13,983 | Standalone Band Worksheet HTML |
| `handouts/html/dying_scribe_letter.html` | 77 | 8,423 | Standalone Dying Scribe Letter HTML |
| `handouts/html/node_map.html` | 100 | 11,226 | Standalone Node Map HTML |
| `handouts/html/handouts_complete_bundle.html` | 439 | 34,469 | Complete Handouts 4-in-1 Bundle HTML |
| `handouts/pdf/gm_cheat_sheet.pdf` | — | 191,238 | A4 Vector PDF: GM Cheat Sheet |
| `handouts/pdf/band_worksheet.pdf` | — | 178,872 | A4 Vector PDF: Band Worksheet |
| `handouts/pdf/dying_scribe_letter.pdf` | — | 146,108 | A4 Vector PDF: Dying Scribe Letter |
| `handouts/pdf/node_map.pdf` | — | 130,587 | A4 Vector PDF: Node Map |
| `handouts/pdf/handouts_complete_bundle.pdf` | — | 317,615 | A4 Vector PDF: Complete Handouts Bundle |

### 3.6 Automation Scripts (`scripts/`)
| Filename | Lines | Bytes | Description |
| :--- | :---: | :---: | :--- |
| `scripts/__init__.py` | 0 | 0 | Package marker |
| `scripts/build_master_document.py` | 494 | 15,138 | Master book assembler (MD -> HTML -> PDF) |
| `scripts/render_handouts.py` | 946 | 39,540 | Handout renderer (HTML -> PDF) |
| `scripts/validate_module_suite.py` | 830 | 40,973 | 4-tier static and semantic validation engine |

### 3.7 Test Suites (`tests/`)
| Filename | Lines | Bytes | Description |
| :--- | :---: | :---: | :--- |
| `tests/__init__.py` | 4 | 82 | Package marker & docstring |
| `tests/test_tor2e_compliance.py` | 800 | 44,624 | Comprehensive 4-tier automated compliance test harness |
| `tests/test_math_and_balance.py` | 474 | 26,107 | Mathematical consistency & balance validator |
| `tests/test_adversarial_coverage.py` | 346 | 17,150 | Adversarial stress test suite |

### 3.8 Documentation & Configuration Files (Root)
| Filename | Lines | Bytes | Description |
| :--- | :---: | :---: | :--- |
| `PROJECT.md` | 77 | 7,636 | Project architectural specification & milestone tracker |
| `README.md` | 49 | 5,057 | Module directory overview & table guide |
| `TEST_INFRA.md` | 37 | 3,253 | E2E testing infrastructure specification |
| `TEST_READY.md` | 72 | 5,949 | Test readiness and verification declaration |

---

## 4. Build Execution Dependencies & R5 Verification Criteria

### 4.1 Execution Dependencies
1. **Python Environment**:
   - Python 3.10+ (Python 3.13 tested in environment).
   - Standard Library modules: `os`, `sys`, `re`, `json`, `argparse`, `pathlib`, `typing`, `subprocess`, `dataclasses`, `unittest`.
   - Third-Party Package: `markdown2` (`pip install markdown2`).
2. **Headless PDF Engine**:
   - Microsoft Edge (`msedge.exe`) or Google Chrome (`chrome.exe`).
   - If no browser executable is found, `find_pdf_engine()` gracefully falls back to generating HTML files only.
3. **Execution Commands**:
   - Master document build: `python scripts/build_master_document.py`
   - Handout build: `python scripts/render_handouts.py` (recommend adding `scripts/build_handouts.py` wrapper)
   - Validation test: `python scripts/validate_module_suite.py`
   - Unittest suite: `python -m unittest discover -s tests`

### 4.2 R5 Verification Criteria Checklist
To verify requirement R5 upon completion of all revisions:
1. **Script Execution Integrity**:
   - `python scripts/build_master_document.py` exits with returncode `0`.
   - `python scripts/render_handouts.py` (and `build_handouts.py`) exits with returncode `0`.
2. **Master Document Assembly Accuracy**:
   - `armouries_of_the_third_deep_master.md` is updated and matches the content of chapters `01` through `07` and appendices A–D with zero missing sections.
   - Zero occurrences of "Daunted" across `armouries_of_the_third_deep_master.md`.
   - Zero occurrences of hardcoded pregen TN listings (e.g. `Torvir 15, Einar 15, Khoril 16`) across `armouries_of_the_third_deep_master.md`.
3. **HTML & Presentation Styling**:
   - `print/armouries_of_the_third_deep_master.html` correctly renders all tables, Swedish read-aloud boxes (`.boxed-read-aloud`), ASCII cards (`.ascii-card`), and page-breaks.
   - `handouts/html/*.html` and `handouts/pdf/*.pdf` are updated to match the revised TOR 2e format.
4. **Quickstart Alignment**:
   - All 6 files in `quickstart/` (`00` to `05`) are verified to have "Daunted" purged, pregen TNs removed from skill checks, and neutral scene descriptions.
5. **Automated Test Certification**:
   - `python scripts/validate_module_suite.py` passes with 0 errors across all 4 tiers.
   - `python -m unittest discover -s tests` executes with 100% passing tests across all test modules.

---

## 5. Proposed Actionable Recommendations for Implementation Phase

1. **Create `scripts/build_handouts.py` Wrapper**:
   Create a small wrapper script `scripts/build_handouts.py` that executes `scripts/render_handouts.py` so that both script names work identically.
2. **Update `scripts/render_handouts.py` HTML Templates**:
   Synchronize `render_handouts.py` internal HTML builders with the new standard TOR 2e check format, removing hardcoded pre-gen numbers from the cheat sheet and node map.
3. **Update `scripts/validate_module_suite.py` & `tests/*.py`**:
   Adjust validation regexes to enforce:
   - Zero occurrences of `Daunted` across the entire codebase.
   - Standard skill format (e.g. `**SCAN roll**`, `**STEALTH roll**` with situational modifiers) without requiring pregen attribute TN strings in adventure text.
   - Neutral GM phrasing in read-aloud boxes and scene setups.
4. **Post-Edit Rebuild Pipeline**:
   After workers update `01`–`07`, `handouts/*.md`, and `quickstart/*.md`, execute `build_master_document.py` and `render_handouts.py` to regenerate all presentation assets in one pass.
