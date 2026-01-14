#!/usr/bin/env python3
"""
FRED (Federal Reserve Economic Data) collector.
Provides official government data on energy prices and economic indicators.
"""

import os
from datetime import datetime, timedelta

try:
    from fredapi import Fred
    FRED_AVAILABLE = True
except ImportError:
    FRED_AVAILABLE = False


API_KEY = os.getenv('FRED_API_KEY', '')

# FRED series IDs for chemical industry relevant data
FRED_SERIES = {
    'DHHNGSP': {
        'name': 'Natural Gas (Henry Hub)',
        'unit': '$/MMBtu',
        'frequency': 'daily'
    },
    'DCOILWTICO': {
        'name': 'WTI Crude Oil',
        'unit': '$/barrel',
        'frequency': 'daily'
    },
    'DCOILBRENTEU': {
        'name': 'Brent Crude Oil',
        'unit': '$/barrel',
        'frequency': 'daily'
    },
    'GASREGW': {
        'name': 'Regular Gasoline Price',
        'unit': '$/gallon',
        'frequency': 'weekly'
    },
    'PCU325325': {
        'name': 'PPI: Chemical Manufacturing',
        'unit': 'index',
        'frequency': 'monthly'
    },
}


def get_fred_prices() -> dict:
    """
    Fetch prices from FRED API.

    Returns:
        dict with FRED series data
    """
    if not FRED_AVAILABLE:
        print("Warning: fredapi not installed")
        return {}

    if not API_KEY:
        print("Warning: FRED_API_KEY not set")
        return {}

    try:
        fred = Fred(api_key=API_KEY)
    except Exception as e:
        print(f"Error initializing FRED client: {e}")
        return {}

    prices = {}
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)  # Get last week of data

    for series_id, info in FRED_SERIES.items():
        try:
            data = fred.get_series(
                series_id,
                observation_start=start_date,
                observation_end=end_date
            )

            if len(data) > 0:
                # Get the most recent non-null value
                latest = data.dropna().iloc[-1]
                prev = data.dropna().iloc[-2] if len(data.dropna()) >= 2 else latest

                change = latest - prev
                change_pct = (change / prev * 100) if prev != 0 else 0

                key = info['name'].replace(' ', '_').replace(':', '').lower()
                prices[key] = {
                    'name': info['name'],
                    'price': round(float(latest), 2),
                    'unit': info['unit'],
                    'change_1d': round(float(change), 2),
                    'change_pct': round(float(change_pct), 2),
                    'date': str(data.dropna().index[-1].date()),
                    'source': 'fred',
                    'series_id': series_id
                }

        except Exception as e:
            print(f"Error fetching FRED series {series_id}: {e}")

    return prices


if __name__ == '__main__':
    # Test the collector
    prices = get_fred_prices()
    for key, data in prices.items():
        print(f"{data['name']}: ${data['price']} {data['unit']} ({data['change_pct']:+.2f}%)")
