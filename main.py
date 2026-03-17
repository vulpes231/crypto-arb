import time
from price_fetch import get_binance_price, get_kucoin_price
from alerts import send_alert
from config import SPREAD_THRESHOLD, LAST_ALERT_TIME, ALERT_COOLDOWN

current_time = time.time()
SYMBOLS = ["BTC", "ETH", "SOL"]

while True:
    for coin in SYMBOLS:
        binance_price = get_binance_price(coin)
        kucoin_price = get_kucoin_price(coin)

        if binance_price and kucoin_price:
            if binance_price < kucoin_price:
                direction = "Buy Binance -> Sell KuCoin"
            else:
                direction = "Buy KuCoin -> Sell Binance"

            spread = round(abs(binance_price - kucoin_price), 2)
            print(f"{coin} | {direction} | Spread: {spread}")

            if spread >= SPREAD_THRESHOLD and current_time - LAST_ALERT_TIME > ALERT_COOLDOWN:
                send_alert(
                    f"$$$ Arbitrage Alert!\n"
                    f"Coin: {coin}\n"
                    f"Binance: {binance_price}\n"
                    f"KuCoin: {kucoin_price}\n"
                    f"Spread: {spread}"
                )
        
            LAST_ALERT_TIME = current_time

    time.sleep(10)