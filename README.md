# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-05-29)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $88.90 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $93.71 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.29 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $3.62 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $34.77 | +0.28 (+0.81%) |
| LyondellBasell | LYB | $68.35 | +0.68 (+1.00%) |
| DuPont | DD | $47.71 | +0.05 (+0.10%) |
| Air Products | APD | $283.65 | -2.08 (-0.73%) |
| Linde | LIN | $501.98 | -5.89 (-1.16%) |
| Eastman Chemical | EMN | $76.36 | +0.45 (+0.59%) |
| Celanese | CE | $53.27 | +0.34 (+0.64%) |
| Huntsman | HUN | $15.47 | +0.63 (+4.25%) |

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
