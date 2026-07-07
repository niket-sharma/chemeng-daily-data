# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-07-07)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $70.48 | +1.93 (+2.82%) | $/barrel |
| Brent Crude Oil | $74.10 | +2.11 (+2.93%) | $/barrel |
| Natural Gas | $3.28 | +0.03 (+0.99%) | $/MMBtu |
| Heating Oil | $3.29 | -0.01 (-0.26%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $27.72 | +0.39 (+1.41%) |
| LyondellBasell | LYB | $53.22 | +0.25 (+0.48%) |
| DuPont | DD | $138.25 | -2.80 (-1.99%) |
| Air Products | APD | $307.64 | -1.22 (-0.39%) |
| Linde | LIN | $536.35 | -4.17 (-0.77%) |
| Eastman Chemical | EMN | $69.29 | +0.39 (+0.57%) |
| Celanese | CE | $47.56 | -0.08 (-0.16%) |
| Huntsman | HUN | $10.76 | +0.18 (+1.70%) |

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
