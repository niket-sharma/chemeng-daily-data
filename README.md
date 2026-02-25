# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-02-25)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $65.58 | -0.05 (-0.08%) | $/barrel |
| Brent Crude Oil | $70.65 | -0.12 (-0.17%) | $/barrel |
| Natural Gas | $2.89 | -0.02 (-0.75%) | $/MMBtu |
| Heating Oil | $2.49 | -0.20 (-7.44%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $30.81 | -0.24 (-0.77%) |
| LyondellBasell | LYB | $57.51 | -0.81 (-1.39%) |
| DuPont | DD | $51.28 | +0.21 (+0.41%) |
| Air Products | APD | $280.65 | +1.18 (+0.42%) |
| Linde | LIN | $507.94 | +3.94 (+0.78%) |
| Eastman Chemical | EMN | $76.84 | -0.28 (-0.36%) |
| Celanese | CE | $52.46 | -0.63 (-1.19%) |
| Huntsman | HUN | $12.99 | -0.01 (-0.08%) |

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
