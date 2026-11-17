---
name: supabase-postgres-best-practices
description: Use before writing or changing anything that lives in a Postgres database (on Supabase or anywhere else) and when diagnosing database problems. Covers creating or altering tables and columns, choosing column types, constraints and migrations, indexes, queries and pagination, batch writes and upserts, locking and queue processing, connection pooling and limits, privileges and row-level security, and slow queries, EXPLAIN plans, bloat or connection exhaustion. A pinned, reviewed copy of Supabase's Postgres rules with incorrect and correct SQL for each.
license: MIT for the rule files (see LICENSE, copyright 2026 Supabase); the wrapper is part of Vel-Skills.
metadata:
  origin: adapted
  source: https://github.com/supabase/agent-skills
  source-ref: c9be0e931b7930f7d02126d04774d904c381e7d7 (main after v0.1.9, 2026-10-02; skill 1.6.0)
  created: "2026-11-17"
  reviewed: "2026-11-17"
  reviewed-by: Claude Code (Opus 5.5)
  review-every-days: "30"
  review-due: "2026-12-17"
  notes: Rule files only, unchanged. Not installed with npx skills add (the skills CLI and plugin marketplace are not used); upstream authoring templates and changelog left out. No scripts, telemetry or runtime fetches.
---

# Supabase Postgres best practices (pinned copy)

## First: check this skill is still reviewed

This skill is adapted from an external repository. Before relying on it, compare
today's date with `review-due` above.

- **On or before the due date:** use the skill.
- **After the due date:** tell the person, before doing the task:
  "Supabase Postgres best practices was last reviewed on <reviewed> against
  <source> at <source-ref>. Its review was due on <review-due>. Shall I check
  upstream for changes now?" If they agree, follow **Reviewing this skill**
  below. If they decline, or nobody can be asked, use the pinned copy and say in
  your report that the review is overdue.

The `meta/skill-review` skill lists every skill's review state at once.

## Purpose

Give agents concrete Postgres rules for schema design, migrations, queries,
indexes, locking, connections and security. Each rule file shows the wrong
pattern first, then the right one, with its impact. The rules apply to any
Postgres; a few carry Supabase-specific notes.

## Inputs

- The task: the table, migration, query or database problem in hand.
- The rule files under [references/](references/), listed below.
- [references/_sections.md](references/_sections.md): the eight categories and
  their priority.
- The project's own database conventions, migration process and data rules.
  These take precedence over a general rule when they conflict; say so in the
  report.

## Outputs

- SQL, schema and migration changes that follow the matching rules.
- One line per rule used in the report: which rule, and the problem it avoided.

## Non-goals

- Supabase platform work (Data API exposure, CLI, MCP server, Auth, Storage):
  use `data/supabase-platform`.
- Running SQL against a hosted or shared database. This skill guides what to
  write; the task's own authority decides where it runs.
- Installing the upstream plugin or running `npx skills add`.

## Workflow

1. Match the task to categories. Read the higher-priority categories first:

   | Priority | Category | Prefix |
   | --- | --- | --- |
   | 1 | Query performance | `query-` |
   | 2 | Connection management | `conn-` |
   | 3 | Security and RLS | `security-` |
   | 4 | Schema design | `schema-` |
   | 5 | Concurrency and locking | `lock-` |
   | 6 | Data access patterns | `data-` |
   | 7 | Monitoring and diagnostics | `monitor-` |
   | 8 | Advanced features | `advanced-` |

2. Open the matching rule files from the table below and read them in full.
3. Apply the correct pattern. For a migration on an existing table, always read
   [schema-constraints](references/schema-constraints.md) and
   [lock-short-transactions](references/lock-short-transactions.md).
4. Apply the RLS rules only where the project uses row-level security. When the
   database is reached only by a trusted server role, least privilege
   ([security-privileges](references/security-privileges.md)) still applies.
5. Name the rules used in the report.

### Rule files

