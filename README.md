# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-06-29)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $70.48 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $73.66 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.18 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $3.18 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $27.77 | -1.27 (-4.37%) |
| LyondellBasell | LYB | $54.19 | -1.54 (-2.76%) |
| DuPont | DD | $134.24 | -2.98 (-2.17%) |
| Air Products | APD | $271.83 | -5.96 (-2.14%) |
| Linde | LIN | $511.35 | -8.27 (-1.59%) |
| Eastman Chemical | EMN | $67.54 | -3.17 (-4.48%) |
| Celanese | CE | $46.68 | -2.74 (-5.54%) |
| Huntsman | HUN | $10.94 | -0.47 (-4.16%) |

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
