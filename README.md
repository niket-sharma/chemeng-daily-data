# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-01-31)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $65.21 | -0.21 (-0.32%) | $/barrel |
| Brent Crude Oil | $70.69 | -0.02 (-0.03%) | $/barrel |
| Natural Gas | $4.35 | +0.44 (+11.13%) | $/MMBtu |
| Heating Oil | $2.74 | +0.15 (+5.81%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $27.55 | +0.39 (+1.44%) |
| LyondellBasell | LYB | $49.00 | -0.95 (-1.90%) |
| DuPont | DD | $43.92 | -0.68 (-1.52%) |
| Air Products | APD | $272.50 | +16.48 (+6.44%) |
| Linde | LIN | $456.97 | +1.97 (+0.43%) |
| Eastman Chemical | EMN | $69.32 | +0.33 (+0.48%) |
| Celanese | CE | $44.44 | -1.00 (-2.20%) |
| Huntsman | HUN | $10.82 | -0.36 (-3.22%) |

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
