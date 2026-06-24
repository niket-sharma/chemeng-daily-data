# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-06-24)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $73.21 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $77.08 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.15 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $3.15 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $30.33 | -0.46 (-1.49%) |
| LyondellBasell | LYB | $57.60 | -0.92 (-1.57%) |
| DuPont | DD | $140.01 | -4.56 (-3.15%) |
| Air Products | APD | $282.45 | -0.66 (-0.23%) |
| Linde | LIN | $512.26 | -4.45 (-0.86%) |
| Eastman Chemical | EMN | $69.48 | -2.48 (-3.45%) |
| Celanese | CE | $48.13 | -1.60 (-3.22%) |
| Huntsman | HUN | $11.38 | -0.12 (-1.04%) |

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
