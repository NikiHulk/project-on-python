from unittest.mock import patch
import wikipedia
from src.assistant.CheckWiki import searchInWikipedia  # Замените на правильный путь


def test_searchInWikipedia():
    query = "Python"

    with patch('wikipedia.summary') as mock_summary:
        mock_summary.return_value = "Python is a programming language."

        with patch('builtins.print') as mock_print:
            searchInWikipedia(query)
            mock_print.assert_any_call("Результат поиска по запросу 'Python':\nPython is a programming language.")


def test_searchInWikipedia_with_disambiguation():
    query = "Python"

    with patch('wikipedia.summary') as mock_summary:
        mock_summary.side_effect = wikipedia.exceptions.DisambiguationError(
            ["Python (язык программирования)", "Python (модуль)"], "Python"
        )

        with patch('builtins.print') as mock_print:
            searchInWikipedia(query)
            mock_print.assert_any_call(f"Найдено несколько вариантов для запроса '{query}'. Вот возможные варианты:")
            mock_print.assert_any_call("Python")


def test_searchInWikipedia_with_http_timeout_error():
    query = "Python (язык программирования)"

    with patch('wikipedia.summary') as mock_summary:
        mock_summary.side_effect = wikipedia.exceptions.HTTPTimeoutError("Timeout Error")

        with patch('builtins.print') as mock_print:
            searchInWikipedia(query)
            mock_print.assert_any_call(
                'Ошибка сети при поиске в Википедии: Searching for "Timeout Error" resulted in a timeout. Try again in a few seconds, and make sure you have rate limiting set to True.'
            )


def test_searchInWikipedia_with_redirect_error():
    query = "Python (язык программирования)"

    with patch('wikipedia.summary') as mock_summary:
        mock_summary.side_effect = wikipedia.exceptions.RedirectError("Redirect Error")

        with patch('builtins.print') as mock_print:
            searchInWikipedia(query)
            mock_print.assert_any_call(
                'Ошибка: запрос перенаправлен на другую статью: "Redirect Error" resulted in a redirect. Set the redirect property to True to allow automatic redirects.'
            )


def test_searchInWikipedia_with_generic_exception():
    query = "Python"

    with patch('wikipedia.summary') as mock_summary:
        mock_summary.side_effect = Exception("Generic Error")

        with patch('builtins.print') as mock_print:
            searchInWikipedia(query)
            mock_print.assert_any_call("Ошибка при поиске: Generic Error")
