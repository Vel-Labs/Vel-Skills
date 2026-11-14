# Goal Board Reconciliation Receipt

Use one receipt for the audit, accepted migration, and rollback record. Omit a
migration result when the execution boundary is unstable.

```yaml
goal_board_reconciliation_receipt_v1:
  result: proposed | reconciled | blocked
  recorded_at: "<ISO-8601 timestamp>"
  canonical_parent:
    board_path: "<path to parent state.yaml>"
    goal_id: "<stable goal identity>"
    candidate_identity: "<hash, version, receipt, or none>"
  execution_boundary:
    stable: true | false
    active_task: "<task ID or null>"
    authority_holder: "<role or actor>"
    sole_writer: "<role or actor, or unknown>"
    dirty_ownership: "<known, unknown, or not applicable>"
    rollback_source: "<path, commit, receipt, or none>"
    blockers: []
  compared_sources:
    implementation_plans: []
    parent_board: "<path>"
    child_boards: []
  findings:
    phase_task_conflation: []
    hidden_milestones: []
    stale_plan_entries: []
    excessive_identity_depth: []
  dispositions:
    - identity: "<original phase, task, or milestone ID>"
      source: "<plan or board path>"
      disposition: keep | move | compact | supersede | defer | remove-with-receipt
      destination_or_replacement: "<path or identity, or null>"
      evidence: []
      reason: "<short reason>"
      recovery_source: "<path, receipt, or null>"
  child_board:
    action: none | propose | create | update
    path: "<depth-one child path or null>"
    parent_link_verified: true | false | not_applicable
  parent_rollup:
    before: {}
    after: {}
    child_receipt: "<receipt identity or null>"
  validation:
    parent_checker:
      command: "<exact command>"
      result: pass | fail | not_run
    child_checker:
      command: "<exact command or null>"
      result: pass | fail | not_applicable | not_run
    semantic_review:
      result: pass | fail | blocked
      unresolved_conflicts: []
  changed_files: []
  history_preserved: true | false
  candidate_identity_preserved: true | false
  unrelated_dirty_work_preserved: true | false
  remaining_risks: []
```

For a proposal or blocked result, set `execution_boundary.stable` to `false`,
list the blockers, keep `child_board.action` as `none` or `propose`, and do not
record board files in `changed_files`.
