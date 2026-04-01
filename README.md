# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-04-01)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $101.38 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $118.35 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $2.88 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $4.16 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $41.65 | -0.22 (-0.53%) |
| LyondellBasell | LYB | $80.56 | -1.82 (-2.21%) |
| DuPont | DD | $45.80 | +1.58 (+3.57%) |
| Air Products | APD | $290.49 | -1.07 (-0.37%) |
| Linde | LIN | $495.76 | -3.50 (-0.70%) |
| Eastman Chemical | EMN | $76.32 | +3.77 (+5.20%) |
| Celanese | CE | $65.77 | +1.52 (+2.37%) |
| Huntsman | HUN | $13.31 | +0.74 (+5.89%) |

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
