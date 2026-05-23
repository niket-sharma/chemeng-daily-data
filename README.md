# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-05-23)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $96.60 | +0.25 (+0.26%) | $/barrel |
| Brent Crude Oil | $103.54 | +0.96 (+0.94%) | $/barrel |
| Natural Gas | $2.91 | -0.11 (-3.68%) | $/MMBtu |
| Heating Oil | $3.89 | +0.06 (+1.47%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $36.01 | +0.10 (+0.28%) |
| LyondellBasell | LYB | $69.72 | -0.36 (-0.51%) |
| DuPont | DD | $48.12 | +0.97 (+2.06%) |
| Air Products | APD | $289.47 | -0.72 (-0.25%) |
| Linde | LIN | $517.58 | +3.07 (+0.60%) |
| Eastman Chemical | EMN | $74.12 | +0.93 (+1.27%) |
| Celanese | CE | $52.39 | -0.51 (-0.96%) |
| Huntsman | HUN | $14.51 | +0.13 (+0.90%) |

## Data Sources

- **Yahoo Finance** - Stock prices and commodity futures
- **FRED** - Federal Reserve Economic Data (when API key configured)
- **Alpha Vantage** - Additional commodity data (when API key configured)

## Project Structure

```
chemeng-daily-data/
├── data/
│   ├── prices/        # Category-specific historical data
│   ├── latest/        # Today's snapshot
│   └── historical/    # Daily archives by month
├── scripts/
│   ├── collectors/    # Data source collectors
│   └── daily_price_update.py
├── visualizations/    # Generated charts
└── logs/              # Update logs
```

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. (Optional) Set API keys for additional data sources:
   - `FRED_API_KEY` - Get from https://fred.stlouisfed.org/docs/api/api_key.html
   - `ALPHA_VANTAGE_API_KEY` - Get from https://www.alphavantage.co/support/#api-key

## Automation

This repository updates daily via:
- **GitHub Actions** - Runs at 2 PM UTC
- **Local cron job** - Runs at midnight local time

---

*Data is collected for educational and research purposes.*
