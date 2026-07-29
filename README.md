# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-07-29)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $84.55 | +5.29 (+6.67%) | $/barrel |
| Brent Crude Oil | $90.11 | +6.02 (+7.16%) | $/barrel |
| Natural Gas | $2.73 | +0.07 (+2.44%) | $/MMBtu |
| Heating Oil | $4.20 | +0.05 (+1.19%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $29.73 | +0.00 (+0.00%) |
| LyondellBasell | LYB | $60.13 | +0.00 (+0.00%) |
| DuPont | DD | $136.83 | +0.00 (+0.00%) |
| Air Products | APD | $292.14 | +0.00 (+0.00%) |
| Linde | LIN | $506.16 | +0.00 (+0.00%) |
| Eastman Chemical | EMN | $66.99 | +0.00 (+0.00%) |
| Celanese | CE | $43.16 | +0.00 (+0.00%) |
| Huntsman | HUN | $11.54 | +0.00 (+0.00%) |

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
