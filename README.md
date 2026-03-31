# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-03-31)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $102.31 | -0.57 (-0.55%) | $/barrel |
| Brent Crude Oil | $106.69 | -6.09 (-5.40%) | $/barrel |
| Natural Gas | $2.94 | +0.05 (+1.77%) | $/MMBtu |
| Heating Oil | $4.13 | -0.24 (-5.46%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $42.44 | +0.57 (+1.35%) |
| LyondellBasell | LYB | $83.52 | +1.14 (+1.38%) |
| DuPont | DD | $45.33 | +1.10 (+2.50%) |
| Air Products | APD | $292.88 | +1.32 (+0.45%) |
| Linde | LIN | $500.03 | +0.77 (+0.15%) |
| Eastman Chemical | EMN | $74.72 | +2.17 (+2.99%) |
| Celanese | CE | $66.60 | +2.35 (+3.66%) |
| Huntsman | HUN | $13.23 | +0.66 (+5.21%) |

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
