# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-10-01)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $92.96 | +2.54 (+2.81%) | $/barrel |
| Brent Crude Oil | $102.43 | -1.10 (-1.06%) | $/barrel |
| Natural Gas | $2.96 | -0.07 (-2.18%) | $/MMBtu |
| Heating Oil | $4.64 | -0.32 (-6.45%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $27.57 | +0.02 (+0.09%) |
| LyondellBasell | LYB | $57.92 | +0.45 (+0.78%) |
| DuPont | DD | $129.64 | -0.25 (-0.19%) |
| Air Products | APD | $272.29 | -5.94 (-2.13%) |
| Linde | LIN | $469.69 | -4.96 (-1.04%) |
| Eastman Chemical | EMN | $63.88 | -0.96 (-1.48%) |
| Celanese | CE | $44.22 | -0.15 (-0.34%) |
| Huntsman | HUN | $8.60 | +0.20 (+2.32%) |

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
