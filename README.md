# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-10-29)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $102.20 | -0.58 (-0.56%) | $/barrel |
| Brent Crude Oil | $110.93 | -4.39 (-3.81%) | $/barrel |
| Natural Gas | $2.93 | +0.11 (+3.90%) | $/MMBtu |
| Heating Oil | $4.57 | -0.24 (-5.04%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $33.49 | -0.64 (-1.86%) |
| LyondellBasell | LYB | $65.27 | -1.86 (-2.77%) |
| DuPont | DD | $140.35 | +1.67 (+1.20%) |
| Air Products | APD | $310.23 | +3.03 (+0.99%) |
| Linde | LIN | $502.68 | -5.48 (-1.08%) |
| Eastman Chemical | EMN | $67.73 | +1.06 (+1.59%) |
| Celanese | CE | $47.91 | -0.94 (-1.92%) |
| Huntsman | HUN | $8.95 | -0.16 (-1.76%) |

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
