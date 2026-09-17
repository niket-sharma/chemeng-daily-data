# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-09-17)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $101.90 | -0.53 (-0.52%) | $/barrel |
| Brent Crude Oil | $104.62 | -1.21 (-1.14%) | $/barrel |
| Natural Gas | $2.91 | +0.02 (+0.69%) | $/MMBtu |
| Heating Oil | $4.89 | -0.36 (-6.88%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $29.70 | -0.38 (-1.26%) |
| LyondellBasell | LYB | $64.26 | -0.64 (-0.99%) |
| DuPont | DD | $129.48 | +1.91 (+1.50%) |
| Air Products | APD | $286.20 | -0.88 (-0.31%) |
| Linde | LIN | $458.97 | -3.12 (-0.68%) |
| Eastman Chemical | EMN | $66.72 | +1.65 (+2.54%) |
| Celanese | CE | $46.92 | +0.05 (+0.11%) |
| Huntsman | HUN | $9.27 | +0.09 (+0.92%) |

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
