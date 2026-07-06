# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-07-06)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $68.34 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $71.84 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.23 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $3.29 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $27.15 | -0.56 (-2.02%) |
| LyondellBasell | LYB | $52.59 | -0.77 (-1.44%) |
| DuPont | DD | $140.22 | +0.31 (+0.22%) |
| Air Products | APD | $305.85 | -8.34 (-2.65%) |
| Linde | LIN | $533.69 | -12.95 (-2.37%) |
| Eastman Chemical | EMN | $68.36 | -0.50 (-0.73%) |
| Celanese | CE | $47.22 | -0.47 (-0.98%) |
| Huntsman | HUN | $10.52 | -0.30 (-2.82%) |

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
