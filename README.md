# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-07-13)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $74.93 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $79.77 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $2.90 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $3.66 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $29.92 | +0.89 (+3.07%) |
| LyondellBasell | LYB | $57.75 | +1.40 (+2.48%) |
| DuPont | DD | $133.12 | -1.56 (-1.16%) |
| Air Products | APD | $302.84 | +3.31 (+1.11%) |
| Linde | LIN | $523.63 | -6.16 (-1.16%) |
| Eastman Chemical | EMN | $66.80 | -0.77 (-1.14%) |
| Celanese | CE | $47.21 | +0.29 (+0.62%) |
| Huntsman | HUN | $11.49 | +0.36 (+3.23%) |

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
