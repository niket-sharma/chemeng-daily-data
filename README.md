# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-10-08)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $91.35 | +3.07 (+3.48%) | $/barrel |
| Brent Crude Oil | $104.12 | +3.92 (+3.91%) | $/barrel |
| Natural Gas | $3.15 | -0.05 (-1.69%) | $/MMBtu |
| Heating Oil | $4.87 | +0.25 (+5.43%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $28.62 | +0.85 (+3.08%) |
| LyondellBasell | LYB | $60.30 | +1.81 (+3.09%) |
| DuPont | DD | $132.31 | +1.23 (+0.94%) |
| Air Products | APD | $278.18 | +0.07 (+0.02%) |
| Linde | LIN | $481.44 | -2.54 (-0.52%) |
| Eastman Chemical | EMN | $63.66 | +0.41 (+0.65%) |
| Celanese | CE | $44.73 | +0.87 (+1.98%) |
| Huntsman | HUN | $8.45 | -0.18 (-2.03%) |

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
