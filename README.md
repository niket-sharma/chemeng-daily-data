# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-06-19)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $75.23 | -1.56 (-2.03%) | $/barrel |
| Brent Crude Oil | $79.17 | -0.38 (-0.48%) | $/barrel |
| Natural Gas | $3.21 | +0.06 (+1.94%) | $/MMBtu |
| Heating Oil | $3.07 | -0.12 (-3.89%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $31.73 | -0.77 (-2.37%) |
| LyondellBasell | LYB | $60.07 | -1.74 (-2.82%) |
| DuPont | DD | $47.71 | -0.24 (-0.50%) |
| Air Products | APD | $280.21 | -1.54 (-0.55%) |
| Linde | LIN | $512.15 | -3.70 (-0.72%) |
| Eastman Chemical | EMN | $72.49 | +0.37 (+0.51%) |
| Celanese | CE | $51.16 | -0.07 (-0.14%) |
| Huntsman | HUN | $12.07 | -0.66 (-5.18%) |

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
