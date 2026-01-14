#!/usr/bin/env python3
"""
Generate price visualizations for the chemical commodity tracker.
"""

import json
from datetime import datetime
from pathlib import Path

try:
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    import pandas as pd
    PLOTTING_AVAILABLE = True
except ImportError:
    PLOTTING_AVAILABLE = False
    print("Warning: matplotlib/pandas not installed, skipping visualizations")

# Paths
DATA_DIR = Path(__file__).parent.parent / 'data'
PRICES_DIR = DATA_DIR / 'prices'
VIZ_DIR = Path(__file__).parent.parent / 'visualizations'


def load_price_history(category: str) -> list:
    """Load historical price data for a category."""
    filepath = PRICES_DIR / f"{category}.json"
    if filepath.exists():
        with open(filepath, 'r') as f:
            return json.load(f)
    return []


def create_energy_chart():
    """Create energy price trend chart."""
    if not PLOTTING_AVAILABLE:
        return

    history = load_price_history('energy')
    if len(history) < 2:
        print("  Not enough energy data for chart (need at least 2 days)")
        return

    # Prepare data
    dates = []
    wti_prices = []
    brent_prices = []
    ng_prices = []

    for entry in history:
        dates.append(datetime.strptime(entry['date'], '%Y-%m-%d'))
        data = entry['data']

        wti_prices.append(data.get('wti_crude_oil', {}).get('price'))
        brent_prices.append(data.get('brent_crude_oil', {}).get('price'))
        ng_prices.append(data.get('natural_gas', {}).get('price'))

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    # Oil prices
    if any(wti_prices):
        ax1.plot(dates, wti_prices, 'b-', label='WTI Crude', linewidth=2)
    if any(brent_prices):
        ax1.plot(dates, brent_prices, 'r-', label='Brent Crude', linewidth=2)

    ax1.set_ylabel('Price ($/barrel)')
    ax1.set_title('Crude Oil Prices')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Natural gas prices
    if any(ng_prices):
        ax2.plot(dates, ng_prices, 'g-', label='Natural Gas', linewidth=2)

    ax2.set_ylabel('Price ($/MMBtu)')
    ax2.set_xlabel('Date')
    ax2.set_title('Natural Gas Prices')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    # Format x-axis
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax2.xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.xticks(rotation=45)

    plt.tight_layout()

    VIZ_DIR.mkdir(exist_ok=True)
    filepath = VIZ_DIR / 'energy_prices.png'
    plt.savefig(filepath, dpi=150)
    plt.close()
    print(f"  Saved energy chart to {filepath}")


def create_stocks_chart():
    """Create chemical stocks performance chart."""
    if not PLOTTING_AVAILABLE:
        return

    history = load_price_history('stocks')
    if len(history) < 2:
        print("  Not enough stock data for chart (need at least 2 days)")
        return

    # Get unique stock symbols
    all_symbols = set()
    for entry in history:
        all_symbols.update(entry['data'].keys())

    # Prepare data
    dates = [datetime.strptime(entry['date'], '%Y-%m-%d') for entry in history]

    fig, ax = plt.subplots(figsize=(12, 6))

    colors = plt.cm.tab10.colors
    for i, symbol in enumerate(sorted(all_symbols)):
        prices = []
        for entry in history:
            price = entry['data'].get(symbol, {}).get('price')
            prices.append(price)

        if any(prices):
            ax.plot(dates, prices, color=colors[i % len(colors)],
                   label=symbol, linewidth=1.5)

    ax.set_xlabel('Date')
    ax.set_ylabel('Stock Price ($)')
    ax.set_title('Chemical Company Stock Prices')
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.grid(True, alpha=0.3)

    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax.xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.xticks(rotation=45)

    plt.tight_layout()

    VIZ_DIR.mkdir(exist_ok=True)
    filepath = VIZ_DIR / 'stock_prices.png'
    plt.savefig(filepath, dpi=150)
    plt.close()
    print(f"  Saved stock chart to {filepath}")


def main():
    print("Generating visualizations...")

    VIZ_DIR.mkdir(exist_ok=True)

    create_energy_chart()
    create_stocks_chart()

    print("Visualization generation complete!")


if __name__ == '__main__':
    main()
