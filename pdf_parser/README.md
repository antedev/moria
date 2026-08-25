# 📖 PDF Translation & Parsing Pipeline (`pdf_parser`)

A standalone toolchain for automatically converting tabletop RPG rulebook PDFs into structured Markdown and indexed JSONL datasets. Uses local AI models (via `marker-pdf`) for layout detection and Google Gemini for intelligent text refinement, heading hierarchy, and table formatting.

---

## 📁 Directory Structure

```text
pdf_parser/
├── Source_Material/
│   ├── Unprocessed/    ← DROP YOUR SOURCE PDFs HERE (gitignored)
│   └── Processed/      ← Script moves files here after successful conversion (gitignored)
├── output/             ← Output Markdown files & extracted images appear here (gitignored)
│   ├── <BookName>/
│   │   ├── <BookName>.md
│   │   ├── <BookName>.jsonl
│   │   └── <images>.jpeg
│   └── quick_indexes/  ← Fast heuristic JSONL extractions
├── pd2jsonl.py         ← Fast spatial heuristic PDF to JSONL extractor
├── sync_lore.py        ← Full Marker + Gemini LLM refinement pipeline
└── README.md           ← This guide
```

---

## ✅ Prerequisites

1. **Python 3.11+** (Python 3.13 tested)
2. **NVIDIA GPU** *(strongly recommended)* — CUDA support provides ~2-3s/page conversion speed.
3. **Google Gemini API Key** — For intelligent layout, table, and heading refinement.
4. **Environment Variables**:
   Ensure `.env` exists in the project root or inside `pdf_parser/`:
   ```env
   GOOGLE_API_KEY=your_gemini_api_key
   GEMINI_MODEL=gemini-3.1-pro-preview
   ```

---

## ⚙️ Installation

```powershell
# 1. Install PyTorch with CUDA support
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126

# 2. Install dependencies
pip install marker-pdf PyMuPDF python-dotenv

# 3. (Optional) Patch marker-pdf for 504 retry stability:
# In <python_path>/site-packages/marker/services/gemini.py
# Change: if e.code in [429, 443, 503]:
# To:     if e.code in [429, 443, 503, 504]:
```

---

## 🚀 Running the Tools

### Tool 1: Full Marker + Gemini Refinement (`sync_lore.py`)

Converts PDFs in `Source_Material/Unprocessed/` to structured Markdown and high-quality JSONL search indexes.

```powershell
# Convert all PDFs in Source_Material/Unprocessed
python pdf_parser/sync_lore.py

# Test run on pages 1-5
python pdf_parser/sync_lore.py --pages 1-5

# Convert without LLM refinement (fast raw layout only)
python pdf_parser/sync_lore.py --no-llm

# Specify custom Gemini model
python pdf_parser/sync_lore.py --model gemini-3.1-pro-preview
```

### Tool 2: Fast Heuristic Indexer (`pd2jsonl.py`)

Uses PyMuPDF font-size and spatial gap heuristics to rapidly convert PDFs into page-by-page JSONL lines without external API calls.

```powershell
# Run batch indexer on all unprocessed PDFs
python pdf_parser/pd2jsonl.py

# Custom input/output paths
python pdf_parser/pd2jsonl.py -i pdf_parser/Source_Material/Unprocessed -o pdf_parser/output/quick_indexes
```
