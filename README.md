# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-11-18)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $82.13 | -3.88 (-4.51%) | $/barrel |
| Brent Crude Oil | $88.95 | -4.19 (-4.50%) | $/barrel |
| Natural Gas | $3.40 | +0.19 (+5.92%) | $/MMBtu |
| Heating Oil | $3.88 | -0.17 (-4.20%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $30.37 | -1.00 (-3.19%) |
| LyondellBasell | LYB | $58.46 | -2.23 (-3.67%) |
| DuPont | DD | $150.23 | +0.09 (+0.06%) |
| Air Products | APD | $308.11 | +1.19 (+0.39%) |
| Linde | LIN | $512.16 | -2.95 (-0.57%) |
| Eastman Chemical | EMN | $62.36 | +0.06 (+0.10%) |
| Celanese | CE | $48.21 | -0.45 (-0.92%) |
| Huntsman | HUN | $9.03 | -0.16 (-1.74%) |

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
