# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-03-06)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $79.90 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $84.42 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $2.98 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $2.90 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $33.72 | +1.38 (+4.27%) |
| LyondellBasell | LYB | $65.88 | +3.96 (+6.40%) |
| DuPont | DD | $46.72 | -1.36 (-2.83%) |
| Air Products | APD | $276.35 | +2.15 (+0.78%) |
| Linde | LIN | $490.06 | -9.13 (-1.83%) |
| Eastman Chemical | EMN | $72.18 | -1.27 (-1.73%) |
| Celanese | CE | $52.55 | +1.40 (+2.74%) |
| Huntsman | HUN | $12.55 | -0.34 (-2.64%) |

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
