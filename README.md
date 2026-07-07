# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-07-07)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $68.55 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $71.99 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.24 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $3.30 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $27.33 | -0.38 (-1.37%) |
| LyondellBasell | LYB | $52.97 | -0.39 (-0.73%) |
| DuPont | DD | $141.05 | +1.14 (+0.81%) |
| Air Products | APD | $308.86 | -5.33 (-1.70%) |
| Linde | LIN | $540.52 | -6.12 (-1.12%) |
| Eastman Chemical | EMN | $68.90 | +0.04 (+0.06%) |
| Celanese | CE | $47.64 | -0.04 (-0.08%) |
| Huntsman | HUN | $10.58 | -0.24 (-2.22%) |

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
