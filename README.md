# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-07-31)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $85.01 | +1.42 (+1.70%) | $/barrel |
| Brent Crude Oil | $90.03 | +1.00 (+1.12%) | $/barrel |
| Natural Gas | $2.72 | -0.04 (-1.49%) | $/MMBtu |
| Heating Oil | $4.17 | -0.04 (-0.87%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $29.83 | -0.26 (-0.85%) |
| LyondellBasell | LYB | $61.37 | +0.93 (+1.53%) |
| DuPont | DD | $137.65 | -1.19 (-0.86%) |
| Air Products | APD | $292.70 | -7.51 (-2.50%) |
| Linde | LIN | $478.95 | -29.69 (-5.84%) |
| Eastman Chemical | EMN | $68.51 | -1.56 (-2.22%) |
| Celanese | CE | $43.26 | -1.55 (-3.46%) |
| Huntsman | HUN | $9.73 | -2.34 (-19.43%) |

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
