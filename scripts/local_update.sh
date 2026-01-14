#!/bin/bash
#
# Local script to update the chemeng-daily-data repository
# Fetches daily chemical commodity prices and pushes to GitHub
#

set -e

REPO_DIR="/home/niket/ai/chemeng-daily-data"
LOG_FILE="$REPO_DIR/logs/local_cron.log"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

cd "$REPO_DIR"

# Activate virtual environment if it exists
if [ -d ".venv" ]; then
    source .venv/bin/activate
fi

log "Starting daily price update..."

# Pull latest changes first (autostash handles any local changes)
log "Pulling latest changes..."
git pull --rebase --autostash

# Run the price update script
log "Running daily_price_update.py..."
python3 scripts/daily_price_update.py

# Generate visualizations (optional, may fail if matplotlib not installed)
log "Generating visualizations..."
python3 scripts/generate_charts.py || log "Visualization generation skipped"

# Check if there are changes to commit
if git diff --quiet && git diff --staged --quiet; then
    log "No changes to commit"
    exit 0
fi

# Stage, commit and push
log "Committing changes..."
git add .
git commit -m "Daily price update: $(date '+%Y-%m-%d')"

log "Pushing to remote..."
git push

log "Update complete!"
