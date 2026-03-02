# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-03-02)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $71.16 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $77.55 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $2.90 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $2.83 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $30.73 | +1.18 (+3.99%) |
| LyondellBasell | LYB | $57.52 | +1.22 (+2.17%) |
| DuPont | DD | $50.04 | -0.31 (-0.62%) |
| Air Products | APD | $275.67 | -0.56 (-0.20%) |
| Linde | LIN | $508.08 | +9.57 (+1.92%) |
| Eastman Chemical | EMN | $75.51 | +0.29 (+0.39%) |
| Celanese | CE | $49.94 | +0.81 (+1.65%) |
| Huntsman | HUN | $12.65 | +0.68 (+5.68%) |

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
