# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-04-30)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $105.04 | -1.84 (-1.72%) | $/barrel |
| Brent Crude Oil | $109.73 | -8.30 (-7.03%) | $/barrel |
| Natural Gas | $2.67 | +0.02 (+0.91%) | $/MMBtu |
| Heating Oil | $4.07 | -0.13 (-3.07%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $39.89 | +0.34 (+0.86%) |
| LyondellBasell | LYB | $74.26 | +0.97 (+1.33%) |
| DuPont | DD | $45.95 | +1.33 (+2.98%) |
| Air Products | APD | $300.20 | -2.30 (-0.76%) |
| Linde | LIN | $505.86 | +1.15 (+0.23%) |
| Eastman Chemical | EMN | $72.15 | +1.74 (+2.46%) |
| Celanese | CE | $66.66 | +1.57 (+2.41%) |
| Huntsman | HUN | $14.05 | +0.80 (+6.04%) |

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
