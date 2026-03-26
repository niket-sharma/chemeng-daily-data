# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-03-26)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $92.78 | +2.46 (+2.72%) | $/barrel |
| Brent Crude Oil | $100.81 | -1.41 (-1.38%) | $/barrel |
| Natural Gas | $2.92 | -0.04 (-1.22%) | $/MMBtu |
| Heating Oil | $4.03 | +0.03 (+0.69%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $39.99 | +0.37 (+0.92%) |
| LyondellBasell | LYB | $77.90 | +0.71 (+0.93%) |
| DuPont | DD | $46.42 | +0.08 (+0.18%) |
| Air Products | APD | $293.30 | +3.21 (+1.11%) |
| Linde | LIN | $495.35 | +3.01 (+0.61%) |
| Eastman Chemical | EMN | $72.20 | +0.80 (+1.12%) |
| Celanese | CE | $62.88 | +0.22 (+0.34%) |
| Huntsman | HUN | $12.78 | +0.41 (+3.31%) |

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
