# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-03-12)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $94.68 | +7.43 (+8.52%) | $/barrel |
| Brent Crude Oil | $95.50 | +3.52 (+3.83%) | $/barrel |
| Natural Gas | $3.21 | +0.01 (+0.19%) | $/MMBtu |
| Heating Oil | $3.36 | -0.32 (-8.63%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $36.87 | +2.50 (+7.27%) |
| LyondellBasell | LYB | $70.57 | +3.20 (+4.75%) |
| DuPont | DD | $45.38 | -0.61 (-1.33%) |
| Air Products | APD | $285.28 | +7.59 (+2.73%) |
| Linde | LIN | $488.23 | +6.68 (+1.39%) |
| Eastman Chemical | EMN | $66.88 | -0.84 (-1.24%) |
| Celanese | CE | $55.97 | +4.03 (+7.77%) |
| Huntsman | HUN | $11.95 | +0.20 (+1.70%) |

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
