#!/usr/bin/env bash
# Wrapper around edit_demo.py — reserved caption bar, title/end cards, punch-ins.
#
#   ./edit_demo.sh --input recording.mp4 --timeline example_timeline.json --output demo.mp4
#   ./edit_demo.sh --input recording.mp4 --timeline example_timeline.json --output demo.mp4 --fps 25
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
exec python3 "$HERE/edit_demo.py" "$@"
