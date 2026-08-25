import os
import argparse
import shutil
import logging
from pathlib import Path
from dotenv import load_dotenv

# Suppress annoying C++ GRPC logs from underlying LLM calls
os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"

import gc
import json
import fitz # PyMuPDF for TOC
try:
    import torch
except ImportError:
    torch = None

# 1. Import Marker modules natively
from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import save_output
from marker.config.parser import ConfigParser

# Load Credentials
load_dotenv()

# Setup Basic Logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

def clear_memory():
    """Flush any cached memory to avoid OOM crashes on large PDFs."""
    gc.collect()
    if torch and torch.cuda.is_available():
        torch.cuda.empty_cache()

def get_chapter_ranges(pdf_path, chunk_size=50):
    """
    Analyzes PDF's TOC to find logical chapter ranges.
    Falls back to fixed-size blocks if no TOC matches are found.
    """
    ranges = []
    try:
        doc = fitz.open(pdf_path)
        total_pages = len(doc)
        toc = doc.get_toc()
        
        # We only care about level 1 headers for batching
        # Shift TOC start pages to 0-indexed (PyMuPDF uses 1-indexed)
        start_pages = sorted(list(set([entry[2] - 1 for entry in toc if entry[0] == 1])))
        doc.close()

        # Ensure we always start at page 0
        if not start_pages or start_pages[0] != 0:
            start_pages.insert(0, 0)

        if len(start_pages) == 1: # Only the 0-page exists
            logger.info("No TOC level 1 headers found. Falling back to fixed chunks.")
            for i in range(0, total_pages, chunk_size):
                end = min(i + chunk_size - 1, total_pages - 1)
                ranges.append(f"{i}-{end}")
            return ranges

        # Build ranges from TOC points
        for i in range(len(start_pages)):
            start = start_pages[i]
            # End is either the next chapter's start-1, or the last page (0-indexed)
            end = start_pages[i+1] - 1 if i+1 < len(start_pages) else total_pages - 1
            
            # If a chapter is too big, split it to be safe
            if end - start + 1 > chunk_size:
                for sub_start in range(start, end + 1, chunk_size):
                    sub_end = min(sub_start + chunk_size - 1, end)
                    ranges.append(f"{sub_start}-{sub_end}")
            else:
                ranges.append(f"{start}-{end}")
                
        return ranges
    except Exception as e:
        logger.warning(f"Failed to extract TOC: {e}. Using default 1-5 batch.")
        return [None] # Use default 'None' which marker handles as 'all' or we'll fallback to p1-p50

