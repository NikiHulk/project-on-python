from unittest.mock import patch, MagicMock
from src import GetMoscowNewsFromRss

# Тест на корректный парсинг RSS
def test_get_moscow_news_success():
    # Мокируем объект, возвращаемый feedparser.parse
    mock_feed = MagicMock()
    # mock_feed.entries должен быть списком, в котором каждый элемент имеет атрибут 'title'
    mock_feed.entries = [MagicMock(title='Новости 1'), MagicMock(title='Новости 2'), MagicMock(title='Новости 3')]
    mock_feed.bozo = False  # Указываем, что ошибок при парсинге нет

    with patch('feedparser.parse', return_value=mock_feed):
        rss_url = 'https://govoritmoskva.ru/rss/news/1'
        result = GetMoscowNewsFromRss(rss_url)
        # Проверяем, что функция вернула правильный список заголовков
        assert result == ['Новости 1', 'Новости 2', 'Новости 3'], "Функция должна вернуть список новостей"

# Тест на обработку ошибки при парсинге RSS
def test_get_moscow_news_parsing_error():
    # Мокируем ошибку при парсинге
    mock_feed = MagicMock()
    mock_feed.bozo = True
    mock_feed.bozo_exception = "Ошибка парсинга"

    with patch('feedparser.parse', return_value=mock_feed):
        rss_url = 'https://govoritmoskva.ru/rss/news/1'
        result = GetMoscowNewsFromRss(rss_url)
        assert result is None, "Функция должна вернуть None в случае ошибки парсинга"

# Тест на обработку исключений
def test_get_moscow_news_exception():
    # Мокируем исключение в процессе получения данных
    with patch('feedparser.parse', side_effect=Exception('Произошла ошибка')):
        rss_url = 'https://govoritmoskva.ru/rss/news/1'
        result = GetMoscowNewsFromRss(rss_url)
        assert result is None, "Функция должна вернуть None в случае исключения"
