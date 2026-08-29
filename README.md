# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-08-29)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $nan | +nan (+nan%) | $/barrel |
| Brent Crude Oil | $nan | +nan (+nan%) | $/barrel |
| Natural Gas | $nan | +nan (+nan%) | $/MMBtu |
| Heating Oil | $nan | +nan (+nan%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $30.51 | +0.18 (+0.59%) |
| LyondellBasell | LYB | $63.67 | +0.61 (+0.97%) |
| DuPont | DD | $136.98 | -1.82 (-1.31%) |
| Air Products | APD | $308.09 | +2.62 (+0.86%) |
| Linde | LIN | $489.51 | +4.16 (+0.86%) |
| Eastman Chemical | EMN | $73.03 | +0.38 (+0.52%) |
| Celanese | CE | $45.00 | +0.13 (+0.29%) |
| Huntsman | HUN | $9.47 | -0.18 (-1.87%) |

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
