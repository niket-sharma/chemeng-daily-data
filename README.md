# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-05-28)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $92.30 | +3.62 (+4.08%) | $/barrel |
| Brent Crude Oil | $95.68 | +1.39 (+1.47%) | $/barrel |
| Natural Gas | $3.08 | +0.04 (+1.38%) | $/MMBtu |
| Heating Oil | $3.61 | +0.02 (+0.43%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $34.49 | -0.79 (-2.24%) |
| LyondellBasell | LYB | $67.67 | -1.34 (-1.94%) |
| DuPont | DD | $47.66 | -1.80 (-3.64%) |
| Air Products | APD | $285.73 | -3.87 (-1.34%) |
| Linde | LIN | $507.87 | -7.10 (-1.38%) |
| Eastman Chemical | EMN | $75.91 | +1.52 (+2.04%) |
| Celanese | CE | $52.93 | +0.56 (+1.07%) |
| Huntsman | HUN | $14.84 | +0.10 (+0.68%) |

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
