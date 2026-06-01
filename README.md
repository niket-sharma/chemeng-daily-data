# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-06-01)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $89.76 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $93.28 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.37 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $3.59 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $33.75 | -0.67 (-1.95%) |
| LyondellBasell | LYB | $66.65 | -1.70 (-2.49%) |
| DuPont | DD | $48.42 | +0.71 (+1.49%) |
| Air Products | APD | $278.62 | -5.03 (-1.77%) |
| Linde | LIN | $497.69 | -4.29 (-0.85%) |
| Eastman Chemical | EMN | $75.87 | -0.49 (-0.64%) |
| Celanese | CE | $53.13 | -0.14 (-0.26%) |
| Huntsman | HUN | $15.35 | -0.12 (-0.78%) |

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
