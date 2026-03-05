# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-03-05)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $77.38 | +2.72 (+3.64%) | $/barrel |
| Brent Crude Oil | $83.78 | +2.38 (+2.92%) | $/barrel |
| Natural Gas | $2.97 | +0.05 (+1.85%) | $/MMBtu |
| Heating Oil | $2.88 | -0.42 (-12.61%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $32.34 | +1.60 (+5.20%) |
| LyondellBasell | LYB | $61.92 | +3.71 (+6.37%) |
| DuPont | DD | $48.08 | -0.19 (-0.39%) |
| Air Products | APD | $274.20 | +1.16 (+0.42%) |
| Linde | LIN | $499.19 | -2.49 (-0.50%) |
| Eastman Chemical | EMN | $73.45 | -0.71 (-0.96%) |
| Celanese | CE | $51.15 | -0.17 (-0.33%) |
| Huntsman | HUN | $12.89 | +0.51 (+4.12%) |

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
