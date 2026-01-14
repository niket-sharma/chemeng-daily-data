#!/bin/bash
#
# Local script to update the chemeng-daily-data repository
# Run this manually or via cron to add one entry from the queue daily
#

set -e

REPO_DIR="/home/niket/ai/chemeng-daily-data"
LOG_FILE="$REPO_DIR/logs/local_cron.log"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

cd "$REPO_DIR"

log "Starting daily update..."

# Pull latest changes first (autostash handles any local changes)
log "Pulling latest changes..."
git pull --rebase --autostash

# Run the Python update script
log "Running daily_update.py..."
python3 scripts/daily_update.py

# Check if there are changes to commit
if git diff --quiet && git diff --staged --quiet; then
    log "No changes to commit"
    exit 0
fi

# Stage, commit and push
log "Committing changes..."
git add .
git commit -m "Daily data update - $(date '+%Y-%m-%d')"

log "Pushing to remote..."
git push

log "Update complete!"
