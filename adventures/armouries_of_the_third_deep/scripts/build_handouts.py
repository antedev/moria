#!/usr/bin/env python3
"""
build_handouts.py — Handout Build Automation Wrapper
====================================================
Standard build entry point for rendering all player and GM handouts
into print-ready A4 HTML and PDF assets in handouts/html/ and handouts/pdf/.

Invokes render_handouts.render_all().
"""

import sys
from pathlib import Path

# Ensure scripts directory is in sys.path
SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from render_handouts import render_all


def main():
    render_all()


if __name__ == "__main__":
    main()
