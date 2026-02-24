# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-02-24)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $66.52 | +0.21 (+0.32%) | $/barrel |
| Brent Crude Oil | $71.39 | -0.10 (-0.14%) | $/barrel |
| Natural Gas | $2.88 | -0.10 (-3.48%) | $/MMBtu |
| Heating Oil | $2.54 | -0.13 (-5.01%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $30.76 | +0.46 (+1.52%) |
| LyondellBasell | LYB | $58.01 | +1.35 (+2.38%) |
| DuPont | DD | $50.67 | +0.59 (+1.18%) |
| Air Products | APD | $282.76 | -0.49 (-0.17%) |
| Linde | LIN | $495.64 | -2.55 (-0.51%) |
| Eastman Chemical | EMN | $76.94 | +0.37 (+0.48%) |
| Celanese | CE | $53.94 | +1.60 (+3.05%) |
| Huntsman | HUN | $13.09 | +0.60 (+4.80%) |

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
