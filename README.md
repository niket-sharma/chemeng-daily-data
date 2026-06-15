# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-06-15)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $80.41 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $82.94 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.11 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $3.24 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $32.83 | -1.01 (-3.00%) |
| LyondellBasell | LYB | $62.63 | -1.95 (-3.02%) |
| DuPont | DD | $49.09 | +0.83 (+1.72%) |
| Air Products | APD | $280.96 | -0.66 (-0.23%) |
| Linde | LIN | $520.55 | -3.02 (-0.58%) |
| Eastman Chemical | EMN | $76.23 | +1.01 (+1.34%) |
| Celanese | CE | $53.60 | +0.12 (+0.22%) |
| Huntsman | HUN | $15.84 | +0.10 (+0.64%) |

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
