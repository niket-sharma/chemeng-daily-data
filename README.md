# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-04-23)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $93.31 | +0.35 (+0.38%) | $/barrel |
| Brent Crude Oil | $102.67 | +0.76 (+0.75%) | $/barrel |
| Natural Gas | $2.77 | +0.05 (+1.65%) | $/MMBtu |
| Heating Oil | $3.80 | -0.14 (-3.58%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $37.20 | -1.61 (-4.15%) |
| LyondellBasell | LYB | $70.21 | -1.79 (-2.48%) |
| DuPont | DD | $46.42 | +0.44 (+0.96%) |
| Air Products | APD | $302.08 | +5.32 (+1.79%) |
| Linde | LIN | $502.10 | +7.48 (+1.51%) |
| Eastman Chemical | EMN | $72.17 | -0.36 (-0.50%) |
| Celanese | CE | $64.69 | -0.79 (-1.21%) |
| Huntsman | HUN | $13.62 | -0.24 (-1.73%) |

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
