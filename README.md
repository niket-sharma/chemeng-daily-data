# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-10-23)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $103.01 | +3.54 (+3.56%) | $/barrel |
| Brent Crude Oil | $111.36 | -1.81 (-1.60%) | $/barrel |
| Natural Gas | $3.05 | +0.26 (+9.19%) | $/MMBtu |
| Heating Oil | $4.78 | -0.15 (-3.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $32.67 | +0.86 (+2.72%) |
| LyondellBasell | LYB | $66.43 | +1.06 (+1.62%) |
| DuPont | DD | $135.83 | +0.73 (+0.54%) |
| Air Products | APD | $307.09 | -1.13 (-0.37%) |
| Linde | LIN | $508.17 | -2.19 (-0.43%) |
| Eastman Chemical | EMN | $64.85 | -0.46 (-0.71%) |
| Celanese | CE | $47.23 | +0.01 (+0.02%) |
| Huntsman | HUN | $8.78 | +0.06 (+0.75%) |

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
