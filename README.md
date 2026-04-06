# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-04-06)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $112.66 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $109.69 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $2.84 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $4.40 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $40.16 | -1.24 (-3.00%) |
| LyondellBasell | LYB | $77.78 | -1.82 (-2.29%) |
| DuPont | DD | $45.06 | -0.42 (-0.92%) |
| Air Products | APD | $291.92 | -1.63 (-0.56%) |
| Linde | LIN | $500.05 | -2.55 (-0.51%) |
| Eastman Chemical | EMN | $73.41 | -1.66 (-2.21%) |
| Celanese | CE | $62.26 | -1.80 (-2.81%) |
| Huntsman | HUN | $12.54 | -0.37 (-2.87%) |

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
