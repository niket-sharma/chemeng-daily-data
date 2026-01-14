#!/usr/bin/env python3
"""
Yahoo Finance collector for stock and commodity prices.
No API key required - uses yfinance library.
"""

import yfinance as yf
from datetime import datetime, timedelta


# Chemical company tickers
CHEMICAL_STOCKS = {
    'DOW': 'Dow Inc.',
    'LYB': 'LyondellBasell',
    'DD': 'DuPont',
    'APD': 'Air Products',
    'LIN': 'Linde',
    'EMN': 'Eastman Chemical',
    'CE': 'Celanese',
    'HUN': 'Huntsman',
}

# Commodity futures
COMMODITY_FUTURES = {
    'CL=F': {'name': 'WTI Crude Oil', 'unit': '$/barrel'},
    'BZ=F': {'name': 'Brent Crude Oil', 'unit': '$/barrel'},
    'NG=F': {'name': 'Natural Gas', 'unit': '$/MMBtu'},
    'HO=F': {'name': 'Heating Oil', 'unit': '$/gallon'},
}


def get_stock_prices() -> dict:
    """
    Fetch chemical company stock prices.

    Returns:
        dict with stock prices and changes
    """
    prices = {}

    for symbol, name in CHEMICAL_STOCKS.items():
        try:
            ticker = yf.Ticker(symbol)
            hist = ticker.history(period='2d')

            if len(hist) >= 1:
                latest_close = hist['Close'].iloc[-1]
                prev_close = hist['Close'].iloc[-2] if len(hist) >= 2 else latest_close
                change = latest_close - prev_close
                change_pct = (change / prev_close * 100) if prev_close != 0 else 0

                prices[symbol] = {
                    'name': name,
                    'price': round(latest_close, 2),
                    'change_1d': round(change, 2),
                    'change_pct': round(change_pct, 2),
                    'source': 'yfinance'
                }
        except Exception as e:
            print(f"Error fetching {symbol}: {e}")

    return prices


def get_commodity_futures() -> dict:
    """
    Fetch commodity futures prices.

    Returns:
        dict with commodity futures prices
    """
    prices = {}

    for symbol, info in COMMODITY_FUTURES.items():
        try:
            ticker = yf.Ticker(symbol)
            hist = ticker.history(period='2d')

            if len(hist) >= 1:
                latest_close = hist['Close'].iloc[-1]
                prev_close = hist['Close'].iloc[-2] if len(hist) >= 2 else latest_close
                change = latest_close - prev_close
                change_pct = (change / prev_close * 100) if prev_close != 0 else 0

                prices[info['name'].replace(' ', '_').lower()] = {
                    'name': info['name'],
                    'price': round(latest_close, 2),
                    'unit': info['unit'],
                    'change_1d': round(change, 2),
                    'change_pct': round(change_pct, 2),
                    'source': 'yfinance'
                }
        except Exception as e:
            print(f"Error fetching {symbol}: {e}")

    return prices


if __name__ == '__main__':
    # Test the collectors
    print("Stock prices:")
    stocks = get_stock_prices()
    for symbol, data in stocks.items():
        print(f"  {symbol}: ${data['price']} ({data['change_pct']:+.2f}%)")

    print("\nCommodity futures:")
    commodities = get_commodity_futures()
    for key, data in commodities.items():
        print(f"  {data['name']}: ${data['price']} {data['unit']} ({data['change_pct']:+.2f}%)")
