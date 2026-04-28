# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-04-28)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $97.41 | +1.04 (+1.08%) | $/barrel |
| Brent Crude Oil | $102.59 | -5.64 (-5.21%) | $/barrel |
| Natural Gas | $2.72 | +0.17 (+6.59%) | $/MMBtu |
| Heating Oil | $3.88 | -0.10 (-2.40%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $38.10 | -0.56 (-1.45%) |
| LyondellBasell | LYB | $71.02 | +1.15 (+1.65%) |
| DuPont | DD | $46.69 | +0.36 (+0.78%) |
| Air Products | APD | $302.38 | +0.62 (+0.21%) |
| Linde | LIN | $510.75 | +0.45 (+0.09%) |
| Eastman Chemical | EMN | $72.11 | +0.11 (+0.15%) |
| Celanese | CE | $65.09 | +0.12 (+0.18%) |
| Huntsman | HUN | $13.72 | +0.10 (+0.73%) |

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
