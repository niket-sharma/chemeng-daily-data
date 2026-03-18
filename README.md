# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-03-18)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $98.08 | +1.87 (+1.94%) | $/barrel |
| Brent Crude Oil | $109.15 | +5.73 (+5.54%) | $/barrel |
| Natural Gas | $3.05 | +0.02 (+0.66%) | $/MMBtu |
| Heating Oil | $4.03 | +0.02 (+0.42%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $37.24 | +0.33 (+0.89%) |
| LyondellBasell | LYB | $72.99 | +1.79 (+2.51%) |
| DuPont | DD | $44.38 | -1.16 (-2.55%) |
| Air Products | APD | $284.12 | -2.03 (-0.71%) |
| Linde | LIN | $490.68 | -3.37 (-0.68%) |
| Eastman Chemical | EMN | $70.46 | -0.81 (-1.14%) |
| Celanese | CE | $59.50 | -0.68 (-1.13%) |
| Huntsman | HUN | $11.99 | -0.22 (-1.80%) |

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
