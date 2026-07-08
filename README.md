# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-07-08)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $75.77 | +5.33 (+7.57%) | $/barrel |
| Brent Crude Oil | $80.21 | +6.05 (+8.16%) | $/barrel |
| Natural Gas | $3.27 | +0.00 (+0.00%) | $/MMBtu |
| Heating Oil | $3.75 | +0.45 (+13.65%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $29.64 | +1.00 (+3.49%) |
| LyondellBasell | LYB | $56.94 | +2.34 (+4.29%) |
| DuPont | DD | $134.10 | -5.51 (-3.95%) |
| Air Products | APD | $298.68 | -6.37 (-2.09%) |
| Linde | LIN | $529.39 | -8.84 (-1.64%) |
| Eastman Chemical | EMN | $67.54 | -2.08 (-2.99%) |
| Celanese | CE | $47.61 | -1.07 (-2.20%) |
| Huntsman | HUN | $11.56 | +0.59 (+5.42%) |

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
