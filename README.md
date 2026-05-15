# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-05-15)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $99.76 | -1.41 (-1.39%) | $/barrel |
| Brent Crude Oil | $108.52 | +2.80 (+2.65%) | $/barrel |
| Natural Gas | $2.96 | +0.07 (+2.25%) | $/MMBtu |
| Heating Oil | $4.02 | +0.11 (+2.94%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $39.11 | +0.33 (+0.85%) |
| LyondellBasell | LYB | $75.07 | +1.80 (+2.45%) |
| DuPont | DD | $49.33 | -1.27 (-2.51%) |
| Air Products | APD | $297.18 | -2.68 (-0.90%) |
| Linde | LIN | $508.82 | -2.83 (-0.55%) |
| Eastman Chemical | EMN | $71.98 | -0.49 (-0.68%) |
| Celanese | CE | $56.70 | -0.63 (-1.10%) |
| Huntsman | HUN | $13.96 | -0.35 (-2.45%) |

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
