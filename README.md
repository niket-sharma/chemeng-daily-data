# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-11-09)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $86.53 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $92.47 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.20 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $4.20 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $30.96 | -0.44 (-1.40%) |
| LyondellBasell | LYB | $59.50 | -1.22 (-2.01%) |
| DuPont | DD | $155.14 | +8.62 (+5.88%) |
| Air Products | APD | $311.08 | +6.24 (+2.05%) |
| Linde | LIN | $520.33 | +5.08 (+0.99%) |
| Eastman Chemical | EMN | $65.39 | +0.98 (+1.52%) |
| Celanese | CE | $48.75 | +2.26 (+4.86%) |
| Huntsman | HUN | $9.54 | +0.09 (+0.95%) |

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
