# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-04-17)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $81.24 | -13.45 (-14.20%) | $/barrel |
| Brent Crude Oil | $88.29 | -11.10 (-11.17%) | $/barrel |
| Natural Gas | $2.65 | +0.01 (+0.23%) | $/MMBtu |
| Heating Oil | $3.22 | -0.61 (-16.03%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $35.71 | -4.21 (-10.55%) |
| LyondellBasell | LYB | $67.05 | -8.24 (-10.94%) |
| DuPont | DD | $47.62 | +0.87 (+1.86%) |
| Air Products | APD | $292.18 | -5.06 (-1.70%) |
| Linde | LIN | $492.35 | -6.87 (-1.38%) |
| Eastman Chemical | EMN | $74.10 | +0.75 (+1.02%) |
| Celanese | CE | $64.25 | -4.09 (-5.99%) |
| Huntsman | HUN | $13.44 | -0.30 (-2.15%) |

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
