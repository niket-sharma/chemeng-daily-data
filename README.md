# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-03-25)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $88.74 | -3.61 (-3.91%) | $/barrel |
| Brent Crude Oil | $96.22 | -8.27 (-7.91%) | $/barrel |
| Natural Gas | $2.87 | -0.07 (-2.48%) | $/MMBtu |
| Heating Oil | $3.72 | -0.57 (-13.29%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $39.33 | +1.02 (+2.68%) |
| LyondellBasell | LYB | $76.58 | +0.57 (+0.75%) |
| DuPont | DD | $45.91 | +0.58 (+1.28%) |
| Air Products | APD | $285.64 | -0.61 (-0.21%) |
| Linde | LIN | $483.89 | +4.05 (+0.84%) |
| Eastman Chemical | EMN | $70.79 | +0.84 (+1.19%) |
| Celanese | CE | $62.55 | +1.75 (+2.88%) |
| Huntsman | HUN | $11.92 | +0.51 (+4.47%) |

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
