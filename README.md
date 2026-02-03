# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-02-03)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $61.89 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $66.06 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.17 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $2.36 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $28.88 | +1.33 (+4.83%) |
| LyondellBasell | LYB | $50.25 | +1.25 (+2.55%) |
| DuPont | DD | $44.43 | +0.51 (+1.16%) |
| Air Products | APD | $270.99 | -1.51 (-0.55%) |
| Linde | LIN | $460.16 | +3.19 (+0.70%) |
| Eastman Chemical | EMN | $71.48 | +2.16 (+3.12%) |
| Celanese | CE | $45.87 | +1.43 (+3.22%) |
| Huntsman | HUN | $11.48 | +0.66 (+6.10%) |

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
