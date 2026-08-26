## 2026-08-26T05:12:23Z
You are worker_m4. Your working directory is `c:/Users/ante/Documents/github/Moria/adventures/armouries_of_the_third_deep/.agents/worker_m4`.
Read the following authoritative references before starting:
1. `c:/Users/ante/Documents/github/Moria/adventures/armouries_of_the_third_deep/.agents/ORIGINAL_REQUEST.md`
2. `c:/Users/ante/Documents/github/Moria/adventures/armouries_of_the_third_deep/.agents/survey_explorer_3/analysis.md`
3. `c:/Users/ante/Documents/github/Moria/adventures/armouries_of_the_third_deep/.agents/test_writer_e2e/test_report.md`
4. `c:/Users/ante/Documents/github/Moria/adventures/armouries_of_the_third_deep/.agents/teamwork_preview_orchestrator_2/PROJECT.md`

Your Exclusive File Write Ownership:
- `scripts/`
- `armouries_of_the_third_deep_master.md`
- `print/`
- `handouts/html/`
- `handouts/pdf/`

Mandatory Tasks:
1. **Update Build Scripts & Handout Renderers**:
   - Audit `scripts/build_master_document.py`, `scripts/render_handouts.py`, and `scripts/validate_module_suite.py`. Ensure templates in `scripts/render_handouts.py` reflect the updated neutral presentation, clean TOR 2e test blocks, and zero "Daunted" conditions.
   - Ensure `scripts/build_handouts.py` exists (e.g. wrapper/alias calling `render_handouts.py` or equivalent) so both `python scripts/build_master_document.py` and `python scripts/build_handouts.py` succeed with returncode 0.
2. **Execute Full Build Pipeline**:
   - Run `python scripts/build_master_document.py` to regenerate the master compiled markdown document (`armouries_of_the_third_deep_master.md`) and HTML/PDF presentation assets in `print/`.
   - Run `python scripts/build_handouts.py` (and `python scripts/render_handouts.py`) to regenerate all HTML and PDF handouts.
3. **Execute Static Validator and Full Automated Test Suite**:
   - Run `python scripts/validate_module_suite.py` and verify all tiers pass.
   - Run `python -m unittest discover -s tests` and verify that all 149+ test cases pass cleanly with returncode 0.
   - If any test fails, diagnose the failure, fix the build scripts or master compilation as appropriate, and rerun until 100% pass.
