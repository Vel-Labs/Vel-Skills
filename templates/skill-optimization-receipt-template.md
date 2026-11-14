# Skill Optimization Receipt Template

Use this sidecar when a non-trivial skill change is based on observed agent
successes, failures, human feedback, paper learnings, or repeated workflow
friction. Store it near the skill when practical, for example:

```text
skills/<group>/<skill-name>/optimization/YYYY-MM-DD-short-topic.md
```

```md
# Skill Optimization Receipt

Date:
Skill:
Change type: add | delete | replace | restructure | no-change
Status: proposed | accepted | rejected | deferred

## Trigger

What observation, paper, report, failure, success, or human feedback prompted
this candidate change?

## Evidence Sources

- <file, report, command output, issue, review queue item, or user note>

## Failure Patterns

- <recurring error, hidden trust, drift, overclaim, missing gate, or confusing route>

## Success Patterns To Preserve

- <behavior already working and worth keeping>

## Candidate Edits

Edit budget:

```text
1-3 focused edits unless the existing skill is structurally broken.
```

Proposed edits:

- add:
- delete:
- replace:

## Rejected Edits

- <edit not accepted and why>

## Validation Gate

Held-out surface:

- <fixture, representative task, command, report, dashboard, review queue item>

Commands or checks:

```bash
<command>
```

Result:

- passed | failed | skipped with reason

## Accepted Outcome

What changed in the skill, and why is it safer or more useful?

## Remaining Risks

- <risk, review item, or follow-up>
```
