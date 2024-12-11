import feedparser

def get_moscow_news_from_rss(rss_url):
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
    num = input("Введите номер интересующей вас новости, например 1, 2 ... 25: ") #каждому номеру соответствует определенный топик из новостей
    rss_url = f"https://govoritmoskva.ru/rss/news/{num}"
    moscow_news = get_moscow_news_from_rss(rss_url)
    if moscow_news:
        print("Новости Москвы:")
        for news_item in moscow_news:
            print(f"- {news_item}")

