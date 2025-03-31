#!/bin/bash
set -e

# Install containerlab
curl -sL https://containerlab.dev/setup | sudo -E bash -s "all"

# Install gdown
pip install --no-cache-dir gdown

# Download file
gdown https://drive.google.com/uc?id=1b8xp2blIO2a7YAFfy5pqvYXiD79ykBT1

# Import Docker image
docker import cEOS-lab-4.33.2F.tar.xz ceosimage:4.33.2F
