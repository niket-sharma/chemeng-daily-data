# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-04-20)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $86.09 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $94.16 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $2.68 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $3.42 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $36.49 | +0.90 (+2.51%) |
| LyondellBasell | LYB | $67.52 | +1.25 (+1.89%) |
| DuPont | DD | $47.42 | +0.08 (+0.16%) |
| Air Products | APD | $297.28 | +5.47 (+1.87%) |
| Linde | LIN | $500.08 | +7.85 (+1.59%) |
| Eastman Chemical | EMN | $73.48 | -0.30 (-0.41%) |
| Celanese | CE | $63.76 | +1.73 (+2.79%) |
| Huntsman | HUN | $13.71 | +0.36 (+2.70%) |

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
