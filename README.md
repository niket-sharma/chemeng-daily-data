# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-07-02)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $67.61 | -0.97 (-1.41%) | $/barrel |
| Brent Crude Oil | $70.73 | -0.84 (-1.17%) | $/barrel |
| Natural Gas | $3.16 | -0.06 (-1.83%) | $/MMBtu |
| Heating Oil | $3.16 | -0.05 (-1.69%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $28.12 | +1.10 (+4.07%) |
| LyondellBasell | LYB | $53.63 | +1.05 (+2.01%) |
| DuPont | DD | $139.18 | +0.71 (+0.51%) |
| Air Products | APD | $308.90 | +2.50 (+0.81%) |
| Linde | LIN | $543.44 | +9.89 (+1.85%) |
| Eastman Chemical | EMN | $68.62 | +1.53 (+2.28%) |
| Celanese | CE | $47.28 | +2.08 (+4.61%) |
| Huntsman | HUN | $10.69 | +0.14 (+1.28%) |

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
