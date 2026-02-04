# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-02-04)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $63.18 | -0.03 (-0.05%) | $/barrel |
| Brent Crude Oil | $67.37 | +0.04 (+0.06%) | $/barrel |
| Natural Gas | $3.53 | +0.22 (+6.55%) | $/MMBtu |
| Heating Oil | $2.41 | +0.00 (+0.15%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $32.07 | +1.58 (+5.18%) |
| LyondellBasell | LYB | $56.71 | +3.26 (+6.10%) |
| DuPont | DD | $46.70 | +1.40 (+3.09%) |
| Air Products | APD | $282.15 | +4.19 (+1.51%) |
| Linde | LIN | $468.15 | +4.58 (+0.99%) |
| Eastman Chemical | EMN | $77.85 | +1.95 (+2.57%) |
| Celanese | CE | $51.24 | +3.20 (+6.66%) |
| Huntsman | HUN | $13.24 | +0.26 (+2.00%) |

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
