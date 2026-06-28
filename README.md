# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-06-28)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $69.23 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $72.60 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.28 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $3.10 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $29.04 | -0.27 (-0.92%) |
| LyondellBasell | LYB | $55.73 | -0.11 (-0.20%) |
| DuPont | DD | $137.22 | -0.58 (-0.42%) |
| Air Products | APD | $277.79 | -2.14 (-0.76%) |
| Linde | LIN | $519.62 | -2.66 (-0.51%) |
| Eastman Chemical | EMN | $70.71 | +0.10 (+0.14%) |
| Celanese | CE | $49.42 | +0.50 (+1.02%) |
| Huntsman | HUN | $11.41 | +0.08 (+0.71%) |

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
