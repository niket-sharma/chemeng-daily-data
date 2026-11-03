# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-11-03)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $96.66 | +0.20 (+0.21%) | $/barrel |
| Brent Crude Oil | $104.31 | -0.46 (-0.44%) | $/barrel |
| Natural Gas | $2.91 | +0.06 (+2.00%) | $/MMBtu |
| Heating Oil | $4.56 | +0.14 (+3.18%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $33.88 | -0.30 (-0.86%) |
| LyondellBasell | LYB | $66.33 | -0.55 (-0.82%) |
| DuPont | DD | $154.09 | +12.79 (+9.05%) |
| Air Products | APD | $313.68 | -2.35 (-0.74%) |
| Linde | LIN | $514.00 | -5.72 (-1.10%) |
| Eastman Chemical | EMN | $65.75 | -1.03 (-1.53%) |
| Celanese | CE | $50.21 | +2.27 (+4.74%) |
| Huntsman | HUN | $9.72 | -0.23 (-2.34%) |

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
