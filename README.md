# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-02-13)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $62.74 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $67.46 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.19 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $2.39 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $32.65 | -1.35 (-3.97%) |
| LyondellBasell | LYB | $57.78 | -1.69 (-2.84%) |
| DuPont | DD | $49.43 | -2.10 (-4.08%) |
| Air Products | APD | $291.50 | -1.64 (-0.56%) |
| Linde | LIN | $472.86 | +5.35 (+1.14%) |
| Eastman Chemical | EMN | $79.81 | -1.55 (-1.91%) |
| Celanese | CE | $58.82 | -1.74 (-2.87%) |
| Huntsman | HUN | $13.27 | -0.79 (-5.62%) |

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
