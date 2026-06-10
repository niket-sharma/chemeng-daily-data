# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-06-10)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $90.05 | +1.85 (+2.10%) | $/barrel |
| Brent Crude Oil | $92.92 | +1.47 (+1.61%) | $/barrel |
| Natural Gas | $3.21 | +0.07 (+2.10%) | $/MMBtu |
| Heating Oil | $3.61 | +0.07 (+1.90%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $33.75 | +0.53 (+1.60%) |
| LyondellBasell | LYB | $64.08 | +0.44 (+0.69%) |
| DuPont | DD | $46.04 | -1.02 (-2.16%) |
| Air Products | APD | $282.83 | -0.15 (-0.05%) |
| Linde | LIN | $516.13 | +0.54 (+0.10%) |
| Eastman Chemical | EMN | $73.05 | +0.12 (+0.16%) |
| Celanese | CE | $50.32 | -0.60 (-1.18%) |
| Huntsman | HUN | $14.39 | -0.15 (-1.07%) |

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
