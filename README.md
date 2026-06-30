# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-06-30)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $70.73 | -0.02 (-0.03%) | $/barrel |
| Brent Crude Oil | $74.16 | +1.01 (+1.38%) | $/barrel |
| Natural Gas | $3.30 | +0.12 (+3.74%) | $/MMBtu |
| Heating Oil | $3.24 | -0.09 (-2.78%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $27.51 | -0.41 (-1.45%) |
| LyondellBasell | LYB | $52.92 | -0.70 (-1.31%) |
| DuPont | DD | $136.20 | +0.46 (+0.34%) |
| Air Products | APD | $296.38 | +25.03 (+9.22%) |
| Linde | LIN | $516.55 | +5.49 (+1.08%) |
| Eastman Chemical | EMN | $66.53 | -0.39 (-0.59%) |
| Celanese | CE | $46.09 | +0.16 (+0.35%) |
| Huntsman | HUN | $10.51 | -0.44 (-4.02%) |

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
