# 🏔️ Moria: Through the Doors of Durin

A comprehensive campaign toolkit and adventure repository for ***The One Ring 2nd Edition*** (Year 2989 TA / Balin's Expedition Era).

---

## 🗺️ Repository Overview

This repository is organized to prioritize **lore, session preparation, adventure modules, and GM table play aids**, while housing source ingestion tools in dedicated subpackages.

```text
Moria/
├── adventures/                          # Publication-Ready Adventure Modules
│   └── armouries_of_the_third_deep/     # The Armouries of the Third Deep (Complete 3-Act Module)
│       ├── 00_overview_and_background.md
│       ├── 01_campaign_context.md
│       ├── 02_band_mechanics.md
│       ├── 03_operational_mechanics.md
│       ├── 04_keyed_locations.md
│       ├── 05_adversaries_and_hazards.md
│       ├── 06_relics_and_rewards.md
│       ├── 07_gm_playbook_and_pacing.md
│       └── handouts/                    # GM Cheat Sheets, Band Worksheets, Node Maps, Letter Props
├── campaign_log.md                      # Ongoing Campaign Chronicle & Hero Rosters
├── session_prep_armouries.md            # Session Prep & Extended Fellowship Phase Guide
├── PROJECT.md                           # Master Architecture & Feature Inventory
├── TEST_INFRA.md                        # E2E Test Suite Specification
├── TEST_READY.md                        # Verification Audit & Multi-Agent Sign-off Report
├── tests/                               # 4-Tier Automated System Verification Suite
└── pdf_parser/                          # Rulebook PDF Ingestion & OCR Pipeline (see pdf_parser/README.md)
```

---

## 📜 Campaign & Lore Highlights

### 1. The Fellowship & Campaign Chronicle ([`campaign_log.md`](campaign_log.md))
- **Active Heroes**:
  - **Torvir Hammerstone** (*Champion*, Dwarf of Durin) — Great Axe specialist & frontline anchor.
  - **Einar son of Anar** (*Treasure Hunter*, Dwarf of Durin) — Master scout carrying the Broken Key.
  - **Khoril Hornblower** (*Captain*, Dwarf of Durin) — Band leader carrying the ancient battle-horn.
- **Strategic State**: Transitioning from Thrym Thistlebeard's Caves to the East-Gate Camp; Eye Awareness tracking and Balin's colony politics.

### 2. Session Preparation ([`session_prep_armouries.md`](session_prep_armouries.md))
- **Extended Fellowship Phase**: Undertakings at Dimrill Dale, healing, companion hardening, and council with Lord Balin.
- **Ascent Journey Rolls**: Travel mechanics, hazard resolution, and safe haven establishment.

### 3. Feature Adventure: *The Armouries of the Third Deep* ([`adventures/armouries_of_the_third_deep/`](adventures/armouries_of_the_third_deep/))
- **Act I: The Descent & Mustering**: Staging at the Upper Mustering-Yard and entering the darkened shafts.
- **Act II: Despoiled Halls & Toxic Deeps**: Navigating toxic miasma, the Goblin Village, and siege weapon positions.
- **Act III: The Apex Vault & Fighting Withdrawal**: The duel with The Mauler, Grimnar's ambush at the King's Door, claiming Durin's Axe, and the timed escape.
- **Handouts & Play Aids**:
  - [`gm_cheat_sheet.md`](adventures/armouries_of_the_third_deep/handouts/gm_cheat_sheet.md): 1-page quick combat and DC dashboard.
  - [`band_worksheet.md`](adventures/armouries_of_the_third_deep/handouts/band_worksheet.md): Band tactical roles, readiness, and morale tracking.
  - [`node_map.md`](adventures/armouries_of_the_third_deep/handouts/node_map.md): 3-tier elevation tactical flowchart.
  - [`dying_scribe_letter.md`](adventures/armouries_of_the_third_deep/handouts/dying_scribe_letter.md): In-world prop clue for the Marshal's Key.

---

## 🧪 Verification & Automated Testing

The adventure mechanics, DC math, Band operational rules, adversary balance, and multi-session workflows are covered by a comprehensive 188-test E2E test harness.

```powershell
# Run the complete test suite (Tiers 1-4)
python tests/test_runner.py

# Run a specific tier (e.g. Tier 1: Feature Coverage)
python tests/test_runner.py --tier 1
```

---

## ⚙️ PDF Ingestion & Rulebook Processing

For processing source PDFs into searchable Markdown and JSONL indexes, see the documentation in [`pdf_parser/README.md`](pdf_parser/README.md).
