# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-02-18)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $62.40 | +0.07 (+0.11%) | $/barrel |
| Brent Crude Oil | $67.61 | +0.19 (+0.28%) | $/barrel |
| Natural Gas | $3.01 | -0.02 (-0.69%) | $/MMBtu |
| Heating Oil | $2.32 | -0.07 (-2.97%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $31.42 | -1.07 (-3.29%) |
| LyondellBasell | LYB | $55.98 | -1.63 (-2.83%) |
| DuPont | DD | $50.87 | +0.65 (+1.29%) |
| Air Products | APD | $277.69 | -2.05 (-0.73%) |
| Linde | LIN | $482.22 | +1.22 (+0.25%) |
| Eastman Chemical | EMN | $79.11 | -0.97 (-1.21%) |
| Celanese | CE | $55.74 | -3.11 (-5.28%) |
| Huntsman | HUN | $12.35 | -0.86 (-6.51%) |

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
