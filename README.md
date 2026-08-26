# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-08-26)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $81.63 | -0.73 (-0.89%) | $/barrel |
| Brent Crude Oil | $86.59 | -1.99 (-2.25%) | $/barrel |
| Natural Gas | $2.90 | +0.13 (+4.66%) | $/MMBtu |
| Heating Oil | $4.12 | -0.12 (-2.87%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $30.02 | -0.14 (-0.47%) |
| LyondellBasell | LYB | $61.98 | -0.57 (-0.90%) |
| DuPont | DD | $137.32 | +1.28 (+0.94%) |
| Air Products | APD | $307.87 | +4.02 (+1.32%) |
| Linde | LIN | $491.92 | +4.71 (+0.97%) |
| Eastman Chemical | EMN | $72.42 | +0.40 (+0.56%) |
| Celanese | CE | $44.66 | +0.14 (+0.31%) |
| Huntsman | HUN | $9.48 | -0.05 (-0.52%) |

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
