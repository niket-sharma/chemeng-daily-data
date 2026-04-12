# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-04-12)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $96.57 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $95.20 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $2.65 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $3.76 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $39.01 | +0.97 (+2.55%) |
| LyondellBasell | LYB | $73.72 | +1.45 (+2.01%) |
| DuPont | DD | $47.25 | -0.17 (-0.36%) |
| Air Products | APD | $298.71 | +0.97 (+0.33%) |
| Linde | LIN | $503.15 | -0.15 (-0.03%) |
| Eastman Chemical | EMN | $74.25 | +1.54 (+2.12%) |
| Celanese | CE | $63.13 | +0.82 (+1.32%) |
| Huntsman | HUN | $13.65 | +0.13 (+0.96%) |

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
