import flet as ft
from utils.json_utils import load_data_from_file


def analysis_page(page):
    def create_news_card(item):
        if item["sentiment"] == "Positive":
            sentiment_color = "#10B57F"
            container_bgcolor = "#103239"
        elif item["sentiment"] == "Neutral":
            sentiment_color = "#CD9B24"
            container_bgcolor = "#3E2D21"
        elif item["sentiment"] == "Negative":
            sentiment_color = "#E13800"
            container_bgcolor = "#3E2121"
        else:
            sentiment_color = "#FFFFFF"
            container_bgcolor = "#11112C"

        return ft.Card(
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text(
                            value=item["title"], weight=ft.FontWeight.BOLD, size=14
                        ),
                        ft.Text(
                            value=item["description"],
                            size=12,
                            color="#7A7F8E",
                            weight=ft.FontWeight.W_600,
                        ),
                        ft.Row(
                            controls=[
                                ft.Container(
                                    content=ft.Text(
                                        value=item["sentiment"] + " Impact",
                                        size=12,
                                        color=sentiment_color,
                                        weight=ft.FontWeight.BOLD,
                                    ),
                                    padding=ft.padding.all(8),
                                    bgcolor=container_bgcolor,
                                    border_radius=ft.border_radius.all(10),
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.LINK,
                                    icon_color="#4F46E5",
                                    on_click=lambda _: page.launch(item["url"]),
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    spacing=6,
                ),
                padding=ft.padding.all(16),
                expand=True,
            ),
            expand=True,
            shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(10)),
            color="#11112C",
        )

    def create_investment_card(item):
        if item["performance"].startswith("-"):
            performance_color = "#E13800"
        else:
            performance_color = "#10B57F"

        if item["signal"] == "Strong Buy" or item["signal"] == "Buy":
            signal_color = "#10B57F"
        elif item["signal"] == "Hold":
            signal_color = "#CD9B24"
        else:
            signal_color = "#FFFFFF"

        return ft.Card(
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Row(
                                    [
                                        ft.Text(
                                            value=item["name"],
                                            weight=ft.FontWeight.BOLD,
                                            size=14,
                                        ),
                                        ft.Text(
                                            value=item["symbol"],
                                            weight=ft.FontWeight.W_600,
                                            size=12,
                                            color="#7A7F8E",
                                        ),
                                    ]
                                ),
                                ft.Text(
                                    value=f"${item["price"]}",
                                    weight=ft.FontWeight.BOLD,
                                    size=14,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                        ft.Row(
                            controls=[
                                ft.Text(
                                    value=item["signal"],
                                    weight=ft.FontWeight.BOLD,
                                    size=12,
                                    color=signal_color,
                                ),
                                ft.Text(
                                    value=item["performance"],
                                    weight=ft.FontWeight.BOLD,
                                    size=12,
                                    color=performance_color,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    spacing=2,
                ),
                padding=ft.padding.all(16),
                expand=True,
            ),
            expand=True,
            shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(10)),
            color="#11112C",
        )

    def create_market_trend_card(market_trend):
        confidence_value = market_trend["confidence"].replace("%", "")

        if market_trend["status"] == "Bullish":
            status_color = "#10B57F"
            icon_color = "#10B57F"
            progress_bar_color = "#10B57F"
            trend_message = "We predict a strong upward trend"
        elif market_trend["status"] == "Bearish":
            status_color = "#E13800"
            icon_color = "#E13800"
            progress_bar_color = "#E13800"
            trend_message = "We predict a downturn in the market"
        elif market_trend["status"] == "Neutral":
            status_color = "#CD9B24"
            icon_color = "#CD9B24"
            progress_bar_color = "#CD9B24"
            trend_message = (
                "Market trends are uncertain caution is advised in the short term."
            )
        else:
            status_color = "#FFFFFF"
            icon_color = "#FFFFFF"
            progress_bar_color = "#FFFFFF"
            trend_message = "Market trend is unclear further analysis is required."

        return ft.Row(
            controls=[
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Text(
                                            value=market_trend["status"].upper(),
                                            weight=ft.FontWeight.BOLD,
                                            color=status_color,
                                            size=16,
                                        ),
                                        ft.Icon(
                                            name=ft.Icons.SHOW_CHART,
                                            color=icon_color,
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Text(
                                            value="Confidence Score",
                                            color=ft.colors.WHITE,
                                            size=14,
                                        ),
                                        ft.Text(
                                            value=market_trend["confidence"],
                                            color=status_color,
                                            size=12,
                                            weight=ft.FontWeight.BOLD,
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                ),
                                ft.ProgressBar(
                                    value=float(confidence_value) / 100,
                                    color=progress_bar_color,
                                    bar_height=10,
                                ),
                                ft.Text(
                                    value=trend_message,
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
                    shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(10)),
                    color="#11112C",
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            expand=True,
        )

    try:
        analysis_data = load_data_from_file()
    except Exception as e:
        print(f"[ERROR] Failed to load analysis data: {e}")
        analysis_data = {}

    if analysis_data is None or "error" in analysis_data:
        page.add(ft.Text("Error: Unable to get analysis"))
    else:
        summary = analysis_data.get("summary", "No summary available.")
        top_articles = analysis_data.get("top_articles", [])
        investment_opportunities = analysis_data.get("investment_opportunities", [])
        market_trend = analysis_data.get("market_trend", {})

    summary_label = ft.Row(
        controls=[
            ft.Icon(
                name=ft.Icons.PIE_CHART,
                color="#4F46E5",
            ),
            ft.Text(value="Market Summary", size=16, weight=ft.FontWeight.BOLD),
        ],
    )
    summary_content = ft.Card(
        content=ft.Container(
            content=ft.Text(
                value=summary,
                size=12,
            ),
            padding=ft.padding.all(16),
            expand=True,
        ),
        expand=True,
        shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(10)),
        color="#11112C",
    )

    news_label = ft.Row(
        controls=[
            ft.Icon(
                name=ft.Icons.NEWSPAPER,
                color="#4F46E5",
            ),
            ft.Text(value="Latest News Impact", size=16, weight=ft.FontWeight.BOLD),
        ],
    )
    news_content = ft.Column(
        controls=[create_news_card(news_item) for news_item in top_articles],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        scroll=ft.ScrollMode.ALWAYS,
        height=350,
    )

    investment_opportunities_label = ft.Row(
        controls=[
            ft.Icon(
                name=ft.Icons.STAR,
                color="#4F46E5",
            ),
            ft.Text(
                value="Investment Opportunities", size=16, weight=ft.FontWeight.BOLD
            ),
        ],
    )
    investment_opportunities_content = ft.Column(
        controls=[
            create_investment_card(investment_item)
            for investment_item in investment_opportunities
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        scroll=ft.ScrollMode.ALWAYS,
        height=200,
    )

    market_trend_label = ft.Row(
        controls=[
            ft.Icon(
                name=ft.Icons.EARBUDS,
                color="#4F46E5",
            ),
            ft.Text(value="Market Trend", size=16, weight=ft.FontWeight.BOLD),
        ],
    )
    market_trend_content = create_market_trend_card(market_trend)

    appBar = ft.Container(
        content=ft.Container(
            content=ft.Row(
                controls=[
                    ft.IconButton(
                        icon=ft.Icons.ARROW_BACK,
                        icon_color="#4F46E5",
                        on_click=lambda e: page.go("/home"),
                    ),
                    ft.Text("Market Analysis", size=17, weight=ft.FontWeight.BOLD),
                    ft.IconButton(icon=ft.Icons.SETTINGS, icon_color="#4F46E5"),
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
                summary_label,
                summary_content,
                news_label,
                news_content,
                investment_opportunities_label,
                investment_opportunities_content,
                market_trend_label,
                market_trend_content,
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment=ft.CrossAxisAlignment.START,
        ),
        alignment=ft.alignment.center_left,
        margin=ft.margin.only(left=20, right=20),
    )

    return ft.View(
        controls=[
            ft.Container(
                content=ft.SafeArea(
                    content=ft.Container(
                        content=ft.Column(
                            controls=[appBar, body],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            alignment=ft.MainAxisAlignment.START,
                            scroll=ft.ScrollMode.HIDDEN,
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
