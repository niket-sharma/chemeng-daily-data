# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-03-10)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $90.02 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $93.89 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.12 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $3.24 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $34.31 | +1.03 (+3.09%) |
| LyondellBasell | LYB | $66.82 | -0.29 (-0.43%) |
| DuPont | DD | $45.24 | -0.02 (-0.04%) |
| Air Products | APD | $274.40 | +2.22 (+0.82%) |
| Linde | LIN | $483.62 | -1.12 (-0.23%) |
| Eastman Chemical | EMN | $69.60 | -0.73 (-1.04%) |
| Celanese | CE | $51.45 | +2.13 (+4.32%) |
| Huntsman | HUN | $12.11 | +0.67 (+5.86%) |

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
