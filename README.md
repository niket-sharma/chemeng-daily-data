# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-04-09)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $101.46 | +7.05 (+7.47%) | $/barrel |
| Brent Crude Oil | $98.92 | +4.17 (+4.40%) | $/barrel |
| Natural Gas | $2.70 | -0.02 (-0.70%) | $/MMBtu |
| Heating Oil | $4.07 | +0.26 (+6.90%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $40.10 | +0.83 (+2.10%) |
| LyondellBasell | LYB | $75.68 | +1.46 (+1.97%) |
| DuPont | DD | $47.46 | -0.39 (-0.82%) |
| Air Products | APD | $298.68 | +2.08 (+0.70%) |
| Linde | LIN | $504.72 | +4.24 (+0.85%) |
| Eastman Chemical | EMN | $73.06 | -1.21 (-1.63%) |
| Celanese | CE | $64.37 | +0.62 (+0.97%) |
| Huntsman | HUN | $13.44 | -0.13 (-0.96%) |

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
