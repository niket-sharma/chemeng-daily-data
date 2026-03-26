# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-03-26)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $90.32 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $102.22 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $2.95 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $4.01 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $39.62 | +1.31 (+3.42%) |
| LyondellBasell | LYB | $77.19 | +1.18 (+1.55%) |
| DuPont | DD | $46.33 | +1.00 (+2.21%) |
| Air Products | APD | $290.09 | +3.84 (+1.34%) |
| Linde | LIN | $492.34 | +12.50 (+2.61%) |
| Eastman Chemical | EMN | $71.40 | +1.45 (+2.07%) |
| Celanese | CE | $62.66 | +1.86 (+3.06%) |
| Huntsman | HUN | $12.37 | +0.96 (+8.41%) |

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
