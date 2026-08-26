# Handoff Report: Build Pipeline, Scripts, Master Document & Repository Survey
**Agent**: `survey_explorer_3`  
**Working Directory**: `c:/Users/ante/Documents/github/Moria/adventures/armouries_of_the_third_deep/.agents/survey_explorer_3`  
**Date**: 2026-08-26  
**Type**: Hard Handoff (Task Complete)

---

## 1. Observation

### Build Pipeline Scripts
- `scripts/build_master_document.py` (494 lines):
  - Directly concatenates `CHAPTER_FILES` (7 files: `01_campaign_context.md` through `07_gm_playbook_and_pacing.md`) and `APPENDIX_FILES` (4 files: `handouts/node_map.md`, `handouts/gm_cheat_sheet.md`, `handouts/band_worksheet.md`, `handouts/dying_scribe_letter.md`).
  - Converts markdown to HTML via `markdown2.markdown(..., extras=['tables', 'fenced-code-blocks', 'header-ids', 'strike', 'smarty-pants', 'cuddled-lists'])` (line 140).
  - Uses regex substitutions for Swedish read-aloud blocks (`<blockquote>\s*<p>\s*<em>(.*?)</em>\s*</p>\s*</blockquote>` -> `<div class="boxed-read-aloud">...</div>`, line 152) and page-break markers (`<!-- PAGE BREAK: (.*?) -->` -> `<div class="page-break" data-chapter="\1"></div>`, line 156).
  - Detects Microsoft Edge or Chrome in `EDGE_PATHS` (lines 45–49) and runs headless CLI `--print-to-pdf` to generate `print/armouries_of_the_third_deep_master.pdf`.
- `scripts/render_handouts.py` (946 lines):
  - Contains dedicated HTML template builder functions (`build_gm_cheat_sheet_html()`, `build_band_worksheet_html()`, `build_dying_scribe_letter_html()`, `build_node_map_html()`) rather than parsing `handouts/*.md`.
  - Lines 296–334, 736–748, and 784–832 embed hardcoded pregen Target Numbers (e.g. `Torvir: STR 13 / HRT 18 / WIT 15`, `Wits TN 15/16`, `Strength TN 13/14`, `Stealth WIT TN 15`, `Valour HRT TN 18`).
  - Output files: 5 HTML in `handouts/html/` and 5 PDF in `handouts/pdf/`.
  - Note: `ORIGINAL_REQUEST.md` (lines 90, 112) references `scripts/build_handouts.py`, but the script in the repository is named `scripts/render_handouts.py`.
- `scripts/validate_module_suite.py` (830 lines):
  - Validates 19 markdown files across 4 tiers.

### Synchronization & Rules Deficiencies in Current Assets
- `grep_search` for `daunted` yielded 5 matches in `armouries_of_the_third_deep_master.md` (lines 1520, 1525, 1534, 2113, 2284), 5 matches in `print/armouries_of_the_third_deep_master.html` (lines 2195, 2203, 2220, 3100, 3307), 4 matches in `04_keyed_locations.md` (lines 472, 477, 486, 1065), 1 match in `05_adversaries_and_hazards.md` (line 115), and 4 matches in `quickstart/02_keyed_locations.md` (lines 210, 215, 224, 452).
- `grep_search` for `Torvir 13` / `Torvir 15` / `Einar 14` / `Khoril 16` yielded over 212 occurrences across chapters `01` to `07`, quickstart `00` to `05`, handouts, and master documents.

### Repository File Map
- Complete inventory confirms 17 source markdown files (7 chapters, 4 handouts, 6 quickstart), 1 master markdown file, 4 project/test config docs, 4 Python scripts in `scripts/`, 4 Python test files in `tests/`, 6 HTML files, and 6 PDF files.

---

## 2. Logic Chain

