# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-10-24)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $103.27 | +3.80 (+3.82%) | $/barrel |
| Brent Crude Oil | $116.72 | +3.55 (+3.14%) | $/barrel |
| Natural Gas | $2.64 | -0.16 (-5.58%) | $/MMBtu |
| Heating Oil | $4.98 | +0.05 (+1.06%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $32.61 | +0.80 (+2.51%) |
| LyondellBasell | LYB | $66.45 | +1.08 (+1.65%) |
| DuPont | DD | $136.55 | +1.45 (+1.07%) |
| Air Products | APD | $307.15 | -1.07 (-0.35%) |
| Linde | LIN | $508.83 | -1.53 (-0.30%) |
| Eastman Chemical | EMN | $64.93 | -0.38 (-0.58%) |
| Celanese | CE | $47.71 | +0.49 (+1.04%) |
| Huntsman | HUN | $8.80 | +0.08 (+0.92%) |

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
