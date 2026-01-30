# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-01-30)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $64.33 | -1.09 (-1.67%) | $/barrel |
| Brent Crude Oil | $68.46 | -2.25 (-3.18%) | $/barrel |
| Natural Gas | $3.86 | -0.06 (-1.53%) | $/MMBtu |
| Heating Oil | $2.46 | -0.12 (-4.71%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $27.16 | -0.62 (-2.23%) |
| LyondellBasell | LYB | $49.95 | -0.52 (-1.03%) |
| DuPont | DD | $44.60 | -0.03 (-0.07%) |
| Air Products | APD | $256.02 | +0.13 (+0.05%) |
| Linde | LIN | $455.00 | +3.50 (+0.78%) |
| Eastman Chemical | EMN | $68.99 | -0.04 (-0.06%) |
| Celanese | CE | $45.44 | -0.73 (-1.58%) |
| Huntsman | HUN | $11.18 | -0.23 (-2.02%) |

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
