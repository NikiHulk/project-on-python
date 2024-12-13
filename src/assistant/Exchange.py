import requests
from bs4 import BeautifulSoup

from SpeechUtils import speak


def exchangeRate(currencyUnit):
    """
    Получает и озвучивает текущий обменный курс рубля к указанной валюте с использованием Google Finance.
    Args:
        currencyUnit (str): Код валюты (например, "USD", "EUR").
    Returns:
        None. Выводит информацию о курсе в консоль и озвучивает её.
    Raises:
        requests.exceptions.RequestException: При ошибках HTTP-запроса.
        AttributeError: Если на странице Google Finance не найден необходимый элемент.
    Notes:
            Функция использует веб-скрапинг страницы Google Finance. Структура страницы может измениться, что может привести к ошибкам.
            Необходимо установить библиотеки requests и beautifulsoup4: pip install requests beautifulsoup4
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

