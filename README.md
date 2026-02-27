# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-02-27)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $67.53 | +2.32 (+3.56%) | $/barrel |
| Brent Crude Oil | $73.28 | +2.53 (+3.58%) | $/barrel |
| Natural Gas | $2.88 | +0.05 (+1.80%) | $/MMBtu |
| Heating Oil | $2.61 | -0.01 (-0.23%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $29.51 | -0.39 (-1.29%) |
| LyondellBasell | LYB | $56.40 | +0.10 (+0.19%) |
| DuPont | DD | $49.87 | -0.48 (-0.95%) |
| Air Products | APD | $275.81 | -0.42 (-0.15%) |
| Linde | LIN | $500.98 | +2.47 (+0.50%) |
| Eastman Chemical | EMN | $74.57 | -0.65 (-0.87%) |
| Celanese | CE | $48.33 | -0.80 (-1.63%) |
| Huntsman | HUN | $11.94 | -0.03 (-0.29%) |

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
