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
        
        try:
            response = requests.get(URL)
            data = response.json()
            
            if response.status_code == 200:
                
                temp = data['main']['temp']
                weather_desc = data['weather'][0]['description']
                humidity = data['main']['humidity']
                wind_speed = data['wind']['speed']
                
                
                result_text.value = f"Город: {city}\nТемпература: {temp}°C\nПогода: {weather_desc}\nВлажность: {humidity}%\nСкорость ветра: {wind_speed} м/с"
            
