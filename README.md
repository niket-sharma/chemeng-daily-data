# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-02-19)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $66.13 | +0.94 (+1.44%) | $/barrel |
| Brent Crude Oil | $71.40 | +1.05 (+1.49%) | $/barrel |
| Natural Gas | $2.99 | -0.02 (-0.80%) | $/MMBtu |
| Heating Oil | $2.47 | -0.05 (-2.10%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $31.40 | -0.18 (-0.56%) |
| LyondellBasell | LYB | $56.26 | +0.29 (+0.53%) |
| DuPont | DD | $51.24 | -0.11 (-0.22%) |
| Air Products | APD | $280.40 | -1.99 (-0.70%) |
| Linde | LIN | $484.52 | -0.76 (-0.16%) |
| Eastman Chemical | EMN | $79.93 | -0.33 (-0.40%) |
| Celanese | CE | $53.90 | -0.97 (-1.76%) |
| Huntsman | HUN | $12.98 | -0.43 (-3.21%) |

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
