import wikipedia

def searchInWikipedia(query):

    """
    Выполняет поиск в Википедии по указанному запросу и выводит сводку статьи.

    Функция отправляет запрос в Википедию и пытается получить краткое описание статьи по указанному запросу.
    Если запрос приводит к неоднозначным результатам, функция выведет список возможных вариантов.
    Также обрабатываются ошибки, такие как тайм-ауты, перенаправления и другие.

    Аргументы:
        query (str): Текстовый запрос для поиска статьи в Википедии.

    Исключения:
        wikipedia.exceptions.DisambiguationError: Если запрос ведет к нескольким возможным статьям.
        wikipedia.exceptions.HTTPTimeoutError: Если происходит ошибка сети при поиске.
        wikipedia.exceptions.RedirectError: Если запрос приводит к перенаправлению на другую статью.
        Exception: Для обработки других непредвиденных ошибок.

    Пример:
        searchInWikipedia("Python")
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
