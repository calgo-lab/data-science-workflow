#!/usr/bin/env bash
# Publish DSA Lecture 10 to the website + refresh the slides download.
#
# DSA/ is gitignored (your live working copy, edited in Jupyter), so this
# snapshots the notebook into the tracked DSA-sessions/ folder and rebuilds
# the reveal.js slides that the web page offers as a download.
#
# Usage: save the notebook in Jupyter first, then run from the repo root:
#     ./publish-lecture-10.sh
# It uses the outputs already stored in the notebook; it does NOT re-execute.
#
# Code inputs are hidden EXCEPT the CLIP load+encode demo cell (left untagged
# on purpose so students see the .encode() API). Slides use the CENTERED
# scrollable layout (Session 8+).
set -euo pipefail
cd "$(dirname "$0")"

# venv lives at DSA/.venv on some setups, .venv at the repo root on others —
# try both before giving up.
PY="DSA/.venv/bin/python"
[ -x "$PY" ] || PY=".venv/bin/python"
SRC="DSA/lecture-10.ipynb"
DST_DIR="DSA-sessions"
DST_BASE="session10_two_tower_multimodal"

[ -x "$PY" ]  || { echo "error: no python venv found (tried DSA/.venv and .venv)"; exit 1; }
[ -f "$SRC" ] || { echo "error: $SRC not found"; exit 1; }

echo "-> snapshot  $SRC -> $DST_DIR/$DST_BASE.ipynb"
cp "$SRC" "$DST_DIR/$DST_BASE.ipynb"

echo "-> slides    $DST_DIR/$DST_BASE.slides.html  (code inputs hidden except the CLIP encode cell)"
"$PY" -m nbconvert --to slides \
  --output "$DST_BASE" --output-dir "$DST_DIR" \
  --TagRemovePreprocessor.enabled=True \
  --TagRemovePreprocessor.remove_input_tags hide-input \
  "$DST_DIR/$DST_BASE.ipynb"

echo "-> inject    scrollable-slide CSS, centered (matching local preview)"
"$PY" inject_scrollable_css.py "$DST_DIR/$DST_BASE.slides.html" center

echo "✓ published. Review with 'git status', then commit & push (push deploys the site)."
