# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-11-10)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $86.35 | -0.50 (-0.58%) | $/barrel |
| Brent Crude Oil | $91.96 | -0.61 (-0.66%) | $/barrel |
| Natural Gas | $3.32 | +0.10 (+3.14%) | $/MMBtu |
| Heating Oil | $4.15 | -0.06 (-1.54%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $31.32 | +0.36 (+1.15%) |
| LyondellBasell | LYB | $60.28 | +0.78 (+1.30%) |
| DuPont | DD | $155.96 | +0.82 (+0.53%) |
| Air Products | APD | $311.86 | +0.78 (+0.25%) |
| Linde | LIN | $521.55 | +1.22 (+0.23%) |
| Eastman Chemical | EMN | $65.34 | -0.05 (-0.08%) |
| Celanese | CE | $48.63 | -0.12 (-0.25%) |
| Huntsman | HUN | $9.51 | -0.03 (-0.37%) |

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
