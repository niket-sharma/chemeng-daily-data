# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-08-12)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $82.97 | -0.23 (-0.28%) | $/barrel |
| Brent Crude Oil | $88.79 | -0.12 (-0.13%) | $/barrel |
| Natural Gas | $2.82 | +0.05 (+1.92%) | $/MMBtu |
| Heating Oil | $4.14 | -0.11 (-2.54%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $30.78 | -0.48 (-1.54%) |
| LyondellBasell | LYB | $63.15 | -0.83 (-1.29%) |
| DuPont | DD | $142.38 | -2.11 (-1.46%) |
| Air Products | APD | $305.67 | -3.64 (-1.18%) |
| Linde | LIN | $484.41 | -6.12 (-1.25%) |
| Eastman Chemical | EMN | $72.86 | -1.90 (-2.55%) |
| Celanese | CE | $43.58 | -1.26 (-2.81%) |
| Huntsman | HUN | $10.17 | -0.27 (-2.59%) |

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
