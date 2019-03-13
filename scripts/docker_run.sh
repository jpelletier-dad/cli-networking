#!/usr/bin/env bash
[[ "$TRACE" ]] && set -x
set -eu -o pipefail

echo  "Usage: python main.py <env> <region> <network> <availability_zone_count>"
echo  "Example: python main.py ops us-east-1 mgmt 4"

docker run --rm -it \
  -v $(pwd):/cli-networking \
  -w /cli-networking \
    python:3 /bin/bash
