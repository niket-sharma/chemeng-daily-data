# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-03-19)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $96.84 | +0.52 (+0.54%) | $/barrel |
| Brent Crude Oil | $106.08 | -1.30 (-1.21%) | $/barrel |
| Natural Gas | $3.25 | +0.19 (+6.17%) | $/MMBtu |
| Heating Oil | $4.15 | -0.05 (-1.12%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $38.31 | +0.62 (+1.65%) |
| LyondellBasell | LYB | $76.00 | +0.80 (+1.06%) |
| DuPont | DD | $43.38 | -0.62 (-1.41%) |
| Air Products | APD | $282.10 | +0.67 (+0.24%) |
| Linde | LIN | $485.33 | -3.24 (-0.66%) |
| Eastman Chemical | EMN | $68.35 | -0.56 (-0.81%) |
| Celanese | CE | $59.30 | -0.59 (-0.99%) |
| Huntsman | HUN | $11.48 | -0.48 (-4.01%) |

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
