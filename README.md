# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-02-10)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $64.25 | -0.11 (-0.17%) | $/barrel |
| Brent Crude Oil | $69.13 | +0.09 (+0.13%) | $/barrel |
| Natural Gas | $3.16 | +0.03 (+0.83%) | $/MMBtu |
| Heating Oil | $2.33 | -0.08 (-3.48%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $32.53 | +0.45 (+1.40%) |
| LyondellBasell | LYB | $56.08 | +0.61 (+1.10%) |
| DuPont | DD | $48.38 | +1.28 (+2.72%) |
| Air Products | APD | $288.96 | +2.59 (+0.90%) |
| Linde | LIN | $457.41 | +1.07 (+0.23%) |
| Eastman Chemical | EMN | $79.67 | +1.29 (+1.65%) |
| Celanese | CE | $56.40 | +1.37 (+2.48%) |
| Huntsman | HUN | $13.19 | +0.14 (+1.11%) |

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
