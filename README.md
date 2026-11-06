# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-11-06)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $90.97 | +0.45 (+0.50%) | $/barrel |
| Brent Crude Oil | $98.41 | +0.12 (+0.12%) | $/barrel |
| Natural Gas | $2.99 | +0.05 (+1.56%) | $/MMBtu |
| Heating Oil | $4.35 | -0.00 (-0.03%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $31.69 | -0.28 (-0.89%) |
| LyondellBasell | LYB | $61.40 | -0.24 (-0.38%) |
| DuPont | DD | $147.27 | +2.34 (+1.61%) |
| Air Products | APD | $306.87 | -2.62 (-0.85%) |
| Linde | LIN | $517.98 | -3.25 (-0.62%) |
| Eastman Chemical | EMN | $64.89 | -0.82 (-1.24%) |
| Celanese | CE | $46.81 | -1.03 (-2.16%) |
| Huntsman | HUN | $9.51 | -0.28 (-2.91%) |

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
