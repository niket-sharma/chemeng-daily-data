# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-10-13)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $94.57 | +0.83 (+0.89%) | $/barrel |
| Brent Crude Oil | $106.07 | -0.58 (-0.54%) | $/barrel |
| Natural Gas | $3.32 | +0.15 (+4.67%) | $/MMBtu |
| Heating Oil | $4.95 | +0.23 (+4.80%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $28.55 | +0.42 (+1.51%) |
| LyondellBasell | LYB | $60.01 | +0.60 (+1.00%) |
| DuPont | DD | $129.46 | +0.09 (+0.07%) |
| Air Products | APD | $289.11 | +5.24 (+1.85%) |
| Linde | LIN | $492.14 | +4.79 (+0.98%) |
| Eastman Chemical | EMN | $62.97 | +0.88 (+1.41%) |
| Celanese | CE | $44.72 | +0.15 (+0.35%) |
| Huntsman | HUN | $8.15 | +0.09 (+1.05%) |

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
