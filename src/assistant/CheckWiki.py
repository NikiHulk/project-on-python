import wikipedia

def searchInWikipedia(query):
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
