# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: 2026-04-07)

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
| WTI Crude Oil | $116.76 | +4.35 (+3.87%) | $/barrel |
| Brent Crude Oil | $110.57 | +0.80 (+0.73%) | $/barrel |
| Natural Gas | $2.87 | +0.06 (+2.24%) | $/MMBtu |
| Heating Oil | $4.40 | +0.07 (+1.66%) | $/gallon |

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
| Dow Inc. | DOW | $41.99 | +1.43 (+3.53%) |
| LyondellBasell | LYB | $81.61 | +2.99 (+3.80%) |
| DuPont | DD | $45.37 | -0.20 (-0.44%) |
| Air Products | APD | $295.71 | +1.60 (+0.54%) |
| Linde | LIN | $495.57 | -3.90 (-0.78%) |
| Eastman Chemical | EMN | $74.83 | +1.54 (+2.11%) |
| Celanese | CE | $64.95 | +1.16 (+1.82%) |
| Huntsman | HUN | $13.20 | +0.66 (+5.26%) |

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
