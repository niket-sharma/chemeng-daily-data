# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-07-30)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $84.40 | -0.06 (-0.07%) | $/barrel |
| Brent Crude Oil | $89.78 | -0.96 (-1.06%) | $/barrel |
| Natural Gas | $2.76 | +0.04 (+1.36%) | $/MMBtu |
| Heating Oil | $4.15 | -0.22 (-5.04%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $29.76 | -0.69 (-2.27%) |
| LyondellBasell | LYB | $59.62 | -0.87 (-1.44%) |
| DuPont | DD | $139.67 | +1.57 (+1.14%) |
| Air Products | APD | $300.16 | +5.89 (+2.00%) |
| Linde | LIN | $504.81 | -6.36 (-1.24%) |
| Eastman Chemical | EMN | $67.96 | +0.68 (+1.02%) |
| Celanese | CE | $44.33 | +0.40 (+0.91%) |
| Huntsman | HUN | $12.02 | +0.06 (+0.46%) |

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
