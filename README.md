# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-10-12)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $93.16 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $105.92 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.18 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $4.69 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $28.12 | -0.30 (-1.06%) |
| LyondellBasell | LYB | $59.41 | -0.62 (-1.03%) |
| DuPont | DD | $129.37 | -0.63 (-0.48%) |
| Air Products | APD | $283.87 | +2.61 (+0.93%) |
| Linde | LIN | $487.35 | +3.62 (+0.75%) |
| Eastman Chemical | EMN | $62.10 | -0.59 (-0.94%) |
| Celanese | CE | $44.56 | -0.46 (-1.02%) |
| Huntsman | HUN | $8.07 | -0.07 (-0.86%) |

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
