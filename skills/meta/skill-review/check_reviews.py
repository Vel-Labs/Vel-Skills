#!/usr/bin/env python3
"""Report every skill's review state: OK, DUE SOON, OVERDUE or MISSING fields.

Usage:
    python3 check_reviews.py [--root DIR ...] [--today YYYY-MM-DD] [--soon DAYS]

With no --root, checks the library this file belongs to (the `skills/` folder
three levels up). Pass --root for other folders, for example an agent's local
skills directory. Exit code 1 when any skill is overdue or missing fields, so a
scheduled job or CI can use it. Changes nothing.
"""

import argparse
import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from skill_meta import skills_under  # noqa: E402

LIBRARY = Path(__file__).resolve().parents[2]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", action="append", type=Path)
    parser.add_argument("--today", default=date.today().isoformat())
    parser.add_argument("--soon", type=int, default=7)
    args = parser.parse_args()
    today = date.fromisoformat(args.today)
    failing = 0
    for root in args.root or [LIBRARY]:
        for skill in skills_under(root.expanduser()):
            label = skill.path.parent.relative_to(root.expanduser()).as_posix()
            problems = skill.problems()
            due = skill.due()
            if problems:
                failing += 1
                print(f"MISSING   {label}: " + "; ".join(problems))
            elif due and due < today:
                failing += 1
                print(f"OVERDUE   {label}: due {due} ({(today - due).days} days ago), {skill.origin}")
            elif due and due <= today + timedelta(days=args.soon):
                print(f"DUE SOON  {label}: due {due}, {skill.origin}")
            else:
                print(f"OK        {label}: reviewed {skill.meta['reviewed']}, next {due}, {skill.origin}")
            if skill.origin in {"external", "adapted"} and skill.meta.get("source"):
                print(f"          {skill.meta['source']} @ {skill.meta.get('source-ref', '?')}")
    return 1 if failing else 0


if __name__ == "__main__":
    sys.exit(main())
