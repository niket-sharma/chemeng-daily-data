# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-05-06)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $100.33 | -1.94 (-1.90%) | $/barrel |
| Brent Crude Oil | $107.89 | -1.98 (-1.80%) | $/barrel |
| Natural Gas | $2.78 | -0.01 (-0.39%) | $/MMBtu |
| Heating Oil | $3.99 | -0.04 (-0.90%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $40.80 | +0.22 (+0.54%) |
| LyondellBasell | LYB | $77.76 | +1.72 (+2.26%) |
| DuPont | DD | $49.24 | +3.83 (+8.43%) |
| Air Products | APD | $303.93 | +5.58 (+1.87%) |
| Linde | LIN | $500.29 | +6.74 (+1.37%) |
| Eastman Chemical | EMN | $77.29 | +0.57 (+0.74%) |
| Celanese | CE | $69.01 | +0.27 (+0.39%) |
| Huntsman | HUN | $14.99 | +0.77 (+5.41%) |

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
