"""Shared reading of skill frontmatter for the skill-review helpers (standard library only)."""

import re
from dataclasses import dataclass, field
from datetime import date, timedelta
from pathlib import Path

ORIGINS = {"internal", "external", "adapted"}
DATED = ["created", "reviewed", "review-every-days", "review-due"]
UPSTREAM = ["source", "source-ref"]


@dataclass
class Skill:
    path: Path
    name: str
    description: str
    meta: dict[str, str] = field(default_factory=dict)

    @property
    def origin(self) -> str:
        return self.meta.get("origin", "")

    def problems(self) -> list[str]:
        """Missing or inconsistent review fields, in plain words."""
        found = []
        if self.origin not in ORIGINS:
            found.append(f"metadata.origin must be one of {sorted(ORIGINS)}")
        required = DATED + (UPSTREAM if self.origin in {"external", "adapted"} else [])
        missing = [key for key in required if not self.meta.get(key)]
        if missing:
            found.append("missing metadata: " + ", ".join(missing))
        try:
            reviewed = date.fromisoformat(self.meta["reviewed"])
            every = int(self.meta["review-every-days"])
            due = date.fromisoformat(self.meta["review-due"])
            if due != reviewed + timedelta(days=every):
                found.append(f"review-due should be {reviewed + timedelta(days=every)} (reviewed + review-every-days)")
        except (KeyError, ValueError):
            pass
        return found

    def due(self) -> date | None:
        try:
            return date.fromisoformat(self.meta["review-due"])
        except (KeyError, ValueError):
            return None


def read(path: Path) -> Skill:
    """Read `name`, `description` and the one-level `metadata:` map from SKILL.md."""
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---", text, re.S)
    top: dict[str, str] = {}
    meta: dict[str, str] = {}
    if match:
        in_meta = False
        for line in match.group(1).splitlines():
            if re.match(r"^metadata:\s*$", line):
                in_meta = True
                continue
            nested = re.match(r"^\s{2,}([\w-]+):\s*(.*)$", line)
            plain = re.match(r"^([\w-]+):\s*(.*)$", line)
            if in_meta and nested:
                meta[nested.group(1)] = nested.group(2).strip().strip('"')
            elif plain:
                in_meta = False
                top[plain.group(1)] = plain.group(2).strip().strip('"')
    return Skill(path, top.get("name", path.parent.name), top.get("description", ""), meta)


def skills_under(root: Path) -> list[Skill]:
    return [read(p) for p in sorted(root.glob("**/SKILL.md")) if "/guides/" not in p.as_posix()]
