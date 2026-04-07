# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-04-07)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $116.19 | +3.78 (+3.36%) | $/barrel |
| Brent Crude Oil | $111.67 | +1.90 (+1.73%) | $/barrel |
| Natural Gas | $2.80 | -0.02 (-0.57%) | $/MMBtu |
| Heating Oil | $4.45 | +0.12 (+2.80%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $40.56 | -0.84 (-2.03%) |
| LyondellBasell | LYB | $78.62 | -0.98 (-1.23%) |
| DuPont | DD | $45.57 | +0.09 (+0.20%) |
| Air Products | APD | $294.12 | +0.57 (+0.19%) |
| Linde | LIN | $499.47 | -3.13 (-0.62%) |
| Eastman Chemical | EMN | $73.29 | -1.78 (-2.37%) |
| Celanese | CE | $63.79 | -0.27 (-0.42%) |
| Huntsman | HUN | $12.54 | -0.37 (-2.87%) |

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