| Rule | Title |
| --- | --- |
| [advanced-full-text-search](references/advanced-full-text-search.md) | Use tsvector for Full-Text Search |
| [advanced-jsonb-indexing](references/advanced-jsonb-indexing.md) | Index JSONB Columns for Efficient Querying |
| [conn-idle-timeout](references/conn-idle-timeout.md) | Configure Idle Connection Timeouts |
| [conn-limits](references/conn-limits.md) | Set Appropriate Connection Limits |
| [conn-pooling](references/conn-pooling.md) | Use Connection Pooling for All Applications |
| [conn-prepared-statements](references/conn-prepared-statements.md) | Use Prepared Statements Correctly with Pooling |
| [data-batch-inserts](references/data-batch-inserts.md) | Batch INSERT Statements for Bulk Data |
| [data-n-plus-one](references/data-n-plus-one.md) | Eliminate N+1 Queries with Batch Loading |
| [data-pagination](references/data-pagination.md) | Use Cursor-Based Pagination Instead of OFFSET |
| [data-upsert](references/data-upsert.md) | Use UPSERT for Insert-or-Update Operations |
| [lock-advisory](references/lock-advisory.md) | Use Advisory Locks for Application-Level Locking |
| [lock-deadlock-prevention](references/lock-deadlock-prevention.md) | Prevent Deadlocks with Consistent Lock Ordering |
| [lock-short-transactions](references/lock-short-transactions.md) | Keep Transactions Short to Reduce Lock Contention |
| [lock-skip-locked](references/lock-skip-locked.md) | Use SKIP LOCKED for Non-Blocking Queue Processing |
| [monitor-explain-analyze](references/monitor-explain-analyze.md) | Use EXPLAIN ANALYZE to Diagnose Slow Queries |
| [monitor-pg-stat-statements](references/monitor-pg-stat-statements.md) | Enable pg_stat_statements for Query Analysis |
| [monitor-vacuum-analyze](references/monitor-vacuum-analyze.md) | Maintain Table Statistics with VACUUM and ANALYZE |
| [query-composite-indexes](references/query-composite-indexes.md) | Create Composite Indexes for Multi-Column Queries |
| [query-covering-indexes](references/query-covering-indexes.md) | Use Covering Indexes to Avoid Table Lookups |
| [query-index-types](references/query-index-types.md) | Choose the Right Index Type for Your Data |
| [query-missing-indexes](references/query-missing-indexes.md) | Add Indexes on WHERE and JOIN Columns |
| [query-partial-indexes](references/query-partial-indexes.md) | Use Partial Indexes for Filtered Queries |
| [schema-constraints](references/schema-constraints.md) | Add Constraints Safely in Migrations |
| [schema-data-types](references/schema-data-types.md) | Choose Appropriate Data Types |
| [schema-foreign-key-indexes](references/schema-foreign-key-indexes.md) | Index Foreign Key Columns |
| [schema-lowercase-identifiers](references/schema-lowercase-identifiers.md) | Use Lowercase Identifiers for Compatibility |
| [schema-partitioning](references/schema-partitioning.md) | Partition Large Tables for Better Performance |
| [schema-primary-keys](references/schema-primary-keys.md) | Select Optimal Primary Key Strategy |
| [security-privileges](references/security-privileges.md) | Apply Principle of Least Privilege |
| [security-rls-basics](references/security-rls-basics.md) | Enable Row Level Security for Multi-Tenant Data |
| [security-rls-performance](references/security-rls-performance.md) | Optimize RLS Policies for Performance |

### Reviewing this skill

1. Read upstream on github.com, or clone it into an empty temporary folder. Do
   not install it, and do not run its package scripts.
2. Compare `skills/supabase-postgres-best-practices/` at the new commit with
   `source-ref`, for example
   `git diff <source-ref> <new-sha> -- skills/supabase-postgres-best-practices`.
3. Look for wrong or stale guidance, new rule files, and any new instruction to
   run code, send data, file issues or fetch at runtime.
4. On approval, copy the changed rule files into [references/](references/)
   unchanged, update the rule table, then update `source-ref`, `reviewed`,
   `reviewed-by` and `review-due` and rebuild the library index.
5. If you hold the update, still update `reviewed` and `review-due` and say why.

## Checks

- The review is not overdue, or the person was told and chose how to proceed.
- Every rule named in the report exists under [references/](references/).
- New indexes on large, live tables use `create index concurrently`, and new
  constraints on existing tables follow
  [schema-constraints](references/schema-constraints.md).
- Files under [references/](references/) were not edited by hand.

## Failure modes & recovery

| What went wrong | How to recover |
| --- | --- |
| No rule matches the task | Use the category table to find the nearest rule; if nothing fits, follow the Postgres manual and say so. |
| A rule conflicts with the project's conventions | Follow the project and record the conflict in the report. |
| A rule assumes Supabase Auth or RLS the project does not use | Apply only the general Postgres part (privileges, indexes on policy columns). |
| The review is overdue and nobody can be asked | Use the pinned copy and report that the review is overdue. |
| Upstream adds a script, telemetry or a runtime fetch | Hold the update and record why in `notes`. |

## Associated files

- [references/](references/): upstream rule files at `source-ref`, unchanged.
  Upstream's `_contributing.md` and `_template.md` (authoring guides) are left out.
- [LICENSE](LICENSE): the upstream MIT licence.
