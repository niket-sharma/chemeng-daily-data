# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-03-28)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $99.64 | +5.16 (+5.46%) | $/barrel |
| Brent Crude Oil | $112.57 | +4.56 (+4.22%) | $/barrel |
| Natural Gas | $3.10 | +0.10 (+3.20%) | $/MMBtu |
| Heating Oil | $4.50 | +0.22 (+5.20%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $40.82 | +1.35 (+3.42%) |
| LyondellBasell | LYB | $80.45 | +2.73 (+3.51%) |
| DuPont | DD | $45.26 | -0.76 (-1.65%) |
| Air Products | APD | $292.19 | -0.98 (-0.33%) |
| Linde | LIN | $491.12 | -4.37 (-0.88%) |
| Eastman Chemical | EMN | $71.20 | -1.30 (-1.79%) |
| Celanese | CE | $63.41 | +1.87 (+3.04%) |
| Huntsman | HUN | $12.66 | +0.11 (+0.88%) |

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
