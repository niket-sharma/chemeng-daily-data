# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-04-29)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $105.03 | +5.10 (+5.10%) | $/barrel |
| Brent Crude Oil | $109.47 | -1.79 (-1.61%) | $/barrel |
| Natural Gas | $2.65 | +0.09 (+3.56%) | $/MMBtu |
| Heating Oil | $4.06 | +0.09 (+2.30%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $39.06 | +1.05 (+2.76%) |
| LyondellBasell | LYB | $72.90 | +1.42 (+1.99%) |
| DuPont | DD | $45.15 | -0.18 (-0.40%) |
| Air Products | APD | $301.82 | -1.53 (-0.50%) |
| Linde | LIN | $504.42 | -5.88 (-1.15%) |
| Eastman Chemical | EMN | $71.33 | -0.30 (-0.42%) |
| Celanese | CE | $66.25 | +1.60 (+2.48%) |
| Huntsman | HUN | $13.71 | +0.05 (+0.37%) |

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
