# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-04-02)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $111.24 | +11.12 (+11.11%) | $/barrel |
| Brent Crude Oil | $108.23 | +7.07 (+6.99%) | $/barrel |
| Natural Gas | $2.79 | -0.03 (-1.17%) | $/MMBtu |
| Heating Oil | $4.47 | +0.41 (+10.08%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $41.42 | +0.73 (+1.79%) |
| LyondellBasell | LYB | $79.65 | +2.94 (+3.84%) |
| DuPont | DD | $45.10 | -1.10 (-2.39%) |
| Air Products | APD | $293.46 | +4.03 (+1.39%) |
| Linde | LIN | $499.09 | +5.26 (+1.07%) |
| Eastman Chemical | EMN | $74.89 | -0.92 (-1.21%) |
| Celanese | CE | $63.40 | -0.15 (-0.24%) |
| Huntsman | HUN | $12.90 | -0.12 (-0.92%) |

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
