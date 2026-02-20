# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-02-20)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $66.03 | -0.40 (-0.60%) | $/barrel |
| Brent Crude Oil | $70.90 | -0.76 (-1.06%) | $/barrel |
| Natural Gas | $2.96 | -0.04 (-1.20%) | $/MMBtu |
| Heating Oil | $2.51 | -0.10 (-3.94%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $30.59 | -0.80 (-2.55%) |
| LyondellBasell | LYB | $54.72 | -0.61 (-1.10%) |
| DuPont | DD | $49.92 | -0.32 (-0.64%) |
| Air Products | APD | $279.82 | -0.90 (-0.32%) |
| Linde | LIN | $490.55 | +0.44 (+0.09%) |
| Eastman Chemical | EMN | $77.50 | -0.52 (-0.67%) |
| Celanese | CE | $54.44 | -0.48 (-0.87%) |
| Huntsman | HUN | $12.43 | -0.26 (-2.05%) |

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
