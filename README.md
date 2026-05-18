# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-05-18)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $102.04 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $110.04 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.02 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $4.00 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $38.62 | -0.12 (-0.32%) |
| LyondellBasell | LYB | $74.33 | -0.73 (-0.97%) |
| DuPont | DD | $49.25 | -0.06 (-0.12%) |
| Air Products | APD | $294.29 | -1.09 (-0.37%) |
| Linde | LIN | $509.89 | +3.78 (+0.75%) |
| Eastman Chemical | EMN | $71.91 | +0.33 (+0.46%) |
| Celanese | CE | $56.70 | -0.10 (-0.18%) |
| Huntsman | HUN | $13.96 | +0.26 (+1.89%) |

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
