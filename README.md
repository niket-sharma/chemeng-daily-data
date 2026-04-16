# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-04-16)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $90.51 | -0.78 (-0.85%) | $/barrel |
| Brent Crude Oil | $98.01 | +3.08 (+3.24%) | $/barrel |
| Natural Gas | $2.64 | +0.04 (+1.34%) | $/MMBtu |
| Heating Oil | $3.68 | -0.08 (-2.05%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $39.25 | +0.41 (+1.06%) |
| LyondellBasell | LYB | $73.85 | +0.72 (+0.98%) |
| DuPont | DD | $46.04 | -0.02 (-0.04%) |
| Air Products | APD | $296.74 | +1.53 (+0.52%) |
| Linde | LIN | $499.67 | +1.73 (+0.35%) |
| Eastman Chemical | EMN | $72.61 | -0.14 (-0.19%) |
| Celanese | CE | $66.31 | +1.58 (+2.44%) |
| Huntsman | HUN | $13.41 | -0.18 (-1.32%) |

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
