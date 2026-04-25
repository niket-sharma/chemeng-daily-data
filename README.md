# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-04-25)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $94.40 | -1.45 (-1.51%) | $/barrel |
| Brent Crude Oil | $105.33 | +0.26 (+0.25%) | $/barrel |
| Natural Gas | $2.52 | -0.09 (-3.48%) | $/MMBtu |
| Heating Oil | $3.89 | -0.10 (-2.53%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $38.66 | +0.13 (+0.34%) |
| LyondellBasell | LYB | $69.87 | -0.85 (-1.20%) |
| DuPont | DD | $46.33 | -0.04 (-0.09%) |
| Air Products | APD | $301.76 | -1.89 (-0.62%) |
| Linde | LIN | $510.30 | +2.24 (+0.44%) |
| Eastman Chemical | EMN | $72.00 | +0.08 (+0.11%) |
| Celanese | CE | $65.00 | -0.23 (-0.35%) |
| Huntsman | HUN | $13.62 | +0.07 (+0.52%) |

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
