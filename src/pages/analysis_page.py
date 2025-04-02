import flet as ft


def analysis_page(page):
    # analysis_data = page.data
    analysis_data = {
        "summary": "The articles highlight significant developments in the cryptocurrency market, including institutional adoption, regulatory advancements, and technological upgrades. Bitcoin and Ethereum remain central to these narratives, with Bitcoin seeing increased institutional interest and Ethereum progressing in its technological roadmap. Altcoins like Cardano, XRP, and Cosmos are also making strides in adoption and interoperability. Overall, the market sentiment leans towards cautious optimism with a mix of bullish and neutral trends.",
        "top_articles": [
            {
                "title": "GameStop Completes $1.5 Billion Offering to Fund Bitcoin Reserve",
                "url": "https://decrypt.co",
                "description": "GameStop has raised $1.5 billion to establish a Bitcoin reserve, signaling increased institutional interest in Bitcoin as a store of value.",
                "sentiment": "Positive",
            },
            {
                "title": "Mastercard Plans to Enable 3.5 Billion Cardholders to Transact with Bitcoin ($BTC) and Crypto",
                "url": "https://thedefiant.io",
                "description": "Mastercard's initiative to integrate crypto transactions for its global user base could significantly boost mainstream adoption of Bitcoin and other cryptocurrencies.",
                "sentiment": "Positive",
            },
            {
                "title": "Ethereum edges closer to deploying Pectra on mainnet with successful upgrade on Hoodi testnet",
                "url": "https://theblock.co",
                "description": "Ethereum's Pectra upgrade demonstrates progress in its technological evolution, potentially enhancing its scalability and utility.",
                "sentiment": "Positive",
            },
            {
                "title": "Cardano (ADA) Achieves New Coinbase Listing, and It's Both Institutional and Retail",
                "url": "https://u.today",
                "description": "Cardano's inclusion on Coinbase for both institutional and retail trading highlights its growing acceptance and potential for price appreciation.",
                "sentiment": "Positive",
            },
            {
                "title": "BlackRock's Larry Fink: U.S. Dollar risks losing global reserve status to Bitcoin if U.S. doesn't get debt under control.",
                "url": "https://BTC_Archive",
                "description": "BlackRock's CEO underscores Bitcoin's potential as a global reserve asset amidst concerns over U.S. fiscal policy, reflecting a bullish outlook for BTC.",
                "sentiment": "Positive",
            },
        ],
        "investment_opportunities": [
            "Bitcoin (BTC)",
            "Ethereum (ETH)",
            "Cardano (ADA)",
            "Cosmos (ATOM)",
            "Ripple (XRP)",
        ],
        "market_trend": {"status": "Bullish", "confidence": "75%"},
    }

    if "error" in analysis_data:
        page.add(ft.Text("Error: Unable to get analysis"))
    else:
        # Extract the relevant information from the data
        summary = analysis_data.get("summary", "No summary available.")
        top_articles = analysis_data.get("top_articles", [])
        investment_opportunities = analysis_data.get("investment_opportunities", [])
        market_trend = analysis_data.get("market_trend", {})

    appBar = ft.Container(
        content=ft.Container(
            content=ft.Row(
                controls=[
                    ft.IconButton(icon=ft.Icons.ARROW_BACK, icon_color="#4F46E5"),
                    ft.Text("Market Analysis"),
                    ft.IconButton(icon=ft.Icons.REFRESH, icon_color="#4F46E5"),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            alignment=ft.alignment.center,
            margin=ft.margin.only(left=20, right=20),
        ),
        alignment=ft.alignment.center,
        height=48,
        bgcolor="#11112C",
    )

    body = ft.Container(
        content=ft.Column(
            controls=[],
        ),
    )

    return ft.View(
        controls=[
            ft.Container(
                content=ft.SafeArea(
                    content=ft.Container(
                        content=ft.Column(
                            controls=[appBar, body],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                        alignment=ft.alignment.center,
                    ),
                    expand=True,
                ),
                expand=True,
                bgcolor="#0B0B1F",
            )
        ]
    )
