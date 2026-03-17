# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-03-17)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $94.49 | +0.99 (+1.06%) | $/barrel |
| Brent Crude Oil | $102.14 | +1.93 (+1.93%) | $/barrel |
| Natural Gas | $3.07 | +0.04 (+1.46%) | $/MMBtu |
| Heating Oil | $3.81 | -0.03 (-0.69%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $36.98 | +0.98 (+2.72%) |
| LyondellBasell | LYB | $72.48 | +1.40 (+1.97%) |
| DuPont | DD | $45.81 | +0.41 (+0.90%) |
| Air Products | APD | $290.17 | +1.01 (+0.35%) |
| Linde | LIN | $498.41 | +1.00 (+0.20%) |
| Eastman Chemical | EMN | $71.47 | +1.90 (+2.74%) |
| Celanese | CE | $58.97 | +2.90 (+5.17%) |
| Huntsman | HUN | $12.39 | +0.59 (+5.00%) |

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
