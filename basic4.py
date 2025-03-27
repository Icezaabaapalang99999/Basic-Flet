from flet import *

def main(page: Page):
    switch = Switch(label="Dark mode")

    def toggle_theme(e):
        page.theme_mode = "Dark" if switch.value else "light"
        page.update()

    switch.on_change = toggle_theme
    page.add(switch)

app(target=main)