# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-10-18)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $99.02 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $109.86 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.12 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $4.72 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $29.93 | +0.27 (+0.91%) |
| LyondellBasell | LYB | $64.01 | +1.34 (+2.14%) |
| DuPont | DD | $130.45 | -1.15 (-0.87%) |
| Air Products | APD | $299.59 | +2.99 (+1.01%) |
| Linde | LIN | $498.43 | +5.21 (+1.06%) |
| Eastman Chemical | EMN | $62.33 | -1.54 (-2.41%) |
| Celanese | CE | $47.49 | +1.05 (+2.26%) |
| Huntsman | HUN | $8.58 | +0.02 (+0.23%) |

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
