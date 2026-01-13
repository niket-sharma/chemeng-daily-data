# Chemical Engineering Daily Data Repository

A growing collection of chemical engineering reference data, updated automatically every day.

## Contents

- **Compounds**: Physical properties of common industrial chemicals
- **Correlations**: Important engineering equations and correlations
- **Constants**: Fundamental values and engineering constants

## Data Sources

Data compiled from Perry's Chemical Engineers' Handbook, CRC Handbook, NIST, and other authoritative sources.

## Automation

This repository updates daily via GitHub Actions, adding one new data point each day to maintain consistent GitHub activity.

## Usage

```python
import json

# Load compound data
with open('data/compounds.json') as f:
    compounds = json.load(f)

# Import correlations
from data.experiment_correlations import *

# Import constants
from data.experiment_constants import *
```

## Statistics

- Started: 2026-01-12
- Total entries: Check [logs/update_log.md](logs/update_log.md)
- Current queue size: 50 entries (expandable)

## Adding More Entries

To add more entries to the queue, run:

```bash
python scripts/generate_entries.py
```

You can modify the script to add additional batches of compounds, correlations, or constants.

## Manual Testing

To test the daily update manually:

```bash
python scripts/daily_update.py
```

## Repository Structure

```
chemeng-daily-data/
├── README.md
├── data/
│   ├── compounds.json          # Chemical compound properties
│   ├── experiment_correlations.py  # Engineering equations
│   └── experiment_constants.py      # Engineering constants and values
├── queue/
│   └── pending_entries.json    # Pre-generated queue of entries
├── scripts/
│   ├── daily_update.py         # Script that GitHub Actions runs
│   └── generate_entries.py     # Script to add more entries to queue
├── logs/
│   └── update_log.md           # Track what was added and when
└── .github/
    └── workflows/
        └── daily-update.yml    # GitHub Actions workflow
```

## Author

Niket Sharma - Chemical Process Simulation Engineer
- GitHub: [@niket-sharma](https://github.com/niket-sharma)

## License

This data is provided for educational and reference purposes.
