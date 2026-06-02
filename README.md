# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-06-02)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $91.59 | -0.57 (-0.62%) | $/barrel |
| Brent Crude Oil | $94.64 | -0.34 (-0.36%) | $/barrel |
| Natural Gas | $3.15 | -0.03 (-1.04%) | $/MMBtu |
| Heating Oil | $3.67 | +0.03 (+0.82%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $34.49 | -0.20 (-0.58%) |
| LyondellBasell | LYB | $67.12 | -0.02 (-0.03%) |
| DuPont | DD | $49.26 | +1.67 (+3.51%) |
| Air Products | APD | $280.38 | +1.49 (+0.53%) |
| Linde | LIN | $493.03 | -4.38 (-0.88%) |
| Eastman Chemical | EMN | $76.89 | +1.40 (+1.85%) |
| Celanese | CE | $56.35 | +1.07 (+1.94%) |
| Huntsman | HUN | $15.40 | +0.40 (+2.70%) |

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
