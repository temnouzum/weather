import requests
import telegram
import datetime

OPENWEATHER_API_KEY = "59ae975323fa8661e51be285b657f511"
TELEGRAM_BOT_TOKEN = "7591315433:AAF5vB0yHgfmszQVRuKP68NodC9IvebbsxE"
CHAT_ID = "@tashkan_weather_bot"

def get_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?q=Tashkent&appid={OPENWEATHER_API_KEY}&units=metric&lang=ru"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        description = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        weather_message = (
            f"🌤 Погода в Ташкенте на {datetime.datetime.now().strftime('%d.%m.%Y')}:\n"
            f"- Температура: {temp}°C (ощущается как {feels_like}°C)\n"
            f"- Влажность: {humidity}%\n"
            f"- Описание: {description.capitalize()}"
        )
        return weather_message
    else:
        return "Не удалось получить данные о погоде."

def send_to_telegram(message):
    bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=message)

if __name__ == "__main__":
    weather_message = get_weather()
    send_to_telegram(weather_message)
