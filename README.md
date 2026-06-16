# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-06-16)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $76.15 | -4.60 (-5.70%) | $/barrel |
| Brent Crude Oil | $79.95 | -3.22 (-3.87%) | $/barrel |
| Natural Gas | $3.22 | +0.08 (+2.48%) | $/MMBtu |
| Heating Oil | $3.15 | -0.11 (-3.48%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $32.84 | -0.39 (-1.17%) |
| LyondellBasell | LYB | $62.35 | +0.00 (+0.00%) |
| DuPont | DD | $48.10 | +0.00 (+0.00%) |
| Air Products | APD | $281.62 | +0.00 (+0.00%) |
| Linde | LIN | $517.93 | +0.00 (+0.00%) |
| Eastman Chemical | EMN | $73.04 | -2.24 (-2.98%) |
| Celanese | CE | $51.97 | +0.00 (+0.00%) |
| Huntsman | HUN | $12.84 | +0.00 (+0.00%) |

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
