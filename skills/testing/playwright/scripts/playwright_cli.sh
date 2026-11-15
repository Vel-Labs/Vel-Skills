#!/usr/bin/env bash
set -euo pipefail

# Vel-Skills uses a preinstalled CLI and avoids downloading packages.

if ! command -v playwright-cli >/dev/null 2>&1; then
  echo "Error: Use a reviewed installation of playwright-cli on PATH." >&2
  exit 1
fi

has_session_flag="false"
for arg in "$@"; do
  case "$arg" in
    --session|--session=*)
      has_session_flag="true"
      break
      ;;
  esac
done

cmd=(playwright-cli)
if [[ "${has_session_flag}" != "true" && -n "${PLAYWRIGHT_CLI_SESSION:-}" ]]; then
  cmd+=(--session "${PLAYWRIGHT_CLI_SESSION}")
fi
cmd+=("$@")

exec "${cmd[@]}"
