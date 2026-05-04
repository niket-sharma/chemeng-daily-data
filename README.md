# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-05-04)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $102.03 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $110.73 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $2.86 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $3.93 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $40.03 | -0.26 (-0.65%) |
| LyondellBasell | LYB | $74.89 | -0.10 (-0.13%) |
| DuPont | DD | $45.94 | -0.30 (-0.66%) |
| Air Products | APD | $296.66 | -4.41 (-1.46%) |
| Linde | LIN | $497.76 | -10.17 (-2.00%) |
| Eastman Chemical | EMN | $76.96 | -0.57 (-0.73%) |
| Celanese | CE | $68.85 | -0.39 (-0.56%) |
| Huntsman | HUN | $14.31 | -0.32 (-2.22%) |

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
