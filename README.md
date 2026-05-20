# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-05-20)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $100.83 | -6.94 (-6.44%) | $/barrel |
| Brent Crude Oil | $107.31 | -3.97 (-3.57%) | $/barrel |
| Natural Gas | $3.03 | -0.09 (-2.83%) | $/MMBtu |
| Heating Oil | $3.94 | -0.23 (-5.45%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $36.90 | -0.85 (-2.24%) |
| LyondellBasell | LYB | $71.50 | -1.54 (-2.11%) |
| DuPont | DD | $47.75 | +1.19 (+2.56%) |
| Air Products | APD | $288.32 | -3.45 (-1.18%) |
| Linde | LIN | $508.83 | +2.76 (+0.55%) |
| Eastman Chemical | EMN | $69.06 | +0.91 (+1.34%) |
| Celanese | CE | $53.84 | +0.35 (+0.65%) |
| Huntsman | HUN | $13.91 | +0.59 (+4.43%) |

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
