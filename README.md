# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-08-05)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $75.28 | -0.49 (-0.65%) | $/barrel |
| Brent Crude Oil | $79.12 | -0.24 (-0.30%) | $/barrel |
| Natural Gas | $2.67 | -0.01 (-0.52%) | $/MMBtu |
| Heating Oil | $3.84 | +0.07 (+1.78%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $29.28 | -1.05 (-3.45%) |
| LyondellBasell | LYB | $59.35 | -1.76 (-2.88%) |
| DuPont | DD | $145.87 | +2.94 (+2.05%) |
| Air Products | APD | $295.00 | +0.29 (+0.10%) |
| Linde | LIN | $490.18 | +5.54 (+1.14%) |
| Eastman Chemical | EMN | $72.86 | -1.04 (-1.40%) |
| Celanese | CE | $41.22 | -4.02 (-8.89%) |
| Huntsman | HUN | $10.18 | -0.25 (-2.41%) |

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
