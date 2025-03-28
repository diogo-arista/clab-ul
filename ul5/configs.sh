#!/bin/bash

# Base directory
BASE_DIR="/home/student/clab-ul/ul5/clab-UL5"
DEST_DIR="/home/student/clab-ul/ul5/configs"

# List of devices
DEVICES=("SW1" "SW2" "SW3" "R1" "Controller")

# Loop through each device and copy the startup-config
for DEVICE in "${DEVICES[@]}"; do
    SRC_PATH="$BASE_DIR/$DEVICE/flash/startup-config"
    DEST_PATH="$DEST_DIR/$DEVICE-startup-config"

    if [[ -f "$SRC_PATH" ]]; then
        cp "$SRC_PATH" "$DEST_PATH"
        echo "Copied $DEVICE config to $DEST_PATH"
    else
        echo "Warning: $SRC_PATH not found for $DEVICE"
    fi
done
