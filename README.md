# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-04-08)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $93.93 | -19.02 (-16.84%) | $/barrel |
| Brent Crude Oil | $93.01 | -16.26 (-14.88%) | $/barrel |
| Natural Gas | $2.74 | -0.13 (-4.46%) | $/MMBtu |
| Heating Oil | $3.78 | -0.69 (-15.48%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $36.64 | -4.77 (-11.52%) |
| LyondellBasell | LYB | $69.17 | -11.09 (-13.82%) |
| DuPont | DD | $47.06 | +1.53 (+3.36%) |
| Air Products | APD | $285.83 | -6.56 (-2.24%) |
| Linde | LIN | $490.58 | -4.01 (-0.81%) |
| Eastman Chemical | EMN | $73.49 | -1.07 (-1.43%) |
| Celanese | CE | $61.08 | -2.49 (-3.92%) |
| Huntsman | HUN | $13.05 | -0.22 (-1.62%) |

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
