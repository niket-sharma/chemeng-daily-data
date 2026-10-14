# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-10-14)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $95.40 | +1.26 (+1.34%) | $/barrel |
| Brent Crude Oil | $106.32 | +0.63 (+0.60%) | $/barrel |
| Natural Gas | $3.19 | -0.09 (-2.77%) | $/MMBtu |
| Heating Oil | $4.94 | +0.01 (+0.21%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $29.09 | +0.58 (+2.03%) |
| LyondellBasell | LYB | $61.04 | +1.03 (+1.72%) |
| DuPont | DD | $127.90 | -1.65 (-1.27%) |
| Air Products | APD | $290.86 | +1.90 (+0.66%) |
| Linde | LIN | $491.46 | -0.64 (-0.13%) |
| Eastman Chemical | EMN | $62.29 | -0.71 (-1.12%) |
| Celanese | CE | $45.63 | +0.90 (+2.01%) |
| Huntsman | HUN | $8.15 | -0.01 (-0.12%) |

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
