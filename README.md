# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-07-28)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $79.18 | -3.43 (-4.15%) | $/barrel |
| Brent Crude Oil | $84.36 | -4.00 (-4.53%) | $/barrel |
| Natural Gas | $2.68 | -0.09 (-3.18%) | $/MMBtu |
| Heating Oil | $4.00 | -0.12 (-2.83%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $28.92 | +0.17 (+0.59%) |
| LyondellBasell | LYB | $59.28 | +0.66 (+1.13%) |
| DuPont | DD | $141.78 | +1.82 (+1.30%) |
| Air Products | APD | $294.37 | +1.79 (+0.61%) |
| Linde | LIN | $518.35 | +11.33 (+2.23%) |
| Eastman Chemical | EMN | $68.78 | +1.10 (+1.62%) |
| Celanese | CE | $44.38 | -0.02 (-0.05%) |
| Huntsman | HUN | $11.70 | -0.03 (-0.30%) |

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
