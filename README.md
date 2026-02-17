# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-02-17)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $62.63 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $67.69 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.05 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $2.31 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $32.31 | -0.18 (-0.55%) |
| LyondellBasell | LYB | $57.25 | -0.36 (-0.62%) |
| DuPont | DD | $50.39 | +0.17 (+0.34%) |
| Air Products | APD | $278.90 | -0.83 (-0.30%) |
| Linde | LIN | $480.13 | -0.87 (-0.18%) |
| Eastman Chemical | EMN | $79.34 | -0.74 (-0.92%) |
| Celanese | CE | $55.87 | -2.98 (-5.06%) |
| Huntsman | HUN | $12.89 | -0.32 (-2.42%) |

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
