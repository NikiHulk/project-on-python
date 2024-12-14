from unittest.mock import patch
from src import getRouteBetweenAddresses


def test_getRouteBetweenAddresses():
    # Мокаем запрос к OSRM, чтобы получить заранее предсказуемые данные
    with patch('requests.get') as mock_get:
        mock_response = {
            "routes": [
                {
                    "legs": [
                        {
                            "distance": 10000,  # 10 км
                            "duration": 600  # 10 минут
                        }
                    ]
                }
            ]
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        # Мокаем функцию getCoordinates, чтобы она возвращала предсказуемые координаты
        with patch('assistant.CheckMaps.getCoordinates', return_value=(55.7558, 37.6176)) as mock_getCoordinates:
            # Запускаем функцию
            result = getRouteBetweenAddresses('Москва, Красная площадь', 'Москва, Ленинградский вокзал')

            # Проверяем, что результат правильный
            assert result['distance'] == 10.0
            assert result['duration'] == 10.0
