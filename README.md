# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-10-19)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $98.46 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $109.32 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.04 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $4.73 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $30.01 | +0.08 (+0.27%) |
| LyondellBasell | LYB | $63.73 | -0.28 (-0.44%) |
| DuPont | DD | $129.73 | -0.72 (-0.55%) |
| Air Products | APD | $299.50 | -0.09 (-0.03%) |
| Linde | LIN | $502.58 | +4.15 (+0.83%) |
| Eastman Chemical | EMN | $62.27 | -0.06 (-0.10%) |
| Celanese | CE | $48.05 | +0.56 (+1.18%) |
| Huntsman | HUN | $8.30 | -0.28 (-3.26%) |

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
