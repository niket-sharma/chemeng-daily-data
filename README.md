# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-01-22)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $59.89 | -0.73 (-1.20%) | $/barrel |
| Brent Crude Oil | $64.48 | -0.76 (-1.16%) | $/barrel |
| Natural Gas | $5.33 | +0.46 (+9.42%) | $/MMBtu |
| Heating Oil | $2.34 | -0.09 (-3.81%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $28.41 | +1.83 (+6.88%) |
| LyondellBasell | LYB | $51.82 | +2.96 (+6.06%) |
| DuPont | DD | $43.38 | +1.10 (+2.60%) |
| Air Products | APD | $263.11 | +4.93 (+1.91%) |
| Linde | LIN | $439.35 | +6.20 (+1.43%) |
| Eastman Chemical | EMN | $68.30 | +2.11 (+3.19%) |
| Celanese | CE | $48.12 | +3.89 (+8.79%) |
| Huntsman | HUN | $12.00 | +0.70 (+6.19%) |

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
