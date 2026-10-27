# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-10-27)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $100.01 | -1.75 (-1.72%) | $/barrel |
| Brent Crude Oil | $109.57 | -6.24 (-5.39%) | $/barrel |
| Natural Gas | $3.01 | +0.40 (+15.53%) | $/MMBtu |
| Heating Oil | $4.61 | -0.30 (-6.20%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $33.83 | -0.16 (-0.46%) |
| LyondellBasell | LYB | $67.33 | -0.01 (-0.02%) |
| DuPont | DD | $137.65 | +1.40 (+1.03%) |
| Air Products | APD | $305.88 | +0.16 (+0.05%) |
| Linde | LIN | $507.00 | -0.56 (-0.11%) |
| Eastman Chemical | EMN | $66.16 | +0.43 (+0.65%) |
| Celanese | CE | $48.51 | +0.43 (+0.89%) |
| Huntsman | HUN | $9.09 | +0.19 (+2.19%) |

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
