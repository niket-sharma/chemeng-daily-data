# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-05-15)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $102.43 | +1.26 (+1.25%) | $/barrel |
| Brent Crude Oil | $106.98 | +1.26 (+1.19%) | $/barrel |
| Natural Gas | $2.92 | +0.02 (+0.83%) | $/MMBtu |
| Heating Oil | $3.94 | +0.04 (+0.98%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $38.78 | -0.06 (-0.15%) |
| LyondellBasell | LYB | $73.27 | -0.47 (-0.64%) |
| DuPont | DD | $50.60 | -0.56 (-1.09%) |
| Air Products | APD | $299.87 | -6.33 (-2.07%) |
| Linde | LIN | $511.65 | -1.61 (-0.31%) |
| Eastman Chemical | EMN | $72.47 | -1.36 (-1.84%) |
| Celanese | CE | $57.33 | -2.64 (-4.40%) |
| Huntsman | HUN | $14.31 | -0.08 (-0.56%) |

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
