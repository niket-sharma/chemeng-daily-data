# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-08-10)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $80.44 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $85.84 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $2.80 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $4.11 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $29.79 | +0.45 (+1.53%) |
| LyondellBasell | LYB | $60.92 | +1.33 (+2.23%) |
| DuPont | DD | $142.26 | -0.21 (-0.15%) |
| Air Products | APD | $305.84 | +2.40 (+0.79%) |
| Linde | LIN | $489.18 | -0.80 (-0.16%) |
| Eastman Chemical | EMN | $72.85 | -0.79 (-1.07%) |
| Celanese | CE | $43.73 | -0.16 (-0.36%) |
| Huntsman | HUN | $10.11 | -0.01 (-0.10%) |

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
