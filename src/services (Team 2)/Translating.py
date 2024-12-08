import requests
from bs4 import BeautifulSoup


def translate():
    """Функция для перевода текста с помощью парсинга Google Translate."""

    # Запрос исходного языка
    source_lang = input(
        "Введите код языка исходного текста (например, 'en' для английского, 'ru' для русского): ").strip()

    # Запрос целевого языка
    target_lang = input("Введите код целевого языка (например, 'en' для английского, 'ru' для русского): ").strip()

    # Запрос текста для перевода
    text_to_translate = input("Введите текст для перевода: ").strip()

    # Формирование URL для мобильной версии Google Translate
    url = f"https://translate.google.com/m?sl={source_lang}&tl={target_lang}&q={text_to_translate}"

    # Отправка запроса
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)

        # Проверка успешности запроса
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Поиск переведенного текста
            translation = soup.find("div", class_="result-container")
            if translation:
                print(f"\nПеревод: {translation.text}")
            else:
                print("Перевод не найден")
        else:
            print("Ошибка при запросе. Код ответа:", response.status_code)

    except Exception as e:
        print(f"Ошибка при выполнении запроса: {e}")

# Пример вызова функции:
# translate()
