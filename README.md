# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-03-13)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $94.61 | -1.12 (-1.17%) | $/barrel |
| Brent Crude Oil | $100.00 | -0.46 (-0.46%) | $/barrel |
| Natural Gas | $3.16 | -0.08 (-2.35%) | $/MMBtu |
| Heating Oil | $3.32 | -0.57 (-14.72%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $37.16 | -0.42 (-1.12%) |
| LyondellBasell | LYB | $72.58 | -1.75 (-2.35%) |
| DuPont | DD | $45.35 | +0.01 (+0.02%) |
| Air Products | APD | $292.83 | +2.35 (+0.81%) |
| Linde | LIN | $495.70 | +5.29 (+1.08%) |
| Eastman Chemical | EMN | $70.68 | +0.09 (+0.13%) |
| Celanese | CE | $59.09 | -0.51 (-0.86%) |
| Huntsman | HUN | $12.23 | -0.57 (-4.45%) |

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
