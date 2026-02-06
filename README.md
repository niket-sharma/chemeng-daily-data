# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-02-06)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $63.66 | +0.37 (+0.58%) | $/barrel |
| Brent Crude Oil | $67.88 | +0.33 (+0.49%) | $/barrel |
| Natural Gas | $3.49 | -0.02 (-0.54%) | $/MMBtu |
| Heating Oil | $2.41 | +0.02 (+0.73%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $30.60 | -1.80 (-5.56%) |
| LyondellBasell | LYB | $53.88 | -3.22 (-5.64%) |
| DuPont | DD | $45.68 | -2.15 (-4.50%) |
| Air Products | APD | $283.50 | -3.09 (-1.08%) |
| Linde | LIN | $459.69 | -13.64 (-2.88%) |
| Eastman Chemical | EMN | $76.08 | -2.41 (-3.07%) |
| Celanese | CE | $52.06 | -0.75 (-1.42%) |
| Huntsman | HUN | $13.20 | -0.53 (-3.86%) |

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
