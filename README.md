# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-06-12)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $86.51 | -1.20 (-1.37%) | $/barrel |
| Brent Crude Oil | $89.25 | -1.13 (-1.25%) | $/barrel |
| Natural Gas | $3.12 | +0.03 (+1.10%) | $/MMBtu |
| Heating Oil | $3.42 | -0.09 (-2.66%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $33.94 | +0.31 (+0.92%) |
| LyondellBasell | LYB | $64.55 | +1.08 (+1.70%) |
| DuPont | DD | $47.93 | +1.09 (+2.33%) |
| Air Products | APD | $285.76 | +7.64 (+2.75%) |
| Linde | LIN | $522.75 | +7.31 (+1.42%) |
| Eastman Chemical | EMN | $75.02 | +1.70 (+2.32%) |
| Celanese | CE | $53.22 | +1.55 (+3.00%) |
| Huntsman | HUN | $15.85 | +0.77 (+5.11%) |

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
