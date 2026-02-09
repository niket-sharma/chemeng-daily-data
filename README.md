# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-02-09)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $62.95 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $67.40 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $3.22 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $2.39 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $31.78 | +1.18 (+3.86%) |
| LyondellBasell | LYB | $55.10 | +1.22 (+2.26%) |
| DuPont | DD | $46.73 | +1.05 (+2.30%) |
| Air Products | APD | $283.12 | -0.38 (-0.13%) |
| Linde | LIN | $448.24 | -11.45 (-2.49%) |
| Eastman Chemical | EMN | $77.43 | +1.35 (+1.77%) |
| Celanese | CE | $54.88 | +2.82 (+5.42%) |
| Huntsman | HUN | $13.46 | +0.26 (+1.97%) |

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
