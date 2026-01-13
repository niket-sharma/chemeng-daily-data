# Deployment Checklist

## Pre-Deployment Status ✅

- [x] All directories created
- [x] All scripts created and tested
- [x] GitHub Actions workflow configured
- [x] Queue populated with 50 entries
- [x] Data files reset to clean state
- [x] Update script tested (compounds, correlations, constants all working)

## Deployment Steps

Follow these steps in order:

### 1. Push to GitHub

```bash
# Navigate to project directory
cd /home/niket/ai/chemeng-daily-data

# Initialize git
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial setup: Chemical engineering daily data repository"

# Add remote repository
git remote add origin https://github.com/niket-sharma/chemeng-daily-data.git

# Set main branch and push
git branch -M main
git push -u origin main
```

### 2. Verify Repository on GitHub

Go to: `https://github.com/niket-sharma/chemeng-daily-data`

Check that you can see:
- [ ] README.md is displayed
- [ ] All folders are present (data, queue, scripts, logs, .github)
- [ ] Files are accessible

### 3. Enable GitHub Actions

1. Go to repository **Settings** → **Actions** → **General**
2. Under "Actions permissions", ensure **"Allow all actions and reusable workflows"** is selected
3. Under "Workflow permissions", select **"Read and write permissions"**
4. Check **"Allow GitHub Actions to create and approve pull requests"** (optional, but helpful)
5. Click **Save**

### 4. Test the Workflow Manually

#### Option A: GitHub Web Interface (Recommended)

1. Go to the **Actions** tab
2. Click **"Daily Chemical Engineering Data Update"** in the left sidebar
3. Click **"Run workflow"** button (top right)
4. Select branch: `main`
5. Click **"Run workflow"**
6. Wait for the workflow to complete (should take ~10-20 seconds)
7. Verify success: Green checkmark appears

#### Option B: GitHub CLI

```bash
# Install gh if needed: https://cli.github.com/
gh workflow run daily-update.yml
gh run watch
```

### 5. Verify the Workflow Worked

After the workflow completes, check:

- [ ] New commit appears from `github-actions[bot]`
- [ ] One entry added to either:
  - `data/compounds.json`, OR
  - `data/experiment_correlations.py`, OR
  - `data/experiment_constants.py`
- [ ] `logs/update_log.md` has a new entry
- [ ] `queue/pending_entries.json` reduced from 50 to 49 entries

### 6. Run a Second Test (Optional)

Trigger the workflow again manually to verify consistency:

1. Run workflow again from Actions tab
2. Verify another entry is added
3. Queue should now have 48 entries

### 7. All Done! 🎉

Your repository is now:
- ✅ Deployed on GitHub
- ✅ Automated to update daily at 9:00 AM UTC
- ✅ Ready to maintain your GitHub activity for 50 days

## Scheduled Runs

The workflow will automatically run **every day at 9:00 AM UTC**.

To see when that is in your timezone:
- Convert 9:00 AM UTC to your local time
- Example: 9:00 AM UTC = 2:30 PM IST (India)

## Adding More Entries

When queue gets low (under 10 entries):

```bash
# Run the generator script
python scripts/generate_entries.py

# Commit and push
git add queue/pending_entries.json
git commit -m "Add more entries to queue"
git push
```

I can help you create more batches with different types of data!

## Monitoring

- Check the **Actions** tab periodically to ensure daily runs are successful
- Star your own repository to see updates in your feed
- The green contribution graph will update automatically

## Troubleshooting

If a workflow fails:
1. Click on the failed run in Actions tab
2. Click on the "update" job
3. Expand the failed step to see error message
4. Common fixes:
   - Queue empty → Run generate_entries.py
   - Permission error → Check workflow permissions in Settings
   - Syntax error → Check the Python script

## What Happens Next

Starting tomorrow, your repository will automatically:
1. Add one new chemical engineering data point
2. Commit it with message "Daily data update - YYYY-MM-DD"
3. Push to main branch
4. Keep your GitHub activity consistent

No maintenance required for 50 days (or longer if you add more batches)!
