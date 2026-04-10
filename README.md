# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-04-10)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $98.27 | +0.40 (+0.41%) | $/barrel |
| Brent Crude Oil | $96.08 | +0.16 (+0.17%) | $/barrel |
| Natural Gas | $2.65 | -0.02 (-0.64%) | $/MMBtu |
| Heating Oil | $3.85 | -0.09 (-2.24%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $38.40 | +0.36 (+0.95%) |
| LyondellBasell | LYB | $73.13 | +0.86 (+1.19%) |
| DuPont | DD | $47.56 | +0.14 (+0.30%) |
| Air Products | APD | $298.58 | +0.84 (+0.28%) |
| Linde | LIN | $503.10 | -0.20 (-0.04%) |
| Eastman Chemical | EMN | $74.25 | +1.54 (+2.11%) |
| Celanese | CE | $63.12 | +0.81 (+1.29%) |
| Huntsman | HUN | $13.65 | +0.13 (+0.96%) |

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
