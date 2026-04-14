# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-04-14)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $93.46 | -5.62 (-5.67%) | $/barrel |
| Brent Crude Oil | $95.86 | -3.50 (-3.52%) | $/barrel |
| Natural Gas | $2.62 | -0.01 (-0.42%) | $/MMBtu |
| Heating Oil | $3.55 | -0.29 (-7.46%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $38.58 | -1.53 (-3.81%) |
| LyondellBasell | LYB | $72.83 | -2.68 (-3.54%) |
| DuPont | DD | $46.69 | -0.46 (-0.98%) |
| Air Products | APD | $293.46 | -5.19 (-1.74%) |
| Linde | LIN | $497.16 | -11.71 (-2.30%) |
| Eastman Chemical | EMN | $74.50 | +0.49 (+0.66%) |
| Celanese | CE | $65.09 | -3.13 (-4.59%) |
| Huntsman | HUN | $13.63 | -0.41 (-2.92%) |

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
