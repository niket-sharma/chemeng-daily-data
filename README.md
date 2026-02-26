# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-02-26)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $64.14 | -1.28 (-1.96%) | $/barrel |
| Brent Crude Oil | $69.78 | -1.07 (-1.51%) | $/barrel |
| Natural Gas | $2.81 | -0.16 (-5.42%) | $/MMBtu |
| Heating Oil | $2.49 | -0.18 (-6.91%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $29.68 | -0.34 (-1.13%) |
| LyondellBasell | LYB | $55.36 | -1.39 (-2.45%) |
| DuPont | DD | $50.70 | -0.04 (-0.08%) |
| Air Products | APD | $279.50 | -0.80 (-0.29%) |
| Linde | LIN | $508.17 | -0.10 (-0.02%) |
| Eastman Chemical | EMN | $75.93 | +0.46 (+0.61%) |
| Celanese | CE | $49.19 | -0.84 (-1.68%) |
| Huntsman | HUN | $12.02 | -0.39 (-3.14%) |

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
