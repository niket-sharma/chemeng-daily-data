# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-11-02)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $96.26 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $104.23 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $2.86 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $4.42 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $34.18 | -0.52 (-1.50%) |
| LyondellBasell | LYB | $66.88 | -1.76 (-2.56%) |
| DuPont | DD | $141.30 | +1.25 (+0.89%) |
| Air Products | APD | $316.03 | -0.40 (-0.13%) |
| Linde | LIN | $519.72 | +5.48 (+1.07%) |
| Eastman Chemical | EMN | $66.78 | +0.25 (+0.38%) |
| Celanese | CE | $47.94 | -1.36 (-2.76%) |
| Huntsman | HUN | $9.95 | +0.31 (+3.22%) |

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
