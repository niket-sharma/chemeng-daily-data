# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-08-31)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $85.78 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $88.18 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $2.92 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $4.42 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $30.31 | +0.00 (+0.00%) |
| LyondellBasell | LYB | $64.77 | +0.00 (+0.00%) |
| DuPont | DD | $134.32 | +0.00 (+0.00%) |
| Air Products | APD | $308.68 | +0.00 (+0.00%) |
| Linde | LIN | $489.30 | +0.00 (+0.00%) |
| Eastman Chemical | EMN | $72.25 | +0.00 (+0.00%) |
| Celanese | CE | $45.36 | +0.00 (+0.00%) |
| Huntsman | HUN | $9.52 | +0.00 (+0.00%) |

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
