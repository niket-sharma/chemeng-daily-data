# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-07-01)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $68.67 | -0.83 (-1.19%) | $/barrel |
| Brent Crude Oil | $71.74 | -1.18 (-1.62%) | $/barrel |
| Natural Gas | $3.21 | -0.06 (-1.95%) | $/MMBtu |
| Heating Oil | $3.23 | -0.08 (-2.48%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $27.29 | -0.07 (-0.26%) |
| LyondellBasell | LYB | $52.71 | +0.06 (+0.12%) |
| DuPont | DD | $137.27 | +1.63 (+1.20%) |
| Air Products | APD | $303.62 | +10.44 (+3.56%) |
| Linde | LIN | $530.86 | +11.92 (+2.30%) |
| Eastman Chemical | EMN | $68.01 | +1.03 (+1.55%) |
| Celanese | CE | $45.17 | -0.83 (-1.80%) |
| Huntsman | HUN | $10.48 | -0.14 (-1.32%) |

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
