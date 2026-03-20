# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-03-20)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $96.14 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $108.65 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.17 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $4.34 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $37.49 | -0.20 (-0.53%) |
| LyondellBasell | LYB | $74.57 | -0.63 (-0.84%) |
| DuPont | DD | $43.52 | -0.48 (-1.09%) |
| Air Products | APD | $284.15 | +2.73 (+0.97%) |
| Linde | LIN | $489.80 | +1.23 (+0.25%) |
| Eastman Chemical | EMN | $68.76 | -0.15 (-0.22%) |
| Celanese | CE | $60.33 | +0.44 (+0.73%) |
| Huntsman | HUN | $11.51 | -0.45 (-3.76%) |

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
