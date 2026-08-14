# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-08-14)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $81.34 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $87.14 | +0.07 (+0.08%) | $/barrel |
| Natural Gas | $2.75 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $4.11 | -0.14 (-3.30%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $30.36 | -0.21 (-0.69%) |
| LyondellBasell | LYB | $62.40 | -0.40 (-0.64%) |
| DuPont | DD | $144.10 | -0.27 (-0.19%) |
| Air Products | APD | $305.52 | +1.45 (+0.48%) |
| Linde | LIN | $478.20 | -1.23 (-0.26%) |
| Eastman Chemical | EMN | $73.77 | +1.23 (+1.70%) |
| Celanese | CE | $44.30 | +0.99 (+2.29%) |
| Huntsman | HUN | $10.32 | +0.17 (+1.67%) |

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
