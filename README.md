# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-06-03)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $93.76 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $96.00 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.17 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $3.70 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $34.72 | +0.03 (+0.09%) |
| LyondellBasell | LYB | $67.31 | +0.17 (+0.25%) |
| DuPont | DD | $48.66 | +1.07 (+2.25%) |
| Air Products | APD | $279.29 | +0.40 (+0.14%) |
| Linde | LIN | $495.91 | -1.50 (-0.30%) |
| Eastman Chemical | EMN | $76.67 | +1.18 (+1.56%) |
| Celanese | CE | $55.27 | -0.01 (-0.02%) |
| Huntsman | HUN | $14.99 | -0.01 (-0.07%) |

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
