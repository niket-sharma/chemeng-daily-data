# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-01-28)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $62.80 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $66.93 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.74 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $2.42 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $27.81 | -0.37 (-1.31%) |
| LyondellBasell | LYB | $50.43 | -0.43 (-0.85%) |
| DuPont | DD | $44.61 | +0.41 (+0.93%) |
| Air Products | APD | $259.12 | -3.50 (-1.33%) |
| Linde | LIN | $453.03 | -2.00 (-0.44%) |
| Eastman Chemical | EMN | $68.92 | +0.03 (+0.04%) |
| Celanese | CE | $46.86 | -0.67 (-1.41%) |
| Huntsman | HUN | $11.37 | -0.35 (-2.99%) |

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
