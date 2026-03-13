# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-03-13)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $95.73 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $100.46 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.23 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $3.90 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $37.58 | +3.21 (+9.34%) |
| LyondellBasell | LYB | $74.33 | +6.96 (+10.33%) |
| DuPont | DD | $45.34 | -0.65 (-1.41%) |
| Air Products | APD | $290.48 | +12.79 (+4.61%) |
| Linde | LIN | $490.41 | +8.86 (+1.84%) |
| Eastman Chemical | EMN | $70.59 | +2.87 (+4.24%) |
| Celanese | CE | $59.60 | +7.66 (+14.75%) |
| Huntsman | HUN | $12.80 | +1.05 (+8.94%) |

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
