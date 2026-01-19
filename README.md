# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-01-19)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $59.05 | -0.39 (-0.66%) | $/barrel |
| Brent Crude Oil | $63.77 | -0.36 (-0.56%) | $/barrel |
| Natural Gas | $3.62 | +0.51 (+16.50%) | $/MMBtu |
| Heating Oil | $2.24 | +0.00 (+0.09%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $27.57 | -0.37 (-1.32%) |
| LyondellBasell | LYB | $50.91 | +0.03 (+0.06%) |
| DuPont | DD | $42.86 | -0.53 (-1.22%) |
| Air Products | APD | $267.53 | +1.55 (+0.58%) |
| Linde | LIN | $438.96 | -1.08 (-0.25%) |
| Eastman Chemical | EMN | $68.67 | -1.56 (-2.22%) |
| Celanese | CE | $46.94 | -0.20 (-0.42%) |
| Huntsman | HUN | $11.91 | -0.14 (-1.16%) |

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
