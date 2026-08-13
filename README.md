# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-08-13)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $80.94 | -2.33 (-2.80%) | $/barrel |
| Brent Crude Oil | $86.69 | -2.29 (-2.57%) | $/barrel |
| Natural Gas | $2.73 | -0.07 (-2.46%) | $/MMBtu |
| Heating Oil | $4.24 | -0.07 (-1.51%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $30.41 | -0.16 (-0.54%) |
| LyondellBasell | LYB | $62.26 | -0.54 (-0.86%) |
| DuPont | DD | $144.20 | -0.17 (-0.12%) |
| Air Products | APD | $305.10 | +1.03 (+0.34%) |
| Linde | LIN | $481.36 | +1.93 (+0.40%) |
| Eastman Chemical | EMN | $73.26 | +0.72 (+0.99%) |
| Celanese | CE | $43.90 | +0.58 (+1.35%) |
| Huntsman | HUN | $10.37 | +0.22 (+2.17%) |

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
