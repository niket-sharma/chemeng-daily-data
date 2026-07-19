# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-07-19)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $81.78 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $88.10 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $2.91 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $3.94 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $29.92 | +0.62 (+2.12%) |
| LyondellBasell | LYB | $59.17 | +1.37 (+2.37%) |
| DuPont | DD | $135.29 | +1.00 (+0.74%) |
| Air Products | APD | $295.62 | -1.67 (-0.56%) |
| Linde | LIN | $513.22 | -7.52 (-1.44%) |
| Eastman Chemical | EMN | $68.60 | -0.56 (-0.81%) |
| Celanese | CE | $45.70 | -0.08 (-0.17%) |
| Huntsman | HUN | $11.79 | -0.07 (-0.59%) |

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
