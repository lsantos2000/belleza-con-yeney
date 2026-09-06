#!/usr/bin/env bash
# Run the YeneyWellness site locally.
#   ./dev.sh                Development server with hot reload
#   ./dev.sh --prod         Production build, then serve it locally
#   ./dev.sh --port 4000    Listen on a different port
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")"

PORT=3000
MODE="dev"

while [ $# -gt 0 ]; do
  case "$1" in
    --prod|--production) MODE="prod"; shift ;;
    --port|-p) PORT="${2:?--port requires a value}"; shift 2 ;;
    -h|--help)
      sed -n '2,6p' "$0" | sed 's/^# \{0,1\}//'
      exit 0 ;;
    *) echo "Error: unknown option '$1'." >&2; exit 1 ;;
  esac
done

if [ ! -d node_modules ]; then
  echo "Error: dependencies are missing. Run ./setup.sh first." >&2
  exit 1
fi

VINEXT="node node_modules/vinext/dist/cli.js"

echo "Synchronizing shared resources into public web paths..."
node tools/sync-public-assets.mjs

echo
echo "Spanish home: http://localhost:${PORT}/"
echo "English home: http://localhost:${PORT}/en"
echo

if [ "$MODE" = "prod" ]; then
  echo "Building for production..."
  $VINEXT build
  echo "Starting the production server on port ${PORT}..."
  exec $VINEXT start -p "$PORT"
fi

echo "Starting the development server on port ${PORT}..."
exec $VINEXT dev -p "$PORT"
