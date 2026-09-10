# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-09-10)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $96.05 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $101.21 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $2.82 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $4.80 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $29.40 | -0.17 (-0.57%) |
| LyondellBasell | LYB | $64.51 | -0.08 (-0.12%) |
| DuPont | DD | $127.92 | -3.40 (-2.59%) |
| Air Products | APD | $295.24 | -2.47 (-0.83%) |
| Linde | LIN | $466.65 | -1.73 (-0.37%) |
| Eastman Chemical | EMN | $68.34 | -2.05 (-2.91%) |
| Celanese | CE | $44.45 | -0.08 (-0.18%) |
| Huntsman | HUN | $9.58 | -0.22 (-2.24%) |

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
