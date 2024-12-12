import requests
from geopy.geocoders import Nominatim


def getRouteBetweenAddresses(startAddress, endAddress):
    # Функция для получения координат по адресу
    def getCoordinates(address):
        geolocator = Nominatim(user_agent="myGeocoder")
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
        else:
            raise ValueError(f"Не удалось найти координаты для адреса: {address}")

    # Функция для получения маршрута с использованием OSRM
    def getRouteOSRM(startCoords, endCoords):
        osrmUrl = f"http://router.project-osrm.org/route/v1/driving/{startCoords[1]},{startCoords[0]};{endCoords[1]},{endCoords[0]}?overview=full&steps=true"
        response = requests.get(osrmUrl)
        if response.status_code == 200:
            data = response.json()
            try:
                routeInfo = {
                    "distance": round(data["routes"][0]["legs"][0]["distance"] / 1000, 1),  # Расстояние в километрах, округленное до десятых
                    "duration": round(data["routes"][0]["legs"][0]["duration"] / 60, 1),  # Время в пути в минутах, округленное до десятых
                }
                return routeInfo
            except (IndexError, KeyError) as e:
                raise ValueError(f"Ошибка в обработке данных маршрута: {e}")
        else:
            raise ValueError(f"Ошибка при запросе маршрута: {response.status_code} - {response.text}")

    try:
        # Получаем координаты для обеих точек
        startCoords = getCoordinates(startAddress)
        endCoords = getCoordinates(endAddress)

        # Получаем маршрут
        route = getRouteOSRM(startCoords, endCoords)

        # Приводим результат в читаемый вид
        print("————————————————————————————————————————————————————————————————")
        print(f"Маршрут между '{startAddress}' и '{endAddress}'")
        print("————————————————————————————————————————————————————————————————")
        print(f"Расстояние: {route['distance']} километров")
        print(f"Время в пути: {route['duration']} минут")
        print("————————————————————————————————————————————————————————————————")

    except Exception as e:
        print(f"Ошибка: {e}")


# Пример использования
#startAddress = "Москва, Красная площадь"
#endAddress = "Москва, Ленинградский вокзал"
#getRouteBetweenAddresses(startAddress, endAddress)
