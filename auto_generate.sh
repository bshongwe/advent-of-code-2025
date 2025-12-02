#!/bin/bash
# Advent of Code 2025 - Auto Generator Cron Script
# This script is designed to be run by cron at 06:00 SAST daily
# It will automatically generate the day's files when they become available

# Set the script directory (where generate_day.py is located)
SCRIPT_DIR="/Users/ernie-dev/Documents/advent-of-code-2025"
LOG_FILE="$SCRIPT_DIR/auto_generate.log"

# Change to the script directory
cd "$SCRIPT_DIR" || {
    echo "$(date): ERROR - Could not change to directory $SCRIPT_DIR" >> "$LOG_FILE"
    exit 1
}

# Add timestamp to log
echo "$(date): Starting auto-generation check..." >> "$LOG_FILE"

# Run the generate_day.py script and capture output
if python3 generate_day.py >> "$LOG_FILE" 2>&1; then
    echo "$(date): Auto-generation completed successfully" >> "$LOG_FILE"
else
    exit_code=$?
    echo "$(date): Auto-generation failed with exit code $exit_code" >> "$LOG_FILE"
fi

# Add separator line for readability
echo "----------------------------------------" >> "$LOG_FILE"
