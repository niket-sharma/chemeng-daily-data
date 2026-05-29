# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-05-29)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $87.86 | -1.04 (-1.17%) | $/barrel |
| Brent Crude Oil | $91.12 | -2.59 (-2.76%) | $/barrel |
| Natural Gas | $3.32 | +0.03 (+1.04%) | $/MMBtu |
| Heating Oil | $3.55 | -0.07 (-1.89%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $34.13 | -0.64 (-1.84%) |
| LyondellBasell | LYB | $68.25 | -0.10 (-0.15%) |
| DuPont | DD | $47.64 | -0.07 (-0.15%) |
| Air Products | APD | $279.26 | -4.39 (-1.55%) |
| Linde | LIN | $500.42 | -1.57 (-0.31%) |
| Eastman Chemical | EMN | $75.50 | -0.86 (-1.13%) |
| Celanese | CE | $53.26 | -0.01 (-0.01%) |
| Huntsman | HUN | $15.45 | -0.02 (-0.10%) |

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
