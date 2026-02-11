# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-02-11)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $64.46 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $69.29 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.12 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $2.41 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $33.60 | +1.52 (+4.74%) |
| LyondellBasell | LYB | $57.66 | +2.19 (+3.95%) |
| DuPont | DD | $49.43 | +2.33 (+4.95%) |
| Air Products | APD | $290.77 | +4.40 (+1.54%) |
| Linde | LIN | $460.51 | +4.17 (+0.91%) |
| Eastman Chemical | EMN | $80.59 | +2.21 (+2.82%) |
| Celanese | CE | $58.32 | +3.29 (+5.98%) |
| Huntsman | HUN | $13.60 | +0.55 (+4.21%) |

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
