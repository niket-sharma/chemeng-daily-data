# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-09-24)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $95.50 | +3.34 (+3.62%) | $/barrel |
| Brent Crude Oil | $107.31 | +4.23 (+4.10%) | $/barrel |
| Natural Gas | $3.39 | +0.36 (+12.04%) | $/MMBtu |
| Heating Oil | $4.66 | -0.12 (-2.53%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $28.83 | +0.18 (+0.64%) |
| LyondellBasell | LYB | $60.66 | +0.69 (+1.15%) |
| DuPont | DD | $130.63 | -0.25 (-0.19%) |
| Air Products | APD | $285.93 | -1.04 (-0.36%) |
| Linde | LIN | $469.70 | -0.02 (-0.00%) |
| Eastman Chemical | EMN | $66.01 | -0.79 (-1.18%) |
| Celanese | CE | $47.92 | -0.58 (-1.19%) |
| Huntsman | HUN | $8.90 | -0.20 (-2.25%) |

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
