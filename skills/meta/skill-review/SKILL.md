---
name: skill-review
description: Use when adding a skill to this library, when a skill's review is due or overdue, when importing a skill from another repository or vendor, or when rebuilding the skills index. Records where each skill came from and when it was last reviewed, checks review dates, and regenerates SKILLS_INDEX.md.
metadata:
  origin: internal
  source: Vel-Skills
  created: "2026-11-14"
  reviewed: "2026-11-14"
  reviewed-by: Claude Code (Opus 5.5)
  review-every-days: "90"
  review-due: "2027-02-12"
  notes: The library's review rule. Every skill records origin, review date and next review; external content is pinned, never fetched at runtime.
---

# Skill review

## Purpose

Skills drift. An external skill can change upstream, add data collection or
start running code; an internal one can fall behind the tools it describes. Every
skill in this library therefore records where it came from and when someone last
read it critically, and agents check that date when they use it.

## Inputs

- The skill folder(s) to add or review.
- For an external or adapted skill: the upstream repository or package, and the
  exact commit, tag or version being reviewed.
- [check_reviews.py](check_reviews.py), [build_index.py](build_index.py) and
  [skill_meta.py](skill_meta.py).

## Outputs

- Review metadata in each skill's frontmatter (below).
- For external and adapted skills, a "First: check this skill is still reviewed"
  section at the top of the body.
- A regenerated [SKILLS_INDEX.md](../../../SKILLS_INDEX.md) and README skills table.

## Non-goals

- Rewriting a skill's substance during a date-only review.
- Installing upstream plugins or running upstream CLIs.
- Publishing a skill that contains secrets, personal data or employer/client data.

## The metadata every skill carries

```yaml
metadata:
  origin: internal | external | adapted   # adapted = external content with local changes
  source: <upstream URL, or Vel-Skills>
  source-ref: <exact commit, tag or version>   # required for external and adapted
  created: "YYYY-MM-DD"                        # first added here, or best known date
  reviewed: "YYYY-MM-DD"
  reviewed-by: <person or agent>
  review-every-days: "<N>"                     # internal 90; external and adapted 14 to 30
  review-due: "YYYY-MM-DD"                     # reviewed + review-every-days
  notes: <one line for the index: what to know before using it>
```

Use `notes` for anything a person should see in the index at a glance, for
example "Upstream telemetry removed; guides only" or "Needs a paid API key".

## Workflow

### Adding a skill

1. Put it at `skills/<group>/<kebab-name>/` per [CONTRIBUTING.md](../../../CONTRIBUTING.md).
2. Fill in the metadata. For external or adapted content, record the
   redistribution license in top-level `license` and include required notices.
   Copy a pinned snapshot into the folder; do not fetch, `npx -y`, or run `@latest` at use time.
3. For external and adapted skills, start the body with the check section:
   compare today with `review-due`; if past, tell the person when it was last
   reviewed against which source and ref, and offer to review now; if they
   decline or nobody can be asked, use the pinned copy and report it overdue.
4. Note any upstream telemetry, network calls or runtime downloads, and what you
   removed, in `notes` and in the skill's boundaries.
5. Run `python3 skills/meta/skill-review/build_index.py` and
   `python3 skills/meta/skill-review/check_reviews.py` from the repository root.

### Reviewing a skill

1. Read the skill and what it points to. For external content, compare the pinned
   ref with upstream (use the skill's own refresh script if it has one) and read
   the changes.
2. Look for: wrong or stale guidance, new data collection or network calls, new
   instructions to run code, secrets or personal data, broken relative paths.
3. Fix or hold. Either way set `reviewed`, `reviewed-by` and `review-due`, and
   update `source-ref` if you adopted upstream changes.
4. Rebuild the index.

## Checks

- `python3 skills/meta/skill-review/check_reviews.py` exits 0 (no MISSING, no OVERDUE).
- `python3 skills/meta/skill-review/build_index.py --check` exits 0.
- External and adapted skills start with the review check section.
- No secrets, tokens, personal data or employer/client data in any skill.

## Failure modes & recovery

| What went wrong | How to recover |
| --- | --- |
| A skill's origin is unknown | Look for upstream text, licence headers or the folder it was copied from; if still unknown, mark `internal`, review it, and say "origin unknown" in `notes`. |
| `review-due` does not equal reviewed + interval | Recompute it; the checker prints the expected date. |
| Upstream added telemetry or runtime fetching | Hold the update, keep the pinned copy, record why in `notes`. |
| The index is out of date | Run `build_index.py`; never edit `SKILLS_INDEX.md` by hand. |
| An agent's local skills folder differs from this library | Run `check_reviews.py --root <that folder>` and reconcile from the library. |
