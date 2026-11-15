---
name: "vercel-deploy"
description: "Deploy applications and websites to Vercel. Use when the user requests deployment actions like \"deploy my app\", \"deploy and give me the link\", \"push this live\", or \"create a preview deployment\"."
license: "Apache-2.0"
metadata:
  origin: adapted
  source: https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/vercel-deploy
  source-ref: 49f948faa9258a0c61caceaf225e179651397431
  created: "2026-01-31"
  reviewed: "2026-11-14"
  reviewed-by: Codex (GPT-6)
  review-every-days: "14"
  review-due: "2026-11-28"
  notes: Uses the authenticated Vercel CLI with telemetry disabled. Removed the relay that uploaded project archives.
---

## First: check this skill is still reviewed

Compare today's date with `review-due`. If overdue, tell the user when it was
reviewed and identify `source` and `source-ref`. Offer to review upstream.
If the user declines or is unavailable, use this pinned copy and report that
its review is overdue.

# Vercel Deploy

<!-- Vel-Skills added its review contract and portability or safety changes. -->

## Purpose

Deploy an authorized project through the installed Vercel CLI.

## Inputs

- Project or directory, requested environment, and authenticated local CLI.

## Non-goals

- Unauthenticated project uploads and production changes outside the request.

Deploy any project to Vercel instantly. **Always deploy as preview** (not production) unless the user explicitly asks for production.

## Prerequisites

Set `VERCEL_TELEMETRY_DISABLED=1` before invoking Vercel CLI. See [Vercel CLI telemetry](https://vercel.com/docs/cli/about-telemetry).

- Check whether the Vercel CLI is installed **without** escalated permissions (for example, `command -v vercel`).
- The deployment might take a few minutes. Use appropriate timeout values.

## Workflow

1. Check whether the Vercel CLI is installed (no escalation for this check):

```bash
command -v vercel
```

2. If `vercel` is installed, run this (with a 10 minute timeout):
```bash
vercel deploy [path] -y
```

**Important:** Use a 10 minute (600000ms) timeout for the deploy command since builds can take a while.

3. If the reviewed CLI is unavailable or returns an authentication error, report the missing prerequisite and wait for authorized access.

## Production Deploys

Only if user explicitly asks:
```bash
vercel deploy [path] --prod -y
```

## Outputs

Show the user the deployment URL.

Report deployment status from the CLI. Verify a URL only when the requested acceptance check calls for it.

## Failure modes & recovery

Check CLI authentication and network access. Retry only within the requested environment and preserve the exact deployment result.

## Checks

- Confirm the intended project and scope before deploying. Verify the result the CLI returns.
