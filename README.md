# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-04-17)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $89.72 | -4.97 (-5.25%) | $/barrel |
| Brent Crude Oil | $98.17 | -1.22 (-1.23%) | $/barrel |
| Natural Gas | $2.66 | +0.01 (+0.53%) | $/MMBtu |
| Heating Oil | $3.61 | -0.22 (-5.73%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $39.92 | +1.08 (+2.78%) |
| LyondellBasell | LYB | $75.29 | +2.16 (+2.95%) |
| DuPont | DD | $46.75 | +0.69 (+1.50%) |
| Air Products | APD | $297.24 | +2.03 (+0.69%) |
| Linde | LIN | $499.22 | +1.28 (+0.26%) |
| Eastman Chemical | EMN | $73.35 | +0.60 (+0.82%) |
| Celanese | CE | $68.34 | +3.61 (+5.58%) |
| Huntsman | HUN | $13.74 | +0.15 (+1.10%) |

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
