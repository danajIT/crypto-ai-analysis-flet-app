import requests
import os
from dotenv import load_dotenv

load_dotenv()

CMC_API_KEY = os.getenv("COIN_MARKET_CAP_API_KEY")


def fetch_crypto_prices(symbols=["BTC", "ETH", "SOL"]):
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"

    params = {"symbol": ",".join(symbols)}

    headers = {"X-CMC_PRO_API_KEY": CMC_API_KEY, "Accepts": "application/json"}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json().get("data", {})

        prices = []
        for symbol in symbols:
            quote = data[symbol]["quote"]["USD"]
            prices.append(
                {
                    "symbol": symbol,
                    "price": round(quote["price"], 2),
                    "change_7h": round(quote["percent_change_7d"], 2),
                }
            )

        return prices

    except requests.exceptions.RequestException as e:
        print(f"Error fetching crypto prices: {e}")
        return None
