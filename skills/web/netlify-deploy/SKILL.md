---
name: "netlify-deploy"
description: "Deploy web projects to Netlify using the Netlify CLI (`netlify`). Use when the user asks to deploy, host, publish, or link a site/repo on Netlify, including preview and production deploys."
license: "Apache-2.0"
metadata:
  origin: adapted
  source: https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/netlify-deploy
  source-ref: 49f948faa9258a0c61caceaf225e179651397431
  created: "2026-01-31"
  reviewed: "2026-11-14"
  reviewed-by: Codex (GPT-6)
  review-every-days: "14"
  review-due: "2026-11-28"
  notes: Uses a preinstalled Netlify CLI with telemetry disabled. Removed implicit CLI downloads.
---

## First: check this skill is still reviewed

Compare today's date with `review-due`. If overdue, tell the user when it was
reviewed and identify `source` and `source-ref`. Offer to review upstream.
If the user declines or is unavailable, use this pinned copy and report that
its review is overdue.

# Netlify Deployment Skill

## Inputs

- Project, target site and environment, authorized account, and a reviewed Netlify CLI on PATH.

## Outputs

- Deployment URL, deployment ID when available, and any dashboard follow-up.

## Non-goals

- Production deploys outside the user’s authorization.

Deploy web projects to Netlify using the Netlify CLI with intelligent detection of project configuration and deployment context.

<!-- Vel-Skills added its review contract and portability or safety changes. -->

## Purpose

This skill automates Netlify deployments by:
- Verifying Netlify CLI authentication
- Detecting project configuration and framework
- Linking to existing sites or creating new ones
- Deploying to production or preview environments

## Prerequisites

