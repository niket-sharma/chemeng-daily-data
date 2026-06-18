# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-06-18)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $76.79 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $79.55 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.14 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $3.19 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $32.50 | -0.46 (-1.40%) |
| LyondellBasell | LYB | $61.81 | -0.78 (-1.25%) |
| DuPont | DD | $47.95 | -0.09 (-0.19%) |
| Air Products | APD | $281.75 | +1.27 (+0.45%) |
| Linde | LIN | $515.85 | -2.32 (-0.45%) |
| Eastman Chemical | EMN | $72.12 | -1.16 (-1.58%) |
| Celanese | CE | $51.23 | -0.70 (-1.35%) |
| Huntsman | HUN | $12.73 | -0.45 (-3.41%) |

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
