# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-03-25)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $88.56 | -3.79 (-4.10%) | $/barrel |
| Brent Crude Oil | $99.26 | -5.23 (-5.01%) | $/barrel |
| Natural Gas | $2.84 | -0.11 (-3.64%) | $/MMBtu |
| Heating Oil | $3.78 | -0.51 (-11.96%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $38.31 | +2.27 (+6.30%) |
| LyondellBasell | LYB | $76.01 | +4.54 (+6.35%) |
| DuPont | DD | $45.33 | +1.19 (+2.70%) |
| Air Products | APD | $286.25 | +7.59 (+2.72%) |
| Linde | LIN | $479.84 | +1.79 (+0.37%) |
| Eastman Chemical | EMN | $69.95 | +1.94 (+2.85%) |
| Celanese | CE | $60.80 | +4.67 (+8.32%) |
| Huntsman | HUN | $11.41 | +0.58 (+5.36%) |

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
