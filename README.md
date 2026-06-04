# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-06-04)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $92.77 | -3.25 (-3.38%) | $/barrel |
| Brent Crude Oil | $95.20 | -2.61 (-2.67%) | $/barrel |
| Natural Gas | $3.34 | +0.12 (+3.80%) | $/MMBtu |
| Heating Oil | $3.69 | -0.15 (-4.02%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $34.84 | -0.56 (-1.58%) |
| LyondellBasell | LYB | $66.15 | -1.15 (-1.70%) |
| DuPont | DD | $47.39 | -0.58 (-1.21%) |
| Air Products | APD | $284.05 | +1.78 (+0.63%) |
| Linde | LIN | $510.67 | +3.10 (+0.61%) |
| Eastman Chemical | EMN | $73.14 | -1.69 (-2.26%) |
| Celanese | CE | $54.96 | -0.52 (-0.94%) |
| Huntsman | HUN | $14.35 | -0.38 (-2.58%) |

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
