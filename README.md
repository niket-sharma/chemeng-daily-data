# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-08-14)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $81.55 | +0.30 (+0.37%) | $/barrel |
| Brent Crude Oil | $87.61 | +0.54 (+0.62%) | $/barrel |
| Natural Gas | $2.78 | +0.05 (+1.76%) | $/MMBtu |
| Heating Oil | $4.13 | -0.12 (-2.88%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $31.01 | +0.65 (+2.16%) |
| LyondellBasell | LYB | $63.86 | +1.46 (+2.34%) |
| DuPont | DD | $145.70 | +1.60 (+1.11%) |
| Air Products | APD | $305.66 | +0.14 (+0.05%) |
| Linde | LIN | $479.48 | +1.28 (+0.27%) |
| Eastman Chemical | EMN | $74.02 | +0.25 (+0.34%) |
| Celanese | CE | $45.29 | +0.99 (+2.23%) |
| Huntsman | HUN | $10.36 | +0.04 (+0.39%) |

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
