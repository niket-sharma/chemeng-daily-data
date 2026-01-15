# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-01-15)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $59.25 | -2.77 (-4.47%) | $/barrel |
| Brent Crude Oil | $63.79 | -2.73 (-4.10%) | $/barrel |
| Natural Gas | $3.13 | +0.01 (+0.29%) | $/MMBtu |
| Heating Oil | $2.19 | -0.09 (-4.05%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $28.26 | +1.71 (+6.44%) |
| LyondellBasell | LYB | $52.00 | +3.33 (+6.84%) |
| DuPont | DD | $42.89 | -0.90 (-2.06%) |
| Air Products | APD | $267.25 | +1.07 (+0.40%) |
| Linde | LIN | $439.98 | -2.92 (-0.66%) |
| Eastman Chemical | EMN | $69.29 | +1.22 (+1.79%) |
| Celanese | CE | $46.96 | +1.08 (+2.35%) |
| Huntsman | HUN | $11.72 | +0.36 (+3.17%) |

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
