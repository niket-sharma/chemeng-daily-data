# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-05-26)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $93.80 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $96.91 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.07 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $3.68 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $35.44 | -0.57 (-1.58%) |
| LyondellBasell | LYB | $69.49 | -0.24 (-0.34%) |
| DuPont | DD | $50.14 | +2.02 (+4.20%) |
| Air Products | APD | $289.14 | -0.33 (-0.11%) |
| Linde | LIN | $516.01 | -1.57 (-0.30%) |
| Eastman Chemical | EMN | $74.76 | +0.64 (+0.86%) |
| Celanese | CE | $52.75 | +0.36 (+0.69%) |
| Huntsman | HUN | $14.73 | +0.22 (+1.48%) |

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
