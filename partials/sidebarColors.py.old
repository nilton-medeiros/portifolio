import flet as ft


class SidebarColors(ft.UserControl):
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)

    def change_color(self, e):
        self.page.theme.color_scheme.primary = e.control.data
        self.page.update()

    def build(self):
        # Lista de cores e nomes associados
        colors = [
            (ft.colors.AMBER, "amber"),
            (ft.colors.RED, "red"),
            (ft.colors.DEEP_ORANGE, "deeporange"),
            (ft.colors.PINK, "pink"),
            (ft.colors.DEEP_PURPLE, "deeppurple"),
            (ft.colors.INDIGO, "indigo"),
            (ft.colors.BLUE, "blue"),
            (ft.colors.GREEN, "green"),
        ]

        # Criação de containers para cada cor
        color_containers = [
            ft.Container(
                alignment=ft.alignment.center,
                content=ft.Text(value=name, color=ft.colors.WHITE),
                width=100,
                height=50,
                margin=ft.margin.symmetric(vertical=10),
                bgcolor=color,
                data=name,
                border_radius=ft.border_radius.all(5),
                shadow=ft.BoxShadow(
                    color='#f5f5f5',
                    offset=ft.Offset(x=2, y=2),
                    spread_radius=0,
                    blur_radius=16,
                ),
                on_click=self.change_color,  # Evento vinculado
            )
            for color, name in colors
        ]

        # Retorna o layout com as cores
        return ft.Container(
            expand=True,
            alignment=ft.alignment.center,
            content=ft.Column(controls=color_containers, alignment=ft.MainAxisAlignment.CENTER),
            bgcolor=ft.colors.BLACK,
        )
