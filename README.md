# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-02-23)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $66.96 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $71.72 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.00 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $2.53 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $30.75 | +0.23 (+0.74%) |
| LyondellBasell | LYB | $57.05 | +0.38 (+0.67%) |
| DuPont | DD | $50.48 | +0.07 (+0.14%) |
| Air Products | APD | $284.12 | +2.95 (+1.05%) |
| Linde | LIN | $498.59 | +2.08 (+0.42%) |
| Eastman Chemical | EMN | $78.45 | -0.71 (-0.90%) |
| Celanese | CE | $53.86 | -0.25 (-0.46%) |
| Huntsman | HUN | $12.66 | +0.07 (+0.56%) |

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
