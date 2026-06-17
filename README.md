# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-06-17)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $75.09 | -0.96 (-1.26%) | $/barrel |
| Brent Crude Oil | $78.67 | -0.29 (-0.37%) | $/barrel |
| Natural Gas | $3.25 | +0.01 (+0.28%) | $/MMBtu |
| Heating Oil | $3.15 | -0.02 (-0.78%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $nan | +nan (+nan%) |
| LyondellBasell | LYB | $62.59 | -0.71 (-1.12%) |
| DuPont | DD | $48.04 | -0.50 (-1.03%) |
| Air Products | APD | $280.48 | -2.48 (-0.88%) |
| Linde | LIN | $518.17 | -3.31 (-0.63%) |
| Eastman Chemical | EMN | $73.28 | -2.00 (-2.66%) |
| Celanese | CE | $51.93 | -1.84 (-3.42%) |
| Huntsman | HUN | $13.18 | -2.71 (-17.05%) |

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
