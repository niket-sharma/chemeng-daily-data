# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-07-14)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $78.44 | +0.30 (+0.38%) | $/barrel |
| Brent Crude Oil | $84.06 | +0.76 (+0.91%) | $/barrel |
| Natural Gas | $2.88 | -0.02 (-0.52%) | $/MMBtu |
| Heating Oil | $3.78 | -0.04 (-1.12%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $30.34 | -0.03 (-0.08%) |
| LyondellBasell | LYB | $58.18 | -0.14 (-0.24%) |
| DuPont | DD | $133.80 | +1.14 (+0.86%) |
| Air Products | APD | $304.00 | +2.04 (+0.68%) |
| Linde | LIN | $525.31 | +1.25 (+0.24%) |
| Eastman Chemical | EMN | $67.34 | +0.13 (+0.19%) |
| Celanese | CE | $47.79 | -0.13 (-0.27%) |
| Huntsman | HUN | $11.73 | +0.12 (+1.08%) |

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
