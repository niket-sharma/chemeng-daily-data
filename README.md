# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-06-01)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $93.86 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $96.98 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.18 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $3.73 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $34.78 | +1.03 (+3.05%) |
| LyondellBasell | LYB | $67.07 | +0.42 (+0.63%) |
| DuPont | DD | $47.57 | -0.85 (-1.76%) |
| Air Products | APD | $276.51 | -2.11 (-0.76%) |
| Linde | LIN | $490.91 | -6.78 (-1.36%) |
| Eastman Chemical | EMN | $75.83 | -0.04 (-0.05%) |
| Celanese | CE | $55.84 | +2.71 (+5.10%) |
| Huntsman | HUN | $14.74 | -0.61 (-3.97%) |

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
