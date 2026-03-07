# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-03-07)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $90.90 | +9.89 (+12.21%) | $/barrel |
| Brent Crude Oil | $92.69 | +7.28 (+8.52%) | $/barrel |
| Natural Gas | $3.19 | +0.18 (+6.09%) | $/MMBtu |
| Heating Oil | $3.62 | +0.01 (+0.22%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $33.28 | -0.44 (-1.30%) |
| LyondellBasell | LYB | $67.11 | +1.23 (+1.87%) |
| DuPont | DD | $45.26 | -1.46 (-3.13%) |
| Air Products | APD | $272.18 | -4.17 (-1.51%) |
| Linde | LIN | $484.74 | -5.32 (-1.09%) |
| Eastman Chemical | EMN | $70.33 | -1.85 (-2.56%) |
| Celanese | CE | $49.32 | -3.23 (-6.15%) |
| Huntsman | HUN | $11.44 | -1.11 (-8.84%) |

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
