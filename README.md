# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-10-22)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $99.41 | +2.26 (+2.33%) | $/barrel |
| Brent Crude Oil | $112.98 | +4.16 (+3.82%) | $/barrel |
| Natural Gas | $2.82 | +0.03 (+1.08%) | $/MMBtu |
| Heating Oil | $4.72 | -0.04 (-0.86%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $31.27 | +0.90 (+2.95%) |
| LyondellBasell | LYB | $65.03 | +1.76 (+2.78%) |
| DuPont | DD | $133.67 | -0.48 (-0.36%) |
| Air Products | APD | $307.86 | +5.20 (+1.72%) |
| Linde | LIN | $509.98 | +9.41 (+1.88%) |
| Eastman Chemical | EMN | $64.83 | +1.33 (+2.09%) |
| Celanese | CE | $47.05 | -0.22 (-0.47%) |
| Huntsman | HUN | $8.40 | +0.17 (+2.00%) |

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
