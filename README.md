# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-07-20)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $81.51 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $88.11 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $2.85 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $4.00 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $30.27 | +0.35 (+1.17%) |
| LyondellBasell | LYB | $59.98 | +0.81 (+1.37%) |
| DuPont | DD | $136.21 | +0.92 (+0.68%) |
| Air Products | APD | $296.34 | +0.72 (+0.24%) |
| Linde | LIN | $514.42 | +1.20 (+0.23%) |
| Eastman Chemical | EMN | $68.03 | -0.57 (-0.83%) |
| Celanese | CE | $44.88 | -0.82 (-1.79%) |
| Huntsman | HUN | $11.90 | +0.11 (+0.89%) |

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
