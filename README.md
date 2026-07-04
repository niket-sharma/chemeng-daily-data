# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-07-04)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $68.78 | +0.09 (+0.13%) | $/barrel |
| Brent Crude Oil | $72.13 | +0.33 (+0.46%) | $/barrel |
| Natural Gas | $3.24 | +0.05 (+1.53%) | $/MMBtu |
| Heating Oil | $3.26 | +0.07 (+2.34%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $27.71 | +0.69 (+2.55%) |
| LyondellBasell | LYB | $53.36 | +0.78 (+1.48%) |
| DuPont | DD | $139.91 | +1.44 (+1.04%) |
| Air Products | APD | $314.19 | +7.79 (+2.54%) |
| Linde | LIN | $546.64 | +13.09 (+2.45%) |
| Eastman Chemical | EMN | $68.86 | +1.77 (+2.64%) |
| Celanese | CE | $47.68 | +2.48 (+5.49%) |
| Huntsman | HUN | $10.82 | +0.27 (+2.56%) |

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
