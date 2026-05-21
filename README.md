# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-05-21)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $98.83 | +0.57 (+0.58%) | $/barrel |
| Brent Crude Oil | $105.55 | +0.53 (+0.50%) | $/barrel |
| Natural Gas | $3.03 | +0.02 (+0.77%) | $/MMBtu |
| Heating Oil | $3.83 | -0.11 (-2.89%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $36.27 | -1.47 (-3.90%) |
| LyondellBasell | LYB | $71.30 | -1.74 (-2.38%) |
| DuPont | DD | $47.25 | +0.69 (+1.48%) |
| Air Products | APD | $289.19 | -2.58 (-0.88%) |
| Linde | LIN | $506.63 | +0.56 (+0.11%) |
| Eastman Chemical | EMN | $70.65 | +2.50 (+3.67%) |
| Celanese | CE | $53.50 | +0.01 (+0.02%) |
| Huntsman | HUN | $14.06 | +0.74 (+5.56%) |

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
