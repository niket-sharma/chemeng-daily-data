# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-11-24)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $81.60 | +1.43 (+1.78%) | $/barrel |
| Brent Crude Oil | $88.38 | -0.99 (-1.11%) | $/barrel |
| Natural Gas | $3.68 | +0.50 (+15.61%) | $/MMBtu |
| Heating Oil | $3.65 | -0.05 (-1.30%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $28.95 | +0.35 (+1.22%) |
| LyondellBasell | LYB | $55.62 | +0.88 (+1.61%) |
| DuPont | DD | $150.71 | -0.54 (-0.36%) |
| Air Products | APD | $308.58 | +4.40 (+1.45%) |
| Linde | LIN | $516.83 | -0.17 (-0.03%) |
| Eastman Chemical | EMN | $60.74 | +0.09 (+0.15%) |
| Celanese | CE | $44.36 | -0.86 (-1.90%) |
| Huntsman | HUN | $8.75 | +0.21 (+2.46%) |

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
