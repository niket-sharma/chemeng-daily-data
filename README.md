# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-02-16)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $63.38 | +0.49 (+0.78%) | $/barrel |
| Brent Crude Oil | $68.21 | +0.46 (+0.68%) | $/barrel |
| Natural Gas | $3.04 | -0.20 (-6.20%) | $/MMBtu |
| Heating Oil | $2.31 | -0.07 (-3.12%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $32.49 | -0.16 (-0.49%) |
| LyondellBasell | LYB | $57.61 | -0.17 (-0.29%) |
| DuPont | DD | $50.22 | +0.79 (+1.60%) |
| Air Products | APD | $279.74 | -11.76 (-4.03%) |
| Linde | LIN | $481.00 | +8.14 (+1.72%) |
| Eastman Chemical | EMN | $80.08 | +0.27 (+0.34%) |
| Celanese | CE | $58.85 | +0.03 (+0.05%) |
| Huntsman | HUN | $13.21 | -0.06 (-0.45%) |

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
