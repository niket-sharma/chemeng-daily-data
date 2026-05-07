# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-05-07)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $91.42 | -3.66 (-3.85%) | $/barrel |
| Brent Crude Oil | $97.42 | -3.85 (-3.80%) | $/barrel |
| Natural Gas | $2.77 | +0.04 (+1.43%) | $/MMBtu |
| Heating Oil | $3.65 | -0.14 (-3.62%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $37.10 | -1.40 (-3.62%) |
| LyondellBasell | LYB | $70.78 | -2.70 (-3.67%) |
| DuPont | DD | $49.10 | -0.97 (-1.94%) |
| Air Products | APD | $294.26 | -5.95 (-1.98%) |
| Linde | LIN | $498.10 | -3.77 (-0.75%) |
| Eastman Chemical | EMN | $75.42 | -0.32 (-0.42%) |
| Celanese | CE | $58.89 | -3.23 (-5.20%) |
| Huntsman | HUN | $14.87 | -0.23 (-1.52%) |

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
