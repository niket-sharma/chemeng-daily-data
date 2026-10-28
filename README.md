# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-10-28)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $102.97 | +3.07 (+3.07%) | $/barrel |
| Brent Crude Oil | $111.81 | -2.07 (-1.82%) | $/barrel |
| Natural Gas | $3.02 | +0.33 (+12.12%) | $/MMBtu |
| Heating Oil | $4.67 | -0.10 (-2.14%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $33.76 | -0.01 (-0.04%) |
| LyondellBasell | LYB | $66.93 | -0.50 (-0.74%) |
| DuPont | DD | $137.89 | +0.22 (+0.16%) |
| Air Products | APD | $306.08 | -1.03 (-0.34%) |
| Linde | LIN | $505.53 | -3.12 (-0.61%) |
| Eastman Chemical | EMN | $66.09 | -0.03 (-0.05%) |
| Celanese | CE | $48.26 | -0.37 (-0.76%) |
| Huntsman | HUN | $8.95 | -0.16 (-1.81%) |

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
