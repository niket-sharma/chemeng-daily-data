# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-09-09)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $95.24 | +2.21 (+2.38%) | $/barrel |
| Brent Crude Oil | $100.25 | +2.33 (+2.38%) | $/barrel |
| Natural Gas | $2.83 | -0.09 (-3.09%) | $/MMBtu |
| Heating Oil | $4.74 | +0.17 (+3.81%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $29.41 | -0.16 (-0.56%) |
| LyondellBasell | LYB | $64.49 | -0.10 (-0.15%) |
| DuPont | DD | $129.29 | -2.03 (-1.54%) |
| Air Products | APD | $298.26 | +0.55 (+0.18%) |
| Linde | LIN | $466.65 | -1.73 (-0.37%) |
| Eastman Chemical | EMN | $68.67 | -1.72 (-2.45%) |
| Celanese | CE | $44.39 | -0.14 (-0.31%) |
| Huntsman | HUN | $9.65 | -0.15 (-1.48%) |

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
