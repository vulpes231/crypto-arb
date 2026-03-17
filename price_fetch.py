import requests

def get_binance_price():
    try:
        url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
        response = requests.get(url).json()
        return float(response["price"])
    except Exception as e:
        print("Binance fetch error:", e)
        return None

def get_kucoin_price():
    try:
        url = "https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=BTC-USDT"
        response = requests.get(url).json()
        return float(response["data"]["price"])
    except Exception as e:
        print("KuCoin fetch error:", e)
        return None