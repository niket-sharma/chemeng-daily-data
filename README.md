# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-03-17)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $95.87 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $102.80 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.02 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $3.73 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $36.00 | -0.62 (-1.69%) |
| LyondellBasell | LYB | $71.08 | -1.22 (-1.69%) |
| DuPont | DD | $45.40 | +0.50 (+1.11%) |
| Air Products | APD | $289.16 | +1.18 (+0.41%) |
| Linde | LIN | $497.41 | +3.49 (+0.71%) |
| Eastman Chemical | EMN | $69.57 | +0.32 (+0.46%) |
| Celanese | CE | $56.07 | -1.67 (-2.89%) |
| Huntsman | HUN | $11.80 | -0.23 (-1.91%) |

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
