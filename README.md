# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-05-20)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $107.77 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $111.28 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.11 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $4.16 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $37.74 | -0.82 (-2.13%) |
| LyondellBasell | LYB | $73.04 | -1.09 (-1.47%) |
| DuPont | DD | $46.56 | -2.08 (-4.28%) |
| Air Products | APD | $291.77 | -1.54 (-0.53%) |
| Linde | LIN | $506.07 | -4.79 (-0.94%) |
| Eastman Chemical | EMN | $68.15 | -2.79 (-3.93%) |
| Celanese | CE | $53.49 | -2.26 (-4.05%) |
| Huntsman | HUN | $13.32 | -0.49 (-3.55%) |

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
