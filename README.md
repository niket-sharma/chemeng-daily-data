# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-02-22)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $66.48 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $71.30 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $2.98 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $2.48 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $30.52 | -0.87 (-2.77%) |
| LyondellBasell | LYB | $56.67 | +1.34 (+2.42%) |
| DuPont | DD | $50.41 | +0.17 (+0.34%) |
| Air Products | APD | $281.18 | +0.46 (+0.16%) |
| Linde | LIN | $496.51 | +6.40 (+1.31%) |
| Eastman Chemical | EMN | $79.16 | +1.14 (+1.46%) |
| Celanese | CE | $54.11 | -0.81 (-1.47%) |
| Huntsman | HUN | $12.59 | -0.10 (-0.79%) |

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
