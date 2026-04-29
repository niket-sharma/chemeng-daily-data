# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-04-29)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $99.36 | -0.57 (-0.57%) | $/barrel |
| Brent Crude Oil | $104.12 | -7.14 (-6.42%) | $/barrel |
| Natural Gas | $2.67 | +0.11 (+4.26%) | $/MMBtu |
| Heating Oil | $3.88 | -0.09 (-2.31%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $38.01 | -0.09 (-0.24%) |
| LyondellBasell | LYB | $71.48 | +0.46 (+0.65%) |
| DuPont | DD | $45.33 | -1.36 (-2.91%) |
| Air Products | APD | $303.35 | +0.97 (+0.32%) |
| Linde | LIN | $510.29 | -0.46 (-0.09%) |
| Eastman Chemical | EMN | $71.63 | -0.48 (-0.67%) |
| Celanese | CE | $64.65 | -0.44 (-0.68%) |
| Huntsman | HUN | $13.66 | -0.06 (-0.44%) |

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
