# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-10-07)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $88.97 | -0.47 (-0.53%) | $/barrel |
| Brent Crude Oil | $101.03 | +0.45 (+0.45%) | $/barrel |
| Natural Gas | $3.21 | +0.09 (+2.95%) | $/MMBtu |
| Heating Oil | $4.68 | +0.11 (+2.39%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $27.86 | -0.30 (-1.05%) |
| LyondellBasell | LYB | $58.54 | -0.39 (-0.65%) |
| DuPont | DD | $130.84 | -2.44 (-1.83%) |
| Air Products | APD | $278.75 | -2.25 (-0.80%) |
| Linde | LIN | $485.08 | -4.87 (-0.99%) |
| Eastman Chemical | EMN | $63.23 | -0.88 (-1.37%) |
| Celanese | CE | $43.90 | -0.95 (-2.12%) |
| Huntsman | HUN | $8.67 | -0.10 (-1.14%) |

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
