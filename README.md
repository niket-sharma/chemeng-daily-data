# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-07-23)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $92.37 | +5.54 (+6.38%) | $/barrel |
| Brent Crude Oil | $87.22 | -6.85 (-7.28%) | $/barrel |
| Natural Gas | $2.94 | +0.01 (+0.44%) | $/MMBtu |
| Heating Oil | $4.26 | +0.11 (+2.68%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $31.24 | -0.01 (-0.05%) |
| LyondellBasell | LYB | $62.43 | +0.11 (+0.18%) |
| DuPont | DD | $136.89 | -2.75 (-1.97%) |
| Air Products | APD | $296.26 | -0.74 (-0.25%) |
| Linde | LIN | $508.31 | -0.36 (-0.07%) |
| Eastman Chemical | EMN | $68.04 | -1.34 (-1.93%) |
| Celanese | CE | $47.78 | -0.58 (-1.20%) |
| Huntsman | HUN | $13.00 | -0.22 (-1.66%) |

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
