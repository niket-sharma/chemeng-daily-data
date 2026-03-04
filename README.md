# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-03-04)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $74.19 | -0.37 (-0.50%) | $/barrel |
| Brent Crude Oil | $81.26 | -0.14 (-0.17%) | $/barrel |
| Natural Gas | $2.96 | -0.10 (-3.14%) | $/MMBtu |
| Heating Oil | $2.79 | -0.39 (-12.35%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $30.74 | +0.14 (+0.46%) |
| LyondellBasell | LYB | $58.21 | +0.33 (+0.57%) |
| DuPont | DD | $48.27 | -1.37 (-2.76%) |
| Air Products | APD | $273.04 | -3.39 (-1.23%) |
| Linde | LIN | $501.68 | -7.66 (-1.50%) |
| Eastman Chemical | EMN | $74.16 | -1.12 (-1.49%) |
| Celanese | CE | $51.32 | +1.59 (+3.20%) |
| Huntsman | HUN | $12.38 | +0.08 (+0.65%) |

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
