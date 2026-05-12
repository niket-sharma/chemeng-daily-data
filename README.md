# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-05-12)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $101.59 | +3.52 (+3.59%) | $/barrel |
| Brent Crude Oil | $107.56 | +3.35 (+3.21%) | $/barrel |
| Natural Gas | $2.83 | -0.08 (-2.68%) | $/MMBtu |
| Heating Oil | $4.09 | +0.12 (+3.12%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $38.83 | +0.08 (+0.19%) |
| LyondellBasell | LYB | $73.52 | -0.01 (-0.01%) |
| DuPont | DD | $49.52 | -1.06 (-2.10%) |
| Air Products | APD | $299.45 | -5.05 (-1.66%) |
| Linde | LIN | $499.45 | -4.95 (-0.98%) |
| Eastman Chemical | EMN | $72.86 | -1.78 (-2.39%) |
| Celanese | CE | $58.60 | -0.95 (-1.60%) |
| Huntsman | HUN | $14.27 | -0.57 (-3.81%) |

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
