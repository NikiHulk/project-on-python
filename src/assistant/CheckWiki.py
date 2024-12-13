import wikipedia

def searchInWikipedia(query):
    """
    Ищет информацию в Википедии по заданному запросу и выводит результат.

    Этот метод использует библиотеку Wikipedia для получения сводки статьи по запросу и выводит её в консоль.

    Аргументы:
        query (str): Запрос для поиска в Википедии.

    Возвращает:
        None. Функция выводит результат поиска в консоль.

    Исключения:
        wikipedia.exceptions.DisambiguationError: Если запрос ведет к нескольким вариантам, функция выводит возможные варианты.
        wikipedia.exceptions.HTTPTimeoutError: При ошибке сети или тайм-ауте при запросе.
        wikipedia.exceptions.RedirectError: Если запрос перенаправляется на другую статью.
        Exception: Обработка всех остальных ошибок.

    Примечания:
        Функция использует библиотеку wikipedia. Необходимо установить её: pip install wikipedia
    """

    try:
        # Пытаемся получить сводку статьи
        summary = wikipedia.summary(query)
        print(f"Результат поиска по запросу '{query}':\n{summary}")
    except wikipedia.exceptions.DisambiguationError as e:
        # Обработка ошибки неоднозначности
        print(f"Найдено несколько вариантов для запроса '{query}'. Вот возможные варианты:")
        print(e.options)
    except wikipedia.exceptions.HTTPTimeoutError as e:
        # Обработка ошибки тайм-аута
        print(f"Ошибка сети при поиске в Википедии: {str(e)}")
    except wikipedia.exceptions.RedirectError as e:
        # Обработка ошибки перенаправления
        print(f"Ошибка: запрос перенаправлен на другую статью: {str(e)}")
    except Exception as e:
        # Обработка всех остальных ошибок
        print(f"Ошибка при поиске: {str(e)}")
