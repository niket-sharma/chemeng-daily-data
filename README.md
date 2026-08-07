# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-08-07)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $77.55 | +0.26 (+0.34%) | $/barrel |
| Brent Crude Oil | $82.61 | +0.12 (+0.15%) | $/barrel |
| Natural Gas | $2.68 | +0.04 (+1.70%) | $/MMBtu |
| Heating Oil | $3.88 | -0.00 (-0.10%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $29.69 | -0.60 (-2.00%) |
| LyondellBasell | LYB | $60.22 | -1.22 (-1.99%) |
| DuPont | DD | $144.60 | +0.55 (+0.38%) |
| Air Products | APD | $300.14 | +0.22 (+0.08%) |
| Linde | LIN | $492.04 | +1.93 (+0.39%) |
| Eastman Chemical | EMN | $73.97 | +0.47 (+0.64%) |
| Celanese | CE | $44.62 | +0.67 (+1.52%) |
| Huntsman | HUN | $10.33 | +0.19 (+1.87%) |

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
