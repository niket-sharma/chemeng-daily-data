# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-02-06)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $62.71 | -0.58 (-0.92%) | $/barrel |
| Brent Crude Oil | $67.04 | -0.51 (-0.75%) | $/barrel |
| Natural Gas | $3.54 | +0.03 (+0.85%) | $/MMBtu |
| Heating Oil | $2.37 | -0.02 (-0.89%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $31.09 | +0.49 (+1.60%) |
| LyondellBasell | LYB | $54.64 | +0.76 (+1.41%) |
| DuPont | DD | $45.97 | +0.29 (+0.63%) |
| Air Products | APD | $283.73 | +0.23 (+0.08%) |
| Linde | LIN | $453.86 | -5.83 (-1.27%) |
| Eastman Chemical | EMN | $76.61 | +0.53 (+0.70%) |
| Celanese | CE | $53.08 | +1.02 (+1.96%) |
| Huntsman | HUN | $13.22 | +0.02 (+0.11%) |

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
