# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-11-12)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $89.02 | +2.49 (+2.88%) | $/barrel |
| Brent Crude Oil | $96.13 | +3.37 (+3.63%) | $/barrel |
| Natural Gas | $3.34 | +0.12 (+3.83%) | $/MMBtu |
| Heating Oil | $4.30 | +0.09 (+2.11%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $33.15 | +0.61 (+1.87%) |
| LyondellBasell | LYB | $63.87 | +1.29 (+2.06%) |
| DuPont | DD | $154.74 | -0.87 (-0.56%) |
| Air Products | APD | $316.18 | +1.00 (+0.32%) |
| Linde | LIN | $522.49 | -4.06 (-0.77%) |
| Eastman Chemical | EMN | $65.60 | -0.91 (-1.37%) |
| Celanese | CE | $51.27 | -0.18 (-0.35%) |
| Huntsman | HUN | $9.64 | -0.14 (-1.43%) |

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
