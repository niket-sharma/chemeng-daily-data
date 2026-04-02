# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-04-02)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $105.28 | +5.16 (+5.15%) | $/barrel |
| Brent Crude Oil | $107.36 | +6.20 (+6.13%) | $/barrel |
| Natural Gas | $2.87 | +0.05 (+1.70%) | $/MMBtu |
| Heating Oil | $4.37 | +0.31 (+7.75%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $40.69 | -0.96 (-2.30%) |
| LyondellBasell | LYB | $76.71 | -3.85 (-4.78%) |
| DuPont | DD | $46.21 | +0.41 (+0.90%) |
| Air Products | APD | $289.43 | +0.75 (+0.26%) |
| Linde | LIN | $493.83 | -1.93 (-0.39%) |
| Eastman Chemical | EMN | $75.81 | -0.51 (-0.67%) |
| Celanese | CE | $63.55 | -2.22 (-3.38%) |
| Huntsman | HUN | $13.02 | -0.29 (-2.18%) |

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
