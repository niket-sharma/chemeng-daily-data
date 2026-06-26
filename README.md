# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-06-26)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $68.99 | -2.93 (-4.07%) | $/barrel |
| Brent Crude Oil | $72.37 | -2.89 (-3.84%) | $/barrel |
| Natural Gas | $3.35 | +0.01 (+0.21%) | $/MMBtu |
| Heating Oil | $3.12 | -0.18 (-5.54%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $29.14 | -0.17 (-0.60%) |
| LyondellBasell | LYB | $55.70 | -0.14 (-0.25%) |
| DuPont | DD | $135.21 | -2.60 (-1.88%) |
| Air Products | APD | $279.82 | -0.11 (-0.04%) |
| Linde | LIN | $520.24 | -2.04 (-0.39%) |
| Eastman Chemical | EMN | $69.73 | -0.88 (-1.25%) |
| Celanese | CE | $47.86 | -1.06 (-2.17%) |
| Huntsman | HUN | $11.61 | +0.28 (+2.47%) |

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
