# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-06-18)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $73.27 | -3.52 (-4.58%) | $/barrel |
| Brent Crude Oil | $76.99 | -2.56 (-3.22%) | $/barrel |
| Natural Gas | $3.15 | +0.01 (+0.29%) | $/MMBtu |
| Heating Oil | $3.01 | -0.18 (-5.78%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $31.65 | -0.85 (-2.63%) |
| LyondellBasell | LYB | $59.56 | -2.25 (-3.64%) |
| DuPont | DD | $48.03 | +0.08 (+0.18%) |
| Air Products | APD | $280.57 | -1.18 (-0.42%) |
| Linde | LIN | $517.96 | +2.11 (+0.41%) |
| Eastman Chemical | EMN | $72.26 | +0.14 (+0.19%) |
| Celanese | CE | $51.05 | -0.18 (-0.35%) |
| Huntsman | HUN | $12.27 | -0.46 (-3.61%) |

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
