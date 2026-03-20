# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-03-20)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $95.48 | -0.66 (-0.69%) | $/barrel |
| Brent Crude Oil | $104.55 | -4.10 (-3.77%) | $/barrel |
| Natural Gas | $3.07 | -0.10 (-3.19%) | $/MMBtu |
| Heating Oil | $4.08 | -0.27 (-6.13%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $37.06 | -0.43 (-1.15%) |
| LyondellBasell | LYB | $73.78 | -0.79 (-1.07%) |
| DuPont | DD | $42.90 | -0.62 (-1.42%) |
| Air Products | APD | $282.72 | -1.43 (-0.50%) |
| Linde | LIN | $491.36 | +1.56 (+0.32%) |
| Eastman Chemical | EMN | $67.22 | -1.54 (-2.24%) |
| Celanese | CE | $58.66 | -1.67 (-2.77%) |
| Huntsman | HUN | $10.86 | -0.65 (-5.60%) |

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
