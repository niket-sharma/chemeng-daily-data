# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-03-30)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $102.30 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $108.28 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $2.87 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $4.33 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $41.72 | +0.90 (+2.21%) |
| LyondellBasell | LYB | $83.47 | +3.02 (+3.75%) |
| DuPont | DD | $44.98 | -0.28 (-0.62%) |
| Air Products | APD | $294.15 | +1.96 (+0.67%) |
| Linde | LIN | $496.49 | +5.37 (+1.09%) |
| Eastman Chemical | EMN | $72.68 | +1.48 (+2.08%) |
| Celanese | CE | $65.04 | +1.63 (+2.57%) |
| Huntsman | HUN | $12.73 | +0.07 (+0.55%) |

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
