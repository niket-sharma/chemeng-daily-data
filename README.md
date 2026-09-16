# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-09-16)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $102.41 | -3.42 (-3.23%) | $/barrel |
| Brent Crude Oil | $105.67 | -3.08 (-2.83%) | $/barrel |
| Natural Gas | $2.89 | -0.03 (-1.03%) | $/MMBtu |
| Heating Oil | $5.00 | -0.26 (-5.03%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $30.28 | +0.43 (+1.46%) |
| LyondellBasell | LYB | $64.98 | -0.45 (-0.69%) |
| DuPont | DD | $128.65 | +0.61 (+0.48%) |
| Air Products | APD | $289.18 | -1.38 (-0.47%) |
| Linde | LIN | $463.99 | +1.03 (+0.22%) |
| Eastman Chemical | EMN | $66.12 | +0.24 (+0.36%) |
| Celanese | CE | $47.54 | +0.32 (+0.68%) |
| Huntsman | HUN | $9.31 | +0.09 (+0.98%) |

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
