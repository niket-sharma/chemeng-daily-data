# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-02-04)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $63.82 | +0.61 (+0.97%) | $/barrel |
| Brent Crude Oil | $67.86 | +0.53 (+0.79%) | $/barrel |
| Natural Gas | $3.31 | -0.01 (-0.15%) | $/MMBtu |
| Heating Oil | $2.43 | +0.02 (+0.92%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $30.49 | +1.61 (+5.57%) |
| LyondellBasell | LYB | $53.45 | +3.20 (+6.37%) |
| DuPont | DD | $45.30 | +0.87 (+1.96%) |
| Air Products | APD | $277.96 | +6.97 (+2.57%) |
| Linde | LIN | $463.57 | +3.41 (+0.74%) |
| Eastman Chemical | EMN | $75.90 | +4.42 (+6.18%) |
| Celanese | CE | $48.04 | +2.17 (+4.73%) |
| Huntsman | HUN | $12.98 | +1.50 (+13.07%) |

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
