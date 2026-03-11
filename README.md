# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-03-11)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $85.15 | +1.70 (+2.04%) | $/barrel |
| Brent Crude Oil | $86.55 | -1.25 (-1.42%) | $/barrel |
| Natural Gas | $3.09 | +0.07 (+2.35%) | $/MMBtu |
| Heating Oil | $3.06 | -0.29 (-8.67%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $34.01 | +0.12 (+0.37%) |
| LyondellBasell | LYB | $66.28 | +0.67 (+1.02%) |
| DuPont | DD | $45.55 | -0.42 (-0.91%) |
| Air Products | APD | $274.42 | -0.70 (-0.25%) |
| Linde | LIN | $474.12 | -3.82 (-0.80%) |
| Eastman Chemical | EMN | $68.62 | -0.60 (-0.87%) |
| Celanese | CE | $51.70 | +1.03 (+2.03%) |
| Huntsman | HUN | $12.01 | -0.07 (-0.58%) |

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
