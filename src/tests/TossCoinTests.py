from unittest.mock import patch
from TossCoin import TossCoin  # Убедитесь, что путь к классу правильный


@patch('SpeechUtils.speak')  # Патчим SpeechUtils.speak
@patch('random.choice')  # Патчим random.choice
def test_tossCoin_oriel(mock_random_choice, mock_speak):
    """Тестируем метод tossCoin для случая, когда выпал 'орел'."""

    # Настроим mock random.choice так, чтобы он всегда возвращал 'орел'
    mock_random_choice.return_value = "орел"

    # Создаем объект класса TossCoin
    coin_tosser = TossCoin()

    # Подбрасываем монету 1 раз
    coin_tosser.tossCoin(1)

    # Проверяем, что random.choice был вызван с аргументом ["орел", "решка"]
    mock_random_choice.assert_called_once_with(["орел", "решка"])

    # Проверяем, что speak был вызван с правильным сообщением
    mock_speak.assert_called_once_with("Монета подброшена, вам выпал орел")
