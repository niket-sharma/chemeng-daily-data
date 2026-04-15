# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-04-15)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $91.11 | -0.17 (-0.19%) | $/barrel |
| Brent Crude Oil | $94.85 | +0.06 (+0.06%) | $/barrel |
| Natural Gas | $2.59 | -0.00 (-0.19%) | $/MMBtu |
| Heating Oil | $3.52 | -0.11 (-2.91%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $39.32 | +0.16 (+0.41%) |
| LyondellBasell | LYB | $73.62 | +0.37 (+0.51%) |
| DuPont | DD | $46.04 | -0.64 (-1.37%) |
| Air Products | APD | $295.42 | -1.21 (-0.41%) |
| Linde | LIN | $495.02 | -4.63 (-0.93%) |
| Eastman Chemical | EMN | $71.82 | -1.97 (-2.68%) |
| Celanese | CE | $64.49 | -0.61 (-0.94%) |
| Huntsman | HUN | $13.52 | -0.05 (-0.37%) |

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
