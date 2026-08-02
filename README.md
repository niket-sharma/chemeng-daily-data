# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-08-02)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $84.67 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $90.12 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $2.75 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $4.10 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $30.29 | +0.20 (+0.66%) |
| LyondellBasell | LYB | $62.08 | +1.64 (+2.71%) |
| DuPont | DD | $137.00 | -1.84 (-1.33%) |
| Air Products | APD | $294.89 | -5.31 (-1.77%) |
| Linde | LIN | $478.38 | -30.26 (-5.95%) |
| Eastman Chemical | EMN | $69.95 | -0.12 (-0.17%) |
| Celanese | CE | $44.72 | -0.09 (-0.20%) |
| Huntsman | HUN | $9.76 | -2.31 (-19.14%) |

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
