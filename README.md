# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-05-05)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $104.15 | -2.27 (-2.13%) | $/barrel |
| Brent Crude Oil | $113.05 | -1.39 (-1.21%) | $/barrel |
| Natural Gas | $2.84 | -0.03 (-0.87%) | $/MMBtu |
| Heating Oil | $4.01 | -0.06 (-1.45%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $40.58 | +0.29 (+0.72%) |
| LyondellBasell | LYB | $76.04 | +1.05 (+1.40%) |
| DuPont | DD | $45.41 | -0.83 (-1.79%) |
| Air Products | APD | $298.35 | -2.72 (-0.90%) |
| Linde | LIN | $493.55 | -14.37 (-2.83%) |
| Eastman Chemical | EMN | $76.72 | -0.81 (-1.04%) |
| Celanese | CE | $68.74 | -0.50 (-0.72%) |
| Huntsman | HUN | $14.22 | -0.41 (-2.80%) |

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
