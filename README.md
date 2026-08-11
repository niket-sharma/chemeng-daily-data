# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-08-11)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $82.21 | +0.08 (+0.10%) | $/barrel |
| Brent Crude Oil | $87.88 | +0.16 (+0.18%) | $/barrel |
| Natural Gas | $2.77 | -0.03 (-0.97%) | $/MMBtu |
| Heating Oil | $4.19 | +0.00 (+0.01%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $31.20 | +0.62 (+2.03%) |
| LyondellBasell | LYB | $63.77 | +1.12 (+1.79%) |
| DuPont | DD | $145.41 | +3.86 (+2.73%) |
| Air Products | APD | $310.08 | +1.90 (+0.61%) |
| Linde | LIN | $492.58 | +0.12 (+0.02%) |
| Eastman Chemical | EMN | $74.85 | +1.43 (+1.95%) |
| Celanese | CE | $45.64 | +1.18 (+2.65%) |
| Huntsman | HUN | $10.56 | +0.20 (+1.93%) |

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
