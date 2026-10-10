# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-10-10)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $91.85 | +0.36 (+0.39%) | $/barrel |
| Brent Crude Oil | $104.72 | +0.44 (+0.42%) | $/barrel |
| Natural Gas | $3.22 | +0.05 (+1.64%) | $/MMBtu |
| Heating Oil | $4.74 | -0.14 (-2.96%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $28.42 | -0.17 (-0.59%) |
| LyondellBasell | LYB | $60.03 | -0.31 (-0.51%) |
| DuPont | DD | $130.00 | -2.48 (-1.87%) |
| Air Products | APD | $281.26 | +2.88 (+1.03%) |
| Linde | LIN | $483.73 | +2.03 (+0.42%) |
| Eastman Chemical | EMN | $62.69 | -1.07 (-1.68%) |
| Celanese | CE | $45.02 | +0.21 (+0.47%) |
| Huntsman | HUN | $8.14 | -0.36 (-4.24%) |

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
