# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-05-04)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $101.56 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $108.05 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $2.84 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $3.93 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $40.29 | -0.20 (-0.49%) |
| LyondellBasell | LYB | $74.99 | +0.39 (+0.52%) |
| DuPont | DD | $46.24 | +0.58 (+1.27%) |
| Air Products | APD | $301.07 | +1.02 (+0.34%) |
| Linde | LIN | $507.92 | +6.78 (+1.35%) |
| Eastman Chemical | EMN | $77.53 | +4.44 (+6.07%) |
| Celanese | CE | $69.24 | +1.48 (+2.18%) |
| Huntsman | HUN | $14.63 | +0.26 (+1.81%) |

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
