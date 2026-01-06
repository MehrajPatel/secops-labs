#!/usr/bin/env bash
set -euo pipefail

IMAGE_NAME="supplychain-demo:sbom"

echo "[+] Building image: ${IMAGE_NAME}"
docker build -t ${IMAGE_NAME} .

echo "[+] Generating SPDX SBOM"
syft ${IMAGE_NAME} -o spdx-json > sbom1.spdx.json

echo "[+] Generating CycloneDX SBOM"
syft ${IMAGE_NAME} -o cyclonedx-json > sbom1.cdx.json

echo "[+] SBOM files generated:"
ls -lh sbom.*.json
