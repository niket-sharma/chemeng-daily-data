# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-02-12)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $64.21 | -0.42 (-0.65%) | $/barrel |
| Brent Crude Oil | $68.90 | -0.50 (-0.72%) | $/barrel |
| Natural Gas | $3.31 | +0.15 (+4.62%) | $/MMBtu |
| Heating Oil | $2.42 | -0.02 (-0.87%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $34.36 | +0.36 (+1.06%) |
| LyondellBasell | LYB | $60.29 | +0.82 (+1.39%) |
| DuPont | DD | $52.64 | +1.11 (+2.15%) |
| Air Products | APD | $296.17 | +3.03 (+1.03%) |
| Linde | LIN | $471.63 | +4.12 (+0.88%) |
| Eastman Chemical | EMN | $83.22 | +1.86 (+2.29%) |
| Celanese | CE | $61.50 | +0.94 (+1.55%) |
| Huntsman | HUN | $14.35 | +0.28 (+2.03%) |

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
