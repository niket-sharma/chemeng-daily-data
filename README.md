# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-11-07)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $90.83 | +0.31 (+0.34%) | $/barrel |
| Brent Crude Oil | $98.32 | +0.03 (+0.03%) | $/barrel |
| Natural Gas | $3.00 | +0.05 (+1.73%) | $/MMBtu |
| Heating Oil | $4.33 | -0.02 (-0.46%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $31.40 | -0.58 (-1.81%) |
| LyondellBasell | LYB | $60.72 | -0.91 (-1.48%) |
| DuPont | DD | $146.52 | +1.59 (+1.10%) |
| Air Products | APD | $304.84 | -4.65 (-1.50%) |
| Linde | LIN | $515.25 | -5.98 (-1.15%) |
| Eastman Chemical | EMN | $64.41 | -1.30 (-1.98%) |
| Celanese | CE | $46.49 | -1.35 (-2.82%) |
| Huntsman | HUN | $9.45 | -0.34 (-3.47%) |

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
