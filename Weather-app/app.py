from textual.app import App
from textual.widgets import Label
import requests


def get_weather(city: str, api_key: str):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = {
            "city": city,
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        return weather
    else:
        return None


class WeatherApp(App):

    def __init__(self, api_key: str, city: str):
        super().__init__()
        self.api_key = api_key
        self.city = city
        self.weather = None

    async def on_mount(self) -> None:
        self.weather = get_weather(self.city, self.api_key)
        if self.weather:
            await self.display_weather()
        else:
            await self.display_error()

    async def display_weather(self):
        temperature = f"{self.weather['temperature']}°C"
        description = self.weather['description'].capitalize()
        humidity = f"Humidity: {self.weather['humidity']}%"
        wind_speed = f"Wind Speed: {self.weather['wind_speed']} m/s"

        await self.view.dock(
            Label(f"Weather in {self.weather['city']}"),
            Label(temperature),
            Label(description),
            Label(humidity),
            Label(wind_speed)
        )

    async def display_error(self):
        await self.view.dock(
            Label(f"Failed to retrieve weather for {self.city}. Please try again.")
        )


if __name__ == "__main__":
    api_key = int(input('API:'))
    city = "London"
    app = WeatherApp(api_key, city)
    app.run()

