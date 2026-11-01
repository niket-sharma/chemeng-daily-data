# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-11-01)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $104.12 | +0.00 (+0.00%) | $/barrel |
| Brent Crude Oil | $113.43 | +0.00 (+0.00%) | $/barrel |
| Natural Gas | $2.90 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $4.68 | +0.00 (+0.00%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $34.70 | +1.08 (+3.21%) |
| LyondellBasell | LYB | $68.64 | +3.27 (+5.00%) |
| DuPont | DD | $140.05 | -0.53 (-0.38%) |
| Air Products | APD | $316.43 | +4.68 (+1.50%) |
| Linde | LIN | $514.24 | +11.09 (+2.20%) |
| Eastman Chemical | EMN | $66.53 | -1.40 (-2.06%) |
| Celanese | CE | $49.30 | +0.98 (+2.03%) |
| Huntsman | HUN | $9.64 | +0.67 (+7.47%) |

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
