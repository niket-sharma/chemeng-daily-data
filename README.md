# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-02-26)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $65.58 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $70.86 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $2.86 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $2.53 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $30.02 | -1.03 (-3.32%) |
| LyondellBasell | LYB | $56.75 | -1.57 (-2.69%) |
| DuPont | DD | $50.74 | -0.33 (-0.65%) |
| Air Products | APD | $280.30 | +0.83 (+0.30%) |
| Linde | LIN | $508.27 | +4.27 (+0.85%) |
| Eastman Chemical | EMN | $75.47 | -1.65 (-2.14%) |
| Celanese | CE | $50.03 | -3.06 (-5.76%) |
| Huntsman | HUN | $12.41 | -0.59 (-4.54%) |

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
