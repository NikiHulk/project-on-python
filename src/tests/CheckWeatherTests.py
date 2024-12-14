from unittest.mock import patch
from src.assistant.CheckWeather import checkWeatherNow


# Тест для проверки функции checkWeatherNow
def testCheckWeatherNow():
    cityName = "Москва"

    # Мокаем функцию requests.get
    with patch('requests.get') as mockGet:
        # Мокаем ответ от API Google с данными погоды
        mockResponse = {
            "routes": [
                {
                    "legs": [
                        {
                            "distance": 10000,  # 10 км
                            "duration": 600  # 10 минут
                        }
                    ]
                }
            ]
        }
        mockGet.return_value.status_code = 200
        mockGet.return_value.text = "<html><body><div id='wob_dc'>Ясно</div><div id='wob_tm'>5</div><div id='wob_hm'>55%</div><div id='wob_dts'>12:00</div><div id='wob_ws'>5 м/с</div></body></html>"

        # Мокаем функцию speak
        with patch('assistant.CheckWeather.speak') as mockSpeak:
            # Вызываем функцию
            checkWeatherNow(cityName)

            # Проверяем, что запрос был выполнен с правильным URL
            mockGet.assert_called_with(f"https://www.google.com/search?q=погода+в+{cityName}", headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 YaBrowser/24.10.0.0 Safari/537.36'})

            # Проверяем, что функция speak была вызвана
            mockSpeak.assert_called_once_with(
                "В городе Москва сейчас ясно: \nТемпература составляет: 5℃ \nВлажность составляет: 55% \nНастоящее время: 12:00 \nВетер: 5 метров в секунду"
            )
