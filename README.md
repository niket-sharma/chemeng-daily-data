# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-07-17)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $80.52 | +1.57 (+1.99%) | $/barrel |
| Brent Crude Oil | $86.57 | +2.34 (+2.78%) | $/barrel |
| Natural Gas | $2.89 | +0.04 (+1.26%) | $/MMBtu |
| Heating Oil | $3.95 | -0.08 (-1.99%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $30.08 | +0.78 (+2.65%) |
| LyondellBasell | LYB | $59.24 | +1.44 (+2.48%) |
| DuPont | DD | $135.24 | +0.95 (+0.71%) |
| Air Products | APD | $301.39 | +4.10 (+1.38%) |
| Linde | LIN | $522.24 | +1.50 (+0.29%) |
| Eastman Chemical | EMN | $69.57 | +0.41 (+0.60%) |
| Celanese | CE | $45.52 | -0.26 (-0.57%) |
| Huntsman | HUN | $11.96 | +0.10 (+0.84%) |

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
