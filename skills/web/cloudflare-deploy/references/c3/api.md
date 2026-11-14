<!-- Vel-Skills removed implicit CLI downloads and remote shell execution. -->
# C3 CLI Reference

## Invocation

```bash
create-cloudflare [name] [-- flags]  # NPM requires --
create-cloudflare [name] [flags]
pcreate-cloudflare [name] [-- flags]
```

## Core Flags

| Flag | Values | Description |
|------|--------|-------------|
| `--type` | `hello-world`, `web-app`, `demo`, `pre-existing`, `remote-template` | Application type |
| `--platform` | `workers` (default), `pages` | Target platform |
| `--framework` | `next`, `remix`, `astro`, `react-router`, `solid`, `svelte`, `qwik`, `vue`, `angular`, `hono` | Web framework (requires `--type=web-app`) |
| `--lang` | `ts`, `js`, `python` | Language (for `--type=hello-world`) |
| `--ts` / `--no-ts` | - | TypeScript for web apps |

## Deployment Flags

| Flag | Description |
|------|-------------|
| `--deploy` / `--no-deploy` | Deploy immediately (prompts interactive, skips in CI) |
| `--git` / `--no-git` | Initialize git (default: yes) |
| `--open` | Open browser after deploy |

## Advanced Flags

| Flag | Description |
|------|-------------|
| `--template=user/repo` | GitHub template or local path |
| `--existing-script=./src/worker.ts` | Existing script (requires `--type=pre-existing`) |
| `--category=ai\|database\|realtime` | Demo filter (requires `--type=demo`) |
| `--experimental` | Enable experimental features |
| `--wrangler-defaults` | Skip wrangler prompts |

## Environment Variables

```bash
CLOUDFLARE_API_TOKEN=xxx    # For deployment
CLOUDFLARE_ACCOUNT_ID=xxx   # Account ID
CF_TELEMETRY_DISABLED=1     # Disable telemetry
```

## Exit Codes

`0` success, `1` user abort, `2` error

## Examples

```bash
# TypeScript Worker
create-cloudflare my-api -- --type=hello-world --lang=ts --no-deploy

# Next.js on Pages
create-cloudflare my-app -- --type=web-app --framework=next --platform=pages --ts

# Astro blog
create-cloudflare my-blog -- --type=web-app --framework=astro --ts --deploy

# CI: non-interactive
create-cloudflare my-app -- --type=web-app --framework=next --ts --no-git --no-deploy

# GitHub template
create-cloudflare -- --template=cloudflare/templates/worker-openapi

# Convert existing project
create-cloudflare . -- --type=pre-existing --existing-script=./build/worker.js
```
