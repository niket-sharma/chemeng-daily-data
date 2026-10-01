# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-10-01)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $88.83 | -1.59 (-1.76%) | $/barrel |
| Brent Crude Oil | $96.57 | -6.96 (-6.72%) | $/barrel |
| Natural Gas | $2.98 | -0.05 (-1.65%) | $/MMBtu |
| Heating Oil | $4.61 | -0.35 (-7.03%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $27.54 | -0.07 (-0.25%) |
| LyondellBasell | LYB | $57.47 | -0.71 (-1.22%) |
| DuPont | DD | $129.89 | -0.23 (-0.18%) |
| Air Products | APD | $278.23 | -0.96 (-0.34%) |
| Linde | LIN | $474.65 | +1.28 (+0.27%) |
| Eastman Chemical | EMN | $64.84 | -0.91 (-1.38%) |
| Celanese | CE | $44.37 | -0.47 (-1.05%) |
| Huntsman | HUN | $8.40 | +0.02 (+0.24%) |

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
