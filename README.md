# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-07-15)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $78.85 | -0.49 (-0.62%) | $/barrel |
| Brent Crude Oil | $83.82 | -0.91 (-1.07%) | $/barrel |
| Natural Gas | $2.91 | +0.00 (+0.10%) | $/MMBtu |
| Heating Oil | $3.83 | -0.18 (-4.60%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $29.53 | -0.78 (-2.57%) |
| LyondellBasell | LYB | $57.91 | +0.00 (+0.00%) |
| DuPont | DD | $134.19 | +0.00 (+0.00%) |
| Air Products | APD | $296.48 | +0.00 (+0.00%) |
| Linde | LIN | $515.79 | +0.00 (+0.00%) |
| Eastman Chemical | EMN | $68.08 | +0.00 (+0.00%) |
| Celanese | CE | $47.55 | +0.00 (+0.00%) |
| Huntsman | HUN | $11.96 | +0.00 (+0.00%) |

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
