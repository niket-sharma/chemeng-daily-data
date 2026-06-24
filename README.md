# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-06-24)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $70.00 | -3.21 (-4.38%) | $/barrel |
| Brent Crude Oil | $73.66 | -3.42 (-4.44%) | $/barrel |
| Natural Gas | $3.23 | +0.08 (+2.54%) | $/MMBtu |
| Heating Oil | $3.08 | -0.08 (-2.49%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $29.08 | -1.25 (-4.10%) |
| LyondellBasell | LYB | $55.66 | -1.94 (-3.37%) |
| DuPont | DD | $139.97 | -0.04 (-0.03%) |
| Air Products | APD | $279.21 | -3.24 (-1.15%) |
| Linde | LIN | $521.86 | +9.60 (+1.87%) |
| Eastman Chemical | EMN | $70.45 | +0.97 (+1.40%) |
| Celanese | CE | $47.46 | -0.67 (-1.39%) |
| Huntsman | HUN | $11.28 | -0.10 (-0.83%) |

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
