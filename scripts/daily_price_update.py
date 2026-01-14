#!/usr/bin/env python3
"""
Daily Chemical Commodity Price Update

Main orchestrator that:
1. Fetches prices from all sources (yfinance, FRED, Alpha Vantage)
2. Validates and cleans data
3. Updates JSON files
4. Updates README with latest prices
5. Logs the update
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from collectors.yfinance_collector import get_stock_prices, get_commodity_futures
from collectors.fred_collector import get_fred_prices

# Paths
DATA_DIR = Path(__file__).parent.parent / 'data'
PRICES_DIR = DATA_DIR / 'prices'
LATEST_DIR = DATA_DIR / 'latest'
HISTORICAL_DIR = DATA_DIR / 'historical'
LOG_FILE = Path(__file__).parent.parent / 'logs' / 'update_log.md'
README_FILE = Path(__file__).parent.parent / 'README.md'


def ensure_dirs():
    """Create directories if they don't exist."""
    PRICES_DIR.mkdir(parents=True, exist_ok=True)
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    HISTORICAL_DIR.mkdir(parents=True, exist_ok=True)


def collect_all_prices() -> dict:
    """Collect prices from all available sources."""
    today = datetime.now().strftime('%Y-%m-%d')
    timestamp = datetime.now().isoformat()

    print(f"Collecting prices for {today}...")

    # Collect from yfinance (no API key needed)
    print("  Fetching commodity futures...")
    commodities = get_commodity_futures()

    print("  Fetching chemical stocks...")
    stocks = get_stock_prices()

    # Collect from FRED (requires API key)
    print("  Fetching FRED data...")
    fred_data = get_fred_prices()

    return {
        'date': today,
        'timestamp': timestamp,
        'energy': commodities,
        'stocks': stocks,
        'fred': fred_data
    }


def save_latest(prices: dict):
    """Save latest prices to JSON."""
    filepath = LATEST_DIR / 'latest_prices.json'
    with open(filepath, 'w') as f:
        json.dump(prices, f, indent=2)
    print(f"  Saved latest prices to {filepath}")


def append_historical(prices: dict):
    """Append to historical price files."""
    today = datetime.now()
    month_dir = HISTORICAL_DIR / today.strftime('%Y-%m')
    month_dir.mkdir(exist_ok=True)

    filepath = month_dir / f"prices_{prices['date']}.json"
    with open(filepath, 'w') as f:
        json.dump(prices, f, indent=2)
    print(f"  Saved historical data to {filepath}")

    # Also append to category-specific files
    for category in ['energy', 'stocks']:
        if category in prices and prices[category]:
            category_file = PRICES_DIR / f"{category}.json"
            if category_file.exists():
                with open(category_file, 'r') as f:
                    history = json.load(f)
            else:
                history = []

            history.append({
                'date': prices['date'],
                'data': prices[category]
            })

            # Keep last 365 days
            history = history[-365:]

            with open(category_file, 'w') as f:
                json.dump(history, f, indent=2)


def update_readme(prices: dict):
    """Update README with latest prices."""
    date = prices['date']

    # Build energy table
    energy_rows = []
    for key, data in prices.get('energy', {}).items():
        change_str = f"{data['change_1d']:+.2f} ({data['change_pct']:+.2f}%)"
        energy_rows.append(
            f"| {data['name']} | ${data['price']:.2f} | {change_str} | {data['unit']} |"
        )

    # Build stocks table
    stock_rows = []
    for symbol, data in prices.get('stocks', {}).items():
        change_str = f"{data['change_1d']:+.2f} ({data['change_pct']:+.2f}%)"
        stock_rows.append(
            f"| {data['name']} | {symbol} | ${data['price']:.2f} | {change_str} |"
        )

    readme_content = f"""# Chemical Commodity Price Tracker

Automated daily tracking of chemical commodity prices and chemical company stocks.

## Latest Prices (Updated: {date})

### Energy Commodities

| Commodity | Price | Change (24h) | Unit |
|-----------|-------|--------------|------|
{chr(10).join(energy_rows) if energy_rows else "| No data available | - | - | - |"}

### Chemical Company Stocks

| Company | Ticker | Price | Change (24h) |
|---------|--------|-------|--------------|
{chr(10).join(stock_rows) if stock_rows else "| No data available | - | - | - |"}

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
"""

    with open(README_FILE, 'w') as f:
        f.write(readme_content)
    print(f"  Updated README.md")


def log_update(prices: dict):
    """Log the update."""
    today = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    energy_count = len(prices.get('energy', {}))
    stock_count = len(prices.get('stocks', {}))
    fred_count = len(prices.get('fred', {}))

    log_entry = f"- **{today}**: Updated {energy_count} energy prices, {stock_count} stocks, {fred_count} FRED series\n"

    # Ensure log file exists
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not LOG_FILE.exists():
        with open(LOG_FILE, 'w') as f:
            f.write("# Price Update Log\n\n")

    with open(LOG_FILE, 'a') as f:
        f.write(log_entry)

    print(f"  Logged update")


def main():
    print("=" * 50)
    print("Chemical Commodity Price Update")
    print("=" * 50)

    ensure_dirs()

    # Collect all prices
    prices = collect_all_prices()

    # Check if we got any data
    total_items = (
        len(prices.get('energy', {})) +
        len(prices.get('stocks', {})) +
        len(prices.get('fred', {}))
    )

    if total_items == 0:
        print("\nNo price data collected. Check your internet connection.")
        return

    print(f"\nCollected {total_items} data points")

    # Save data
    print("\nSaving data...")
    save_latest(prices)
    append_historical(prices)
    update_readme(prices)
    log_update(prices)

    print("\nUpdate complete!")
    print("=" * 50)


if __name__ == '__main__':
    main()
