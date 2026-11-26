# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-11-26)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $84.91 | +1.23 (+1.47%) | $/barrel |
| Brent Crude Oil | $91.73 | -2.88 (-3.04%) | $/barrel |
| Natural Gas | $3.60 | +0.33 (+10.09%) | $/MMBtu |
| Heating Oil | $3.70 | -0.00 (-0.05%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $29.66 | +0.71 (+2.45%) |
| LyondellBasell | LYB | $56.96 | +1.34 (+2.41%) |
| DuPont | DD | $153.62 | +2.91 (+1.93%) |
| Air Products | APD | $314.26 | +5.68 (+1.84%) |
| Linde | LIN | $524.61 | +7.78 (+1.51%) |
| Eastman Chemical | EMN | $61.64 | +0.90 (+1.48%) |
| Celanese | CE | $45.44 | +1.08 (+2.43%) |
| Huntsman | HUN | $9.29 | +0.54 (+6.17%) |

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
