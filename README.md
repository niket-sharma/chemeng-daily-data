# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-09-02)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $91.13 | +0.91 (+1.01%) | $/barrel |
| Brent Crude Oil | $95.85 | +1.20 (+1.27%) | $/barrel |
| Natural Gas | $2.95 | +0.05 (+1.58%) | $/MMBtu |
| Heating Oil | $4.70 | +0.02 (+0.45%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $31.26 | +0.81 (+2.64%) |
| LyondellBasell | LYB | $66.88 | +1.71 (+2.62%) |
| DuPont | DD | $133.05 | +0.94 (+0.72%) |
| Air Products | APD | $309.06 | +3.74 (+1.22%) |
| Linde | LIN | $488.39 | +1.63 (+0.33%) |
| Eastman Chemical | EMN | $72.28 | +2.14 (+3.05%) |
| Celanese | CE | $46.42 | +2.29 (+5.19%) |
| Huntsman | HUN | $9.74 | +0.35 (+3.73%) |

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
