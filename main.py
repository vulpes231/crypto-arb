import time
from price_fetch import get_binance_price, get_kucoin_price
from alerts import send_alert
from config import SPREAD_THRESHOLD, last_alert_time, ALERT_COOLDOWN

current_time = time.time()
SYMBOLS = ["BTC", "ETH", "SOL"]

while True:
    for coin in SYMBOLS:
        binance_price = get_binance_price()
        kucoin_price = get_kucoin_price()

        if binance_price and kucoin_price:
            spread = round(abs(binance_price - kucoin_price), 2)
            print(f"Binance: {binance_price} | KuCoin: {kucoin_price} | Spread: {spread}")

            if spread >= SPREAD_THRESHOLD and current_time - last_alert_time > ALERT_COOLDOWN:
                send_alert(
                    f"$$$ Arbitrage Alert!\n"
                    f"Coin: {coin}\n"
                    f"Binance: {binance_price}\n"
                    f"KuCoin: {kucoin_price}\n"
                    f"Spread: {spread}"
                )
        
            last_alert_time = current_time

    time.sleep(10)