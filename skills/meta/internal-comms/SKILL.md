---
name: "internal-comms"
description: "A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. Claude should use this skill whenever asked to write some sort of internal communications (status reports, leadership updates, 3P updates, company newsletters, FAQs, incident reports, project updates, etc.)."
license: "Apache-2.0"
metadata:
  origin: external
  source: https://github.com/anthropics/skills/tree/ef740771ac901e03fbca3ce4e1c453a96010f30a/skills/internal-comms
  source-ref: ef740771ac901e03fbca3ce4e1c453a96010f30a
  created: "2025-10-15"
  reviewed: "2026-11-14"
  reviewed-by: Codex (GPT-6)
  review-every-days: "30"
  review-due: "2026-12-14"
  notes: Uses Anthropic’s format examples for internal status and announcement drafts.
---

## First: check this skill is still reviewed

Compare today's date with `review-due`. If overdue, tell the user when it was
reviewed and identify `source` and `source-ref`. Offer to review upstream.
If the user declines or is unavailable, use this pinned copy and report that
its review is overdue.

# Internal Comms

## Inputs

- Audience, communication type, and approved source facts.

## Outputs

- A reviewable internal draft.

## Non-goals

- Sending the draft or disclosing material outside its audience.

<!-- Vel-Skills added its review contract and portability or safety changes. -->

## Purpose

To write internal communications, use this skill for:
- 3P updates (Progress, Plans, Problems)
- Company newsletters
- FAQ responses
- Status reports
- Leadership updates
- Project updates
- Incident reports

## Workflow

To write any internal communication:

1. **Identify the communication type** from the request
2. **Load the appropriate guideline file** from the `examples/` directory:
    - `examples/3p-updates.md` - For Progress/Plans/Problems team updates
    - `examples/company-newsletter.md` - For company-wide newsletters
    - `examples/faq-answers.md` - For answering frequently asked questions
    - `examples/general-comms.md` - For anything else that doesn't explicitly match one of the above
3. **Follow the specific instructions** in that file for formatting, tone, and content gathering

If the communication type doesn't match any existing guideline, ask for clarification or more context about the desired format.

## Keywords
3P updates, company newsletter, company comms, weekly update, faqs, common questions, updates, internal comms

## Checks

- Check facts and audience fit with the selected examples.

## Failure modes & recovery

If no template fits, clarify the audience and purpose before drafting.
