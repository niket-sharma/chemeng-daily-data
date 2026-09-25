# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-09-25)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $92.23 | -2.38 (-2.52%) | $/barrel |
| Brent Crude Oil | $97.11 | -9.49 (-8.90%) | $/barrel |
| Natural Gas | $3.24 | -0.06 (-1.70%) | $/MMBtu |
| Heating Oil | $4.43 | -0.30 (-6.42%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $27.67 | -0.89 (-3.10%) |
| LyondellBasell | LYB | $57.90 | -2.28 (-3.78%) |
| DuPont | DD | $131.35 | +1.12 (+0.86%) |
| Air Products | APD | $282.13 | -2.36 (-0.83%) |
| Linde | LIN | $467.70 | -0.44 (-0.09%) |
| Eastman Chemical | EMN | $66.55 | +0.36 (+0.54%) |
| Celanese | CE | $46.69 | -0.87 (-1.83%) |
| Huntsman | HUN | $8.81 | +0.02 (+0.28%) |

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
