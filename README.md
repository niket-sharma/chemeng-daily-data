# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-05-27)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $90.77 | -3.12 (-3.32%) | $/barrel |
| Brent Crude Oil | $94.00 | -5.58 (-5.60%) | $/barrel |
| Natural Gas | $3.08 | +0.19 (+6.50%) | $/MMBtu |
| Heating Oil | $3.54 | -0.18 (-4.77%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $34.72 | -0.56 (-1.59%) |
| LyondellBasell | LYB | $68.29 | -0.72 (-1.04%) |
| DuPont | DD | $47.74 | -1.72 (-3.48%) |
| Air Products | APD | $286.20 | -3.40 (-1.18%) |
| Linde | LIN | $511.54 | -3.43 (-0.67%) |
| Eastman Chemical | EMN | $76.21 | +1.82 (+2.45%) |
| Celanese | CE | $52.36 | -0.01 (-0.02%) |
| Huntsman | HUN | $14.86 | +0.12 (+0.85%) |

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
