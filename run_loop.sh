#!/bin/bash

while true; do
    python3 GUI.py

    if [ -f "run.txt" ]; then
        echo "Starting Easy-Wav2Lip..."
        python3 run.py
    else
        break  # Exit the loop when "run.txt" does not exist
    fi
done
