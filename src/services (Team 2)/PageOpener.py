import webbrowser

class PageOpener:

    def __init__(self):
        pass

    def open_youtube(self):
        self._open_url("https://www.youtube.com")

    def open_rutube(self):
        self._open_url("https://rutube.ru")

    def open_vk(self):
        self._open_url("https://vk.com")

    def open_telegram(self):
        self._open_url("https://web.telegram.org")

    def open_vkvideo(self):
        self._open_url("https://vkvideo.ru/")

    def open_ivi(self):
        self._open_url("https://www.ivi.ru/")

    def open_kinopoisk(self):
        self._open_url("https://www.kinopoisk.ru")

    def _open_url(self, url):
        try:
            webbrowser.open(url)
            print(f"Страница {url} открыта.")
        except Exception as e:
            print(f"Ошибка при открытии страницы: {e}")


opener = PageOpener()
opener.open_kinopoisk()

