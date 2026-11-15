---
name: "gh-address-comments"
description: "Help address review/issue comments on the open GitHub PR for the current branch using gh CLI; verify gh auth first and prompt the user to authenticate if not logged in."
license: "Apache-2.0"
metadata:
  origin: adapted
  source: https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/gh-address-comments
  source-ref: 49f948faa9258a0c61caceaf225e179651397431
  created: "2025-12-19"
  reviewed: "2026-11-14"
  reviewed-by: Codex (GPT-6)
  review-every-days: "30"
  review-due: "2026-12-14"
  notes: Fetches GitHub review threads. Disables CLI telemetry, removes host-specific escalation, and fixes duplicate pagination.
---

## First: check this skill is still reviewed

Compare today's date with `review-due`. If overdue, tell the user when it was
reviewed and identify `source` and `source-ref`. Offer to review upstream.
If the user declines or is unavailable, use this pinned copy and report that
its review is overdue.

# PR Comment Handler

<!-- Vel-Skills added its review contract and portability or safety changes. -->

## Purpose

Inspect a pull request’s comments and address the selected feedback.

## Inputs

Set `GH_TELEMETRY=false` for GitHub CLI commands. The bundled helper sets it for its own process calls.

- Repository checkout, authenticated GitHub CLI, and requested comment scope.

## Outputs

- Numbered comment summary and verified fixes for the chosen items.

## Non-goals

- Applying changes for comments outside the selected scope.

Authenticate with the installed GitHub CLI and confirm access with `gh auth status`.

## 1) Inspect comments needing attention
- Run scripts/fetch_comments.py which will print out all the comments and review threads on the PR

## 2) Ask the user for clarification
- Number all the review threads and comments and provide a short summary of what would be required to apply a fix for it
- Ask the user which numbered comments should be addressed

## 3) If user chooses comments
- Apply fixes for the selected comments

Notes:
- If gh hits auth/rate issues mid-run, prompt the user to re-authenticate with `gh auth login`, then retry.

## Workflow

Use the steps below.

## Checks

- Confirm the current PR, summarize only relevant content, and verify each fix.

## Failure modes & recovery

If authentication or a rate limit blocks retrieval, report the problem and retry after access is restored.