1. **Premise**: `build_master_document.py` builds `armouries_of_the_third_deep_master.md`, `print/armouries_of_the_third_deep_master.html`, and `print/armouries_of_the_third_deep_master.pdf` by concatenating `01_*.md` through `07_*.md` and `handouts/*.md`.
2. **Observation**: Chapters `01` through `07` and `handouts/*.md` currently contain non-canonical "Daunted" conditions, hardcoded pre-gen numbers in skill checks, prescriptive PC actions, and read-aloud spoilers.
3. **Inference 1**: `armouries_of_the_third_deep_master.md` and `print/armouries_of_the_third_deep_master.html` directly reflect those non-canonical elements and are therefore out of date with respect to the new R1–R5 directives.
4. **Observation**: `scripts/render_handouts.py` contains hardcoded HTML templates rather than reading `handouts/*.md`.
5. **Inference 2**: Updating `handouts/*.md` alone will NOT update the HTML and PDF assets in `handouts/html/` and `handouts/pdf/`. `scripts/render_handouts.py` must either have its internal string templates updated in sync or be refactored to render from markdown.
6. **Observation**: `ORIGINAL_REQUEST.md` specifies testing `python scripts/build_handouts.py`, while the script is currently `scripts/render_handouts.py`.
7. **Inference 3**: Creating `scripts/build_handouts.py` as an executable entry point or wrapper calling `render_handouts.py` ensures 100% compatibility with the requirement specification.

---

## 3. Caveats

1. **PDF Rendering Environment**: PDF generation relies on headless Microsoft Edge or Google Chrome. If running in a headless CI/CD or restricted environment without Edge/Chrome binaries on standard paths, the script logs a warning and generates only the HTML files.
2. **Interactive Terminal Execution**: In environments where interactive subprocess execution (`run_command`) prompts for user permissions, verification can be performed statically by checking file contents or running standalone python commands in authorized environments.
3. **Scope Discipline**: As an explorer in a read-only investigation role, no source code, markdown files, or scripts were modified during this survey.

---

## 4. Conclusion

1. **Build Scripts**: `scripts/build_master_document.py` is fully functional and well-structured for compiling master MD, HTML, and PDF. `scripts/render_handouts.py` works but uses hardcoded HTML strings rather than parsing `handouts/*.md`.
2. **Sync Status**: `armouries_of_the_third_deep_master.md`, `print/*.html`, `print/*.pdf`, `handouts/html/*.html`, and `handouts/pdf/*.pdf` are out of date relative to R1–R5 and will need to be recompiled after chapter/handout edits.
3. **Repository Inventory**: Fully inventoried 17 markdown source files, 1 master markdown file, 4 project docs, 4 scripts, 4 test files, and 12 presentation assets (6 HTML, 6 PDF).
4. **Actionable Path Forward**:
   - Update markdown chapters `01` to `07`, quickstart `00` to `05`, and `handouts/*.md` for R1–R4.
   - Synchronize `scripts/render_handouts.py` (and create `scripts/build_handouts.py` alias).
   - Re-run `scripts/build_master_document.py` and `scripts/render_handouts.py` to regenerate all master and presentation assets cleanly for R5.
   - Update `scripts/validate_module_suite.py` and `tests/*.py` to validate R1–R5 criteria.

---

## 5. Verification Method

To independently verify these survey findings:
1. **Inspect Build Scripts**:
   - `view_file` on `scripts/build_master_document.py` (lines 28–43 for source mapping, lines 58–125 for assembly, lines 128–162 for HTML conversion).
   - `view_file` on `scripts/render_handouts.py` (lines 278–850 for hardcoded HTML templates).
2. **Check Current Stale State**:
   - `grep_search "daunted"` across `armouries_of_the_third_deep/` (confirms occurrences in master MD, master HTML, keyed locations, adversaries, and quickstart).
   - `grep_search "Torvir 13"` across `armouries_of_the_third_deep/` (confirms hardcoded pregen TN listings across all files).
3. **Execution Verification (R5)**:
   - `python scripts/build_master_document.py`
   - `python scripts/render_handouts.py`
   - `python scripts/validate_module_suite.py`
   - `python -m unittest discover -s tests`
