# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-11-16)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $85.06 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $91.84 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.12 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $3.97 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $31.96 | -1.08 (-3.27%) |
| LyondellBasell | LYB | $61.67 | -2.76 (-4.28%) |
| DuPont | DD | $149.99 | -3.79 (-2.46%) |
| Air Products | APD | $313.90 | -2.63 (-0.83%) |
| Linde | LIN | $523.46 | -2.60 (-0.49%) |
| Eastman Chemical | EMN | $63.49 | -1.54 (-2.37%) |
| Celanese | CE | $48.96 | -2.45 (-4.77%) |
| Huntsman | HUN | $9.30 | -0.23 (-2.41%) |

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
