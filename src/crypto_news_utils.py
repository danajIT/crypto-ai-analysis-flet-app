import requests
import os
from dotenv import load_dotenv

load_dotenv()

CRYPTO_PANIC_API_KEY = os.getenv("CRYPTO_PANIC_API_KEY")


def fetch_crypto_news():
    url = "https://cryptopanic.com/api/v1/posts/"

    params = {
        "auth_token": CRYPTO_PANIC_API_KEY,
        "filter": "hot",
        "languages": "en",
        "page_size": 1,
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        articles = response.json().get("results", [])

        news = []
        for article in articles:
            news.append(
                {
                    "title": article.get("title"),
                    "source_domain": article["source"]["domain"],
                }
            )
        return news
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")
        return None
