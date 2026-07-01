# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-07-01)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $69.78 | +0.28 (+0.40%) | $/barrel |
| Brent Crude Oil | $73.26 | +0.34 (+0.47%) | $/barrel |
| Natural Gas | $3.25 | -0.02 (-0.67%) | $/MMBtu |
| Heating Oil | $3.25 | -0.07 (-2.07%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $27.36 | -0.56 (-2.01%) |
| LyondellBasell | LYB | $52.65 | -0.97 (-1.81%) |
| DuPont | DD | $135.64 | -0.10 (-0.07%) |
| Air Products | APD | $293.18 | +21.83 (+8.04%) |
| Linde | LIN | $518.94 | +7.88 (+1.54%) |
| Eastman Chemical | EMN | $66.98 | +0.06 (+0.09%) |
| Celanese | CE | $46.00 | +0.07 (+0.15%) |
| Huntsman | HUN | $10.62 | -0.33 (-3.01%) |

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
