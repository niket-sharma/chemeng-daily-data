# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-09-23)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $91.78 | -2.81 (-2.97%) | $/barrel |
| Brent Crude Oil | $97.65 | -1.60 (-1.61%) | $/barrel |
| Natural Gas | $3.14 | +0.17 (+5.87%) | $/MMBtu |
| Heating Oil | $4.58 | -0.36 (-7.28%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $28.78 | +0.00 (+0.00%) |
| LyondellBasell | LYB | $59.86 | +0.00 (+0.00%) |
| DuPont | DD | $131.78 | +0.00 (+0.00%) |
| Air Products | APD | $287.83 | +0.00 (+0.00%) |
| Linde | LIN | $470.32 | +0.00 (+0.00%) |
| Eastman Chemical | EMN | $67.32 | +0.00 (+0.00%) |
| Celanese | CE | $49.48 | +0.00 (+0.00%) |
| Huntsman | HUN | $9.15 | +0.00 (+0.00%) |

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
