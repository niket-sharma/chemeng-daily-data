# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-09-08)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $92.08 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $96.90 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $2.88 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $4.55 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $29.74 | +0.30 (+1.00%) |
| LyondellBasell | LYB | $64.98 | +1.46 (+2.30%) |
| DuPont | DD | $131.68 | +0.09 (+0.07%) |
| Air Products | APD | $299.01 | -2.26 (-0.75%) |
| Linde | LIN | $468.48 | -9.09 (-1.90%) |
| Eastman Chemical | EMN | $70.06 | -1.13 (-1.59%) |
| Celanese | CE | $44.90 | +0.23 (+0.51%) |
| Huntsman | HUN | $9.78 | +0.16 (+1.66%) |

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
