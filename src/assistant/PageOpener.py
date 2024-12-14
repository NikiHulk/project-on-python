import webbrowser

"""
Этот модуль содержит функции для открытия популярных сайтов с использованием браузера.

Функции:
- openVkontakte(): Открывает страницу ВКонтакте (https://vk.com).
- openVkVideo(): Открывает страницу видеоконтента ВКонтакте (https://vk.com/video).
- openKinopoisk(): Открывает страницу Кинопоиска (https://www.kinopoisk.ru).
- openIvi(): Открывает страницу ИВИ (https://www.ivi.ru).
- openRutube(): Открывает страницу Rutube (https://rutube.ru).
- openYouTube(): Открывает страницу YouTube (https://www.youtube.com).
- openTelegram(): Открывает страницу Telegram Web (https://web.telegram.org).
- openYandexMaps(): Открывает страницу Яндекс.Карт (https://yandex.ru/maps/).

Зависимости:
- webbrowser: Модуль для взаимодействия с веб-браузером и открытия URL.

Примечания:
- Каждая функция открывает соответствующую веб-страницу в браузере и выводит сообщение об этом.
"""


# Открытие страницы ВКонтакте
def openVkontakte():
    url = "https://vk.com"
    webbrowser.open(url)
    print(f"Открыта страница: {url}")

# Открытие страницы VkВидео
def openVkVideo():
    url = "https://vk.com/video"
    webbrowser.open(url)
    print(f"Открыта страница: {url}")

# Открытие страницы Кинопоиск
def openKinopoisk():
    url = "https://www.kinopoisk.ru"
    webbrowser.open(url)
    print(f"Открыта страница: {url}")

# Открытие страницы ИВИ
def openIvi():
    url = "https://www.ivi.ru"
    webbrowser.open(url)
    print(f"Открыта страница: {url}")

# Открытие страницы Rutube
def openRutube():
    url = "https://rutube.ru"
    webbrowser.open(url)
    print(f"Открыта страница: {url}")

# Открытие страницы YouTube
def openYouTube():
    url = "https://www.youtube.com"
    webbrowser.open(url)
    print(f"Открыта страница: {url}")

# Открытие страницы Telegram
def openTelegram():
    url = "https://web.telegram.org"
    webbrowser.open(url)
    print(f"Открыта страница: {url}")

def openYandexMaps():
    url = "https://yandex.ru/maps/"
    webbrowser.open(url)
    print(f"Открыта страница: {url}")