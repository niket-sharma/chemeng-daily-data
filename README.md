# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-06-25)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $70.78 | +0.44 (+0.63%) | $/barrel |
| Brent Crude Oil | $74.30 | +0.56 (+0.76%) | $/barrel |
| Natural Gas | $3.23 | +0.01 (+0.16%) | $/MMBtu |
| Heating Oil | $3.15 | -0.02 (-0.76%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $28.58 | -0.80 (-2.74%) |
| LyondellBasell | LYB | $54.86 | -1.26 (-2.25%) |
| DuPont | DD | $139.70 | +1.88 (+1.36%) |
| Air Products | APD | $280.82 | +2.09 (+0.75%) |
| Linde | LIN | $526.20 | +10.47 (+2.03%) |
| Eastman Chemical | EMN | $70.10 | -0.31 (-0.43%) |
| Celanese | CE | $47.19 | -0.85 (-1.77%) |
| Huntsman | HUN | $11.35 | +0.03 (+0.31%) |

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
