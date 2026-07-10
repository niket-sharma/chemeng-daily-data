# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-07-10)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $71.19 | -0.89 (-1.23%) | $/barrel |
| Brent Crude Oil | $75.66 | -0.64 (-0.84%) | $/barrel |
| Natural Gas | $2.90 | -0.11 (-3.59%) | $/MMBtu |
| Heating Oil | $3.54 | -0.03 (-0.80%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $28.78 | +0.28 (+1.00%) |
| LyondellBasell | LYB | $55.68 | +0.29 (+0.52%) |
| DuPont | DD | $135.77 | +0.98 (+0.73%) |
| Air Products | APD | $299.30 | +3.45 (+1.17%) |
| Linde | LIN | $531.67 | +6.11 (+1.16%) |
| Eastman Chemical | EMN | $67.77 | +0.56 (+0.83%) |
| Celanese | CE | $46.72 | +0.08 (+0.17%) |
| Huntsman | HUN | $10.90 | +0.09 (+0.79%) |

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
