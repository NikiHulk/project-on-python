import feedparser

def GetMoscowNewsFromRss(rss_url):

    """
    Получает новости Москвы из RSS-ленты по заданному URL.

    Эта функция подключается к RSS-каналу, парсит его содержимое и возвращает список заголовков новостей.

    Параметры:
        rss_url (str): URL RSS-ленты, откуда нужно извлечь новости.

    Возвращаемое значение:
        list: Список заголовков новостей, если парсинг прошел успешно.
        None: Если произошла ошибка при парсинге или загрузке RSS-ленты.
    """

    try:
        feed = feedparser.parse(rss_url)
        if feed.bozo:  # Проверка на ошибки при парсинге RSS
            print(f"Ошибка при парсинге RSS: {feed.bozo_exception}")
            return None

        news_items = []
        for entry in feed.entries:
            news_items.append(entry.title)
        return news_items

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

if __name__ == "__main__":

    """
    Главная функция программы. Запрашивает у пользователя номер новости и выводит список новостей из Москвы
    по указанному RSS-каналу.
    """

    num = input("Введите номер интересующей вас новости, например 1, 2 ... 25: ") #каждому номеру соответствует определенный топик из новостей
    rss_url = f"https://govoritmoskva.ru/rss/news/{num}"
    moscow_news = GetMoscowNewsFromRss(rss_url)
    if moscow_news:
        print("Новости Москвы:")
        for news_item in moscow_news:
            print(f"- {news_item}")

