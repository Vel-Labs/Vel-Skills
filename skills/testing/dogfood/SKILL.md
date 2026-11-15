---
name: "dogfood"
description: "Dogfood an application through independent first-time-user journeys in real browsers, consolidate evidence, and verify authorized fixes. Use for hands-on product dogfooding and launch-readiness checks."
metadata:
  origin: internal
  source: Vel-Skills
  created: "2026-10-28"
  reviewed: "2026-11-14"
  reviewed-by: Codex (GPT-6)
  review-every-days: "90"
  review-due: "2027-02-12"
  notes: Independent browser journeys with evidence and post-fix verification.
---

# Dogfood

## Purpose

Test a first-use browser journey through an observable result.

## Inputs

- Target build, journey, expected result, test data, and authorization described in [the run contract](references/run-contract.md).

## Outputs

- A consolidated report with persona evidence and any authorized verification.

## Non-goals

- Population research, inferred root causes presented as observations, or repairs outside the task.

Test the path from first encounter to an observable useful result. Keep persona
observations distinct from technical diagnosis and real-user research.

## Workflow

### Establish the run

Read [run-contract.md](references/run-contract.md). Infer the target, journey,
success criteria, and authority from the request and project context. Ask only
for missing information that blocks execution. A discussion about designing this
skill does not start an application test. An audit request does not authorize fixes.

Read [browser-execution.md](references/browser-execution.md) and only the relevant
driver reference. Verify actual capabilities before assigning work. Do not claim
a browser journey from source inspection, mocked interaction, or an API probe.

### Run independent journeys

Use these five profiles by default for a comprehensive run; honor a narrower or
different requested set:

- [Impatient](references/personas/impatient.md)
- [Skeptic](references/personas/skeptic.md)
- [Mobile](references/personas/mobile.md)
- [Literal reader](references/personas/literal-reader.md)
- [Breaker](references/personas/breaker.md)

Delegate independent observation when supported. Give each worker the run brief,
its profile, [evidence.md](references/evidence.md), the selected browser guidance,
and relevant project constraints. Prefer fresh context: omit source internals,
known defects, other findings, and suggested routes through the interface.
Workers own only their assigned session, test data, and evidence; they do not edit
application code, repair the environment, or operate another worker's surface.

Run in waves to fit worker capacity and verified browser isolation. If independent
agents are unavailable, run separate fresh sessions sequentially and disclose
that these are not independent-agent observations. Preserve baseline findings
before changing the app; do not mix pre-fix and post-fix builds in one cohort.

The coordinator applies the relevant [coverage checks](references/coverage.md)
separately. Do not count these checks as extra persona users.

### Consolidate and repair

Merge findings by supported root cause, retaining each observation and evidence
link. Rank by consequence, then affected/exposed personas and recovery cost.
These counts describe this run; they are not population failure rates.
Separate observed failure from inferred cause and proposed improvement.

When fixes are authorized, the coordinator owns integration. Inspect affected
callers and project rules, fix coherent causes in small batches, and run relevant
regressions. Preserve unrelated work. Resolve ambiguous intended behavior before
changing it; continue independent work when one issue is blocked. Do not silently
change success criteria, expected behavior, or fixtures to obtain a pass.

### Verify and report

After fixes, replay each original failure against the recorded expectation.
Also rerun the selected personas in fresh sessions and, where available, fresh
agents with the original brief and no defect/fix narrative. Hold the candidate
build stable during that cohort. If a new defect requires another change, record
the new revision and repeat affected checks; ensure the final selected journeys
refer to the same final candidate before claiming they passed together.

Verify resulting application state as well as screenshots. Technical inspection
may corroborate success after the UI journey; it must not secretly complete it.
Report resolved, remaining, new, blocked, and unverified findings with conditions
and evidence. Stop repeating an unchanged failure without a new hypothesis.
State which journeys passed on which build; do not equate that with universal
launch readiness or real-user comprehension.

Keep one consolidated report and the evidence it references in the project's
designated output location. Do not store run history inside this installed skill.

## Checks

- Run the [coverage checks](references/coverage.md) and verify application state on the final candidate.

## Failure modes & recovery

If browser isolation is unavailable, run separate fresh sessions sequentially. If a browser journey is blocked, record the condition and evidence and report it as unverified.
