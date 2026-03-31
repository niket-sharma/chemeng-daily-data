# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-03-31)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $102.93 | +0.05 (+0.05%) | $/barrel |
| Brent Crude Oil | $107.37 | -5.41 (-4.80%) | $/barrel |
| Natural Gas | $2.83 | -0.05 (-1.84%) | $/MMBtu |
| Heating Oil | $4.25 | -0.11 (-2.59%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $41.87 | +1.05 (+2.57%) |
| LyondellBasell | LYB | $82.38 | +1.93 (+2.40%) |
| DuPont | DD | $44.22 | -1.04 (-2.30%) |
| Air Products | APD | $291.56 | -0.63 (-0.22%) |
| Linde | LIN | $499.26 | +8.14 (+1.66%) |
| Eastman Chemical | EMN | $72.55 | +1.35 (+1.90%) |
| Celanese | CE | $64.25 | +0.84 (+1.32%) |
| Huntsman | HUN | $12.57 | -0.09 (-0.71%) |

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
