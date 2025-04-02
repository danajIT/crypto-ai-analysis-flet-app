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


def news_analysis(client):
    articles = fetch_crypto_news()

    articles_data = "\n".join(
        [
            f"Title: {article['title']}\nSource Domain: {article['source_domain']}"
            for article in articles
        ]
    )

    prompt = f"""
Analyze the following crypto news articles and provide insights based on the following:

- The potential impact of these articles on Bitcoin and Ethereum.
- Key developments for altcoins mentioned in the news.
- A summary of trends in the market based on these articles.

I also need:

Top 5 Important Articles
   - Provide the title, link, and a short 2-3 sentence description.  
   - Assign a sentiment rating (Positive, Neutral, or Negative).  

Cryptocurrencies to Invest In  
   - List 3-5 coins with strong potential based on the news analysis.  

Market Trend Analysis 
   - Indicate if the market is Bullish, Bearish, or Neutral.  
   - Provide a confidence percentage for the trend prediction.

Here are the articles:

{articles_data}

Please ensure that the summary is focused on the impact of the articles on crypto market trends and sentiments.
All of that information i need in json format

### IMPORTANT:
- Your response **MUST** be a valid JSON.
- Do **NOT** include extra explanations or markdown.
- **Only return JSON**, formatted correctly.

### JSON Output Format (Example)
  "summary": "summary what you provide",
  "top_articles": [
      "title": "Title of the article",
      "url": "Direct link to the article",
      "description": "Short summary of the article",
      "sentiment": "Positive/Negative/Neutral"
  ],
  "investment_opportunities": [
    "List of cryptocurrencies recommended for investment"
  ],
  "market_trend":
    "status": "Bullish/Bearish/Neutral",
    "confidence": "Confidence percentage in %"
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
        return {"error": "Invalid JSON response from AI"}

    return response_json


response = news_analysis(client)
