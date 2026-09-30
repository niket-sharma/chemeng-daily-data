# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-09-30)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $90.63 | +1.25 (+1.40%) | $/barrel |
| Brent Crude Oil | $98.27 | -4.32 (-4.21%) | $/barrel |
| Natural Gas | $3.03 | +0.02 (+0.53%) | $/MMBtu |
| Heating Oil | $4.70 | -0.19 (-3.97%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $27.64 | +0.02 (+0.09%) |
| LyondellBasell | LYB | $57.88 | -0.30 (-0.52%) |
| DuPont | DD | $130.59 | +0.47 (+0.36%) |
| Air Products | APD | $281.20 | +2.01 (+0.72%) |
| Linde | LIN | $478.24 | +4.87 (+1.03%) |
| Eastman Chemical | EMN | $65.00 | -0.75 (-1.14%) |
| Celanese | CE | $44.76 | -0.08 (-0.19%) |
| Huntsman | HUN | $8.37 | -0.01 (-0.12%) |

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
