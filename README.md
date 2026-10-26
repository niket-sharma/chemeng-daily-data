# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-10-26)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $102.32 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $111.22 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.04 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $4.75 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $34.15 | +1.54 (+4.72%) |
| LyondellBasell | LYB | $67.43 | +0.98 (+1.47%) |
| DuPont | DD | $137.02 | +0.47 (+0.34%) |
| Air Products | APD | $306.71 | -0.43 (-0.14%) |
| Linde | LIN | $508.97 | +0.14 (+0.03%) |
| Eastman Chemical | EMN | $65.94 | +1.01 (+1.56%) |
| Celanese | CE | $48.49 | +0.78 (+1.63%) |
| Huntsman | HUN | $8.97 | +0.16 (+1.87%) |

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
