# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-08-04)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $75.60 | -4.74 (-5.90%) | $/barrel |
| Brent Crude Oil | $79.14 | -4.63 (-5.53%) | $/barrel |
| Natural Gas | $2.67 | -0.11 (-4.10%) | $/MMBtu |
| Heating Oil | $3.78 | -0.10 (-2.58%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $29.83 | -0.06 (-0.18%) |
| LyondellBasell | LYB | $60.05 | -0.57 (-0.94%) |
| DuPont | DD | $139.58 | -1.70 (-1.20%) |
| Air Products | APD | $295.35 | +2.40 (+0.82%) |
| Linde | LIN | $484.21 | +3.76 (+0.78%) |
| Eastman Chemical | EMN | $73.06 | +1.08 (+1.50%) |
| Celanese | CE | $44.97 | +1.08 (+2.45%) |
| Huntsman | HUN | $10.19 | +0.17 (+1.70%) |

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
