# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-09-04)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $91.20 | -0.10 (-0.11%) | $/barrel |
| Brent Crude Oil | $95.96 | +0.44 (+0.46%) | $/barrel |
| Natural Gas | $2.95 | +0.03 (+1.20%) | $/MMBtu |
| Heating Oil | $4.52 | -0.07 (-1.57%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $30.23 | -0.13 (-0.43%) |
| LyondellBasell | LYB | $64.75 | -0.01 (-0.02%) |
| DuPont | DD | $130.79 | -0.34 (-0.26%) |
| Air Products | APD | $302.09 | -2.13 (-0.70%) |
| Linde | LIN | $479.70 | -2.49 (-0.52%) |
| Eastman Chemical | EMN | $71.48 | +0.71 (+1.00%) |
| Celanese | CE | $45.44 | +0.24 (+0.53%) |
| Huntsman | HUN | $9.69 | +0.29 (+3.03%) |

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
