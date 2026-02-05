# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-02-05)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $63.54 | -1.60 (-2.46%) | $/barrel |
| Brent Crude Oil | $67.73 | -1.73 (-2.49%) | $/barrel |
| Natural Gas | $3.50 | +0.03 (+0.98%) | $/MMBtu |
| Heating Oil | $2.40 | -0.07 (-3.02%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $31.60 | -0.80 (-2.47%) |
| LyondellBasell | LYB | $55.72 | -1.38 (-2.43%) |
| DuPont | DD | $46.60 | -1.23 (-2.57%) |
| Air Products | APD | $284.45 | -2.14 (-0.74%) |
| Linde | LIN | $469.51 | -3.82 (-0.81%) |
| Eastman Chemical | EMN | $77.36 | -1.13 (-1.45%) |
| Celanese | CE | $52.70 | -0.11 (-0.21%) |
| Huntsman | HUN | $13.39 | -0.34 (-2.48%) |

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
