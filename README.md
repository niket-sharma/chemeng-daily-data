# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-04-14)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $96.74 | -2.34 (-2.36%) | $/barrel |
| Brent Crude Oil | $97.71 | -1.65 (-1.66%) | $/barrel |
| Natural Gas | $2.61 | -0.02 (-0.76%) | $/MMBtu |
| Heating Oil | $3.61 | -0.22 (-5.78%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $40.11 | +1.10 (+2.82%) |
| LyondellBasell | LYB | $75.51 | +1.79 (+2.43%) |
| DuPont | DD | $47.15 | -0.10 (-0.21%) |
| Air Products | APD | $298.65 | -0.06 (-0.02%) |
| Linde | LIN | $508.87 | +5.72 (+1.14%) |
| Eastman Chemical | EMN | $74.01 | -0.24 (-0.32%) |
| Celanese | CE | $68.22 | +5.09 (+8.06%) |
| Huntsman | HUN | $14.04 | +0.39 (+2.86%) |

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
