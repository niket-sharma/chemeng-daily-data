# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-06-11)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $89.97 | -0.06 (-0.07%) | $/barrel |
| Brent Crude Oil | $92.56 | -0.54 (-0.58%) | $/barrel |
| Natural Gas | $3.07 | -0.11 (-3.58%) | $/MMBtu |
| Heating Oil | $3.58 | -0.03 (-0.96%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $34.76 | +0.51 (+1.50%) |
| LyondellBasell | LYB | $66.39 | +1.24 (+1.90%) |
| DuPont | DD | $45.45 | +0.39 (+0.87%) |
| Air Products | APD | $278.86 | +2.35 (+0.85%) |
| Linde | LIN | $513.49 | +4.33 (+0.85%) |
| Eastman Chemical | EMN | $72.07 | +0.73 (+1.02%) |
| Celanese | CE | $51.34 | +0.96 (+1.91%) |
| Huntsman | HUN | $14.68 | +0.45 (+3.16%) |

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
