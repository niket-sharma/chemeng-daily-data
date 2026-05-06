# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-05-06)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $95.09 | -7.18 (-7.02%) | $/barrel |
| Brent Crude Oil | $101.87 | -8.00 (-7.28%) | $/barrel |
| Natural Gas | $2.71 | -0.08 (-2.80%) | $/MMBtu |
| Heating Oil | $3.79 | -0.24 (-5.97%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $38.36 | -2.44 (-5.98%) |
| LyondellBasell | LYB | $72.52 | -5.24 (-6.74%) |
| DuPont | DD | $49.58 | +0.34 (+0.69%) |
| Air Products | APD | $302.00 | -1.93 (-0.64%) |
| Linde | LIN | $501.17 | +0.88 (+0.18%) |
| Eastman Chemical | EMN | $76.77 | -0.52 (-0.67%) |
| Celanese | CE | $61.99 | -7.02 (-10.17%) |
| Huntsman | HUN | $14.81 | -0.18 (-1.17%) |

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
