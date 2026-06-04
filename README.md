# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-06-04)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $95.24 | -0.78 (-0.81%) | $/barrel |
| Brent Crude Oil | $96.94 | -0.87 (-0.89%) | $/barrel |
| Natural Gas | $3.23 | +0.02 (+0.56%) | $/MMBtu |
| Heating Oil | $3.83 | -0.01 (-0.39%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $35.40 | +0.68 (+1.96%) |
| LyondellBasell | LYB | $67.30 | -0.01 (-0.01%) |
| DuPont | DD | $47.97 | -0.69 (-1.42%) |
| Air Products | APD | $282.27 | +2.98 (+1.07%) |
| Linde | LIN | $507.57 | +11.66 (+2.35%) |
| Eastman Chemical | EMN | $74.83 | -1.84 (-2.40%) |
| Celanese | CE | $55.48 | +0.21 (+0.38%) |
| Huntsman | HUN | $14.73 | -0.26 (-1.73%) |

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
