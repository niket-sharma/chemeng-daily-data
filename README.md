# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-06-05)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $91.10 | -1.94 (-2.09%) | $/barrel |
| Brent Crude Oil | $93.61 | -1.42 (-1.49%) | $/barrel |
| Natural Gas | $3.25 | -0.08 (-2.46%) | $/MMBtu |
| Heating Oil | $3.61 | -0.06 (-1.70%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $34.23 | -0.56 (-1.61%) |
| LyondellBasell | LYB | $65.55 | -0.63 (-0.95%) |
| DuPont | DD | $47.70 | +0.05 (+0.10%) |
| Air Products | APD | $286.26 | +3.41 (+1.21%) |
| Linde | LIN | $514.71 | +7.26 (+1.43%) |
| Eastman Chemical | EMN | $72.64 | +0.22 (+0.30%) |
| Celanese | CE | $52.74 | -1.23 (-2.28%) |
| Huntsman | HUN | $14.40 | +0.14 (+0.95%) |

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
