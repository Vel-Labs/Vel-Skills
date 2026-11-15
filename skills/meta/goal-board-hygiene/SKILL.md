---
name: "goal-board-hygiene"
description: "Audit and reconcile an existing oversized or structurally confused GoalBuddy board when phases, tasks, milestones, or planning ledgers no longer agree. Use for board hygiene, not ordinary goal creation, product planning, or implementation work."
metadata:
  origin: internal
  source: Vel-Skills
  created: "2026-08-24"
  reviewed: "2026-11-14"
  reviewed-by: Codex (GPT-6)
  review-every-days: "90"
  review-due: "2027-02-12"
  notes: Reconciles GoalBuddy plans and boards while preserving task IDs and evidence.
---

# Goal Board Hygiene

## Purpose

Audit and reconcile an existing GoalBuddy board.

## Inputs

- Parent board, implementation plan, child boards, checker contract, and authorization.

## Outputs

- Bounded dispositions and [one reconciliation receipt](references/reconciliation-receipt.md).

## Non-goals

- Creating competing goals, choosing strategy, or changing implementation scope.

Preserve one canonical board while you make its execution structure easier to
understand. Do not use this skill to create a competing goal, choose product
strategy, or change implementation scope.

## Workflow

### Route The Request

Use this skill when an existing GoalBuddy board has one or more of these signs:

- phase containers and executable tasks use the same identity level;
- an implementation plan names milestones that are not visible on the board;
- a Markdown plan ledger is stale relative to live board tasks;
- repair rounds, evidence items, or nested substeps have become board-visible
  identities;
- the board is too large to show the current phase, authority, and proof gate
  clearly.

For a healthy board or a request to create a new goal, use the normal GoalBuddy
workflow. Route source changes, product decisions, and repository cleanup to
their owning workflows.

## Establish The Boundary

Open the canonical parent `goal.md` and `state.yaml`, the visible implementation
plan, referenced child boards, and the official checker contract. Identify the
current active task, authority holder, candidate identity, dirty-path ownership,
and any concurrent writer.

The execution boundary is stable only when:

- one parent board is canonical;
- current authority and the active task agree;
- the candidate or proof identity is recorded and will not change during the
  migration;
- affected board files have one writer and unrelated dirty work can remain
  untouched;
- the intended parent-to-child relationship and rollback path are explicit.

If any condition is false or uncertain, stop at a read-only audit and proposal.
Record the uncertainty. Preserve the current board and active authority. Do not
create a board, move an entry, or rewrite history.

## Audit Before Reconciliation

Compare the implementation plan with every visible parent and child task. For
each plan item or board entry, record its source, current identity, owner,
status, candidate or proof reference, and whether it is visible in both views.
Detect:

- phase/task conflation;
- hidden milestones that exist only in prose or a plan ledger;
- stale planned entries that no longer match the live board;
- excessive identity depth below parent phase and one depth-one child board;
- duplicate, superseded, deferred, or completed work that still appears active.

Do not infer completion from prose, file presence, or a passing lower proof
gate. Preserve exact task IDs, receipts, candidate hashes, and decision history.

## Classify Each Entry

Assign exactly one disposition:

- `keep`: retain the entry and its identity at its current level;
- `move`: place executable work on the depth-one child board without changing
  its evidence or authority;
- `compact`: retain the history and result in a rollup or receipt while removing
  unnecessary board-visible detail;
- `supersede`: preserve the old identity and link it to the replacement;
- `defer`: keep the item visible as non-active work with its reason and return
  condition;
- `remove-with-receipt`: remove only a proven redundant entry after the receipt
  records its former identity, evidence, reason, and recovery source.

When evidence is incomplete, use `keep` or `defer`. Never erase history to make
the board smaller.

## Reconcile A Stable Board

Keep the existing parent board canonical. Propose or create one depth-one child
board for the current phase when executable tasks need separation. Do not create
a second parent board or deeper hierarchy. Preserve the active task and
authority unless the governing workflow explicitly authorizes a transition.

Apply the accepted dispositions as one bounded migration. Update the parent
phase status, completed and total milestone counts, current milestone, next
milestone, blocker, and latest accepted receipt from the child rollup. Keep
deferred and superseded counts consistent. Do not touch unrelated dirty files.

Produce one reconciliation receipt. Read
[the reconciliation receipt template](references/reconciliation-receipt.md)
when preparing the proposal or migration record. Do not create parallel
scratchpads or duplicate ledgers.

## Checks

Run the official GoalBuddy checker against the parent board and the affected
child board. Inspect both rendered task lists and confirm:

- there is one canonical parent and no competing board;
- there is at most one active task on each board;
- the child is depth one and its parent link is correct;
- parent progress and status equal the child rollup;
- every moved, compacted, superseded, deferred, or removed identity is
  recoverable from the reconciliation receipt;
- active authority, candidate identity, and unrelated dirty work did not change.

Treat checker success as structural proof only. Report unresolved semantic or
ownership conflicts as blockers. Do not claim implementation, release, or
acceptance proof from board reconciliation.

## Failure modes & recovery

If single-writer ownership, proof identity, or rollback is uncertain, stop at a read-only proposal.
