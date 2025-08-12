#!/usr/bin/env bash
set -e
if diff -u tests/snapshots/styles.css s3/styles.css; then
  echo "Stylesheet snapshot matches"
else
  echo "Stylesheet snapshot mismatch" >&2
  exit 1
fi
