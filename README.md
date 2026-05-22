# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-05-22)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $97.31 | +0.96 (+1.00%) | $/barrel |
| Brent Crude Oil | $104.07 | +1.49 (+1.45%) | $/barrel |
| Natural Gas | $3.14 | +0.12 (+3.91%) | $/MMBtu |
| Heating Oil | $3.75 | -0.08 (-2.10%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $35.91 | -0.36 (-0.99%) |
| LyondellBasell | LYB | $70.08 | -1.22 (-1.71%) |
| DuPont | DD | $47.15 | -0.10 (-0.21%) |
| Air Products | APD | $290.19 | +1.00 (+0.35%) |
| Linde | LIN | $514.51 | +7.88 (+1.56%) |
| Eastman Chemical | EMN | $73.19 | +2.54 (+3.60%) |
| Celanese | CE | $52.90 | -0.60 (-1.12%) |
| Huntsman | HUN | $14.38 | +0.32 (+2.28%) |

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
