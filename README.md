# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-05-22)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $97.40 | +1.05 (+1.09%) | $/barrel |
| Brent Crude Oil | $104.03 | +1.45 (+1.41%) | $/barrel |
| Natural Gas | $3.06 | +0.04 (+1.39%) | $/MMBtu |
| Heating Oil | $3.79 | -0.04 (-1.05%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $35.76 | -0.15 (-0.42%) |
| LyondellBasell | LYB | $69.47 | -0.61 (-0.86%) |
| DuPont | DD | $47.98 | +0.83 (+1.76%) |
| Air Products | APD | $290.92 | +0.73 (+0.25%) |
| Linde | LIN | $515.80 | +1.29 (+0.25%) |
| Eastman Chemical | EMN | $73.96 | +0.77 (+1.06%) |
| Celanese | CE | $52.21 | -0.69 (-1.30%) |
| Huntsman | HUN | $14.39 | +0.01 (+0.03%) |

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
