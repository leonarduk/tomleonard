#!/usr/bin/env bash
set -euo pipefail

# Ensure this script runs from the project root containing package.json
if [ ! -f package.json ]; then
  echo "package.json not found. Run this script from the project root." >&2
  exit 1
fi

# First install packages already listed in package.json
npm install

# List of dependencies required by the project
DEPS=(react-router-dom i18next react-i18next recharts)

# Determine which dependencies are missing
MISSING=()
for dep in "${DEPS[@]}"; do
  if ! npm list "$dep" >/dev/null 2>&1; then
    MISSING+=("$dep")
  fi
done

# Install any missing dependencies
if [ ${#MISSING[@]} -gt 0 ]; then
  echo "Installing missing dependencies: ${MISSING[*]}"
  npm install "${MISSING[@]}"
fi

# Start the development server
npm run dev
