# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-04-03)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $111.54 | +11.42 (+11.41%) | $/barrel |
| Brent Crude Oil | $109.03 | +7.87 (+7.78%) | $/barrel |
| Natural Gas | $2.80 | -0.02 (-0.67%) | $/MMBtu |
| Heating Oil | $4.36 | +0.30 (+7.50%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $41.40 | +0.71 (+1.74%) |
| LyondellBasell | LYB | $79.60 | +2.89 (+3.77%) |
| DuPont | DD | $45.48 | -0.73 (-1.58%) |
| Air Products | APD | $293.55 | +4.12 (+1.42%) |
| Linde | LIN | $502.60 | +8.77 (+1.78%) |
| Eastman Chemical | EMN | $75.07 | -0.74 (-0.98%) |
| Celanese | CE | $64.06 | +0.51 (+0.80%) |
| Huntsman | HUN | $12.91 | -0.11 (-0.84%) |

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
