# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-06-23)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $73.73 | -1.09 (-1.46%) | $/barrel |
| Brent Crude Oil | $77.62 | -0.28 (-0.36%) | $/barrel |
| Natural Gas | $3.27 | +0.01 (+0.40%) | $/MMBtu |
| Heating Oil | $3.06 | -0.04 (-1.22%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $30.79 | -0.94 (-2.96%) |
| LyondellBasell | LYB | $58.52 | -1.55 (-2.58%) |
| DuPont | DD | $48.19 | +0.48 (+1.01%) |
| Air Products | APD | $283.11 | +2.90 (+1.03%) |
| Linde | LIN | $516.71 | +4.56 (+0.89%) |
| Eastman Chemical | EMN | $71.96 | -0.53 (-0.73%) |
| Celanese | CE | $49.73 | -1.43 (-2.80%) |
| Huntsman | HUN | $11.50 | -0.57 (-4.72%) |

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
