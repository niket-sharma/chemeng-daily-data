# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-05-01)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $105.07 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $111.55 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $2.77 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $4.14 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $40.49 | +0.94 (+2.38%) |
| LyondellBasell | LYB | $74.60 | +1.31 (+1.79%) |
| DuPont | DD | $45.66 | +1.04 (+2.33%) |
| Air Products | APD | $300.05 | -2.45 (-0.81%) |
| Linde | LIN | $501.14 | -3.57 (-0.71%) |
| Eastman Chemical | EMN | $73.09 | +2.67 (+3.79%) |
| Celanese | CE | $67.76 | +2.67 (+4.10%) |
| Huntsman | HUN | $14.37 | +1.12 (+8.45%) |

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
