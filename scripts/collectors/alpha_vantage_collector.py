#!/usr/bin/env python3
"""
Alpha Vantage API collector for commodity prices.
Free tier: 25 API calls per day.
"""

import os
import requests
from datetime import datetime


API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY', '')
BASE_URL = 'https://www.alphavantage.co/query'


def get_commodity_price(commodity: str) -> dict:
    """
    Fetch daily commodity price from Alpha Vantage.

    Args:
        commodity: One of 'WTI', 'BRENT', 'NATURAL_GAS'

    Returns:
        dict with price data or None if failed
    """
    if not API_KEY:
        print("Warning: ALPHA_VANTAGE_API_KEY not set")
        return None

    params = {
        'function': commodity,
        'interval': 'daily',
        'apikey': API_KEY
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()

        if 'data' in data and len(data['data']) > 0:
            latest = data['data'][0]
            return {
                'date': latest.get('date'),
                'price': float(latest.get('value', 0)),
                'source': 'alpha_vantage'
            }
        elif 'Note' in data:
            print(f"Alpha Vantage API limit reached: {data['Note']}")
            return None
        else:
            print(f"Unexpected response format for {commodity}")
            return None

    except requests.RequestException as e:
        print(f"Error fetching {commodity}: {e}")
        return None


def get_oil_gas_prices() -> dict:
    """
    Fetch all oil and gas commodity prices.

    Returns:
        dict with commodity prices
    """
    commodities = {
        'WTI': 'WTI',
        'BRENT': 'BRENT',
        'NATURAL_GAS': 'NATURAL_GAS'
    }

    prices = {}
    for name, symbol in commodities.items():
        result = get_commodity_price(symbol)
        if result:
            prices[name] = result

    return prices


if __name__ == '__main__':
    # Test the collector
    prices = get_oil_gas_prices()
    print(prices)
