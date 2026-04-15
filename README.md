# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-04-15)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $91.13 | -0.15 (-0.16%) | $/barrel |
| Brent Crude Oil | $95.15 | +0.36 (+0.38%) | $/barrel |
| Natural Gas | $2.59 | -0.01 (-0.27%) | $/MMBtu |
| Heating Oil | $3.49 | -0.13 (-3.59%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $39.16 | -0.95 (-2.37%) |
| LyondellBasell | LYB | $73.25 | -2.26 (-2.99%) |
| DuPont | DD | $46.68 | -0.47 (-1.00%) |
| Air Products | APD | $296.63 | -2.02 (-0.68%) |
| Linde | LIN | $499.65 | -9.22 (-1.81%) |
| Eastman Chemical | EMN | $73.79 | -0.22 (-0.30%) |
| Celanese | CE | $65.10 | -3.12 (-4.57%) |
| Huntsman | HUN | $13.57 | -0.47 (-3.35%) |

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
