# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-09-15)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $106.29 | +4.90 (+4.83%) | $/barrel |
| Brent Crude Oil | $109.11 | +3.43 (+3.25%) | $/barrel |
| Natural Gas | $2.91 | +0.01 (+0.45%) | $/MMBtu |
| Heating Oil | $5.01 | +0.04 (+0.89%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $29.82 | +0.92 (+3.17%) |
| LyondellBasell | LYB | $65.18 | +2.43 (+3.87%) |
| DuPont | DD | $125.82 | +1.53 (+1.24%) |
| Air Products | APD | $288.66 | +1.53 (+0.53%) |
| Linde | LIN | $462.25 | -2.16 (-0.47%) |
| Eastman Chemical | EMN | $66.36 | -0.64 (-0.96%) |
| Celanese | CE | $46.49 | +1.71 (+3.81%) |
| Huntsman | HUN | $9.23 | -0.07 (-0.70%) |

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
