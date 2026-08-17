# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-08-17)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $82.51 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $88.90 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $2.69 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $4.24 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $31.15 | +0.08 (+0.24%) |
| LyondellBasell | LYB | $64.06 | +0.30 (+0.47%) |
| DuPont | DD | $144.31 | -1.95 (-1.33%) |
| Air Products | APD | $303.64 | -5.33 (-1.73%) |
| Linde | LIN | $476.91 | -5.83 (-1.21%) |
| Eastman Chemical | EMN | $73.25 | -0.82 (-1.10%) |
| Celanese | CE | $44.35 | -1.31 (-2.87%) |
| Huntsman | HUN | $10.31 | +0.01 (+0.10%) |

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
