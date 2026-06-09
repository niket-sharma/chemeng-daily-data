# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-06-09)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $91.30 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $94.25 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.15 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $3.60 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $34.20 | +0.23 (+0.68%) |
| LyondellBasell | LYB | $64.43 | -0.07 (-0.11%) |
| DuPont | DD | $46.99 | +0.14 (+0.30%) |
| Air Products | APD | $276.77 | -5.58 (-1.98%) |
| Linde | LIN | $501.92 | -5.98 (-1.18%) |
| Eastman Chemical | EMN | $71.67 | -0.17 (-0.24%) |
| Celanese | CE | $49.08 | -1.95 (-3.82%) |
| Huntsman | HUN | $14.23 | +0.02 (+0.14%) |

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
