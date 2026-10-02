# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-10-02)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $91.20 | -1.67 (-1.80%) | $/barrel |
| Brent Crude Oil | $102.25 | -0.06 (-0.06%) | $/barrel |
| Natural Gas | $3.04 | +0.07 (+2.36%) | $/MMBtu |
| Heating Oil | $4.51 | -0.13 (-2.79%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $28.02 | +0.43 (+1.58%) |
| LyondellBasell | LYB | $58.67 | +0.90 (+1.55%) |
| DuPont | DD | $130.74 | +1.54 (+1.19%) |
| Air Products | APD | $277.93 | +4.60 (+1.68%) |
| Linde | LIN | $477.99 | +8.54 (+1.82%) |
| Eastman Chemical | EMN | $65.37 | +1.32 (+2.06%) |
| Celanese | CE | $44.56 | +0.36 (+0.83%) |
| Huntsman | HUN | $8.55 | -0.12 (-1.38%) |

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
