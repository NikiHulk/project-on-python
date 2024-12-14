import requests
from bs4 import BeautifulSoup

from SpeechUtils import speak


def exchangeRate(currencyUnit):

    """
    Получает текущий курс рубля к указанной валюте.

    Функция отправляет запрос на Google для получения актуального курса рубля к выбранной валюте и выводит
    информацию о курсе, а также озвучивает её с помощью функции speak.

    Аргументы:
        currencyUnit (str): Символ или аббревиатура валюты для которой требуется получить курс, например, "USD", "EUR", и т.д.

    Возвращает:
        None: Функция ничего не возвращает, но выводит курс в консоль и озвучивает его.

    Исключения:
        Если курс не был найден или произошла ошибка при запросе, функция сообщает об этом в консоли и озвучивает ошибку.
    """

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 YaBrowser/24.10.0.0 Safari/537.36"
    }
    url = f"https://www.google.com/search?q=курсы+рубля+к+{currencyUnit}"
    response = requests.get(url, headers=headers)

    getHtmlPage = BeautifulSoup(response.text, "lxml")
    span = getHtmlPage.find('span', class_="DFlfde SwHCTb")

    if span:
        value = span.text.strip()
        # Проверяем, если значение курса равно "Not Found"
        if value == "Not Found":
            print(f"Не удалось получить курс для валюты {currencyUnit}. Возможно, ошибка в запросе или валюта не поддерживается.")
            speak(f"Не удалось получить курс для валюты {currencyUnit}. Возможно, ошибка в запросе или валюта не поддерживается.")
        else:
            print(f"Один Российский рубль равен {value} {currencyUnit}")
            speak(f"Один Российский рубль равен {value} {currencyUnit}")
    else:
        print(f"Не удалось получить курс для валюты {currencyUnit}. Возможно, ошибка в запросе или валюта не поддерживается.")
        speak(f"Не удалось получить курс для валюты {currencyUnit}. Возможно, ошибка в запросе или валюта не поддерживается.")

if __name__ == "__main__":
    speak("Введите валюту для получения курса (например, USD, EUR): ")
    currency = input("Введите валюту для получения курса (например, USD, EUR): ")
    exchangeRate(currency)

