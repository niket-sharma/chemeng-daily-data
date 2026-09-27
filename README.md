# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-09-27)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $92.41 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $97.44 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.22 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $4.46 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $28.02 | -0.54 (-1.89%) |
| LyondellBasell | LYB | $58.14 | -2.04 (-3.39%) |
| DuPont | DD | $131.71 | +1.49 (+1.14%) |
| Air Products | APD | $281.76 | -2.73 (-0.96%) |
| Linde | LIN | $469.89 | +1.75 (+0.37%) |
| Eastman Chemical | EMN | $66.97 | +0.78 (+1.18%) |
| Celanese | CE | $47.09 | -0.47 (-0.99%) |
| Huntsman | HUN | $8.90 | +0.11 (+1.25%) |

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
