# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-03-27)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $97.48 | +3.00 (+3.18%) | $/barrel |
| Brent Crude Oil | $103.66 | -4.35 (-4.03%) | $/barrel |
| Natural Gas | $2.99 | -0.01 (-0.20%) | $/MMBtu |
| Heating Oil | $4.16 | -0.11 (-2.59%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $40.21 | +0.74 (+1.87%) |
| LyondellBasell | LYB | $78.29 | +0.57 (+0.73%) |
| DuPont | DD | $45.94 | -0.08 (-0.17%) |
| Air Products | APD | $291.79 | -1.39 (-0.47%) |
| Linde | LIN | $492.34 | -3.15 (-0.64%) |
| Eastman Chemical | EMN | $72.01 | -0.49 (-0.67%) |
| Celanese | CE | $63.58 | +2.03 (+3.31%) |
| Huntsman | HUN | $12.73 | +0.18 (+1.43%) |

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
