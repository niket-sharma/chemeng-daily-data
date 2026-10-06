# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-10-06)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $89.60 | +0.17 (+0.19%) | $/barrel |
| Brent Crude Oil | $100.78 | +0.46 (+0.46%) | $/barrel |
| Natural Gas | $3.13 | +0.06 (+1.96%) | $/MMBtu |
| Heating Oil | $4.57 | +0.03 (+0.60%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $28.15 | -0.36 (-1.28%) |
| LyondellBasell | LYB | $58.80 | -0.42 (-0.71%) |
| DuPont | DD | $133.54 | +2.85 (+2.18%) |
| Air Products | APD | $280.45 | +0.99 (+0.36%) |
| Linde | LIN | $491.13 | +8.75 (+1.81%) |
| Eastman Chemical | EMN | $64.18 | -0.76 (-1.16%) |
| Celanese | CE | $44.99 | -0.54 (-1.19%) |
| Huntsman | HUN | $8.80 | -0.05 (-0.51%) |

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
