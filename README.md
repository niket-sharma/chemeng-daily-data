# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-11-04)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $88.76 | -7.33 (-7.63%) | $/barrel |
| Brent Crude Oil | $95.29 | -8.31 (-8.02%) | $/barrel |
| Natural Gas | $2.95 | +0.06 (+2.07%) | $/MMBtu |
| Heating Oil | $4.22 | -0.31 (-6.80%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $32.74 | -1.05 (-3.11%) |
| LyondellBasell | LYB | $63.06 | -3.03 (-4.58%) |
| DuPont | DD | $152.88 | -0.58 (-0.38%) |
| Air Products | APD | $318.07 | +5.10 (+1.63%) |
| Linde | LIN | $524.85 | +13.30 (+2.60%) |
| Eastman Chemical | EMN | $67.58 | +2.25 (+3.44%) |
| Celanese | CE | $49.64 | -0.72 (-1.43%) |
| Huntsman | HUN | $9.89 | +0.34 (+3.53%) |

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
