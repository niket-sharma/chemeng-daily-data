# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-05-11)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $97.52 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $103.72 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $2.88 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $3.91 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $38.07 | +1.20 (+3.25%) |
| LyondellBasell | LYB | $72.57 | +0.81 (+1.12%) |
| DuPont | DD | $50.47 | +0.71 (+1.43%) |
| Air Products | APD | $302.76 | +7.35 (+2.49%) |
| Linde | LIN | $499.84 | +6.68 (+1.35%) |
| Eastman Chemical | EMN | $74.10 | +0.44 (+0.60%) |
| Celanese | CE | $58.80 | +1.63 (+2.85%) |
| Huntsman | HUN | $15.03 | +0.07 (+0.50%) |

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
