# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-10-04)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $91.11 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $102.25 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.04 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $4.50 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $27.97 | +0.38 (+1.38%) |
| LyondellBasell | LYB | $58.58 | +0.80 (+1.38%) |
| DuPont | DD | $129.98 | +0.78 (+0.60%) |
| Air Products | APD | $277.57 | +4.24 (+1.55%) |
| Linde | LIN | $479.48 | +10.03 (+2.14%) |
| Eastman Chemical | EMN | $64.87 | +0.82 (+1.28%) |
| Celanese | CE | $44.19 | -0.01 (-0.02%) |
| Huntsman | HUN | $8.53 | -0.14 (-1.61%) |

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
