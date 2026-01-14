# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-01-14)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $61.81 | +0.66 (+1.08%) | $/barrel |
| Brent Crude Oil | $66.22 | +0.75 (+1.15%) | $/barrel |
| Natural Gas | $3.22 | -0.19 (-5.67%) | $/MMBtu |
| Heating Oil | $2.23 | -0.01 (-0.37%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $26.55 | +0.05 (+0.19%) |
| LyondellBasell | LYB | $48.67 | +0.47 (+0.98%) |
| DuPont | DD | $43.79 | +0.36 (+0.83%) |
| Air Products | APD | $266.18 | -0.86 (-0.32%) |
| Linde | LIN | $442.90 | -0.73 (-0.16%) |
| Eastman Chemical | EMN | $68.07 | -0.33 (-0.48%) |
| Celanese | CE | $45.88 | +0.24 (+0.53%) |
| Huntsman | HUN | $11.36 | -0.15 (-1.30%) |

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
