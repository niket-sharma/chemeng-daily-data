# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-08-15)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $82.40 | +1.15 (+1.42%) | $/barrel |
| Brent Crude Oil | $88.52 | +1.45 (+1.67%) | $/barrel |
| Natural Gas | $2.73 | +0.01 (+0.22%) | $/MMBtu |
| Heating Oil | $4.28 | +0.03 (+0.76%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $31.07 | +0.71 (+2.34%) |
| LyondellBasell | LYB | $63.76 | +1.36 (+2.18%) |
| DuPont | DD | $146.26 | +2.16 (+1.50%) |
| Air Products | APD | $308.97 | +3.45 (+1.13%) |
| Linde | LIN | $482.74 | +4.54 (+0.95%) |
| Eastman Chemical | EMN | $74.07 | +0.30 (+0.41%) |
| Celanese | CE | $45.66 | +1.36 (+3.07%) |
| Huntsman | HUN | $10.30 | -0.02 (-0.19%) |

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
