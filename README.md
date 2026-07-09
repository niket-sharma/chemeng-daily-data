# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-07-09)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $72.22 | -1.30 (-1.77%) | $/barrel |
| Brent Crude Oil | $76.65 | -1.37 (-1.76%) | $/barrel |
| Natural Gas | $3.03 | -0.18 (-5.76%) | $/MMBtu |
| Heating Oil | $3.57 | -0.09 (-2.38%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $28.23 | -0.81 (-2.77%) |
| LyondellBasell | LYB | $54.61 | -1.11 (-2.00%) |
| DuPont | DD | $136.04 | -0.93 (-0.68%) |
| Air Products | APD | $297.00 | +0.25 (+0.08%) |
| Linde | LIN | $520.62 | -7.05 (-1.34%) |
| Eastman Chemical | EMN | $67.26 | +0.36 (+0.54%) |
| Celanese | CE | $46.75 | -0.55 (-1.16%) |
| Huntsman | HUN | $10.65 | -0.65 (-5.75%) |

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
