# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-04-21)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $87.65 | -1.96 (-2.19%) | $/barrel |
| Brent Crude Oil | $91.18 | -4.30 (-4.50%) | $/barrel |
| Natural Gas | $2.68 | -0.01 (-0.30%) | $/MMBtu |
| Heating Oil | $3.52 | -0.02 (-0.58%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $37.21 | +0.44 (+1.20%) |
| LyondellBasell | LYB | $69.18 | +0.60 (+0.87%) |
| DuPont | DD | $47.04 | +0.04 (+0.09%) |
| Air Products | APD | $296.76 | +0.61 (+0.21%) |
| Linde | LIN | $496.52 | -1.63 (-0.33%) |
| Eastman Chemical | EMN | $73.79 | +0.15 (+0.20%) |
| Celanese | CE | $64.26 | +0.69 (+1.09%) |
| Huntsman | HUN | $13.78 | +0.13 (+0.95%) |

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
