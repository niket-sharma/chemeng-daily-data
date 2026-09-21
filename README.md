# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-09-21)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $92.44 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $96.38 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $2.82 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $4.72 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $28.35 | -0.38 (-1.31%) |
| LyondellBasell | LYB | $60.55 | -1.38 (-2.23%) |
| DuPont | DD | $130.05 | +1.04 (+0.81%) |
| Air Products | APD | $281.95 | -2.23 (-0.78%) |
| Linde | LIN | $457.89 | -2.51 (-0.54%) |
| Eastman Chemical | EMN | $65.30 | -0.39 (-0.59%) |
| Celanese | CE | $45.01 | -0.40 (-0.87%) |
| Huntsman | HUN | $8.91 | -0.18 (-1.98%) |

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
