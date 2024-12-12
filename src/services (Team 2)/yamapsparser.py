import time
import requests
import json

def GetRouteInfo(api_key, point_a, point_b):
    base_url = "https://api.maps.yandex.ru/1.x/"
    params = {
        "apikey": api_key,
        "rll": f"{point_a},{point_b}",
        "lang": "ru_RU",
        "results": 1,
        "format": "json",
    }

    try:
        response = requests.get(base_url, params=params, timeout=10) # добавлено timeout
        response.raise_for_status()
        data = response.json()

        route = data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        distance = route["properties"]["length"]
        duration = route["properties"]["time"]
        link = route["properties"]["text"]

        return {
            "distance": distance,
            "duration": duration,
            "link": link,
        }

    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")
        return None
    except (KeyError, IndexError) as e:
        print(f"Ошибка обработки ответа API: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Ошибка декодирования JSON: {e}")
        return None
if __name__ == "__main__":
    api_key = "....."  #Ваш API ключ
    point_a = input("Введите координаты точки А (широта,долгота): ")
    point_b = input("Введите координаты точки Б (широта,долгота): ")
    route_info = GetRouteInfo(api_key, point_a, point_b)

    if route_info:
        print("Информация о маршруте:")
        print(f"  Расстояние: {route_info['distance']} м")
        print(f"  Время: {route_info['duration']} сек")
        print(f"  Ссылка: {route_info['link']}")

#Нужно решить проблему с максимумом запросов API ключа