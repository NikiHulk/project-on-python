import feedparser


def GetMoscowNewsFromRss(rss_url):
    """
    Получает заголовки новостей из RSS-ленты сайта Говорит Москва.

    Аргументы:
        rss_url (str): URL RSS-ленты для получения новостей.

    Возвращает:
        list: Список заголовков новостей в виде строк. Если произошла ошибка, возвращает None.

    Исключения:
        Exception: Если возникают ошибки при обработке или парсинге RSS-ленты.

    Примечания:
        Для работы функции требуется библиотека feedparser. Установите её с помощью: pip install feedparser.
        Проверка ошибки парсинга выполняется через атрибут bozo, если он равен True, то происходит возврат ошибки.
    """

    try:
        feed = feedparser.parse(rss_url)

        if feed.bozo:  # Проверка на ошибки при парсинге RSS
            print(f"Ошибка при парсинге RSS: {feed.bozo_exception}")
            return None

        # Составляем список заголовков новостей
        news_items = []
        for entry in feed.entries:
            news_items.append(entry.title)
        return news_items

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None


if __name__ == "__main__":
    num = input(
        "Введите номер интересующей вас новости, например 1, 2 ... 25: ")  # каждому номеру соответствует определенный топик из новостей
    rss_url = f"https://govoritmoskva.ru/rss/news/{num}"
    moscow_news = GetMoscowNewsFromRss(rss_url)
    if moscow_news:
        print("Новости Москвы:")
        for news_item in moscow_news:
            print(f"- {news_item}")
