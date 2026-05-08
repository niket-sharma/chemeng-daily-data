# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-05-08)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $96.29 | +1.48 (+1.56%) | $/barrel |
| Brent Crude Oil | $101.59 | +1.53 (+1.53%) | $/barrel |
| Natural Gas | $2.78 | +0.01 (+0.25%) | $/MMBtu |
| Heating Oil | $3.91 | +0.09 (+2.41%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $37.32 | -1.18 (-3.06%) |
| LyondellBasell | LYB | $71.51 | -1.97 (-2.68%) |
| DuPont | DD | $48.36 | -1.71 (-3.42%) |
| Air Products | APD | $294.99 | -5.22 (-1.74%) |
| Linde | LIN | $493.85 | -8.02 (-1.60%) |
| Eastman Chemical | EMN | $73.69 | -2.05 (-2.71%) |
| Celanese | CE | $58.40 | -3.72 (-5.99%) |
| Huntsman | HUN | $14.74 | -0.36 (-2.38%) |

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
