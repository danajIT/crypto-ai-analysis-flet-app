import flet as ft
from utils.ai_utils import client, start_news_analysis
from time import sleep
from utils.json_utils import (
    save_data_to_file,
    update_crypto_data,
    extract_crypto_symbols,
)
from utils.crypto_prices_utils import fetch_crypto_prices


def home_page(page):
    def start_analysis_click(e):
        start_button.visible = False
        progress_ring.visible = True
        page.update()
        # sleep(3)
        analysis_data = {
            "summary": "The crypto market is facing mixed signals, with Bitcoin showing potential for decoupling from traditional equities and Ethereum struggling amidst bearish sentiment. Altcoins like Solana are gaining traction due to potential ETF approvals, while DeFi narratives are shifting towards Bitcoin. Ethereum's technical upgrades and whale activity suggest long-term potential despite short-term bearish outlooks.",
            "top_articles": [
                {
                    "title": "Bitcoin shows signs of decoupling from US equities, could reclaim $100K",
                    "url": "https://cryptobriefing.com",
                    "description": "Bitcoin is showing signs of decoupling from traditional markets, with analysts predicting a potential rally to $100K. This could signal increased institutional interest and a shift in market dynamics.",
                    "sentiment": "Positive",
                },
                {
                    "title": "Signs point to approval of Solana ETFs in May",
                    "url": "https://cryptovalleyjournal.com",
                    "description": "Regulatory signals suggest that Solana-based ETFs could be approved in May, potentially driving increased institutional adoption and market interest in the altcoin.",
                    "sentiment": "Positive",
                },
                {
                    "title": "Ethereum whales accumulate 130,000 ETH amid price drop",
                    "url": "https://cryptobriefing.com",
                    "description": "Despite Ethereum's recent price decline, whale investors are accumulating large amounts of ETH, indicating confidence in the asset's long-term potential.",
                    "sentiment": "Neutral",
                },
                {
                    "title": "Ethereum faces a storm: Could the crypto giant plummet by 91%?",
                    "url": "https://cointrackdaily.com",
                    "description": "Bearish analysts warn of a potential massive price drop for Ethereum, citing technical indicators and growing competition from Bitcoin in DeFi.",
                    "sentiment": "Negative",
                },
                {
                    "title": "The future of DeFi isn’t on Ethereum — it’s on Bitcoin",
                    "url": "https://cointelegraph.com",
                    "description": "A growing narrative suggests that Bitcoin could become the primary platform for DeFi, challenging Ethereum's dominance in the sector.",
                    "sentiment": "Neutral",
                },
            ],
            "investment_opportunities": [
                {
                    "name": "Bitcoin",
                    "symbol": "BTC",
                    "price": 83686.82,
                    "performance": "0.33%",
                    "signal": "Buy",
                },
                {
                    "name": "Solana",
                    "symbol": "SOL",
                    "price": 121.32,
                    "performance": "-4.16%",
                    "signal": "Strong Buy",
                },
                {
                    "name": "Ethereum",
                    "symbol": "ETH",
                    "price": 1817.43,
                    "performance": "-3.16%",
                    "signal": "Hold",
                },
            ],
            "market_trend": {"status": "Neutral", "confidence": "65%"},
        }
        analysis_data = start_news_analysis(client)
        symbols = extract_crypto_symbols(analysis_data)
        crypto_real_time_info = fetch_crypto_prices(symbols)
        update_crypto_data(analysis_data, crypto_real_time_info)
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
                                            size=14,
                                        ),
                                        ft.Text(
                                            value="Smart market forecasting",
                                            color="#7A7F8E",
                                            size=12,
                                            weight=ft.FontWeight.W_600,
                                        ),
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
                                            size=14,
                                        ),
                                        ft.Text(
                                            value="Real-time news impact",
                                            color="#7A7F8E",
                                            size=12,
                                            weight=ft.FontWeight.W_600,
                                        ),
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
