# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-04-01)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $99.00 | -2.38 (-2.35%) | $/barrel |
| Brent Crude Oil | $101.31 | -17.04 (-14.40%) | $/barrel |
| Natural Gas | $2.83 | -0.06 (-1.98%) | $/MMBtu |
| Heating Oil | $4.00 | -0.16 (-3.92%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $40.54 | -1.11 (-2.67%) |
| LyondellBasell | LYB | $77.29 | -3.27 (-4.07%) |
| DuPont | DD | $46.67 | +0.88 (+1.91%) |
| Air Products | APD | $288.37 | -2.12 (-0.73%) |
| Linde | LIN | $491.75 | -4.01 (-0.81%) |
| Eastman Chemical | EMN | $76.79 | +0.47 (+0.62%) |
| Celanese | CE | $62.93 | -2.84 (-4.32%) |
| Huntsman | HUN | $13.12 | -0.19 (-1.43%) |

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
