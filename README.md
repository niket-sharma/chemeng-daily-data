# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-08-25)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $82.48 | -2.53 (-2.98%) | $/barrel |
| Brent Crude Oil | $88.00 | -4.17 (-4.52%) | $/barrel |
| Natural Gas | $2.78 | -0.01 (-0.25%) | $/MMBtu |
| Heating Oil | $4.18 | -0.09 (-2.08%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $30.71 | -0.73 (-2.32%) |
| LyondellBasell | LYB | $63.62 | -1.58 (-2.42%) |
| DuPont | DD | $137.01 | +0.35 (+0.25%) |
| Air Products | APD | $305.28 | -0.96 (-0.31%) |
| Linde | LIN | $486.40 | -3.63 (-0.74%) |
| Eastman Chemical | EMN | $71.70 | -0.99 (-1.36%) |
| Celanese | CE | $44.51 | -0.75 (-1.67%) |
| Huntsman | HUN | $9.52 | -0.09 (-0.89%) |

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
