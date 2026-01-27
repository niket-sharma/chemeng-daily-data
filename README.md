# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-01-27)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $61.50 | +0.87 (+1.43%) | $/barrel |
| Brent Crude Oil | $65.58 | -0.01 (-0.02%) | $/barrel |
| Natural Gas | $3.76 | -3.04 (-44.65%) | $/MMBtu |
| Heating Oil | $2.37 | -0.20 (-7.83%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $28.18 | -0.07 (-0.25%) |
| LyondellBasell | LYB | $50.86 | -0.13 (-0.25%) |
| DuPont | DD | $44.20 | +0.06 (+0.14%) |
| Air Products | APD | $262.62 | +1.27 (+0.49%) |
| Linde | LIN | $455.03 | +3.46 (+0.77%) |
| Eastman Chemical | EMN | $68.89 | +0.18 (+0.26%) |
| Celanese | CE | $47.53 | +0.01 (+0.02%) |
| Huntsman | HUN | $11.72 | -0.13 (-1.10%) |

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
