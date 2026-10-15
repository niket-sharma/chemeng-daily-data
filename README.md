# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-10-15)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $96.52 | +1.43 (+1.50%) | $/barrel |
| Brent Crude Oil | $105.94 | -0.12 (-0.11%) | $/barrel |
| Natural Gas | $3.22 | +0.03 (+0.84%) | $/MMBtu |
| Heating Oil | $4.69 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $29.69 | +0.50 (+1.73%) |
| LyondellBasell | LYB | $62.52 | +1.35 (+2.21%) |
| DuPont | DD | $129.79 | +1.31 (+1.02%) |
| Air Products | APD | $295.47 | +2.94 (+1.01%) |
| Linde | LIN | $493.61 | +0.91 (+0.18%) |
| Eastman Chemical | EMN | $63.31 | +0.43 (+0.69%) |
| Celanese | CE | $46.26 | +0.44 (+0.96%) |
| Huntsman | HUN | $8.49 | +0.26 (+3.09%) |

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
