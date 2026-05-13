# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-05-13)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $103.05 | +0.87 (+0.85%) | $/barrel |
| Brent Crude Oil | $107.58 | -0.19 (-0.18%) | $/barrel |
| Natural Gas | $2.88 | +0.03 (+1.13%) | $/MMBtu |
| Heating Oil | $4.07 | -0.09 (-2.23%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $39.96 | +0.53 (+1.34%) |
| LyondellBasell | LYB | $74.95 | +0.64 (+0.86%) |
| DuPont | DD | $50.88 | +0.34 (+0.67%) |
| Air Products | APD | $306.73 | +3.13 (+1.03%) |
| Linde | LIN | $508.37 | +4.50 (+0.89%) |
| Eastman Chemical | EMN | $74.45 | +0.21 (+0.28%) |
| Celanese | CE | $59.86 | +0.39 (+0.66%) |
| Huntsman | HUN | $14.85 | +0.47 (+3.27%) |

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
