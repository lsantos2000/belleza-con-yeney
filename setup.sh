#!/usr/bin/env bash
# Install dependencies and synchronize shared assets for local development.
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")"

REQUIRED_NODE="22.13.0"

if ! command -v node >/dev/null 2>&1; then
  echo "Error: Node.js is not installed. Install Node.js ${REQUIRED_NODE} or newer." >&2
  exit 1
fi

CURRENT_NODE="$(node -v)"
CURRENT_NODE="${CURRENT_NODE#v}"
if [ "$(printf '%s\n%s\n' "$REQUIRED_NODE" "$CURRENT_NODE" | sort -V | head -n1)" != "$REQUIRED_NODE" ]; then
  echo "Error: Node.js ${REQUIRED_NODE} or newer is required, but ${CURRENT_NODE} is active." >&2
  exit 1
fi
echo "Node.js ${CURRENT_NODE} detected."

if ! command -v pnpm >/dev/null 2>&1; then
  echo "Error: pnpm is not installed. Run 'corepack enable pnpm' or 'npm install -g pnpm'." >&2
  exit 1
fi
echo "pnpm $(pnpm --version) detected."

# 'allowBuilds' in pnpm-workspace.yaml still holds placeholder values, so pnpm
# refuses to finish the install. Downgrade that condition to a warning until the
# entries are answered with 'pnpm approve-builds'.
echo "Installing dependencies..."
pnpm --config.strict-dep-builds=false install

echo "Synchronizing shared resources into public web paths..."
node tools/sync-public-assets.mjs

echo
echo "Setup complete. Start the local site with:"
echo "  ./dev.sh          Development server with hot reload"
echo "  ./dev.sh --prod   Production build served locally"
