# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-08-20)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $86.44 | +0.61 (+0.71%) | $/barrel |
| Brent Crude Oil | $93.69 | +2.07 (+2.26%) | $/barrel |
| Natural Gas | $2.75 | -0.06 (-2.24%) | $/MMBtu |
| Heating Oil | $4.36 | -0.09 (-2.03%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $32.60 | +0.85 (+2.69%) |
| LyondellBasell | LYB | $67.94 | +1.89 (+2.85%) |
| DuPont | DD | $139.27 | -0.41 (-0.29%) |
| Air Products | APD | $308.08 | +4.86 (+1.60%) |
| Linde | LIN | $485.95 | +4.82 (+1.00%) |
| Eastman Chemical | EMN | $73.72 | -1.44 (-1.92%) |
| Celanese | CE | $45.99 | -0.27 (-0.58%) |
| Huntsman | HUN | $9.98 | -0.20 (-1.96%) |

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
