import flet as ft
from data import make_text, make_time_now

def main(page: ft.Page):
    page.title = "App"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    
    flag = False

    def update_text(e):
        result = make_text(user_text.value, flag)
        viever_texter.value = f"{result}"
        page.update()

    
    def set_flag_true(e):
        nonlocal flag
        flag = True
        update_text(e)

    
    def set_flag_false(e):
        nonlocal flag
        flag = False
        update_text(e)

    def set_time_now(e):
        result = make_time_now()
        viever_texter.value = f"{result}"
        page.update()
   
    my_text = ft.Text('Enter ur date', color="blue")
    user_text = ft.TextField(
        value="",
        width=200,
        hint_text="",
        hint_style=ft.TextStyle(color="gray"),
        border_color="blue",
        text_align=ft.TextAlign.CENTER,
    )

    button_true = ft.IconButton(ft.Icons.RECYCLING, on_click=set_flag_true)  
    button_false = ft.IconButton(ft.Icons.MUSIC_NOTE, on_click=set_flag_false)  
    button_time_now = ft.IconButton(ft.Icons.WATCH_LATER_OUTLINED, on_click = set_time_now)

    viever_texter = ft.Text("Just your future date", color='blue')

    page.add(
        ft.Column([
            ft.Row(
                [viever_texter],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [my_text, user_text, button_true, button_false,button_time_now],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ], spacing=20)
    )

ft.app(target=main)
