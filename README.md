# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-11-20)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $82.51 | -0.70 (-0.84%) | $/barrel |
| Brent Crude Oil | $89.43 | -2.55 (-2.77%) | $/barrel |
| Natural Gas | $3.22 | -0.04 (-1.38%) | $/MMBtu |
| Heating Oil | $3.87 | -0.08 (-2.12%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $nan | +nan (+nan%) |
| LyondellBasell | LYB | $58.19 | -0.27 (-0.46%) |
| DuPont | DD | $149.69 | -0.54 (-0.36%) |
| Air Products | APD | $303.83 | -4.28 (-1.39%) |
| Linde | LIN | $510.21 | -1.95 (-0.38%) |
| Eastman Chemical | EMN | $61.71 | -0.65 (-1.04%) |
| Celanese | CE | $47.40 | -0.81 (-1.68%) |
| Huntsman | HUN | $8.97 | -0.06 (-0.66%) |

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
