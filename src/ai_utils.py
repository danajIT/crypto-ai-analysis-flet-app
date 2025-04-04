from openai import OpenAI
from dotenv import load_dotenv
from crypto_news_utils import fetch_crypto_news
import os
import json

load_dotenv()

client = OpenAI(
    base_url=os.getenv("OPENAI_API_ENDPOINT"),
    api_key=os.getenv("OPENAI_API_KEY"),
)


def start_news_analysis(client):
    try:
        articles = fetch_crypto_news()

        if not articles:
            raise ValueError("No articles found for analysis.")

        articles_data = "\n".join(
            [
                f"Title: {article['title']}\nSource Domain: {article['source_domain']}"
                for article in articles
            ]
        )

        prompt = f"""
Analyze the following crypto news articles and other important crypto news and trends, and provide insights based on the following:

1. The potential impact of these articles on Bitcoin and Ethereum.
2. Key developments for altcoins mentioned in the news.
3. A summary of trends in the market based on these articles.

I also need:

**Top 5 Important Articles**
- Provide the title, link, and a short 2-3 sentence description.
- Assign a sentiment rating: "Positive", "Neutral", or "Negative".

**3-5 Cryptocurrencies to Invest In**
- Provide 3 to 5 cryptocurrencies that show strong potential for investment.
- For each coin, include:
  - `name`: The cryptocurrency name and symbol.
  - `price`: The current price in USD.
  - `performance`: Its recent performance percentage (positive or negative, e.g. +5.2% or -3.1%).
  - `signal`: The investment recommendation ("Strong Buy", "Buy", or "Hold").
- If the market is currently unfavorable for investment, return an empty array.

**Market Trend Analysis**
- Indicate if the market is "Bullish", "Bearish", or "Neutral".
- Provide a confidence percentage (e.g. "75%").

Use the following input articles:

{articles_data}

### FORMAT REQUIREMENTS:
- Your response MUST be valid JSON.
- Do NOT include any extra text or markdown — only the raw JSON.
- Always use the exact field names shown below.

### OUTPUT FORMAT (Strict JSON Template):

{{
  "summary": "A concise summary of the impact of the articles on the crypto market, Bitcoin, Ethereum, and altcoins.",
  "top_articles": [
    {{
      "title": "Article Title",
      "url": "https://example.com",
      "description": "2-3 sentence summary of the article.",
      "sentiment": "Positive" | "Neutral" | "Negative"
    }},
    ...
  ],
  "investment_opportunities": [
    {{
      "name": "Bitcoin (BTC)",
      "price": "$65,342.21",
      "performance": "+4.2%",
      "signal": "Buy"
    }},
    ...
  ],
  "market_trend": {{
    "status": "Bullish" | "Bearish" | "Neutral",
    "confidence": "76%"
  }}
}}

### IMPORTANT:
- If **no cryptocurrencies are recommended**, return `"investment_opportunities": []`.
- Use only the listed `signal` and `status` values. Do not invent new ones.
"""

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a financial news analyst."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=700,
            temperature=0.5,
            n=1,
            stop=None,
        )

        try:
            response_json = json.loads(response.choices[0].message.content)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON response from AI.")

        return response_json

    except (ValueError, KeyError, json.JSONDecodeError) as e:
        return {"error": f"An error occurred: {str(e)}"}

    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}
