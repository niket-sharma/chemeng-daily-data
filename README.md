# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-05-21)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $101.19 | +2.93 (+2.98%) | $/barrel |
| Brent Crude Oil | $107.46 | +2.44 (+2.32%) | $/barrel |
| Natural Gas | $3.16 | +0.16 (+5.26%) | $/MMBtu |
| Heating Oil | $3.87 | -0.08 (-2.07%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $36.46 | +0.19 (+0.51%) |
| LyondellBasell | LYB | $71.19 | -0.11 (-0.15%) |
| DuPont | DD | $46.27 | -0.98 (-2.07%) |
| Air Products | APD | $291.47 | +2.28 (+0.79%) |
| Linde | LIN | $513.29 | +6.66 (+1.32%) |
| Eastman Chemical | EMN | $71.16 | +0.51 (+0.72%) |
| Celanese | CE | $52.33 | -1.17 (-2.19%) |
| Huntsman | HUN | $14.07 | +0.01 (+0.07%) |

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
