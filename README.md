# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-07-26)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $89.31 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $96.78 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $2.89 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $4.10 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $29.84 | -1.06 (-3.43%) |
| LyondellBasell | LYB | $60.32 | -1.40 (-2.27%) |
| DuPont | DD | $137.70 | +0.30 (+0.22%) |
| Air Products | APD | $297.87 | +3.58 (+1.22%) |
| Linde | LIN | $512.28 | +5.96 (+1.18%) |
| Eastman Chemical | EMN | $68.20 | +0.28 (+0.41%) |
| Celanese | CE | $46.43 | -0.92 (-1.94%) |
| Huntsman | HUN | $nan | +nan (+nan%) |

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
