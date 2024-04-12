import flet as ft


def main(page: ft.Page):
    page.title = "Ecualand Calc App"
    result = ft.Text(value="0")

    page.add(
        result,
        ft.ElevatedButton(text="#^%"),
        ft.ElevatedButton(text="None"),

    )

ft.app(target=main)

ft.app(main)
