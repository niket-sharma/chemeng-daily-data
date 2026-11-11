# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-11-11)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $86.37 | +0.33 (+0.38%) | $/barrel |
| Brent Crude Oil | $92.50 | +1.01 (+1.10%) | $/barrel |
| Natural Gas | $3.24 | -0.06 (-1.73%) | $/MMBtu |
| Heating Oil | $4.20 | +0.07 (+1.71%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $32.52 | +1.04 (+3.30%) |
| LyondellBasell | LYB | $62.56 | +1.96 (+3.23%) |
| DuPont | DD | $155.64 | -1.24 (-0.79%) |
| Air Products | APD | $314.98 | +2.73 (+0.88%) |
| Linde | LIN | $526.25 | +4.47 (+0.86%) |
| Eastman Chemical | EMN | $66.55 | +1.10 (+1.68%) |
| Celanese | CE | $51.28 | +2.35 (+4.80%) |
| Huntsman | HUN | $9.78 | +0.28 (+3.00%) |

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
