# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-03-19)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $96.32 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $107.38 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.07 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $4.20 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $37.69 | +0.78 (+2.11%) |
| LyondellBasell | LYB | $75.20 | +4.00 (+5.62%) |
| DuPont | DD | $44.00 | -1.54 (-3.38%) |
| Air Products | APD | $281.42 | -4.73 (-1.65%) |
| Linde | LIN | $488.57 | -5.48 (-1.11%) |
| Eastman Chemical | EMN | $68.91 | -2.36 (-3.31%) |
| Celanese | CE | $59.89 | -0.29 (-0.48%) |
| Huntsman | HUN | $11.96 | -0.25 (-2.05%) |

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
