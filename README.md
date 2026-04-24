# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-04-24)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $95.01 | -0.84 (-0.88%) | $/barrel |
| Brent Crude Oil | $98.94 | -6.13 (-5.83%) | $/barrel |
| Natural Gas | $2.68 | +0.07 (+2.56%) | $/MMBtu |
| Heating Oil | $3.86 | -0.13 (-3.16%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $38.59 | +0.06 (+0.16%) |
| LyondellBasell | LYB | $70.67 | -0.05 (-0.07%) |
| DuPont | DD | $46.11 | -0.26 (-0.56%) |
| Air Products | APD | $304.14 | +0.49 (+0.16%) |
| Linde | LIN | $507.43 | -0.63 (-0.12%) |
| Eastman Chemical | EMN | $72.38 | +0.46 (+0.63%) |
| Celanese | CE | $65.68 | +0.45 (+0.69%) |
| Huntsman | HUN | $13.71 | +0.16 (+1.18%) |

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
