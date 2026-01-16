# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-01-16)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $58.99 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $63.66 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.17 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $2.19 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $27.94 | -0.32 (-1.13%) |
| LyondellBasell | LYB | $50.88 | -1.12 (-2.15%) |
| DuPont | DD | $43.39 | +0.50 (+1.17%) |
| Air Products | APD | $265.98 | -1.27 (-0.48%) |
| Linde | LIN | $440.04 | +0.06 (+0.01%) |
| Eastman Chemical | EMN | $70.23 | +0.94 (+1.36%) |
| Celanese | CE | $47.14 | +0.18 (+0.38%) |
| Huntsman | HUN | $12.05 | +0.33 (+2.82%) |

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
