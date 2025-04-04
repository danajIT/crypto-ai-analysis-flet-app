import flet as ft
from ai_utils import client, start_news_analysis
from time import sleep
from json_utils import save_data_to_file


def home_page(page):
    def start_analysis_click(e):
        start_button.visible = False
        progress_ring.visible = True
        page.update()

        # analysis_data = start_news_analysis(client)
        sleep(3)
        analysis_data = {
            "summary": "The crypto market is currently experiencing mixed sentiments. Bitcoin shows signs of adoption with Mastercard's initiative, while Ethereum faces bearish pressure due to technical concerns and whale sell-offs. Altcoins like Solana and Ripple's RLUSD are gaining traction due to ETF approval signals and stablecoin integration. Market trends suggest a neutral stance with cautious optimism for long-term investments.",
            "top_articles": [
                {
                    "title": "Mastercard Plans to Enable 3.5 Billion Cardholders to Transact with Bitcoin ($BTC) and Crypto",
                    "url": "https://thedefiant.io",
                    "description": "Mastercard's plan to enable crypto transactions for 3.5 billion cardholders marks a significant step in crypto adoption, potentially boosting Bitcoin's utility and value.",
                    "sentiment": "Positive",
                },
                {
                    "title": "Signs point to approval of Solana ETFs in May",
                    "url": "https://cryptovalleyjournal.com",
                    "description": "The potential approval of Solana ETFs could attract institutional investors, driving liquidity and price growth for Solana.",
                    "sentiment": "Positive",
                },
                {
                    "title": "Ethereum developers aim for May 7 mainnet deployment of Pectra upgrade",
                    "url": "https://theblock.co",
                    "description": "The upcoming Pectra upgrade for Ethereum aims to improve scalability and network efficiency, but technical hurdles have delayed its deployment.",
                    "sentiment": "Neutral",
                },
                {
                    "title": "Analyst Warns of Massive Ethereum Drop Against Bitcoin",
                    "url": "https://cryptodnes.bg",
                    "description": "A bearish technical pattern suggests Ethereum may face significant downside against Bitcoin, raising concerns for ETH holders.",
                    "sentiment": "Negative",
                },
                {
                    "title": "Kraken Announces Support for RLUSD As Stablecoin Integrates Into Ripple’s Payment’s Network",
                    "url": "https://dailyhodl.com",
                    "description": "Kraken's support for RLUSD and its integration into Ripple's network highlights growing adoption of Ripple's payment solutions.",
                    "sentiment": "Positive",
                },
            ],
            "investment_opportunities": [
                {
                    "name": "Bitcoin (BTC)",
                    "price": "$66,200.00",
                    "performance": "+3.8%",
                    "signal": "Buy",
                },
                {
                    "name": "Solana (SOL)",
                    "price": "$145.75",
                    "performance": "+6.1%",
                    "signal": "Strong Buy",
                },
                {
                    "name": "Ripple (XRP)",
                    "price": "$0.63",
                    "performance": "+4.5%",
                    "signal": "Buy",
                },
            ],
            "market_trend": {"status": "Neutral", "confidence": "65%"},
        }

        save_data_to_file(analysis_data)

        if "error" in analysis_data:
            page.add(ft.Text("Error: Unable to get analysis"))
        else:
            page.go("/analysis")

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
