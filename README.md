# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-04-22)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $91.32 | -0.81 (-0.88%) | $/barrel |
| Brent Crude Oil | $94.86 | -3.62 (-3.68%) | $/barrel |
| Natural Gas | $2.73 | +0.04 (+1.33%) | $/MMBtu |
| Heating Oil | $3.73 | +0.00 (+0.09%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $38.46 | +0.15 (+0.38%) |
| LyondellBasell | LYB | $71.64 | +0.22 (+0.31%) |
| DuPont | DD | $46.23 | -0.48 (-1.03%) |
| Air Products | APD | $296.60 | +1.82 (+0.62%) |
| Linde | LIN | $500.74 | +5.90 (+1.19%) |
| Eastman Chemical | EMN | $72.38 | -0.08 (-0.11%) |
| Celanese | CE | $65.87 | +0.10 (+0.15%) |
| Huntsman | HUN | $13.91 | +0.17 (+1.24%) |

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
