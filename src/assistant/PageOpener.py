import webbrowser


def open_page(url, page_name):
    """Открывает веб-страницу по заданному URL и выводит сообщение.

    Args:
        url (str): URL страницы для открытия.
        page_name (str): Читаемое имя страницы для вывода в сообщение.
    """
    webbrowser.open(url)
    print(f"Открыта страница: {page_name} ({url})")


def openVkontakte():
    open_page("https://vk.com", "ВКонтакте")


def openVkVideo():
    open_page("https://vk.com/video", "ВКонтакте Видео")


def openKinopoisk():
    open_page("https://www.kinopoisk.ru", "Кинопоиск")


def openIvi():
    open_page("https://www.ivi.ru", "ИВИ")


def openRutube():
    open_page("https://rutube.ru", "Rutube")


def openYouTube():
    open_page("https://www.youtube.com", "YouTube")


def openTelegram():
    open_page("https://web.telegram.org", "Telegram")


def openYandexMaps():
    open_page("https://yandex.ru/maps/", "Яндекс.Карты")

