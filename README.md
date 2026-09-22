# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-09-22)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $90.94 | -4.84 (-5.05%) | $/barrel |
| Brent Crude Oil | $99.79 | -0.55 (-0.55%) | $/barrel |
| Natural Gas | $3.11 | +0.28 (+9.80%) | $/MMBtu |
| Heating Oil | $4.75 | -0.14 (-2.87%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $28.39 | +0.11 (+0.41%) |
| LyondellBasell | LYB | $60.44 | +0.20 (+0.33%) |
| DuPont | DD | $131.72 | +1.93 (+1.49%) |
| Air Products | APD | $287.54 | +8.08 (+2.89%) |
| Linde | LIN | $464.46 | +6.96 (+1.52%) |
| Eastman Chemical | EMN | $67.05 | +1.96 (+3.01%) |
| Celanese | CE | $47.89 | +3.51 (+7.91%) |
| Huntsman | HUN | $9.10 | +0.24 (+2.71%) |

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
