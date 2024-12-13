import requests
from bs4 import BeautifulSoup

from SpeechUtils import speak


def translate():
    """
    Переводит текст с помощью парсинга страницы Google Translate.

    Функция запрашивает у пользователя код исходного и целевого языков, а также текст для перевода.
    Затем она отправляет запрос к мобильной версии Google Translate и извлекает переведенный текст с помощью BeautifulSoup.
    Результат выводится на консоль и озвучивается.

    Процесс:
    1. Запрашиваются исходный и целевой языки в формате ISO (например, 'en' для английского, 'ru' для русского).
    2. Запрашивается текст для перевода.
    3. Отправляется HTTP-запрос к мобильной версии Google Translate.
    4. С помощью BeautifulSoup парсится HTML-страница и извлекается переведенный текст.
    5. Перевод выводится на консоль и озвучивается с помощью функции `speak`.

    Обрабатывает возможные ошибки, связанные с запросом и парсингом.

    Пример использования:
        translate()  # Вызов функции для перевода текста с озвучиванием.

    Обрабатываемые исключения:
        - Exception: В случае ошибок в запросе или парсинге.
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
