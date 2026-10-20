# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-10-20)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $97.60 | -6.06 (-5.85%) | $/barrel |
| Brent Crude Oil | $108.45 | -1.10 (-1.00%) | $/barrel |
| Natural Gas | $2.97 | -0.09 (-2.85%) | $/MMBtu |
| Heating Oil | $4.72 | -0.20 (-4.16%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $30.36 | +0.28 (+0.95%) |
| LyondellBasell | LYB | $63.51 | -0.20 (-0.31%) |
| DuPont | DD | $132.15 | +2.81 (+2.17%) |
| Air Products | APD | $300.02 | +1.37 (+0.46%) |
| Linde | LIN | $499.79 | -3.65 (-0.73%) |
| Eastman Chemical | EMN | $63.26 | +0.78 (+1.25%) |
| Celanese | CE | $47.35 | -0.53 (-1.11%) |
| Huntsman | HUN | $8.23 | -0.10 (-1.26%) |

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
