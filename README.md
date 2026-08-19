# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-08-19)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $84.64 | -0.30 (-0.35%) | $/barrel |
| Brent Crude Oil | $91.56 | +0.54 (+0.59%) | $/barrel |
| Natural Gas | $2.83 | +0.05 (+1.95%) | $/MMBtu |
| Heating Oil | $4.32 | -0.13 (-2.93%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $32.01 | +0.82 (+2.63%) |
| LyondellBasell | LYB | $67.53 | +2.20 (+3.37%) |
| DuPont | DD | $139.55 | +0.74 (+0.53%) |
| Air Products | APD | $305.07 | +1.84 (+0.61%) |
| Linde | LIN | $482.14 | +3.43 (+0.72%) |
| Eastman Chemical | EMN | $74.91 | +1.91 (+2.62%) |
| Celanese | CE | $46.50 | +1.85 (+4.14%) |
| Huntsman | HUN | $10.37 | +0.32 (+3.18%) |

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
