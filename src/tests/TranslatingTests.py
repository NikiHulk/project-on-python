# tests/TranslatingTests.py

from unittest.mock import patch
from src.assistant.Translating import translate


# Тестирование успешного перевода
@patch('src.assistant.Translating.speak')
@patch('src.assistant.Translating.requests.get')
@patch('src.assistant.Translating.BeautifulSoup')
def test_translate_success(mock_beautifulsoup, mock_requests, mock_speak):
    """Тестируем успешный перевод."""

    # Мокируем ответ от Google Translate
    mock_response = mock_requests.return_value
    mock_response.status_code = 200
    mock_response.text = "<html><div class='result-container'>Hola</div></html>"

    # Мокируем BeautifulSoup
    mock_soup = mock_beautifulsoup.return_value
    mock_translation = mock_soup.find.return_value
    mock_translation.text = "Hola"

    # Запускаем функцию
    with patch('builtins.input', side_effect=["en", "es", "Hello"]):
        translate()

    # Проверка, что запрос был отправлен с правильным URL
    mock_requests.assert_called_once_with(
        'https://translate.google.com/m?sl=en&tl=es&q=Hello',
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    )

    # Проверка, что speak был вызван с правильным сообщением
    mock_speak.assert_any_call("Зачитываю перевод вашего текста, Hola")

    # Проверка, что BeautifulSoup был вызван с правильным ответом
    mock_beautifulsoup.assert_called_once_with(mock_response.text, 'html.parser')

    # Проверка, что результат был распознан правильно
    mock_soup.find.assert_called_once_with("div", class_="result-container")


# Тестирование ошибки при запросе
@patch('src.assistant.Translating.speak')
@patch('src.assistant.Translating.requests.get')
def test_translate_request_error(mock_requests, mock_speak):
    """Тестируем ошибку запроса (например, 404)."""

    # Мокируем ошибочный ответ от запроса
    mock_response = mock_requests.return_value
    mock_response.status_code = 404

    # Запускаем функцию
    with patch('builtins.input', side_effect=["en", "es", "Hello"]):
        translate()

    # Проверка, что speak был вызван с сообщением об ошибке
    mock_speak.assert_any_call("Ошибка при запросе. Код ответа: 404")


# Тестирование ошибки при парсинге
@patch('src.assistant.Translating.speak')
@patch('src.assistant.Translating.requests.get')
@patch('src.assistant.Translating.BeautifulSoup')
def test_translate_parsing_error(mock_beautifulsoup, mock_requests, mock_speak):
    """Тестируем ошибку парсинга (например, не найден элемент)."""

    # Мокируем успешный запрос
    mock_response = mock_requests.return_value
    mock_response.status_code = 200
    mock_response.text = "<html><div class='result-container'>Hello</div></html>"

    # Мокируем, что парсинг не нашел перевода
    mock_soup = mock_beautifulsoup.return_value
    mock_soup.find.return_value = None

    # Запускаем функцию
    with patch('builtins.input', side_effect=["en", "es", "Hello"]):
        translate()

    # Проверка, что speak был вызван с сообщением о том, что перевод не найден
    mock_speak.assert_any_call("Перевод не найден")


# Тестирование исключения при запросе
@patch('src.assistant.Translating.speak')
@patch('src.assistant.Translating.requests.get')
def test_translate_exception(mock_requests, mock_speak):
    """Тестируем исключение при выполнении запроса (например, ошибки сети)."""

    # Мокируем, чтобы запрос выбросил исключение
    mock_requests.side_effect = Exception("Network Error")

    # Запускаем функцию
    with patch('builtins.input', side_effect=["en", "es", "Hello"]):
        translate()

    # Проверка, что speak был вызван с сообщением об ошибке
    mock_speak.assert_any_call("Ошибка при выполнении запроса: Network Error")
