# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-09-12)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $100.05 | -2.43 (-2.37%) | $/barrel |
| Brent Crude Oil | $104.61 | -3.02 (-2.81%) | $/barrel |
| Natural Gas | $2.83 | -0.00 (-0.11%) | $/MMBtu |
| Heating Oil | $4.96 | -0.10 (-1.94%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $29.03 | -0.61 (-2.06%) |
| LyondellBasell | LYB | $63.69 | -0.61 (-0.95%) |
| DuPont | DD | $126.99 | -0.33 (-0.26%) |
| Air Products | APD | $291.43 | -2.22 (-0.76%) |
| Linde | LIN | $466.22 | +4.60 (+1.00%) |
| Eastman Chemical | EMN | $68.11 | -0.27 (-0.39%) |
| Celanese | CE | $46.09 | +0.37 (+0.81%) |
| Huntsman | HUN | $9.54 | +0.01 (+0.10%) |

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
