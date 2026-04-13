# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-04-13)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $101.21 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $100.00 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $2.67 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $3.75 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $40.29 | +1.28 (+3.28%) |
| LyondellBasell | LYB | $75.99 | +2.27 (+3.08%) |
| DuPont | DD | $46.75 | -0.50 (-1.06%) |
| Air Products | APD | $298.37 | -0.34 (-0.11%) |
| Linde | LIN | $506.45 | +3.30 (+0.66%) |
| Eastman Chemical | EMN | $73.35 | -0.90 (-1.21%) |
| Celanese | CE | $66.36 | +3.23 (+5.11%) |
| Huntsman | HUN | $13.64 | -0.01 (-0.11%) |

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
