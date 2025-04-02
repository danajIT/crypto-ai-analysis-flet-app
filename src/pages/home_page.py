import flet as ft


def home_page(page):
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
                ft.FilledButton(
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
                ),
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
