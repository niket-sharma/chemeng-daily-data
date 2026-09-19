# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-09-19)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $100.30 | -1.61 (-1.58%) | $/barrel |
| Brent Crude Oil | $103.87 | -0.95 (-0.91%) | $/barrel |
| Natural Gas | $2.91 | +0.01 (+0.38%) | $/MMBtu |
| Heating Oil | $5.06 | -0.06 (-1.10%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $28.73 | -0.76 (-2.58%) |
| LyondellBasell | LYB | $61.93 | -2.32 (-3.61%) |
| DuPont | DD | $129.01 | +0.55 (+0.43%) |
| Air Products | APD | $284.18 | -1.94 (-0.68%) |
| Linde | LIN | $460.40 | +1.92 (+0.42%) |
| Eastman Chemical | EMN | $65.69 | -0.55 (-0.83%) |
| Celanese | CE | $45.41 | -1.40 (-2.99%) |
| Huntsman | HUN | $9.09 | -0.03 (-0.33%) |

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
