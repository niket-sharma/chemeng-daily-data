# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-09-29)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $89.51 | -3.09 (-3.34%) | $/barrel |
| Brent Crude Oil | $96.32 | -8.96 (-8.51%) | $/barrel |
| Natural Gas | $3.02 | +0.02 (+0.63%) | $/MMBtu |
| Heating Oil | $4.53 | -0.22 (-4.69%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $27.51 | -0.38 (-1.36%) |
| LyondellBasell | LYB | $58.00 | -0.27 (-0.46%) |
| DuPont | DD | $129.87 | -1.11 (-0.85%) |
| Air Products | APD | $278.83 | +0.08 (+0.03%) |
| Linde | LIN | $473.30 | +1.26 (+0.27%) |
| Eastman Chemical | EMN | $65.87 | -0.60 (-0.90%) |
| Celanese | CE | $44.71 | -1.21 (-2.64%) |
| Huntsman | HUN | $8.38 | -0.26 (-2.95%) |

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
