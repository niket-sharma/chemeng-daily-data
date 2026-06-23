# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-06-23)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $73.20 | -1.62 (-2.17%) | $/barrel |
| Brent Crude Oil | $76.85 | -1.05 (-1.35%) | $/barrel |
| Natural Gas | $3.21 | -0.04 (-1.29%) | $/MMBtu |
| Heating Oil | $3.07 | -0.02 (-0.74%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $30.68 | -0.11 (-0.36%) |
| LyondellBasell | LYB | $58.00 | -0.52 (-0.89%) |
| DuPont | DD | $47.29 | +0.00 (+0.00%) |
| Air Products | APD | $283.49 | +0.39 (+0.14%) |
| Linde | LIN | $518.59 | +1.88 (+0.36%) |
| Eastman Chemical | EMN | $70.76 | -1.20 (-1.67%) |
| Celanese | CE | $49.25 | -0.48 (-0.97%) |
| Huntsman | HUN | $11.55 | +0.05 (+0.39%) |

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
