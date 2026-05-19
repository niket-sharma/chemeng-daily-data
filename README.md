# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-05-19)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $103.63 | -5.03 (-4.63%) | $/barrel |
| Brent Crude Oil | $110.81 | -1.29 (-1.15%) | $/barrel |
| Natural Gas | $3.09 | +0.07 (+2.31%) | $/MMBtu |
| Heating Oil | $4.00 | -0.11 (-2.72%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $37.25 | -1.31 (-3.40%) |
| LyondellBasell | LYB | $72.05 | -2.08 (-2.81%) |
| DuPont | DD | $46.36 | -2.28 (-4.69%) |
| Air Products | APD | $291.12 | -2.18 (-0.74%) |
| Linde | LIN | $506.53 | -4.33 (-0.85%) |
| Eastman Chemical | EMN | $68.32 | -2.62 (-3.69%) |
| Celanese | CE | $52.74 | -3.01 (-5.40%) |
| Huntsman | HUN | $13.27 | -0.54 (-3.87%) |

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
