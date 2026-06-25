# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-06-25)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $69.33 | -1.01 (-1.44%) | $/barrel |
| Brent Crude Oil | $72.49 | -1.25 (-1.70%) | $/barrel |
| Natural Gas | $3.28 | +0.06 (+1.86%) | $/MMBtu |
| Heating Oil | $3.08 | -0.10 (-3.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $29.38 | -0.95 (-3.13%) |
| LyondellBasell | LYB | $56.12 | -1.48 (-2.57%) |
| DuPont | DD | $137.82 | +0.00 (+0.00%) |
| Air Products | APD | $278.73 | -3.72 (-1.32%) |
| Linde | LIN | $515.73 | +3.47 (+0.68%) |
| Eastman Chemical | EMN | $70.40 | +0.92 (+1.32%) |
| Celanese | CE | $48.04 | -0.09 (-0.19%) |
| Huntsman | HUN | $11.32 | -0.06 (-0.53%) |

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
