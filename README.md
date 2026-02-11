# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-02-11)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $65.77 | +1.81 (+2.83%) | $/barrel |
| Brent Crude Oil | $70.64 | +1.84 (+2.67%) | $/barrel |
| Natural Gas | $3.12 | +0.00 (+0.03%) | $/MMBtu |
| Heating Oil | $2.48 | +0.08 (+3.26%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $34.35 | +0.75 (+2.23%) |
| LyondellBasell | LYB | $59.32 | +1.66 (+2.88%) |
| DuPont | DD | $50.69 | +1.26 (+2.56%) |
| Air Products | APD | $290.77 | +0.00 (+0.00%) |
| Linde | LIN | $462.34 | +1.83 (+0.40%) |
| Eastman Chemical | EMN | $81.39 | +0.80 (+0.99%) |
| Celanese | CE | $59.87 | +1.55 (+2.65%) |
| Huntsman | HUN | $14.02 | +0.42 (+3.09%) |

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
