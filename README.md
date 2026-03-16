# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-03-16)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $99.41 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $100.11 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.09 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $3.76 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $36.62 | -0.96 (-2.55%) |
| LyondellBasell | LYB | $72.30 | -2.03 (-2.73%) |
| DuPont | DD | $44.90 | -0.44 (-0.97%) |
| Air Products | APD | $287.98 | -2.50 (-0.86%) |
| Linde | LIN | $493.92 | +3.51 (+0.72%) |
| Eastman Chemical | EMN | $69.25 | -0.50 (-0.72%) |
| Celanese | CE | $57.74 | -1.86 (-3.12%) |
| Huntsman | HUN | $12.03 | -0.68 (-5.37%) |

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
