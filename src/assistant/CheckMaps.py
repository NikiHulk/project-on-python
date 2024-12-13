from geopy.geocoders import Nominatim


def getCoordinates(address):
    """
    Получает координаты (широту и долготу) по заданному адресу.

    Этот метод использует библиотеку geopy для получения координат (широты и долготы)
    на основе введенного адреса с использованием сервиса Nominatim.

    Аргументы:
        address (str): Адрес для поиска координат.

    Возвращает:
        tuple: Кортеж из двух чисел (latitude, longitude) — широта и долгота.

    Исключения:
        ValueError: Если не удалось найти координаты по заданному адресу.
    """
    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.geocode(address)
    if location:
        return location.latitude, location.longitude
    else:
        raise ValueError(f"Не удалось найти координаты для адреса: {address}")


def getRouteBetweenAddresses(startAddress, endAddress):
    """
    Получает информацию о маршруте между двумя адресами с использованием OSRM.

    Этот метод получает координаты начального и конечного адресов, затем делает запрос к
    OSRM для получения информации о маршруте между ними, включая расстояние и время в пути.

    Аргументы:
        startAddress (str): Начальный адрес.
        endAddress (str): Конечный адрес.

    Возвращает:
        dict: Словарь с информацией о маршруте:
              - distance (float): Расстояние в километрах.
              - duration (float): Время в пути в минутах.

    Исключения:
        ValueError: При возникновении ошибок при получении координат, запросе к OSRM или обработке ответа.
        Exception: При любых других непредвиденных ошибках.
    """

    def getRouteOSRM(startCoords, endCoords):
        """
        Вспомогательная функция для получения данных о маршруте от OSRM.

        Этот метод делает запрос к серверу OSRM для получения информации о маршруте между двумя точками
        с заданными координатами и возвращает расстояние и время в пути.

        Аргументы:
            startCoords (tuple): Координаты начальной точки (latitude, longitude).
            endCoords (tuple): Координаты конечной точки (latitude, longitude).

        Возвращает:
            dict: Словарь с информацией о маршруте (distance, duration).

        Исключения:
            ValueError: При ошибках в запросе к OSRM или обработке ответа.
        """
        import requests

        osrmUrl = f"http://router.project-osrm.org/route/v1/driving/{startCoords[1]},{startCoords[0]};{endCoords[1]},{endCoords[0]}?overview=full&steps=true"
        response = requests.get(osrmUrl)
        if response.status_code == 200:
            data = response.json()
            try:
                routeInfo = {
                    "distance": round(data["routes"][0]["legs"][0]["distance"] / 1000, 1),
                    "duration": round(data["routes"][0]["legs"][0]["duration"] / 60, 1),
                }
                return routeInfo
            except (IndexError, KeyError) as e:
                raise ValueError(f"Ошибка в обработке данных маршрута: {e}")
        else:
            raise ValueError(f"Ошибка при запросе маршрута: {response.status_code} - {response.text}")

    try:
        startCoords = getCoordinates(startAddress)
        endCoords = getCoordinates(endAddress)

        # Получаем маршрут
        route = getRouteOSRM(startCoords, endCoords)

        # Приводим результат в читаемый вид
        print(f"Маршрут между '{startAddress}' и '{endAddress}':")
        print(f"Расстояние: {route['distance']} км")
        print(f"Время в пути: {route['duration']} мин")

        return route

    except Exception as e:
        print(f"Ошибка: {e}")
