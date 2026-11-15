#!/usr/bin/env python3
"""Report every skill's review state: OK, DUE SOON, OVERDUE or MISSING fields.

Usage:
    python3 check_reviews.py [--include-private] [--check-links]
                             [--root DIR ...] [--today YYYY-MM-DD] [--soon DAYS]

With no --root, checks the library this file belongs to (the `skills/` folder
three levels up). Pass --root for other folders, for example an agent's local
skills directory. With --include-private, also check direct local private skills
and print only their folder names, states and valid dates. With --check-links,
look for broken links and duplicate standalone installs. Changes nothing.
"""

import argparse
import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from skill_meta import read, skills_under  # noqa: E402

LIBRARY = Path(__file__).resolve().parents[2]
PRIVATE = LIBRARY.parent / "private"


def check_links(public, private_files, home: Path) -> int:
    names = {s.name for s in public} | {s.path.parent.name for s in public}
    names.update(p.parent.name for p in private_files)
    for path in private_files:
        try:
            names.add(read(path).name)
        except (OSError, UnicodeError):
            continue

    count = 0
    for agent, managed in (("codex", ".system"), ("claude", "synced")):
        root = home / f".{agent}" / "skills"
        for entry in sorted(root.rglob("*")):
            relative = entry.relative_to(root)
            if entry.is_symlink():
                problem = "BROKEN LINK" if not entry.exists() else None
            else:
                problem = None
                skill_file = entry / "SKILL.md"
                if relative.parts[0] != managed and entry.is_dir() and skill_file.is_file():
                    try:
                        match = entry.name in names or read(skill_file).name in names
                    except (OSError, UnicodeError):
                        match = False
                    if match:
                        problem = "STANDALONE COPY"
            if problem:
                count += 1
                print(f"{problem}  {agent}/{relative.as_posix()!r}")
    if not count:
        print("Agent skill links are current.")
    return count


def check_private(paths, today: date, warning: date) -> int:
    count = 0
    for path in paths:
        try:
            skill = read(path)
            problems = skill.problems()
        except (OSError, UnicodeError):
            problems = ["cannot read metadata"]
        label = f"private/{path.parent.name}"
        if problems:
            count += 1
            print(f"MISSING   {label}")
            continue
        due = skill.due()
        if due < today:
            count += 1
            state = "OVERDUE"
        elif due <= warning:
            state = "DUE SOON"
        else:
            state = "OK"
        print(f"{state:<10}{label}: reviewed {skill.meta['reviewed']}, next {due}")
    return count


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", action="append", type=Path)
    parser.add_argument("--include-private", action="store_true")
    parser.add_argument("--check-links", action="store_true")
    parser.add_argument("--today", default=date.today().isoformat())
    parser.add_argument("--soon", type=int, default=7)
    args = parser.parse_args()
    today = date.fromisoformat(args.today)
    warning = today + timedelta(days=args.soon)
    failing = 0
    private_files = sorted(PRIVATE.glob("*/SKILL.md"))
    private_root = PRIVATE.resolve()
    private_by_target = {path.resolve(): path for path in private_files}
    checked_private = set()
    for root in args.root or [LIBRARY]:
        root = root.expanduser()
        paths = set(root.glob("**/SKILL.md")) | set(root.glob("*/SKILL.md"))
        for path in sorted(paths):
            if "/guides/" in path.as_posix():
                continue
            resolved = path.resolve()
            if resolved in private_by_target:
                checked_private.add(private_by_target[resolved])
                continue
            if resolved.is_relative_to(private_root):
                continue
            skill = read(path)
            label = path.parent.relative_to(root).as_posix()
            problems = skill.problems()
            due = skill.due()
            if problems:
                failing += 1
                print(f"MISSING   {label}: " + "; ".join(problems))
            elif due and due < today:
                failing += 1
                print(f"OVERDUE   {label}: due {due} ({(today - due).days} days ago), {skill.origin}")
            elif due and due <= warning:
                print(f"DUE SOON  {label}: due {due}, {skill.origin}")
            else:
                print(f"OK        {label}: reviewed {skill.meta['reviewed']}, next {due}, {skill.origin}")
            if skill.origin in {"external", "adapted"} and skill.meta.get("source"):
                print(f"          {skill.meta['source']} @ {skill.meta.get('source-ref', '?')}")
    if args.include_private:
        checked_private.update(private_files)
    failing += check_private(sorted(checked_private), today, warning)
    if args.check_links:
        failing += check_links(skills_under(LIBRARY), private_files, Path.home())
    return 1 if failing else 0


if __name__ == "__main__":
    sys.exit(main())
