# Setup Instructions

## Initial Git Setup and Push

Run these commands to push your code to GitHub:

```bash
# Initialize git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial setup: Chemical engineering daily data repository"

# Add your GitHub repository as remote
git remote add origin https://github.com/niket-sharma/chemeng-daily-data.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## Testing GitHub Actions Manually

After pushing to GitHub, follow these steps to test the workflow manually:

### Method 1: Using GitHub Web Interface

1. Go to your repository: `https://github.com/niket-sharma/chemeng-daily-data`
2. Click on the **"Actions"** tab
3. In the left sidebar, click on **"Daily Chemical Engineering Data Update"**
4. On the right side, click the **"Run workflow"** button
5. Select the branch (main) and click **"Run workflow"**
6. Watch the workflow execute in real-time
7. Once complete, check the repository for new commits

### Method 2: Using GitHub CLI (gh)

If you have GitHub CLI installed:

```bash
# Trigger the workflow manually
gh workflow run daily-update.yml

# View workflow runs
gh run list --workflow=daily-update.yml

# Watch the latest run
gh run watch
```

### Method 3: Using API (curl)

```bash
# Get your GitHub token from: https://github.com/settings/tokens
# Need "repo" and "workflow" permissions

curl -X POST \
  -H "Accept: application/vnd.github.v3+json" \
  -H "Authorization: token YOUR_GITHUB_TOKEN" \
  https://api.github.com/repos/niket-sharma/chemeng-daily-data/actions/workflows/daily-update.yml/dispatches \
  -d '{"ref":"main"}'
```

## Verifying the Workflow

After running the workflow manually, verify it worked:

1. **Check for new commits**: Look at the commit history - you should see a commit from `github-actions[bot]`
2. **Check data files**: Open `data/compounds.json`, `data/experiment_correlations.py`, or `data/experiment_constants.py` to see new entries
3. **Check the log**: Open `logs/update_log.md` to see what was added
4. **Check queue**: The `queue/pending_entries.json` should have one less entry

## Automatic Daily Updates

The workflow is scheduled to run automatically at **9:00 AM UTC** every day. You don't need to do anything - it will:

1. Add one entry from the queue
2. Commit the changes
3. Push to the repository
4. Keep your GitHub activity green!

## Adding More Entries to the Queue

When your queue gets low (under 50 entries), run:

```bash
python scripts/generate_entries.py
```

Then commit and push the updated queue:

```bash
git add queue/pending_entries.json
git commit -m "Add more entries to queue"
git push
```

## Troubleshooting

### Workflow Not Showing Up
- Make sure you've pushed the `.github/workflows/daily-update.yml` file
- Check the Actions tab is enabled in repository Settings → Actions → General

### Workflow Fails
- Check the workflow logs in the Actions tab
- Common issues:
  - Queue is empty (add more entries)
  - Permissions issue (check repository settings)
  - Python syntax errors (check the script)

### No Automatic Runs
- GitHub Actions on schedule can have delays up to 15 minutes
- For new repositories, the first scheduled run might take 24 hours
- Manual triggers always work immediately

## Current Status

- Queue size: 13 entries remaining (after testing)
- Entries tested and working: ✅
- GitHub Actions workflow: Ready to deploy ✅
