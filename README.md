# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-09-11)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $99.63 | -2.85 (-2.78%) | $/barrel |
| Brent Crude Oil | $104.50 | -3.13 (-2.91%) | $/barrel |
| Natural Gas | $2.81 | -0.03 (-0.95%) | $/MMBtu |
| Heating Oil | $4.77 | -0.29 (-5.70%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $29.33 | -0.31 (-1.06%) |
| LyondellBasell | LYB | $65.09 | +0.79 (+1.23%) |
| DuPont | DD | $126.56 | -0.76 (-0.60%) |
| Air Products | APD | $292.92 | -0.73 (-0.25%) |
| Linde | LIN | $467.10 | +5.48 (+1.19%) |
| Eastman Chemical | EMN | $68.14 | -0.24 (-0.36%) |
| Celanese | CE | $46.79 | +1.07 (+2.34%) |
| Huntsman | HUN | $9.62 | +0.10 (+1.00%) |

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
