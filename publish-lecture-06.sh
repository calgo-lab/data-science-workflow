#!/usr/bin/env bash
# Publish DSA Lecture 6 to the website + refresh the slides download.
#
# DSA/ is gitignored (your live working copy, edited in Jupyter), so this
# snapshots the notebook into the tracked DSA-sessions/ folder and rebuilds
# the reveal.js slides that the web page offers as a download.
#
# Usage: save the notebook in Jupyter first, then run from the repo root:
#     ./publish-lecture-06.sh
# It uses the outputs already stored in the notebook; it does NOT re-execute.
set -euo pipefail
cd "$(dirname "$0")"

PY="DSA/.venv/bin/python"
SRC="DSA/lecture-06.ipynb"
DST_DIR="DSA-sessions"
DST_BASE="session6_recommendation_problem"

[ -x "$PY" ]  || { echo "error: $PY not found (is the venv there?)"; exit 1; }
[ -f "$SRC" ] || { echo "error: $SRC not found"; exit 1; }

echo "-> snapshot  $SRC -> $DST_DIR/$DST_BASE.ipynb"
cp "$SRC" "$DST_DIR/$DST_BASE.ipynb"

echo "-> slides    $DST_DIR/$DST_BASE.slides.html  (code inputs hidden)"
"$PY" -m nbconvert --to slides \
  --output "$DST_BASE" --output-dir "$DST_DIR" \
  --TagRemovePreprocessor.enabled=True \
  --TagRemovePreprocessor.remove_input_tags hide-input \
  "$DST_DIR/$DST_BASE.ipynb"

echo "✓ published. Review with 'git status', then commit & push (push deploys the site)."
