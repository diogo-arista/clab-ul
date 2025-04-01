#!/bin/bash
set -e

# Install containerlab
echo "[INFO] Installing containerlab..."
curl -sL https://containerlab.dev/setup | sudo -E bash -s "all"

# Ensure pip is available
echo "[INFO] Installing python3-pip..."
sudo apt-get update
sudo apt-get install -y python3-pip

# Install gdown
echo "[INFO] Installing gdown..."
python3 -m pip install --no-cache-dir gdown

# Download the cEOS image
echo "[INFO] Downloading cEOS image from Google Drive..."
gdown --fuzzy "https://drive.google.com/uc?id=1b8xp2blIO2a7YAFfy5pqvYXiD79ykBT1"

# Install tcpdump
sudo apt-get install -y tcpdump

# Import Docker image
echo "[INFO] Importing Docker image..."
docker import cEOS-lab-4.33.2F.tar.xz ceosimage:4.33.2F

echo "[INFO] Setup complete ✅"
