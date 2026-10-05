# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-10-05)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $89.30 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $100.32 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.08 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $4.51 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $28.51 | +0.54 (+1.93%) |
| LyondellBasell | LYB | $59.22 | +0.64 (+1.09%) |
| DuPont | DD | $130.69 | +0.71 (+0.55%) |
| Air Products | APD | $279.45 | +1.88 (+0.68%) |
| Linde | LIN | $482.38 | +2.90 (+0.60%) |
| Eastman Chemical | EMN | $64.94 | +0.07 (+0.11%) |
| Celanese | CE | $45.53 | +1.34 (+3.03%) |
| Huntsman | HUN | $8.84 | +0.31 (+3.63%) |

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
