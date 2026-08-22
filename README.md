# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-08-22)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $87.06 | -0.77 (-0.88%) | $/barrel |
| Brent Crude Oil | $94.39 | +0.61 (+0.65%) | $/barrel |
| Natural Gas | $2.77 | +0.04 (+1.46%) | $/MMBtu |
| Heating Oil | $4.49 | +0.01 (+0.32%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $32.35 | -0.55 (-1.67%) |
| LyondellBasell | LYB | $67.53 | -0.57 (-0.84%) |
| DuPont | DD | $138.33 | -0.13 (-0.09%) |
| Air Products | APD | $305.10 | +4.77 (+1.59%) |
| Linde | LIN | $487.57 | +6.28 (+1.30%) |
| Eastman Chemical | EMN | $74.09 | +0.30 (+0.41%) |
| Celanese | CE | $46.80 | -0.18 (-0.38%) |
| Huntsman | HUN | $9.97 | -0.19 (-1.87%) |

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
