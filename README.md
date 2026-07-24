# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-07-24)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $89.77 | -2.42 (-2.63%) | $/barrel |
| Brent Crude Oil | $97.23 | -3.46 (-3.44%) | $/barrel |
| Natural Gas | $2.95 | +0.04 (+1.27%) | $/MMBtu |
| Heating Oil | $4.11 | -0.23 (-5.34%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $29.46 | -1.44 (-4.66%) |
| LyondellBasell | LYB | $60.97 | -0.75 (-1.21%) |
| DuPont | DD | $137.51 | +0.11 (+0.08%) |
| Air Products | APD | $296.13 | +1.84 (+0.63%) |
| Linde | LIN | $509.66 | +3.34 (+0.66%) |
| Eastman Chemical | EMN | $68.24 | +0.32 (+0.46%) |
| Celanese | CE | $47.10 | -0.25 (-0.53%) |
| Huntsman | HUN | $12.62 | -0.19 (-1.48%) |

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
