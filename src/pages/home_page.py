import flet as ft
from ai_utils import client, start_news_analysis
from time import sleep


def home_page(page):
    def start_analysis_click(e):
        start_button.visible = False
        progress_ring.visible = True
        page.update()

        # analysis_data = start_news_analysis(client)
        sleep(10)
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
            page.go("/analysis", data=analysis_data)

    start_button = ft.FilledButton(
        content=ft.Row(
            controls=[
                ft.Text("Start Market Analysis"),
                ft.Icon(name=ft.Icons.ARROW_FORWARD, color=ft.colors.WHITE),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        color=ft.colors.WHITE,
        bgcolor="#4F46E5",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(10))
        ),
        height=60,
        width=350,
        on_click=start_analysis_click,
    )

    progress_ring = ft.ProgressRing(
        width=50, height=50, stroke_width=5, color="#4F46E5", visible=False
    )

    appBar = ft.Container(
        content=ft.Container(
            content=ft.Row(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Icon(name=ft.Icons.CIRCLE, color="#10B57F", size=10),
                            ft.Text("Live"),
                        ],
                    ),
                    ft.Row(
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Icon(
                                        name=ft.Icons.ACCESS_TIME_FILLED,
                                        color="#4F46E5",
                                    ),
                                    ft.Text("24/7 Analysis"),
                                ],
                            ),
                            ft.Row(
                                controls=[
                                    ft.Icon(name=ft.Icons.LANGUAGE, color="#4F46E5"),
                                    ft.Text("Global Data"),
                                ],
                            ),
                        ],
                    ),
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
            controls=[
                ft.Icon(name=ft.Icons.CANDLESTICK_CHART, color="#4F46E5", size=100),
                ft.Text(
                    value="AI Crypto Analysis",
                    size=36,
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Text(
                    value="Advanced market insights powered by artificial intelligence",
                    size=16,
                ),
                ft.Row(
                    controls=[
                        ft.Card(
                            content=ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Icon(
                                            name=ft.Icons.SMART_TOY, color="#4F46E5"
                                        ),
                                        ft.Text(
                                            value="AI Prediction",
                                            weight=ft.FontWeight.BOLD,
                                        ),
                                        ft.Text(value="Smart market forecasting"),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                ),
                                padding=ft.padding.all(16),
                                expand=True,
                            ),
                            expand=True,
                            shape=ft.RoundedRectangleBorder(
                                radius=ft.border_radius.all(10)
                            ),
                            color="#11112C",
                        ),
                        ft.Card(
                            content=ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Icon(
                                            name=ft.Icons.NEWSPAPER, color="#4F46E5"
                                        ),
                                        ft.Text(
                                            value="News Analysis",
                                            weight=ft.FontWeight.BOLD,
                                        ),
                                        ft.Text(value="Real-time news impact"),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                ),
                                padding=ft.padding.all(16),
                                expand=True,
                            ),
                            expand=True,
                            shape=ft.RoundedRectangleBorder(
                                radius=ft.border_radius.all(10)
                            ),
                            color="#11112C",
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Container(
                                content=ft.Icon(
                                    name=ft.Icons.CURRENCY_BITCOIN,
                                    color=ft.colors.BLACK,
                                    size=16,
                                ),
                                width=20,
                                height=20,
                                bgcolor="#F59E0B",
                                border_radius=ft.border_radius.all(16),
                                alignment=ft.alignment.center,
                            ),
                            ft.Text(value="BTC"),
                            ft.Text(value="+2.4%", color="#10B57F"),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    width=150,
                    bgcolor="#11112C",
                    padding=ft.padding.all(16),
                    border_radius=ft.border_radius.all(20),
                    alignment=ft.alignment.center,
                ),
                start_button,
                progress_ring,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        alignment=ft.alignment.center,
    )

    bottomBar = ft.Container(
        content=ft.Container(
            content=ft.Row(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Icon(name=ft.Icons.AUTO_AWESOME, color="#4F46E5"),
                            ft.Text("AI Powered"),
                        ],
                    ),
                    ft.Row(
                        controls=[
                            ft.Icon(
                                name=ft.Icons.SECURITY,
                                color="#4F46E5",
                            ),
                            ft.Text("Secure Analysis"),
                        ],
                    ),
                    ft.Row(
                        controls=[
                            ft.Icon(name=ft.Icons.BOLT, color="#4F46E5"),
                            ft.Text("Real-Time"),
                        ],
                    ),
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

    return ft.View(
        controls=[
            ft.Container(
                content=ft.SafeArea(
                    content=ft.Container(
                        content=ft.Column(
                            controls=[appBar, body, bottomBar],
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
