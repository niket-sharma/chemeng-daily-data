# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-08-24)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $85.22 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $92.77 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $2.85 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $4.27 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $31.65 | -0.70 (-2.18%) |
| LyondellBasell | LYB | $65.95 | -1.58 (-2.34%) |
| DuPont | DD | $137.57 | -0.76 (-0.55%) |
| Air Products | APD | $304.46 | -0.64 (-0.21%) |
| Linde | LIN | $489.65 | +2.08 (+0.43%) |
| Eastman Chemical | EMN | $74.34 | +0.25 (+0.34%) |
| Celanese | CE | $46.26 | -0.54 (-1.16%) |
| Huntsman | HUN | $9.89 | -0.09 (-0.85%) |

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
