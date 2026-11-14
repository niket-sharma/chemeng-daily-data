# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-11-14)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $88.56 | -0.18 (-0.20%) | $/barrel |
| Brent Crude Oil | $95.84 | +0.02 (+0.02%) | $/barrel |
| Natural Gas | $3.23 | -0.11 (-3.29%) | $/MMBtu |
| Heating Oil | $4.26 | -0.03 (-0.65%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $33.04 | -0.11 (-0.33%) |
| LyondellBasell | LYB | $64.43 | +0.55 (+0.86%) |
| DuPont | DD | $153.78 | -0.92 (-0.59%) |
| Air Products | APD | $316.53 | +0.33 (+0.10%) |
| Linde | LIN | $526.06 | +3.57 (+0.68%) |
| Eastman Chemical | EMN | $65.03 | -0.58 (-0.88%) |
| Celanese | CE | $51.41 | +0.15 (+0.29%) |
| Huntsman | HUN | $9.53 | -0.13 (-1.35%) |

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
