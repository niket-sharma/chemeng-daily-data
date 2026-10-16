# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-10-16)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $98.66 | +0.69 (+0.70%) | $/barrel |
| Brent Crude Oil | $109.30 | +3.38 (+3.19%) | $/barrel |
| Natural Gas | $3.14 | -0.09 (-2.81%) | $/MMBtu |
| Heating Oil | $4.70 | -0.14 (-2.96%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $29.89 | +0.23 (+0.78%) |
| LyondellBasell | LYB | $64.04 | +1.38 (+2.19%) |
| DuPont | DD | $130.94 | -0.66 (-0.50%) |
| Air Products | APD | $296.07 | -0.53 (-0.18%) |
| Linde | LIN | $497.25 | +4.03 (+0.82%) |
| Eastman Chemical | EMN | $62.83 | -1.03 (-1.62%) |
| Celanese | CE | $47.10 | +0.66 (+1.42%) |
| Huntsman | HUN | $8.58 | +0.02 (+0.23%) |

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
