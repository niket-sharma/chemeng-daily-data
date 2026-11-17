# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-11-17)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $85.54 | -0.18 (-0.21%) | $/barrel |
| Brent Crude Oil | $92.94 | +0.50 (+0.54%) | $/barrel |
| Natural Gas | $3.20 | +0.08 (+2.40%) | $/MMBtu |
| Heating Oil | $3.97 | -0.11 (-2.63%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $31.37 | -0.59 (-1.85%) |
| LyondellBasell | LYB | $60.69 | -0.98 (-1.59%) |
| DuPont | DD | $150.14 | +0.15 (+0.10%) |
| Air Products | APD | $306.92 | -6.98 (-2.22%) |
| Linde | LIN | $515.11 | -8.35 (-1.60%) |
| Eastman Chemical | EMN | $62.30 | -1.19 (-1.87%) |
| Celanese | CE | $48.66 | -0.30 (-0.61%) |
| Huntsman | HUN | $9.19 | -0.11 (-1.18%) |

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
