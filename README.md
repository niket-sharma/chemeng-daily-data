# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-08-10)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $78.47 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $83.99 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $2.74 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $3.95 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $29.34 | -0.96 (-3.17%) |
| LyondellBasell | LYB | $59.59 | -1.85 (-3.01%) |
| DuPont | DD | $142.47 | -1.58 (-1.10%) |
| Air Products | APD | $303.44 | +3.52 (+1.17%) |
| Linde | LIN | $489.98 | -0.13 (-0.03%) |
| Eastman Chemical | EMN | $73.64 | +0.14 (+0.19%) |
| Celanese | CE | $43.89 | -0.06 (-0.14%) |
| Huntsman | HUN | $10.12 | -0.02 (-0.20%) |

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
