import wikipedia


def searchInWikipedia(query):
    """Функция для поиска информации в Википедии и вывода результата в консоль."""
    try:
        # Устанавливаем язык поиска
        wikipedia.set_lang("ru")  # Для поиска на русском языке

        # Ищем статью в Википедии
        result = wikipedia.summary(query, sentences=3)  # Получаем краткое описание (первые 3 предложения)

        # Выводим результат в консоль
        print(f"Результат поиска по запросу '{query}':")
        print(result)
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Найдено несколько вариантов для запроса '{query}'. Вот возможные варианты:")
        print(e.options)
    except wikipedia.exceptions.HTTPTimeoutError:
        print("Ошибка сети при поиске в Википедии.")

    except wikipedia.exceptions.RedirectError:
        print("Ошибка: запрос перенаправлен на другую статью.")

    except Exception as e:
        print(f"Ошибка при поиске: {e}")
