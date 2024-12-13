import pytest
from unittest.mock import patch
from Apologies import Apologies


# Тестирование метода playApologies
def test_playApologies():
    # Мокаем random.choice, чтобы он всегда возвращал определенную фразу
    with patch('random.choice', return_value="Извините, я не хотела вас обидеть. Хотя, возможно, я этого и хотела, но потом передумала"):
        # Мокаем функцию speak в контексте, где она вызывается (внутри Apologies)
        with patch('Apologies.speak') as mock_speak:
            apologies = Apologies()
            apologies.playApologies()

            # Проверяем, что функция speak была вызвана с правильной фразой
            mock_speak.assert_called_once_with("Извините, я не хотела вас обидеть. Хотя, возможно, я этого и хотела, но потом передумала")

            # Проверяем, что фраза была выведена
            with patch('builtins.print') as mock_print:
                apologies.playApologies()
                mock_print.assert_called_once_with("Извините, я не хотела вас обидеть. Хотя, возможно, я этого и хотела, но потом передумала")
