import webbrowser

class PageOpener:

    def __init__(self):
        pass

    def OpenYoutube(self):
        self.OpenUrl("https://www.youtube.com")

    def OpenRutube(self):
        self.OpenUrl("https://rutube.ru")

    def OpenVk(self):
        self.OpenUrl("https://vk.com")

    def OpenTelegram(self):
        self.OpenUrl("https://web.telegram.org")

    def OpenVkvideo(self):
        self.OpenUrl("https://vkvideo.ru/")

    def OpenIvi(self):
        self.OpenUrl("https://www.ivi.ru/")

    def OpenKinopoisk(self):
        self.OpenUrl("https://www.kinopoisk.ru")

    def OpenUrl(self, url):
        try:
            webbrowser.open(url)
            print(f"Страница {url} открыта.")
        except Exception as e:
            print(f"Ошибка при открытии страницы: {e}")


opener = PageOpener()
opener.OpenKinopoisk()

