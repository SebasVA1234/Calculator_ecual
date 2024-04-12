
import controllers.Home_controller as crl_home
import flet as ft
from flet import (
    colors,
    border_radius
)


def home(page: ft.Page):
    page.title = "Ecualand Calc App"

     
    result_display = ft.Text("Total", size=20, color=ft.colors.WHITE,)
    result_display2 = ft.Text("Comision", size=20, color=ft.colors.WHITE)
    input_value = ft.TextField(label="Valor a enviar",
                               label_style=ft.TextStyle(color=ft.colors.BLACK87,size =20),  # Set label color to WHITE12
                               width=350,
                               height=55,
                               value="0",
                               text_size=24,
                               color=ft.colors.WHITE,
                               bgcolor=colors.PURPLE_200)
    input_value_percen = ft.TextField(label="Comisión a cobrar",
                                      label_style=ft.TextStyle(color=ft.colors.BLACK87,size =20), 
                                      width=350,
                                      height=55,
                                      value="0",
                                      text_size=24,
                                      color=ft.colors.WHITE,
                                      bgcolor=colors.PURPLE_200)
    input_value_taxe = ft.TextField(label="Comisión transaccional", 
                                    label_style=ft.TextStyle(color=ft.colors.BLACK87,size =20), 
                                    width=350,
                                    height=55,
                                    value="2",
                                    text_size=24,
                                    color=ft.colors.WHITE,
                                    bgcolor=colors.PURPLE_200)
    home_controller = crl_home.HomeControler()

    def on_click_high_persentage(e):
        try:
            value = float(input_value.value)
            commision = float(input_value_percen.value)
            extra = float(input_value_taxe.value)

            result = home_controller.calculate_procentage(value=float(input_value.value),
                                                      commision=float(input_value_percen.value),
                                                      extra=float(input_value_taxe.value))
            comision = home_controller.procentage(value=float(input_value.value),
                                                      commision=float(input_value_percen.value),
                                                      extra=float(input_value_taxe.value))

            result = round(result, 4)
            result_display.value = str(result)
            result_display2.value = str(comision)
            page.update()
        except ValueError:
            # Handle invalid input (e.g., show an error message)
            print("Invalid input. Please enter numbers only.")


    # Create a container for input fields
    input_fields_container = ft.Container(
        content=ft.Column(
            controls=[
                input_value,
                input_value_percen,
                input_value_taxe,
            ],
            spacing=10,  # Add spacing between fields
        ),
        padding=20,
    )




    # Create a container for buttons and results
    buttons_and_results_container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Column(
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.CALCULATE,
                            icon_color=ft.colors.WHITE,  # Set icon color to white
                            bgcolor=colors.PURPLE_300,
                            on_click=on_click_high_persentage,
                            icon_size=32,  
                        ),
                        ft.IconButton(
                            icon=ft.icons.FILE_COPY_OUTLINED,
                            icon_color=ft.colors.WHITE,  # Set icon color to white
                            bgcolor=colors.PURPLE_300,
                            on_click=lambda e: home_controller.copy_on_clipboard(result_display.value),
                            icon_size=32,  
                        ),
                    ],
                    spacing=10,
                ),
                result_display,
                result_display2,
            ],
            spacing=10,
        ),
        padding=10,
    )

    # Create a main container to wrap both input and buttons/results containers
    main_container = ft.Container(
        width=800,  # Adjust width as needed
        bgcolor=colors.LIME_600,
        border_radius=border_radius.all(25),
        padding=15,
        content=ft.Row(
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                input_fields_container,
                buttons_and_results_container,
            ],
            spacing=10,  # Add spacing between containers
        ),
    )

    page.add(
        main_container,
    )

