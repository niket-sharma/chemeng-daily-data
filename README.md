# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-07-16)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $79.68 | +0.08 (+0.10%) | $/barrel |
| Brent Crude Oil | $85.04 | +0.09 (+0.11%) | $/barrel |
| Natural Gas | $2.84 | -0.09 (-2.98%) | $/MMBtu |
| Heating Oil | $3.92 | -0.03 (-0.77%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $29.67 | -0.03 (-0.12%) |
| LyondellBasell | LYB | $58.60 | +0.60 (+1.03%) |
| DuPont | DD | $134.41 | -0.45 (-0.33%) |
| Air Products | APD | $297.26 | +3.57 (+1.22%) |
| Linde | LIN | $517.73 | +3.58 (+0.70%) |
| Eastman Chemical | EMN | $70.05 | +2.20 (+3.24%) |
| Celanese | CE | $46.65 | -0.56 (-1.20%) |
| Huntsman | HUN | $12.11 | +0.16 (+1.34%) |

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
