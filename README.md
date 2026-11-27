# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-11-27)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $83.08 | -0.60 (-0.72%) | $/barrel |
| Brent Crude Oil | $90.84 | -3.77 (-3.98%) | $/barrel |
| Natural Gas | $3.49 | +0.22 (+6.79%) | $/MMBtu |
| Heating Oil | $3.68 | -0.03 (-0.74%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $30.20 | +0.54 (+1.82%) |
| LyondellBasell | LYB | $57.77 | +0.81 (+1.42%) |
| DuPont | DD | $157.28 | +3.66 (+2.38%) |
| Air Products | APD | $319.09 | +4.83 (+1.54%) |
| Linde | LIN | $532.61 | +8.00 (+1.52%) |
| Eastman Chemical | EMN | $62.56 | +0.92 (+1.49%) |
| Celanese | CE | $46.60 | +1.16 (+2.55%) |
| Huntsman | HUN | $9.48 | +0.19 (+2.05%) |

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
