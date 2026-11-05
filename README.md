# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-11-05)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $90.80 | +2.68 (+3.04%) | $/barrel |
| Brent Crude Oil | $98.47 | +3.85 (+4.07%) | $/barrel |
| Natural Gas | $2.95 | -0.01 (-0.44%) | $/MMBtu |
| Heating Oil | $4.35 | +0.15 (+3.47%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $32.15 | -0.56 (-1.70%) |
| LyondellBasell | LYB | $61.83 | -1.13 (-1.79%) |
| DuPont | DD | $145.13 | -5.60 (-3.72%) |
| Air Products | APD | $312.15 | -6.72 (-2.11%) |
| Linde | LIN | $520.35 | -4.39 (-0.84%) |
| Eastman Chemical | EMN | $65.62 | -1.99 (-2.94%) |
| Celanese | CE | $48.10 | -1.65 (-3.31%) |
| Huntsman | HUN | $9.80 | -0.15 (-1.56%) |

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
