# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-11-13)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $88.85 | +0.11 (+0.12%) | $/barrel |
| Brent Crude Oil | $96.09 | +0.27 (+0.28%) | $/barrel |
| Natural Gas | $3.24 | -0.10 (-2.99%) | $/MMBtu |
| Heating Oil | $4.28 | -0.00 (-0.04%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $32.99 | -0.17 (-0.50%) |
| LyondellBasell | LYB | $64.15 | +0.27 (+0.42%) |
| DuPont | DD | $153.66 | -1.04 (-0.67%) |
| Air Products | APD | $316.08 | -0.12 (-0.04%) |
| Linde | LIN | $525.01 | +2.52 (+0.48%) |
| Eastman Chemical | EMN | $65.02 | -0.59 (-0.90%) |
| Celanese | CE | $51.14 | -0.12 (-0.23%) |
| Huntsman | HUN | $9.48 | -0.18 (-1.81%) |

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
