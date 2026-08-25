import fitz  # PyMuPDF
import json
import argparse
import os
import sys
from pathlib import Path
from collections import Counter

def get_body_font_size(doc, max_pages=15):
    """
    Scans the document to determine the 'standard' body text size.
    """
    font_sizes = []
    for i, page in enumerate(doc):
        if i >= max_pages: break
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            if b['type'] == 0:
                for line in b["lines"]:
                    for span in line["spans"]:
                        if len(span['text'].strip()) > 1:
                            font_sizes.append(round(span['size']))
    
    if not font_sizes: return 11
    return Counter(font_sizes).most_common(1)[0][0]

def analyze_line_spatial(line, body_size):
    """
    Analyzes a line using spatial heuristics (gaps between spans) 
    to correctly reconstruct sentences and headers.
    """
    if not line["spans"]: return "", ""

    # 1. Determine Line Type (Header vs Body) using weighted average size
    total_area = 0
    weighted_size = 0
    
    for span in line["spans"]:
        text = span['text'].strip()
        if not text: continue
        w = len(text)
        weighted_size += w * span['size']
        total_area += w
    
    avg_size = weighted_size / total_area if total_area > 0 else 0
    
    # Header Detection
    prefix = ""
    is_header = False
    if avg_size > body_size + 4:
        prefix = "# "
        is_header = True
    elif avg_size > body_size + 1.5:
        prefix = "## "
        is_header = True

    # 2. Reconstruct Text with Spatial Logic
    md_parts = []
    plain_parts = []
    
    prev_x1 = -100 # Initialize far left
    
    for span in line["spans"]:
        text = span['text']
        # Skip purely empty layout artifacts, but keep text that is just spaces
        if not text: continue 
        
        # Calculate Gap from previous span
        x0 = span['bbox'][0]
        x1 = span['bbox'][2]
        
        # Logic: Should we insert a space?
        # Only check if this isn't the first span
        if prev_x1 != -100:
            gap = x0 - prev_x1
            
            # THE SECRET SAUCE:
            # A distinct space is usually ~25% of the font size. 
            # Kerning (letters in a title) is usually < 5% or even negative.
            # We use a safe threshold: 15% of font size or at least 1.5 pixels.
            threshold = max(1.5, span['size'] * 0.15)
            
            if gap > threshold:
                # Insert space if the text doesn't already have one
                if not text.startswith(" ") and (md_parts and not md_parts[-1].endswith(" ")):
                    md_parts.append(" ")
                    plain_parts.append(" ")

        # Update previous x coord
        prev_x1 = x1

        # Format the text (Bold vs Plain)
        md_text = text
        if not is_header:
            # Check for bold flag (16)
            if span['flags'] & 16:
                if text.strip(): # Don't bold pure whitespace
                    md_text = f"**{text}**"
        
        md_parts.append(md_text)
        plain_parts.append(text)

    # Join and clean
    final_md = "".join(md_parts).strip()
    final_plain = "".join(plain_parts).strip()
    
    # Apply Header Prefix (Headers don't get bold formatted)
    if is_header:
        # We strip bold markers from headers to keep them clean
        final_md = prefix + final_plain
        
    return final_md, final_plain

def pdf_to_jsonl(pdf_path, output_path):
    if not os.path.exists(pdf_path):
        print(f"Error: File {pdf_path} not found.")
        sys.exit(1)

    doc = fitz.open(pdf_path)
    body_size = get_body_font_size(doc)
    print(f"Processing '{pdf_path}'...")
    print(f"Detected Body Font Size: {body_size}pt")

    with open(output_path, 'w', encoding='utf-8') as f_out:
        for page_num, page in enumerate(doc):
            blocks = page.get_text("dict")["blocks"]
            page_md = ""
            page_plain = ""
            
            for b in blocks:
                if b['type'] == 0: # Text Block
                    for line in b["lines"]:
                        md_line, plain_line = analyze_line_spatial(line, body_size)
                        if md_line:
                            page_md += md_line + "\n"
                            page_plain += plain_line + "\n"
                    
                    page_md += "\n" 

            record = {
                "id": f"{os.path.basename(pdf_path)}-p{page_num + 1}",
                "source": os.path.basename(pdf_path),
                "page": page_num + 1,
                "content": page_md.strip(),
                "plain_text": page_plain.strip()
            }
            
            f_out.write(json.dumps(record, ensure_ascii=False) + '\n')

    print(f"Success! Output saved to '{output_path}'")

if __name__ == "__main__":
    BASE_DIR = Path(__file__).parent.resolve()
    parser = argparse.ArgumentParser(description="Convert a directory of PDFs to individual JSONL files (Fast heuristic method).")
    parser.add_argument(
        "--input", "-i", 
        default=str(BASE_DIR / "Source_Material" / "Unprocessed"), 
        help="Directory containing PDFs to process"
    )
    parser.add_argument(
        "--output", "-o", 
        default=str(BASE_DIR / "output" / "quick_indexes"), 
        help="Directory where JSONL files will be saved"
    )
    args = parser.parse_args()
    
    input_dir = Path(args.input)
    output_dir = Path(args.output)
    
    if not input_dir.exists():
        print(f"Error: Input directory '{input_dir}' not found.")
        sys.exit(1)
        
    output_dir.mkdir(parents=True, exist_ok=True)
    
    pdf_files = list(input_dir.glob("*.pdf"))
    if not pdf_files:
        print(f"No PDFs found in {input_dir}")
        sys.exit(0)
        
    print(f"Found {len(pdf_files)} PDFs. Starting fast indexing...")
    
    for pdf_path in pdf_files:
        output_path = output_dir / f"{pdf_path.stem}.jsonl"
        
        # Simple duplicate check
        if output_path.exists():
            print(f"Skipping {pdf_path.name} (Output already exists)")
            continue
            
        try:
            pdf_to_jsonl(str(pdf_path), str(output_path))
        except Exception as e:
            print(f"Error processing {pdf_path.name}: {e}")
            
    print("\nBatch indexing complete!")