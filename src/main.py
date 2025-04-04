import flet as ft
import urllib.parse
import json
from pages.home_page import home_page
from pages.analysis_page import analysis_page


def main_flet(page: ft.Page):
    page.title = "AI CRYPTO ANALYSIS"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0

    def route_change(route):
        page.views.clear()

        if page.route == "/home":
            page.views.append(home_page(page))
        elif page.route.startswith("/analysis"):
            page.views.append(analysis_page(page))

        page.update()

    page.on_route_change = route_change
    page.go("/home")


if __name__ == "__main__":
    ft.app(target=main_flet, view=ft.WEB_BROWSER)
