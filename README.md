# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-05-07)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $95.66 | +0.58 (+0.61%) | $/barrel |
| Brent Crude Oil | $101.90 | +0.63 (+0.62%) | $/barrel |
| Natural Gas | $2.72 | -0.01 (-0.26%) | $/MMBtu |
| Heating Oil | $3.78 | -0.01 (-0.15%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $38.50 | -2.30 (-5.64%) |
| LyondellBasell | LYB | $73.48 | -4.28 (-5.50%) |
| DuPont | DD | $50.07 | +0.83 (+1.69%) |
| Air Products | APD | $300.21 | -3.72 (-1.22%) |
| Linde | LIN | $501.87 | +1.58 (+0.32%) |
| Eastman Chemical | EMN | $75.74 | -1.55 (-2.01%) |
| Celanese | CE | $62.12 | -6.89 (-9.98%) |
| Huntsman | HUN | $15.10 | +0.11 (+0.73%) |

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
