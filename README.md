# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-01-29)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $65.99 | +2.78 (+4.40%) | $/barrel |
| Brent Crude Oil | $70.10 | +1.70 (+2.49%) | $/barrel |
| Natural Gas | $3.85 | -3.61 (-48.43%) | $/MMBtu |
| Heating Oil | $2.49 | -0.18 (-6.63%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $26.98 | -0.80 (-2.88%) |
| LyondellBasell | LYB | $50.68 | +0.21 (+0.42%) |
| DuPont | DD | $44.92 | +0.29 (+0.65%) |
| Air Products | APD | $257.64 | +1.75 (+0.68%) |
| Linde | LIN | $452.85 | +1.35 (+0.30%) |
| Eastman Chemical | EMN | $70.43 | +1.40 (+2.04%) |
| Celanese | CE | $46.18 | +0.01 (+0.02%) |
| Huntsman | HUN | $11.40 | -0.01 (-0.13%) |

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
