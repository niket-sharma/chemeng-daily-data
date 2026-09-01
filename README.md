# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-09-01)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $89.57 | +3.81 (+4.44%) | $/barrel |
| Brent Crude Oil | $94.07 | +3.58 (+3.96%) | $/barrel |
| Natural Gas | $2.90 | -0.03 (-1.09%) | $/MMBtu |
| Heating Oil | $4.66 | +0.17 (+3.72%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $30.24 | -0.28 (-0.93%) |
| LyondellBasell | LYB | $64.77 | -0.31 (-0.48%) |
| DuPont | DD | $132.29 | -2.30 (-1.71%) |
| Air Products | APD | $305.22 | -4.24 (-1.37%) |
| Linde | LIN | $483.45 | -6.13 (-1.25%) |
| Eastman Chemical | EMN | $70.66 | -1.78 (-2.46%) |
| Celanese | CE | $44.47 | -1.01 (-2.22%) |
| Huntsman | HUN | $9.48 | -0.10 (-1.10%) |

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
