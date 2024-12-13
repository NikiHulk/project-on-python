import requests
from bs4 import BeautifulSoup

from SpeechUtils import speak


def checkWeatherNow(city):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 YaBrowser/24.10.0.0 Safari/537.36"
    }

    url = f"https://www.google.com/search?q=погода+в+{city}"
    response = requests.get(url, headers=headers)

    # Парсим HTML-страницу
    getHtmlPage = BeautifulSoup(response.text, "html.parser")

    # Извлекаем данные текущей погоды
    title = getHtmlPage.select("#wob_dc")[0].getText()
    temperature = getHtmlPage.select("#wob_tm")[0].getText()
    humidity = getHtmlPage.select("#wob_hm")[0].getText()
    time = getHtmlPage.select("#wob_dts")[0].getText()
    wind = getHtmlPage.select("#wob_ws")[0].getText()
    temperatureForecast = f"{temperature}"
    windForecast = f"{wind}"
    if "м/с" in windForecast:
        windForecast = windForecast.replace("м/с", "метров в секунду")
    if "-" in temperatureForecast:
        temperatureForecast = temperatureForecast.replace("-", "минус ")
    if "+" in temperatureForecast:
        temperatureForecast = temperatureForecast.replace("+", "плюс ")
    # Выводим текущую погоду
    print(f"В городе {city} сейчас {title.lower()}: \n"
          f"Температура составляет: {temperature}℃ \n"
          f"Влажность составляет: {humidity} \n"
          f"Настоящее время: {time[:1].upper() + time[1:]} \n"
          f"Ветер: {wind}")
    speak(f"В городе {city} сейчас {title.lower()}: \n"
          f"Температура составляет: {temperatureForecast}℃ \n"
          f"Влажность составляет: {humidity} \n"
          f"Настоящее время: {time[:1].upper() + time[1:]} \n"
          f"Ветер: {windForecast}")

if __name__ == "__main__":
    city = input("Введите город: ")  # Получаем город от пользователя
    checkWeatherNow(city)
