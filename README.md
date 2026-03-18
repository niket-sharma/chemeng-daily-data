# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-03-18)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $96.21 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $103.42 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.03 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $4.02 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $36.91 | +0.91 (+2.53%) |
| LyondellBasell | LYB | $71.20 | +0.12 (+0.17%) |
| DuPont | DD | $45.54 | +0.14 (+0.31%) |
| Air Products | APD | $286.15 | -3.01 (-1.04%) |
| Linde | LIN | $494.05 | -3.36 (-0.68%) |
| Eastman Chemical | EMN | $71.27 | +1.70 (+2.44%) |
| Celanese | CE | $60.18 | +4.11 (+7.33%) |
| Huntsman | HUN | $12.21 | +0.41 (+3.47%) |

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
