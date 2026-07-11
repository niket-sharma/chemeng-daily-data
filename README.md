# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-07-11)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $71.41 | -0.67 (-0.93%) | $/barrel |
| Brent Crude Oil | $76.01 | -0.29 (-0.38%) | $/barrel |
| Natural Gas | $2.94 | -0.07 (-2.39%) | $/MMBtu |
| Heating Oil | $3.55 | -0.02 (-0.51%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $29.03 | +0.53 (+1.86%) |
| LyondellBasell | LYB | $56.35 | +0.96 (+1.73%) |
| DuPont | DD | $134.68 | -0.11 (-0.08%) |
| Air Products | APD | $299.53 | +3.68 (+1.24%) |
| Linde | LIN | $529.79 | +4.23 (+0.80%) |
| Eastman Chemical | EMN | $67.57 | +0.36 (+0.54%) |
| Celanese | CE | $46.92 | +0.28 (+0.60%) |
| Huntsman | HUN | $11.13 | +0.32 (+2.96%) |

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
