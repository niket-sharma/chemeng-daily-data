# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-01-23)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $59.90 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $64.62 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $4.98 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $2.32 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $28.33 | -0.08 (-0.28%) |
| LyondellBasell | LYB | $51.54 | -0.28 (-0.54%) |
| DuPont | DD | $43.79 | +0.41 (+0.95%) |
| Air Products | APD | $264.04 | +0.93 (+0.35%) |
| Linde | LIN | $445.64 | +6.29 (+1.43%) |
| Eastman Chemical | EMN | $68.95 | +0.65 (+0.95%) |
| Celanese | CE | $47.98 | -0.14 (-0.29%) |
| Huntsman | HUN | $12.13 | +0.13 (+1.08%) |

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
