import flet as ft
from flet import *

def main(page: ft.Page):
    page.title="My Password Manager"
    page.window_width = 385       # window's width is 385 px
    page.window_height = 430       # window's height is 430 px
    page.window_resizable = False
    page.scroll="auto"

    page.horizontal_alignment="center"
    page.vertical_alignment="start"
    page.padding=padding.only(top=50)
    
    page.update()


    def button_clicked(e):
        t.value = f"Textboxes values are:  '{tbLink.value}'."
        page.update()

    t=ft.Text()
    tbLink=ft.TextField(label="Link",width=350)
    b = ft.ElevatedButton(text="Download", on_click=button_clicked)

    page.add(tbLink,b,t)
    
if __name__ == "__main__":    
    ft.app(target=main)