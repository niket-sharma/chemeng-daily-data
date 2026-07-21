# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-07-21)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $84.17 | +0.94 (+1.13%) | $/barrel |
| Brent Crude Oil | $91.02 | +1.80 (+2.02%) | $/barrel |
| Natural Gas | $2.87 | +0.01 (+0.24%) | $/MMBtu |
| Heating Oil | $4.01 | -0.11 (-2.71%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $31.06 | +0.68 (+2.26%) |
| LyondellBasell | LYB | $61.99 | +1.26 (+2.07%) |
| DuPont | DD | $138.58 | +2.83 (+2.08%) |
| Air Products | APD | $298.62 | +1.99 (+0.67%) |
| Linde | LIN | $507.02 | -5.02 (-0.98%) |
| Eastman Chemical | EMN | $69.16 | +1.08 (+1.59%) |
| Celanese | CE | $46.51 | +1.95 (+4.39%) |
| Huntsman | HUN | $12.35 | +0.36 (+3.04%) |

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
