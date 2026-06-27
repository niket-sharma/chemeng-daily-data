# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-06-27)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $69.23 | -2.69 (-3.74%) | $/barrel |
| Brent Crude Oil | $71.99 | -3.27 (-4.34%) | $/barrel |
| Natural Gas | $3.23 | -0.11 (-3.35%) | $/MMBtu |
| Heating Oil | $3.21 | -0.09 (-2.73%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $nan | +nan (+nan%) |
| LyondellBasell | LYB | $nan | +nan (+nan%) |
| DuPont | DD | $nan | +nan (+nan%) |
| Air Products | APD | $nan | +nan (+nan%) |
| Linde | LIN | $nan | +nan (+nan%) |
| Eastman Chemical | EMN | $nan | +nan (+nan%) |
| Celanese | CE | $nan | +nan (+nan%) |
| Huntsman | HUN | $nan | +nan (+nan%) |

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
