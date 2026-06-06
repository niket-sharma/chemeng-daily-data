# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-06-06)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $90.54 | -2.50 (-2.69%) | $/barrel |
| Brent Crude Oil | $93.09 | -1.94 (-2.04%) | $/barrel |
| Natural Gas | $3.23 | -0.11 (-3.21%) | $/MMBtu |
| Heating Oil | $3.59 | -0.09 (-2.35%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $33.97 | -0.82 (-2.36%) |
| LyondellBasell | LYB | $64.50 | -1.68 (-2.54%) |
| DuPont | DD | $46.85 | -0.80 (-1.68%) |
| Air Products | APD | $282.35 | -0.50 (-0.18%) |
| Linde | LIN | $507.90 | +0.45 (+0.09%) |
| Eastman Chemical | EMN | $71.84 | -0.58 (-0.80%) |
| Celanese | CE | $51.03 | -2.94 (-5.45%) |
| Huntsman | HUN | $14.21 | -0.05 (-0.35%) |

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
