import flet as ft
from components.skills import SkillRing, SkillProgressBar


class SidebarHeader(ft.UserControl):
    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Badge(
                        content=ft.Image(
                            src='images/face-1.jpg',
                            border_radius=ft.border_radius.all(100),
                            width=100,
                        ),
                        alignment=ft.alignment.bottom_right,
                        bgcolor=ft.colors.PRIMARY,
                        small_size=20,
                    ),
                    ft.Text(value='Dalton Peixoto',
                            theme_style=ft.TextThemeStyle.BODY_LARGE),
                    ft.Text(value='Desenvolvedor Fullstack',
                            theme_style=ft.TextThemeStyle.BODY_MEDIUM)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=ft.padding.symmetric(vertical=20, horizontal=40),
            alignment=ft.alignment.center,
        )


class SidebarContent(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.expand = True

    def build(self):
        location = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text(value='Residência:',
                                theme_style=ft.TextThemeStyle.BODY_LARGE),
                        ft.Text(value='Brasil',
                                theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Row(
                    controls=[
                        ft.Text(value='Cidade:',
                                theme_style=ft.TextThemeStyle.BODY_LARGE),
                        ft.Text(value='São Paulo',
                                theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Row(
                    controls=[
                        ft.Text(value='Idade:',
                                theme_style=ft.TextThemeStyle.BODY_LARGE),
                        ft.Text(
                            value='28', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
            ]
        )

        languages = ft.Row(
            controls=[
                SkillRing(title='Português', value=1),
                SkillRing(title='Inglês', value=1),
                SkillRing(title='Espanhol', value=0.5),
            ]
        )

        skills = ft.Column(
            controls=[
                SkillProgressBar(title='HTML', value=1),
                SkillProgressBar(title='CSS', value=1),
                SkillProgressBar(title='PYTHON', value=1),
                SkillProgressBar(title='JS', value=0.8),
                SkillProgressBar(title='PHP', value=0.6),
            ]
        )

        technologies = ft.Column(
            controls=[
                ft.ListTile(
                    leading=ft.Icon(name=ft.icons.CHECK,
                                    color=ft.colors.PRIMARY),
                    title=ft.Text(
                        value='Flet', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                ),
                ft.ListTile(
                    leading=ft.Icon(name=ft.icons.CHECK,
                                    color=ft.colors.PRIMARY),
                    title=ft.Text(value='Versionamento com GIT',
                                  theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                ),
                ft.ListTile(
                    leading=ft.Icon(name=ft.icons.CHECK,
                                    color=ft.colors.PRIMARY),
                    title=ft.Text(value='Bootstrap, Webpack, Framer Motion, Tailwind',
                                  theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                ),
                ft.ListTile(
                    leading=ft.Icon(name=ft.icons.CHECK,
                                    color=ft.colors.PRIMARY),
                    title=ft.Text(value='Typescript, ReactJS, Angular',
                                  theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                ),
                ft.ListTile(
                    leading=ft.Icon(name=ft.icons.CHECK,
                                    color=ft.colors.PRIMARY),
                    title=ft.Text(value='Django, Flask, FastAPI',
                                  theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=0,
        )

        cv = ft.TextButton(
            text='DOWNLOAD CV',
            style=ft.ButtonStyle(color=ft.colors.GREY),
            icon=ft.icons.DOWNLOAD,
            icon_color=ft.colors.GREY,
            url='https://drive.google.com/uc?export=download&id=1vHKz5-tKDC_HMwqaGYMbsAicGrKPwyFL',

            # https://sites.google.com/site/gdocs2direct/?pli=1
        )

        return ft.Container(
            bgcolor=ft.colors.BLACK12,
            padding=ft.padding.all(20),
            content=ft.Column(
                scroll=ft.ScrollMode.HIDDEN,
                controls=[
                    location,
                    ft.Divider(height=30),
                    languages,
                    ft.Divider(height=30),
                    skills,
                    ft.Divider(height=30),
                    technologies,
                    ft.Divider(height=30),
                    cv,
                ]
            )
        )


class SidebarFooter(ft.UserControl):
    def build(self):
        def change_primary_color(e):
            e.page.theme.color_scheme.primary = e.control.data
            e.page.update()

        return ft.Container(
            padding=ft.padding.symmetric(vertical=10),
            content=ft.Row(
                controls=[
                    ft.IconButton(
                        content=ft.Image(
                            src="icons/001-instagram.png", height=15, color="white"),
                        url="https://www.instagram.com/nilton_g_medeiros/",
                    ),
                    ft.IconButton(
                        content=ft.Image(
                            src="icons/002-linkedin.png", height=15, color="white"),
                        url="https://www.linkedin.com/in/nilton-goncalves-medeiros//",
                    ),
                    ft.IconButton(
                        content=ft.Image(
                            src="icons/003-github.png", height=15, color="white"),
                        url="https://github.com/nilton-medeiros",
                    ),
                    ft.IconButton(
                        content=ft.Image(
                            src="icons/004-youtube.png", height=15, color="white"),
                        url="https://www.youtube.com/@niltonmedeiros9313",
                    ),
                    ft.Container(
                        expand=True,
                    ),
                    ft.PopupMenuButton(
                        tooltip="Cores",
                        expand=True,
                        content=ft.Icon(
                            name=ft.icons.COLOR_LENS_OUTLINED,
                            color=ft.colors.WHITE,
                            size=15,
                        ),
                        items=[
                            ft.PopupMenuItem(
                                content=ft.Row(
                                    controls=[
                                        ft.Container(
                                            height=10,
                                            width=10,
                                            bgcolor=ft.colors.AMBER
                                        ),
                                        ft.Text(value='Amarelo')
                                    ]
                                ),
                                data='amber',
                                on_click=change_primary_color,
                            ),
                            ft.PopupMenuItem(
                                content=ft.Row(
                                    controls=[
                                        ft.Container(
                                            height=10,
                                            width=10,
                                            bgcolor=ft.colors.RED
                                        ),
                                        ft.Text(value='Vermelho')
                                    ]
                                ),
                                data='red',
                                on_click=change_primary_color,
                            ),
                            ft.PopupMenuItem(
                                content=ft.Row(
                                    controls=[
                                        ft.Container(
                                            height=10,
                                            width=10,
                                            bgcolor=ft.colors.DEEP_ORANGE
                                        ),
                                        ft.Text(value='Laranja')
                                    ]
                                ),
                                data='deeporange',
                                on_click=change_primary_color,
                            ),
                            ft.PopupMenuItem(
                                content=ft.Row(
                                    controls=[
                                        ft.Container(
                                            height=10,
                                            width=10,
                                            bgcolor=ft.colors.PINK
                                        ),
                                        ft.Text(value='Rosa')
                                    ]
                                ),
                                data='pink',
                                on_click=change_primary_color,
                            ),
                            ft.PopupMenuItem(
                                content=ft.Row(
                                    controls=[
                                        ft.Container(
                                            height=10,
                                            width=10,
                                            bgcolor=ft.colors.DEEP_PURPLE
                                        ),
                                        ft.Text(value='Violeta')
                                    ]
                                ),
                                data='deeppurple',
                                on_click=change_primary_color,
                            ),
                            ft.PopupMenuItem(
                                content=ft.Row(
                                    controls=[
                                        ft.Container(
                                            height=10,
                                            width=10,
                                            bgcolor=ft.colors.PURPLE
                                        ),
                                        ft.Text(value='Roxo')
                                    ]
                                ),
                                data='purple',
                                on_click=change_primary_color,
                            ),
                            ft.PopupMenuItem(
                                content=ft.Row(
                                    controls=[
                                        ft.Container(
                                            height=10,
                                            width=10,
                                            bgcolor=ft.colors.INDIGO
                                        ),
                                        ft.Text(value='Índigo')
                                    ]
                                ),
                                data='indigo',
                                on_click=change_primary_color,
                            ),
                            ft.PopupMenuItem(
                                content=ft.Row(
                                    controls=[
                                        ft.Container(
                                            height=10,
                                            width=10,
                                            bgcolor=ft.colors.BLUE
                                        ),
                                        ft.Text(value='Azul')
                                    ]
                                ),
                                data='blue',
                                on_click=change_primary_color,
                            ),
                            ft.PopupMenuItem(
                                content=ft.Row(
                                    controls=[
                                        ft.Container(
                                            height=10,
                                            width=10,
                                            bgcolor=ft.colors.GREEN
                                        ),
                                        ft.Text(value='Verde')
                                    ]
                                ),
                                data='green',
                                on_click=change_primary_color,
                            ),
                        ],
                    ),
                ]
            )
        )


class Sidebar(ft.UserControl):
    def build(self):
        return ft.Container(
            expand=True,
            content=ft.Column(
                controls=[
                    SidebarHeader(),
                    SidebarContent(),
                    SidebarFooter(),
                ]
            ),
            bgcolor=ft.colors.BACKGROUND,
        )
