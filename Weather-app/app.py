import flet as ft
import requests

def main(page):
    page.title = "Weather"
    page.theme_mode = 'dark'

    user_data = ft.TextField(label='Введите город', width=400)
    result_text = ft.Text(value='', size=16, color='white')

    def get_info(e):
        city = user_data.value
        if not city:
            result_text.value = "Пожалуйста, введите название города."
            page.update()
            return
        
        API = 'f91a2b525491521109dd34d4f8132567'
        URL = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric'

