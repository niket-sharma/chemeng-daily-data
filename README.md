# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-02-09)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $63.46 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $67.98 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.16 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $2.39 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $31.05 | -0.74 (-2.31%) |
| LyondellBasell | LYB | $53.83 | -1.27 (-2.30%) |
| DuPont | DD | $46.46 | -0.27 (-0.58%) |
| Air Products | APD | $281.11 | -2.01 (-0.71%) |
| Linde | LIN | $444.76 | -3.48 (-0.78%) |
| Eastman Chemical | EMN | $76.82 | -0.61 (-0.79%) |
| Celanese | CE | $53.92 | -0.96 (-1.74%) |
| Huntsman | HUN | $13.22 | -0.24 (-1.78%) |

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
