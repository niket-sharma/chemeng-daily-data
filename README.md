# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-05-14)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $101.38 | +0.36 (+0.36%) | $/barrel |
| Brent Crude Oil | $105.63 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $2.84 | -0.02 (-0.84%) | $/MMBtu |
| Heating Oil | $3.92 | -0.05 (-1.30%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $38.75 | -0.09 (-0.23%) |
| LyondellBasell | LYB | $73.28 | -0.46 (-0.62%) |
| DuPont | DD | $50.33 | -0.83 (-1.61%) |
| Air Products | APD | $301.94 | -4.26 (-1.39%) |
| Linde | LIN | $510.42 | -2.85 (-0.55%) |
| Eastman Chemical | EMN | $73.24 | -0.59 (-0.80%) |
| Celanese | CE | $58.99 | -0.98 (-1.63%) |
| Huntsman | HUN | $14.46 | +0.07 (+0.49%) |

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
