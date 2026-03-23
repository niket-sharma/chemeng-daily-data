# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-03-23)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $88.44 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $100.20 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $2.93 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $3.89 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $36.56 | -0.09 (-0.25%) |
| LyondellBasell | LYB | $72.42 | -0.90 (-1.23%) |
| DuPont | DD | $44.67 | +2.23 (+5.25%) |
| Air Products | APD | $283.36 | +2.35 (+0.83%) |
| Linde | LIN | $487.15 | -1.00 (-0.20%) |
| Eastman Chemical | EMN | $68.18 | +2.85 (+4.36%) |
| Celanese | CE | $56.66 | -0.29 (-0.51%) |
| Huntsman | HUN | $11.02 | +0.61 (+5.86%) |

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