def generate_jsonl_output(markdown_text, book_name, output_path):
    """
    Parses the final high-quality Markdown and turns it into a JSONL search index.
    Divides by headers or large breaks to keep records logical.
    """
    records = []
    # Split by level 1 or 2 headers
    sections = markdown_text.split("\n#")
    
    for i, section in enumerate(sections):
        if not section.strip(): continue
        
        # Clean up the prefix we split on
        content = ("#" if i > 0 else "") + section
        
        # Try to find a title in the first line
        lines = content.strip().split("\n")
        title = lines[0].replace("#", "").strip() if lines else "General"
        
        record = {
            "id": f"{book_name}-section-{i}",
            "source": book_name,
            "title": title,
            "content": content.strip()
        }
        records.append(record)
        
    with open(output_path, "w", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    logger.info(f"✅ Generated high-quality search index: {output_path}")

def get_args():
    parser = argparse.ArgumentParser(description="Convert RPG PDFs to Markdown using local models and Gemini.")
    
    parser.add_argument(
        "--pages", "-p",
        type=str,
        default=None,
        help="Page range to process (e.g., '1-10', '5-', or empty for all). Default is all pages."
    )
    
    parser.add_argument(
        "--ocr",
        action="store_true",
        default=False,
        help="Force OCR on all pages (even digital ones)."
    )
    
    parser.add_argument(
        "--no-llm",
        action="store_false",
        dest="use_llm",
        default=True,
        help="Disable LLM refinement (Gemini)."
    )
    
    parser.add_argument(
        "--model", "-m",
        type=str,
        default=os.getenv("GEMINI_MODEL", "gemini-3.1-pro-preview"),
        help="Gemini model to use for refinement."
    )

    return parser.parse_args()

def main():
    args = get_args()
    
    # 2. Define our Directory Pipeline
    BASE_DIR = Path(__file__).parent.resolve()
    UNPROCESSED_DIR = BASE_DIR / "Source_Material" / "Unprocessed"
    PROCESSED_DIR = BASE_DIR / "Source_Material" / "Processed"
    OUTPUT_BASE_DIR = BASE_DIR / "output"

    # Make sure folders exist
    UNPROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_BASE_DIR.mkdir(parents=True, exist_ok=True)

    # 3. Find PDFs in the Unprocessed directory
    pdf_files = list(UNPROCESSED_DIR.glob("*.pdf"))
    if not pdf_files:
        logger.info(f"No PDFs found in {UNPROCESSED_DIR}. Exiting.")
        return

    logger.info(f"Found {len(pdf_files)} PDF(s) to process. Initializing Converter...")

    # 4. Initialize Global Models (loaded once)
    model_dict = create_model_dict()

    # 5. Process Each PDF
    for pdf_path in pdf_files:
        base_name = pdf_path.stem
        target_output_dir = OUTPUT_BASE_DIR / base_name
        target_processed_file = PROCESSED_DIR / pdf_path.name

        # Duplicate Safety Check
        if target_output_dir.exists():
            logger.warning(f"[SKIP] Output directory already exists: {target_output_dir}")
            continue
        
        if target_processed_file.exists():
            logger.warning(f"[SKIP] File already exists in Processed folder: {target_processed_file}")
            continue

        # 6. Determine Logical Chapters/Batches
        chapter_ranges = get_chapter_ranges(str(pdf_path))
        logger.info(f"--- Processing: {pdf_path.name} ({len(chapter_ranges)} chapter batches) ---")
        
        full_markdown = ""
        aggregated_document = None

        try:
            target_output_dir.mkdir(parents=True, exist_ok=True)
            
            for i, p_range in enumerate(chapter_ranges):
                logger.info(f"  [Batch {i+1}/{len(chapter_ranges)}] Pages {p_range}...")
                
                # Clear memory before every heavy batch
                clear_memory()

                # Configure Converter for this chunk
                custom_config = {
                    "use_llm": args.use_llm,
                    "force_ocr": args.ocr,
                    "output_format": "markdown",
                    "page_range": p_range,
                    "gemini_api_key": os.getenv("GOOGLE_API_KEY"),
                    "gemini_model_name": args.model,
                    "llm_timeout": 300 
                }

                config_parser = ConfigParser(custom_config)
                
                converter = PdfConverter(
                    config=config_parser.generate_config_dict(),
                    artifact_dict=model_dict,
                    processor_list=config_parser.get_processors(),
                    renderer=config_parser.get_renderer(),
                    llm_service=config_parser.get_llm_service()
                )

                # Execute conversion for this chapter
                rendered_document = converter(str(pdf_path))
                
                # Stitch Markdown
                full_markdown += rendered_document.markdown + "\n\n"
                
                # Use the first document as a base for metadata, but merge images
                if aggregated_document is None:
                    aggregated_document = rendered_document
                else:
                    # Merge metadata (images) into the primary document
                    aggregated_document.metadata.update(rendered_document.metadata)

            # 7. Post-Process & Save Total Results
            if aggregated_document:
                aggregated_document.markdown = full_markdown
                
                # Save MD and images
                save_output(aggregated_document, str(target_output_dir), base_name)
                
                # Generate Search Index from cleaned Markdown
                jsonl_path = target_output_dir / f"{base_name}.jsonl"
                generate_jsonl_output(full_markdown, base_name, str(jsonl_path))
                
                # 8. Move the original to Processed
                shutil.move(str(pdf_path), str(target_processed_file))
                logger.info(f"✅ Successfully completed all {len(chapter_ranges)} batches!")

        except Exception as e:
            logger.error(f"❌ Failed to process {pdf_path.name}. Error: {e}")
            import traceback
            logger.error(traceback.format_exc())

if __name__ == "__main__":
    main()
