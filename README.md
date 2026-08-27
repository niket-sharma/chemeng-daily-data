# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-08-27)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $83.58 | +1.35 (+1.64%) | $/barrel |
| Brent Crude Oil | $88.63 | +0.79 (+0.90%) | $/barrel |
| Natural Gas | $2.90 | +0.06 (+2.11%) | $/MMBtu |
| Heating Oil | $4.18 | -0.08 (-1.87%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $30.33 | +0.00 (+0.00%) |
| LyondellBasell | LYB | $63.06 | +0.44 (+0.70%) |
| DuPont | DD | $138.80 | +0.82 (+0.59%) |
| Air Products | APD | $305.47 | -1.19 (-0.39%) |
| Linde | LIN | $485.35 | -4.98 (-1.02%) |
| Eastman Chemical | EMN | $72.65 | -0.28 (-0.38%) |
| Celanese | CE | $44.87 | +0.17 (+0.38%) |
| Huntsman | HUN | $9.65 | +0.02 (+0.21%) |

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
