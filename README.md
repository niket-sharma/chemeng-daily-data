# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-06-03)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $95.24 | +1.48 (+1.58%) | $/barrel |
| Brent Crude Oil | $97.34 | +1.34 (+1.40%) | $/barrel |
| Natural Gas | $3.18 | +0.02 (+0.54%) | $/MMBtu |
| Heating Oil | $3.82 | +0.12 (+3.16%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $35.59 | +0.87 (+2.51%) |
| LyondellBasell | LYB | $68.21 | +0.90 (+1.34%) |
| DuPont | DD | $48.58 | -0.08 (-0.15%) |
| Air Products | APD | $284.13 | +4.84 (+1.73%) |
| Linde | LIN | $509.42 | +13.51 (+2.72%) |
| Eastman Chemical | EMN | $76.43 | -0.24 (-0.31%) |
| Celanese | CE | $56.65 | +1.38 (+2.50%) |
| Huntsman | HUN | $14.86 | -0.13 (-0.87%) |

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
