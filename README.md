# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-05-01)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $99.50 | -5.57 (-5.30%) | $/barrel |
| Brent Crude Oil | $106.53 | -7.48 (-6.56%) | $/barrel |
| Natural Gas | $2.75 | -0.02 (-0.61%) | $/MMBtu |
| Heating Oil | $3.91 | -0.23 (-5.58%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $39.86 | -0.63 (-1.56%) |
| LyondellBasell | LYB | $73.06 | -1.54 (-2.06%) |
| DuPont | DD | $46.21 | +0.55 (+1.20%) |
| Air Products | APD | $302.73 | +2.68 (+0.89%) |
| Linde | LIN | $516.18 | +15.04 (+3.00%) |
| Eastman Chemical | EMN | $74.94 | +1.86 (+2.54%) |
| Celanese | CE | $67.50 | -0.26 (-0.39%) |
| Huntsman | HUN | $15.21 | +0.84 (+5.85%) |

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
