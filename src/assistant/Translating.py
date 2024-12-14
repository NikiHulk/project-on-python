import requests
from bs4 import BeautifulSoup

from SpeechUtils import speak


def translate():

    """
    Функция для перевода текста с помощью парсинга Google Translate.

    Описание:
    Эта функция запрашивает у пользователя исходный и целевой языки, а также текст для перевода. Затем выполняется
    HTTP-запрос к мобильной версии Google Translate, где текст переводится. Результат перевода выводится на экран
    и озвучивается с помощью функции speak.

    Шаги работы:
    1. Получение исходного языка.
    2. Получение целевого языка.
    3. Получение текста для перевода.
    4. Формирование URL для запроса в Google Translate.
    5. Отправка запроса на сервер и извлечение переведенного текста из HTML-ответа.
    6. Озвучивание и вывод перевода.

    Исключения:
    - Обрабатывает ошибки запроса, такие как сбой соединения или недоступность Google Translate.
    - Проверяется успешность выполнения запроса (код состояния 200).

    Аргументы:
    Нет.

    Возвращает:
    None.
    """

    # Запрос исходного языка
    speak("Введите код языка исходного текста (например, 'en' для английского, 'ru' для русского)")
    source_lang = input(
        "Введите код языка исходного текста (например, 'en' для английского, 'ru' для русского): ").strip()

    # Запрос целевого языка
    speak("Введите код целевого языка (например, 'en' для английского, 'ru' для русского)")
    target_lang = input("Введите код целевого языка (например, 'en' для английского, 'ru' для русского): ").strip()

    # Запрос текста для перевода
    speak("Введите текст перевода")
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
                speak(f"Зачитываю перевод вашего текста, {translation.text}")
            else:
                print("Перевод не найден")
                speak("Перевод не найден")
        else:
            print("Ошибка при запросе. Код ответа:", response.status_code)
            speak(f"Ошибка при запросе. Код ответа: {response.status_code}")

    except Exception as e:
        print(f"Ошибка при выполнении запроса: {e}")
        speak(f"Ошибка при выполнении запроса: {e}")

# Пример вызова функции:
# translate()
