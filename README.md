# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-03-21)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $98.23 | +2.09 (+2.17%) | $/barrel |
| Brent Crude Oil | $106.41 | -2.24 (-2.06%) | $/barrel |
| Natural Gas | $3.10 | -0.07 (-2.24%) | $/MMBtu |
| Heating Oil | $4.24 | -0.10 (-2.29%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $36.65 | -0.84 (-2.24%) |
| LyondellBasell | LYB | $73.32 | -1.25 (-1.68%) |
| DuPont | DD | $42.44 | -1.08 (-2.48%) |
| Air Products | APD | $281.01 | -3.14 (-1.11%) |
| Linde | LIN | $488.15 | -1.65 (-0.34%) |
| Eastman Chemical | EMN | $65.33 | -3.43 (-4.99%) |
| Celanese | CE | $56.95 | -3.38 (-5.60%) |
| Huntsman | HUN | $10.41 | -1.10 (-9.56%) |

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
