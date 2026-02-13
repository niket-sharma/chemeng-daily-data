# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-02-13)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $62.79 | -0.05 (-0.08%) | $/barrel |
| Brent Crude Oil | $67.57 | +0.05 (+0.07%) | $/barrel |
| Natural Gas | $3.15 | -0.07 (-2.05%) | $/MMBtu |
| Heating Oil | $2.32 | -0.08 (-3.18%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $32.58 | -0.07 (-0.21%) |
| LyondellBasell | LYB | $57.23 | -0.55 (-0.95%) |
| DuPont | DD | $49.39 | -0.04 (-0.09%) |
| Air Products | APD | $280.99 | -10.51 (-3.60%) |
| Linde | LIN | $476.93 | +4.07 (+0.86%) |
| Eastman Chemical | EMN | $79.99 | +0.18 (+0.22%) |
| Celanese | CE | $58.42 | -0.40 (-0.68%) |
| Huntsman | HUN | $12.98 | -0.29 (-2.19%) |

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
