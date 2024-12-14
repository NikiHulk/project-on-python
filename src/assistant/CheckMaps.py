from geopy.geocoders import Nominatim


# Перемещаем getCoordinates сюда для мока
def getCoordinates(address):
    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.geocode(address)
    if location:
        return location.latitude, location.longitude
    else:
        raise ValueError(f"Не удалось найти координаты для адреса: {address}")


def getRouteBetweenAddresses(startAddress, endAddress):
    # Функция для получения маршрута с использованием OSRM
    def getRouteOSRM(startCoords, endCoords):
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
