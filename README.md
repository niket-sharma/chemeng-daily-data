# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-09-05)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $91.48 | +0.18 (+0.20%) | $/barrel |
| Brent Crude Oil | $96.28 | +0.76 (+0.80%) | $/barrel |
| Natural Gas | $2.97 | +0.06 (+2.13%) | $/MMBtu |
| Heating Oil | $4.54 | -0.05 (-1.16%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $29.44 | -0.92 (-3.03%) |
| LyondellBasell | LYB | $63.52 | -1.24 (-1.91%) |
| DuPont | DD | $131.59 | +0.46 (+0.35%) |
| Air Products | APD | $301.27 | -2.95 (-0.97%) |
| Linde | LIN | $477.57 | -4.62 (-0.96%) |
| Eastman Chemical | EMN | $71.19 | +0.42 (+0.59%) |
| Celanese | CE | $44.67 | -0.53 (-1.17%) |
| Huntsman | HUN | $9.62 | +0.22 (+2.34%) |

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
