# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-11-22)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $83.41 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $89.95 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.75 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $3.85 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $29.03 | -1.22 (-4.03%) |
| LyondellBasell | LYB | $55.84 | -2.35 (-4.04%) |
| DuPont | DD | $145.43 | -4.26 (-2.85%) |
| Air Products | APD | $297.09 | -6.74 (-2.22%) |
| Linde | LIN | $502.83 | -7.38 (-1.45%) |
| Eastman Chemical | EMN | $58.77 | -2.94 (-4.76%) |
| Celanese | CE | $45.01 | -2.39 (-5.04%) |
| Huntsman | HUN | $8.36 | -0.61 (-6.80%) |

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
