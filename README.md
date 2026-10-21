# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-10-21)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $97.03 | -4.76 (-4.68%) | $/barrel |
| Brent Crude Oil | $108.74 | -0.05 (-0.05%) | $/barrel |
| Natural Gas | $2.79 | -0.17 (-5.91%) | $/MMBtu |
| Heating Oil | $4.57 | -0.36 (-7.24%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $30.22 | -0.47 (-1.52%) |
| LyondellBasell | LYB | $62.98 | -0.98 (-1.53%) |
| DuPont | DD | $134.65 | +1.69 (+1.27%) |
| Air Products | APD | $303.35 | +0.77 (+0.25%) |
| Linde | LIN | $502.00 | +0.11 (+0.02%) |
| Eastman Chemical | EMN | $63.41 | -0.09 (-0.14%) |
| Celanese | CE | $47.38 | -0.14 (-0.28%) |
| Huntsman | HUN | $8.19 | -0.15 (-1.86%) |

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
