# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-10-09)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $91.16 | -0.33 (-0.36%) | $/barrel |
| Brent Crude Oil | $103.99 | -0.29 (-0.28%) | $/barrel |
| Natural Gas | $3.20 | +0.04 (+1.10%) | $/MMBtu |
| Heating Oil | $4.67 | -0.21 (-4.29%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $28.61 | +0.02 (+0.07%) |
| LyondellBasell | LYB | $60.42 | +0.08 (+0.14%) |
| DuPont | DD | $130.24 | -2.24 (-1.69%) |
| Air Products | APD | $281.39 | +3.01 (+1.08%) |
| Linde | LIN | $484.90 | +3.20 (+0.67%) |
| Eastman Chemical | EMN | $62.80 | -0.96 (-1.51%) |
| Celanese | CE | $44.77 | -0.04 (-0.09%) |
| Huntsman | HUN | $8.17 | -0.33 (-3.88%) |

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
