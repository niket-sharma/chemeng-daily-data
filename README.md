# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-05-19)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $102.79 | -5.87 (-5.40%) | $/barrel |
| Brent Crude Oil | $109.82 | -2.28 (-2.03%) | $/barrel |
| Natural Gas | $3.02 | -0.00 (-0.10%) | $/MMBtu |
| Heating Oil | $3.95 | -0.16 (-3.95%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $38.56 | -0.19 (-0.49%) |
| LyondellBasell | LYB | $74.13 | -0.93 (-1.24%) |
| DuPont | DD | $48.64 | -0.67 (-1.36%) |
| Air Products | APD | $293.31 | -2.07 (-0.70%) |
| Linde | LIN | $510.86 | +4.75 (+0.94%) |
| Eastman Chemical | EMN | $70.94 | -0.64 (-0.89%) |
| Celanese | CE | $55.75 | -1.05 (-1.85%) |
| Huntsman | HUN | $13.81 | +0.11 (+0.80%) |

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
