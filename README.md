# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-09-03)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $91.87 | +0.86 (+0.94%) | $/barrel |
| Brent Crude Oil | $96.00 | +0.37 (+0.39%) | $/barrel |
| Natural Gas | $2.96 | +0.00 (+0.14%) | $/MMBtu |
| Heating Oil | $4.63 | -0.05 (-1.06%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $30.67 | -0.61 (-1.93%) |
| LyondellBasell | LYB | $65.14 | -1.43 (-2.15%) |
| DuPont | DD | $131.29 | -1.63 (-1.23%) |
| Air Products | APD | $305.07 | -4.38 (-1.42%) |
| Linde | LIN | $483.22 | -4.23 (-0.87%) |
| Eastman Chemical | EMN | $71.09 | -1.07 (-1.48%) |
| Celanese | CE | $45.75 | -0.91 (-1.95%) |
| Huntsman | HUN | $9.44 | -0.27 (-2.73%) |

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
