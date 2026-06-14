# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-06-14)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $84.88 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $87.33 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.12 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $3.36 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $33.85 | +0.22 (+0.65%) |
| LyondellBasell | LYB | $64.58 | +1.11 (+1.75%) |
| DuPont | DD | $48.26 | +1.42 (+3.03%) |
| Air Products | APD | $281.62 | +3.50 (+1.26%) |
| Linde | LIN | $523.57 | +8.13 (+1.58%) |
| Eastman Chemical | EMN | $75.22 | +1.90 (+2.59%) |
| Celanese | CE | $53.48 | +1.81 (+3.50%) |
| Huntsman | HUN | $15.74 | +0.66 (+4.38%) |

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