Set `NETLIFY_TELEMETRY_DISABLED=1` for the shell used by all examples. See [Netlify CLI telemetry](https://github.com/netlify/cli/blob/main/CONTRIBUTING.md#telemetry).

- **Netlify CLI**: A reviewed Netlify CLI already on PATH
- **Authentication**: Netlify account with active login session
- **Project**: Valid web project in current directory
- When sandboxing blocks the deployment network calls, rerun with `sandbox_permissions=require_escalated`.
- The deployment might take a few minutes. Use appropriate timeout values.

## Authentication Pattern

The skill uses the **pre-authenticated Netlify CLI** approach:

1. Check authentication status with `netlify status`
2. If not authenticated, guide user through `netlify login`
3. Fail gracefully if authentication cannot be established

Authentication uses either:
- **Browser-based OAuth** (primary): `netlify login` opens browser for authentication
- **API Key** (alternative): Set `NETLIFY_AUTH_TOKEN` environment variable

## Workflow

### 1. Verify Netlify CLI Authentication

Check if the user is logged into Netlify:

```bash
netlify status
```

**Expected output patterns**:
- ✅ Authenticated: Shows logged-in user email and site link status
- ❌ Not authenticated: "Not logged into any site" or authentication error

**If not authenticated**, guide the user:

```bash
netlify login
```

This opens a browser window for OAuth authentication. Wait for user to complete login, then verify with `netlify status` again.

**Alternative: API Key authentication**

If browser authentication isn't available, users can set:

```bash
export NETLIFY_AUTH_TOKEN=your_token_here
```

Tokens can be generated at: https://app.netlify.com/user/applications#personal-access-tokens

### 2. Detect Site Link Status

From `netlify status` output, determine:
- **Linked**: Site already connected to Netlify (shows site name/URL)
- **Not linked**: Need to link or create site

### 3. Link to Existing Site or Create New

**If already linked** → Skip to step 4

**If not linked**, attempt to link by Git remote:

```bash
# Check if project is Git-based
git remote show origin

# If Git-based, extract remote URL
# Format: https://github.com/username/repo or git@github.com:username/repo.git

# Try to link by Git remote
netlify link --git-remote-url <REMOTE_URL>
```

**If link fails** (site doesn't exist on Netlify):

```bash
# Create new site interactively
netlify init
```

This guides user through:
1. Choosing team/account
2. Setting site name
3. Configuring build settings
4. Creating netlify.toml if needed

### 4. Verify Dependencies

Before deploying, ensure project dependencies are installed:

```bash
# For npm projects
npm ci

# For other package managers, detect and use appropriate command
# yarn install, pnpm ci, etc.
```

### 5. Deploy to Netlify

Choose deployment type based on context:

**Preview/Draft Deploy** (default for existing sites):

```bash
netlify deploy
```

This creates a deploy preview with a unique URL for testing.

**Production Deploy** (for new sites or explicit production deployments):

```bash
netlify deploy --prod
```

This deploys to the live production URL.

**Deployment process**:
1. CLI detects build settings (from netlify.toml or prompts user)
2. Builds the project locally
3. Uploads built assets to Netlify
4. Returns deployment URL

### 6. Report Results

After deployment, report to user:
- **Deploy URL**: Unique URL for this deployment
- **Site URL**: Production URL (if production deploy)
- **Deploy logs**: Link to Netlify dashboard for logs
- **Next steps**: Suggest `netlify open` to view site or dashboard

## Handling netlify.toml

If a `netlify.toml` file exists, the CLI uses it automatically. If not, the CLI will prompt for:
- **Build command**: e.g., `npm run build`, `next build`
- **Publish directory**: e.g., `dist`, `build`, `.next`

Common framework defaults:
- **Next.js**: build command `npm run build`, publish `.next`
- **React (Vite)**: build command `npm run build`, publish `dist`
- **Static HTML**: no build command, publish current directory

The skill should detect framework from `package.json` if possible and suggest appropriate settings.

## Example Full Workflow

```bash
# 1. Check authentication
netlify status

# If not authenticated:
netlify login

# 2. Link site (if needed)
# Try Git-based linking first
git remote show origin
netlify link --git-remote-url https://github.com/user/repo

# If no site exists, create new one:
netlify init

# 3. Install dependencies
npm ci

# 4. Deploy (preview for testing)
netlify deploy

# 5. Deploy to production (when ready)
netlify deploy --prod
```

## Failure modes & recovery

Common issues and solutions:

**"Not logged in"**
→ Run `netlify login`

**"No site linked"**
→ Run `netlify link` or `netlify init`

**"Build failed"**
→ Check build command and publish directory in netlify.toml or CLI prompts
→ Verify dependencies are installed
→ Review build logs for specific errors

**"Publish directory not found"**
→ Verify build command ran successfully
→ Check publish directory path is correct

## Troubleshooting

### Escalated Network Access

If deployment fails due to network issues (timeouts, DNS errors, connection resets), rerun the deploy with escalated permissions (use `sandbox_permissions=require_escalated`). The deploy requires escalated network access when sandbox networking blocks outbound requests.

Example guidance to the user:

```
The deploy needs escalated network access to deploy to Netlify. I can rerun the command with escalated permissions—want me to proceed?
```

## Environment Variables

For secrets and configuration:

1. Never commit secrets to Git
2. Set in Netlify dashboard: Site Settings → Environment Variables
3. Access in builds via `process.env.VARIABLE_NAME`

## Tips

- Use `netlify deploy` (no `--prod`) first to test before production
- Run `netlify open` to view site in Netlify dashboard
- Run `netlify logs` to view function logs (if using Netlify Functions)
- Use `netlify dev` for local development with Netlify Functions

## Reference

- Netlify CLI Docs: https://docs.netlify.com/cli/get-started/
- netlify.toml Reference: https://docs.netlify.com/configure-builds/file-based-configuration/

## Bundled References (Load As Needed)

- [CLI commands](references/cli-commands.md)
- [Deployment patterns](references/deployment-patterns.md)
- [netlify.toml guide](references/netlify-toml.md)

## Checks

- Check the output directory, intended site, and returned deployment state.
