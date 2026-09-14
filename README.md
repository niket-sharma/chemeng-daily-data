# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-09-14)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $100.94 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $105.22 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $2.88 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $4.73 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $28.83 | -0.20 (-0.71%) |
| LyondellBasell | LYB | $62.56 | -1.12 (-1.77%) |
| DuPont | DD | $124.14 | -2.85 (-2.24%) |
| Air Products | APD | $288.40 | -3.02 (-1.04%) |
| Linde | LIN | $464.17 | -2.05 (-0.44%) |
| Eastman Chemical | EMN | $67.21 | -0.90 (-1.33%) |
| Celanese | CE | $45.06 | -1.03 (-2.25%) |
| Huntsman | HUN | $9.38 | -0.16 (-1.68%) |

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
