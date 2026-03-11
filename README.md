# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-03-11)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $82.81 | -0.64 (-0.77%) | $/barrel |
| Brent Crude Oil | $84.48 | -3.32 (-3.78%) | $/barrel |
| Natural Gas | $3.03 | +0.01 (+0.26%) | $/MMBtu |
| Heating Oil | $3.15 | -0.20 (-5.86%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $33.89 | -0.42 (-1.22%) |
| LyondellBasell | LYB | $65.61 | -1.21 (-1.81%) |
| DuPont | DD | $45.97 | +0.73 (+1.61%) |
| Air Products | APD | $275.12 | +0.72 (+0.26%) |
| Linde | LIN | $477.94 | -5.68 (-1.17%) |
| Eastman Chemical | EMN | $69.22 | -0.38 (-0.55%) |
| Celanese | CE | $50.67 | -0.78 (-1.52%) |
| Huntsman | HUN | $12.08 | -0.03 (-0.25%) |

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
