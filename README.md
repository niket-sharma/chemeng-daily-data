# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-01-24)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $61.07 | +1.71 (+2.88%) | $/barrel |
| Brent Crude Oil | $65.88 | +1.82 (+2.84%) | $/barrel |
| Natural Gas | $5.28 | +0.23 (+4.56%) | $/MMBtu |
| Heating Oil | $2.43 | +0.06 (+2.61%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $28.25 | -0.08 (-0.28%) |
| LyondellBasell | LYB | $50.99 | -0.55 (-1.07%) |
| DuPont | DD | $44.14 | +0.35 (+0.80%) |
| Air Products | APD | $261.35 | -2.69 (-1.02%) |
| Linde | LIN | $451.57 | +5.93 (+1.33%) |
| Eastman Chemical | EMN | $68.71 | -0.24 (-0.35%) |
| Celanese | CE | $47.52 | -0.46 (-0.96%) |
| Huntsman | HUN | $11.85 | -0.28 (-2.31%) |

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
