# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-07-27)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $83.34 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $89.71 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $2.80 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $4.08 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $28.80 | +0.00 (+0.00%) |
| LyondellBasell | LYB | $58.58 | +0.00 (+0.00%) |
| DuPont | DD | $137.51 | +0.00 (+0.00%) |
| Air Products | APD | $292.30 | +0.00 (+0.00%) |
| Linde | LIN | $507.42 | +0.00 (+0.00%) |
| Eastman Chemical | EMN | $67.60 | +0.00 (+0.00%) |
| Celanese | CE | $44.63 | +0.00 (+0.00%) |
| Huntsman | HUN | $11.95 | +0.00 (+0.00%) |

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
