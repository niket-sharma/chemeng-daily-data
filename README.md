# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-06-22)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $73.55 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $77.49 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.28 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $3.08 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $30.84 | -0.89 (-2.80%) |
| LyondellBasell | LYB | $58.24 | -1.83 (-3.05%) |
| DuPont | DD | $48.22 | +0.51 (+1.06%) |
| Air Products | APD | $283.32 | +3.11 (+1.11%) |
| Linde | LIN | $513.03 | +0.88 (+0.17%) |
| Eastman Chemical | EMN | $72.29 | -0.20 (-0.28%) |
| Celanese | CE | $50.33 | -0.83 (-1.61%) |
| Huntsman | HUN | $11.98 | -0.09 (-0.75%) |

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
