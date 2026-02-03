# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-02-03)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $62.72 | +0.58 (+0.93%) | $/barrel |
| Brent Crude Oil | $66.76 | +0.46 (+0.69%) | $/barrel |
| Natural Gas | $3.27 | +0.03 (+1.02%) | $/MMBtu |
| Heating Oil | $2.40 | +0.04 (+1.66%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $29.50 | +0.62 (+2.15%) |
| LyondellBasell | LYB | $50.84 | +0.59 (+1.17%) |
| DuPont | DD | $44.87 | +0.44 (+0.98%) |
| Air Products | APD | $274.82 | +3.83 (+1.41%) |
| Linde | LIN | $462.01 | +1.85 (+0.40%) |
| Eastman Chemical | EMN | $72.17 | +0.69 (+0.97%) |
| Celanese | CE | $45.99 | +0.12 (+0.26%) |
| Huntsman | HUN | $11.78 | +0.30 (+2.61%) |

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
