import requests

def get_binance_price(symbol):
    try:
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}USDT"
        response = requests.get(url).json()
        return float(response["price"])
    except Exception as e:
        print("Binance fetch error:", e)
        return None

def get_kucoin_price(symbol):
    try:
        url = f"https://api.kucoin.com/api/v1/market/orderbook/level1?symbol={symbol}-USDT"
        response = requests.get(url).json()
        return float(response["data"]["price"])
    except Exception as e:
        print("KuCoin fetch error:", e)
        return None