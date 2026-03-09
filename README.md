# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-03-09)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $103.71 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $105.09 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.29 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $3.25 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $34.70 | +1.42 (+4.27%) |
| LyondellBasell | LYB | $67.47 | +0.36 (+0.54%) |
| DuPont | DD | $43.16 | -2.10 (-4.64%) |
| Air Products | APD | $272.90 | +0.72 (+0.26%) |
| Linde | LIN | $480.80 | -3.94 (-0.81%) |
| Eastman Chemical | EMN | $67.11 | -3.22 (-4.58%) |
| Celanese | CE | $47.97 | -1.35 (-2.73%) |
| Huntsman | HUN | $11.25 | -0.19 (-1.66%) |

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
