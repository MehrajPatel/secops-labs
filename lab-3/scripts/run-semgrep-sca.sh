#!/usr/bin/env bash
set -euo pipefail

echo "[*] Running Semgrep SCA locally"

semgrep scan \
  --sca \
  --severity ERROR \
  --json \
  --output semgrep-sca.json

echo "[!] If you see this, something is wrong — build should have failed"
