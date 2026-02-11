import flet as ft

def main(page: ft.Page):
    page.title = "Bridgerton"
    page.bgcolor = "#d39beb"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def mostrar_mensagem(e):
        page.add(ft.Text("Eu sou a princesa da temporada!"))
    page.add(
        ft.Text("Olá, meu nome é Daphne!"),
        ft.Image(
            src="images/Daphne.webp",
            height=200
        ),
        ft.Button(
            content="Quem sou eu?",
            bgcolor="purple",
            color="white",
            on_click=mostrar_mensagem
        )
    )

ft.app(main)    