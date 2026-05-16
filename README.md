# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-05-16)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $105.42 | +4.25 (+4.20%) | $/barrel |
| Brent Crude Oil | $109.26 | +3.54 (+3.35%) | $/barrel |
| Natural Gas | $2.96 | +0.07 (+2.28%) | $/MMBtu |
| Heating Oil | $4.05 | +0.15 (+3.78%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $38.75 | -0.03 (-0.08%) |
| LyondellBasell | LYB | $75.06 | +1.79 (+2.44%) |
| DuPont | DD | $49.31 | -1.09 (-2.16%) |
| Air Products | APD | $295.38 | -4.49 (-1.50%) |
| Linde | LIN | $506.11 | -5.54 (-1.08%) |
| Eastman Chemical | EMN | $71.58 | -0.89 (-1.23%) |
| Celanese | CE | $56.80 | -0.53 (-0.92%) |
| Huntsman | HUN | $13.70 | -0.61 (-4.26%) |

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
