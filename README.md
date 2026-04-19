# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-04-19)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $82.59 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $90.38 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $2.67 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $3.30 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $35.60 | -4.32 (-10.82%) |
| LyondellBasell | LYB | $66.27 | -9.02 (-11.98%) |
| DuPont | DD | $47.35 | +0.60 (+1.28%) |
| Air Products | APD | $291.81 | -5.43 (-1.83%) |
| Linde | LIN | $492.23 | -6.99 (-1.40%) |
| Eastman Chemical | EMN | $73.78 | +0.43 (+0.59%) |
| Celanese | CE | $62.03 | -6.31 (-9.23%) |
| Huntsman | HUN | $13.35 | -0.39 (-2.84%) |

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
