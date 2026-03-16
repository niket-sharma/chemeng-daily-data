# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-03-16)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $93.75 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $96.52 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.10 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $3.70 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $36.62 | +0.00 (+0.00%) |
| LyondellBasell | LYB | $71.87 | -0.43 (-0.59%) |
| DuPont | DD | $45.84 | +0.94 (+2.10%) |
| Air Products | APD | $287.62 | -0.36 (-0.13%) |
| Linde | LIN | $494.61 | +0.69 (+0.14%) |
| Eastman Chemical | EMN | $70.57 | +1.32 (+1.91%) |
| Celanese | CE | $57.11 | -0.63 (-1.09%) |
| Huntsman | HUN | $12.13 | +0.10 (+0.83%) |

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
