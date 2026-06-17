# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-06-17)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $77.36 | +1.31 (+1.72%) | $/barrel |
| Brent Crude Oil | $81.02 | +2.06 (+2.61%) | $/barrel |
| Natural Gas | $3.16 | -0.08 (-2.56%) | $/MMBtu |
| Heating Oil | $3.20 | +0.03 (+0.88%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $33.50 | +0.54 (+1.64%) |
| LyondellBasell | LYB | $63.53 | +0.94 (+1.49%) |
| DuPont | DD | $48.86 | +0.82 (+1.71%) |
| Air Products | APD | $280.89 | +0.41 (+0.15%) |
| Linde | LIN | $516.20 | -1.97 (-0.38%) |
| Eastman Chemical | EMN | $74.43 | +1.15 (+1.57%) |
| Celanese | CE | $52.64 | +0.71 (+1.37%) |
| Huntsman | HUN | $13.30 | +0.11 (+0.87%) |

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
