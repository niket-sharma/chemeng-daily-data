# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-08-21)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $86.47 | -1.36 (-1.55%) | $/barrel |
| Brent Crude Oil | $93.78 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $2.81 | +0.08 (+2.96%) | $/MMBtu |
| Heating Oil | $4.39 | -0.09 (-2.06%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $33.01 | +0.11 (+0.33%) |
| LyondellBasell | LYB | $68.76 | +0.66 (+0.97%) |
| DuPont | DD | $140.35 | +1.89 (+1.37%) |
| Air Products | APD | $306.91 | +6.58 (+2.19%) |
| Linde | LIN | $491.35 | +10.06 (+2.09%) |
| Eastman Chemical | EMN | $74.42 | +0.63 (+0.85%) |
| Celanese | CE | $47.03 | +0.05 (+0.11%) |
| Huntsman | HUN | $10.15 | -0.01 (-0.10%) |

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
