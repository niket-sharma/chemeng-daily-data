# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-10-30)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $104.54 | +2.54 (+2.49%) | $/barrel |
| Brent Crude Oil | $113.38 | -1.50 (-1.31%) | $/barrel |
| Natural Gas | $2.90 | -0.05 (-1.69%) | $/MMBtu |
| Heating Oil | $4.69 | -0.05 (-1.05%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $34.65 | +1.03 (+3.06%) |
| LyondellBasell | LYB | $68.32 | +2.95 (+4.51%) |
| DuPont | DD | $139.48 | -1.10 (-0.78%) |
| Air Products | APD | $313.70 | +1.95 (+0.62%) |
| Linde | LIN | $514.18 | +11.03 (+2.19%) |
| Eastman Chemical | EMN | $66.09 | -1.84 (-2.71%) |
| Celanese | CE | $48.53 | +0.22 (+0.44%) |
| Huntsman | HUN | $9.61 | +0.64 (+7.19%) |

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
