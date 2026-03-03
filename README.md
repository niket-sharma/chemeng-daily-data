# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-03-03)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $72.69 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $79.74 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.03 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $2.76 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $30.60 | -0.13 (-0.42%) |
| LyondellBasell | LYB | $57.88 | +1.05 (+1.85%) |
| DuPont | DD | $49.64 | -0.20 (-0.40%) |
| Air Products | APD | $276.43 | +0.76 (+0.28%) |
| Linde | LIN | $509.34 | +1.26 (+0.25%) |
| Eastman Chemical | EMN | $75.28 | -0.23 (-0.30%) |
| Celanese | CE | $49.73 | -0.21 (-0.42%) |
| Huntsman | HUN | $12.30 | -0.35 (-2.77%) |

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
