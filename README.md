# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-03-24)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $91.64 | +3.51 (+3.98%) | $/barrel |
| Brent Crude Oil | $102.99 | +3.05 (+3.05%) | $/barrel |
| Natural Gas | $2.89 | +0.00 (+0.07%) | $/MMBtu |
| Heating Oil | $4.01 | -0.05 (-1.25%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $37.39 | +1.35 (+3.75%) |
| LyondellBasell | LYB | $74.70 | +3.23 (+4.52%) |
| DuPont | DD | $44.66 | +0.52 (+1.18%) |
| Air Products | APD | $284.40 | +5.74 (+2.06%) |
| Linde | LIN | $482.64 | +4.59 (+0.96%) |
| Eastman Chemical | EMN | $68.99 | +0.98 (+1.44%) |
| Celanese | CE | $58.69 | +2.56 (+4.56%) |
| Huntsman | HUN | $11.11 | +0.28 (+2.59%) |

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
