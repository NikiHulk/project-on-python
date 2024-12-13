import unittest
from unittest.mock import patch
import webbrowser

# Импортируем только те функции, которые есть в файле
from assistant.PageOpener import openVkontakte, openVkVideo, openKinopoisk, openIvi, openRutube, openYouTube, openTelegram, openYandexMaps


class TestWebFunctions(unittest.TestCase):

    @patch('webbrowser.open')
    def test_open_vkontakte(self, mock_open):
        openVkontakte()
        mock_open.assert_called_once_with("https://vk.com")

    @patch('webbrowser.open')
    def test_open_vk_video(self, mock_open):
        openVkVideo()
        mock_open.assert_called_once_with("https://vk.com/video")

    @patch('webbrowser.open')
    def test_open_kinopoisk(self, mock_open):
        openKinopoisk()
        mock_open.assert_called_once_with("https://www.kinopoisk.ru")

    @patch('webbrowser.open')
    def test_open_ivi(self, mock_open):
        openIvi()
        mock_open.assert_called_once_with("https://www.ivi.ru")

    @patch('webbrowser.open')
    def test_open_rutube(self, mock_open):
        openRutube()
        mock_open.assert_called_once_with("https://rutube.ru")

    @patch('webbrowser.open')
    def test_open_youtube(self, mock_open):
        openYouTube()
        mock_open.assert_called_once_with("https://www.youtube.com")

    @patch('webbrowser.open')
    def test_open_telegram(self, mock_open):
        openTelegram()
        mock_open.assert_called_once_with("https://web.telegram.org")

    @patch('webbrowser.open')
    def test_open_yandex_maps(self, mock_open):
        openYandexMaps()
        mock_open.assert_called_once_with("https://yandex.ru/maps/")

if __name__ == '__main__':
    unittest.main()
