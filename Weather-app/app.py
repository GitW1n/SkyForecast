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
            result_text.value = "Please enter the name of the city."
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
                
                
                result_text.value = f"City: {city}\nTemperature: {temp}°C\nWeather: {weather_desc}\nHumidity: {humidity}%\nWind speed: {wind_speed} m/s"
            else:
                result_text.value = "City not found. Try again."
        except Exception as ex:
            result_text.value = f"Ошибка при получении данных: {ex}"
        
        page.update()

    def change_theme(e):
        page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
        page.update()

    
    theme_button = ft.IconButton(icon=ft.icons.SUNNY, on_click=change_theme)
    header = ft.Text('Weather App', size=20)

    
    page.add(
        ft.Row(
            [theme_button, header],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [user_data],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [ft.ElevatedButton(text='Получить', on_click=get_info)],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [result_text],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


ft.app(target=main, view=ft.AppView.WEB_BROWSER)
