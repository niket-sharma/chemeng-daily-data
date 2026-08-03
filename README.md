# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-08-03)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $79.51 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $83.75 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $2.77 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $3.92 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $30.38 | +0.09 (+0.30%) |
| LyondellBasell | LYB | $61.83 | -0.25 (-0.40%) |
| DuPont | DD | $138.83 | +1.83 (+1.34%) |
| Air Products | APD | $291.30 | -3.59 (-1.22%) |
| Linde | LIN | $479.67 | +1.29 (+0.27%) |
| Eastman Chemical | EMN | $71.50 | +1.55 (+2.22%) |
| Celanese | CE | $44.43 | -0.29 (-0.65%) |
| Huntsman | HUN | $10.05 | +0.28 (+2.92%) |

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
