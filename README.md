# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-03-10)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $87.99 | -6.78 (-7.15%) | $/barrel |
| Brent Crude Oil | $87.41 | -11.55 (-11.67%) | $/barrel |
| Natural Gas | $3.05 | -0.07 (-2.18%) | $/MMBtu |
| Heating Oil | $3.01 | -0.58 (-16.12%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $34.95 | +0.64 (+1.87%) |
| LyondellBasell | LYB | $67.01 | +0.19 (+0.28%) |
| DuPont | DD | $45.68 | +0.44 (+0.97%) |
| Air Products | APD | $273.11 | -1.29 (-0.47%) |
| Linde | LIN | $476.36 | -7.26 (-1.50%) |
| Eastman Chemical | EMN | $70.13 | +0.53 (+0.76%) |
| Celanese | CE | $50.99 | -0.46 (-0.89%) |
| Huntsman | HUN | $12.04 | -0.07 (-0.58%) |

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
