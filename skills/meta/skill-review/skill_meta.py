"""Shared reading of skill frontmatter for the skill-review helpers (standard library only)."""

import re
from dataclasses import dataclass, field
from datetime import date, timedelta
from pathlib import Path

ORIGINS = {"internal", "external", "adapted"}
REQUIRED = ["source", "created", "reviewed", "reviewed-by", "review-every-days", "review-due", "notes"]


@dataclass
class Skill:
    path: Path
    name: str
    description: str
    meta: dict[str, str] = field(default_factory=dict)
    license: str = ""

    @property
    def origin(self) -> str:
        return self.meta.get("origin", "")

    def problems(self) -> list[str]:
        """Missing or inconsistent review fields, in plain words."""
        found = []
        if self.origin not in ORIGINS:
            found.append(f"metadata.origin must be one of {sorted(ORIGINS)}")
        upstream = self.origin in {"external", "adapted"}
        required = REQUIRED + (["source-ref"] if upstream else [])
        missing = [key for key in required if not self.meta.get(key)]
        if missing:
            found.append("missing metadata: " + ", ".join(missing))
        if upstream and not self.license:
            found.append("missing license")
        dates = {}
        for key in ("created", "reviewed", "review-due"):
            if self.meta.get(key):
                try:
                    value = date.fromisoformat(self.meta[key])
                    if value.isoformat() != self.meta[key]:
                        raise ValueError
                    dates[key] = value
                except ValueError:
                    found.append(f"{key} must be YYYY-MM-DD")
        interval = self.meta.get("review-every-days")
        if interval and interval not in ({"14", "30"} if upstream else {"90"}):
            found.append("review-every-days must be 14 or 30 for upstream skills and 90 for internal skills")
        if not found:
            try:
                expected = dates["reviewed"] + timedelta(days=int(interval))
            except OverflowError:
                found.append("review interval falls outside the supported date range")
            else:
                if dates["review-due"] != expected:
                    found.append(f"review-due should be {expected} (reviewed + review-every-days)")
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
    return Skill(path, top.get("name", path.parent.name), top.get("description", ""), meta, top.get("license", ""))


def skills_under(root: Path) -> list[Skill]:
    return [read(p) for p in sorted(root.glob("**/SKILL.md")) if "/guides/" not in p.as_posix()]
