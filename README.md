# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-05-09)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $95.42 | +0.61 (+0.64%) | $/barrel |
| Brent Crude Oil | $101.29 | +1.23 (+1.23%) | $/barrel |
| Natural Gas | $2.76 | -0.01 (-0.43%) | $/MMBtu |
| Heating Oil | $3.90 | +0.08 (+2.16%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $36.87 | -0.45 (-1.21%) |
| LyondellBasell | LYB | $71.76 | +0.25 (+0.35%) |
| DuPont | DD | $49.76 | +1.40 (+2.89%) |
| Air Products | APD | $295.41 | +0.42 (+0.14%) |
| Linde | LIN | $493.16 | -0.69 (-0.14%) |
| Eastman Chemical | EMN | $73.65 | -0.04 (-0.05%) |
| Celanese | CE | $57.17 | -1.23 (-2.11%) |
| Huntsman | HUN | $14.96 | +0.22 (+1.49%) |

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
