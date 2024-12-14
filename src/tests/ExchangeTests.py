from unittest.mock import patch
from src import exchangeRate


# Мокируем requests.get, чтобы не делать реальный HTTP-запрос
@patch('src.assistant.Exchange.requests.get')
# Мокируем функцию speak, чтобы не озвучивать результат
@patch('src.assistant.Exchange.speak')
def test_exchange_rate(mock_speak, mock_get):
    # Мокируем ответ от Google Finance
    mock_get.return_value.text = '''
    <html>
        <span class="DFlfde SwHCTb">76.00</span>
    </html>
    '''
    # Вводим валюту для теста
    currency = "USD"

    # Вызов функции
    exchangeRate(currency)

    # Проверяем, что запрос был сделан с правильным URL
    mock_get.assert_called_once_with('https://www.google.com/search?q=курсы+рубля+к+USD',
                                     headers={
                                         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 YaBrowser/24.10.0.0 Safari/537.36'})

    # Проверяем, что функция speak была вызвана с правильным сообщением
    mock_speak.assert_called_once_with('Один Российский рубль равен 76.00 USD')


def test_exchange_rate_no_span():
    # Мокируем ошибку, когда на странице не найден span с курсом
    with patch('src.assistant.Exchange.requests.get') as mock_get, \
            patch('src.assistant.Exchange.speak') as mock_speak:
        mock_get.return_value.text = '''
        <html>
            <span class="DFlfde SwHCTb">Not Found</span>
        </html>
        '''

        # Вводим валюту для теста
        currency = "EUR"

        # Вызов функции
        exchangeRate(currency)

        # Проверяем, что функция speak была вызвана с ошибкой
        mock_speak.assert_called_once_with(
            'Не удалось получить курс для валюты EUR. Возможно, ошибка в запросе или валюта не поддерживается.')
