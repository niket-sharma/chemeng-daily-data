# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-05-28)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $89.60 | +0.92 (+1.04%) | $/barrel |
| Brent Crude Oil | $93.40 | -0.89 (-0.94%) | $/barrel |
| Natural Gas | $3.22 | +0.18 (+6.02%) | $/MMBtu |
| Heating Oil | $3.53 | -0.07 (-1.88%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $34.82 | +0.33 (+0.96%) |
| LyondellBasell | LYB | $68.82 | +1.15 (+1.70%) |
| DuPont | DD | $47.36 | -0.30 (-0.63%) |
| Air Products | APD | $283.66 | -2.07 (-0.72%) |
| Linde | LIN | $501.58 | -6.29 (-1.24%) |
| Eastman Chemical | EMN | $76.28 | +0.36 (+0.48%) |
| Celanese | CE | $53.53 | +0.60 (+1.13%) |
| Huntsman | HUN | $15.23 | +0.39 (+2.59%) |

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
