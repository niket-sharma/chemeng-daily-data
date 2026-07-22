# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-07-22)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $87.12 | +2.21 (+2.60%) | $/barrel |
| Brent Crude Oil | $94.16 | +3.15 (+3.46%) | $/barrel |
| Natural Gas | $2.92 | +0.05 (+1.82%) | $/MMBtu |
| Heating Oil | $4.08 | -0.05 (-1.19%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $31.30 | +0.83 (+2.71%) |
| LyondellBasell | LYB | $62.19 | +1.00 (+1.63%) |
| DuPont | DD | $141.18 | +2.39 (+1.72%) |
| Air Products | APD | $296.05 | -0.34 (-0.11%) |
| Linde | LIN | $505.44 | +0.41 (+0.08%) |
| Eastman Chemical | EMN | $69.57 | +0.58 (+0.84%) |
| Celanese | CE | $48.00 | +1.59 (+3.43%) |
| Huntsman | HUN | $12.96 | +0.35 (+2.78%) |

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
