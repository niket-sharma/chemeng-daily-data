# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-09-18)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $95.94 | -5.97 (-5.86%) | $/barrel |
| Brent Crude Oil | $98.97 | -5.85 (-5.58%) | $/barrel |
| Natural Gas | $2.92 | +0.02 (+0.55%) | $/MMBtu |
| Heating Oil | $4.80 | -0.31 (-6.07%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $28.51 | -0.98 (-3.31%) |
| LyondellBasell | LYB | $61.83 | -2.42 (-3.76%) |
| DuPont | DD | $128.44 | -0.02 (-0.02%) |
| Air Products | APD | $283.01 | -3.11 (-1.09%) |
| Linde | LIN | $459.74 | +1.26 (+0.27%) |
| Eastman Chemical | EMN | $65.39 | -0.85 (-1.28%) |
| Celanese | CE | $44.94 | -1.88 (-4.01%) |
| Huntsman | HUN | $8.99 | -0.13 (-1.43%) |

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
