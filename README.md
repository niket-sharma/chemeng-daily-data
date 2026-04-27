# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-04-27)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $96.26 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $101.52 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $2.80 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $3.94 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $37.59 | -1.07 (-2.77%) |
| LyondellBasell | LYB | $70.28 | +0.40 (+0.58%) |
| DuPont | DD | $46.54 | +0.21 (+0.46%) |
| Air Products | APD | $302.58 | +0.82 (+0.27%) |
| Linde | LIN | $509.14 | -1.16 (-0.23%) |
| Eastman Chemical | EMN | $72.14 | +0.14 (+0.20%) |
| Celanese | CE | $64.71 | -0.29 (-0.45%) |
| Huntsman | HUN | $13.60 | -0.02 (-0.15%) |

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
